"""Data-driven content shared by every mod: items, blocks, mobs, effects,
enchantments, recipes, loot tables, worldgen and advancements."""
from __future__ import annotations

import os
import re
from collections import defaultdict
from typing import Optional

from .resources import Resources, clean, load_json


def humanize(ident: str) -> str:
    p = ident.split(":")[-1].split("/")[-1]
    return p.replace("_", " ").title()


class Names:
    """Display names for any registry id, across every mod (falls back to a humanized id)."""

    def __init__(self, res: Resources):
        self.res = res

    def item(self, ident: str) -> str:
        ns, p = _split(ident)
        for k in ("item.%s.%s" % (ns, p), "block.%s.%s" % (ns, p), "%s.item.%s" % (ns, p), "%s.block.%s" % (ns, p)):
            v = self.res.tr(k)
            if v:
                return v
        return humanize(ident)

    def block(self, ident: str) -> str:
        ns, p = _split(ident)
        return self.res.tr("block.%s.%s" % (ns, p)) or self.res.tr("%s.block.%s" % (ns, p)) or self.item(ident)

    def entity(self, ident: str) -> str:
        ns, p = _split(ident)
        return self.res.tr("entity.%s.%s" % (ns, p)) or humanize(ident)

    def effect(self, ident: str) -> str:
        ns, p = _split(ident)
        return self.res.tr("effect.%s.%s" % (ns, p)) or humanize(ident)

    def enchantment(self, ident: str) -> str:
        ns, p = _split(ident)
        return self.res.tr("enchantment.%s.%s" % (ns, p)) or humanize(ident)

    def biome(self, ident: str) -> str:
        ns, p = _split(ident)
        return self.res.tr("biome.%s.%s" % (ns, p)) or humanize(ident)

    def skill(self, ident: str) -> str:
        ns, p = _split(ident)
        return self.res.tr("%s.skill.%s" % (ns, p)) or humanize(ident)

    def race(self, ident: str) -> str:
        ns, p = _split(ident)
        return self.res.tr("%s.race.%s" % (ns, p)) or humanize(ident)


def _split(ident: str):
    if ":" in ident:
        return ident.split(":", 1)
    return "minecraft", ident


# ------------------------------------------------------------------ lang scan
def lang_ids(res: Resources, jar_key: str, prefix: str, ns: str) -> list:
    """Ids for keys like 'item.<ns>.<id>' (exactly three dot parts) owned by a jar."""
    out = []
    pref = "%s.%s." % (prefix, ns)
    for k, owner in res.lang_owner.items():
        if owner != jar_key or not k.startswith(pref):
            continue
        rest = k[len(pref):]
        if "." in rest or not rest:
            continue
        out.append(rest)
    return sorted(set(out))


def lang_extras(res: Resources, key: str, exclude=()) -> list:
    """Lines for keys that extend a base key (tooltips, descriptions...)."""
    out = []
    pref = key + "."
    for k in res.lang:
        if k.startswith(pref) and not any(k.endswith(e) for e in exclude):
            out.append((k[len(pref):], res.tr(k)))
    return out


def asset_ids(res: Resources, jar_key: str, ns: str, sub: str) -> list:
    base = os.path.join(res.root, jar_key, "assets", ns, sub)
    out = []
    if not os.path.isdir(base):
        return out
    for dp, _d, files in os.walk(base):
        for fn in files:
            if fn.endswith(".json"):
                rel = os.path.relpath(os.path.join(dp, fn), base).replace("\\", "/")[:-5]
                out.append(rel)
    return sorted(out)


