"""Render the wiki (docs/*.md + mkdocs.yml) from the extracted JSON.

    python -m wikigen.render --data ../data --docs ../docs --content ../content [--pack ../pack]

`content/` holds hand-written pages (mechanics guides, the home page intro).
`pack/` optionally holds the pack's config/ (and defaultconfigs/) folders; any
value that differs from a mod default becomes a "Pack note" on the relevant
page and in the config tables.
"""
from __future__ import annotations

import argparse
import json
import os
import posixpath
import re
import shutil
import tomllib
from collections import defaultdict, OrderedDict

from .mods import MODS, GROUPS

TIER_ORDER = ["ultimate", "unique", "extra", "common", "intrinsic", "resistance", "other"]
TIER_LABEL = {"ultimate": "Ultimate Skills", "unique": "Unique Skills", "extra": "Extra Skills", "common": "Common Skills",
              "intrinsic": "Intrinsic Skills", "resistance": "Resistance Skills", "other": "Other Skills"}
MAGIC_LABEL = {"aspectual": "Aspectual Magic", "spiritual": "Spiritual Magic", "summoning": "Summoning Magic", "misc": "Other Magic"}
CAT_TITLES = OrderedDict([
    ("abilities", "Abilities"), ("races", "Races"), ("items", "Items"), ("blocks", "Blocks"), ("mobs", "Mobs"),
    ("effects", "Effects"), ("enchantments", "Enchantments"), ("biomes", "Biomes"), ("dimensions", "Dimensions"),
    ("structures", "Structures"), ("gateways", "Gateways"), ("perks", "Perks"), ("advancements", "Advancements"),
    ("mechanics", "Mechanics"), ("commands", "Commands"), ("configs", "Configs"),
])
KIND_CAT = {"skill": "abilities", "race": "races", "item": "items", "block": "blocks", "entity": "mobs", "effect": "effects",
            "enchantment": "enchantments", "biome": "biomes", "dimension": "dimensions", "structure": "structures"}
PERM = {0: "Everyone", 1: "Moderator", 2: "Operator (level 2)", 3: "Admin (level 3)", 4: "Owner (level 4)", None: "Everyone"}


def slugify(s: str) -> str:
    s = s.split(":")[-1]
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "entry"


