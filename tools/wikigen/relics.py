"""Relics (SSKirillSS) ability/stat definitions: `constructDefaultRelicData()`.

Used for Relics, More Relics and RAR-Compat (which turns Artifacts items into relics).
"""
from __future__ import annotations

import re
from typing import Optional

from .javaindex import JavaIndex, JClass, text, walk, call_args
from .resources import Resources, clean


def _chain_calls(node):
    """Flatten a builder chain into [(name, args, node)] from the root outwards."""
    calls = []
    cur = node
    while cur is not None and cur.type == "method_invocation":
        calls.append((text(cur.child_by_field_name("name")), call_args(cur), cur))
        cur = cur.child_by_field_name("object")
    calls.reverse()
    return calls


def _find_builder(node, name):
    """Find the outermost chain whose root call is X.builder(...) with X == name."""
    for n in walk(node):
        if n.type == "method_invocation":
            calls = _chain_calls(n)
            if calls and calls[0][0] == "builder":
                obj = calls[0][2].child_by_field_name("object")
                if obj is not None and text(obj).endswith(name) and n.parent is not None and n.parent.type != "method_invocation":
                    return calls
    return None


def parse_relic(ix: JavaIndex, cls: JClass) -> Optional[dict]:
    m = cls.method("constructDefaultRelicData")
    if m is None:
        return None
    rets = m.returns()
    if not rets:
        return None
    root = rets[0]
    calls = _chain_calls(root)
    out = {"abilities": [], "leveling": None, "loot": []}
    for name, args, node in calls:
        if name == "abilities" and args:
            out["abilities"] = _abilities(ix, cls, args[0])
        elif name == "leveling" and args:
            a = args[0]
            if a.type == "object_creation_expression":
                vals = [ix.try_eval(x, cls) for x in call_args(a)]
                out["leveling"] = {"initial_cost": vals[0] if vals else None,
                                   "max_level": vals[1] if len(vals) > 1 else None,
                                   "step": vals[2] if len(vals) > 2 else None}
            else:
                lv = {}
                for nm, aa, _ in _chain_calls(a):
                    if nm in ("initialCost", "maxLevel", "step") and aa:
                        lv[{"initialCost": "initial_cost", "maxLevel": "max_level", "step": "step"}[nm]] = ix.try_eval(aa[0], cls)
                out["leveling"] = lv or None
        elif name == "loot" and args:
            for n in walk(args[0]):
                if n.type == "field_access" and text(n).startswith("LootEntries."):
                    out["loot"].append(text(n).split(".", 1)[1])
    return out


def _abilities(ix, cls, node):
    abilities = []
    calls = _chain_calls(node)
    for name, args, _n in calls:
        if name != "ability" or not args:
            continue
        ab = {"id": None, "required_level": 0, "max_level": None, "cast": None, "stats": []}
        for nm, aa, _ in _chain_calls(args[0]):
            if nm == "builder" and aa:
                ab["id"] = ix.try_eval(aa[0], cls)
            elif nm == "requiredLevel" and aa:
                ab["required_level"] = ix.try_eval(aa[0], cls)
            elif nm == "maxLevel" and aa:
                ab["max_level"] = ix.try_eval(aa[0], cls)
            elif nm == "active" and aa:
                mm = re.search(r"CastType\.([A-Z_]+)", text(aa[0]))
                ab["cast"] = mm.group(1).title() if mm else "Active"
            elif nm == "stat" and aa:
                ab["stats"].append(_stat(ix, cls, aa[0]))
        abilities.append(ab)
    return abilities