# ------------------------------------------------------------------- recipes
def _ingredient(obj):
    """Normalise an ingredient into {'items': [...]} or {'tag': ...}."""
    if obj is None:
        return None
    if isinstance(obj, list):
        items = []
        tags = []
        for o in obj:
            n = _ingredient(o)
            if n is None:
                continue
            items += n.get("items", [])
            if n.get("tag"):
                tags.append(n["tag"])
        r = {"items": items}
        if tags:
            r["tag"] = tags[0]
            r["tags"] = tags
        return r
    if isinstance(obj, str):
        return {"tag": obj[1:]} if obj.startswith("#") else {"items": [obj]}
    if isinstance(obj, dict):
        if "item" in obj:
            return {"items": [obj["item"]], "count": obj.get("count", 1)}
        if "tag" in obj:
            return {"tag": obj["tag"], "count": obj.get("count", 1)}
        if "id" in obj:
            return {"items": [obj["id"]], "count": obj.get("count", 1)}
        if "ingredient" in obj:
            n = _ingredient(obj["ingredient"])
            if n is not None:
                n["count"] = obj.get("count", 1)
            return n
        if obj.get("type") in ("neoforge:compound",) and "children" in obj:
            return _ingredient(obj["children"])
        if "fluid" in obj or "fluid_tag" in obj:
            return {"fluid": obj.get("fluid") or obj.get("fluid_tag"), "amount": obj.get("amount")}
    return None


def _result(obj):
    if obj is None:
        return None
    if isinstance(obj, str):
        return {"id": obj, "count": 1}
    if isinstance(obj, dict):
        ident = obj.get("id") or obj.get("item")
        if isinstance(ident, dict):
            ident = ident.get("id") or ident.get("item")
        if ident:
            return {"id": ident, "count": obj.get("count", obj.get("Count", 1)), "chance": obj.get("chance")}
    if isinstance(obj, list):
        rs = [_result(o) for o in obj]
        rs = [r for r in rs if r]
        return rs[0] if rs else None
    return None


def parse_recipe(rid: str, d: dict) -> Optional[dict]:
    t = d.get("type", "")
    if not t:
        return None
    if ":" not in t:
        t = "minecraft:" + t
    r = {"id": rid, "type": t}
    if d.get("neoforge:conditions") or d.get("conditions"):
        r["conditional"] = True
    if t.endswith("crafting_shaped") or t.endswith("cursed_shaped") or t.endswith("disableable_shaped") or ("pattern" in d and "key" in d):
        pattern = d.get("pattern", [])
        key = {k: _ingredient(v) for k, v in (d.get("key") or {}).items()}
        r.update(kind="shaped", pattern=pattern, key=key, result=_result(d.get("result")))
    elif "ingredients" in d and ("result" in d or "output" in d) and (t.endswith("shapeless") or t.endswith("shapeless_no_remain")):
        r.update(kind="shapeless", ingredients=[_ingredient(i) for i in d.get("ingredients", [])], result=_result(d.get("result")))
    elif t in ("minecraft:smelting", "minecraft:blasting", "minecraft:smoking", "minecraft:campfire_cooking"):
        r.update(kind="cooking", ingredients=[_ingredient(d.get("ingredient"))], result=_result(d.get("result")),
                 experience=d.get("experience"), time=d.get("cookingtime"))
    elif t == "minecraft:stonecutting":
        r.update(kind="stonecutting", ingredients=[_ingredient(d.get("ingredient"))], result=_result(d.get("result")))
    elif t == "minecraft:smithing_transform":
        r.update(kind="smithing", ingredients=[_ingredient(d.get("template")), _ingredient(d.get("base")), _ingredient(d.get("addition"))],
                 result=_result(d.get("result")))
    else:
        # generic / modded: collect anything that looks like input/output
        ins = []
        for k in ("ingredients", "inputs", "ingredient", "base", "addition", "template", "catalyst", "item", "items", "input_items"):
            v = d.get(k)
            if v is None:
                continue
            if isinstance(v, list):
                for x in v:
                    if isinstance(x, dict) and isinstance(x.get("type"), dict):
                        ing = _ingredient(x["type"])
                        if ing is not None:
                            ing["count"] = x.get("amount", x.get("count", 1))
                        ins.append(ing)
                    else:
                        ins.append(_ingredient(x))
            else:
                ins.append(_ingredient(v))
        # Tensura style: input, input1, input2 ... with inputAmountN / left + left_count
        for k in sorted(d):
            mm = re.fullmatch(r"input(\d*)", k)
            if mm:
                ing = _ingredient(d[k])
                if ing is not None:
                    cnt = d.get("inputAmount" + mm.group(1)) or d.get(k + "_count") or ing.get("count", 1)
                    ing["count"] = cnt
                    ins.append(ing)
        for k in ("left", "right", "first_input", "second_input", "leftInput", "rightInput", "left_input", "right_input", "mix", "fuel"):
            if k in d:
                ing = _ingredient(d[k])
                if ing is not None:
                    ing["count"] = d.get(k + "_count", ing.get("count", 1))
                    ins.append(ing)
        if d.get("schematics"):
            r["schematics"] = [x for x in d["schematics"] if isinstance(x, str)]
        molten = []
        for k in ("primary", "secondary"):
            if isinstance(d.get(k), str):
                molten.append({"id": d[k], "count": d.get(k + "_count", 1)})
        if molten:
            r["molten"] = molten
        res = None
        for k in ("result", "output", "results", "outputs", "output_item"):
            if k in d:
                res = _result(d[k])
                if res:
                    break
        extras = {}
        for k, v in d.items():
            if k in ("type", "ingredients", "inputs", "input", "ingredient", "result", "output", "results", "outputs", "neoforge:conditions", "conditions", "key", "pattern", "category", "group", "schematics", "primary", "secondary", "primary_count", "secondary_count", "left_count", "right_count") or re.fullmatch(r"input(Amount)?\d*", k):
                continue
            if isinstance(v, (int, float, str, bool)):
                extras[k] = v
        r.update(kind="custom", ingredients=[i for i in ins if i], result=res, extras=extras)
    return r


