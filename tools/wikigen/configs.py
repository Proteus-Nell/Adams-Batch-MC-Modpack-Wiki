"""Config extraction.

Two config systems cover almost every mod in the pack:

* ManasConfig (ManasCore): plain Java classes whose fields hold the defaults,
  documented with @Comment. Nested ManasSubConfig fields become TOML tables.
* NeoForge ModConfigSpec: builder code (`push`, `comment`, `define...`). We
  run that code through a tiny interpreter that tracks the section path and
  evaluates literal arguments.

Every option is returned as a dict:
    {file, path: [...], key, default, min, max, allowed, comment, type,
     owner: fqcn, field: "Owner.FIELD" or None}
"""
from __future__ import annotations

import re
from typing import Optional

from .javaindex import (JavaIndex, JClass, Unknown, EnumConst, text, walk,
                        call_args, unquote)

BUILDER_METHODS = {
    "comment", "push", "pop", "translation", "worldRestart", "gameRestart",
    "define", "defineInRange", "defineEnum", "defineList", "defineListAllowEmpty",
    "defineInList", "build", "configure", "defineInRangeLong", "defineMap",
}
DEFINE_METHODS = {"define", "defineInRange", "defineEnum", "defineList", "defineListAllowEmpty", "defineInList", "defineInRangeLong"}


def jsonable(v):
    if isinstance(v, EnumConst):
        return v.name
    if isinstance(v, (list, tuple)):
        return [jsonable(x) for x in v]
    if isinstance(v, float) and v != v:
        return None
    return v


# --------------------------------------------------------------- ManasConfig
def manas_configs(ix: JavaIndex, mod_src_keys: set) -> list:
    out = []
    for cls in list(ix.classes.values()):
        if cls.mod not in mod_src_keys or cls.outer is not None:
            continue
        if not ix.is_a(cls, "ManasConfig"):
            continue
        fm = cls.method("getFileName")
        fname = None
        if fm is not None:
            for r in fm.returns():
                fname = ix.try_eval(r, cls)
        if fname is None:
            continue
        sync = "@SyncToClient" in cls.src.split("class", 1)[0]
        _manas_fields(ix, cls, "config/%s.toml" % fname, [], out, sync)
    return out


def _is_subconfig(ix, cls):
    return cls is not None and ix.is_a(cls, "ManasSubConfig")


def _init_overrides(ix, value_node, ctx) -> dict:
    """Field values set when a sub-config is built by a factory or constructor.

    Handles `X field = factory();` where factory does `t = new X(); t.a = 1; return t;`
    and `X field = new X(1, 2)` where the constructor assigns `this.a = a`.
    """
    out = {}
    if value_node is None:
        return out
    v = value_node
    if v.type == "method_invocation":
        name = text(v.child_by_field_name("name"))
        obj = v.child_by_field_name("object")
        owner = ix.resolve(text(obj), ctx) if obj is not None else ctx
        c = owner
        m = None
        while c is not None and m is None:
            for cand in c.methods.get(name, []):
                if len(cand.params) == len(call_args(v)):
                    m = cand
            c = c.outer
        if m is None or m.body is None:
            return out
        rets = m.returns()
        var = text(rets[0]) if rets else None
        env = {}
        for pn, a in zip(m.params, call_args(v)):
            try:
                env[pn] = ix.eval(a, ctx)
            except Exception:
                pass
        for n in walk(m.body):
            if n.type == "assignment_expression":
                lt = text(n.child_by_field_name("left"))
                if var and lt.startswith(var + "."):
                    try:
                        out[lt[len(var) + 1:]] = ix.eval(n.child_by_field_name("right"), m.cls, env)
                    except Exception:
                        pass
        return out
    if v.type == "object_creation_expression":
        args = call_args(v)
        tc = ix.resolve(text(v.child_by_field_name("type")), ctx)
        if tc is None or not args:
            return out
        for ctor in tc.methods.get("<init>", []):
            if len(ctor.params) != len(args):
                continue
            env = {}
            for pn, a in zip(ctor.params, args):
                try:
                    env[pn] = ix.eval(a, ctx)
                except Exception:
                    pass
            for n in walk(ctor.node):
                if n.type == "assignment_expression":
                    lt = text(n.child_by_field_name("left")).replace("this.", "")
                    try:
                        out[lt] = ix.eval(n.child_by_field_name("right"), tc, env)
                    except Exception:
                        pass
            break
    return out


