"""Access to the assets/ and data/ trees of the extracted mod jars."""
from __future__ import annotations

import json
import os
import re
from typing import Iterable, Optional

FORMAT_CODE = re.compile(r"§[0-9a-fk-orA-FK-OR#xu]")
HEX_CODE = re.compile(r"§x(§[0-9a-fA-F]){6}")


def clean(s):
    """Strip Minecraft formatting codes and tidy whitespace."""
    if not isinstance(s, str):
        return s
    s = HEX_CODE.sub("", s)
    s = FORMAT_CODE.sub("", s)
    s = s.replace("§", "")
    return s.strip()


def load_json(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    for enc in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            return json.loads(raw.decode(enc))
        except Exception:
            continue
    # tolerate trailing commas / comments occasionally found in mod data
    txt = raw.decode("utf-8", "replace")
    txt = re.sub(r"//[^\n]*", "", txt)
    txt = re.sub(r",\s*([}\]])", r"\1", txt)
    return json.loads(txt)


class Resources:
    """All extracted jars, keyed by jar key (the extracted folder name)."""

    def __init__(self, extracted_root: str, jar_keys: Iterable[str]):
        self.root = extracted_root
        self.keys = list(jar_keys)
        self.lang: dict = {}
        self.lang_owner: dict = {}
        for k in self.keys:
            for ns, path in self._lang_files(k):
                try:
                    d = load_json(path)
                except Exception:
                    continue
                for kk, v in d.items():
                    if kk not in self.lang:
                        self.lang[kk] = v
                        self.lang_owner[kk] = k
        self._tags: Optional[dict] = None

    def jar_dir(self, key):
        return os.path.join(self.root, key)

    def _lang_files(self, key):
        base = os.path.join(self.root, key, "assets")
        if not os.path.isdir(base):
            return
        for ns in sorted(os.listdir(base)):
            p = os.path.join(base, ns, "lang", "en_us.json")
            if os.path.isfile(p):
                yield ns, p

    def tr(self, key, default=None):
        v = self.lang.get(key)
        return clean(v) if v is not None else default

    def has(self, key):
        return key in self.lang

    # --------------------------------------------------------------- data
    def data_files(self, key, sub: str) -> Iterable:
        """Yield (namespace, id_path, json_path) for data/<ns>/<sub>/**/*.json in one jar."""
        base = os.path.join(self.root, key, "data")
        if not os.path.isdir(base):
            return
        for ns in sorted(os.listdir(base)):
            d = os.path.join(base, ns, sub)
            if not os.path.isdir(d):
                continue
            for dp, _dirs, files in os.walk(d):
                for fn in sorted(files):
                    if not fn.endswith(".json"):
                        continue
                    full = os.path.join(dp, fn)
                    rel = os.path.relpath(full, d).replace("\\", "/")[:-5]
                    yield ns, rel, full

    def all_data_files(self, sub: str):
        for k in self.keys:
            for ns, rel, full in self.data_files(k, sub):
                yield k, ns, rel, full

    def tags(self) -> dict:
        """registry -> tag id -> set(values) merged across every jar."""
        if self._tags is not None:
            return self._tags
        tags: dict = {}
        for k in self.keys:
            base = os.path.join(self.root, k, "data")
            if not os.path.isdir(base):
                continue
            for ns in os.listdir(base):
                tdir = os.path.join(base, ns, "tags")
                if not os.path.isdir(tdir):
                    continue
                for dp, _d, files in os.walk(tdir):
                    for fn in files:
                        if not fn.endswith(".json"):
                            continue
                        full = os.path.join(dp, fn)
                        rel = os.path.relpath(full, tdir).replace("\\", "/")[:-5]
                        if "/" not in rel:
                            continue
                        registry, name = rel.split("/", 1)
                        if registry == "worldgen" and "/" in name:
                            sub, name = name.split("/", 1)
                            registry = "worldgen/" + sub
                        # 1.21 uses singular folder names; older mods use plural
                        registry = {"items": "item", "blocks": "block", "entity_types": "entity_type",
                                    "fluids": "fluid", "mob_effects": "mob_effect"}.get(registry, registry)
                        try:
                            d = load_json(full)
                        except Exception:
                            continue
                        vals = []
                        for v in d.get("values", []):
                            if isinstance(v, dict):
                                v = v.get("id")
                            if isinstance(v, str):
                                vals.append(v)
                        tid = "%s:%s" % (ns, name)
                        bucket = tags.setdefault(registry, {}).setdefault(tid, set())
                        if d.get("replace"):
                            bucket.clear()
                        bucket.update(vals)
        self._tags = tags
        return tags

    def tag_members(self, registry: str, tag: str, depth=0) -> set:
        """Resolve a tag (with or without '#') into concrete ids."""
        tag = tag.lstrip("#")
        vals = self.tags().get(registry, {}).get(tag, set())
        out = set()
        for v in vals:
            if v.startswith("#"):
                if depth < 8:
                    out |= self.tag_members(registry, v, depth + 1)
            else:
                out.add(v)
        return out

    def tags_of(self, registry: str, ident: str) -> list:
        out = []
        for tid, vals in self.tags().get(registry, {}).items():
            if ident in vals:
                out.append(tid)
        return sorted(out)

    # ------------------------------------------------------------- assets
    def asset_path(self, rl: str, prefer: Optional[str] = None) -> Optional[str]:
        """Locate 'ns:path' inside assets/ of any jar (prefer the given jar)."""
        if ":" in rl:
            ns, p = rl.split(":", 1)
        else:
            ns, p = "minecraft", rl
        keys = ([prefer] if prefer else []) + [k for k in self.keys if k != prefer]
        for k in keys:
            f = os.path.join(self.root, k, "assets", ns, p)
            if os.path.isfile(f):
                return f
        return None

    def asset_json(self, rl: str):
        p = self.asset_path(rl)
        if p is None:
            return None
        try:
            return load_json(p)
        except Exception:
            return None