def load_recipes(res: Resources) -> list:
    out = []
    seen = set()
    for key in res.keys:
        for sub in ("recipe", "recipes"):
            for ns, rel, full in res.data_files(key, sub):
                rid = "%s:%s" % (ns, rel)
                if rid in seen:
                    continue
                try:
                    d = load_json(full)
                except Exception:
                    continue
                if not isinstance(d, dict):
                    continue
                r = parse_recipe(rid, d)
                if r is None:
                    continue
                r["jar"] = key
                seen.add(rid)
                out.append(r)
    return out


def recipe_items(r) -> tuple:
    """(outputs, inputs) item ids of a normalised recipe (tags as '#tag')."""
    outs = []
    if r.get("result") and r["result"].get("id"):
        outs.append(r["result"]["id"])
    ins = []
    ings = list(r.get("ingredients") or []) + list((r.get("key") or {}).values())
    for ing in ings:
        if not ing:
            continue
        ins += ing.get("items", [])
        if ing.get("tag"):
            ins.append("#" + ing["tag"])
    return outs, ins


# -------------------------------------------------------------------- loot
def _num(v):
    if isinstance(v, (int, float)):
        return v, v
    if isinstance(v, dict):
        t = v.get("type", "minecraft:uniform")
        if "min" in v and "max" in v:
            a, _ = _num(v["min"])
            _, b = _num(v["max"])
            return a, b
        if "value" in v:
            return _num(v["value"])
        if t.endswith("binomial"):
            n, _ = _num(v.get("n", 1))
            return 0, n
    return 1, 1


