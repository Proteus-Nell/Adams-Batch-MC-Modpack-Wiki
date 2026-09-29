"""Index of decompiled Java sources, built with tree-sitter.

The index knows every class across all decompiled mods, how simple names
resolve to fully-qualified names, class hierarchies, fields and methods.
It also ships a small constant evaluator so extractors can read literal
defaults (numbers, strings, enum constants, arrays) out of the code.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from typing import Iterable, Optional

import tree_sitter as ts
import tree_sitter_java as tsj

JAVA = ts.Language(tsj.language())
_PARSER = ts.Parser(JAVA)


def text(node) -> str:
    return node.text.decode("utf-8", "replace") if node is not None else ""


def walk(node) -> Iterable:
    stack = [node]
    while stack:
        n = stack.pop()
        yield n
        stack.extend(reversed(n.children))


def fix_mojibake(s: str) -> str:
    """Repair UTF-8 text that was decoded as cp1252 somewhere in the mod's build."""
    if not isinstance(s, str) or not any(m in s for m in ("\u00e2\u20ac", "\u00c3", "\u00c2")):
        return s
    try:
        return s.encode("cp1252").decode("utf-8")
    except Exception:
        return s


def unquote(lit: str) -> str:
    return fix_mojibake(_unquote(lit))


def _unquote(lit: str) -> str:
    s = lit
    if s.startswith('"""'):
        return s[3:-3]
    if s.startswith('"') and s.endswith('"'):
        s = s[1:-1]
    elif s.startswith("'") and s.endswith("'"):
        s = s[1:-1]
    try:
        return bytes(s, "utf-8").decode("unicode_escape").encode("latin-1").decode("utf-8")
    except Exception:
        return s.replace('\\"', '"').replace("\\n", "\n").replace("\\\\", "\\")


@dataclass
class JMethod:
    name: str
    node: object
    params: list
    cls: "JClass"

    @property
    def body(self):
        return self.node.child_by_field_name("body")

    @property
    def src(self) -> str:
        return text(self.node)

    def returns(self) -> list:
        """All return expressions in the method body (not in nested lambdas/classes)."""
        out = []
        body = self.body
        if body is None:
            return out
        stack = [body]
        while stack:
            n = stack.pop()
            if n.type in ("lambda_expression", "class_body") and n is not body:
                continue
            if n.type == "return_statement":
                expr = [c for c in n.named_children]
                if expr:
                    out.append(expr[0])
                continue
            stack.extend(reversed(n.children))
        return out


@dataclass
class JField:
    name: str
    type: str
    node: object
    value: object
    modifiers: str
    annotations: dict
    cls: "JClass"


@dataclass
class JClass:
    fqcn: str
    simple: str
    pkg: str
    mod: str
    path: str
    node: object
    kind: str
    superclass: Optional[str]
    interfaces: list
    imports: dict
    star_imports: list
    outer: Optional["JClass"] = None
    fields: dict = field(default_factory=dict)
    methods: dict = field(default_factory=dict)
    inner: dict = field(default_factory=dict)
    enum_constants: list = field(default_factory=list)

    def method(self, name: str) -> Optional[JMethod]:
        m = self.methods.get(name)
        return m[0] if m else None

    @property
    def src(self) -> str:
        return text(self.node)

    def top(self) -> "JClass":
        c = self
        while c.outer is not None:
            c = c.outer
        return c


@dataclass(frozen=True)
class InstanceOf:
    """Stands for `new X()` / a config object whose instance-field defaults we can read."""
    fqcn: str


