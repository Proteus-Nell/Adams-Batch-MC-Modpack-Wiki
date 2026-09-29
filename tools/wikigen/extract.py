"""Extract wiki data from the pack's mod jars.

    python -m wikigen.extract --mods <pack>/mods --work .work --data ../data --icons ../docs/assets/icons

Steps: unzip each jar, decompile it with Vineflower (downloaded from Maven
Central on first use), index the Java sources, then write one JSON file per
documented mod into --data. Rendering pages from that JSON is a separate step
(wikigen.render), so templates can change without needing the jars again.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tomllib
import urllib.request
import zipfile
from collections import defaultdict

from . import abilities as ab
from . import codeinfo, configs, content, relics
from .icons import IconRenderer
from .javaindex import JavaIndex, InstanceOf, text, walk
from .mods import MODS, SUPPORT_JARS
from .registry import find_registrations
from .linker import LiteralLinker
from .gear import GearReader, armor_stats
from .resources import Resources, clean, load_json

VINEFLOWER = "https://repo1.maven.org/maven2/org/vineflower/vineflower/1.12.0/vineflower-1.12.0.jar"


# ---------------------------------------------------------------- jar prep
def find_jar(mods_dir, prefix):
    for fn in sorted(os.listdir(mods_dir)):
        if fn.startswith(prefix) and fn.endswith(".jar"):
            return fn
    return None


def prepare(mods_dir, work):
    os.makedirs(work, exist_ok=True)
    x = os.path.join(work, "x")
    src = os.path.join(work, "src")
    vf = os.path.join(work, "vineflower.jar")
    keys = {}
    for m in MODS:
        fn = find_jar(mods_dir, m["jar"])
        if fn:
            keys[m["slug"]] = fn[:-4]
        else:
            print("!! jar not found for", m["name"])
    support = []
    for p in SUPPORT_JARS:
        fn = find_jar(mods_dir, p)
        if fn:
            support.append(fn[:-4])
    for key in list(keys.values()) + support:
        jar = os.path.join(mods_dir, key + ".jar")
        xd = os.path.join(x, key)
        if not os.path.isdir(xd):
            print("unzip", key)
            with zipfile.ZipFile(jar) as z:
                z.extractall(xd)
            # ManasCore ships its modules as nested jars
            jj = os.path.join(xd, "META-INF", "jars")
            if os.path.isdir(jj):
                for inner in os.listdir(jj):
                    if inner.endswith(".jar"):
                        with zipfile.ZipFile(os.path.join(jj, inner)) as z:
                            z.extractall(xd)
        sd = os.path.join(src, key)
        if not os.path.isdir(sd):
            if not os.path.isfile(vf):
                print("downloading Vineflower")
                urllib.request.urlretrieve(VINEFLOWER, vf)
            print("decompile", key)
            os.makedirs(sd, exist_ok=True)
            inputs = [jar]
            jj = os.path.join(xd, "META-INF", "jars")
            if os.path.isdir(jj):
                inputs = [os.path.join(jj, f) for f in os.listdir(jj) if f.endswith(".jar")] + [jar]
            for inp in inputs:
                subprocess.run(["java", "-Xmx3g", "-jar", vf, "-dgs=1", "-log=ERROR", inp, sd],
                               check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return x, src, keys, support


def mod_meta(xdir, key, modid):
    p = os.path.join(xdir, key, "META-INF", "neoforge.mods.toml")
    meta = {}
    try:
        with open(p, "rb") as fh:
            raw = fh.read().decode("utf-8", "replace")
        try:
            d = tomllib.loads(raw)
        except Exception:
            d = {}
        for m in d.get("mods", []):
            if m.get("modId") == modid:
                meta = {k: m.get(k) for k in ("displayName", "version", "authors", "credits", "description", "displayURL", "issueTrackerURL", "logoFile")}
        meta["license"] = d.get("license")
        deps = []
        for dk, dl in (d.get("dependencies") or {}).items():
            if dk != modid:
                continue
            for dep in dl:
                if dep.get("modId") in ("minecraft", "neoforge"):
                    continue
                deps.append({"modid": dep.get("modId"), "type": dep.get("type") or ("required" if dep.get("mandatory") else "optional"), "version": dep.get("versionRange")})
        meta["depends"] = deps
    except FileNotFoundError:
        pass
    if meta.get("version", "").startswith("${"):
        meta["version"] = None
    if meta.get("description"):
        meta["description"] = clean(meta["description"])
    return meta


# ------------------------------------------------------------------ main
def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--mods", required=True, help="folder containing the pack's mod jars")
    ap.add_argument("--work", default=".work", help="scratch folder for unzipped/decompiled jars")
    ap.add_argument("--data", default="data", help="output folder for JSON")
    ap.add_argument("--icons", default="docs/assets/icons", help="output folder for icons")
    ap.add_argument("--only", nargs="*", help="limit to these mod slugs")
    a = ap.parse_args(argv)

    xdir, srcdir, keys, support = prepare(a.mods, a.work)
    jar_keys = list(keys.values()) + support
    version_of = {}
    for fn in os.listdir(a.mods):
        if fn.endswith(".jar"):
            version_of[fn[:-4]] = fn
    print("indexing sources")
    ix = JavaIndex()
    for k in jar_keys:
        ix.add_tree(os.path.join(srcdir, k), k)
    print("  %d classes" % len(ix.classes))
    res = Resources(xdir, jar_keys)
    icons = IconRenderer(res, a.icons, "assets/icons")

    # ---- registrations for every jar, with namespaces
    modid_of_key = {}
    for m in MODS:
        if m["slug"] in keys:
            modid_of_key[keys[m["slug"]]] = m["modids"][0]
    for k in support:
        modid_of_key[k] = {"manascore": "manascore"}.get(k.split("-")[0], k.split("-")[0].split("_neoforge")[0].lower())
    regs_by_key = {}
    all_regs = []
    for k in jar_keys:
        ns = modid_of_key.get(k, "")
        if k.startswith("tensura_neb"):
            ns = "tensura_neb"
        rs = find_registrations(ix, {k}, ns)
        regs_by_key[k] = rs
        all_regs += rs

    def kind_of(r):
        c = ix.classes.get(r.cls) if r.cls else None
        via = r.via.upper()
        if "EntityType<" in (r.decl_type or "") or "MobCategory." in text(r.node):
            return "entity"
        if c is not None:
            if ix.is_a(c, "ManasSkill"):
                return "skill"
            if ix.is_a(c, "ManasRace"):
                return "race"
            anc = [x.rsplit(".", 1)[-1] for x in ix.ancestors(c)] + [c.simple]
            if "MobEffect" in anc:
                return "effect"
            if any(x in anc for x in ("Block", "BaseEntityBlock")) and "Item" not in anc:
                return "block"
            if any(x.endswith("Item") or x == "Item" for x in anc):
                return "item"
            if "Entity" in anc or "LivingEntity" in anc or "Mob" in anc or "Projectile" in anc:
                return "entity"
        if "ENTIT" in via:
            return "entity"
        if "EFFECT" in via:
            return "effect"
        if "BLOCK" in via and "ENTIT" not in via:
            return "block"
        if "ITEM" in via:
            return "item"
        return None

    known = {}
    for r in all_regs:
        k = kind_of(r)
        if k:
            known.setdefault(r.full_id, k)
    rr = ab.RefResolver(ix, all_regs, known)

    # ---- configs
    print("configs")
    options = []
    for m in MODS:
        if m["slug"] not in keys:
            continue
        k = keys[m["slug"]]
        mo = configs.manas_configs(ix, {k}) + configs.artifacts_configs(ix, {k})
        so = configs.spec_configs(ix, {k})
        regs = configs.spec_registrations(ix, {k}, m["modids"][0])
        for o in mo:
            o["mod"] = m["slug"]
        for o in so:
            o["mod"] = m["slug"]
            owner = o.get("entry") or o.get("owner") or ""
            f = None
            parts = owner.split(".")
            for i in range(len(parts), 0, -1):
                cand = ".".join(parts[:i])
                if cand in regs:
                    f = regs[cand][0]["file"]
                    break
            if f is None:
                allr = [x for v in regs.values() for x in v]
                if m.get("default_config_file"):
                    f = m["default_config_file"]
                elif len(allr) == 1:
                    f = allr[0]["file"]
                else:
                    f = "config/%s-common.toml" % m["modids"][0]
            o["file"] = f
            if o.get("field") and o.get("key") is not None:
                ix.config_defaults[o["field"]] = o.get("default")
        options += mo + so
    for i, o in enumerate(options):
        o["oid"] = i
    opt_by_owner = defaultdict(list)
    opt_by_field = {}
    for o in options:
        if o.get("key") is None:
            continue
        opt_by_owner[o.get("owner")].append(o["oid"])
        if o.get("field"):
            opt_by_field[o["field"]] = o["oid"]

    def config_links(cls):
        out = []
        chain = []
        c = cls
        while c is not None and c.simple not in ab.BASE_SKILL_CLASSES and len(chain) < 8 and c.simple not in ("TensuraRace", "DefaultRace", "ManasRace"):
            chain.append(c)
            c = ix.resolve(c.superclass, c) if c.superclass else None
        seen_owner = set()
        for c in chain:
            for n in walk(c.node):
                t = n.type
                if t in ("type_identifier", "scoped_type_identifier"):
                    rc = ix.resolve(text(n), c)
                    if rc is not None and rc.fqcn in opt_by_owner and rc.fqcn not in seen_owner and ix.is_a(rc, "ManasSubConfig"):
                        seen_owner.add(rc.fqcn)
                        out += opt_by_owner[rc.fqcn]
                elif t == "field_access":
                    try:
                        v = ix.eval(n, c)
                    except Exception:
                        v = None
                    if isinstance(v, InstanceOf) and v.fqcn in opt_by_owner and v.fqcn not in seen_owner:
                        seen_owner.add(v.fqcn)
                        out += opt_by_owner[v.fqcn]
                    key = ix._field_key(n, c)
                    if key in opt_by_field and opt_by_field[key] not in out:
                        out.append(opt_by_field[key])
                elif t == "identifier" and n.parent is not None and n.parent.type not in ("field_access", "method_invocation", "variable_declarator"):
                    f = ix.find_field(c, text(n))
                    if f is not None:
                        key = f.cls.fqcn + "." + f.name
                        if key in opt_by_field and opt_by_field[key] not in out:
                            out.append(opt_by_field[key])
        return out

    # ---- global data
    print("recipes, loot, tags")
    recipes = content.load_recipes(res)
    loot = content.load_loot(res)
    lmods = content.loot_modifiers(res)
    spawns = content.load_spawn_modifiers(res)
    tags = res.tags()
    skill_tags = defaultdict(list)
    for tid, vals in tags.get("manascore_skill", {}).items():
        for v in res.tag_members("manascore_skill", tid):
            skill_tags[v].append(tid)
    race_tags = defaultdict(list)
    for tid, vals in tags.get("manascore_race", {}).items():
        for v in res.tag_members("manascore_race", tid):
            race_tags[v].append(tid)
    names = content.Names(res)
    extractor = ab.AbilityExtractor(ix, res, rr, config_links)
    linker = LiteralLinker(ix)
    gear_reader = GearReader(ix)
    data_refs = set()
    for r in recipes:
        outs, ins = content.recipe_items(r)
        data_refs.update(i for i in outs + ins if isinstance(i, str))
    for t in loot.values():
        for p_ in t["pools"]:
            for it in p_["items"]:
                if it.get("item"):
                    data_refs.add(it["item"])
    for reg_name in ("item", "block"):
        for tid in tags.get(reg_name, {}):
            data_refs.update(res.tag_members(reg_name, tid))
    phantoms = defaultdict(list)

    os.makedirs(a.data, exist_ok=True)
    only = set(a.only or [])
    for m in MODS:
        if m["slug"] not in keys or (only and m["slug"] not in only):
            continue
        k = keys[m["slug"]]
        ns = m["modids"][0]
        print("==", m["name"])
        meta = mod_meta(xdir, k, ns)
        meta["jar"] = version_of.get(k)
        if meta.get("logoFile"):
            lp = os.path.join(xdir, k, meta["logoFile"])
            if os.path.isfile(lp):
                try:
                    from PIL import Image
                    im = Image.open(lp).convert("RGBA")
                    im.thumbnail((256, 256))
                    dest = os.path.join(a.icons, ns, "logo.png")
                    os.makedirs(os.path.dirname(dest), exist_ok=True)
                    im.save(dest, optimize=True)
                    meta["logo_url"] = "assets/icons/%s/logo.png" % ns
                except Exception:
                    pass
        out = {"mod": dict(m, **{"meta": meta}), "categories": {}}
        regs = regs_by_key[k]
        reg_by_id = {}
        for r in regs:
            reg_by_id.setdefault((r.ns, r.id, kind_of(r)), r)

        # ---- abilities & races
        if m["family"] == "tensura":
            sk, rc = [], []
            for r in regs:
                kd = kind_of(r)
                if kd == "skill":
                    rec = extractor.skill(r, r.ns or ns, skill_tags)
                    if rec.get("icon"):
                        p = rec["icon"].split(":", 1)
                        rec["icon_url"] = icons.texture(rec["icon"], os.path.join(p[0], "skill", r.id.replace("/", "_") + ".png"), 32)
                    sk.append(rec)
                elif kd == "race":
                    rc.append(extractor.race(r, r.ns or ns, race_tags))
            out["categories"]["abilities"] = sk
            out["categories"]["races"] = rc

        # ---- items
        items = []
        item_ids = set(content.lang_ids(res, k, "item", ns)) | set(content.lang_ids(res, k, ns, "item"))
        model_ids = set(content.asset_ids(res, k, ns, "models/item"))
        reg_items = {r.id: r for r in regs if kind_of(r) == "item" and r.ns in (ns, "")}
        block_ids = set(content.lang_ids(res, k, "block", ns)) | set(content.lang_ids(res, k, ns, "block"))
        alt_names = defaultdict(list)
        cls_to_item = {r.cls: r.id for r in reg_items.values() if r.cls}
        for iid in sorted((item_ids & (model_ids | set(reg_items))) | (set(reg_items) & model_ids)):
            if iid in block_ids:
                continue
            r = reg_items.get(iid)
            full = "%s:%s" % (ns, iid)
            cls_name = r.cls if r else None
            if r is None:
                if not linker.mentioned([k], iid):
                    # only ever used as a display name (EtheriumCore shows "Starlight Core" while active)?
                    owner = None
                    for lk in ("item.%s.%s" % (ns, iid), "%s.item.%s" % (ns, iid)):
                        owner = owner or linker.owner_of_literal([k], lk)
                    base = cls_to_item.get(owner.fqcn) if owner is not None else None
                    if base and base != iid:
                        alt_names[base].append({"id": full, "name": names.item(full), "class": owner.fqcn})
                        continue
                    if full not in data_refs:
                        phantoms[m["slug"]].append(full)
                        continue
                else:
                    cls_name = linker.link([k], iid, "item")
            cls = ix.classes.get(cls_name) if cls_name else None
            rec = {"id": full, "path": iid, "name": names.item(full), "class": cls_name}
            rec["category"] = codeinfo.item_category(ix, r, iid)
            if m["family"] == "enigmatic" and cls is not None:
                pk = cls.pkg.split(".")
                if "item" in pk and pk.index("item") + 1 < len(pk):
                    rec["category"] = pk[pk.index("item") + 1].replace("_", " ").title()
            rec["props"] = codeinfo.item_properties(ix, r) if r else {}
            if r is not None:
                try:
                    g = gear_reader.stats(r)
                except Exception:
                    g = {}
                if g:
                    rec["gear"] = g
                try:
                    arm = armor_stats(ix, r)
                except Exception:
                    arm = {}
                if arm:
                    rec["armor"] = arm
            tips = codeinfo.tooltip_lines(ix, cls, res.has, res.tr)
            for base in ("item.%s.%s" % (ns, iid), "%s.item.%s" % (ns, iid)):
                for suf, t in content.lang_extras(res, base):
                    if t and t not in tips:
                        tips.append(t)
            for pref in ("tooltip.%s.%s" % (ns, iid), "%s.tooltip.%s" % (ns, iid), "%s.tooltip.item.%s" % (ns, iid)):
                if res.has(pref):
                    t = res.tr(pref)
                    if t not in tips:
                        tips.append(t)
                for suf, t in content.lang_extras(res, pref):
                    if t and t not in tips and not suf.startswith("ability."):
                        tips.append(t)
            rec["tooltips"] = tips
            rec["tags"] = res.tags_of("item", full)
            if m["family"] in ("relics", "artifacts"):
                slots = [t.split("/", 1)[1] for t in rec["tags"] if t.startswith("artifacts:slot/")]
                slots += [t.split(":", 1)[1] for t in rec["tags"] if t.startswith("curios:") and t not in ("curios:curio",)]
                if slots:
                    rec["category"] = slots[0].replace("_", " ").title()
            rec["icon_url"] = icons.item(ns, iid)
            if cls is not None and m["family"] in ("relics", "artifacts") or (cls is not None and cls.method("constructDefaultRelicData")):
                rd = relics.parse_relic(ix, cls)
                if rd:
                    rec["relic"] = _relic_render(ix, res, cls, rd, ns, iid)
            items.append(rec)
        for rec in items:
            if alt_names.get(rec["path"]):
                rec["alt_names"] = alt_names[rec["path"]]
        out["categories"]["items"] = items

        # ---- blocks
        blocks = []
        reg_blocks = {r.id: r for r in regs if kind_of(r) == "block"}
        bs_ids = set(content.asset_ids(res, k, ns, "blockstates"))
        for bid in sorted(block_ids & (bs_ids | set(reg_blocks))):
            full = "%s:%s" % (ns, bid)
            r = reg_blocks.get(bid)
            bcls = r.cls if r else None
            if bcls is None and linker.mentioned([k], bid):
                bcls = linker.link([k], bid, "block")
            rec = {"id": full, "path": bid, "name": names.block(full), "class": bcls,
                   "tags": res.tags_of("block", full), "item_tags": res.tags_of("item", full),
                   "icon_url": icons.block(ns, bid)}
            tips = []
            for pref in ("block.%s.%s" % (ns, bid), "tooltip.%s.%s" % (ns, bid)):
                for suf, t in content.lang_extras(res, pref):
                    if t and t not in tips:
                        tips.append(t)
            rec["tooltips"] = tips
            drops = loot.get("%s:blocks/%s" % (ns, bid))
            rec["drops"] = drops["pools"] if drops else None
            blocks.append(rec)
        out["categories"]["blocks"] = blocks

        # ---- entities
        ents = []
        ent_ids = set(content.lang_ids(res, k, "entity", ns))
        reg_ents = {r.id: r for r in regs if kind_of(r) == "entity"}
        existence = {}
        for kk in jar_keys:
            existence.update(content.load_simple_dir(res, kk, "entity_existence"))
        for eid in sorted(ent_ids | {i for i, r in reg_ents.items() if "%s:%s" % (ns, i) in known}):
            full = "%s:%s" % (ns, eid)
            r = reg_ents.get(eid)
            info = codeinfo.entity_type_info(ix, r) if r else {}
            if r is None:
                if not linker.mentioned([k], eid):
                    phantoms[m["slug"]].append(full)
                    continue
                ecls = linker.link([k], eid, "entity")
                if ecls:
                    info = codeinfo.entity_class_info(ix, ix.classes.get(ecls))
                    if not info.get("living"):
                        continue
            if r is not None and not info.get("living") and not res.has("entity.%s.%s" % (ns, eid)):
                continue
            if r is not None and not info.get("living"):
                continue
            rec = {"id": full, "path": eid, "name": names.entity(full), "info": info}
            ex = existence.get(full)
            if ex:
                rec["existence"] = {"min_magicule": ex.get("min_magicule"), "max_magicule": ex.get("max_magicule"),
                                    "min_aura": ex.get("min_aura"), "max_aura": ex.get("max_aura"),
                                    "spiritual_health": ex.get("spiritualHealth"), "abilities": ex.get("abilities", [])}
            drops = loot.get("%s:entities/%s" % (ns, eid)) or loot.get("%s:entity/%s" % (ns, eid))
            rec["drops"] = drops["pools"] if drops else None
            rec["spawns"] = [s for s in spawns if s["entity"] == full]
            rec["tags"] = res.tags_of("entity_type", full)
            egg = "%s_spawn_egg" % eid
            rec["spawn_egg"] = ("%s:%s" % (ns, egg)) if egg in item_ids else None
            ents.append(rec)
        out["categories"]["mobs"] = ents

        # ---- effects
        effs = []
        reg_eff = {r.id: r for r in regs if kind_of(r) == "effect"}
        for eid in sorted(set(content.lang_ids(res, k, "effect", ns)) | set(reg_eff)):
            full = "%s:%s" % (ns, eid)
            r = reg_eff.get(eid)
            if r is None and not linker.mentioned([k], eid):
                phantoms[m["slug"]].append(full)
                continue
            rec = {"id": full, "path": eid, "name": names.effect(full), "class": r.cls if r else linker.link([k], eid, "effect")}
            rec.update(codeinfo.effect_info(ix, r) if r else {})
            desc = None
            for kk2 in ("effect.%s.%s.description" % (ns, eid), "description.effect.%s.%s" % (ns, eid), "effect.%s.%s.desc" % (ns, eid)):
                if res.has(kk2):
                    desc = res.tr(kk2)
            rec["description"] = desc
            rec["icon_url"] = icons.texture("%s:textures/mob_effect/%s.png" % (ns, eid), os.path.join(ns, "effect", eid + ".png"), 36)
            if r is not None or res.has("effect.%s.%s" % (ns, eid)):
                effs.append(rec)
        out["categories"]["effects"] = effs

        # ---- enchantments, worldgen, advancements, commands
        out["categories"]["enchantments"] = content.load_enchantments(res, k)
        out["categories"]["biomes"] = content.load_biomes(res, k)
        out["categories"]["dimensions"] = content.load_dimensions(res, k)
        out["categories"]["structures"] = content.load_structures(res, k)
        out["categories"]["advancements"] = content.load_advancements(res, k)
        cmds = codeinfo.commands(ix, {k})
        have = {c["syntax"] for c in cmds}
        cmds += [c for c in codeinfo.annotation_commands(ix, {k}) if c["syntax"] not in have]
        out["categories"]["commands"] = sorted(cmds, key=lambda c: c["syntax"])
        out["categories"]["gamerules"] = codeinfo.gamerules(ix, {k}, res)
        cmd_msgs = []
        for kk2 in res.lang:
            if res.lang_owner.get(kk2) == k and (".command." in kk2 or kk2.startswith("command.") or kk2.startswith("commands.")):
                cmd_msgs.append({"key": kk2, "text": res.tr(kk2)})
        out["categories"]["command_messages"] = cmd_msgs
        out["categories"]["configs"] = [o["oid"] for o in options if o.get("mod") == m["slug"]]
        out["guidebooks"] = content.load_patchouli(res, k)
        # the mod's own translations, for tables embedded in hand-written guides
        os.makedirs(os.path.join(a.data, "lang"), exist_ok=True)
        own = {kk: res.tr(kk) for kk, owner in res.lang_owner.items() if owner == k}
        with open(os.path.join(a.data, "lang", m["slug"] + ".json"), "w", encoding="utf-8") as fh:
            json.dump(own, fh, ensure_ascii=False, indent=0, sort_keys=True)
        out["extra"] = family_extras(m, k, ix, res, regs, loot, names, icons, keys)
        if phantoms.get(m["slug"]):
            out["extra"]["phantoms"] = sorted(phantoms[m["slug"]])
        with open(os.path.join(a.data, m["slug"] + ".json"), "w", encoding="utf-8") as fh:
            json.dump(out, fh, indent=1, ensure_ascii=False, default=_json_default)
        cats = out["categories"]
        print("   " + ", ".join("%s=%d" % (c, len(v)) for c, v in cats.items() if isinstance(v, list)))

    # ---- shared data (trimmed to what touches the documented mods)
    doc_ns = {ns for m in MODS for ns in m["modids"]}

    def touches(ids):
        return any(isinstance(i, str) and i.lstrip("#").split(":")[0] in doc_ns for i in ids)

    kept_recipes = []
    for r in recipes:
        outs, ins = content.recipe_items(r)
        if touches(outs + ins) or r["id"].split(":")[0] in doc_ns:
            kept_recipes.append(r)
    recipes = kept_recipes
    kept_loot = {}
    for tid, t in loot.items():
        ids = [it.get("item") or "" for p in t["pools"] for it in p["items"]]
        if tid.split(":")[0] in doc_ns or touches(ids):
            kept_loot[tid] = t
    loot = kept_loot
    gear = {}
    dissolving = {}
    for kk in jar_keys:
        for gid, gd in content.load_simple_dir(res, kk, "gear_existence").items():
            if isinstance(gd, dict) and gd.get("type"):
                gear[gd["type"]] = {k2: gd.get(k2) for k2 in ("minEP", "maxEP", "evolution")}
        for did, dd in content.load_simple_dir(res, kk, "item_dissolving").items():
            if isinstance(dd, dict) and dd.get("item"):
                dissolving[dd["item"]] = dd.get("magicule")
    shared = {
        "gear": gear,
        "dissolving": dissolving,
        "options": options,
        "recipes": recipes,
        "loot": loot,
        "loot_modifiers": lmods,
        "spawns": spawns,
        "known": known,
        "names": _all_names(res, known),
        "tags": {reg: {t: sorted(res.tag_members(reg, t)) for t in v if touches(res.tag_members(reg, t)) or t.split(":")[0] in doc_ns or reg == "worldgen/biome"}
                 for reg, v in tags.items() if reg in ("item", "block", "entity_type", "worldgen/biome")},
        "icons": {("%s:%s" % (kk[1], kk[2])): v for kk, v in icons.cache.items() if kk[0] in ("item", "block") and v},
    }
    with open(os.path.join(a.data, "_shared.json"), "w", encoding="utf-8") as fh:
        json.dump(shared, fh, ensure_ascii=False, default=_json_default)
    print("done")


def _all_names(res, known):
    names = content.Names(res)
    out = {}
    for ident, kind in known.items():
        fn = {"skill": names.skill, "race": names.race, "item": names.item, "block": names.block,
              "effect": names.effect, "entity": names.entity}.get(kind)
        if fn:
            out[ident] = fn(ident)
    # every item/block with a lang name, even if not registered through a field
    for k in res.lang:
        mm = re.match(r"^(item|block|entity|effect|enchantment|biome)\.([a-z0-9_]+)\.([a-z0-9_/]+)$", k)
        if mm:
            out.setdefault("%s:%s" % (mm.group(2), mm.group(3)), res.tr(k))
    return out


def _relic_render(ix, res, cls, rd, ns, iid):
    out = {"leveling": rd.get("leveling"), "loot": rd.get("loot"), "abilities": []}
    for abd in rd["abilities"]:
        aid = abd.get("id")
        maxl = abd.get("max_level") or 10  # AbilityData's default max level
        stats = [relics.stat_summary(ix, cls, st, maxl) for st in abd["stats"]]
        base = "tooltip.relics.%s.ability.%s" % (iid, aid)
        name = res.tr(base) or (aid or "").replace("_", " ").title()
        desc = relics.render_description(res, base + ".description", stats)
        out["abilities"].append({"id": aid, "name": name, "description": desc, "required_level": abd.get("required_level"),
                                 "max_level": maxl, "cast": abd.get("cast"),
                                 "stats": [dict(s, name=(res.tr("tooltip.relics.%s.ability.%s.stat.%s" % (iid, aid, s["id"])) or (s["id"] or "").replace("_", " ").title())) for s in stats]})
    d = res.tr("tooltip.relics.%s.description" % iid)
    if d:
        out["description"] = d
    return out


def family_extras(m, key, ix, res, regs, loot, names, icons, keys):
    """Mod-specific extras that don't fit the generic categories."""
    fam = m["family"]
    ex = {}
    if fam == "artifacts":
        # RAR-Compat: relic versions of every artifact
        rk = [k for k in res.keys if k.startswith("rarcompat")]
        if rk:
            rel = {}
            for c in ix.classes.values():
                if c.mod != rk[0] or c.outer is not None or not c.method("constructDefaultRelicData"):
                    continue
                rd = relics.parse_relic(ix, c)
                if not rd:
                    continue
                iid = re.sub(r"(?<!^)([A-Z])", r"_\1", c.simple.replace("Item", "")).lower()
                rel["artifacts:" + iid] = _relic_render(ix, res, c, rd, "artifacts", iid)
            ex["rarcompat"] = rel
    if fam == "gateways":
        gates = []
        for kk in [key]:
            for ns, rel, full in res.data_files(kk, "gateways"):
                try:
                    d = load_json(full)
                except Exception:
                    continue
                gates.append({"id": "%s:%s" % (ns, rel), "name": res.tr("%s.%s" % (ns, rel)) or content.humanize(rel), "data": d})
        ex["gateways"] = gates
    if fam == "tombstone":
        perks = []
        for k2 in res.lang:
            mm = re.match(r"^tombstone\.perk\.([a-z_]+)$", k2)
            if mm:
                perks.append({"id": mm.group(1), "name": res.tr(k2), "description": res.tr(k2 + ".desc") or res.tr(k2 + ".description"),
                              "levels": [res.tr(x) for x in sorted(res.lang) if x.startswith(k2 + ".") and x != k2 + ".desc"][:10]})
        ex["perks"] = perks
        comp = []
        for k2 in sorted(res.lang):
            if k2.startswith("tombstone.compendium."):
                comp.append({"key": k2, "text": res.tr(k2)})
        ex["compendium"] = comp
    return ex


def _json_default(o):
    if isinstance(o, set):
        return sorted(o)
    if isinstance(o, InstanceOf):
        return o.fqcn
    return str(o)


if __name__ == "__main__":
    main()