def _entry_items(e, depth=0) -> list:
    """(item, weight, count_range, chance_modifier, conditions) tuples from a loot entry."""
    out = []
    t = e.get("type", "minecraft:item")
    w = e.get("weight", 1)
    cond_chance = 1.0
    notes = []
    for c in e.get("conditions", []) or []:
        ct = c.get("condition", "")
        if ct.endswith("random_chance"):
            ch = c.get("chance", 1)
            cond_chance *= ch if isinstance(ch, (int, float)) else 1
        elif ct.endswith("random_chance_with_enchanted_bonus") or ct.endswith("random_chance_with_looting"):
            ch = c.get("unenchanted_chance", c.get("chance", 1))
            cond_chance *= ch if isinstance(ch, (int, float)) else 1
            notes.append("Looting increases the chance")
        elif ct.endswith("killed_by_player"):
            notes.append("Must be killed by a player")
        elif ct.endswith("match_tool"):
            notes.append("Needs a specific tool")
        elif ct:
            notes.append(ct.split(":")[-1].replace("_", " "))
    count = (1, 1)
    for f in e.get("functions", []) or []:
        ft = f.get("function", "")
        if ft.endswith("set_count"):
            count = _num(f.get("count", 1))
        elif ft.endswith("looting_enchant") or ft.endswith("enchanted_count_increase"):
            notes.append("More with Looting")
    if t.endswith(":item"):
        out.append({"item": e.get("name"), "weight": w, "count": count, "cond": cond_chance, "notes": notes})
    elif t.endswith(":tag"):
        out.append({"item": "#" + e.get("name", ""), "weight": w, "count": count, "cond": cond_chance, "notes": notes})
    elif t.endswith(":alternatives") or t.endswith(":group") or t.endswith(":sequence"):
        for ch in e.get("children", []) or []:
            for it in _entry_items(ch, depth + 1):
                it["cond"] *= cond_chance
                it["notes"] = notes + it["notes"]
                out.append(it)
    elif t.endswith(":loot_table"):
        out.append({"table": e.get("value") or e.get("name"), "weight": w, "count": count, "cond": cond_chance, "notes": notes})
    elif t.endswith(":empty"):
        out.append({"item": None, "weight": w, "count": (0, 0), "cond": 1.0, "notes": []})
    return out


def parse_loot(tid: str, d: dict) -> dict:
    pools = []
    for p in d.get("pools", []) or []:
        rmin, rmax = _num(p.get("rolls", 1))
        entries = []
        for e in p.get("entries", []) or []:
            entries += _entry_items(e)
        total = sum(x["weight"] for x in entries if x.get("weight")) or 1
        pool_cond = 1.0
        for c in p.get("conditions", []) or []:
            if c.get("condition", "").endswith("random_chance"):
                ch = c.get("chance", 1)
                pool_cond *= ch if isinstance(ch, (int, float)) else 1
        items = []
        for x in entries:
            if not x.get("item") and not x.get("table"):
                continue
            per_roll = (x["weight"] / total) * x["cond"]
            rolls = (rmin + rmax) / 2.0
            chance = (1 - (1 - per_roll) ** rolls) * pool_cond if rolls > 0 else 0
            items.append({"item": x.get("item"), "table": x.get("table"), "chance": round(chance, 4),
                          "count": list(x["count"]), "notes": sorted(set(x["notes"]))})
        pools.append({"rolls": [rmin, rmax], "items": items})
    return {"id": tid, "type": d.get("type"), "pools": pools}


def load_loot(res: Resources) -> dict:
    out = {}
    for key in res.keys:
        for sub in ("loot_table", "loot_tables"):
            for ns, rel, full in res.data_files(key, sub):
                tid = "%s:%s" % (ns, rel)
                try:
                    d = load_json(full)
                except Exception:
                    continue
                if isinstance(d, dict):
                    t = parse_loot(tid, d)
                    t["jar"] = key
                    out.setdefault(tid, t)
    return out


def loot_modifiers(res: Resources) -> list:
    """Global loot modifiers that inject items/tables into other loot tables."""
    out = []
    for key in res.keys:
        for ns, rel, full in res.data_files(key, "loot_modifiers"):
            try:
                d = load_json(full)
            except Exception:
                continue
            if not isinstance(d, dict):
                continue
            targets = []
            for c in d.get("conditions", []) or []:
                if c.get("condition", "").endswith("loot_table_id"):
                    targets.append(c.get("loot_table_id"))
                for t in c.get("terms", []) or []:
                    if isinstance(t, dict) and t.get("loot_table_id"):
                        targets.append(t.get("loot_table_id"))
            chance = None
            for c in d.get("conditions", []) or []:
                if c.get("condition", "").endswith("random_chance"):
                    chance = c.get("chance")
            item = d.get("item") or d.get("addition") or d.get("result")
            table = d.get("table") or d.get("loot_table")
            out.append({"id": "%s:%s" % (ns, rel), "type": d.get("type"), "targets": targets, "item": item,
                        "table": table, "chance": chance, "jar": key})
    return out


