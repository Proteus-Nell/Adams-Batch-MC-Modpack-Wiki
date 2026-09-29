"""'What it does' text for entry pages.

Two sources, in order of preference:

1. Hand-written notes in content/descriptions/<mod>.md, written from the mod's
   code. Each note is a `## <id>` section (several ids may share one heading,
   separated by commas). A `## class:<fully.qualified.Class>` note applies to
   every entry built from that class, with {name} replaced by the entry's name.
   A category prefix, like `## effects/tensura:curse`, limits a note to one
   category, for ids that name both an effect and a skill. A
   `<!-- kind: effects -->` line gives that prefix to every note after it.
   Notes may use the same placeholders as other hand-written pages
   ({{link:ns:id}}, {{cfg:file|path.key}}, ...), plus {{link:kind/ns:id}} to
   pick a category and {{auto}} to include the generated summary below.

2. A short summary generated from the extracted data (stats, recipes, loot,
   spawns, dimension properties). It only states facts the data shows, so an
   entry with custom behaviour still needs a hand-written note.
"""
from __future__ import annotations

import os
import re
from typing import Optional

NOTE_HEAD = re.compile(r"^## +(.+?)\s*$")
ID_RX = re.compile(r"^(?:[a-z]+/)?(class:[\w.$]+|[a-z0-9_.-]+:[a-z0-9_./-]+)$")
KIND_PREFIX = re.compile(r"^[a-z]+/")
KIND_LINE = re.compile(r"^<!--\s*kind:\s*([a-z]*)\s*-->\s*$")

WEAPON_WORDS = [
    ("GreatSword", "great sword"), ("LongSword", "long sword"), ("ShortSword", "short sword"), ("Katana", "katana"),
    ("Kodachi", "kodachi"), ("Odachi", "odachi"), ("Tachi", "tachi"), ("Spear", "spear"), ("Scythe", "scythe"),
    ("Sickle", "sickle"), ("Kunai", "kunai"), ("Knife", "knife"), ("Dagger", "dagger"), ("Club", "club"),
    ("Hammer", "hammer"), ("Axe", "axe"), ("Pickaxe", "pickaxe"), ("Shovel", "shovel"), ("Hoe", "hoe"),
    ("Bow", "bow"), ("Sword", "sword"),
]
VARIANT_BLOCKS = {"SlabBlock": "slab", "StairBlock": "stairs", "WallBlock": "wall", "FenceBlock": "fence",
                  "FenceGateBlock": "fence gate", "ButtonBlock": "button", "PressurePlateBlock": "pressure plate",
                  "DoorBlock": "door", "TrapDoorBlock": "trapdoor"}
PLAIN_BLOCKS = {"Block", "RotatedPillarBlock", "SidewayDirectionalBlock", "LooseBlock", "GlassBlock", "TransparentBlock",
                "IronBarsBlock", "StainedGlassPaneBlock", "LanternBlock", "CarpetBlock", "HorizontalDirectionalBlock",
                "DirectionalBlock"}
GENERIC_ITEMS = {"Item", "BlockItem", "BaseItem", "SimpleItem", "TensuraItem"}


class Notes:
    def __init__(self, content_dir: str):
        self.by_id = {}
        d = os.path.join(content_dir, "descriptions")
        if not os.path.isdir(d):
            return
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md"):
                continue
            ids, buf, kind = None, [], ""
            with open(os.path.join(d, fn), encoding="utf-8") as fh:
                lines = fh.read().split("\n")
            for line in lines + ["## <end>"]:
                km = KIND_LINE.match(line)
                if km:
                    kind = km.group(1)
                    continue
                m = NOTE_HEAD.match(line)
                heads = [h.strip() for h in m.group(1).split(",")] if m else []
                if m and (all(ID_RX.match(h) for h in heads) or m.group(1) == "<end>"):
                    if ids:
                        body = "\n".join(buf).strip()
                        if body:
                            for i in ids:
                                self.by_id[i] = body
                    ids, buf = None, []
                    if m.group(1) != "<end>":
                        ids = [h if KIND_PREFIX.match(h) or not kind else "%s/%s" % (kind, h) for h in heads]
                elif ids is not None:
                    buf.append(line)

    def get(self, ident: str, cls: Optional[str] = None, name: str = "", kind: str = "") -> Optional[str]:
        """A note for this category first, then an untagged note, then a class note."""
        keys = ["%s/%s" % (kind, ident)] if kind else []
        keys.append(ident)
        if cls:
            keys += (["%s/class:%s" % (kind, cls)] if kind else []) + ["class:" + cls]
        for k in keys:
            t = self.by_id.get(k)
            if t is not None:
                return t.replace("{name}", name)
        return None

    def __len__(self):
        return len(self.by_id)