def _manas_fields(ix, cls: JClass, file, path, out, sync, depth=0, preset=None):
    if depth > 6:
        return
    preset = preset or {}
    chain = []
    c = cls
    while c is not None and c.simple not in ("ManasSubConfig", "ManasConfig"):
        chain.append(c)
        c = ix.resolve(c.superclass, c) if c.superclass else None
    # Walk parents first so the field order matches the TOML, but let a subclass
    # that redeclares a field (e.g. LesserDragon.minAura over DragonTier.minAura)
    # supply the default.
    order = []
    owner_of = {}
    for c in reversed(chain):
        for fname, f in c.fields.items():
            if "static" in f.modifiers:
                continue
            if fname not in owner_of:
                order.append(fname)
            owner_of[fname] = (c, f)
    for fname in order:
        c, f = owner_of[fname]
        ftype = ix.resolve(f.type, c)
        if _is_subconfig(ix, ftype):
            comment = _annotation_comment(ix, f)
            if comment:
                out.append({"file": file, "path": path + [fname], "key": None, "section_comment": comment, "owner": ftype.fqcn})
            _manas_fields(ix, ftype, file, path + [fname], out, sync, depth + 1, _init_overrides(ix, f.value, c))
            continue
        if fname in preset:
            default = preset[fname]
        else:
            default = ix.try_eval(f.value, c, {"__this__": cls.fqcn}, default=_Missing)
        if default is _Missing:
            default = text(f.value) if f.value is not None else None
        out.append({
            "file": file, "path": path, "key": fname, "default": jsonable(default),
            "type": f.type, "comment": _annotation_comment(ix, f),
            "owner": cls.fqcn, "field": cls.fqcn + "." + fname, "sync": sync,
        })


class _MissingT:
    pass


_Missing = _MissingT()


def _annotation_comment(ix, f) -> Optional[str]:
    a = f.annotations.get("Comment")
    if a is None:
        return None
    vals = []
    for n in a.named_children:
        v = ix.try_eval(n, f.cls)
        if isinstance(v, list):
            vals.extend(str(x) for x in v)
        elif v is not None:
            vals.append(str(v))
        elif n.type == "element_value_pair":
            vv = ix.try_eval(n.child_by_field_name("value"), f.cls)
            if vv is not None:
                vals.append(str(vv) if not isinstance(vv, list) else "\n".join(map(str, vv)))
        elif n.type == "element_value_array_initializer":
            for x in n.named_children:
                xv = ix.try_eval(x, f.cls)
                if xv is not None:
                    vals.append(str(xv))
    return "\n".join(vals) if vals else None


# ------------------------------------------------------------ ModConfigSpec
class _State:
    def __init__(self, path=None):
        self.path = list(path or [])
        self.comment = None
        self.translation = None