# ------------------------------------------------------------ enchantments
def load_enchantments(res: Resources, key: str) -> list:
    out = []
    for ns, rel, full in res.data_files(key, "enchantment"):
        try:
            d = load_json(full)
        except Exception:
            continue
        eid = "%s:%s" % (ns, rel)
        desc = None
        for k in ("enchantment.%s.%s.desc" % (ns, rel), "enchantment.%s.%s.description" % (ns, rel)):
            if res.has(k):
                desc = res.tr(k)
        effects = []
        for comp, lst in (d.get("effects") or {}).items():
            if isinstance(lst, list):
                for e in lst:
                    eff = e.get("effect", e) if isinstance(e, dict) else {}
                    effects.append({"component": comp, "type": eff.get("type") if isinstance(eff, dict) else None,
                                    "value": _level_value(eff.get("value") if isinstance(eff, dict) else None) or _level_value(eff.get("amount") if isinstance(eff, dict) else None)})
            elif isinstance(lst, dict):
                effects.append({"component": comp, "type": None, "value": None})
        out.append({
            "id": eid, "ns": ns, "path": rel,
            "name": res.tr("enchantment.%s.%s" % (ns, rel)) or humanize(rel),
            "description": desc,
            "max_level": d.get("max_level"), "weight": d.get("weight"), "anvil_cost": d.get("anvil_cost"),
            "min_cost": d.get("min_cost"), "max_cost": d.get("max_cost"),
            "slots": d.get("slots"), "supported_items": d.get("supported_items"), "primary_items": d.get("primary_items"),
            "exclusive_set": d.get("exclusive_set"), "effects": effects,
        })
    return out


def _level_value(v):
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, dict):
        t = v.get("type", "")
        if t.endswith("linear"):
            return "%s (+%s per level)" % (v.get("base"), v.get("per_level_above_first"))
        if t.endswith("levels_squared"):
            return "level^2 + %s" % v.get("added")
        if t.endswith("clamped"):
            return _level_value(v.get("value"))
        if t.endswith("lookup"):
            return " / ".join(str(x) for x in v.get("values", []))
        if t.endswith("fraction"):
            return "%s / %s" % (_level_value(v.get("numerator")), _level_value(v.get("denominator")))
    return None


# -------------------------------------------------------------- worldgen
def load_biomes(res: Resources, key: str) -> list:
    out = []
    for ns, rel, full in res.data_files(key, "worldgen/biome"):
        try:
            d = load_json(full)
        except Exception:
            continue
        spawns = []
        for group, lst in (d.get("spawners") or {}).items():
            for s in lst or []:
                spawns.append({"group": group, "type": s.get("type"), "weight": s.get("weight"),
                               "min": s.get("minCount"), "max": s.get("maxCount")})
        eff = d.get("effects") or {}
        out.append({"id": "%s:%s" % (ns, rel), "ns": ns, "path": rel,
                    "name": res.tr("biome.%s.%s" % (ns, rel)) or humanize(rel),
                    "temperature": d.get("temperature"), "downfall": d.get("downfall"),
                    "precipitation": d.get("has_precipitation"), "spawns": spawns,
                    "colors": {k: eff.get(k) for k in ("sky_color", "fog_color", "water_color", "grass_color", "foliage_color") if k in eff},
                    "music": (eff.get("music") or {}).get("sound") if isinstance(eff.get("music"), dict) else None,
                    "features": sum(len(x) for x in (d.get("features") or []) if isinstance(x, list))})
    return out