class JavaIndex:
    def __init__(self):
        self.classes: dict[str, JClass] = {}
        self.by_simple: dict[str, list[JClass]] = {}
        self.by_pkg: dict[str, dict[str, JClass]] = {}
        self._cache: dict = {}
        self._resolving: set = set()
        self._anc_cache: dict = {}
        # "pkg.Owner.FIELD" -> default value, for ModConfigSpec values read with .get()
        self.config_defaults: dict = {}

    # ------------------------------------------------------------------ build
    def add_tree(self, root: str, mod: str, skip: tuple = ("/client/", "/mixin/")):
        for dirpath, _dirs, files in os.walk(root):
            for fn in files:
                if not fn.endswith(".java"):
                    continue
                p = os.path.join(dirpath, fn)
                rel = p.replace("\\", "/")
                if any(s in rel for s in skip) and "/config/" not in rel:
                    continue
                try:
                    self.add_file(p, mod)
                except Exception as e:  # pragma: no cover - best effort
                    print("parse failed", p, e)

    def add_file(self, path: str, mod: str):
        src = open(path, "rb").read()
        tree = _PARSER.parse(src)
        root = tree.root_node
        pkg = ""
        imports: dict[str, str] = {}
        stars: list[str] = []
        for c in root.children:
            if c.type == "package_declaration":
                pkg = text(c).replace("package", "").strip().rstrip(";").strip()
            elif c.type == "import_declaration":
                t = text(c).replace("import", "", 1).strip().rstrip(";").strip()
                if t.startswith("static "):
                    t = t[len("static "):].strip()
                    if not t.endswith(".*"):
                        imports["static:" + t.rsplit(".", 1)[1]] = t
                    continue
                if t.endswith(".*"):
                    stars.append(t[:-2])
                else:
                    imports[t.rsplit(".", 1)[-1]] = t
        for c in root.children:
            if c.type in ("class_declaration", "interface_declaration", "enum_declaration", "record_declaration", "annotation_type_declaration"):
                self._add_class(c, pkg, mod, path, imports, stars, None)

    def _add_class(self, node, pkg, mod, path, imports, stars, outer):
        name = text(node.child_by_field_name("name"))
        fq = (outer.fqcn + "." + name) if outer else (pkg + "." + name if pkg else name)
        sup = node.child_by_field_name("superclass")
        sup_name = None
        if sup is not None:
            tn = [c for c in sup.named_children]
            if tn:
                sup_name = _strip_generics(text(tn[0]))
        ifaces = []
        ic = node.child_by_field_name("interfaces")
        if ic is None:
            for c in node.children:
                if c.type in ("super_interfaces", "extends_interfaces"):
                    ic = c
        if ic is not None:
            for t in walk(ic):
                if t.type in ("type_identifier", "scoped_type_identifier", "generic_type") and t.parent.type == "type_list":
                    ifaces.append(_strip_generics(text(t)))
        kind = node.type.replace("_declaration", "")
        jc = JClass(fq, name, pkg, mod, path, node, kind, sup_name, ifaces, imports, stars, outer)
        self.classes[fq] = jc
        self.by_simple.setdefault(name, []).append(jc)
        if outer is None:
            self.by_pkg.setdefault(pkg, {})[name] = jc
        else:
            outer.inner[name] = jc
        body = node.child_by_field_name("body")
        if body is None:
            return jc
        for m in body.children:
            if m.type == "enum_body_declarations":
                for mm in m.children:
                    self._member(jc, mm, pkg, mod, path, imports, stars)
            elif m.type == "enum_constant":
                jc.enum_constants.append((text(m.child_by_field_name("name")), m))
            else:
                self._member(jc, m, pkg, mod, path, imports, stars)
        return jc

    def _member(self, jc, m, pkg, mod, path, imports, stars):
        if m.type in ("class_declaration", "interface_declaration", "enum_declaration", "record_declaration"):
            self._add_class(m, pkg, mod, path, imports, stars, jc)
        elif m.type in ("field_declaration", "constant_declaration"):
            mods = ""
            annotations = {}
            for c in m.children:
                if c.type == "modifiers":
                    mods = text(c)
                    for a in c.children:
                        if a.type in ("annotation", "marker_annotation"):
                            an = text(a.child_by_field_name("name"))
                            args = a.child_by_field_name("arguments")
                            annotations[an] = args
            ty = _strip_generics(text(m.child_by_field_name("type")))
            for d in m.children:
                if d.type == "variable_declarator":
                    fname = text(d.child_by_field_name("name"))
                    jc.fields[fname] = JField(fname, ty, m, d.child_by_field_name("value"), mods, annotations, jc)
        elif m.type in ("method_declaration", "constructor_declaration"):
            name = text(m.child_by_field_name("name"))
            if m.type == "constructor_declaration":
                name = "<init>"
            params = []
            fp = m.child_by_field_name("parameters")
            if fp is not None:
                for p in fp.named_children:
                    if p.type in ("formal_parameter", "spread_parameter"):
                        params.append(text(p.child_by_field_name("name")) or text(p.named_children[-1]))
            jc.methods.setdefault(name, []).append(JMethod(name, m, params, jc))
        elif m.type == "static_initializer":
            jc.methods.setdefault("<clinit>", []).append(JMethod("<clinit>", m, [], jc))

    # -------------------------------------------------------------- resolve
    def resolve(self, name: Optional[str], ctx: Optional[JClass]) -> Optional[JClass]:
        if not name:
            return None
        key = (name, ctx.fqcn if ctx is not None else None)
        if key in self._cache:
            return self._cache[key]
        if key in self._resolving:
            return None
        self._resolving.add(key)
        try:
            r = self._resolve(name, ctx)
        finally:
            self._resolving.discard(key)
        self._cache[key] = r
        return r

    def _resolve(self, name: str, ctx: Optional[JClass]) -> Optional[JClass]:
        name = _strip_generics(name)
        if name in self.classes:
            return self.classes[name]
        parts = name.split(".")
        head = self._resolve_simple(parts[0], ctx) if ctx else None
        if head is None:
            # Maybe a qualified name with package prefix.
            for i in range(len(parts), 0, -1):
                cand = ".".join(parts[:i])
                if cand in self.classes:
                    head = self.classes[cand]
                    parts = [cand] + parts[i:]
                    break
            if head is None:
                return None
        cur = head
        for p in parts[1:]:
            nxt = self._inner_lookup(cur, p)
            if nxt is None:
                return None
            cur = nxt
        return cur

    def _inner_lookup(self, cls: JClass, name: str, depth=0) -> Optional[JClass]:
        if name in cls.inner:
            return cls.inner[name]
        if depth > 8:
            return None
        sup = self.resolve(cls.superclass, cls) if cls.superclass else None
        if sup is not None:
            r = self._inner_lookup(sup, name, depth + 1)
            if r:
                return r
        for i in cls.interfaces:
            ic = self.resolve(i, cls)
            if ic is not None:
                r = self._inner_lookup(ic, name, depth + 1)
                if r:
                    return r
        return None

    def _resolve_simple(self, name: str, ctx: JClass) -> Optional[JClass]:
        c = ctx
        while c is not None:
            if c.simple == name:
                return c
            if name in c.inner:
                return c.inner[name]
            c = c.outer
        top = ctx.top()
        if name in top.imports:
            fq = top.imports[name]
            if fq in self.classes:
                return self.classes[fq]
            # imported inner class like a.b.Outer.Inner
            r = self.resolve(fq, None)
            if r:
                return r
            return None
        pk = self.by_pkg.get(ctx.pkg, {})
        if name in pk:
            return pk[name]
        for s in top.star_imports:
            fq = s + "." + name
            if fq in self.classes:
                return self.classes[fq]
        # inherited inner classes
        c = ctx
        while c is not None:
            r = self._inner_lookup(c, name)
            if r:
                return r
            c = c.outer
        return None

    def qualified_name(self, name: str, ctx: JClass) -> str:
        """Best-effort FQCN for a type name, even if the class is not indexed."""
        r = self.resolve(name, ctx)
        if r is not None:
            return r.fqcn
        top = ctx.top()
        head = name.split(".")[0]
        if head in top.imports:
            return top.imports[head] + name[len(head):]
        return name

    def ancestors(self, cls: JClass) -> list[str]:
        """FQCNs (or best-effort names) of all superclasses and interfaces."""
        if cls.fqcn in self._anc_cache:
            return self._anc_cache[cls.fqcn]
        out = []
        seen = set()
        stack = [cls]
        while stack:
            c = stack.pop()
            for n in ([c.superclass] if c.superclass else []) + list(c.interfaces):
                q = self.qualified_name(n, c)
                if q in seen:
                    continue
                seen.add(q)
                out.append(q)
                r = self.resolve(n, c)
                if r is not None:
                    stack.append(r)
        self._anc_cache[cls.fqcn] = out
        return out

    def is_a(self, cls: JClass, fqcn_or_simple: str) -> bool:
        for a in self.ancestors(cls):
            if a == fqcn_or_simple or a.rsplit(".", 1)[-1] == fqcn_or_simple:
                return True
        return False

    def find_method(self, cls: JClass, name: str, depth=0) -> Optional[JMethod]:
        """Method lookup walking up the superclass chain."""
        c = cls
        while c is not None and depth < 20:
            m = c.method(name)
            if m is not None:
                return m
            c = self.resolve(c.superclass, c) if c.superclass else None
            depth += 1
        return None

    def find_field(self, cls: JClass, name: str) -> Optional[JField]:
        c = cls
        depth = 0
        while c is not None and depth < 20:
            if name in c.fields:
                return c.fields[name]
            for i in c.interfaces:
                ic = self.resolve(i, c)
                if ic is not None and name in ic.fields:
                    return ic.fields[name]
            nxt = self.resolve(c.superclass, c) if c.superclass else None
            if nxt is None and c.outer is not None:
                nxt = c.outer
            c = nxt
            depth += 1
        return None

    # ------------------------------------------------------------ evaluate
    def eval(self, node, ctx: JClass, env: Optional[dict] = None, depth: int = 0):
        """Evaluate a constant expression. Returns a python value or raises Unknown."""
        if node is None:
            raise Unknown("none")
        if depth > 25:
            raise Unknown("depth")
        t = node.type
        s = text(node)
        if t == "decimal_integer_literal" or t == "hex_integer_literal" or t == "octal_integer_literal" or t == "binary_integer_literal":
            v = s.rstrip("lL").replace("_", "")
            return int(v, 0) if not v.startswith("0") or v in ("0",) or v.startswith(("0x", "0X", "0b", "0B")) else int(v, 8)
        if t == "decimal_floating_point_literal":
            v = s.rstrip("fFdD").replace("_", "")
            return float(v)
        if t in ("string_literal", "text_block"):
            return unquote(s)
        if t == "character_literal":
            return unquote(s)
        if t == "true":
            return True
        if t == "false":
            return False
        if t == "null_literal":
            return None
        if t == "this":
            tc = (env or {}).get("__this__")
            if tc:
                return InstanceOf(tc)
            return InstanceOf(ctx.fqcn)
        if t == "parenthesized_expression":
            return self.eval(node.named_children[0], ctx, env, depth + 1)
        if t == "cast_expression":
            ty = text(node.child_by_field_name("type"))
            try:
                v = self.eval(node.child_by_field_name("value"), ctx, env, depth + 1)
            except Unknown:
                rc = self.resolve(ty, ctx)
                if rc is not None:
                    return InstanceOf(rc.fqcn)
                raise
            if ty in ("int", "long", "short", "byte") and isinstance(v, (int, float)):
                return int(v)
            if ty in ("float", "double") and isinstance(v, (int, float)):
                return float(v)
            return v
        if t == "unary_expression":
            op = text(node.child_by_field_name("operator"))
            v = self.eval(node.child_by_field_name("operand"), ctx, env, depth + 1)
            if op == "-":
                return -v
            if op == "+":
                return v
            if op == "!":
                return not v
            if op == "~":
                return ~v
            raise Unknown(op)
        if t == "binary_expression":
            op = text(node.child_by_field_name("operator"))
            ln, rn = node.child_by_field_name("left"), node.child_by_field_name("right")
            if op in ("!=", "==") and (rn.type == "null_literal" or ln.type == "null_literal"):
                other = ln if rn.type == "null_literal" else rn
                ov = self.eval(other, ctx, env, depth + 1)
                return (ov is not None) if op == "!=" else (ov is None)
            a = self.eval(ln, ctx, env, depth + 1)
            b = self.eval(rn, ctx, env, depth + 1)
            if op == "+":
                if isinstance(a, str) or isinstance(b, str):
                    return fmt_java(a) + fmt_java(b)
                return a + b
            if op == "-":
                return a - b
            if op == "*":
                return a * b
            if op == "/":
                if isinstance(a, int) and isinstance(b, int):
                    return int(a / b)
                return a / b
            if op == "%":
                return a % b
            if op == "<<":
                return a << b
            if op == ">>":
                return a >> b
            if op == "|":
                return a | b
            if op == "&":
                return a & b
            if op == "&&":
                return a and b
            if op == "||":
                return a or b
            if op == "==":
                return a == b
            if op == "!=":
                return a != b
            if op == "<":
                return a < b
            if op == ">":
                return a > b
            if op == "<=":
                return a <= b
            if op == ">=":
                return a >= b
            raise Unknown(op)
        if t == "ternary_expression":
            try:
                c = self.eval(node.child_by_field_name("condition"), ctx, env, depth + 1)
            except Unknown:
                # null-guards like `cfg != null ? cfg.X : new X()` - take the value if both agree
                a = b = None
                try:
                    a = self.eval(node.child_by_field_name("consequence"), ctx, env, depth + 1)
                except Unknown:
                    pass
                try:
                    b = self.eval(node.child_by_field_name("alternative"), ctx, env, depth + 1)
                except Unknown:
                    pass
                if a is not None and (a == b or b is None and isinstance(a, InstanceOf)):
                    return a
                if isinstance(a, InstanceOf) and isinstance(b, InstanceOf) and a.fqcn == b.fqcn:
                    return a
                raise
            return self.eval(node.child_by_field_name("consequence" if c else "alternative"), ctx, env, depth + 1)
        if t == "identifier":
            if env is not None and s in env:
                return env[s]
            f = self.find_field(ctx, s)
            if f is not None and f.value is None and "static" not in f.modifiers:
                v = self._assigned_value(f, depth)
                if v is not _NOVAL:
                    return v
            if f is not None and f.value is not None:
                try:
                    return self.eval(f.value, f.cls, None, depth + 1)
                except Unknown:
                    rc = self.resolve(f.type, f.cls)
                    if rc is not None and rc.kind == "class":
                        return InstanceOf(rc.fqcn)
                    raise
            top = ctx.top()
            if ("static:" + s) in top.imports:
                fq = top.imports["static:" + s]
                owner, fname = fq.rsplit(".", 1)
                oc = self.resolve(owner, None)
                if oc is not None:
                    ff = self.find_field(oc, fname)
                    if ff is not None and ff.value is not None:
                        return self.eval(ff.value, ff.cls, None, depth + 1)
            raise Unknown(s)
        if t == "field_access":
            obj = node.child_by_field_name("object")
            fname = text(node.child_by_field_name("field"))
            if text(obj) == "this" and env is not None and ("this." + fname) in env:
                return env["this." + fname]
            if text(obj) == "this":
                tc = self.classes.get((env or {}).get("__this__")) or ctx
                ff = self.find_field(tc, fname) or self.find_field(ctx, fname)
                if ff is not None and ff.value is None:
                    v = self._assigned_value(ff, depth)
                    if v is not _NOVAL:
                        return v
            if obj.type != "identifier" or self.find_field(ctx, text(obj)) is not None or (env and text(obj) in env):
                try:
                    ov = self.eval(obj, ctx, env, depth + 1)
                except Unknown:
                    ov = None
                if isinstance(ov, InstanceOf):
                    oc2 = self.classes.get(ov.fqcn)
                    if oc2 is not None:
                        ff = self.find_field(oc2, fname)
                        if ff is not None and ff.value is not None:
                            try:
                                return self.eval(ff.value, ff.cls, None, depth + 1)
                            except Unknown:
                                rc = self.resolve(ff.type, ff.cls)
                                if rc is not None:
                                    return InstanceOf(rc.fqcn)
                                raise
                    raise Unknown(s)
            oc = self.resolve(text(obj), ctx)
            if oc is not None:
                if oc.kind == "enum" and any(n == fname for n, _ in oc.enum_constants):
                    return EnumConst(oc.simple, fname)
                ff = self.find_field(oc, fname)
                if ff is not None and ff.value is not None:
                    return self.eval(ff.value, ff.cls, None, depth + 1)
                raise Unknown(s)
            if s in JAVA_CONSTANTS:
                return JAVA_CONSTANTS[s]
            # Unknown owner (e.g. vanilla enums like Operation.ADD_VALUE)
            if re.fullmatch(r"[A-Z][A-Za-z0-9_]*(\.[A-Z][A-Za-z0-9_]*)*\.[A-Z0-9_]+", s):
                return EnumConst(text(obj).rsplit(".", 1)[-1], fname)
            raise Unknown(s)
        if t == "array_creation_expression":
            init = node.child_by_field_name("value")
            if init is None:
                for c in node.children:
                    if c.type == "array_initializer":
                        init = c
            if init is None:
                raise Unknown("array")
            return [self.eval(c, ctx, env, depth + 1) for c in init.named_children]
        if t == "array_initializer":
            return [self.eval(c, ctx, env, depth + 1) for c in node.named_children]
        if t == "method_invocation":
            name = text(node.child_by_field_name("name"))
            objn = node.child_by_field_name("object")
            obj = text(objn)
            args = node.child_by_field_name("arguments")
            argv = args.named_children if args is not None else []
            if name in ("get", "getAsDouble", "getAsInt", "getAsBoolean", "getRaw") and not argv and objn is not None:
                key = self._field_key(objn, ctx)
                if key and key in self.config_defaults:
                    return self.config_defaults[key]
            if name in ("floatValue", "doubleValue", "intValue", "longValue", "booleanValue") and not argv and objn is not None:
                v = self.eval(objn, ctx, env, depth + 1)
                if name == "intValue" or name == "longValue":
                    return int(v)
                if name in ("floatValue", "doubleValue"):
                    return float(v)
                return v
            if objn is not None and name in ("replace", "toLowerCase", "toUpperCase", "trim", "concat", "formatted", "strip", "substring") and obj not in ("String",):
                try:
                    sv = self.eval(objn, ctx, env, depth + 1)
                except Unknown:
                    sv = None
                if isinstance(sv, str):
                    av = [self.eval(a, ctx, env, depth + 1) for a in argv]
                    if name == "replace" and len(av) == 2:
                        return sv.replace(str(av[0]), str(av[1]))
                    if name == "toLowerCase":
                        return sv.lower()
                    if name == "toUpperCase":
                        return sv.upper()
                    if name in ("trim", "strip"):
                        return sv.strip()
                    if name == "concat" and av:
                        return sv + str(av[0])
                    if name == "substring" and av:
                        return sv[av[0]:av[1]] if len(av) > 1 else sv[av[0]:]
                    if name == "formatted":
                        try:
                            return sv % tuple(av)
                        except Exception:
                            raise Unknown(s)
            if name == "format" and obj == "String" and argv:
                fmt_ = self.eval(argv[0], ctx, env, depth + 1)
                av = [self.eval(a, ctx, env, depth + 1) for a in argv[1:]]
                try:
                    return re.sub(r"%(\d+\$)?[sd]", "%s", fmt_) % tuple(fmt_java(x) for x in av)
                except Exception:
                    raise Unknown(s)
            if name == "round" and obj in ("MathUtils", "MathHelper") and len(argv) == 2:
                x = self.eval(argv[0], ctx, env, depth + 1)
                n = self.eval(argv[1], ctx, env, depth + 1)
                return round(float(x), int(n))
            if name in ("ceil", "floor") and obj in ("Mth",) and argv:
                import math
                return int(getattr(math, name)(self.eval(argv[0], ctx, env, depth + 1)))
            if name in ("max", "min", "abs", "round", "floor", "ceil", "pow", "sqrt") and obj in ("Math", "Mth", "MathUtils") and argv:
                vals = [self.eval(a, ctx, env, depth + 1) for a in argv]
                import math
                fn = {"max": max, "min": min, "abs": abs, "round": round, "floor": math.floor, "ceil": math.ceil, "pow": pow, "sqrt": math.sqrt}[name]
                return fn(*vals)
            if name in ("of", "asList", "newArrayList", "copyOf") and obj in ("List", "Set", "Arrays", "Lists", "ImmutableList", "ImmutableSet", "Sets"):
                vals = []
                for a in argv:
                    v = self.eval(a, ctx, env, depth + 1)
                    vals.append(v)
                return vals
            if name == "valueOf" and obj in ("Integer", "Double", "Float", "Long", "Boolean", "String") and argv:
                return self.eval(argv[0], ctx, env, depth + 1)
            if name in ("fromNamespaceAndPath", "tryBuild") and len(argv) == 2:
                return "%s:%s" % (self.eval(argv[0], ctx, env, depth + 1), self.eval(argv[1], ctx, env, depth + 1))
            if name in ("parse", "withDefaultNamespace", "tryParse") and len(argv) == 1 and obj in ("ResourceLocation",):
                v = self.eval(argv[0], ctx, env, depth + 1)
                return v if ":" in v else "minecraft:" + v
            if name == "toString" and obj:
                raise Unknown(s)
            if name == "of" and obj in ("Pair", "Tuple", "Map.Entry") and len(argv) == 2:
                return (self.eval(argv[0], ctx, env, depth + 1), self.eval(argv[1], ctx, env, depth + 1))
            if name in ("getFirst", "getLeft", "getKey", "first", "left") and not argv and objn is not None:
                v = self.eval(objn, ctx, env, depth + 1)
                if isinstance(v, tuple):
                    return v[0]
            if name in ("getSecond", "getRight", "getValue", "second", "right") and not argv and objn is not None:
                v = self.eval(objn, ctx, env, depth + 1)
                if isinstance(v, tuple):
                    return v[1]
            # zero-argument getters on `this`, an implicit receiver, a class (static) or a known instance
            if not argv:
                target = None
                if objn is None or obj == "this":
                    tc = (env or {}).get("__this__")
                    target = self.classes.get(tc) if tc else ctx
                else:
                    ov = None
                    if objn.type == "identifier" and self.find_field(ctx, obj) is None and not (env and obj in env):
                        target = self.resolve(obj, ctx)
                    if target is None:
                        try:
                            ov = self.eval(objn, ctx, env, depth + 1)
                        except Unknown:
                            ov = None
                    if isinstance(ov, InstanceOf):
                        target = self.classes.get(ov.fqcn)
                if target is not None:
                    m = self.find_method(target, name)
                    if m is not None and not m.params:
                        rets = m.returns()
                        if len(rets) == 1:
                            e2 = self.locals_env(rets[0], m.cls, target.fqcn) if depth < 12 else {"__this__": target.fqcn}
                            return self.eval(rets[0], m.cls, e2, depth + 1)
                        vals = {repr(self.eval(r, m.cls, {"__this__": target.fqcn}, depth + 1)) for r in rets}
                        if len(vals) == 1:
                            return self.eval(rets[0], m.cls, {"__this__": target.fqcn}, depth + 1)
            if name in ("secondsToTicks",) and argv:
                return int(self.eval(argv[0], ctx, env, depth + 1) * 20)
            if argv and depth < 20 and (objn is None or obj == "this"):
                # instance helper on `this`, e.g. readTierValue("minAura", this.minAura)
                tc = self.classes.get((env or {}).get("__this__")) or ctx
                cand = None
                c = tc
                while c is not None and cand is None:
                    for mm in c.methods.get(name, []):
                        if len(mm.params) == len(argv) and "static" not in text(mm.node).split("(")[0]:
                            cand = mm
                    c = self.resolve(c.superclass, c) if c.superclass else None
                if cand is not None:
                    src_ = cand.src
                    if ("getDeclaredField" in src_ or "getField(" in src_) and argv:
                        fname_ = self.eval(argv[0], ctx, env, depth + 1)
                        if isinstance(fname_, str):
                            ff = self.find_field(tc, fname_)
                            if ff is not None and ff.value is not None:
                                return self.eval(ff.value, ff.cls, {"__this__": tc.fqcn}, depth + 1)
                            if len(argv) > 1:
                                return self.eval(argv[1], ctx, env, depth + 1)
                    rets = cand.returns()
                    if len(rets) == 1:
                        e2 = {pn: self.eval(a, ctx, env, depth + 1) for pn, a in zip(cand.params, argv)}
                        e2["__this__"] = tc.fqcn
                        return self.eval(rets[0], cand.cls, e2, depth + 1)
            if argv and depth < 20:
                owner = None
                if objn is None:
                    owner = ctx
                elif objn.type == "identifier" and self.find_field(ctx, obj) is None and not (env and obj in env):
                    owner = self.resolve(obj, ctx)
                if owner is not None:
                    cand = None
                    c = owner
                    while c is not None and cand is None:
                        for mm in c.methods.get(name, []):
                            if len(mm.params) == len(argv) and "static" in text(mm.node).split("(")[0]:
                                cand = mm
                        c = c.outer
                    if cand is not None:
                        rets = cand.returns()
                        if len(rets) == 1:
                            e2 = {pn: self.eval(a, ctx, env, depth + 1) for pn, a in zip(cand.params, argv)}
                            return self.eval(rets[0], cand.cls, e2, depth + 1)
            raise Unknown(s)
        if t == "object_creation_expression":
            rc = self.resolve(text(node.child_by_field_name("type")), ctx)
            if rc is not None and not call_args(node):
                return InstanceOf(rc.fqcn)
            raise Unknown(s)
        raise Unknown(t)

    def _assigned_value(self, f, depth):
        """Value of a field that has no initializer but is assigned in a method (lazy caches)."""
        if depth > 18:
            return _NOVAL
        base = f.type.split(".")[-1]
        if not base[:1].isupper() or base in ("String", "Integer", "Double", "Float", "Long", "Boolean", "List", "Map", "Set",
                                               "UUID", "Component", "ItemStack", "LivingEntity", "Player", "Entity", "Level"):
            return _NOVAL
        key = (f.cls.fqcn, f.name)
        cache = self.__dict__.setdefault("_assign_cache", {})
        if key in cache:
            return cache[key]
        cache[key] = _NOVAL  # guards against cycles while we compute
        cache[key] = self._assigned_value_uncached(f, depth)
        return cache[key]

    def _assigned_value_uncached(self, f, depth):
        for ms in f.cls.methods.values():
            for m in ms:
                if f.name not in m.src:
                    continue
                for n in walk(m.node):
                    if n.type != "assignment_expression":
                        continue
                    lt = text(n.child_by_field_name("left"))
                    if lt not in (f.name, "this." + f.name):
                        continue
                    rhs = n.child_by_field_name("right")
                    try:
                        return self.eval(rhs, f.cls, self.locals_env(n, f.cls), depth + 1)
                    except Unknown:
                        continue
        return _NOVAL

    def locals_env(self, node, ctx, this_fqcn=None) -> dict:
        """Evaluate local variables declared before `node` in its enclosing method."""
        env = {"__this__": this_fqcn or ctx.fqcn}
        m = node
        while m is not None and m.type not in ("method_declaration", "constructor_declaration", "lambda_expression"):
            m = m.parent
        if m is None:
            return env
        for n in walk(m):
            if n.type == "local_variable_declaration" and n.start_byte < node.start_byte:
                for d in n.named_children:
                    if d.type == "variable_declarator" and d.child_by_field_name("value") is not None:
                        try:
                            env[text(d.child_by_field_name("name"))] = self.eval(d.child_by_field_name("value"), ctx, env)
                        except Exception:
                            pass
        return env

    def _field_key(self, node, ctx):
        """'pkg.Owner.FIELD' for an expression naming a static field."""
        if node.type == "identifier":
            f = self.find_field(ctx, text(node))
            return (f.cls.fqcn + "." + f.name) if f else None
        if node.type == "field_access":
            objn = node.child_by_field_name("object")
            fname = text(node.child_by_field_name("field"))
            if objn.type not in ("identifier", "this") or (objn.type == "identifier" and self.find_field(ctx, text(objn)) is not None):
                try:
                    ov = self.eval(objn, ctx, None)
                except Exception:
                    ov = None
                if isinstance(ov, InstanceOf):
                    oc2 = self.classes.get(ov.fqcn)
                    f = self.find_field(oc2, fname) if oc2 else None
                    return (f.cls.fqcn + "." + f.name) if f else ov.fqcn + "." + fname
            if objn.type == "field_access":
                # e.g. NightmareRacesConfig.INSTANCE.EPToTrueDwarf -> type of INSTANCE
                inner_owner = self.resolve(text(objn.child_by_field_name("object")), ctx)
                if inner_owner is not None:
                    inst = self.find_field(inner_owner, text(objn.child_by_field_name("field")))
                    if inst is not None:
                        tc = self.resolve(inst.type, inst.cls)
                        if tc is not None:
                            f = self.find_field(tc, fname)
                            return (f.cls.fqcn + "." + f.name) if f else tc.fqcn + "." + fname
            oc = self.resolve(text(objn), ctx)
            if oc is not None:
                f = self.find_field(oc, fname)
                return (f.cls.fqcn + "." + f.name) if f else oc.fqcn + "." + fname
            # this.field
            if text(node.child_by_field_name("object")) == "this":
                f = self.find_field(ctx, fname)
                return (f.cls.fqcn + "." + f.name) if f else None
        return None

    def try_eval(self, node, ctx, env=None, default=None):
        try:
            return self.eval(node, ctx, env)
        except Unknown:
            return default
        except Exception:
            return default