class SpecInterpreter:
    def __init__(self, ix: JavaIndex, out: list):
        self.ix = ix
        self.out = out
        self.seen_methods = set()

    def run_method(self, m, env=None, state=None, builder_names=None, depth=0):
        if depth > 6:
            return None
        body = m.body if m.name != "<clinit>" else [c for c in m.node.children if c.type == "block"][0]
        if body is None:
            return None
        env = dict(env or {})
        state = state or _State()
        names = set(builder_names or ())
        names |= {"BUILDER", "builder", "b", "COMMON_BUILDER", "SERVER_BUILDER", "CLIENT_BUILDER", "configBuilder", "BUILDER_COMMON", "BUILDER_CLIENT", "BUILDER_SERVER", "cfg", "config"}
        # parameters typed Builder
        fp = m.node.child_by_field_name("parameters")
        if fp is not None:
            for p in fp.named_children:
                if "Builder" in text(p.child_by_field_name("type") or p):
                    names.add(text(p.child_by_field_name("name")))
        ret = self._block(body, m.cls, env, state, names, depth)
        return ret

    def _block(self, block, cls, env, state, names, depth):
        ret = None
        for st in block.named_children:
            r = self._stmt(st, cls, env, state, names, depth)
            if r is not None:
                ret = r
        return ret

    def _stmt(self, st, cls, env, state, names, depth):
        t = st.type
        if t == "block":
            return self._block(st, cls, env, state, names, depth)
        if t == "expression_statement":
            e = st.named_children[0] if st.named_children else None
            if e is not None:
                self._expr(e, cls, env, state, names, depth, target=None)
            return None
        if t == "local_variable_declaration":
            ty = text(st.child_by_field_name("type"))
            for d in st.named_children:
                if d.type == "variable_declarator":
                    vn = text(d.child_by_field_name("name"))
                    val = d.child_by_field_name("value")
                    if val is None:
                        continue
                    if "Builder" in ty and "new" in text(val):
                        names.add(vn)
                        continue
                    res = self._expr(val, cls, env, state, names, depth, target=(cls.fqcn, vn, True))
                    if res is not None and isinstance(res, dict):
                        env[vn] = res
                    else:
                        try:
                            env[vn] = self.ix.eval(val, cls, env)
                        except Exception:
                            pass
            return None
        if t == "return_statement":
            if st.named_children:
                return self._expr(st.named_children[0], cls, env, state, names, depth, target=None)
            return None
        if t == "if_statement":
            cons = st.child_by_field_name("consequence")
            alt = st.child_by_field_name("alternative")
            if cons is not None:
                self._stmt(cons, cls, env, state, names, depth)
            if alt is not None:
                self._stmt(alt, cls, env, state, names, depth)
            return None
        if t == "enhanced_for_statement":
            var = text(st.child_by_field_name("name"))
            it = st.child_by_field_name("value")
            body = st.child_by_field_name("body")
            vals = None
            try:
                vals = self.ix.eval(it, cls, env)
            except Exception:
                vals = None
            if isinstance(vals, list) and len(vals) <= 400:
                for v in vals:
                    env2 = dict(env)
                    env2[var] = v
                    self._stmt(body, cls, env2, state, names, depth)
            elif self._mentions_builder(body, names):
                self._stmt(body, cls, dict(env), state, names, depth)
            return None
        if t in ("for_statement", "while_statement", "try_statement", "synchronized_statement"):
            for c in st.named_children:
                if c.type == "block":
                    self._stmt(c, cls, env, state, names, depth)
            return None
        if t == "explicit_constructor_invocation":
            args = call_args(st)
            if any(text(a) in names for a in args):
                ctor_kw = text(st.named_children[0]) if st.named_children else "super"
                target_cls = cls
                if ctor_kw == "super" or st.children and text(st.children[0]) == "super":
                    target_cls = self.ix.resolve(cls.superclass, cls) if cls.superclass else None
                if target_cls is not None:
                    for cand in target_cls.methods.get("<init>", []):
                        if len(cand.params) == len(args):
                            self._run_inlined(cand, st, args, cls, env, state, names, depth, None)
                            break
            return None
        if t == "switch_expression" or t == "switch_statement":
            return None
        return None

    def _mentions_builder(self, node, names):
        s = text(node)
        return any(n + "." in s for n in names)

    def _chain(self, e):
        """Flatten a.b(x).c(y) into (root_node, [(name, argnodes, invnode), ...])."""
        calls = []
        cur = e
        while cur is not None and cur.type == "method_invocation":
            calls.append((text(cur.child_by_field_name("name")), call_args(cur), cur))
            cur = cur.child_by_field_name("object")
        calls.reverse()
        return cur, calls

    def _expr(self, e, cls, env, state, names, depth, target):
        t = e.type
        if t == "assignment_expression":
            left = e.child_by_field_name("left")
            right = e.child_by_field_name("right")
            ln = text(left)
            if left.type == "field_access":
                owner_txt = text(left.child_by_field_name("object"))
                fname = text(left.child_by_field_name("field"))
                if owner_txt == "this":
                    tgt = (cls.fqcn, fname, False)
                else:
                    oc = self.ix.resolve(owner_txt, cls)
                    tgt = ((oc.fqcn if oc else owner_txt), fname, False)
            else:
                f = self.ix.find_field(cls, ln)
                tgt = ((f.cls.fqcn if f else cls.fqcn), ln, False)
            return self._expr(right, cls, env, state, names, depth, target=tgt)
        if t == "cast_expression":
            return self._expr(e.child_by_field_name("value"), cls, env, state, names, depth, target)
        if t == "parenthesized_expression":
            return self._expr(e.named_children[0], cls, env, state, names, depth, target)
        if t == "object_creation_expression":
            args = call_args(e)
            if any(text(a) in names for a in args):
                ty = text(e.child_by_field_name("type"))
                oc = self.ix.resolve(ty, cls)
                if oc is not None:
                    for cand in oc.methods.get("<init>", []):
                        if len(cand.params) == len(args):
                            return self._run_inlined(cand, e, args, cls, env, state, names, depth, target)
            return None
        if t != "method_invocation":
            return None
        root, calls = self._chain(e)
        root_txt = text(root) if root is not None else ""
        is_builder = (root_txt in names or root_txt.startswith("this.") and root_txt[5:] in names
                      or (root is not None and root.type == "object_creation_expression" and "Builder" in root_txt))
        if not is_builder and root is not None and root.type == "identifier":
            f = self.ix.find_field(cls, root_txt)
            if f is not None and "Builder" in f.type:
                names.add(root_txt)
                is_builder = True
        if is_builder and all(c[0] in BUILDER_METHODS for c in calls):
            return self._builder_calls(calls, cls, env, state, names, depth, target)
        if is_builder and calls and calls[0][0] not in BUILDER_METHODS:
            # a helper defined on a Builder subclass, e.g. BuilderHandler.add(name, comment, default)
            name, args, inv = calls[0]
            m = self._builder_subclass_method(name, len(args), cls)
            if m is not None:
                return self._run_inlined(m, inv, args, cls, env, state, names, depth, target)
        # helper call passing the builder along
        if len(calls) >= 1:
            name, args, inv = calls[-1]
            if any(text(a) in names for a in args):
                return self._inline(inv, name, args, root, cls, env, state, names, depth, target)
        return None

    def _builder_subclass_method(self, name, argc, ctx):
        if not hasattr(self, "_bsub"):
            self._bsub = [c for c in self.ix.classes.values() if c.superclass and c.superclass.split(".")[-1] == "Builder" and "ModConfigSpec" in c.top().src[:4000]]
        for c in self._bsub:
            if c.mod != ctx.mod:
                continue
            for m in c.methods.get(name, []):
                if len(m.params) == argc:
                    return m
        return None

    def _eval(self, n, cls, env):
        try:
            return self.ix.eval(n, cls, env)
        except Unknown:
            return _Unk(text(n))
        except Exception:
            return _Unk(text(n))

    def _builder_calls(self, calls, cls, env, state, names, depth, target):
        result = None
        for name, args, inv in calls:
            if name == "comment":
                vals = []
                for a in args:
                    v = self._eval(a, cls, env)
                    if isinstance(v, list):
                        vals.extend(str(x) for x in v)
                    elif not isinstance(v, _Unk):
                        vals.append(str(v))
                state.comment = "\n".join(vals) if vals else None
            elif name == "translation":
                v = self._eval(args[0], cls, env) if args else None
                state.translation = v if isinstance(v, str) else None
            elif name == "push":
                v = self._eval(args[0], cls, env) if args else None
                parts = []
                if isinstance(v, list):
                    parts = [str(x) for x in v]
                elif isinstance(v, str):
                    parts = v.split(".")
                else:
                    parts = [str(v)]
                if state.comment:
                    self.out.append({"path": state.path + parts, "key": None, "section_comment": state.comment, "owner": cls.fqcn})
                state.path.extend(parts)
                state.comment = None
                state.translation = None
            elif name == "pop":
                n = 1
                if args:
                    v = self._eval(args[0], cls, env)
                    if isinstance(v, int):
                        n = v
                for _ in range(n):
                    if state.path:
                        state.path.pop()
            elif name in DEFINE_METHODS:
                if not args:
                    continue
                keyv = self._eval(args[0], cls, env)
                if isinstance(keyv, _Unk):
                    # e.g. SynchedEntityData.Builder.define(DATA_X, 0): not a config
                    continue
                if isinstance(keyv, list):
                    kparts = [str(x) for x in keyv]
                elif isinstance(keyv, str):
                    kparts = keyv.split(".")
                else:
                    kparts = [str(keyv)]
                rec = {"path": state.path + kparts[:-1], "key": kparts[-1], "comment": state.comment,
                       "translation": state.translation, "owner": cls.fqcn,
                       "field": ("%s.%s" % (target[0], target[1])) if target and not target[2] else None,
                       "local": target[1] if target and target[2] else None, "method": name}
                if name == "defineInRange" or name == "defineInRangeLong":
                    vals = [self._eval(a, cls, env) for a in args[1:4]]
                    rec["default"] = vals[0] if vals else None
                    rec["min"] = vals[1] if len(vals) > 1 else None
                    rec["max"] = vals[2] if len(vals) > 2 else None
                elif name == "defineEnum":
                    rec["default"] = self._eval(args[1], cls, env) if len(args) > 1 else None
                    ec = None
                    if isinstance(rec["default"], EnumConst):
                        ec = self.ix.resolve(rec["default"].owner, cls)
                    if ec is not None and ec.kind == "enum":
                        rec["allowed"] = [n for n, _ in ec.enum_constants]
                elif name == "defineInList":
                    rec["default"] = self._eval(args[1], cls, env) if len(args) > 1 else None
                    rec["allowed"] = self._eval(args[2], cls, env) if len(args) > 2 else None
                else:
                    if len(args) > 1:
                        d = args[1]
                        if d.type == "lambda_expression":
                            d = d.child_by_field_name("body")
                        rec["default"] = self._eval(d, cls, env)
                    else:
                        rec["default"] = None
                rec["default"] = jsonable(_clean(rec.get("default")))
                for k in ("min", "max", "allowed"):
                    if k in rec:
                        rec[k] = jsonable(_clean(rec[k]))
                self.out.append(rec)
                state.comment = None
                state.translation = None
                result = rec
        return result

    def _inline(self, inv, name, args, root, cls, env, state, names, depth, target):
        # resolve target method
        owner = cls
        if root is not None and root.type in ("identifier", "field_access", "scoped_identifier") and text(root) != "this":
            oc = self.ix.resolve(text(root), cls)
            if oc is None:
                return None
            owner = oc
        m = None
        c = owner
        while c is not None and m is None:
            for cand in c.methods.get(name, []):
                if len(cand.params) == len(args):
                    m = cand
                    break
            c = c.outer if m is None else c
        if m is None:
            return None
        return self._run_inlined(m, inv, args, cls, env, state, names, depth, target)

    def _run_inlined(self, m, inv, args, cls, env, state, names, depth, target):
        key = (m.cls.fqcn, m.name, text(inv)[:200], tuple(state.path))
        if key in self.seen_methods:
            return None
        self.seen_methods.add(key)
        env2 = {}
        bnames = set()
        if m.cls.superclass and m.cls.superclass.split(".")[-1] == "Builder":
            bnames.add("this")
        for pn, a in zip(m.params, args):
            if text(a) in names:
                bnames.add(pn)
            else:
                v = self._eval(a, cls, env)
                if not isinstance(v, _Unk):
                    env2[pn] = v
        res = self.run_method(m, env2, state, bnames, depth + 1)
        if isinstance(res, dict) and target is not None and not target[2]:
            res["field"] = "%s.%s" % (target[0], target[1])
        return res