def _stat(ix, cls, node):
    st = {"id": None, "initial": None, "upgrade": None, "format": None, "thresholds": None}
    for nm, aa, _ in _chain_calls(node):
        if nm == "builder" and aa:
            st["id"] = ix.try_eval(aa[0], cls)
        elif nm == "initialValue" and aa:
            st["initial"] = [ix.try_eval(a, cls) for a in aa[:2]]
        elif nm == "upgradeModifier" and len(aa) >= 2:
            mm = re.search(r"UpgradeOperation\.([A-Z_]+)", text(aa[0]))
            st["upgrade"] = {"op": mm.group(1) if mm else text(aa[0]), "value": ix.try_eval(aa[1], cls)}
        elif nm == "formatValue" and aa:
            st["format"] = aa[0]
        elif nm == "thresholdValue" and aa:
            st["thresholds"] = [ix.try_eval(a, cls) for a in aa[:2]]
    return st


def fmt(ix, cls, st, value):
    """Apply a stat's formatValue lambda to a number."""
    lam = st.get("format")
    if lam is None or value is None:
        return value
    try:
        params = lam.child_by_field_name("parameters")
        pname = text(params).strip("()") if params is not None else "value"
        body = lam.child_by_field_name("body")
        if body.type == "block":
            rets = [c for c in walk(body) if c.type == "return_statement"]
            if not rets:
                return value
            body = rets[0].named_children[0]
        v = ix.eval(body, cls, {pname: value})
        return v
    except Exception:
        return value


def _n(v):
    if isinstance(v, bool) or v is None:
        return str(v)
    if isinstance(v, (int, float)):
        if float(v) == int(v):
            return str(int(v))
        return ("%.3f" % v).rstrip("0").rstrip(".")
    return str(v)


def stat_summary(ix, cls, st, max_level):
    ini = st.get("initial") or [None, None]
    a, b = ini[0], ini[1] if len(ini) > 1 else ini[0]
    fa, fb = fmt(ix, cls, st, a), fmt(ix, cls, st, b)
    base = _n(fa) if fa == fb else "%s-%s" % (_n(fa), _n(fb))
    up = st.get("upgrade") or {}
    op, val = up.get("op"), up.get("value")
    per = None
    maxv = None
    lo, hi = 0.0, float("inf")  # Relics clamps to [Double.MIN_VALUE, Double.MAX_VALUE] by default
    th = st.get("thresholds")
    if th and all(isinstance(x, (int, float)) for x in th):
        lo, hi = th[0], th[1]
    if isinstance(val, (int, float)) and isinstance(a, (int, float)) and isinstance(b, (int, float)) and max_level and val:
        sign = "+" if val > 0 else "-"
        if op == "MULTIPLY_BASE":
            per = "%s%s%% of base per level" % (sign, _n(abs(val) * 100))
            ma, mb = a + a * val * max_level, b + b * val * max_level
        elif op == "MULTIPLY_TOTAL":
            per = "x%s per level" % _n(1 + val)
            ma, mb = a * (1 + val) ** max_level, b * (1 + val) ** max_level
        elif op == "ADD":
            fv = fmt(ix, cls, st, abs(val))
            per = "%s%s per level" % (sign, _n(fv if fv is not None else abs(val)))
            ma, mb = a + val * max_level, b + val * max_level
        else:
            ma = mb = None
        if ma is not None:
            ma, mb = min(max(ma, lo), hi), min(max(mb, lo), hi)
            fma, fmb = fmt(ix, cls, st, ma), fmt(ix, cls, st, mb)
            maxv = _n(fma) if fma == fmb else "%s-%s" % (_n(fma), _n(fmb))
    return {"id": st.get("id"), "base": base, "per_level": per, "max": maxv}


def render_description(res: Resources, key: str, stats: list) -> Optional[str]:
    t = res.tr(key)
    if t is None:
        return None
    vals = []
    for s in stats:
        v = s["base"]
        if s.get("max"):
            v = "%s (up to %s)" % (v, s["max"])
        vals.append(v)

    def rep(m):
        i = int(m.group(1)) - 1
        return "**%s**" % vals[i] if 0 <= i < len(vals) else m.group(0)

    t = re.sub(r"%(\d+)\$s", rep, t)
    t = t.replace("%%", "%")
    return clean(t)