def load_dimensions(res: Resources, key: str) -> list:
    out = []
    types = {}
    for ns, rel, full in res.data_files(key, "dimension_type"):
        try:
            types["%s:%s" % (ns, rel)] = load_json(full)
        except Exception:
            pass
    for ns, rel, full in res.data_files(key, "dimension"):
        try:
            d = load_json(full)
        except Exception:
            continue
        gen = d.get("generator") or {}
        bs = gen.get("biome_source") or {}
        biomes = []
        if isinstance(bs.get("biome"), str):
            biomes.append(bs["biome"])
        for b in bs.get("biomes", []) or []:
            if isinstance(b, dict) and isinstance(b.get("biome"), str):
                biomes.append(b["biome"])
        dt = types.get(d.get("type")) or {}
        name = None
        for k in ("dimension.%s.%s" % (ns, rel), "%s.dimension.%s" % (ns, rel), "dimension.%s" % rel):
            if res.has(k):
                name = res.tr(k)
        out.append({"id": "%s:%s" % (ns, rel), "ns": ns, "path": rel, "name": name or humanize(rel),
                    "type": d.get("type"), "generator": gen.get("type"), "settings": gen.get("settings") if isinstance(gen.get("settings"), str) else None,
                    "biomes": biomes,
                    "properties": {k: dt.get(k) for k in ("has_skylight", "has_ceiling", "ultrawarm", "natural", "piglin_safe", "bed_works", "respawn_anchor_works", "has_raids", "fixed_time", "min_y", "height", "ambient_light", "coordinate_scale") if k in dt}})
    return out


def load_structures(res: Resources, key: str) -> list:
    out = []
    sets = {}
    for ns, rel, full in res.data_files(key, "worldgen/structure_set"):
        try:
            d = load_json(full)
        except Exception:
            continue
        pl = d.get("placement") or {}
        for s in d.get("structures", []) or []:
            sid = s.get("structure") if isinstance(s, dict) else s
            sets[sid] = {"spacing": pl.get("spacing"), "separation": pl.get("separation"),
                         "placement": pl.get("type"), "frequency": pl.get("frequency")}
    for ns, rel, full in res.data_files(key, "worldgen/structure"):
        try:
            d = load_json(full)
        except Exception:
            continue
        sid = "%s:%s" % (ns, rel)
        name = None
        for k in ("structure.%s.%s" % (ns, rel), "%s.structure.%s" % (ns, rel)):
            if res.has(k):
                name = res.tr(k)
        out.append({"id": sid, "ns": ns, "path": rel, "name": name or humanize(rel),
                    "type": d.get("type"), "biomes": d.get("biomes"), "step": d.get("step"),
                    "terrain_adaptation": d.get("terrain_adaptation"), "start_pool": d.get("start_pool"),
                    "max_distance": d.get("max_distance_from_center"), "size": d.get("size"),
                    "spawn_overrides": list((d.get("spawn_overrides") or {}).keys()),
                    "placement": sets.get(sid)})
    return out


def load_advancements(res: Resources, key: str) -> list:
    out = []
    for sub in ("advancement", "advancements"):
        for ns, rel, full in res.data_files(key, sub):
            if rel.startswith("recipes/"):
                continue
            try:
                d = load_json(full)
            except Exception:
                continue
            disp = d.get("display")
            if not isinstance(disp, dict):
                continue

            def txt(c):
                if isinstance(c, dict):
                    if "translate" in c:
                        return res.tr(c["translate"]) or c.get("fallback") or c["translate"]
                    return c.get("text")
                return c
            icon = disp.get("icon") or {}
            out.append({"id": "%s:%s" % (ns, rel), "title": clean(txt(disp.get("title"))), "description": clean(txt(disp.get("description"))),
                        "frame": disp.get("frame", "task"), "hidden": disp.get("hidden", False), "parent": d.get("parent"),
                        "icon": icon.get("id") or icon.get("item"),
                        "criteria": list((d.get("criteria") or {}).keys()),
                        "rewards": d.get("rewards")})
    return out


def load_spawn_modifiers(res: Resources) -> list:
    out = []
    for key in res.keys:
        for sub in ("neoforge/biome_modifier", "forge/biome_modifier"):
            for ns, rel, full in res.data_files(key, sub):
                try:
                    d = load_json(full)
                except Exception:
                    continue
                if not isinstance(d, dict) or not d.get("type", "").endswith("add_spawns"):
                    continue
                sp = d.get("spawners")
                sp = sp if isinstance(sp, list) else [sp] if sp else []
                for s in sp:
                    out.append({"entity": s.get("type"), "biomes": d.get("biomes"), "weight": s.get("weight"),
                                "min": s.get("minCount"), "max": s.get("maxCount"), "jar": key})
    return out