def esc(s) -> str:
    """Escape text for use inside Markdown (tables and paragraphs)."""
    if s is None:
        return ""
    s = str(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = s.replace("|", "\\|")
    s = s.replace("*", "\\*") if s.count("*") == 1 else s
    return s


def cell(s) -> str:
    return esc(s).replace("\r", "").replace("\n", "<br>")


def para(s) -> str:
    """Multi-line lang text as Markdown paragraphs/lines."""
    s = esc(s).replace("\\|", "|")
    lines = [l.rstrip() for l in s.split("\n")]
    return "  \n".join(lines)


def num(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, float):
        if v != v:
            return "?"
        if abs(v) >= 1e300:
            return "no limit"
        if v == int(v) and abs(v) < 1e15:
            return "{:,}".format(int(v))
        return ("%.4f" % v).rstrip("0").rstrip(".")
    if isinstance(v, int):
        if abs(v) >= 2 ** 31 - 1:
            return "no limit"
        return "{:,}".format(v)
    return str(v)


def pct(p):
    if p is None:
        return "?"
    p = p * 100
    if p >= 99.95:
        return "100%"
    if p >= 10:
        return "%.0f%%" % p
    if p >= 1:
        return "%.1f%%" % p
    return "%.2f%%" % p


def humanize(ident: str) -> str:
    return ident.split(":")[-1].split("/")[-1].replace("_", " ").title()


class Page:
    def __init__(self, path, title):
        self.path = path
        self.title = title
        self.lines = []

    def add(self, *ls):
        for l in ls:
            self.lines.append(l)

    def text(self):
        return "\n".join(self.lines).rstrip() + "\n"


class Site:
    def __init__(self, data_dir, docs_dir, content_dir, pack_dir=None):
        self.data_dir = data_dir
        self.docs = docs_dir
        self.content = content_dir
        self.pack = pack_dir
        self.mods = []
        for m in MODS:
            p = os.path.join(data_dir, m["slug"] + ".json")
            if os.path.isfile(p):
                with open(p, encoding="utf-8") as fh:
                    self.mods.append(json.load(fh))
        with open(os.path.join(data_dir, "_shared.json"), encoding="utf-8") as fh:
            self.shared = json.load(fh)
        self.options = self.shared["options"]
        self.names = self.shared["names"]
        self.icons = self.shared.get("icons", {})
        self.refs = {}       # id -> dict(path, name, icon, kind, mod)
        self.pages = []
        self.nav = []
        self.overrides = self.load_pack_overrides()
        self.index()

    # ---------------------------------------------------------- indexing
    def entry_path(self, mod, cat, ident, group=None):
        if group:
            return "%s/%s/%s/%s.md" % (mod["mod"]["slug"], cat, slugify(group), slugify(ident.replace("/", "-")))
        return "%s/%s/%s.md" % (mod["mod"]["slug"], cat, slugify(ident.replace("/", "-")))

    def item_groups(self, mod):
        groups = {i.get("category") or "Miscellaneous" for i in mod["categories"].get("items", [])}
        return len(groups) > 1

    def path_of(self, kind, ident):
        return self.refs[kind + "|" + ident]["path"]

    def index(self):
        self.ability_by_id = {}
        self.race_by_id = {}
        self.reverse = defaultdict(lambda: defaultdict(list))  # target -> relation -> [ids]
        for mod in self.mods:
            c = mod["categories"]
            for s in c.get("abilities", []):
                self._ref(mod, "abilities", s["id"], s["name"], s.get("icon_url"), "skill", self.ability_group(s))
                self.ability_by_id[s["id"]] = (mod, s)
            for r in c.get("races", []):
                self._ref(mod, "races", r["id"], r["name"], None, "race")
                self.race_by_id[r["id"]] = (mod, r)
            grouped = self.item_groups(mod)
            for kind, cat in (("item", "items"), ("block", "blocks"), ("entity", "mobs"), ("effect", "effects"),
                              ("enchantment", "enchantments"), ("biome", "biomes"), ("dimension", "dimensions"), ("structure", "structures")):
                for e in c.get(cat, []):
                    grp = (e.get("category") or "Miscellaneous") if (kind == "item" and grouped) else None
                    self._ref(mod, cat, e["id"], e["name"], e.get("icon_url"), kind, grp)
            for g in mod.get("extra", {}).get("gateways", []) or []:
                self._ref(mod, "gateways", g["id"], g["name"], None, "gateway")
        # reverse relations
        for mod in self.mods:
            c = mod["categories"]
            for s in c.get("abilities", []):
                for e in s.get("effects", []):
                    self.reverse[e]["applied_by"].append(s["id"])
                for e in s.get("related", []):
                    self.reverse[e]["mentioned_by"].append(s["id"])
                for e in s.get("items", []):
                    self.reverse[e]["used_by_skill"].append(s["id"])
                for e in s.get("acquire_requirement_refs", []) or []:
                    self.reverse[s["id"]]["requires"].append(e)
            for r in c.get("races", []):
                for sk in r.get("intrinsic", []):
                    self.reverse[sk]["intrinsic_of"].append(r["id"])
                for sk in r.get("learnable", []):
                    self.reverse[sk]["learnable_by"].append(r["id"])
                for key, lst in r.get("evolutions", {}).items():
                    if key == "previous":
                        for p in lst:
                            self.reverse[r["id"]]["evolves_from"].append(p)
                            self.reverse[p]["evolves_into"].append(r["id"])
                        continue
                    for t in lst:
                        self.reverse[t]["evolves_from"].append(r["id"])
                        self.reverse[r["id"]]["evolves_into"].append(t)
            for e in c.get("mobs", []):
                for ab in (e.get("existence") or {}).get("abilities", []) or []:
                    self.reverse[ab]["innate_to_mob"].append(e["id"])
        # skills listed in config lists (reincarnation pools etc.)
        for o in self.options:
            d = o.get("default")
            if isinstance(d, list):
                for v in d:
                    if isinstance(v, str) and v in self.ability_by_id:
                        self.reverse[v]["config_lists"].append(o["oid"])
        # recipes
        self.recipes_out = defaultdict(list)
        self.recipes_in = defaultdict(list)
        for r in self.shared["recipes"]:
            res = r.get("result") or {}
            if res.get("id"):
                self.recipes_out[res["id"]].append(r)
            ings = list(r.get("ingredients") or []) + list((r.get("key") or {}).values())
            seen = set()
            for ing in ings:
                if not ing:
                    continue
                for i in ing.get("items", []):
                    if i not in seen:
                        seen.add(i)
                        self.recipes_in[i].append(r)
                if ing.get("tag"):
                    for i in self.shared["tags"].get("item", {}).get(ing["tag"], []):
                        if i not in seen:
                            seen.add(i)
                            self.recipes_in[i].append(r)
        # loot
        self.loot_sources = defaultdict(list)
        for tid, t in self.shared["loot"].items():
            for p in t["pools"]:
                for it in p["items"]:
                    if it.get("item"):
                        self.loot_sources[it["item"]].append((tid, it))
        for lm in self.shared.get("loot_modifiers", []):
            item = lm.get("item")
            if isinstance(item, dict):
                item = item.get("id") or item.get("item")
            if isinstance(item, str):
                for tgt in lm.get("targets") or []:
                    self.loot_sources[item].append((tgt, {"chance": lm.get("chance"), "count": [1, 1], "notes": ["added by a loot modifier"]}))
        # config ownership: item class -> options
        self.opts_by_owner = defaultdict(list)
        self.opts_by_item = defaultdict(list)
        for o in self.options:
            if o.get("key") is None:
                continue
            self.opts_by_owner[o.get("owner")].append(o["oid"])
            if o.get("item"):
                self.opts_by_item[o["item"]].append(o["oid"])

    def _ref(self, mod, cat, ident, name, icon, kind, group=None):
        path = self.entry_path(mod, cat, ident, group)
        rec = {"path": path, "name": name, "icon": icon, "kind": kind, "mod": mod["mod"]["slug"], "cat": cat, "group": group}
        self.refs.setdefault(ident, rec)
        self.refs.setdefault(kind + "|" + ident, rec)

    # ------------------------------------------------------------ links
    def rel(self, frm, to):
        return posixpath.relpath(to, posixpath.dirname(frm))

    def name_of(self, ident, kind=None):
        if kind and (kind + "|" + ident) in self.refs:
            return self.refs[kind + "|" + ident]["name"]
        if ident in self.refs:
            return self.refs[ident]["name"]
        return self.names.get(ident) or humanize(ident)

    def link(self, frm, ident, kind=None, text=None, icon=False):
        if not ident:
            return ""
        if ident.startswith("#"):
            return "`%s`" % ident
        ref = self.refs.get(kind + "|" + ident) if kind else None
        ref = ref or self.refs.get(ident)
        label = esc(text or (ref["name"] if ref else self.name_of(ident, kind)))
        ic = ""
        if icon:
            ic = self.icon(frm, ident) + " "
        if ref:
            return "%s[%s](%s)" % (ic, label, self.rel(frm, ref["path"]))
        if ident.startswith("minecraft:"):
            wiki = "https://minecraft.wiki/w/" + (text or self.name_of(ident)).replace(" ", "_")
            return "%s[%s](%s)" % (ic, label, wiki)
        return ic + label

    def icon(self, frm, ident):
        ref = self.refs.get(ident)
        url = (ref or {}).get("icon") or self.icons.get(ident)
        if not url:
            return ""
        return "![](%s)" % self.rel(frm, url)

    def links(self, frm, ids, kind=None, sep=", ", limit=None):
        ids = list(OrderedDict.fromkeys(i for i in ids if i))
        more = ""
        if limit and len(ids) > limit:
            more = " and %d more" % (len(ids) - limit)
            ids = ids[:limit]
        return sep.join(self.link(frm, i, kind) for i in ids) + more

    def expand_refs(self, frm, text):
        return re.sub(r"\[\[([a-z0-9_.-]+:[a-z0-9_./-]+)\]\]", lambda m: self.link(frm, m.group(1)), text)

    # ------------------------------------------------------- pack notes
    def load_pack_overrides(self):
        out = {}
        if not self.pack or not os.path.isdir(self.pack):
            return out
        cache = {}

        def load(rel):
            if rel in cache:
                return cache[rel]
            d = None
            sub = rel.split("/", 1)[1] if "/" in rel else rel
            for base in ("config", "defaultconfigs", "serverconfig"):
                p = os.path.join(self.pack, base, sub)
                if os.path.isfile(p):
                    try:
                        with open(p, "rb") as fh:
                            d = tomllib.load(fh)
                        break
                    except Exception:
                        d = None
            cache[rel] = d
            return d

        for o in self.options:
            if o.get("key") is None or not o.get("file"):
                continue
            d = load(o["file"])
            if d is None:
                continue
            cur = d
            ok = True
            for p in list(o.get("path") or []) + [o["key"]]:
                if isinstance(cur, dict) and p in cur:
                    cur = cur[p]
                else:
                    ok = False
                    break
            if ok and not _same(cur, o.get("default")):
                out[o["oid"]] = cur
        return out

    # ------------------------------------------------------------- write
    def write(self, page: Page):
        full = os.path.join(self.docs, page.path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(page.text())
        self.pages.append(page)

    def run(self):
        # clean generated output (keep assets and hand-written overrides)
        for m in self.mods:
            d = os.path.join(self.docs, m["mod"]["slug"])
            if os.path.isdir(d):
                shutil.rmtree(d)
        nav = []
        for group in GROUPS:
            gnav = []
            for mod in self.mods:
                if mod["mod"]["group"] != group:
                    continue
                gnav.append({mod["mod"]["name"]: self.render_mod(mod)})
            nav.append({group: gnav})
        self.render_home()
        self.render_pack_notes_page()
        self.nav = [{"Home": "index.md"}, {"Pack notes": "pack-notes.md"}] + nav + [{"About this wiki": "about.md"}]
        self.render_about()

    # ============================================================ pages
    def render_mod(self, mod):
        m = mod["mod"]
        slug = m["slug"]
        c = mod["categories"]
        nav = [{"Overview": "%s/index.md" % slug}]
        cats = []
        if c.get("abilities"):
            nav.append({"Abilities": self.render_abilities(mod)})
            cats.append("abilities")
        if c.get("races"):
            nav.append({"Races": self.render_races(mod)})
            cats.append("races")
        for cat in ("items", "blocks", "mobs", "effects", "enchantments", "biomes", "dimensions", "structures"):
            if c.get(cat):
                nav.append({CAT_TITLES[cat]: getattr(self, "render_" + cat)(mod)})
                cats.append(cat)
        ex = mod.get("extra") or {}
        if ex.get("gateways"):
            nav.append({"Gateways": self.render_gateways(mod)})
            cats.append("gateways")
        if ex.get("perks"):
            nav.append({"Perks": self.render_perks(mod)})
            cats.append("perks")
        if c.get("advancements"):
            nav.append({"Advancements": self.render_advancements(mod)})
            cats.append("advancements")
        mech = self.render_mechanics(mod)
        books = self.render_guidebooks(mod)
        if mech or books:
            mnav = ([{"Guide": mech}] if mech else []) + books
            nav.append({"Mechanics": mnav if len(mnav) > 1 else (mech or books[0])})
            cats.append("mechanics")
        if c.get("commands") or c.get("command_messages") or c.get("gamerules"):
            nav.append({"Commands": self.render_commands(mod)})
            cats.append("commands")
        if c.get("configs"):
            nav.append({"Configs": self.render_configs(mod)})
            cats.append("configs")
        self.render_mod_index(mod, cats)
        return nav

    def breadcrumb(self, page, mod, cat=None, sub=None):
        parts = ["[%s](%s)" % (esc(mod["mod"]["name"]), self.rel(page.path, "%s/index.md" % mod["mod"]["slug"]))]
        if cat:
            parts.append("[%s](%s)" % (CAT_TITLES.get(cat, cat.title()), self.rel(page.path, "%s/%s/index.md" % (mod["mod"]["slug"], cat))))
        if sub:
            gp = "%s/%s/%s/index.md" % (mod["mod"]["slug"], cat, slugify(sub))
            if cat and os.path.dirname(page.path) == os.path.dirname(gp) and not page.path.endswith("index.md"):
                parts.append("[%s](%s)" % (esc(sub), self.rel(page.path, gp)))
            else:
                parts.append(esc(sub))
        page.add("<small>%s</small>" % " &rsaquo; ".join(parts), "")

    def infobox(self, page, icon_url, rows, caption=None):
        page.add('<div class="infobox" markdown>', "")
        if icon_url:
            page.add("![%s](%s)" % (esc(caption or ""), self.rel(page.path, icon_url)), "")
        page.add("| | |", "|---|---|")
        for k, v in rows:
            if v in (None, "", [], "None"):
                continue
            page.add("| **%s** | %s |" % (k, v))
        page.add("", "</div>", "")

    def pack_note(self, page, oids):
        notes = [(o, self.overrides[o]) for o in oids if o in self.overrides]
        if not notes:
            return
        page.add("> [!NOTE]", "> **Pack note:** this pack changes the defaults below.")
        for oid, val in notes:
            o = self.options[oid]
            page.add("> - `%s` is **%s** (mod default: %s)" % (".".join(list(o.get("path") or []) + [o["key"]]), cell(_fmtval(val)), cell(_fmtval(o.get("default")))))
        page.add("")

    def config_table(self, page, oids, title="Stats (config defaults)", level=2):
        opts = [self.options[o] for o in oids if o < len(self.options) and self.options[o].get("key") is not None]
        if not opts:
            return
        page.add("%s %s" % ("#" * level, title), "")
        files = OrderedDict()
        for o in opts:
            files.setdefault(o.get("file"), []).append(o)
        for f, lst in files.items():
            cfgpage = self.config_file_path(lst[0])
            page.add("Set in [`%s`](%s)." % (f, self.rel(page.path, cfgpage)) if cfgpage else "Set in `%s`." % f, "")
            has_pack = any(o["oid"] in self.overrides for o in lst)
            head = "| Option | Default |" + (" This pack |" if has_pack else "") + " Description |"
            page.add(head, "|---|---|" + ("---|" if has_pack else "") + "---|")
            for o in lst:
                key = ".".join(list(o.get("path") or [])[-1:] + [o["key"]]) if o.get("path") else o["key"]
                rng = _range(o)
                pv = (" %s |" % cell(_fmtval(self.overrides[o["oid"]])) if o["oid"] in self.overrides else " |") if has_pack else ""
                page.add("| `%s` | %s%s |%s %s |" % (key, cell(_fmtval(o.get("default"))), rng, pv, cell(o.get("comment") or "")))
            page.add("")

    def config_file_path(self, o):
        f = o.get("file")
        if not f:
            return None
        return "%s/configs/%s.md" % (o["mod"], slugify(f.replace("/", "-").replace(".toml", "")))

    # --------------------------------------------------------- mod index
    def render_mod_index(self, mod, cats):
        m = mod["mod"]
        meta = m.get("meta") or {}
        c = mod["categories"]
        page = Page("%s/index.md" % m["slug"], m["name"])
        page.add("# %s" % m["name"], "")
        logo = self.mod_logo(mod)
        rows = [("Mod ID", "`%s`" % m["modids"][0]), ("Version", esc(meta.get("version") or "")),
                ("File", "`%s`" % meta.get("jar") if meta.get("jar") else None),
                ("Authors", esc(meta.get("authors") or "")), ("License", esc(meta.get("license") or "")),
                ("Website", "[%s](%s)" % (esc(meta["displayURL"]), meta["displayURL"]) if meta.get("displayURL") else None),
                ("Requires", ", ".join(self.dep_link(page, d) for d in meta.get("depends", []) if d["type"] in ("required", "REQUIRED")))]
        self.infobox(page, logo, rows, m["name"])
        page.add(esc(m["blurb"]), "")
        if meta.get("description") and meta["description"].strip() != m["blurb"]:
            page.add("> %s" % para(meta["description"]).replace("\n", "\n> "), "")
        intro = self.content_file(m["slug"], "overview.md")
        if intro:
            page.add(intro, "")
        page.add("## Contents", "")
        page.add("| Section | Entries |", "|---|---|")
        for cat in cats:
            n = self.cat_count(mod, cat)
            page.add("| [%s](%s/index.md) | %s |" % (CAT_TITLES[cat], cat, n))
        page.add("")
        # quick breakdown for abilities
        if c.get("abilities"):
            cnt = defaultdict(int)
            for s in c["abilities"]:
                cnt[self.ability_group(s)] += 1
            page.add("### Abilities at a glance", "")
            page.add(", ".join("%s **%d**" % (k, v) for k, v in sorted(cnt.items(), key=lambda kv: self.group_sort(kv[0]))), "")
        self.write(page)

    def mod_logo(self, mod):
        return (mod["mod"].get("meta") or {}).get("logo_url")

    def dep_link(self, page, d):
        for mm in self.mods:
            if d["modid"] in mm["mod"]["modids"]:
                return "[%s](%s)" % (esc(mm["mod"]["name"]), self.rel(page.path, "%s/index.md" % mm["mod"]["slug"]))
        return "`%s`" % d["modid"]

    def cat_count(self, mod, cat):
        c = mod["categories"]
        ex = mod.get("extra") or {}
        if cat in c and isinstance(c[cat], list):
            if cat == "configs":
                return "%s options" % num(len([o for o in c[cat] if self.options[o].get("key") is not None]))
            return num(len(c[cat]))
        if cat == "gateways":
            return num(len(ex.get("gateways", [])))
        if cat == "perks":
            return num(len(ex.get("perks", [])))
        if cat == "mechanics":
            return "guide"
        return ""

    def content_file(self, slug, name):
        p = os.path.join(self.content, slug, name)
        if os.path.isfile(p):
            with open(p, encoding="utf-8") as fh:
                return fh.read().strip()
        return None

    # --------------------------------------------------------- abilities
    def ability_group(self, s):
        if s.get("category") == "magic":
            return MAGIC_LABEL.get(s.get("tier"), "Magic")
        if s.get("category") == "battlewill":
            return "Battlewill"
        return TIER_LABEL.get(s.get("tier"), "Other Skills")

    def group_sort(self, g):
        order = [TIER_LABEL[t] for t in TIER_ORDER] + list(MAGIC_LABEL.values()) + ["Battlewill"]
        return order.index(g) if g in order else 99

    def render_abilities(self, mod):
        slug = mod["mod"]["slug"]
        skills = mod["categories"]["abilities"]
        groups = defaultdict(list)
        for s in skills:
            groups[self.ability_group(s)].append(s)
        glist = sorted(groups, key=self.group_sort)
        index = Page("%s/abilities/index.md" % slug, "Abilities")
        index.add("# Abilities", "")
        self.breadcrumb(index, mod)
        index.add("%s adds **%d** abilities: skills, magic and battlewill arts. "
                  "Each ability has its own page with modes, costs, how to get it and its default config values." % (esc(mod["mod"]["name"]), len(skills)), "")
        nav = [{"All abilities": "%s/abilities/index.md" % slug}]
        index.add("| Group | Count |", "|---|---|")
        for g in glist:
            index.add("| [%s](%s/index.md) | %d |" % (g, slugify(g), len(groups[g])))
        index.add("")
        for g in glist:
            gp = Page("%s/abilities/%s/index.md" % (slug, slugify(g)), g)
            gp.add("# %s" % g, "")
            self.breadcrumb(gp, mod, "abilities")
            gp.add(GROUP_BLURB.get(g, ""), "") if GROUP_BLURB.get(g) else None
            gp.add("| | Ability | Description |", "|---|---|---|")
            for s in sorted(groups[g], key=lambda s: s["name"].lower()):
                gp.add("| %s | %s | %s |" % (self.icon(gp.path, s["id"]), self.link(gp.path, s["id"], "skill"), cell(_short(s.get("description")))))
            gp.add("")
            self.write(gp)
            nav.append({g: gp.path})
            index.add("## %s" % g, "")
            index.add(", ".join(self.link(index.path, s["id"], "skill") for s in sorted(groups[g], key=lambda s: s["name"].lower())), "")
            for s in groups[g]:
                self.render_ability(mod, s, g)
        self.write(index)
        return nav

    def render_ability(self, mod, s, group):
        page = Page(self.path_of("skill", s["id"]), s["name"])
        page.add("# %s" % esc(s["name"]), "")
        self.breadcrumb(page, mod, "abilities", group)
        rows = [("Type", group[:-1] if group.endswith("s") and group != "Battlewill" else group), ("ID", "`%s`" % s["id"])]
        if s.get("element"):
            rows.append(("Element" if s.get("category") == "magic" else "Kind", s["element"].replace("_", " ").title()))
        if s.get("modes"):
            rows.append(("Modes", str(len(s["modes"]))))
        for key, label in (("acquire_cost", "Acquisition cost (MP)"), ("max_mastery", "Max mastery")):
            v = s.get(key)
            if v:
                vals = [x["value"] for x in v if x.get("value") and re.search(r"\d", str(x["value"]))]
                if vals:
                    rows.append((label, cell(" / ".join(vals))))
        if s.get("cooldowns"):
            rows.append(("Cooldowns (s)", cell(", ".join(s["cooldowns"]))))
        act = [h["key"] for h in s.get("hooks", [])]
        kinds = []
        if "toggle" in act:
            kinds.append("Toggle")
        if "press" in act:
            kinds.append("Press")
        if "hold" in act or "release" in act:
            kinds.append("Hold")
        if not kinds:
            kinds.append("Passive")
        rows.append(("Activation", ", ".join(kinds)))
        self.infobox(page, s.get("icon_url"), rows, s["name"])
        if s.get("description"):
            page.add("> %s" % para(s["description"]).replace("\n", "\n> "), "")
        self.pack_note(page, s.get("config", []))
        # modes and costs
        modes = s.get("modes") or []
        mc = s.get("magicule_cost") or []
        ac = s.get("aura_cost") or []
        if modes:
            page.add("## Modes", "")
            page.add("| # | Mode |", "|---|---|")
            for md in modes:
                page.add("| %d | %s |" % (md["index"] + 1, cell(md["name"])))
            page.add("")
        if mc or ac:
            page.add("## Costs", "")
            page.add("| When | Magicule (MP) | Aura (AP) |", "|---|---|---|")
            rowsn = max(len(mc), len(ac))
            for i in range(rowsn):
                a = mc[i] if i < len(mc) else {}
                b = ac[i] if i < len(ac) else {}
                when = a.get("when") or b.get("when") or "Always"
                page.add("| %s | %s | %s |" % (cell(when), _costcell(a.get("value", "")), _costcell(b.get("value", ""))))
            page.add("")
        # how it works
        hooks = s.get("hooks") or []
        if hooks:
            page.add("## How it works", "")
            for h in hooks:
                page.add("- %s" % h["label"])
            page.add("")
        attrs = s.get("attributes") or []
        if attrs:
            page.add("### Attribute changes", "")
            page.add("| Attribute | Amount | Operation |", "|---|---|---|")
            for a in attrs:
                page.add("| %s | %s | %s |" % (cell(a["attribute"]), cell(a["amount"]), cell(_op(a["operation"]))))
            page.add("")
        # obtaining
        ob = []
        if s.get("obtainment_text"):
            ob.append(esc(s["obtainment_text"]))
        rv = self.reverse.get(s["id"], {})
        if rv.get("intrinsic_of"):
            ob.append("Intrinsic skill of: " + self.links(page.path, rv["intrinsic_of"], "race"))
        if rv.get("learnable_by"):
            ob.append("Can be learned by: " + self.links(page.path, rv["learnable_by"], "race"))
        if rv.get("innate_to_mob"):
            ob.append("Innate to mobs: " + self.links(page.path, rv["innate_to_mob"], "entity"))
        for t in s.get("tags", []):
            src = TAG_SOURCES.get(t.split(":")[-1].split("/")[-1])
            if src:
                ob.append(src)
        for oid in rv.get("config_lists", []):
            o = self.options[oid]
            ob.append("Listed in the `%s` config option (%s)%s" % (o["key"], o["file"], (": " + esc(_short(o.get("comment"), 140))) if o.get("comment") else ""))
        req_refs = s.get("acquire_requirement_refs") or []
        if req_refs:
            ob.append("Acquisition checks: " + self.links(page.path, req_refs))
        for msg in s.get("acquire_requirement_messages") or []:
            ob.append("In-game message: *%s*" % esc(msg))
        if ob:
            page.add("## Obtaining", "")
            for o in OrderedDict.fromkeys(ob):
                page.add("- %s" % o)
            page.add("")
        # related
        rel = []
        if s.get("related"):
            rel.append(("Related skills", self.links(page.path, s["related"], "skill", limit=20)))
        if s.get("effects"):
            rel.append(("Effects", self.links(page.path, s["effects"], "effect")))
        if s.get("items"):
            rel.append(("Items", self.links(page.path, s["items"], "item")))
        if s.get("entities"):
            rel.append(("Summons / entities", self.links(page.path, s["entities"], "entity")))
        if rv.get("mentioned_by"):
            rel.append(("Referenced by", self.links(page.path, rv["mentioned_by"], "skill", limit=20)))
        if rel:
            page.add("## Related", "")
            for k, v in rel:
                page.add("- **%s:** %s" % (k, v))
            page.add("")
        self.config_table(page, s.get("config", []))
        if s.get("messages"):
            page.add("## In-game messages", "")
            page.add('<details markdown><summary>Show %d messages</summary>' % len(s["messages"]), "")
            for msg in s["messages"]:
                page.add("- %s" % esc(msg["text"]).replace("\n", " "))
            page.add("", "</details>", "")
        if s.get("tags"):
            page.add("## Tags", "")
            page.add(", ".join("`%s`" % t for t in s["tags"]), "")
        self.write(page)

    # ------------------------------------------------------------- races
    def race_stats(self, r):
        """Pull the common race stats out of the linked config options."""
        stat_keys = OrderedDict([
            ("minAura", "Min aura"), ("maxAura", "Max aura"), ("minMagicule", "Min magicule"), ("maxMagicule", "Max magicule"),
            ("maxHealth", "Health bonus"), ("maxHealthBonus", "Health bonus"), ("maxSpiritualHealth", "Spiritual health bonus"),
            ("spiritualHealthBonus", "Spiritual health bonus"), ("attack", "Attack damage bonus"), ("attackDamageBonus", "Attack damage bonus"),
            ("attackSpeed", "Attack speed bonus"), ("knockbackResistance", "Knockback resistance"), ("movementSpeed", "Movement speed bonus"),
            ("movementSpeedBonus", "Movement speed bonus"), ("swimSpeed", "Swim speed bonus"), ("size", "Size bonus"),
            ("startingEpMin", "Starting EP (min)"), ("startingEpMax", "Starting EP (max)"), ("evolutionEpRequirement", "EP to evolve into"),
            ("epRequirement", "EP to evolve into"),
        ])
        found = OrderedDict()
        for oid in r.get("config", []):
            o = self.options[oid]
            if o.get("key") in stat_keys and stat_keys[o["key"]] not in found:
                v = self.overrides.get(oid, o.get("default"))
                found[stat_keys[o["key"]]] = v
        return found

    STAGES = ("Starting", "In-between", "Final")

    def race_stage(self, rid):
        """Where a race sits in its evolution line, across every mod in the pack.
        A race nothing evolves into and that evolves into nothing is both Starting and Final."""
        rel = self.reverse.get(rid, {})
        prev = [p for p in rel.get("evolves_from", []) if p != rid]
        nxt = [n for n in rel.get("evolves_into", []) if n != rid]
        if prev and nxt:
            return ["In-between"]
        return (["Starting"] if not prev else []) + (["Final"] if not nxt else [])

    @staticmethod
    def stage_cell(stages):
        return " / ".join('<span class="stage stage-%s">%s</span>' % (s.lower(), s) for s in stages)

    def render_races(self, mod):
        slug = mod["mod"]["slug"]
        races = mod["categories"]["races"]
        index = Page("%s/races/index.md" % slug, "Races")
        index.add("# Races", "")
        self.breadcrumb(index, mod)
        stages = {r["id"]: self.race_stage(r["id"]) for r in races}
        counts = {s: sum(1 for v in stages.values() if s in v) for s in self.STAGES}
        both = sum(1 for v in stages.values() if len(v) > 1)
        index.add("%s adds **%d** races: **%d** starting, **%d** in-between and **%d** final.%s" % (
            esc(mod["mod"]["name"]), len(races), counts["Starting"], counts["In-between"], counts["Final"],
            (" %s no evolutions at all, so %s both starting and final." % ("1 race has" if both == 1 else "%d races have" % both, "it counts as" if both == 1 else "they count as")) if both else ""), "")
        index.add("- **Starting:** the first race of its evolution line. Nothing evolves into it, so you get it by reincarnating into it or through a special item, skill or event.",
                  "- **In-between:** reached by evolving, and can evolve further.",
                  "- **Final:** the last step of its line. It does not evolve any further.", "")
        index.add("Races that link to other mods' races (for example an addon race that evolves from a Tensura race) are placed using the whole pack's evolution trees.", "")
        index.add('<div class="filter-table" data-filter="Stage" data-order="%s" markdown>' % ",".join(self.STAGES), "")
        index.add("| Race | Stage | Difficulty | Alignment | Evolves from | Evolves into |", "|---|---|---|---|---|---|")
        for r in sorted(races, key=lambda r: r["name"].lower()):
            rel = self.reverse.get(r["id"], {})
            prev = list(dict.fromkeys(p for p in rel.get("evolves_from", []) if p != r["id"]))
            nxt = list(dict.fromkeys(n for n in rel.get("evolves_into", []) if n != r["id"]))
            index.add("| %s | %s | %s | %s | %s | %s |" % (
                self.link(index.path, r["id"], "race"), self.stage_cell(stages[r["id"]]), cell(r.get("difficulty") or ""),
                cell(r.get("alignment") or ""), self.links(index.path, prev, "race", limit=6), self.links(index.path, nxt, "race", limit=6)))
        index.add("", "</div>", "")
        # evolution trees (mermaid), one per connected family
        fams = self.race_families(races)
        if fams:
            index.add("## Evolution trees", "")
            for fam in fams:
                root = min(fam, key=lambda i: (len(self.reverse.get(i, {}).get("evolves_from", [])) > 0, self.name_of(i, "race")))
                index.add("### %s line" % esc(self.name_of(root, "race")), "")
                index.add(self.mermaid(fam), "")
        self.write(index)
        for r in races:
            self.render_race(mod, r)
        return index.path

    def race_families(self, races):
        ids = [r["id"] for r in races]
        adj = defaultdict(set)
        by = {r["id"]: r for r in races}
        for r in races:
            for key, lst in r.get("evolutions", {}).items():
                for t in lst:
                    adj[r["id"]].add(t)
                    adj[t].add(r["id"])
        seen = set()
        fams = []
        for i in ids:
            if i in seen:
                continue
            stack = [i]
            comp = set()
            while stack:
                x = stack.pop()
                if x in comp:
                    continue
                comp.add(x)
                stack.extend(adj[x] - comp)
            seen |= comp
            if len(comp) > 1:
                fams.append(sorted(comp))
        return sorted(fams, key=lambda f: -len(f))

    def mermaid(self, fam):
        idx = {r: "r%d" % i for i, r in enumerate(fam)}
        lines = ["```mermaid", "flowchart LR"]
        for r in fam:
            lines.append('  %s["%s"]' % (idx[r], self.name_of(r, "race").replace('"', "'")))
        edges = set()
        for r in fam:
            ref = self.race_by_id.get(r)
            if not ref:
                continue
            ev = ref[1].get("evolutions", {})
            for key in ("next", "default", "awakening", "harvest_festival"):
                for t in ev.get(key, []):
                    if t in idx:
                        edges.add((r, t))
            for p in ev.get("previous", []):
                if p in idx:
                    edges.add((p, r))
        for a, b in sorted(edges):
            lines.append("  %s --> %s" % (idx[a], idx[b]))
        lines.append("```")
        return "\n".join(lines)

    def resolve_req_text(self, mod, t):
        """Fill in values the code reads from per-race config tables (Ascension's getEvolutionEp("id"))."""
        def rep(m):
            rid = m.group(1)
            for o in self.options:
                if o.get("mod") == mod["mod"]["slug"] and o.get("key") == "evolutionEpRequirement" and (o.get("path") or [None])[-1] == rid:
                    return num(self.overrides.get(o["oid"], o.get("default")))
            return m.group(0)
        return re.sub(r"\b([a-z0-9_]+) \(evolution ep\)", rep, t)

    def render_race(self, mod, r):
        page = Page(self.entry_path(mod, "races", r["id"]), r["name"])
        page.add("# %s" % esc(r["name"]), "")
        self.breadcrumb(page, mod, "races")
        stats = self.race_stats(r)
        rows = [("ID", "`%s`" % r["id"]), ("Stage", self.stage_cell(self.race_stage(r["id"]))),
                ("Difficulty", esc(r.get("difficulty") or "")), ("Alignment", esc(r.get("alignment") or ""))]
        if "Min aura" in stats or "Max aura" in stats:
            rows.append(("Aura", "%s - %s" % (num(stats.get("Min aura")), num(stats.get("Max aura")))))
        if "Min magicule" in stats or "Max magicule" in stats:
            rows.append(("Magicule", "%s - %s" % (num(stats.get("Min magicule")), num(stats.get("Max magicule")))))
        for k in ("Health bonus", "Spiritual health bonus", "Attack damage bonus", "Movement speed bonus", "EP to evolve into"):
            if k in stats:
                rows.append((k, num(stats[k])))
        self.infobox(page, None, rows, r["name"])
        if r.get("description"):
            page.add("> %s" % para(r["description"]).replace("\n", "\n> "), "")
        self.pack_note(page, r.get("config", []))
        ev = r.get("evolutions", {})
        prev = list(OrderedDict.fromkeys((ev.get("previous") or []) + self.reverse.get(r["id"], {}).get("evolves_from", [])))
        page.add("## Evolution", "")
        if prev:
            page.add("- **Evolves from:** " + self.links(page.path, prev, "race"))
        listed = {x for k, lst in ev.items() if k != "previous" for x in lst}
        nxt = list(OrderedDict.fromkeys((ev.get("next") or []) + [x for x in self.reverse.get(r["id"], {}).get("evolves_into", []) if x not in listed]))
        if nxt:
            page.add("- **Evolves into:** " + self.links(page.path, nxt, "race"))
        if ev.get("default"):
            page.add("- **Default evolution:** " + self.links(page.path, ev["default"], "race"))
        if ev.get("awakening"):
            page.add("- **On awakening (True Demon Lord / True Hero):** " + self.links(page.path, ev["awakening"], "race"))
        if ev.get("harvest_festival"):
            page.add("- **During the Harvest Festival:** " + self.links(page.path, ev["harvest_festival"], "race"))
        if not (prev or nxt or any(ev.values())):
            page.add("This race has no evolutions.")
        page.add("")
        reqs = r.get("requirements") or []
        if reqs and prev:
            page.add("### Requirements to evolve into %s" % esc(r["name"]), "")
            page.add("Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.", "")
            page.add("| Requirement | Weight |", "|---|---|")
            for q in reqs:
                page.add("| %s | %s%% |" % (self.expand_refs(page.path, cell(self.resolve_req_text(mod, q["text"]))), cell(q.get("weight") or "?")))
            page.add("")
        fam = [f for f in self.race_families([x[1] for x in self.race_by_id.values()]) if r["id"] in f]
        if fam and len(fam[0]) <= 40:
            page.add("### Evolution tree", "")
            page.add(self.mermaid(fam[0]), "")
        if r.get("intrinsic"):
            page.add("## Intrinsic skills", "")
            page.add("Granted automatically when you become this race.", "")
            for sk in r["intrinsic"]:
                page.add("- %s %s" % (self.icon(page.path, sk), self.link(page.path, sk, "skill")))
            page.add("")
        if r.get("learnable"):
            page.add("## Learnable skills", "")
            page.add("This race can learn these skills through training.", "")
            for sk in r["learnable"]:
                page.add("- %s %s" % (self.icon(page.path, sk), self.link(page.path, sk, "skill")))
            page.add("")
        if r.get("traits"):
            page.add("## Traits", "")
            for t in r["traits"]:
                page.add("- %s" % esc(t))
            page.add("")
        attrs = [a for a in (r.get("attributes") or []) if not str(a.get("amount", "")).startswith("`")]
        if attrs:
            page.add("## Attribute modifiers", "")
            page.add("| Attribute | Amount | Operation |", "|---|---|---|")
            for a in attrs:
                page.add("| %s | %s | %s |" % (cell(a["attribute"]), cell(a["amount"]), cell(_op(a["operation"]))))
            page.add("")
        self.config_table(page, r.get("config", []))
        if r.get("tags"):
            page.add("## Tags", "")
            page.add(", ".join("`%s`" % t for t in r["tags"]), "")
        self.write(page)

    # ------------------------------------------------------------- items
    def render_items(self, mod):
        return self._render_things(mod, "items", "Items", self.render_item, lambda i: i.get("category") or "Miscellaneous")

    def render_blocks(self, mod):
        return self._render_things(mod, "blocks", "Blocks", self.render_block, lambda b: "Blocks")

    def _render_things(self, mod, cat, title, fn, grouper):
        slug = mod["mod"]["slug"]
        things = mod["categories"][cat]
        groups = defaultdict(list)
        for t in things:
            groups[grouper(t)].append(t)
        index = Page("%s/%s/index.md" % (slug, cat), title)
        index.add("# %s" % title, "")
        self.breadcrumb(index, mod)
        index.add("%s adds **%d** %s." % (esc(mod["mod"]["name"]), len(things), title.lower()), "")
        nav = [{"All %s" % title.lower(): index.path}]
        kind = {"items": "item", "blocks": "block"}[cat]
        ordered = sorted(groups, key=lambda g: (g in ("Miscellaneous", "Misc"), g))
        if len(groups) > 1:
            index.add("| Group | Count |", "|---|---|")
            for g in ordered:
                index.add("| [%s](%s/index.md) | %d |" % (esc(g), slugify(g), len(groups[g])))
            index.add("")
        for g in ordered:
            if len(groups) > 1:
                index.add("## %s" % esc(g), "")
                gp = Page("%s/%s/%s/index.md" % (slug, cat, slugify(g)), g)
                gp.add("# %s" % esc(g), "")
                self.breadcrumb(gp, mod, cat)
                gp.add("| | Name | Description |", "|---|---|---|")
                for t in sorted(groups[g], key=lambda t: t["name"].lower()):
                    d = (t.get("relic") or {}).get("description") or ((t.get("tooltips") or [None])[0])
                    gp.add("| %s | %s | %s |" % (self.icon(gp.path, t["id"]), self.link(gp.path, t["id"], kind), cell(_short(d, 120))))
                gp.add("")
                self.write(gp)
                nav.append({g: gp.path})
            index.add("| | Name | ID |", "|---|---|---|")
            for t in sorted(groups[g], key=lambda t: t["name"].lower()):
                index.add("| %s | %s | `%s` |" % (self.icon(index.path, t["id"]), self.link(index.path, t["id"], kind), t["id"]))
            index.add("")
            for t in groups[g]:
                fn(mod, t, g)
        self.write(index)
        return nav if len(nav) > 1 else index.path

    def render_item(self, mod, it, group):
        page = Page(self.path_of("item", it["id"]), it["name"])
        page.add("# %s" % esc(it["name"]), "")
        self.breadcrumb(page, mod, "items", group)
        props = it.get("props") or {}
        slots = [t.split(":", 1)[1] for t in it.get("tags", []) if t.startswith("curios:") and t != "curios:curio"]
        slots = slots or [t.split("/", 1)[1] for t in it.get("tags", []) if t.startswith("artifacts:slot/")]
        gear = self.gear_info(page, it["id"])
        rows = [("ID", "`%s`" % it["id"]), ("Category", esc(group)),
                ("Stack size", str(props["stack"]) if "stack" in props else None),
                ("Durability", num(props["durability"]) if "durability" in props else None),
                ("Rarity", props.get("rarity")), ("Fire resistant", "Yes" if props.get("fire_resistant") else None),
                ("Curio slot", ", ".join(s.replace("_", " ").title() for s in slots) if slots else None)]
        rows += gear
        self.infobox(page, it.get("icon_url"), rows, it["name"])
        rel = it.get("relic")
        tips = [t for t in it.get("tooltips") or [] if t and not (rel and t == rel.get("description"))]
        if tips:
            page.add("## Description", "")
            for t in tips:
                page.add(para(t), "")
        oids = list(self.opts_by_item.get(it["id"], [])) + (list(self.opts_by_owner.get(it.get("class"), [])) if it.get("class") else [])
        self.pack_note(page, oids)
        if rel:
            self.relic_section(page, rel, "Relic abilities")
        rar = (mod.get("extra") or {}).get("rarcompat", {}).get(it["id"])
        if rar:
            page.add("## In this pack: relic version (RAR-Compat)", "")
            page.add("> [!NOTE]", "> **Pack note:** this pack includes RAR-Compat, which turns %s into a Relics-style relic. "
                     "It levels up as you use it and unlocks the abilities below instead of the stock behaviour." % esc(it["name"]), "")
            self.relic_section(page, rar, None, level=3)
        self.obtaining(page, it["id"])
        self.usage(page, it["id"])
        self.config_table(page, oids, "Config")
        if it.get("tags"):
            page.add("## Tags", "")
            page.add(", ".join("`%s`" % t for t in it["tags"]), "")
        self.write(page)

    def gear_info(self, page, ident):
        rows = []
        g = (self.shared.get("gear") or {}).get(ident)
        if g:
            if g.get("minEP") is not None or g.get("maxEP") is not None:
                rows.append(("Gear EP", "%s - %s" % (num(g.get("minEP")), num(g.get("maxEP")))))
            if g.get("evolution"):
                rows.append(("Evolves into", self.link(page.path, g["evolution"], "item")))
        d = (self.shared.get("dissolving") or {}).get(ident)
        if d is not None:
            rows.append(("Magicule when dissolved", num(d)))
        return rows

    def relic_section(self, page, rel, title, level=2):
        if title:
            page.add("%s %s" % ("#" * level, title), "")
        lv = rel.get("leveling") or {}
        if lv:
            page.add("Relic levelling: up to level **%s**, first level costs **%s** XP, +%s XP per level." % (
                lv.get("max_level", "?"), lv.get("initial_cost", "?"), lv.get("step", "?")), "")
        if rel.get("description"):
            if "experience" in rel["description"].lower():
                page.add("**How it earns experience:**", "", para(rel["description"]), "")
            else:
                page.add("> %s" % para(rel["description"]).replace("\n", "\n> "), "")
        if rel.get("loot"):
            page.add("Found in loot chests of kind: %s." % ", ".join(RELIC_LOOT.get(l, l.replace("_", " ").lower()) for l in rel["loot"]), "")
        for ab in rel.get("abilities", []):
            head = "#" * (level + 1)
            extra = []
            if ab.get("required_level"):
                extra.append("unlocks at relic level %s" % ab["required_level"])
            if ab.get("cast"):
                extra.append("active (%s)" % ab["cast"].lower().replace("_", " "))
            else:
                extra.append("passive")
            page.add("%s %s" % (head, esc(ab["name"])), "")
            page.add("*%s. Ability max level %s.*" % (", ".join(extra).capitalize(), ab.get("max_level", "?")), "")
            if ab.get("description"):
                page.add(para(ab["description"]).replace("\\*\\*", "**"), "")
            if ab.get("stats"):
                page.add("| Stat | Starting value | Per level | At max level |", "|---|---|---|---|")
                for st in ab["stats"]:
                    page.add("| %s | %s | %s | %s |" % (cell(st.get("name")), cell(st.get("base")), cell(st.get("per_level") or "-"), cell(st.get("max") or "-")))
                page.add("")

    def render_block(self, mod, b, group):
        page = Page(self.path_of("block", b["id"]), b["name"])
        page.add("# %s" % esc(b["name"]), "")
        self.breadcrumb(page, mod, "blocks")
        tool = [t.split("/")[-1] for t in b.get("tags", []) if t.startswith("minecraft:mineable/")]
        level = [t.split(":")[-1].replace("needs_", "").replace("_tool", "") for t in b.get("tags", []) if "needs_" in t]
        rows = [("ID", "`%s`" % b["id"]), ("Tool", ", ".join(t.title() for t in tool) if tool else None),
                ("Tool tier", ", ".join(l.title() for l in level) if level else None)]
        self.infobox(page, b.get("icon_url"), rows, b["name"])
        tips = b.get("tooltips") or []
        if tips:
            page.add("## Description", "")
            for t in tips:
                page.add(para(t), "")
        if b.get("drops"):
            page.add("## Drops", "")
            self.loot_table(page, b["drops"])
        self.obtaining(page, b["id"])
        self.usage(page, b["id"])
        if b.get("tags"):
            page.add("## Tags", "")
            page.add(", ".join("`%s`" % t for t in b["tags"]), "")
        self.write(page)

    def loot_table(self, page, pools):
        page.add("| Item | Count | Chance | Notes |", "|---|---|---|---|")
        for p in pools:
            for it in p["items"]:
                label = self.link(page.path, it["item"], "item", icon=True) if it.get("item") else ("table `%s`" % it.get("table"))
                cnt = it.get("count") or [1, 1]
                c = num(cnt[0]) if cnt[0] == cnt[1] else "%s-%s" % (num(cnt[0]), num(cnt[1]))
                page.add("| %s | %s | %s | %s |" % (label, c, pct(it.get("chance")), cell(", ".join(it.get("notes") or []))))
        page.add("")

    def obtaining(self, page, ident):
        recs = self.recipes_out.get(ident, [])
        src = self.loot_sources.get(ident, [])
        if not recs and not src:
            return
        page.add("## Obtaining", "")
        if recs:
            page.add("### Recipes", "")
            for r in recs[:12]:
                self.recipe(page, r)
            if len(recs) > 12:
                page.add("*...and %d more recipes.*" % (len(recs) - 12), "")
        if src:
            page.add("### Loot", "")
            page.add("| Source | Count | Chance | Notes |", "|---|---|---|---|")
            for tid, it in sorted(src, key=lambda x: -(x[1].get("chance") or 0))[:40]:
                cnt = it.get("count") or [1, 1]
                c = num(cnt[0]) if cnt[0] == cnt[1] else "%s-%s" % (num(cnt[0]), num(cnt[1]))
                page.add("| %s | %s | %s | %s |" % (self.loot_source_label(page, tid), c, pct(it.get("chance")), cell(", ".join(it.get("notes") or []))))
            page.add("")

    def loot_source_label(self, page, tid):
        ns, path = tid.split(":", 1) if ":" in tid else ("minecraft", tid)
        parts = path.split("/")
        if parts[0] in ("entities", "entity") and len(parts) > 1:
            eid = "%s:%s" % (ns, "/".join(parts[1:]))
            return "Dropped by " + self.link(page.path, eid, "entity")
        if parts[0] == "blocks" and len(parts) > 1:
            return "Breaking " + self.link(page.path, "%s:%s" % (ns, "/".join(parts[1:])), "block")
        if parts[0] == "chests":
            return "Chest: %s (`%s`)" % (humanize(parts[-1]), tid)
        if parts[0] == "archaeology":
            return "Archaeology: %s" % humanize(parts[-1])
        if parts[0] == "gameplay":
            return "Gameplay: %s" % humanize(parts[-1])
        return "`%s`" % tid

    def usage(self, page, ident):
        uses = [r for r in self.recipes_in.get(ident, []) if (r.get("result") or {}).get("id") != ident]
        outs = OrderedDict()
        for r in uses:
            o = (r.get("result") or {}).get("id")
            if o:
                outs.setdefault(o, r)
        if not outs:
            return
        page.add("## Used in", "")
        page.add(", ".join(self.link(page.path, o, "item") for o in list(outs)[:60]) + (" and %d more" % (len(outs) - 60) if len(outs) > 60 else ""), "")

    def ing_cell(self, page, ing):
        if not ing:
            return " "
        if ing.get("fluid"):
            return "%s %s mB" % (humanize(ing["fluid"]), ing.get("amount") or "")
        items = ing.get("items") or []
        cnt = ing.get("count", 1)
        suffix = " x%s" % cnt if cnt and cnt != 1 else ""
        if ing.get("tag"):
            members = self.shared["tags"].get("item", {}).get(ing["tag"], [])
            first = members[0] if members else None
            ic = self.icon(page.path, first) if first else ""
            return "%s `#%s`%s" % (ic, ing["tag"], suffix)
        if items:
            ic = self.icon(page.path, items[0])
            return "%s %s%s" % (ic, self.link(page.path, items[0], "item"), suffix) + (" (or %d others)" % (len(items) - 1) if len(items) > 1 else "")
        return " "

    def recipe(self, page, r):
        kind = r.get("kind")
        res = r.get("result") or {}
        out = "%s %s" % (self.icon(page.path, res.get("id")), self.link(page.path, res.get("id"), "item")) if res.get("id") else "?"
        if res.get("count", 1) not in (1, None):
            out += " x%s" % res["count"]
        typ = RECIPE_TYPES.get(r.get("type"), humanize(r.get("type", "")))
        page.add("**%s** &rarr; %s" % (typ, out), "")
        if kind == "shaped":
            pat = r.get("pattern") or []
            width = max((len(p) for p in pat), default=0)
            page.add('<div class="recipe" markdown>', "")
            page.add("|" + " |" * width, "|" + "---|" * width)
            for row in pat:
                cells = []
                for ch in row.ljust(width):
                    cells.append(self.ing_cell(page, r["key"].get(ch)) if ch != " " else " ")
                page.add("| " + " | ".join(cells) + " |")
            page.add("", "</div>", "")
        else:
            ings = [i for i in r.get("ingredients") or [] if i]
            if ings:
                page.add("Ingredients: " + ", ".join(self.ing_cell(page, i) for i in ings), "")
            if r.get("molten"):
                page.add("Produces molten: " + ", ".join("%s x%s" % (humanize(x["id"]), x.get("count", 1)) for x in r["molten"]), "")
            if r.get("schematics"):
                page.add("Requires schematic: " + ", ".join(self.link(page.path, x, "item", icon=True) for x in r["schematics"]), "")
            ex = r.get("extras") or {}
            if ex:
                page.add("Details: " + ", ".join("%s %s" % (re.sub(r"(?<!^)([A-Z])", r" \1", k).replace("_", " ").lower(), cell(v)) for k, v in list(ex.items())[:6]), "")

    # -------------------------------------------------------------- mobs
    def render_mobs(self, mod):
        slug = mod["mod"]["slug"]
        mobs = mod["categories"]["mobs"]
        index = Page("%s/mobs/index.md" % slug, "Mobs")
        index.add("# Mobs", "")
        self.breadcrumb(index, mod)
        bosses = [m for m in mobs if (m.get("info") or {}).get("boss")]
        index.add("%s adds **%d** mobs%s." % (esc(mod["mod"]["name"]), len(mobs), (", including %d bosses" % len(bosses)) if bosses else ""), "")
        groups = defaultdict(list)
        for m in mobs:
            groups["Bosses" if (m.get("info") or {}).get("boss") else (m.get("info") or {}).get("category") or "Other"].append(m)
        for g in sorted(groups, key=lambda g: (g != "Bosses", g)):
            index.add("## %s" % g.replace("_", " ").title(), "")
            index.add("| Mob | Health | Attack | EP (magicule) |", "|---|---|---|---|")
            for m in sorted(groups[g], key=lambda m: m["name"].lower()):
                at = (m.get("info") or {}).get("attributes") or {}
                ex = m.get("existence") or {}
                ep = ("%s - %s" % (num(ex.get("min_magicule")), num(ex.get("max_magicule")))) if ex.get("max_magicule") else ""
                index.add("| %s | %s | %s | %s |" % (self.link(index.path, m["id"], "entity"), cell(num(at.get("Health", "")) if at.get("Health") is not None else ""),
                                                    cell(num(at.get("Attack damage")) if at.get("Attack damage") is not None else ""), ep))
            index.add("")
            for m in groups[g]:
                self.render_mob(mod, m, g)
        self.write(index)
        return index.path

    def render_mob(self, mod, m, group):
        page = Page(self.entry_path(mod, "mobs", m["id"]), m["name"])
        page.add("# %s" % esc(m["name"]), "")
        self.breadcrumb(page, mod, "mobs", group.replace("_", " ").title())
        info = m.get("info") or {}
        at = info.get("attributes") or {}
        ex = m.get("existence") or {}
        rows = [("ID", "`%s`" % m["id"]), ("Type", "Boss" if info.get("boss") else (info.get("category") or "").replace("_", " ").title())]
        for k in ("Health", "Attack damage", "Armor", "Armor toughness", "Speed", "Follow range", "Knockback resistance"):
            if k in at:
                rows.append((k, cell(num(at[k]) if isinstance(at[k], (int, float)) else at[k])))
        if ex.get("max_magicule"):
            rows.append(("Magicule (EP)", "%s - %s" % (num(ex.get("min_magicule")), num(ex.get("max_magicule")))))
        if ex.get("max_aura"):
            rows.append(("Aura", "%s - %s" % (num(ex.get("min_aura")), num(ex.get("max_aura")))))
        if ex.get("spiritual_health"):
            rows.append(("Spiritual health", num(ex["spiritual_health"])))
        if info.get("size"):
            rows.append(("Hitbox", "%s x %s blocks" % (num(info["size"][0]), num(info["size"][1]))))
        if info.get("fire_immune"):
            rows.append(("Fire immune", "Yes"))
        if m.get("spawn_egg"):
            rows.append(("Spawn egg", self.link(page.path, m["spawn_egg"], "item", icon=True)))
        self.infobox(page, self.refs.get(m.get("spawn_egg") or "", {}).get("icon"), rows, m["name"])
        if ex.get("abilities"):
            page.add("## Abilities", "")
            page.add("This mob has these skills (and they can be obtained from it, for example with Predator-type skills):", "")
            for a in ex["abilities"]:
                page.add("- %s %s" % (self.icon(page.path, a), self.link(page.path, a, "skill")))
            page.add("")
        if m.get("spawns"):
            page.add("## Spawning", "")
            page.add("| Biomes | Weight | Group size |", "|---|---|---|")
            for s in m["spawns"]:
                page.add("| %s | %s | %s-%s |" % (self.biome_list(page, s.get("biomes")), s.get("weight"), s.get("min"), s.get("max")))
            page.add("")
        if m.get("drops"):
            page.add("## Drops", "")
            self.loot_table(page, m["drops"])
        if m.get("tags"):
            page.add("## Tags", "")
            page.add(", ".join("`%s`" % t for t in m["tags"]), "")
        self.write(page)

    def biome_list(self, page, b):
        if isinstance(b, str):
            if b.startswith("#"):
                members = self.shared["tags"].get("worldgen/biome", {}).get(b[1:], [])
                if members:
                    return cell(", ".join(self.name_of(x) for x in members[:12]) + (" +%d more" % (len(members) - 12) if len(members) > 12 else ""))
                return "`%s`" % b
            return self.link(page.path, b, "biome")
        if isinstance(b, list):
            return ", ".join(self.biome_list(page, x) for x in b)
        return "?"

    # ----------------------------------------------------------- effects
    def render_effects(self, mod):
        slug = mod["mod"]["slug"]
        effs = mod["categories"]["effects"]
        index = Page("%s/effects/index.md" % slug, "Effects")
        index.add("# Effects", "")
        self.breadcrumb(index, mod)
        index.add("Status effects added by %s." % esc(mod["mod"]["name"]), "")
        index.add("| | Effect | Type | Description |", "|---|---|---|---|")
        for e in sorted(effs, key=lambda e: e["name"].lower()):
            index.add("| %s | %s | %s | %s |" % (self.icon(index.path, e["id"]), self.link(index.path, e["id"], "effect"), cell(e.get("category") or ""), cell(_short(e.get("description")))))
        index.add("")
        for e in effs:
            page = Page(self.entry_path(mod, "effects", e["id"]), e["name"])
            page.add("# %s" % esc(e["name"]), "")
            self.breadcrumb(page, mod, "effects")
            self.infobox(page, e.get("icon_url"), [("ID", "`%s`" % e["id"]), ("Type", e.get("category")),
                                                   ("Color", "`%s`" % e["color"] if e.get("color") else None)], e["name"])
            if e.get("description"):
                page.add("> %s" % para(e["description"]).replace("\n", "\n> "), "")
            if e.get("attributes"):
                page.add("## Attribute changes (per level)", "")
                page.add("| Attribute | Amount | Operation |", "|---|---|---|")
                for a in e["attributes"]:
                    page.add("| %s | %s | %s |" % (cell(a["attribute"]), cell(a["amount"]), cell(_op(a["operation"]))))
                page.add("")
            rv = self.reverse.get(e["id"], {})
            if rv.get("applied_by"):
                page.add("## Applied by", "")
                page.add(self.links(page.path, rv["applied_by"], "skill"), "")
            self.write(page)
        self.write(index)
        return index.path

    # ------------------------------------------------------ enchantments
    def render_enchantments(self, mod):
        slug = mod["mod"]["slug"]
        ens = mod["categories"]["enchantments"]
        index = Page("%s/enchantments/index.md" % slug, "Enchantments")
        index.add("# Enchantments", "")
        self.breadcrumb(index, mod)
        index.add("Enchantments added by %s. You can find them as enchanted books or apply them at an enchanting table or anvil." % esc(mod["mod"]["name"]), "")
        index.add("| Enchantment | Max level | Weight | Applies to |", "|---|---|---|---|")
        for e in sorted(ens, key=lambda e: e["name"].lower()):
            index.add("| %s | %s | %s | %s |" % (self.link(index.path, e["id"], "enchantment"), e.get("max_level") or "", e.get("weight") or "", cell(_tagname(e.get("supported_items")))))
        index.add("")
        for e in ens:
            page = Page(self.entry_path(mod, "enchantments", e["id"]), e["name"])
            page.add("# %s" % esc(e["name"]), "")
            self.breadcrumb(page, mod, "enchantments")
            rows = [("ID", "`%s`" % e["id"]), ("Max level", e.get("max_level")), ("Weight (rarity)", e.get("weight")),
                    ("Anvil cost", e.get("anvil_cost")), ("Slots", ", ".join(e.get("slots") or []) if e.get("slots") else None),
                    ("Applies to", cell(_tagname(e.get("supported_items")))), ("Primary items", cell(_tagname(e.get("primary_items")))),
                    ("Incompatible with", cell(_tagname(e.get("exclusive_set"))))]
            self.infobox(page, None, [(k, str(v) if v is not None else None) for k, v in rows], e["name"])
            if e.get("description"):
                page.add("> %s" % para(e["description"]).replace("\n", "\n> "), "")
            if e.get("effects"):
                page.add("## Effects", "")
                page.add("| Component | Effect | Value |", "|---|---|---|")
                for x in e["effects"]:
                    page.add("| `%s` | %s | %s |" % (x["component"], cell((x.get("type") or "").split(":")[-1].replace("_", " ")), cell(x.get("value") or "")))
                page.add("")
            sup = e.get("supported_items")
            if isinstance(sup, str) and sup.startswith("#"):
                members = self.shared["tags"].get("item", {}).get(sup[1:], [])
                if members:
                    page.add("## Compatible items", "")
                    page.add(self.links(page.path, members, "item", limit=60), "")
            self.write(page)
        self.write(index)
        return index.path

    # ---------------------------------------------------------- worldgen
    def render_biomes(self, mod):
        slug = mod["mod"]["slug"]
        bs = mod["categories"]["biomes"]
        index = Page("%s/biomes/index.md" % slug, "Biomes")
        index.add("# Biomes", "")
        self.breadcrumb(index, mod)
        index.add("| Biome | Temperature | Rain/Snow | Spawns |", "|---|---|---|---|")
        for b in sorted(bs, key=lambda b: b["name"].lower()):
            index.add("| %s | %s | %s | %d |" % (self.link(index.path, b["id"], "biome"), b.get("temperature"), "Yes" if b.get("precipitation") else "No", len(b.get("spawns") or [])))
        index.add("")
        for b in bs:
            page = Page(self.entry_path(mod, "biomes", b["id"]), b["name"])
            page.add("# %s" % esc(b["name"]), "")
            self.breadcrumb(page, mod, "biomes")
            rows = [("ID", "`%s`" % b["id"]), ("Temperature", b.get("temperature")), ("Downfall", b.get("downfall")),
                    ("Precipitation", "Yes" if b.get("precipitation") else "No")]
            for k, v in (b.get("colors") or {}).items():
                if isinstance(v, int):
                    rows.append((k.replace("_", " ").title(), "`#%06X`" % v))
            self.infobox(page, None, [(k, str(v) if v is not None else None) for k, v in rows], b["name"])
            dims = [d for mm in self.mods for d in mm["categories"].get("dimensions", []) if b["id"] in d.get("biomes", [])]
            if dims:
                page.add("Found in: " + ", ".join(self.link(page.path, d["id"], "dimension") for d in dims), "")
            if b.get("spawns"):
                page.add("## Mob spawns", "")
                page.add("| Mob | Group | Weight | Group size |", "|---|---|---|---|")
                for s in b["spawns"]:
                    page.add("| %s | %s | %s | %s-%s |" % (self.link(page.path, s["type"], "entity"), s["group"], s.get("weight"), s.get("min"), s.get("max")))
                page.add("")
            self.write(page)
        self.write(index)
        return index.path

    def render_dimensions(self, mod):
        slug = mod["mod"]["slug"]
        ds = mod["categories"]["dimensions"]
        index = Page("%s/dimensions/index.md" % slug, "Dimensions")
        index.add("# Dimensions", "")
        self.breadcrumb(index, mod)
        index.add("| Dimension | Biomes |", "|---|---|")
        for d in ds:
            index.add("| %s | %s |" % (self.link(index.path, d["id"], "dimension"), self.links(index.path, d.get("biomes", []), "biome", limit=6)))
        index.add("")
        for d in ds:
            page = Page(self.entry_path(mod, "dimensions", d["id"]), d["name"])
            page.add("# %s" % esc(d["name"]), "")
            self.breadcrumb(page, mod, "dimensions")
            rows = [("ID", "`%s`" % d["id"]), ("Dimension type", "`%s`" % d.get("type") if d.get("type") else None),
                    ("Generator", "`%s`" % d.get("generator") if d.get("generator") else None)]
            for k, v in (d.get("properties") or {}).items():
                rows.append((k.replace("_", " ").capitalize(), str(v)))
            self.infobox(page, None, rows, d["name"])
            if d.get("biomes"):
                page.add("## Biomes", "")
                page.add(self.links(page.path, d["biomes"], "biome"), "")
            self.write(page)
        self.write(index)
        return index.path

    def render_structures(self, mod):
        slug = mod["mod"]["slug"]
        ss = mod["categories"]["structures"]
        index = Page("%s/structures/index.md" % slug, "Structures")
        index.add("# Structures", "")
        self.breadcrumb(index, mod)
        index.add("| Structure | Biomes | Spacing |", "|---|---|---|")
        for s in sorted(ss, key=lambda s: s["name"].lower()):
            pl = s.get("placement") or {}
            index.add("| %s | %s | %s |" % (self.link(index.path, s["id"], "structure"), self.biome_list(index, s.get("biomes")),
                                           ("%s chunks" % pl["spacing"]) if pl.get("spacing") else ""))
        index.add("")
        for s in ss:
            page = Page(self.entry_path(mod, "structures", s["id"]), s["name"])
            page.add("# %s" % esc(s["name"]), "")
            self.breadcrumb(page, mod, "structures")
            pl = s.get("placement") or {}
            rows = [("ID", "`%s`" % s["id"]), ("Type", "`%s`" % s.get("type") if s.get("type") else None),
                    ("Biomes", self.biome_list(page, s.get("biomes"))), ("Generation step", s.get("step")),
                    ("Spacing / separation", ("%s / %s chunks" % (pl.get("spacing"), pl.get("separation"))) if pl.get("spacing") else None),
                    ("Terrain adaptation", s.get("terrain_adaptation")),
                    ("Size (jigsaw depth)", s.get("size"))]
            self.infobox(page, None, [(k, str(v) if v is not None else None) for k, v in rows], s["name"])
            chests = [tid for tid in self.shared["loot"] if tid.split(":")[0] == s["ns"] and "chests/" in tid and s["path"].split("/")[0] in tid]
            if chests:
                page.add("## Loot", "")
                for tid in sorted(chests):
                    page.add("### `%s`" % tid, "")
                    self.loot_table(page, self.shared["loot"][tid]["pools"])
            self.write(page)
        self.write(index)
        return index.path

    # ---------------------------------------------------------- gateways
    def render_gateways(self, mod):
        slug = mod["mod"]["slug"]
        gates = mod["extra"]["gateways"]
        index = Page("%s/gateways/index.md" % slug, "Gateways")
        index.add("# Gateways", "")
        self.breadcrumb(index, mod)
        index.add("A Gateway is opened by using a **Gate Pearl** for that gateway. Survive every wave to collect the rewards. "
                  "Each gateway below lists its waves, the enemies, the stat boosts they get and the rewards.", "")
        index.add("| Gateway | Size | Waves |", "|---|---|---|")
        for g in gates:
            d = g["data"]
            index.add("| %s | %s | %s |" % (self.link(index.path, g["id"]), cell(d.get("size", "")), len(d.get("waves") or []) or ("endless" if "endless" in g["id"] else "")))
        index.add("")
        for g in gates:
            d = g["data"]
            page = Page(self.entry_path(mod, "gateways", g["id"]), g["name"])
            page.add("# %s" % esc(g["name"]), "")
            self.breadcrumb(page, mod, "gateways")
            rows = [("ID", "`%s`" % g["id"]), ("Size", d.get("size")), ("Color", "`%s`" % d.get("color") if d.get("color") else None),
                    ("Waves", str(len(d.get("waves") or [])) if d.get("waves") else None),
                    ("Leash range", str(d.get("leash_range") or (d.get("rules") or {}).get("leash_range") or "") or None)]
            self.infobox(page, None, rows, g["name"])
            waves = d.get("waves") or ([d.get("base_wave")] if d.get("base_wave") else [])
            for i, w in enumerate(waves, 1):
                page.add("## Wave %d" % i if d.get("waves") else "## Base wave", "")
                ents = ", ".join("%s x%s" % (self.link(page.path, e.get("entity") or e.get("type", "?"), "entity"), e.get("count", 1)) for e in w.get("entities") or [])
                if ents:
                    page.add("**Enemies:** " + ents, "")
                mods_ = w.get("modifiers") or []
                if mods_:
                    page.add("**Enemy boosts:** " + ", ".join("%s %s%s" % (m_.get("attribute", "?").split(":")[-1].replace("generic.", "").replace("_", " "),
                                                                           "+" if (m_.get("value") or 0) >= 0 else "", _gate_mod(m_)) for m_ in mods_), "")
                rw = w.get("rewards") or []
                if rw:
                    page.add("**Rewards:** " + "; ".join(self.gate_reward(page, r_) for r_ in rw), "")
                if w.get("max_wave_time"):
                    page.add("Time limit: %s s, setup time: %s s." % (num(w["max_wave_time"] / 20), num(w.get("setup_time", 0) / 20)), "")
            rw = d.get("rewards") or []
            if rw:
                page.add("## Completion rewards", "")
                for r_ in rw:
                    page.add("- " + self.gate_reward(page, r_))
                page.add("")
            fl = d.get("failures") or []
            if fl:
                page.add("## If you fail", "")
                for f in fl:
                    page.add("- %s" % cell(json.dumps(f)[:200]))
                page.add("")
            recs = [r for r in self.shared["recipes"] if r.get("type") == "gateways:gate_recipe" and g["id"] in json.dumps(r)]
            self.write(page)
        self.write(index)
        return index.path

    def gate_reward(self, page, r):
        t = (r.get("type") or "").split(":")[-1]
        if t == "stack":
            st = r.get("stack") or {}
            return "%s x%s" % (self.link(page.path, st.get("id") or st.get("item"), "item", icon=True), st.get("count", 1))
        if t == "stack_list":
            return ", ".join("%s x%s" % (self.link(page.path, s.get("id") or s.get("item"), "item", icon=True), s.get("count", 1)) for s in r.get("stacks") or [])
        if t == "entity_loot":
            return "%s rolls of %s loot" % (r.get("rolls"), self.link(page.path, r.get("entity"), "entity"))
        if t == "experience":
            return "%s experience" % r.get("experience")
        if t == "loot_table":
            return "%s rolls of loot table `%s`" % (r.get("rolls"), r.get("loot_table"))
        if t == "chanced":
            return "%s chance: %s" % (pct(r.get("chance")), self.gate_reward(page, r.get("reward") or {}))
        if t == "command":
            return "runs a command"
        return cell(json.dumps(r)[:120])

    # ------------------------------------------------------------- perks
    def render_perks(self, mod):
        slug = mod["mod"]["slug"]
        perks = mod["extra"]["perks"]
        page = Page("%s/perks/index.md" % slug, "Perks")
        page.add("# Perks", "")
        self.breadcrumb(page, mod)
        page.add("Perks are upgrades bought with Knowledge of Death points. Open the perk screen from the Tombstone menu to spend them.", "")
        page.add("| Perk | Description | Improves |", "|---|---|---|")
        for p in sorted(perks, key=lambda p: p["name"].lower()):
            page.add("| **%s** | %s | %s |" % (cell(p["name"]), cell(p.get("description") or ""), cell(", ".join(x for x in p.get("levels") or [] if x))))
        page.add("")
        self.write(page)
        return page.path

    # ------------------------------------------------------ advancements
    def render_advancements(self, mod):
        slug = mod["mod"]["slug"]
        adv = mod["categories"]["advancements"]
        page = Page("%s/advancements/index.md" % slug, "Advancements")
        page.add("# Advancements", "")
        self.breadcrumb(page, mod)
        page.add("%s has **%d** advancements." % (esc(mod["mod"]["name"]), len(adv)), "")
        trees = defaultdict(list)
        for a in adv:
            trees[a["id"].split(":")[1].split("/")[0] if "/" in a["id"] else "main"].append(a)
        for t, lst in sorted(trees.items()):
            if len(trees) > 1:
                page.add("## %s" % humanize(t), "")
            page.add("| | Advancement | Description | Type |", "|---|---|---|---|")
            for a in lst:
                ic = self.icon(page.path, a.get("icon")) if a.get("icon") else ""
                page.add("| %s | **%s** | %s | %s%s |" % (ic, cell(a.get("title") or a["id"]), cell(a.get("description") or ""), a.get("frame", "task").title(), " (hidden)" if a.get("hidden") else ""))
            page.add("")
        self.write(page)
        return page.path

    # ----------------------------------------------------------- commands
    def render_commands(self, mod):
        slug = mod["mod"]["slug"]
        c = mod["categories"]
        page = Page("%s/commands/index.md" % slug, "Commands")
        page.add("# Commands", "")
        self.breadcrumb(page, mod)
        cmds = c.get("commands") or []
        extra = self.content_file(slug, "commands.md")
        if extra:
            page.add(extra, "")
        if cmds:
            page.add("`<value>` is a required argument, `[value]` is optional. The permission column shows who can run it by default.", "")
            roots = OrderedDict()
            for cm in cmds:
                parts = cm["syntax"].split(" ")
                root = " ".join(parts[:2]) if len(parts) > 2 and not parts[1].startswith("<") else parts[0]
                roots.setdefault(root, []).append(cm)
            for root, lst in roots.items():
                page.add("## `%s`" % root, "")
                page.add("| Syntax | Permission |", "|---|---|")
                for cm in lst:
                    page.add("| `%s` | %s |" % (cm["syntax"].replace("|", "\\|"), PERM.get(cm.get("permission"), str(cm.get("permission")))))
                page.add("")
        grs = c.get("gamerules") or []
        if grs:
            page.add("## Game rules", "")
            page.add("Change these with `/gamerule <name> <value>`.", "")
            page.add("| Game rule | Default | Description |", "|---|---|---|")
            for g in grs:
                page.add("| `%s` | %s | %s |" % (g["name"], cell(_fmtval(g.get("default")).strip('"')), cell(g.get("description") or g.get("title") or "")))
            page.add("")
        msgs = c.get("command_messages") or []
        if msgs:
            page.add("## Command feedback messages", "")
            page.add('<details markdown><summary>Show %d messages</summary>' % len(msgs), "")
            page.add("| Key | Message |", "|---|---|")
            for m_ in msgs:
                page.add("| `%s` | %s |" % (m_["key"], cell(m_["text"])))
            page.add("", "</details>", "")
        self.write(page)
        return page.path

    # ------------------------------------------------------------ configs
    def render_configs(self, mod):
        slug = mod["mod"]["slug"]
        oids = mod["categories"]["configs"]
        files = OrderedDict()
        for oid in oids:
            o = self.options[oid]
            files.setdefault(o.get("file") or "?", []).append(o)
        index = Page("%s/configs/index.md" % slug, "Configs")
        index.add("# Configs", "")
        self.breadcrumb(index, mod)
        index.add("Every config option %s defines, with its default value. Files under `config/` are shared by the whole instance; "
                  "files under `serverconfig/` live inside each world's folder (put copies in `defaultconfigs/` to apply them to new worlds)." % esc(mod["mod"]["name"]), "")
        if any(o in self.overrides for o in oids):
            index.add("> [!NOTE]", "> Values this pack changes are shown in the **This pack** column of each table.", "")
        index.add("| File | Options |", "|---|---|")
        nav = [{"All config files": index.path}]
        for f, lst in sorted(files.items()):
            n = len([o for o in lst if o.get("key") is not None])
            p = "%s/configs/%s.md" % (slug, slugify(f.replace("/", "-").replace(".toml", "")))
            index.add("| [`%s`](%s) | %d |" % (f, self.rel(index.path, p), n))
            self.render_config_file(mod, f, lst, p)
        index.add("")
        self.write(index)
        return nav

    def render_config_file(self, mod, f, lst, path):
        page = Page(path, f)
        page.add("# `%s`" % f, "")
        self.breadcrumb(page, mod, "configs")
        sections = OrderedDict()
        comments = {}
        for o in lst:
            key = tuple(o.get("path") or [])
            if o.get("key") is None:
                if o.get("section_comment"):
                    comments[key] = o["section_comment"]
                continue
            sections.setdefault(key, []).append(o)
        has_pack = any(o["oid"] in self.overrides for o in lst)
        for sec, opts in sections.items():
            page.add("## `[%s]`" % ".".join(sec) if sec else "## Top level", "")
            if comments.get(sec):
                page.add(para(comments[sec]), "")
            page.add("| Option | Default |" + (" This pack |" if has_pack else "") + " Range | Description |", "|---|---|" + ("---|" if has_pack else "") + "---|---|")
            for o in opts:
                pv = (" %s |" % cell(_fmtval(self.overrides[o["oid"]])) if o["oid"] in self.overrides else " |") if has_pack else ""
                page.add("| `%s` | %s |%s %s | %s |" % (o["key"], cell(_fmtval(o.get("default"))), pv, cell(_range(o).strip(" ()")), cell(o.get("comment") or "")))
            page.add("")
        self.write(page)

    # ----------------------------------------------------------- mechanics
    def render_guidebooks(self, mod):
        slug = mod["mod"]["slug"]
        nav = []
        for book in mod.get("guidebooks") or []:
            bslug = slugify(book["id"].split(":")[-1])
            index = Page("%s/mechanics/%s/index.md" % (slug, bslug), book["name"])
            index.add("# %s" % esc(book["name"]), "")
            self.breadcrumb(index, mod, "mechanics")
            index.add("This is the text of the in-game guide book **%s**, one page per chapter." % esc(book["name"]), "")
            if book.get("landing"):
                index.add(para(book["landing"]), "")
            index.add("| Chapter | Entries | About |", "|---|---|---|")
            bnav = [{"Contents": index.path}]
            for c in book["categories"]:
                if not c["entries"]:
                    continue
                cp = Page("%s/mechanics/%s/%s.md" % (slug, bslug, slugify(c["name"] or c["id"])), c["name"])
                index.add("| [%s](%s) | %d | %s |" % (esc(c["name"]), self.rel(index.path, cp.path), len(c["entries"]), cell(_short(c.get("description"), 140))))
                cp.add("# %s" % esc(c["name"]), "")
                cp.add("<small>[%s](%s) &rsaquo; [%s](%s)</small>" % (esc(mod["mod"]["name"]), self.rel(cp.path, "%s/index.md" % slug),
                                                                     esc(book["name"]), self.rel(cp.path, index.path)), "")
                if c.get("description"):
                    cp.add(para(c["description"]), "")
                for e in c["entries"]:
                    ic = self.icon(cp.path, e["icon"]) if isinstance(e.get("icon"), str) else ""
                    cp.add("## %s %s" % (ic, esc(e["name"] or "")) if ic else "## %s" % esc(e["name"] or ""), "")
                    for pg in e["pages"]:
                        if pg.get("title"):
                            cp.add("**%s**" % esc(pg["title"]), "")
                        if pg.get("item") and isinstance(pg["item"], str):
                            it = pg["item"].split("{")[0].split(",")[0]
                            cp.add(self.link(cp.path, it, "item", icon=True), "")
                        if pg.get("text"):
                            cp.add(_book_md(pg["text"]), "")
                        if pg.get("recipe") and isinstance(pg["recipe"], str):
                            cp.add("*Recipe:* `%s`" % pg["recipe"], "")
                self.write(cp)
                bnav.append({c["name"]: cp.path})
            index.add("")
            self.write(index)
            nav.append({book["name"]: bnav})
        return nav

    def render_mechanics(self, mod):
        slug = mod["mod"]["slug"]
        body = self.content_file(slug, "mechanics.md")
        if not body:
            return None
        page = Page("%s/mechanics/index.md" % slug, "Mechanics")
        if not body.lstrip().startswith("# "):
            page.add("# Mechanics", "")
        self.breadcrumb(page, mod)
        page.add(self.expand_content(page, body), "")
        self.write(page)
        return page.path

    def mod_lang(self, slug):
        if not hasattr(self, "_lang"):
            self._lang = {}
        if slug not in self._lang:
            p = os.path.join(self.data_dir, "lang", slug + ".json")
            self._lang[slug] = json.load(open(p, encoding="utf-8")) if os.path.isfile(p) else {}
        return self._lang[slug]

    def expand_content(self, page, body):
        """Hand-written pages may use {{link:ns:id}}, {{cfg:file|path.key}} placeholders."""
        def link(m):
            return self.link(page.path, m.group(1))

        def cfg(m):
            f, k = m.group(1), m.group(2)
            for o in self.options:
                if o.get("file") == f and ".".join(list(o.get("path") or []) + [o.get("key") or ""]) == k:
                    return _fmtval(self.overrides.get(o["oid"], o.get("default"))).strip('"')
            return "?"
        def langtable(m):
            rx, label = m.group(1), (m.group(2) or "Entry")
            lang = self.mod_lang(page.path.split("/")[0])
            rows = []
            for k in sorted(lang):
                mm = re.fullmatch(rx, k)
                if mm:
                    name = mm.group(1) if mm.groups() else k
                    rows.append("| %s | %s |" % (cell(name.replace("_", " ").replace(".", " / ").title()), cell(lang[k])))
            if not rows:
                return ""
            return "\n".join(["| %s | Details |" % label, "|---|---|"] + rows)

        def langlist(m):
            rx = m.group(1)
            lang = self.mod_lang(page.path.split("/")[0])
            return "\n".join("- %s" % esc(lang[k]).replace("\n", " ") for k in sorted(lang) if re.fullmatch(rx, k))
        def gamerule(m):
            for mm in self.mods:
                for g in mm["categories"].get("gamerules") or []:
                    if g["name"] == m.group(1):
                        return _fmtval(g.get("default")).strip('"')
            return "?"
        body = re.sub(r"\{\{gamerule:([A-Za-z0-9_]+)\}\}", gamerule, body)
        body = re.sub(r"\{\{langtable:([^|}]+)(?:\|([^}]+))?\}\}", langtable, body)
        body = re.sub(r"\{\{langlist:([^}]+)\}\}", langlist, body)
        body = re.sub(r"\{\{link:([a-z0-9_.-]+:[a-z0-9_./-]+)\}\}", link, body)
        body = re.sub(r"\{\{cfg:([^|}]+)\|([^}]+)\}\}", cfg, body)
        body = re.sub(r"\]\(@/([^)]+)\)", lambda m: "](%s)" % self.rel(page.path, m.group(1)), body)
        return body

    # ------------------------------------------------------------- home
    def render_home(self):
        page = Page("index.md", "Home")
        intro = self.content_file("", "home.md") or "# Adam's Batch Modpack Wiki"
        page.add(self.expand_content(page, intro), "")
        page.add("## Mods", "")
        for group in GROUPS:
            page.add("### %s" % group, "")
            page.add("| Mod | Version | What's inside |", "|---|---|---|")
            for mod in self.mods:
                m = mod["mod"]
                if m["group"] != group:
                    continue
                c = mod["categories"]
                bits = []
                for cat in ("abilities", "races", "items", "blocks", "mobs", "effects", "enchantments"):
                    if c.get(cat):
                        bits.append("%s %s" % (num(len(c[cat])), CAT_TITLES[cat].lower()))
                if (mod.get("extra") or {}).get("gateways"):
                    bits.append("%d gateways" % len(mod["extra"]["gateways"]))
                page.add("| **[%s](%s/index.md)** | %s | %s |" % (esc(m["name"]), m["slug"], esc((m.get("meta") or {}).get("version") or ""), ", ".join(bits)))
            page.add("")
        total = sum(len(mod["categories"].get(c, [])) for mod in self.mods for c in ("abilities", "races", "items", "blocks", "mobs", "effects", "enchantments"))
        page.add("*%s documented entries across %d mods, generated from the mod files themselves.*" % (num(total), len(self.mods)), "")
        self.write(page)

    def render_pack_notes_page(self):
        page = Page("pack-notes.md", "Pack notes")
        body = self.content_file("", "pack-notes.md")
        page.add(self.expand_content(page, body) if body else "# Pack notes", "")
        if self.overrides:
            page.add("## Config values changed by this pack", "")
            page.add("| Mod | File | Option | This pack | Mod default |", "|---|---|---|---|---|")
            for oid, val in sorted(self.overrides.items()):
                o = self.options[oid]
                modname = next((mm["mod"]["name"] for mm in self.mods if mm["mod"]["slug"] == o.get("mod")), o.get("mod"))
                page.add("| %s | `%s` | `%s` | %s | %s |" % (esc(modname), o["file"], ".".join(list(o.get("path") or []) + [o["key"]]), cell(_fmtval(val)), cell(_fmtval(o.get("default")))))
            page.add("")
        else:
            page.add("> [!NOTE]", "> No pack config files have been added yet, so every page shows the mods' default values. "
                     "See [About this wiki](about.md) for how to add the pack's `config/` folder and regenerate.", "")
        self.write(page)

    def render_about(self):
        page = Page("about.md", "About this wiki")
        body = self.content_file("", "about.md")
        page.add(self.expand_content(page, body) if body else "# About this wiki", "")
        page.add("## Mod versions documented", "")
        page.add("| Mod | Version | File |", "|---|---|---|")
        for mod in self.mods:
            meta = mod["mod"].get("meta") or {}
            page.add("| %s | %s | `%s` |" % (esc(mod["mod"]["name"]), esc(meta.get("version") or ""), meta.get("jar") or ""))
        page.add("")
        self.write(page)


# ---------------------------------------------------------------- helpers
GROUP_BLURB = {
    "Ultimate Skills": "The most powerful tier of skills. Many are one-of-a-kind and evolve from Unique skills.",
    "Unique Skills": "Personal skills that shape a character. You usually start with one and can gain more through feats.",
    "Extra Skills": "Strong skills that can be learned, evolved from Common skills or granted by races.",
    "Common Skills": "Basic skills anyone can pick up, often from mobs.",
    "Intrinsic Skills": "Skills that come with a race.",
    "Resistance Skills": "Passive resistances and nullifications that reduce certain kinds of damage.",
    "Aspectual Magic": "Elemental magic cast with magicules through chants.",
    "Spiritual Magic": "Magic borrowed from spirits and elementals.",
    "Summoning Magic": "Magic that calls creatures or spirits to fight for you.",
    "Battlewill": "Martial arts powered by aura (AP) instead of magicules.",
}

TAG_SOURCES = {
    "found_in_tome": "Can be found in skill tomes",
    "hell_treasure_tome": "Can appear in Hell treasure tomes",
    "epic_tome_wizard_tower": "Can appear in epic tomes from wizard towers",
    "reset_with_race": "Removed and re-rolled when you change race",
}
for _t in ("common", "uncommon", "rare"):
    for _s in ("buried", "burnt", "frozen", "rotted", "ruined"):
        TAG_SOURCES["%s_tome_%s_wizard_tower" % (_t, _s)] = "Can appear in %s tomes in %s wizard towers" % (_t, _s)
for _t in ("low", "medium", "high", "great"):
    for _k in ("basic_tome", "rare_tome", "upgraded_tome", "manual"):
        TAG_SOURCES["%s_%s_dwarf_trade" % (_t, _k)] = "Sold by dwarf traders (%s %s)" % (_t, _k.replace("_", " "))

RELIC_LOOT = {"WILDCARD": "any chest", "OVERWORLD": "any Overworld chest", "NETHER_LIKE": "fire/Nether-themed chests (and ruined portals)",
              "THE_NETHER": "any Nether chest", "END_LIKE": "End and stronghold chests", "THE_END": "any End chest",
              "DESERT": "chests in desert biomes", "SAVANNA": "chests in savanna biomes", "FOREST": "chests in forest biomes",
              "MOUNTAIN": "chests in mountain biomes", "AQUATIC": "chests in ocean/river biomes", "TROPIC": "chests in jungle/tropical biomes",
              "TAIGA": "chests in taiga biomes", "PLAINS": "chests in plains biomes", "SWAMP": "chests in swamp biomes",
              "FROST": "chests in snowy biomes", "CAVE": "chests in cave biomes", "SCULK": "chests in the deep dark",
              "VILLAGE": "village and pillager chests", "BASTION": "bastion chests", "MINESHAFT": "mineshaft chests"}

RECIPE_TYPES = {
    "minecraft:crafting_shaped": "Crafting (shaped)", "minecraft:crafting_shapeless": "Crafting (shapeless)",
    "minecraft:smelting": "Smelting", "minecraft:blasting": "Blasting", "minecraft:smoking": "Smoking",
    "minecraft:campfire_cooking": "Campfire", "minecraft:stonecutting": "Stonecutter", "minecraft:smithing_transform": "Smithing Table",
    "tensura:refining": "Refining (Great Sage / Researcher)", "tensura:woodcutting": "Woodcutting", "tensura:smithing_bench": "Smithing Bench",
    "tensura:kiln_melting": "Kiln (melting)", "tensura:kiln_mixing": "Kiln (mixing)", "tensura:mining_station": "Mining Station",
    "tensura:smithing": "Tensura Smithing", "enigmaticlegacyplus:cursed_shaped": "Crafting (cursed)",
    "enigmaticlegacyplus:spellstone_table": "Spellstone Table", "gateways:gate_recipe": "Crafting (Gate Pearl)",
    "tombstone:disableable_shaped": "Crafting (shaped)", "tombstone:disableable_shapeless": "Crafting (shapeless)",
    "create:compacting": "Create: Compacting", "create:crushing": "Create: Crushing",
}


def _costcell(v):
    """Cost values without any number are config/formula names; point readers to the config table."""
    if not v:
        return ""
    v = str(v)
    if not re.search(r"\d", v) and not v.startswith("`"):
        return "*set by config (%s)*" % cell(v)
    return cell(v)


def _book_md(t):
    lines = []
    for l in t.split("\n"):
        l = l.rstrip()
        lines.append(esc(l).replace("\\*\\*", "**").replace("\\*", "*") if l else "")
    out = "\n".join(lines)
    out = re.sub(r"\n(?!\n|- )", "  \n", out)
    return out


def _short(s, n=160):
    if not s:
        return ""
    s = s.replace("\n", " ")
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "..."


def _op(op):
    return {"ADD_VALUE": "add", "ADD_MULTIPLIED_BASE": "add x base", "ADD_MULTIPLIED_TOTAL": "multiply total",
            "ADDITION": "add", "MULTIPLY_BASE": "add x base", "MULTIPLY_TOTAL": "multiply total"}.get(op, str(op).lower())


def _fmtval(v):
    if isinstance(v, list):
        if not v:
            return "[] (empty)"
        return ", ".join(_fmtval(x) for x in v[:20]) + (" ... (%d total)" % len(v) if len(v) > 20 else "")
    if isinstance(v, str):
        return v if v.startswith("`") else '"%s"' % v
    if v is None:
        return "-"
    return num(v)


def _range(o):
    lo, hi = o.get("min"), o.get("max")
    if lo is None and hi is None:
        if o.get("allowed"):
            return " (one of: %s)" % ", ".join(str(x) for x in o["allowed"][:12])
        return ""
    return " (%s to %s)" % (num(lo) if lo is not None else "?", num(hi) if hi is not None else "?")


def _same(a, b):
    if b is None:
        return True  # we couldn't read the default, so we can't claim the pack changed it
    if isinstance(b, str) and (b.startswith("`") or "(" in b):
        return True  # default is computed at runtime (e.g. a random seed); nothing to compare
    if isinstance(a, str) and isinstance(b, str):
        return a.strip().lower() == b.strip().lower()
    if isinstance(a, list) and isinstance(b, str):
        return _same(a, [x.strip() for x in b.split(",") if x.strip()])
    if isinstance(b, list) and isinstance(a, str):
        return _same([x.strip() for x in a.split(",") if x.strip()], b)
    if isinstance(a, bool) or isinstance(b, bool):
        return bool(a) == bool(b) if isinstance(a, bool) and isinstance(b, bool) else str(a).lower() == str(b).lower()
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        # float fields are written as 32-bit floats (0.06 -> 0.0599999986...)
        return abs(float(a) - float(b)) <= 1e-6 * max(1.0, abs(float(a)), abs(float(b)))
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(_same(x, y) for x, y in zip(a, b))
    return str(a) == str(b)


def _tagname(t):
    if not t:
        return ""
    if isinstance(t, list):
        return ", ".join(_tagname(x) for x in t)
    t = str(t)
    if t.startswith("#"):
        base = t[1:].split(":")[-1].split("/")[-1]
        return base.replace("_", " ").replace("enchantable", "").strip().title() or t
    return humanize(t)


def _gate_mod(m):
    op = m.get("operation", "")
    v = m.get("value", 0)
    if "multiplied" in op:
        return "%s%%" % num(round(v * 100, 2))
    return num(v)


def write_mkdocs(site: Site, path: str, site_url: str, repo: str):
    import yaml  # provided by mkdocs
    cfg = OrderedDict()
    lines = []
    lines.append("# Generated by tools/wikigen/render.py - edit mkdocs.base.yml instead.")
    base_path = os.path.join(os.path.dirname(path), "mkdocs.base.yml")
    with open(base_path, encoding="utf-8") as fh:
        base = fh.read()
    nav = yaml.safe_dump({"nav": site.nav}, sort_keys=False, allow_unicode=True, width=200)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n" + base.rstrip() + "\n\n" + nav)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data")
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--content", default="content")
    ap.add_argument("--pack", default="pack")
    ap.add_argument("--mkdocs", default="mkdocs.yml")
    a = ap.parse_args(argv)
    site = Site(a.data, a.docs, a.content, a.pack)
    site.run()
    write_mkdocs(site, a.mkdocs, "", "")
    print("wrote %d pages" % len(site.pages))


if __name__ == "__main__":
    main()
