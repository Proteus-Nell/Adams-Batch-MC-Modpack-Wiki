"""Skills, magic, battlewill and races for Tensura and its addons (ManasCore)."""
from __future__ import annotations

import re
from typing import Optional

from .javaindex import (JavaIndex, JClass, Unknown, EnumConst, InstanceOf, text, walk,
                        call_args, method_invocations)
from .registry import Reg, holder_ref
from .resources import Resources, clean

BASE_SKILL_CLASSES = {
    "ManasSkill", "TensuraSkill", "Skill", "Magic", "Battlewill", "ElementalTransformSkill",
    "MagicElementalTransformSkill",
}

HOOKS = [
    ("onToggleOn", "toggle", "Can be toggled on and off"),
    ("onPressed", "press", "Activated by pressing the skill key"),
    ("onHeld", "hold", "Charged or channelled by holding the skill key"),
    ("onRelease", "release", "Triggers when the held key is released"),
    ("onScroll", "scroll", "Adjusted by scrolling while active"),
    ("onTick", "tick", "Has a continuous (per-tick) effect"),
    ("onDamageEntity", "on_damage_dealt", "Triggers when you damage a target"),
    ("onTouchEntity", "on_melee_hit", "Triggers on melee contact"),
    ("onBeingDamaged", "on_attacked", "Triggers when you are attacked"),
    ("onTakenDamage", "on_damage_taken", "Triggers when you take damage"),
    ("onBeingTargeted", "on_targeted", "Triggers when a mob targets you"),
    ("onEffectAdded", "on_effect", "Triggers when an effect is applied to you"),
    ("onProjectileHit", "on_projectile", "Triggers when a projectile hits you"),
    ("onDeath", "on_death", "Triggers when you die"),
    ("onRespawn", "on_respawn", "Triggers when you respawn"),
    ("onLearnSkill", "on_learn", "Does something when first learned"),
    ("onSkillMastered", "on_mastered", "Does something when mastered"),
    ("onSubordinateDeath", "on_subordinate_death", "Triggers when one of your subordinates dies"),
    ("onNumberKeyPress", "number_keys", "Uses number keys for extra actions"),
]

RACE_TAG_TRAITS = {
    "can_breath_water": "Can breathe underwater",
    "can_glide": "Can glide",
    "cold_blooded": "Cold-blooded",
    "has_creative_flight": "Has creative-style flight",
    "need_moist": "Needs moisture",
    "no_blood": "Has no blood",
    "spiritual": "Spiritual lifeform",
    "spawn_as_spiritual": "Spawns as a spiritual lifeform",
    "undead": "Undead",
    "divine": "Divine",
    "human_like": "Human-like",
    "beastfolk": "Beastfolk",
    "daemon": "Daemon",
    "slime": "Slime",
    "necromancer": "Necromancer",
    "unable_to_heal_with_food": "Cannot heal by eating",
    "limited_ep_in_central": "EP is limited in the central world",
}


def fmt_num(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, float):
        if v != v:
            return "?"
        if v == int(v) and abs(v) < 1e15:
            v = int(v)
        else:
            return ("%.4f" % v).rstrip("0").rstrip(".")
    if isinstance(v, int):
        return "{:,}".format(v)
    return str(v)