def load_simple_dir(res: Resources, key: str, sub: str) -> dict:
    out = {}
    for ns, rel, full in res.data_files(key, sub):
        try:
            out["%s:%s" % (ns, rel)] = load_json(full)
        except Exception:
            pass
    return out


# ------------------------------------------------------------ patchouli books
def _patchouli_text(s: str) -> str:
    """Convert Patchouli formatting codes to Markdown."""
    if not s:
        return ""
    s = s.replace("$(br2)", "\n\n").replace("$(br)", "\n").replace("$(p)", "\n\n")
    s = re.sub(r"<br2\s*/?>", "\n\n", s)
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"\$\(li\)", "\n- ", s)
    s = re.sub(r"\$\(l:[^)]*\)(.*?)\$\(/l\)", r"\1", s)
    s = re.sub(r"\$\((item|thing|bold|b|l|italic|i|o)\)(.*?)\$\(\)", lambda m: ("*%s*" if m.group(1) in ("italic", "i", "o") else "**%s**") % m.group(2), s)
    s = re.sub(r"\$\([^)]*\)", "", s)
    return s.strip()


def load_patchouli(res: Resources, key: str) -> list:
    books = []
    base = os.path.join(res.root, key, "assets")
    if not os.path.isdir(base):
        return books
    for ns in os.listdir(base):
        pb = os.path.join(base, ns, "patchouli_books")
        if not os.path.isdir(pb):
            continue
        for book in sorted(os.listdir(pb)):
            root = os.path.join(pb, book, "en_us")
            if not os.path.isdir(root):
                continue
            meta = {}
            bj = os.path.join(res.root, key, "data", ns, "patchouli_books", book, "book.json")
            if os.path.isfile(bj):
                try:
                    meta = load_json(bj)
                except Exception:
                    meta = {}

            def tr(v):
                if isinstance(v, str) and res.has(v):
                    return res.tr(v)
                return v
            cats = {}
            cdir = os.path.join(root, "categories")
            for dp, _d, files in os.walk(cdir):
                for fn in files:
                    if fn.endswith(".json"):
                        rel = os.path.relpath(os.path.join(dp, fn), cdir).replace("\\", "/")[:-5]
                        try:
                            c = load_json(os.path.join(dp, fn))
                        except Exception:
                            continue
                        cats["%s:%s" % (ns, rel)] = {"id": "%s:%s" % (ns, rel), "name": clean(tr(c.get("name"))), "description": _patchouli_text(clean(tr(c.get("description")) or "")),
                                                     "icon": c.get("icon"), "sortnum": c.get("sortnum", 0), "entries": []}
            edir = os.path.join(root, "entries")
            for dp, _d, files in os.walk(edir):
                for fn in sorted(files):
                    if not fn.endswith(".json"):
                        continue
                    try:
                        e = load_json(os.path.join(dp, fn))
                    except Exception:
                        continue
                    cat = e.get("category", "")
                    if ":" not in cat:
                        cat = "%s:%s" % (ns, cat)
                    pages = []
                    for p in e.get("pages", []) or []:
                        if isinstance(p, str):
                            p = {"type": "text", "text": p}
                        pages.append({"type": (p.get("type") or "text").split(":")[-1], "title": clean(tr(p.get("title"))),
                                      "text": _patchouli_text(clean(tr(p.get("text")) or "")), "item": p.get("item"), "recipe": p.get("recipe")})
                    ent = {"name": clean(tr(e.get("name"))), "icon": e.get("icon"), "sortnum": e.get("sortnum", 0), "pages": pages}
                    if cat in cats:
                        cats[cat]["entries"].append(ent)
            for c in cats.values():
                c["entries"].sort(key=lambda x: (x["sortnum"], x["name"] or ""))
            books.append({"id": "%s:%s" % (ns, book), "name": clean(tr(meta.get("name"))) or content_humanize(book),
                          "landing": _patchouli_text(clean(tr(meta.get("landing_text")) or "")),
                          "categories": sorted(cats.values(), key=lambda c: (c["sortnum"], c["name"] or ""))})
    return books


def content_humanize(s):
    return s.replace("_", " ").title()