def first_sentence(md: str, n=150) -> str:
    """Plain first sentence of a note, for index tables."""
    s = re.sub(r"\{\{link:(?:[a-z]+/)?[a-z0-9_.-]+:([a-z0-9_./-]+)\}\}", lambda m: m.group(1).rsplit("/", 1)[-1].replace("_", " "), md or "")
    s = re.sub(r"\{\{[^}]*\}\}", "", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"[*_`>#]", "", s).strip()
    s = s.split("\n\n")[0].replace("\n", " ")
    m = re.match(r"(.+?[.!?])(\s|$)", s)
    s = m.group(1) if m else s
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "..."


def _n(v):
    if isinstance(v, float) and v == int(v):
        return "{:,}".format(int(v))
    if isinstance(v, (int, float)):
        return "{:,}".format(v) if isinstance(v, int) else ("%g" % v)
    return str(v)


def _list(words):
    words = [w for w in words if w]
    if len(words) <= 1:
        return "".join(words)
    return ", ".join(words[:-1]) + " and " + words[-1]


class Summarizer:
    def __init__(self, site):
        self.site = site

    # ------------------------------------------------------------ helpers
    def _links(self, page, ids, kind=None, limit=5):
        ids = list(dict.fromkeys(i for i in ids if i))
        more = len(ids) - limit
        out = [self.site.link(page.path, i, kind) for i in ids[:limit]]
        if more > 0:
            out.append("%d more" % more)
        return _list(out)

    def _obtain(self, page, ident):
        s = self.site
        bits = []
        recs = s.recipes_out.get(ident, [])
        if recs:
            from .render import RECIPE_TYPES
            kinds = []
            for r in recs:
                k = RECIPE_TYPES.get(r.get("type"), (r.get("type") or "").split(":")[-1].replace("_", " ").title())
                k = re.sub(r" \((shaped|shapeless)\)$", "", k)
                if k and k not in kinds:
                    kinds.append(k)
            verbs = {"Crafting": "crafted", "Smelting": "smelted in a furnace", "Blasting": "smelted in a blast furnace",
                     "Smoking": "cooked in a smoker", "Campfire": "cooked on a campfire", "Stonecutter": "cut in a stonecutter",
                     "Smithing Table": "made at a smithing table", "Create: Compacting": "made with Create's compacting",
                     "Create: Crushing": "made with Create's crushing wheels"}
            done = []
            for k in kinds:
                v = verbs.get(k) or ("made with " + k if k.startswith("Refining") else "made at the " + k)
                if v not in done:
                    done.append(v)
            bits.extend(done)
        src = s.loot_sources.get(ident, [])
        mobs = [tid for tid, _ in src if tid.split(":", 1)[-1].startswith(("entities/", "entity/"))]
        chests = [tid for tid, _ in src if "chests/" in tid]
        blocks = [tid for tid, _ in src if tid.split(":", 1)[-1].startswith("blocks/")]
        if mobs:
            ids = ["%s:%s" % (t.split(":")[0], t.split(":", 1)[1].split("/", 1)[1]) for t in mobs]
            bits.append("dropped by " + self._links(page, ids, "entity", 4))
        if blocks:
            ids = ["%s:%s" % (t.split(":")[0], t.split(":", 1)[1].split("/", 1)[1]) for t in blocks if t.split(":", 1)[1].split("/", 1)[1] != ident.split(":")[-1]]
            if ids:
                bits.append("dropped when you break " + self._links(page, ids, "block", 4))
        if chests:
            bits.append("found in %d kind%s of loot chest" % (len(chests), "s" if len(chests) > 1 else ""))
        return bits

    def _uses(self, page, ident):
        s = self.site
        outs = []
        for r in s.recipes_in.get(ident, []):
            o = (r.get("result") or {}).get("id")
            if o and o != ident and o not in outs:
                outs.append(o)
        return outs

    # -------------------------------------------------------------- items
    def item(self, page, it) -> list:
        s = self.site
        ident = it["id"]
        cls = (it.get("class") or "").rsplit(".", 1)[-1]
        out = []
        if ident.endswith("_spawn_egg") or cls in ("SpawnEggItem", "DeferredSpawnEggItem"):
            mob = ident[: -len("_spawn_egg")]
            out.append("Creative-mode spawn egg. Use it on a block to spawn %s." % s.link(page.path, mob, "entity"))
            return out
        g = it.get("gear") or {}
        a = it.get("armor") or {}
        if g:
            wt = next((w for k, w in WEAPON_WORDS if k in cls), None) or next((w for k, w in WEAPON_WORDS if k.lower() in ident), "weapon")
            tier = g.get("tier")
            two, one, main = g.get("two_handed"), g.get("one_handed"), g.get("main")
            head = "A %s%s" % ((tier + " ") if tier and tier.lower() not in ident.replace("_", " ") else "", wt)
            if two and one:
                out.append("%s you can hold in one or both hands. Two-handed it deals **%s** attack damage at **%s** attack speed; "
                           "one-handed **%s** damage at **%s** speed." % (head, _n(two.get("attack_damage", "?")), _n(two.get("attack_speed", "?")),
                                                                        _n(one.get("attack_damage", "?")), _n(one.get("attack_speed", "?"))))
                main = two
            elif main:
                out.append("%s that deals **%s** attack damage at **%s** attack speed." % (head, _n(main.get("attack_damage", "?")), _n(main.get("attack_speed", "?"))))
            extra = []
            if main:
                if main.get("reach"):
                    extra.append("%+g block%s of reach" % (main["reach"], "" if abs(main["reach"]) == 1 else "s"))
                if main.get("crit_chance"):
                    extra.append("+%g%% critical hit chance" % main["crit_chance"])
                if main.get("crit_multiplier"):
                    extra.append("+%g critical damage multiplier" % main["crit_multiplier"])
                if main.get("sweep") and main["sweep"] > 0:
                    extra.append("%g%% sweeping damage" % (main["sweep"] * 100))
                elif main.get("sweep") and main["sweep"] < 0:
                    extra.append("no sweeping attack")
                if main.get("knockback"):
                    extra.append("+%g knockback" % main["knockback"])
            if extra:
                out.append("It also has " + _list(extra) + ".")
            if g.get("durability"):
                out.append("Durability: **%s**." % _n(g["durability"]))
        elif a:
            bits = ["**%s** armor" % _n(a["armor"])]
            if a.get("toughness"):
                bits.append("**%s** toughness" % _n(a["toughness"]))
            if a.get("knockback_resistance"):
                bits.append("**%g%%** knockback resistance" % (a["knockback_resistance"] * 100))
            out.append("%s armor for the %s slot: %s." % (a.get("material", ""), a.get("slot", "").lower(), _list(bits)))
            if a.get("durability"):
                out.append("Durability: **%s**." % _n(a["durability"]))
        elif "schematic" in ident or cls == "SmithingSchematicItem":
            makes = [(r.get("result") or {}).get("id") for rs in s.recipes_out.values() for r in rs if ident in (r.get("schematics") or [])]
            makes = list(dict.fromkeys(m for m in makes if m))
            if makes:
                out.append("Smithing schematic. You need it to forge %s." % self._links(page, makes, "item", 6))
        if not out and (it.get("props") or {}).get("food"):
            out.append("Food.")
        obtain = self._obtain(page, ident)
        uses = self._uses(page, ident)
        if not out and uses and cls in GENERIC_ITEMS | {""}:
            out.append("Crafting material, used to make %s." % self._links(page, uses, "item", 5))
        elif uses and not g and not a:
            out.append("Used to make %s." % self._links(page, uses, "item", 5))
        if obtain:
            out.append("It is %s." % _list(obtain))
        return out

    # ------------------------------------------------------------- blocks
    def block(self, page, b) -> list:
        s = self.site
        ident = b["id"]
        cls = (b.get("class") or "").rsplit(".", 1)[-1]
        ns, path = ident.split(":", 1)
        out = []
        if cls in VARIANT_BLOCKS or re.search(r"_(slab|stairs|wall|fence|fence_gate|button|pressure_plate|door|trapdoor)$", path):
            kind = VARIANT_BLOCKS.get(cls) or re.search(r"_(slab|stairs|wall|fence_gate|fence|button|pressure_plate|door|trapdoor)$", path).group(1).replace("_", " ")
            base = re.sub(r"_(slab|stairs|wall|fence_gate|fence|button|pressure_plate|door|trapdoor)$", "", path)
            cands = [base, base + "s", base.replace("brick", "bricks"), base.replace("tile", "tiles"), base + "_block", base + "_planks"]
            found = next((c for c in cands if ("block|%s:%s" % (ns, c)) in s.refs), None)
            if found:
                out.append("Decorative %s made from %s." % (kind, s.link(page.path, "%s:%s" % (ns, found), "block")))
            else:
                out.append("Decorative %s building block." % kind)
        elif "_ore" in path or any(t.endswith(":ores") or "/ores" in t for t in b.get("item_tags") or []):
            drops = [it.get("item") for p in b.get("drops") or [] for it in p["items"] if it.get("item") and it["item"] != ident]
            level = [t.split(":")[-1].replace("needs_", "").replace("_tool", "") for t in b.get("tags", []) if "needs_" in t]
            txt = "Ore block."
            if drops:
                txt += " Mining it drops %s." % self._links(page, drops, "item", 3)
            if level:
                txt += " You need a %s pickaxe or better." % level[0]
            out.append(txt)
        elif cls in PLAIN_BLOCKS or not cls:
            stor = [r for r in s.recipes_out.get(ident, []) if r.get("kind") == "shaped" and len(set("".join(r.get("pattern") or []))) == 1 and len("".join(r.get("pattern") or [])) == 9]
            if stor:
                key = next(iter(stor[0]["key"].values()))
                src = (key or {}).get("items") or []
                if src:
                    out.append("Storage block: nine %s packed into one block." % s.link(page.path, src[0], "item"))
            if not out and cls in PLAIN_BLOCKS:
                out.append("Building block.")
        uses = self._uses(page, ident)
        if uses and out:
            out.append("Used to make %s." % self._links(page, uses, "item", 5))
        return out

    # --------------------------------------------------------------- mobs
    def mob(self, page, m) -> list:
        s = self.site
        info = m.get("info") or {}
        at = info.get("attributes") or {}
        ex = m.get("existence") or {}
        cat = (info.get("category") or "").lower()
        kind = "A boss" if info.get("boss") else {"monster": "A hostile mob", "creature": "A passive mob", "water_creature": "A water mob",
                                                 "ambient": "An ambient mob", "misc": "An entity"}.get(cat, "A mob")
        bits = []
        hp = at.get("Health")
        if isinstance(hp, (int, float)):
            bits.append("**%s** health" % _n(hp))
        dmg = at.get("Attack damage")
        if isinstance(dmg, (int, float)):
            bits.append("**%s** attack damage" % _n(dmg))
        if ex.get("max_magicule"):
            mn, mx = ex.get("min_magicule"), ex.get("max_magicule")
            bits.append("**%s** magicule" % (_n(mx) if mn == mx else "%s-%s" % (_n(mn), _n(mx))))
        out = [kind + (" with " + _list(bits) if bits else "") + "."]
        if m.get("spawns"):
            biomes = []
            for sp in m["spawns"]:
                b = sp.get("biomes")
                biomes += b if isinstance(b, list) else [b]
            names = [s.name_of(b[1:]).replace("Is ", "") if isinstance(b, str) and b.startswith("#") else s.name_of(b) for b in biomes if b]
            out.append("Spawns naturally in %s." % _list(list(dict.fromkeys(names))[:5]))
        if ex.get("abilities"):
            out.append("It has %d skill%s you can take from it with Predator-type skills." % (len(ex["abilities"]), "" if len(ex["abilities"]) == 1 else "s"))
        drops = [it.get("item") for p in m.get("drops") or [] for it in p["items"] if it.get("item")]
        if drops:
            out.append("Drops %s." % self._links(page, drops, "item", 4))
        return out

    # ------------------------------------------------------------ effects
    def effect(self, page, e) -> list:
        s = self.site
        cat = (e.get("category") or "").lower()
        out = ["%s status effect." % {"beneficial": "A beneficial", "harmful": "A harmful", "neutral": "A neutral"}.get(cat, "A")]
        if e.get("attributes"):
            bits = []
            for a in e["attributes"]:
                try:
                    v = float(a["amount"])
                except (TypeError, ValueError):
                    continue
                op = a.get("operation") or ""
                if "MULTIPLIED" in op:
                    bits.append("%s %+g%%" % (a["attribute"].lower(), v * 100))
                else:
                    bits.append("%s %+g" % (a["attribute"].lower(), v))
            if bits:
                out.append("Each level changes %s." % _list(bits))
        return out if len(out) > 1 else []

    # ----------------------------------------------------------- worldgen
    def biome(self, page, b, dims) -> list:
        s = self.site
        out = []
        where = (" in " + _list([s.link(page.path, d["id"], "dimension") for d in dims])) if dims else ""
        t = b.get("temperature")
        feel = "" if t is None else (" frozen" if t <= 0.0 else " cold" if t < 0.3 else " hot" if t >= 1.5 else " warm" if t > 0.9 else " temperate")
        out.append("A%s biome%s%s." % (feel, where, "" if b.get("precipitation") else " where it never rains or snows"))
        if b.get("spawns"):
            mobs = [x["type"] for x in b["spawns"]]
            out.append("Mobs that spawn here: %s." % self._links(page, mobs, "entity", 6))
        elif b.get("features", 0) == 0:
            out.append("It has no mob spawns and no terrain features of its own.")
        return out

    def dimension(self, page, d) -> list:
        p = d.get("properties") or {}
        gen = (d.get("generator") or "").split(":")[-1]
        out = []
        head = {"flat": "A flat, superflat-style dimension", "noise": "A dimension with generated terrain", "debug": "A debug dimension"}.get(gen, "A dimension")
        out.append(head + ".")
        ft = p.get("fixed_time")
        if isinstance(ft, (int, float)):
            tod = {0: "sunrise", 6000: "noon", 12000: "sunset", 18000: "midnight"}.get(int(ft) % 24000, "tick %s" % _n(ft))
            out.append("Time never moves: it is always %s." % tod)
        rules = []
        if p.get("bed_works") is False:
            rules.append("beds explode if you try to sleep")
        if p.get("respawn_anchor_works") is False:
            rules.append("respawn anchors don't work")
        if p.get("ultrawarm"):
            rules.append("water evaporates")
        if p.get("has_ceiling"):
            rules.append("there is a bedrock ceiling")
        if p.get("natural") is False:
            rules.append("compasses and clocks spin")
        if rules:
            out.append(_list(rules).capitalize() + ".")
        if p.get("ambient_light") and float(p["ambient_light"]) >= 1.0:
            out.append("It is fully lit everywhere.")
        if isinstance(p.get("height"), int):
            out.append("Build height: Y %s to %s." % (_n(p.get("min_y", 0)), _n(p.get("min_y", 0) + p["height"] - 1)))
        return out

    def structure(self, page, st) -> list:
        s = self.site
        pl = st.get("placement") or {}
        out = []
        b = st.get("biomes")
        where = s.biome_list(page, b) if b else None
        txt = "Generates" + ((" in " + where) if where and where != "?" else "")
        if pl.get("spacing"):
            sep = pl.get("separation", "?")
            txt += ", about one every %s chunks (at least %s chunk%s apart)" % (pl["spacing"], sep, "" if sep == 1 else "s")
        out.append(txt + ".")
        return out

    def enchantment(self, page, e) -> list:
        return []