class _Unk:
    def __init__(self, s):
        self.s = s

    def __repr__(self):
        return "<%s>" % self.s


def _clean(v):
    if isinstance(v, _Unk):
        s = v.s
        return "`%s`" % s if len(s) < 80 else None
    if isinstance(v, list):
        return [_clean(x) for x in v]
    return v


def spec_configs(ix: JavaIndex, mod_src_keys: set) -> list:
    out: list = []
    interp = SpecInterpreter(ix, out)
    helpers_called = set()
    entries = []
    rest = []
    for cls in ix.classes.values():
        if cls.mod not in mod_src_keys:
            continue
        for mname, ms in cls.methods.items():
            for m in ms:
                s = m.src
                has_define = ".define" in s
                creates = ("new Builder()" in s or "new ModConfigSpec.Builder()" in s or "@SubscribeConfig" in s)
                builder_param = m.name == "<init>" and "Builder" in text(m.node.child_by_field_name("parameters") or m.node)
                if (creates and not builder_param) or (m.name in ("<clinit>", "<init>") and not builder_param and "Builder" in s and (has_define or ".push(" in s)):
                    entries.append(m)
                elif has_define or builder_param:
                    rest.append(m)
    # Methods that receive the builder as a parameter are normally reached by
    # inlining from an entry point, which gives them the right section path and
    # argument values. Only leftovers are run on their own.
    for m in entries:
        before = len(out)
        interp.run_method(m)
        for r in out[before:]:
            r.setdefault("entry", m.cls.fqcn)
        helpers_called |= {k[:2] for k in interp.seen_methods}
    for m in rest:
        if (m.cls.fqcn, m.name) in helpers_called:
            continue
        before = len(out)
        interp.run_method(m)
        for r in out[before:]:
            r.setdefault("entry", m.cls.fqcn)
    # dedupe
    seen = set()
    uniq = []
    for r in out:
        k = (tuple(r["path"]), r.get("key"), r.get("owner"))
        if k in seen:
            continue
        seen.add(k)
        uniq.append(r)
    return uniq


