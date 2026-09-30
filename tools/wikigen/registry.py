"""Find registry entries declared in code.

Most mods declare registry objects as static fields:

    public static final RegistrySupplier<GreatSageSkill> GREAT_SAGE = register("great_sage", GreatSageSkill::new);
    public static final DeferredHolder<ManasSkill, CoffinSkill> COFFIN = SKILLS.register("coffin", CoffinSkill::new);
    public static final DeferredItem<Item> RUBY = ITEMS.registerSimpleItem("ruby");

We record the holder field, the registry id, the constructed class (if any)
and the name of the registry the call went through.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import re

from .javaindex import JavaIndex, JClass, text, walk, call_args

_ID = re.compile(r"([a-z0-9_.-]+:)?[a-z0-9_./-]+")


@dataclass
class Reg:
    holder: str          # fqcn.FIELD
    holder_cls: str
    field: str
    id: str              # path, no namespace
    cls: Optional[str]   # fqcn of constructed class
    via: str             # e.g. "SKILLS.register" or "register"
    decl_type: str       # e.g. RegistrySupplier<GreatSageSkill>
    ctor_args: list      # argument nodes passed to the constructor (if any)
    ctx: JClass
    node: object
    ns: str = ""

    @property
    def full_id(self) -> str:
        return "%s:%s" % (self.ns, self.id)


def _namespace(ix: JavaIndex, cls: JClass, inv, rid_raw: str, default: str) -> str:
    if ":" in rid_raw:
        return rid_raw.split(":", 1)[0]
    # DeferredRegister.create(KEY, "ns") on the registry object we called through
    obj = inv.child_by_field_name("object")
    if obj is not None:
        f = ix.find_field(cls, text(obj)) if obj.type == "identifier" else None
        if f is None and obj.type == "field_access":
            oc = ix.resolve(text(obj.child_by_field_name("object")), cls)
            f = ix.find_field(oc, text(obj.child_by_field_name("field"))) if oc else None
        if f is not None and f.value is not None:
            for n in walk(f.value):
                if n.type == "method_invocation" and text(n.child_by_field_name("name")) in ("create", "createItems", "createBlocks", "createDataComponents", "createEntities"):
                    for a in call_args(n):
                        v = ix.try_eval(a, f.cls)
                        if isinstance(v, str) and re.fullmatch(r"[a-z0-9_.-]+", v):
                            return v
    else:
        # helper in the same class: look for fromNamespaceAndPath("ns", ...)
        name = text(inv.child_by_field_name("name"))
        for m in cls.methods.get(name, []):
            for n in walk(m.node):
                if n.type == "method_invocation" and text(n.child_by_field_name("name")) in ("fromNamespaceAndPath", "create"):
                    a = call_args(n)
                    if a:
                        v = ix.try_eval(a[0] if text(n.child_by_field_name("name")) == "fromNamespaceAndPath" else a[-1], cls)
                        if isinstance(v, str) and re.fullmatch(r"[a-z0-9_.-]+", v):
                            return v
    return default


def find_registrations(ix: JavaIndex, mod_keys: set, default_ns: str = "") -> list:
    out = []
    for cls in ix.classes.values():
        if cls.mod not in mod_keys:
            continue
        for fname, f in cls.fields.items():
            if f.value is None or "static" not in f.modifiers:
                continue
            v = f.value
            if v.type == "ternary_expression":
                v = v.child_by_field_name("consequence")
            if v.type == "cast_expression":
                v = v.child_by_field_name("value")
            if v.type != "method_invocation":
                continue
            name = text(v.child_by_field_name("name"))
            args = call_args(v)
            if not args:
                continue
            is_reg_name = name.lower().startswith("register") or name in ("create", "createSimple", "block", "item")
            has_ctor = any(a.type in ("method_reference", "lambda_expression", "object_creation_expression") for a in args[1:])
            if not is_reg_name and not has_ctor:
                continue
            rid = ix.try_eval(args[0], cls)
            if not isinstance(rid, str) or not _ID.fullmatch(rid):
                continue
            ns = _namespace(ix, cls, v, rid, default_ns)
            if ":" in rid:
                rid = rid.split(":", 1)[1]
            obj = v.child_by_field_name("object")
            via = (text(obj) + "." if obj is not None else "") + name
            ctor_cls, ctor_args = _constructed_class(ix, args[1:], cls)
            decl = _raw_type(f.node)
            if ctor_cls is None:
                # e.g. RegistrySupplier<GreatSageSkill>: take the last type argument
                ta = _type_args(decl)
                for t in reversed(ta):
                    rc = ix.resolve(t, cls)
                    if rc is not None:
                        ctor_cls = rc.fqcn
                        break
            out.append(Reg(cls.fqcn + "." + fname, cls.fqcn, fname, rid, ctor_cls, via, decl, ctor_args, cls, v, ns))
    return out


def _raw_type(field_node) -> str:
    t = field_node.child_by_field_name("type")
    return text(t) if t is not None else ""


def _type_args(decl: str) -> list:
    if "<" not in decl:
        return []
    inner = decl[decl.index("<") + 1: decl.rindex(">")]
    depth = 0
    cur = ""
    parts = []
    for ch in inner:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur.strip())
    out = []
    for p in parts:
        out.append(p.split("<")[0].strip())
    return out


def _constructed_class(ix, args, ctx):
    for a in args:
        if a.type == "method_reference":
            parts = [c for c in a.named_children]
            if parts and text(a).endswith("::new"):
                rc = ix.resolve(text(parts[0]), ctx)
                return (rc.fqcn if rc else text(parts[0])), []
        if a.type == "lambda_expression":
            body = a.child_by_field_name("body")
            for n in walk(body):
                if n.type == "object_creation_expression":
                    ty = text(n.child_by_field_name("type"))
                    rc = ix.resolve(ty, ctx)
                    return (rc.fqcn if rc else ty), call_args(n)
            # () -> EntityType.Builder.of(GoblinEntity::new, MobCategory.MONSTER)...build(...)
            for n in walk(body):
                if n.type == "method_reference" and text(n).endswith("::new"):
                    parts = [c for c in n.named_children]
                    rc = ix.resolve(text(parts[0]), ctx) if parts else None
                    if rc is not None:
                        return rc.fqcn, []
        if a.type == "object_creation_expression":
            ty = text(a.child_by_field_name("type"))
            rc = ix.resolve(ty, ctx)
            return (rc.fqcn if rc else ty), call_args(a)
    return None, []


def holder_ref(node) -> Optional[str]:
    """For `UniqueSkills.GREAT_SAGE.get()` (or without .get()) return 'UniqueSkills.GREAT_SAGE'."""
    s = text(node)
    if s.endswith(".get()"):
        s = s[:-6]
    if s.endswith(".value()"):
        s = s[:-8]
    while s.startswith("(") and ")" in s:
        # cast like (ManasSkill)X.Y.get()
        s = s[s.index(")") + 1:]
        if s.endswith(".get()"):
            s = s[:-6]
    return s