class RefResolver:
    """Maps code references (holders, classes, resource locations) to registry ids."""

    def __init__(self, ix: JavaIndex, regs: list, known_ids: dict):
        self.ix = ix
        self.by_holder = {}
        self.by_class: dict = {}
        for r in regs:
            self.by_holder[r.holder] = r
            if r.cls:
                self.by_class.setdefault(r.cls, []).append(r)
        self.known_ids = known_ids  # full id -> kind

    def holder(self, node, ctx: JClass) -> Optional[Reg]:
        h = holder_ref(node)
        if not h or "." not in h:
            f = self.ix.find_field(ctx, h) if h else None
            if f is not None:
                return self.by_holder.get(f.cls.fqcn + "." + f.name)
            return None
        owner, fname = h.rsplit(".", 1)
        oc = self.ix.resolve(owner, ctx)
        if oc is None:
            return None
        f = self.ix.find_field(oc, fname)
        if f is None:
            return None
        return self.by_holder.get(f.cls.fqcn + "." + f.name)

    def refs(self, node, ctx: JClass, kinds=("skill", "race", "item", "block", "effect", "entity")) -> list:
        """Registry ids referenced inside a code fragment, in order, de-duplicated."""
        out = []
        seen = set()
        if node is None:
            return out
        for n in walk(node):
            rid = None
            if n.type == "field_access":
                p = n.parent
                # skip the inner part of X.Y.get() - handled on the full node
                r = self.holder(n, ctx)
                if r is not None:
                    rid = r.full_id
            elif n.type == "object_creation_expression":
                ty = text(n.child_by_field_name("type"))
                rc = self.ix.resolve(ty, ctx)
                if rc is not None and rc.fqcn in self.by_class and len(self.by_class[rc.fqcn]) == 1:
                    rid = self.by_class[rc.fqcn][0].full_id
            elif n.type == "method_invocation" and text(n.child_by_field_name("name")) in ("fromNamespaceAndPath", "parse", "tryParse"):
                v = self.ix.try_eval(n, ctx)
                if isinstance(v, str) and v in self.known_ids:
                    rid = v
            if rid and rid not in seen and self.known_ids.get(rid) in kinds:
                seen.add(rid)
                out.append(rid)
        return out


