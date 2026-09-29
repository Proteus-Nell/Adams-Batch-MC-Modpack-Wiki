"""Second-chance linking for entries the registry scan missed.

Some mods register things in ways `find_registrations` can't read as static
fields (Corail Tombstone registers inside an event handler, Elite Tensura goes
through obfuscated helpers). Every real entry still has its id written in the
code as a string literal, so we look the literal up and read the class from
the call around it:

    register(event, abandoned_grave = new BlockAbandonedGrave(), "abandoned_grave")
    super("ankh_of_prayer", getBuilder()...)                    (inside ItemAnkhOfPrayer)
    a("forge_station_basic", ForgeTier.BASIC)                    (helper that does `new ForgeStationBlock(...)`)

An id that appears in the lang file but nowhere in the code was never
registered, so it is not in the game ("phantom"). A lang key that the code only
uses as a display name, like `item.enigmaticlegacyplus.etherium_core_active`
inside EtheriumCore.getName(), is an alternate name of that item.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Optional

from .javaindex import JavaIndex, JClass, text, walk, call_args

KIND_HINTS = {
    "item": ("Item",),
    "block": ("Block",),
    "entity": ("Entity", "Mob", "Monster", "Animal", "Boss", "Golem", "Projectile"),
    "effect": ("Effect",),
}


class LiteralLinker:
    def __init__(self, ix: JavaIndex):
        self.ix = ix
        self._idx = {}

    def literals(self, key: str) -> dict:
        """literal value -> [(class, node)] for one jar's code."""
        if key in self._idx:
            return self._idx[key]
        d = defaultdict(list)
        for c in self.ix.classes.values():
            if c.mod != key or c.outer is not None:
                continue
            for n in walk(c.node):
                if n.type == "string_literal":
                    s = text(n)
                    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
                        d[s[1:-1]].append((c, n))
        self._idx[key] = d
        return d

    def mentioned(self, keys, value: str) -> bool:
        return any(value in self.literals(k) for k in keys)

    def owner_of_literal(self, keys, value: str) -> Optional[JClass]:
        """Innermost class whose code contains the literal (for display-name keys)."""
        for k in keys:
            for c, n in self.literals(k).get(value, []):
                return self._enclosing_class(n, c)
        return None

    def _enclosing_class(self, node, top: JClass) -> JClass:
        p = node.parent
        names = []
        while p is not None:
            if p.type in ("class_declaration", "enum_declaration", "record_declaration", "interface_declaration"):
                nm = p.child_by_field_name("name")
                if nm is not None:
                    names.append(text(nm))
            p = p.parent
        names.reverse()
        c = top
        for nm in names[1:]:
            c = c.inner.get(nm, c)
        return c

    def link(self, keys, ident: str, kind: str) -> Optional[str]:
        """Best-effort class for a registry id, by reading the call around its literal."""
        hints = KIND_HINTS.get(kind, ())
        for k in keys:
            for top, n in self.literals(k).get(ident, []):
                ctx = self._enclosing_class(n, top)
                call = n.parent.parent if n.parent is not None and n.parent.type == "argument_list" else None
                if call is None:
                    continue
                if call.type == "explicit_constructor_invocation":
                    if self._fits(ctx, hints):
                        return ctx.fqcn
                    continue
                if call.type not in ("method_invocation", "object_creation_expression"):
                    continue
                if call.type == "object_creation_expression":
                    rc = self.ix.resolve(text(call.child_by_field_name("type")), ctx)
                    if rc is not None and self._fits(rc, hints):
                        return rc.fqcn
                    continue
                for a in call_args(call):
                    rc = self._constructed(a, ctx)
                    if rc is not None and self._fits(rc, hints):
                        return rc.fqcn
                # a helper in the same class: register(name, ...) { ... new X(...) ... }
                name = text(call.child_by_field_name("name"))
                obj = call.child_by_field_name("object")
                if obj is None or text(obj) == "this":
                    for m in ctx.methods.get(name, []):
                        rc = self._constructed(m.body, ctx) if m.body is not None else None
                        if rc is not None and self._fits(rc, hints):
                            return rc.fqcn
        return None

    def _constructed(self, node, ctx) -> Optional[JClass]:
        for x in walk(node):
            if x.type == "object_creation_expression":
                rc = self.ix.resolve(text(x.child_by_field_name("type")), ctx)
                if rc is not None:
                    return rc
            elif x.type == "method_reference" and text(x).endswith("::new"):
                parts = [c for c in x.named_children]
                rc = self.ix.resolve(text(parts[0]), ctx) if parts else None
                if rc is not None:
                    return rc
        return None

    def _fits(self, cls: JClass, hints) -> bool:
        if not hints:
            return True
        names = [cls.simple] + [a.rsplit(".", 1)[-1] for a in self.ix.ancestors(cls)]
        return any(h in nm for nm in names for h in hints)
