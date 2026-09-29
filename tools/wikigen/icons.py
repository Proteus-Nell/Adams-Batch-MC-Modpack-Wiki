"""Render item, block, skill and effect icons from the mods' textures."""
from __future__ import annotations

import os
from typing import Optional

from PIL import Image

from .resources import Resources, load_json

CUBE_PARENTS = ("block/cube", "block/cube_all", "block/cube_column", "block/cube_bottom_top",
                "block/orientable", "block/cube_column_horizontal", "block/leaves", "block/cube_top",
                "block/orientable_with_bottom", "block/cube_mirrored_all", "block/cube_directional")


class IconRenderer:
    def __init__(self, res: Resources, out_dir: str, url_prefix: str):
        self.res = res
        self.out = out_dir
        self.url = url_prefix.rstrip("/")
        self.cache: dict = {}

    # ----------------------------------------------------------- textures
    def _texture(self, rl: str) -> Optional[Image.Image]:
        if rl is None:
            return None
        if rl.startswith("#"):
            return None
        if ":" not in rl:
            rl = "minecraft:" + rl
        ns, p = rl.split(":", 1)
        if not p.endswith(".png"):
            p = "textures/%s.png" % p
        path = self.res.asset_path("%s:%s" % (ns, p))
        if path is None:
            return None
        try:
            img = Image.open(path).convert("RGBA")
        except Exception:
            return None
        w, h = img.size
        if h > w and h % w == 0:  # animated strip: first frame
            img = img.crop((0, 0, w, w))
        return img

    def _model(self, rl: str, depth=0) -> dict:
        """Load a model and merge its parents' textures; returns {textures, parents}."""
        if ":" not in rl:
            rl = "minecraft:" + rl
        ns, p = rl.split(":", 1)
        data = self.res.asset_json("%s:models/%s.json" % (ns, p)) or {}
        textures = {}
        parents = [p]
        parent = data.get("parent")
        if parent and depth < 10:
            pm = self._model(parent, depth + 1)
            textures.update(pm["textures"])
            parents += pm["parents"]
        textures.update(data.get("textures", {}) or {})
        # resolve #refs
        for _ in range(5):
            for k, v in list(textures.items()):
                if isinstance(v, str) and v.startswith("#") and v[1:] in textures:
                    textures[k] = textures[v[1:]]
        return {"textures": textures, "parents": parents, "elements": "elements" in data, "loader": data.get("loader")}

    # ------------------------------------------------------------- output
    def _save(self, img: Image.Image, rel: str, size: int = 32) -> str:
        path = os.path.join(self.out, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if img.size[0] < size:
            img = img.resize((size, size * img.size[1] // img.size[0]), Image.NEAREST)
        elif img.size[0] > 64:
            img = img.resize((64, 64 * img.size[1] // img.size[0]), Image.LANCZOS)
        img.save(path, optimize=True)
        return self.url + "/" + rel.replace(os.sep, "/")

    def item(self, ns: str, path: str) -> Optional[str]:
        key = ("item", ns, path)
        if key in self.cache:
            return self.cache[key]
        url = None
        m = self._model("%s:item/%s" % (ns, path))
        tex = m["textures"]
        img = None
        if any(pp.startswith("block/") or "/block/" in pp for pp in m["parents"][1:]) and "layer0" not in tex:
            img = self._block_image(m)
        if img is None:
            img = self._texture(tex.get("layer0"))
            l1 = self._texture(tex.get("layer1")) if tex.get("layer1") else None
            if img is not None and l1 is not None and l1.size == img.size:
                img = Image.alpha_composite(img, l1)
        if img is None:
            for k in ("particle", "all", "texture"):
                img = self._texture(tex.get(k))
                if img is not None:
                    break
        if img is None:
            img = self._texture("%s:item/%s" % (ns, path))
        if img is not None:
            url = self._save(img, os.path.join(ns, "item", path.replace("/", "_") + ".png"))
        self.cache[key] = url
        return url

    def block(self, ns: str, path: str) -> Optional[str]:
        key = ("block", ns, path)
        if key in self.cache:
            return self.cache[key]
        # the item model usually points at the right block model
        url = self.item(ns, path)
        if url is None:
            m = self._model("%s:block/%s" % (ns, path))
            img = self._block_image(m)
            if img is not None:
                url = self._save(img, os.path.join(ns, "block", path.replace("/", "_") + ".png"))
        self.cache[key] = url
        return url

    def _block_image(self, m) -> Optional[Image.Image]:
        tex = m["textures"]
        is_cube = any(any(pp.endswith(cp.split("/", 1)[1]) and pp.startswith("block/") for cp in CUBE_PARENTS) for pp in m["parents"][1:])
        if is_cube:
            top = self._texture(tex.get("top") or tex.get("end") or tex.get("up") or tex.get("all") or tex.get("side"))
            side = self._texture(tex.get("side") or tex.get("all") or tex.get("north") or tex.get("front"))
            front = self._texture(tex.get("front") or tex.get("side") or tex.get("all") or tex.get("south"))
            if top is not None and side is not None:
                return isometric(top, front or side, side)
        for k in ("cross", "plant", "texture", "particle", "all", "side", "layer0"):
            img = self._texture(tex.get(k))
            if img is not None:
                return img
        for v in tex.values():
            img = self._texture(v)
            if img is not None:
                return img
        return None

    def texture(self, rl: str, rel: str, size: int = 32) -> Optional[str]:
        key = ("tex", rl)
        if key in self.cache:
            return self.cache[key]
        img = self._texture(rl)
        url = self._save(img, rel, size) if img is not None else None
        self.cache[key] = url
        return url


def isometric(top: Image.Image, left: Image.Image, right: Image.Image, size: int = 64) -> Image.Image:
    """Tiny isometric cube renderer (top, left face, right face)."""
    n = 16
    top = top.resize((n, n), Image.NEAREST)
    left = left.resize((n, n), Image.NEAREST)
    right = right.resize((n, n), Image.NEAREST)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    px = out.load()
    s = size / 64.0
    cx = 32 * s
    tw = 28 * s  # half width of the diamond
    th = 14 * s
    fh = 32 * s  # face height

    def shade(c, f):
        return (int(c[0] * f), int(c[1] * f), int(c[2] * f), c[3])

    # draw per destination pixel by inverse mapping
    for y in range(size):
        for x in range(size):
            dx = x + 0.5 - cx
            dy = y + 0.5 - (4 * s)
            # top face: u along right-down, v along left-down
            u = (dx / tw + dy / th) / 2
            v = (dy / th - dx / tw) / 2
            if 0 <= u < 1 and 0 <= v < 1:
                c = top.getpixel((min(n - 1, int(u * n)), min(n - 1, int(v * n))))
                if c[3] > 0:
                    px[x, y] = c
                    continue
            # left face
            ly = y + 0.5 - (4 * s + th)
            if -tw <= dx < 0:
                fu = (dx + tw) / tw
                base = ly - fu * th
                fv = base / fh
                if 0 <= fv < 1:
                    c = left.getpixel((min(n - 1, int(fu * n)), min(n - 1, int(fv * n))))
                    if c[3] > 0:
                        px[x, y] = shade(c, 0.78)
                    continue
            if 0 <= dx < tw:
                fu = dx / tw
                base = ly - (1 - fu) * th
                fv = base / fh
                if 0 <= fv < 1:
                    c = right.getpixel((min(n - 1, int(fu * n)), min(n - 1, int(fv * n))))
                    if c[3] > 0:
                        px[x, y] = shade(c, 0.6)
    return out