def spec_registrations(ix: JavaIndex, mod_src_keys: set, modid: str) -> dict:
    """Map owner-class fqcn -> (type, filename) using registerConfig calls."""
    regs = {}
    for cls in ix.classes.values():
        if cls.mod not in mod_src_keys:
            continue
        for ms in cls.methods.values():
            for m in ms:
                if "registerConfig(" not in m.src:
                    continue
                for n in walk(m.node):
                    if n.type != "method_invocation" or text(n.child_by_field_name("name")) != "registerConfig":
                        continue
                    a = call_args(n)
                    if len(a) < 2:
                        continue
                    ty = text(a[0]).rsplit(".", 1)[-1].lower()
                    if ty not in ("common", "server", "client", "startup"):
                        continue
                    spec = text(a[1])
                    fname = None
                    if len(a) > 2:
                        fname = ix.try_eval(a[2], cls)
                    if not fname:
                        fname = "%s-%s.toml" % (modid, ty)
                    folder = "serverconfig" if ty == "server" else "config"
                    owner = None
                    if "." in spec:
                        oc = ix.resolve(spec.rsplit(".", 1)[0], cls)
                        owner = oc.fqcn if oc else None
                    else:
                        f = ix.find_field(cls, spec)
                        owner = f.cls.fqcn if f else cls.fqcn
                    regs.setdefault(owner, []).append({"type": ty, "file": "%s/%s" % (folder, fname), "spec": spec})
    return regs