JAVA_CONSTANTS = {
    "Double.MAX_VALUE": 1.7976931348623157e308, "Double.MIN_VALUE": 5e-324,
    "Float.MAX_VALUE": 3.4028235e38, "Float.MIN_VALUE": 1.4e-45,
    "Integer.MAX_VALUE": 2147483647, "Integer.MIN_VALUE": -2147483648,
    "Long.MAX_VALUE": 9223372036854775807, "Long.MIN_VALUE": -9223372036854775808,
    "Short.MAX_VALUE": 32767, "Byte.MAX_VALUE": 127,
    "Math.PI": 3.141592653589793,
    "Double.POSITIVE_INFINITY": float("inf"), "Float.POSITIVE_INFINITY": float("inf"),
}


_NOVAL = object()


class Unknown(Exception):
    pass


@dataclass(frozen=True)
class EnumConst:
    owner: str
    name: str

    def __str__(self):
        return self.name


def fmt_java(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, float):
        if v == int(v) and abs(v) < 1e15:
            return "%.1f" % v
        return repr(v)
    return str(v)


def _strip_generics(s: str) -> str:
    out = []
    depth = 0
    for ch in s:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        elif depth == 0:
            out.append(ch)
    return "".join(out).replace("[]", "").strip()


def string_literals(node) -> list:
    return [unquote(text(n)) for n in walk(node) if n.type == "string_literal"]


def method_invocations(node, name: Optional[str] = None) -> list:
    out = []
    for n in walk(node):
        if n.type == "method_invocation":
            if name is None or text(n.child_by_field_name("name")) == name:
                out.append(n)
    return out


def call_args(inv) -> list:
    a = inv.child_by_field_name("arguments")
    return list(a.named_children) if a is not None else []
