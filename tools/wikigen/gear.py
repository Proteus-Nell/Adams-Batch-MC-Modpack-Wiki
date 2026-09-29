"""Weapon and tool stats read from code.

Follows the constructor chain from the registration down to the call that
builds the item's attribute modifiers:

    new SimpleKatanaItem(TensuraToolTiers.ADAMANTITE, props)
      -> super(tier, 4, -2.2F, 0.0, 0.25, 20.0, ...)          (TwoHandedSwordItem)
      -> createAttributes(tier, damage, speed, range, ...)    (TensuraSwordItem)
      -> .add(Attributes.ATTACK_DAMAGE, new AttributeModifier(ID, damage + tier.getAttackDamageBonus(), ADD_VALUE))

and resolves the tier (vanilla Tiers or a mod enum implementing Tier) to its
durability and damage bonus. Values are the numbers the tooltip shows: attack
damage includes the player's base 1, attack speed the base 4.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .javaindex import JavaIndex, JClass, EnumConst, InstanceOf, Unknown, text, walk, call_args

# uses, mining speed, attack damage bonus, enchantability
VANILLA_TIERS = {
    "WOOD": (59, 2.0, 0.0, 15), "STONE": (131, 4.0, 1.0, 5), "IRON": (250, 6.0, 2.0, 14),
    "DIAMOND": (1561, 8.0, 3.0, 10), "GOLD": (32, 12.0, 0.0, 22), "NETHERITE": (2031, 9.0, 4.0, 15),
}
# vanilla createAttributes(tier, damage, speed) helpers
VANILLA_ATTR_HELPERS = ("SwordItem", "DiggerItem", "AxeItem", "PickaxeItem", "ShovelItem", "HoeItem", "TridentItem", "MaceItem")
ATTR_KEYS = {
    "ATTACK_DAMAGE": "attack_damage", "ATTACK_SPEED": "attack_speed", "ENTITY_INTERACTION_RANGE": "reach",
    "SWEEPING_DAMAGE_RATIO": "sweep", "CRITICAL_ATTACK_CHANCE": "crit_chance", "CRITICAL_DAMAGE_MULTIPLIER": "crit_multiplier",
    "ATTACK_KNOCKBACK": "knockback", "BLOCK_INTERACTION_RANGE": "block_reach",
}


@dataclass
class TierVal:
    name: str
    uses: Optional[float] = None
    speed: Optional[float] = None
    damage: Optional[float] = None
    enchant: Optional[float] = None

    GETTERS = {"getUses": "uses", "getSpeed": "speed", "getAttackDamageBonus": "damage", "getEnchantmentValue": "enchant"}


class GearReader:
    def __init__(self, ix: JavaIndex):
        self.ix = ix
        self._tiers = {}

    # ------------------------------------------------------------------ tiers
    def tier(self, v) -> Optional[TierVal]:
        if isinstance(v, TierVal):
            return v
        if isinstance(v, EnumConst):
            key = (v.owner, v.name)
            if key in self._tiers:
                return self._tiers[key]
            t = None
            if v.owner.rsplit(".", 1)[-1] == "Tiers" and v.name in VANILLA_TIERS:
                u, s, d, e = VANILLA_TIERS[v.name]
                t = TierVal(v.name, u, s, d, e)
            else:
                t = self._enum_tier(v)
            self._tiers[key] = t
            return t
        return None

    def enum_class(self, owner: str, const: str) -> Optional[JClass]:
        ec = self.ix.classes.get(owner)
        if ec is not None:
            return ec
        # EnumConst.owner is the simple name as written in the code
        for c in self.ix.classes.values():
            if c.simple == owner and c.kind == "enum" and any(n == const for n, _ in c.enum_constants):
                return c
        return None

    def enum_getter(self, v: EnumConst, getter: str):
        """Value of a zero-arg getter on an enum constant: getX() { return this.x; } with this.x = ctor arg."""
        ec = self.enum_class(v.owner, v.name)
        if ec is None:
            return None
        node = next((n for nm, n in ec.enum_constants if nm == v.name), None)
        m = ec.method(getter)
        if node is None or m is None or node.child_by_field_name("arguments") is None:
            return None
        args = call_args(node)
        rets = m.returns()
        if not rets:
            return None
        fld = text(rets[0]).replace("this.", "")
        for ctor in ec.methods.get("<init>", []):
            if len(ctor.params) != len(args) or ctor.body is None:
                continue
            for n in walk(ctor.body):
                if n.type == "assignment_expression" and text(n.child_by_field_name("left")).replace("this.", "") == fld:
                    rhs = text(n.child_by_field_name("right"))
                    if rhs in ctor.params:
                        try:
                            return self.ix.eval(args[ctor.params.index(rhs)], ec)
                        except Exception:
                            return None
        return None

    def _enum_tier(self, v: EnumConst) -> Optional[TierVal]:
        ec = self.enum_class(v.owner, v.name)
        if ec is None:
            return None
        node = next((n for nm, n in ec.enum_constants if nm == v.name), None)
        if node is None:
            return None
        args = call_args(node) if node.child_by_field_name("arguments") is not None else []
        ctor = next((m for m in ec.methods.get("<init>", []) if len(m.params) == len(args)), None)
        if ctor is None:
            return None
        # this.field = param
        field_param = {}
        for n in walk(ctor.body):
            if n.type == "assignment_expression":
                lhs, rhs = n.child_by_field_name("left"), n.child_by_field_name("right")
                ln = text(lhs).replace("this.", "")
                if text(rhs) in ctor.params:
                    field_param[ln] = ctor.params.index(text(rhs))
        t = TierVal(v.name)
        for getter, attr in TierVal.GETTERS.items():
            m = ec.method(getter)
            fld = None
            if m is not None:
                rets = m.returns()
                if rets:
                    fld = text(rets[0]).replace("this.", "")
            else:
                # lombok @Generated getters are usually present; fall back to the field name
                fld = {"uses": "uses", "speed": "speed", "damage": "damage", "enchant": "enchantmentValue"}[attr]
            idx = field_param.get(fld)
            if idx is None:
                continue
            try:
                val = self.ix.eval(args[idx], ec)
            except Exception:
                continue
            if isinstance(val, (int, float)) and not isinstance(val, bool):
                setattr(t, attr, float(val))
        return t if t.damage is not None or t.uses is not None else None

    # ------------------------------------------------------------ evaluation
    def ev(self, node, ctx, env):
        t = node.type
        if t in ("parenthesized_expression",):
            return self.ev(node.named_children[0], ctx, env)
        if t == "cast_expression":
            return self.ev(node.child_by_field_name("value"), ctx, env)
        if t == "identifier" and node.parent is not None and text(node) in env:
            return env[text(node)]
        if t == "method_invocation":
            obj = node.child_by_field_name("object")
            name = text(node.child_by_field_name("name"))
            if obj is not None and name in TierVal.GETTERS:
                tv = self.tier(self.ev(obj, ctx, env))
                if tv is not None:
                    val = getattr(tv, TierVal.GETTERS[name])
                    if val is None:
                        raise Unknown("tier")
                    return val
            if obj is not None and not call_args(node):
                ov = self._try(obj, ctx, env)
                if isinstance(ov, EnumConst):
                    val = self.enum_getter(ov, name)
                    if val is not None:
                        return val
        if t == "binary_expression":
            op = text(node.child_by_field_name("operator"))
            a = self.ev(node.child_by_field_name("left"), ctx, env)
            b = self.ev(node.child_by_field_name("right"), ctx, env)
            if not all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in (a, b)):
                raise Unknown("op")
            return {"+": lambda: a + b, "-": lambda: a - b, "*": lambda: a * b, "/": lambda: a / b if b else 0}.get(op, lambda: (_ for _ in ()).throw(Unknown(op)))()
        if t == "unary_expression" and text(node).startswith("-"):
            v = self.ev(node.named_children[0], ctx, env)
            if isinstance(v, (int, float)):
                return -v
        plain = {k: v for k, v in env.items() if not isinstance(v, TierVal)}
        return self.ix.eval(node, ctx, plain)

    def _try(self, node, ctx, env):
        try:
            return self.ev(node, ctx, env)
        except Exception:
            return None

    # ----------------------------------------------------------------- walk
    def stats(self, reg) -> dict:
        cls = self.ix.classes.get(reg.cls) if reg.cls else None
        out = {}
        # vanilla style: new SwordItem(Tiers.DIAMOND, props.attributes(SwordItem.createAttributes(Tiers.DIAMOND, 3, -2.4F)))
        self._scan_calls(reg.node, reg.ctx, {}, out, None)
        if cls is not None and reg.ctor_args:
            vals = [self._try(a, reg.ctx, {}) for a in reg.ctor_args]
            self._ctor(cls, vals, out, 0)
        return self._finish(out)

    def _ctor(self, cls: JClass, vals, out, depth):
        if depth > 8 or cls is None:
            return
        for v in vals:
            tv = self.tier(v)
            if tv is not None and "tier" not in out:
                out["tier"] = tv
        ctor = next((m for m in cls.methods.get("<init>", []) if len(m.params) == len(vals)), None)
        if ctor is None or ctor.body is None:
            return
        env = dict(zip(ctor.params, vals))
        self._scan_calls(ctor.body, cls, env, out, cls)
        for n in ctor.body.named_children:
            if n.type != "explicit_constructor_invocation":
                continue
            args = call_args(n)
            svals = [self._try(a, cls, env) for a in args]
            head = text(n).split("(")[0].strip()
            if head == "this":
                self._ctor(cls, svals, out, depth + 1)
            else:
                sup = self.ix.resolve(cls.superclass, cls) if cls.superclass else None
                if sup is not None:
                    self._ctor(sup, svals, out, depth + 1)
                else:
                    simple = (cls.superclass or "").split("<")[0].rsplit(".", 1)[-1]
                    if simple in VANILLA_ATTR_HELPERS and svals and self.tier(svals[0]) is not None:
                        out.setdefault("tier", self.tier(svals[0]))

    def _scan_calls(self, root, ctx, env, out, owner):
        for n in walk(root):
            if n.type != "method_invocation" or text(n.child_by_field_name("name")) != "createAttributes":
                continue
            label = self._label(n)
            if label in out.get("_sets", {}):
                continue
            args = call_args(n)
            vals = [self._try(a, ctx, env) for a in args]
            res = self._create_attributes(n, ctx, vals, owner)
            if res:
                out.setdefault("_sets", {})[label] = res

    def _label(self, n):
        # .component(TensuraDataComponents.ONE_HANDED_MODIFIERS.get(), createAttributes(...))
        p = n.parent
        while p is not None and p.type != "method_invocation":
            p = p.parent
        if p is not None and text(p.child_by_field_name("name")) == "component":
            a = call_args(p)
            if a:
                s = text(a[0]).upper()
                if "ONE_HAND" in s:
                    return "one_handed"
                if "TWO_HAND" in s:
                    return "two_handed"
        return "main"

    def _create_attributes(self, call, ctx, vals, owner):
        obj = call.child_by_field_name("object")
        target = None
        if obj is not None:
            target = self.ix.resolve(text(obj), ctx)
        else:
            c = owner or ctx
            depth = 0
            while c is not None and depth < 8 and target is None:
                if any(len(m.params) == len(vals) for m in c.methods.get("createAttributes", [])):
                    target = c
                    break
                c = self.ix.resolve(c.superclass, c) if c.superclass else None
                depth += 1
        m = None
        if target is not None:
            m = next((mm for mm in target.methods.get("createAttributes", []) if len(mm.params) == len(vals)), None)
        if m is None:
            # vanilla SwordItem/DiggerItem.createAttributes(tier, damage, speed)
            simple = text(obj).rsplit(".", 1)[-1] if obj is not None else ""
            if (simple in VANILLA_ATTR_HELPERS or obj is None) and len(vals) == 3:
                tv = self.tier(vals[0])
                if tv is not None and isinstance(vals[1], (int, float)) and isinstance(vals[2], (int, float)):
                    return {"attack_damage": vals[1] + (tv.damage or 0.0), "attack_speed": vals[2], "_tier": tv}
            return None
        env = dict(zip(m.params, vals))
        res = {}
        for n in walk(m.body):
            if n.type != "method_invocation" or text(n.child_by_field_name("name")) != "add":
                continue
            a = call_args(n)
            if len(a) < 2:
                continue
            key = ATTR_KEYS.get(text(a[0]).rsplit(".", 1)[-1])
            if key is None or a[1].type != "object_creation_expression":
                continue
            ma = call_args(a[1])
            if len(ma) < 2:
                continue
            v = self._try(ma[1], m.cls, env)
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                res[key] = float(v)
        tv = self.tier(vals[0]) if vals else None
        if tv is not None:
            res["_tier"] = tv
        return res

    def _finish(self, out) -> dict:
        sets = out.get("_sets") or {}
        if not sets:
            return {}
        res = {}
        tv = out.get("tier")
        if "two_handed" in sets and sets.get("main") == sets["two_handed"]:
            sets = {k: v for k, v in sets.items() if k != "main"}
        for label, s in sets.items():
            tv = tv or s.get("_tier")
            d = {}
            if "attack_damage" in s:
                d["attack_damage"] = round(1.0 + s["attack_damage"], 2)
            if "attack_speed" in s:
                d["attack_speed"] = round(4.0 + s["attack_speed"], 2)
            for k in ("reach", "block_reach", "sweep", "crit_chance", "crit_multiplier", "knockback"):
                if s.get(k):
                    d[k] = round(s[k], 3)
            res[label] = d
        if tv is not None:
            res["tier"] = tv.name.replace("_", " ").title()
            if tv.uses:
                res["durability"] = int(tv.uses)
            if tv.speed:
                res["mining_speed"] = tv.speed
        return res


# ---------------------------------------------------------------- armor
import re as _re

ARMOR_TYPES = ("HELMET", "CHESTPLATE", "LEGGINGS", "BOOTS", "BODY")
ARMOR_BASE_DURABILITY = {"HELMET": 11, "CHESTPLATE": 16, "LEGGINGS": 15, "BOOTS": 13, "BODY": 16}


def armor_stats(ix: JavaIndex, reg) -> dict:
    """Defense, toughness, knockback resistance and durability for ArmorItem-style items.

    Reads `XArmorMaterials.NAME` from the registration or the item's constructors, then the
    `new ArmorMaterial(Map{Type -> defense}, enchantability, sound, repair, layers, toughness, kbRes)`
    it registers, and the durability multiplier passed up the constructor chain."""
    srcs = [text(reg.node)]
    c = ix.classes.get(reg.cls) if reg.cls else None
    depth = 0
    while c is not None and depth < 6:
        for m in c.methods.get("<init>", []):
            srcs.append(m.src)
        c = ix.resolve(c.superclass, c) if c.superclass else None
        depth += 1
    blob = "\n".join(srcs)
    typ = None
    m = _re.search(r"Type\.(HELMET|CHESTPLATE|LEGGINGS|BOOTS|BODY)\b", srcs[0]) or _re.search(r"Type\.(HELMET|CHESTPLATE|LEGGINGS|BOOTS|BODY)\b", blob)
    if m:
        typ = m.group(1)
    else:
        mm = _re.search(r"_(helmet|chestplate|leggings|boots)(?:_[a-z])?$", reg.id)
        if mm:
            typ = mm.group(1).upper()
    mat = None
    for s in srcs:
        for mm in _re.finditer(r"\b(\w*ArmorMaterials?)\.([A-Z][A-Z0-9_]*)\b", s):
            ctx = reg.ctx if s is srcs[0] else (ix.classes.get(reg.cls) or reg.ctx)
            holder = ix.resolve(mm.group(1), ctx)
            f = holder.fields.get(mm.group(2)) if holder is not None else None
            if f is not None and f.value is not None:
                mat = (mm.group(2), f)
                break
        if mat:
            break
    if typ is None or mat is None:
        return {}
    name, f = mat
    body = next((n for n in walk(f.value) if n.type == "object_creation_expression" and "ArmorMaterial" in text(n.child_by_field_name("type"))), None)
    if body is None:
        return {}
    out = {"material": name.replace("_", " ").title(), "slot": typ.title()}
    for mm in _re.finditer(r"put\(\s*(?:ArmorItem\.)?Type\.([A-Z]+)\s*,\s*(\d+)\s*\)", text(body)):
        if mm.group(1) == typ:
            out["armor"] = int(mm.group(2))
    args = call_args(body)
    nums = []
    for a in args:
        try:
            v = ix.eval(a, f.cls)
        except Exception:
            v = None
        nums.append(v if isinstance(v, (int, float)) and not isinstance(v, bool) else None)
    if len(nums) >= 7:
        if nums[5] is not None:
            out["toughness"] = float(nums[5])
        if nums[6] is not None:
            out["knockback_resistance"] = float(nums[6])
    # durability multiplier: last int literal in a super(MATERIAL, type, props, N) call
    for s in srcs[1:] + srcs[:1]:
        mm = _re.search(r"super\(\s*[\w.]*ArmorMaterials?\.[A-Z_]+\s*,[^;]*?,\s*(\d+)\s*\)\s*;", s)
        if mm:
            out["durability"] = ARMOR_BASE_DURABILITY.get(typ, 0) * int(mm.group(1))
            break
        mm = _re.search(r"getDurability\(\s*(\d+)\s*\)", s)
        if mm:
            out["durability"] = ARMOR_BASE_DURABILITY.get(typ, 0) * int(mm.group(1))
            break
    return out if "armor" in out else {}