# ------------------------------------------------------ Artifacts' own configs
def artifacts_configs(ix: JavaIndex, mod_src_keys: set) -> list:
    """Artifacts: ConfigManager subclasses with Category inner classes."""
    out = []
    for cls in ix.classes.values():
        if cls.mod not in mod_src_keys or cls.outer is not None or not ix.is_a(cls, "ConfigManager"):
            continue
        fname = None
        for m in cls.methods.get("<init>", []):
            for n in walk(m.node):
                if n.type == "explicit_constructor_invocation":
                    a = call_args(n)
                    if a:
                        fname = ix.try_eval(a[0], cls)
        if not isinstance(fname, str):
            continue
        file = "config/artifacts/%s.toml" % fname
        targets = [(cls, [], None)]
        for inner in cls.inner.values():
            sect = None
            item = None
            for m in inner.methods.get("<init>", []):
                for n in walk(m.node):
                    if n.type == "explicit_constructor_invocation":
                        a = call_args(n)
                        if a:
                            v = ix.try_eval(a[0], inner)
                            if isinstance(v, str):
                                sect = v
                            else:
                                mm = re.search(r"ModItems\.([A-Z_]+)", text(a[0]))
                                if mm:
                                    item = "artifacts:" + mm.group(1).lower()
                                    sect = mm.group(1).lower()
            if sect is None:
                # e.g. DrinkingHat(ModItems.X, "..."): section from the field that creates it
                for f in cls.fields.values():
                    if f.value is not None and text(f.value).startswith("new ItemConfigs.%s(" % inner.simple):
                        mm = re.search(r"ModItems\.([A-Z_]+)", text(f.value))
                        if mm:
                            targets.append((inner, [mm.group(1).lower()], "artifacts:" + mm.group(1).lower()))
                continue
            targets.append((inner, [sect], item))
        for c, path, item in targets:
            chain = [c]
            sup = ix.resolve(c.superclass, c) if c.superclass else None
            while sup is not None and sup.simple not in ("Category", "ConfigManager") and len(chain) < 5:
                chain.append(sup)
                sup = ix.resolve(sup.superclass, sup) if sup.superclass else None
            for cc in reversed(chain):
                for fn, f in cc.fields.items():
                    if f.value is None or ".define(" not in text(f.value) and not text(f.value).startswith("this.<"):
                        continue
                    key = default = None
                    desc = []
                    vtype = None
                    for n in walk(f.value):
                        if n.type == "method_invocation":
                            nm = text(n.child_by_field_name("name"))
                            a = call_args(n)
                            if nm == "define" and a:
                                key = ix.try_eval(a[0], cc)
                                default = ix.try_eval(a[-1], cc, default=text(a[-1]))
                                if len(a) == 3:
                                    vtype = text(a[1]).split(".")[-1]
                            elif nm in ("descriptionLine", "comment") and a:
                                v = ix.try_eval(a[0], cc)
                                if isinstance(v, str):
                                    desc.insert(0, v)
                    if not isinstance(key, str):
                        continue
                    out.append({"file": file, "path": path, "key": key, "default": jsonable(default),
                                "type": vtype, "comment": "\n".join(desc) or None, "owner": c.fqcn,
                                "field": c.fqcn + "." + fn, "item": item})
    return out