class AbilityExtractor:
    def __init__(self, ix: JavaIndex, res: Resources, resolver: RefResolver, config_links):
        self.ix = ix
        self.res = res
        self.rr = resolver
        self.config_links = config_links  # callable(cls) -> list of option refs

    # ------------------------------------------------------------ helpers
    def _chain(self, cls: JClass):
        """Class and its ancestors up to (not including) the Tensura/ManasCore base classes."""
        out = []
        c = cls
        while c is not None and c.simple not in BASE_SKILL_CLASSES and len(out) < 12:
            out.append(c)
            c = self.ix.resolve(c.superclass, c) if c.superclass else None
        return out

    def _method_in_chain(self, cls, name):
        for c in self._chain(cls):
            m = c.method(name)
            if m is not None:
                return m
        return None

    def _enum_in_super_call(self, cls, pattern):
        c = cls
        depth = 0
        while c is not None and depth < 12:
            for m in c.methods.get("<init>", []):
                for n in walk(m.node):
                    if n.type == "explicit_constructor_invocation":
                        mm = re.search(pattern, text(n))
                        if mm:
                            return mm.group(1)
            gt = c.method("getType")
            if gt is not None:
                for r in gt.returns():
                    mm = re.search(pattern, text(r))
                    if mm:
                        return mm.group(1)
            c = self.ix.resolve(c.superclass, c) if c.superclass else None
            depth += 1
        return None

    def describe(self, node, ctx, env=None):
        """Human-friendly value for an expression (number if we can, else code)."""
        if node is None:
            return None
        try:
            v = self.ix.eval(node, ctx, env)
            if isinstance(v, InstanceOf):
                raise Unknown("inst")
            return fmt_num(v) if not isinstance(v, EnumConst) else v.name
        except Exception:
            pass
        t = node.type
        if t == "ternary_expression":
            a = self.describe(node.child_by_field_name("consequence"), ctx, env)
            b = self.describe(node.child_by_field_name("alternative"), ctx, env)
            cond = text(node.child_by_field_name("condition"))
            if "astered" in cond:
                return "%s mastered, %s otherwise" % (a, b) if "!" not in cond else "%s unmastered, %s mastered" % (a, b)
            return "%s or %s" % (a, b)
        if t == "parenthesized_expression":
            return self.describe(node.named_children[0], ctx, env)
        if t == "cast_expression":
            return self.describe(node.child_by_field_name("value"), ctx, env)
        f = self.formula(node, ctx, env)
        if f:
            return f
        s = re.sub(r"\s+", " ", text(node))
        return "`%s`" % s if len(s) <= 120 else None

    PHRASES = {
        "getMaxMagicule": "max MP", "getBaseMaxMagicule": "base max MP", "getMagicule": "MP",
        "getMaxAura": "max AP", "getBaseMaxAura": "base max AP", "getAura": "AP",
        "getMaxHealth": "max HP", "getHealth": "HP", "getMaxEP": "max EP", "getBaseMaxEP": "base max EP",
        "getEP": "EP", "getExistencePoints": "EP", "getMastery": "mastery", "getSoulPoints": "soul points",
        "getMaxSpiritualHealth": "max spiritual HP", "getSpiritualHealth": "spiritual HP",
        "getMagiculeCost": "base cost", "getAuraCost": "base aura cost",
    }
    CONTEXT_ARGS = {"entity", "instance", "mode", "this", "living", "player", "owner", "user", "caster", "level", "stack"}

    def formula(self, node, ctx, env, depth=0):
        """Readable formula with config numbers filled in, e.g. 'max MP x 0.05'."""
        if node is None or depth > 8:
            return None
        try:
            v = self.ix.eval(node, ctx, env)
            if not isinstance(v, (InstanceOf, tuple, list)):
                return fmt_num(v) if not isinstance(v, EnumConst) else v.name
        except Exception:
            pass
        t = node.type
        if t == "parenthesized_expression":
            inner = self.formula(node.named_children[0], ctx, env, depth + 1)
            return "(%s)" % inner if inner else None
        if t == "cast_expression":
            return self.formula(node.child_by_field_name("value"), ctx, env, depth + 1)
        if t == "binary_expression":
            op = text(node.child_by_field_name("operator"))
            l = self.formula(node.child_by_field_name("left"), ctx, env, depth + 1)
            r = self.formula(node.child_by_field_name("right"), ctx, env, depth + 1)
            if l is None or r is None:
                return None
            sym = {"*": "\u00d7", "/": "\u00f7"}.get(op, op)
            return "%s %s %s" % (l, sym, r)
        if t == "method_invocation":
            name = text(node.child_by_field_name("name"))
            obj = node.child_by_field_name("object")
            args = [a for a in call_args(node) if text(a) not in self.CONTEXT_ARGS]
            if name in self.PHRASES:
                return self.PHRASES[name]
            if name in ("get", "floatValue", "doubleValue", "intValue") and obj is not None and not args:
                return self.formula(obj, ctx, env, depth + 1)
            if name in ("max", "min") and len(args) == 2:
                a = [self.formula(x, ctx, env, depth + 1) for x in args]
                if all(a):
                    return "%s(%s, %s)" % (name, a[0], a[1])
            if name in ("round", "floor", "ceil", "abs") and args:
                return self.formula(args[0], ctx, env, depth + 1)
            parts = [self.formula(x, ctx, env, depth + 1) for x in args]
            label = re.sub(r"(?<!^)([A-Z])", r" \1", re.sub(r"^(get|apply|calc|calculate|compute)", "", name)).strip().lower()
            if parts and all(parts):
                return "%s (%s)" % (parts[0], label) if len(parts) == 1 else "%s(%s)" % (label, ", ".join(parts))
            return label or None
        if t in ("identifier", "field_access"):
            last = text(node).split(".")[-1]
            if last in self.CONTEXT_ARGS:
                return None
            return re.sub(r"(?<!^)([A-Z])", r" \1", last).lower().replace("_", " ")
        return None

    def per_mode(self, m, ctx, modes):
        """Evaluate a cost method: a single value or one per mode for switch statements."""
        if m is None:
            return None
        rets = m.returns()
        if not rets:
            return None
        if len(rets) == 1 and rets[0].type == "switch_expression":
            sw = rets[0]
            body = sw.child_by_field_name("body")
            out = []
            for rule in body.named_children:
                if rule.type not in ("switch_rule", "switch_block_statement_group"):
                    continue
                label = rule.named_children[0]
                labels = text(label).replace("case", "").replace("->", "").replace(":", "").strip()
                val = rule.named_children[-1]
                if val.type == "expression_statement" and val.named_children:
                    val = val.named_children[0]
                d = self.describe(val, ctx, self.ix.locals_env(val, ctx))
                names = []
                for part in labels.split(","):
                    part = part.strip()
                    if part == "default":
                        names.append("other modes")
                    elif part.isdigit() and modes and int(part) < len(modes):
                        names.append(modes[int(part)]["name"])
                    else:
                        names.append(part)
                out.append({"when": ", ".join(names), "value": d})
            return out
        vals = [self.describe(r, ctx, self.ix.locals_env(r, ctx)) for r in rets]
        vals = [v for v in vals if v is not None]
        uniq = []
        for v in vals:
            if v not in uniq:
                uniq.append(v)
        if not uniq:
            return None
        return [{"when": None, "value": v} for v in uniq[:4]]

    def lang_name(self, ns, kind, path, cls):
        for key in ("%s.%s.%s" % (ns, kind, path),):
            if self.res.has(key):
                return self.res.tr(key), key
        # getName override with a literal key
        if cls is not None:
            m = self._method_in_chain(cls, "getName")
            if m is not None:
                for n in walk(m.node):
                    if n.type == "method_invocation" and text(n.child_by_field_name("name")) == "translatable":
                        a = call_args(n)
                        if a:
                            k = self.ix.try_eval(a[0], cls)
                            if isinstance(k, str) and self.res.has(k):
                                return self.res.tr(k), k
        return path.replace("_", " ").title(), None

    def translatable_keys(self, node, ctx) -> list:
        out = []
        for n in walk(node):
            if n.type == "method_invocation" and text(n.child_by_field_name("name")) in ("translatable", "translatableWithFallback"):
                a = call_args(n)
                if a:
                    k = self.ix.try_eval(a[0], ctx)
                    if isinstance(k, str):
                        out.append((k, a[1:], n))
        return out

    # -------------------------------------------------------------- skills
    def skill(self, reg: Reg, ns: str, tags_by_skill: dict) -> dict:
        ix = self.ix
        cls = ix.classes.get(reg.cls)
        path = reg.id
        full = "%s:%s" % (ns, path)
        name, name_key = self.lang_name(ns, "skill", path, cls)
        desc = self.res.tr("%s.skill.%s.description" % (ns, path))
        if desc is None and name_key:
            desc = self.res.tr(name_key + ".description")
        rec = {"id": full, "ns": ns, "path": path, "name": name, "description": desc, "class": reg.cls}
        if cls is None:
            return rec
        if ix.is_a(cls, "Magic"):
            rec["category"] = "magic"
            rec["tier"] = (self._enum_in_super_call(cls, r"MagicType\.([A-Z_]+)") or "misc").lower()
        elif ix.is_a(cls, "Battlewill"):
            rec["category"] = "battlewill"
            rec["tier"] = "battlewill"
        elif ix.is_a(cls, "Skill"):
            rec["category"] = "skill"
            rec["tier"] = (self._enum_in_super_call(cls, r"SkillType\.([A-Z_]+)") or "other").lower()
        else:
            rec["category"] = "skill"
            rec["tier"] = "other"
        # element for magic (package name) e.g. ability.magic.aspectual.fire
        pk = cls.pkg.split(".")
        if rec["category"] == "magic" and len(pk) >= 2 and pk[-2] in ("aspectual", "spiritual"):
            rec["element"] = pk[-1]
        if rec["category"] == "battlewill" and pk[-1] in ("melee", "projectile", "utility"):
            rec["element"] = pk[-1]
        # icon
        rec["icon"] = self.skill_icon(cls, rec, ns, path)
        # modes
        modes = []
        gm = self._method_in_chain(cls, "getModes")
        nmodes = None
        if gm is not None:
            for r in gm.returns():
                v = ix.try_eval(r, cls)
                if isinstance(v, int):
                    nmodes = v
        mid = self._method_in_chain(cls, "getModeId")
        mode_ids = {}
        if mid is not None:
            for n in walk(mid.node):
                if n.type == "switch_rule" or n.type == "switch_block_statement_group":
                    lab = text(n.named_children[0]).replace("case", "").replace("->", "").replace(":", "").strip()
                    val = n.named_children[-1]
                    if val.type == "expression_statement" and val.named_children:
                        val = val.named_children[0]
                    v = ix.try_eval(val, cls)
                    if isinstance(v, str):
                        for part in lab.split(","):
                            part = part.strip()
                            if part.isdigit():
                                mode_ids[int(part)] = v
        if nmodes is None and mode_ids:
            nmodes = max(mode_ids) + 1
        if nmodes and nmodes > 1 or mode_ids:
            for i in range(nmodes or 0):
                mid_ = mode_ids.get(i)
                nm = None
                if mid_:
                    nm = self.res.tr("%s.skill.mode.%s" % (ns, mid_)) or self.res.tr("tensura.skill.mode.%s" % mid_)
                modes.append({"index": i, "id": mid_, "name": nm or (mid_.split(".")[-1].replace("_", " ").title() if mid_ else "Mode %d" % (i + 1))})
        pref = "%s.skill.mode.%s." % (ns, path)
        lang_modes = [(k, self.res.tr(k)) for k in self.res.lang if k.startswith(pref) and k.count(".") == pref.count(".")]
        if not modes:
            for k, v in lang_modes:
                modes.append({"index": len(modes), "id": k[len(ns) + 12:], "name": v})
        elif all(md["id"] is None for md in modes) and lang_modes:
            if len(lang_modes) >= len(modes):
                for md, (k, v) in zip(modes, lang_modes):
                    md["name"] = v
                    md["id"] = k[len(ns) + 12:]
        rec["modes"] = modes
        # activation & hooks
        hooks = []
        chain = self._chain(cls)
        for mname, key, label in HOOKS:
            if any(c.method(mname) is not None for c in chain):
                hooks.append({"key": key, "label": label})
        rec["hooks"] = hooks
        # costs
        rec["magicule_cost"] = self.per_mode(self._method_in_chain(cls, "getMagiculeCost"), cls, modes)
        rec["aura_cost"] = self.per_mode(self._method_in_chain(cls, "getAuraCost"), cls, modes)
        acq = self._method_in_chain(cls, "getDefaultAcquiringMagiculeCost")
        if acq is not None:
            rec["acquire_cost"] = self.per_mode(acq, cls, modes)
        mm = self._method_in_chain(cls, "getMaxMastery")
        if mm is not None:
            rec["max_mastery"] = self.per_mode(mm, cls, modes)
        cd = None
        for n in walk(cls.node):
            if n.type == "method_invocation" and text(n.child_by_field_name("name")) in ("setCoolDown", "addCooldown", "setCooldown"):
                a = call_args(n)
                if a:
                    # ManasSkillInstance.setCoolDown(int coolDown, int mode)
                    d = self.describe(a[0], cls, self.ix.locals_env(n, cls))
                    if d is None or d.startswith("`") or not re.search(r"\d", d) or d == "0":
                        continue
                    if d and d not in (cd or []):
                        cd = (cd or []) + [d]
        if cd:
            rec["cooldowns"] = cd[:6]
        held = self._method_in_chain(cls, "getMaxHeldTime")
        if held is not None:
            rec["max_held"] = self.per_mode(held, cls, modes)
        # acquisition requirement: translatable messages + referenced skills
        car = self._method_in_chain(cls, "checkAcquiringRequirement")
        if car is not None:
            rec["acquire_requirement_refs"] = self.rr.refs(car.body, cls, ("skill", "race", "item"))
            rec["acquire_requirement_messages"] = [self.res.tr(k) for k, _a, _n in self.translatable_keys(car.node, cls) if self.res.tr(k)]
        # attributes
        rec["attributes"] = self.attributes(cls)
        # references
        rec["related"] = [r for r in self.rr.refs(cls.node, cls, ("skill",)) if r != full][:25]
        rec["effects"] = self.rr.refs(cls.node, cls, ("effect",))[:25]
        rec["items"] = self.rr.refs(cls.node, cls, ("item",))[:15]
        rec["entities"] = self.rr.refs(cls.node, cls, ("entity",))[:15]
        rec["tags"] = sorted(tags_by_skill.get(full, []))
        rec["config"] = self.config_links(cls)
        # lang: obtainment + messages
        ob = self.res.tr("%s.skill.%s.obtainment" % (ns, path))
        if ob:
            rec["obtainment_text"] = ob
        msgs = []
        pref = "%s.skill.%s." % (ns, path)
        for k in self.res.lang:
            if k.startswith(pref) and not k.endswith((".description", ".obtainment")):
                msgs.append({"key": k, "text": self.res.tr(k)})
        rec["messages"] = msgs[:40]
        return rec

    def skill_icon(self, cls, rec, ns, path):
        m = self._method_in_chain(cls, "getSkillIcon")
        if m is not None:
            for r in m.returns():
                v = self.ix.try_eval(r, cls)
                if isinstance(v, str) and ":" in v:
                    return v
        base = {"magic": "textures/magic/%s/%s.png" % (rec.get("tier"), path),
                "battlewill": "textures/battlewill/%s.png" % path}.get(rec["category"], "textures/skill/%s/%s.png" % (rec.get("tier"), path))
        for n in (ns, "tensura"):
            cand = "%s:%s" % (n, base)
            if self.res.asset_path(cand):
                return cand
        return "tensura:" + base

    def attributes(self, cls) -> list:
        out = []
        chain = self._chain(cls)
        c = self.ix.resolve(chain[-1].superclass, chain[-1]) if chain and chain[-1].superclass else None
        # include DefaultRace-style helpers that apply config stats
        while c is not None and c.simple in ("DefaultRace",):
            chain.append(c)
            c = self.ix.resolve(c.superclass, c) if c.superclass else None
        for c in chain:
            for n in walk(c.node):
                if n.type != "method_invocation":
                    continue
                name = text(n.child_by_field_name("name"))
                if name not in ("addHeldAttributeModifier", "addAttributeModifier", "addOrReplacePermanentModifier", "addTransientModifier"):
                    continue
                a = call_args(n)
                if name in ("addHeldAttributeModifier", "addAttributeModifier") and len(a) >= 3:
                    attr = text(a[0]).split(".")[-1].replace("_", " ").title()
                    amount = self.describe(a[-2], c, self.ix.locals_env(n, c, cls.fqcn))
                    op = text(a[-1]).split(".")[-1]
                    out.append({"attribute": attr, "amount": amount, "operation": op})
                elif len(a) == 1 and a[0].type == "object_creation_expression":
                    aa = call_args(a[0])
                    tgt = n.child_by_field_name("object")
                    attr = text(tgt)
                    if len(aa) >= 3:
                        out.append({"attribute": attr, "amount": self.describe(aa[1], c), "operation": text(aa[2]).split(".")[-1]})
        uniq = []
        for o in out:
            if o not in uniq:
                uniq.append(o)
        return uniq[:20]

    # --------------------------------------------------------------- races
    def race(self, reg: Reg, ns: str, race_tags: dict) -> dict:
        ix = self.ix
        cls = ix.classes.get(reg.cls)
        path = reg.id
        full = "%s:%s" % (ns, path)
        name, name_key = self.lang_name(ns, "race", path, cls)
        rec = {"id": full, "ns": ns, "path": path, "name": name,
               "description": self.res.tr("%s.race.%s.description" % (ns, path)), "class": reg.cls}
        if cls is None:
            return rec
        # difficulty / alignment
        diff = None
        for arg in reg.ctor_args:
            mm = re.search(r"Difficulty\.([A-Z_]+)", text(arg))
            if mm:
                diff = mm.group(1)
        if diff is None:
            gd = ix.find_method(cls, "getDifficulty")
            if gd is not None:
                for r in gd.returns():
                    mm = re.search(r"Difficulty\.([A-Z_]+)", text(r))
                    if mm:
                        diff = mm.group(1)
        if diff is None:
            c = cls
            depth = 0
            while c is not None and diff is None and depth < 10:
                for m in c.methods.get("<init>", []):
                    if m.params:
                        continue
                    mm = re.search(r"(?:this|super)\([^;]*Difficulty\.([A-Z_]+)", m.src)
                    if mm:
                        diff = mm.group(1)
                c = ix.resolve(c.superclass, c) if c.superclass else None
                depth += 1
        rec["difficulty"] = diff.title() if diff else None
        ga = ix.find_method(cls, "getAlignment")
        if ga is not None:
            for r in ga.returns():
                mm = re.search(r"Alignment\.([A-Z_]+)", text(r))
                if mm:
                    rec["alignment"] = mm.group(1).title()
        # evolutions
        evo = {}
        for key, mname in (("next", "getNextEvolutions"), ("default", "getDefaultEvolution"),
                           ("awakening", "getAwakeningEvolution"), ("harvest_festival", "getHarvestFestivalEvolution"),
                           ("previous", "getPreviousEvolutions")):
            m = ix.find_method(cls, mname)
            if m is None:
                continue
            ids = self.rr.refs(m.body, m.cls, ("race",))
            ids = [i for i in ids if i != full]
            if ids:
                evo[key] = ids
        rec["evolutions"] = evo
        # requirements
        rec["requirements"] = self.requirements(cls)
        # skills
        for key, mname in (("intrinsic", "getIntrinsicSkills"), ("learnable", "getIntrinsicLearnable")):
            ids = []
            c = cls
            depth = 0
            while c is not None and depth < 10:
                m = c.method(mname)
                if m is not None:
                    for i in self.rr.refs(m.body, c, ("skill",)):
                        if i not in ids:
                            ids.append(i)
                    if "super." + mname not in m.src:
                        break
                c = ix.resolve(c.superclass, c) if c.superclass else None
                depth += 1
            rec[key] = ids
        # traits from tags + damage immunities
        rec["tags"] = sorted(race_tags.get(full, []))
        traits = []
        for t in rec["tags"]:
            tn = t.split(":")[-1].split("/")[-1]
            if tn in RACE_TAG_TRAITS:
                traits.append(RACE_TAG_TRAITS[tn])
        oh = ix.find_method(cls, "onHurt")
        if oh is not None and oh.cls in self._chain(cls):
            for mm in re.finditer(r"DamageTypeTags\.([A-Z_]+)", oh.src):
                traits.append("Damage handling for %s" % mm.group(1).replace("IS_", "").replace("_", " ").lower())
        rec["traits"] = sorted(set(traits))
        rec["attributes"] = self.attributes(cls)
        rec["config"] = self.config_links(cls)
        rec["icon"] = None
        return rec

    def requirements(self, cls) -> list:
        # TR: Nightmares routes through getNightmareEvolutionRequirements; others override
        # getEvolutionRequirements directly. Take the first that yields anything.
        for mname in ("getNightmareEvolutionRequirements", "getEvolutionRequirements"):
            m = self.ix.find_method(cls, mname)
            if m is None:
                continue
            out = self._reqs_in(m, cls, {}, 0)
            if out:
                return out
        return []

    def _is_req_class(self, rc):
        return rc is not None and (self.ix.is_a(rc, "EvolutionRequirement") or rc.simple == "EvolutionRequirement")

    def _reqs_in(self, m, cls, penv, depth):
        out = []
        body = m.body
        if body is None:
            return out
        for n in walk(body):
            if n.type == "object_creation_expression":
                rc = self.ix.resolve(text(n.child_by_field_name("type")), m.cls)
                if not self._is_req_class(rc):
                    continue
                env = self.ix.locals_env(n, m.cls, cls.fqcn)
                env.update(penv)
                weight = None
                par = n.parent
                if par is not None and par.type == "argument_list":
                    sib = list(par.named_children)
                    i = sib.index(n) if n in sib else -1
                    if 0 <= i < len(sib) - 1:
                        weight = self.describe(sib[i + 1], m.cls, env)
                out.append({"text": self.requirement_text(n, m.cls, env), "weight": weight})
            elif n.type == "method_invocation" and depth < 3:
                target = self._helper_target(n, m.cls)
                if target is None or target is m:
                    continue
                env = self.ix.locals_env(n, m.cls, cls.fqcn)
                env.update(penv)
                env2 = {"__this__": cls.fqcn}
                for pn, a in zip(target.params, call_args(n)):
                    try:
                        env2[pn] = self.ix.eval(a, m.cls, env)
                    except Exception:
                        pass
                out += self._reqs_in(target, cls, env2, depth + 1)
        return out

    def _helper_target(self, inv, ctx):
        """A called method whose declared return type mentions EvolutionRequirement."""
        name = text(inv.child_by_field_name("name"))
        if name in ("getNightmareEvolutionRequirements", "getEvolutionRequirements", "put", "of", "putAll"):
            return None
        obj = inv.child_by_field_name("object")
        owner = ctx
        if obj is not None and text(obj) != "this":
            owner = self.ix.resolve(text(obj), ctx)
            if owner is None:
                return None
        argc = len(call_args(inv))
        c = owner
        while c is not None:
            for cand in c.methods.get(name, []):
                head = text(cand.node).split("{", 1)[0]
                if len(cand.params) == argc and "EvolutionRequirement" in head:
                    return cand
            c = self.ix.resolve(c.superclass, c) if c.superclass else None
        return None

    def requirement_text(self, creation, ctx, env=None) -> str:
        ix = self.ix
        self._env = env
        ty = text(creation.child_by_field_name("type"))
        rc = ix.resolve(ty, ctx)
        args = call_args(creation)
        if rc is None:
            return "%s(%s)" % (ty.split(".")[-1], ", ".join(self._arg_str(a, ctx) for a in args))
        comp = ix.find_method(rc, "getRequirementComponent")
        anon = [c for c in creation.children if c.type == "class_body"]
        comp_node = comp.node if comp is not None else None
        if anon:
            # anonymous subclass: new EvolutionRequirement() { getRequirementComponent() {...} }
            for mdecl in anon[0].named_children:
                if mdecl.type == "method_declaration" and text(mdecl.child_by_field_name("name")) == "getRequirementComponent":
                    comp_node = mdecl
                    rc = ctx
        if comp_node is None:
            return ty.split(".")[-1]
        keys = self.translatable_keys(comp_node, rc)
        self._comp_locals = {}
        for n in walk(comp_node):
            if n.type == "local_variable_declaration":
                for d in n.named_children:
                    if d.type == "variable_declarator" and d.child_by_field_name("value") is not None:
                        self._comp_locals[text(d.child_by_field_name("name"))] = d.child_by_field_name("value")
        if not keys:
            return _humanize_class(rc.simple)
        # map ctor params -> call-site args
        ctor = None
        for cm in rc.methods.get("<init>", []):
            if len(cm.params) == len(args):
                ctor = cm
        field_to_arg = {}
        if ctor is not None:
            for n in walk(ctor.node):
                if n.type == "assignment_expression":
                    lt = text(n.child_by_field_name("left")).replace("this.", "")
                    rt = text(n.child_by_field_name("right"))
                    if rt in ctor.params:
                        field_to_arg[lt] = args[ctor.params.index(rt)]
        # pick the translatable key; for ternaries on a boolean field, choose the branch
        key, targs, node = keys[0]
        if len(keys) > 1:
            for n in walk(comp_node):
                if n.type == "ternary_expression":
                    cond = text(n.child_by_field_name("condition"))
                    fld = re.sub(r"^this\.|\(\)$|^is|^get", "", cond.replace("this.", "")).strip("()")
                    fld = fld[:1].lower() + fld[1:]
                    if fld in field_to_arg:
                        val = ix.try_eval(field_to_arg[fld], ctx)
                        branch = n.child_by_field_name("consequence" if val else "alternative")
                        ks = self.translatable_keys(branch, rc)
                        if ks:
                            key, targs, node = ks[0]
                    break
        tmpl = self.res.tr(key) or key
        vals = []
        for ta in targs:
            if ta.type == "array_creation_expression":
                init = [c for c in ta.named_children if c.type == "array_initializer"]
                items = init[0].named_children if init else []
            else:
                items = [ta]
            for it in items:
                vals.append(self._template_arg(it, rc, field_to_arg, ctx))
        return _fill(tmpl, vals)

    def _template_arg(self, node, rc, field_to_arg, ctx):
        s = text(node)
        loc = getattr(self, "_comp_locals", {}).get(s)
        if loc is not None:
            node, s = loc, text(loc)
        # nested translatable
        for k, _a, _n in self.translatable_keys(node, rc):
            return self.res.tr(k) or k
        for fld, argn in field_to_arg.items():
            cap = fld[:1].upper() + fld[1:]
            if re.search(r"\b(this\.)?(%s\b|get%s\(\)|is%s\(\))" % (re.escape(fld), re.escape(cap), re.escape(cap)), s):
                return self._arg_str(argn, ctx)
        return self._arg_str(node, rc)

    def _arg_str(self, node, ctx):
        refs = self.rr.refs(node, ctx)
        if refs:
            return "[[%s]]" % refs[0]
        d = self.describe(node, ctx, getattr(self, "_env", None))
        return d if d is not None else text(node)


def _fill(tmpl: str, vals: list) -> str:
    i = 0
    out = tmpl

    def rep(m):
        nonlocal i
        idx = m.group(1)
        if idx:
            j = int(idx) - 1
        else:
            j = i
            i += 1
        return str(vals[j]) if j < len(vals) else m.group(0)

    out = re.sub(r"%(?:(\d+)\$)?[sd]", rep, out)
    return clean(out)


def _humanize_class(n: str) -> str:
    n = re.sub(r"Requirement$", "", n)
    return re.sub(r"(?<!^)([A-Z])", r" \1", n)


def _compact(src: str, limit: int) -> str:
    lines = [l.rstrip() for l in src.splitlines() if l.strip()]
    s = "\n".join(lines)
    return s if len(s) <= limit else s[:limit] + "\n   ..."
