"""Convert docs/ into a flat GitHub Wiki (the repository's Wiki tab).

    python -m tools.wikigen.wiki_sync --docs docs --out wiki-out --site-url https://...

GitHub wikis are flat: every page needs a unique file name and links point at
page names, not paths. This script:

* gives each page a readable, unique name (entry pages get the mod name in
  brackets, e.g. "Great-Sage-(Tensura-Reincarnated)"),
* rewrites every Markdown link and image to the new names,
* copies docs/assets/ so icons keep working,
* turns MkDocs-only syntax (GitHub callouts inside the site, @/ links) into
  plain GitHub Markdown,
* writes _Sidebar.md and _Footer.md.
"""
from __future__ import annotations

import argparse
import html
import os
import posixpath
import re
import shutil

from .mods import MODS, GROUPS

LINK = re.compile(r"(!?)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]+)(\s+\"[^\"]*\")?\)")


def title_of(md: str, fallback: str) -> str:
    for line in md.splitlines():
        if line.startswith("# "):
            t = line[2:].strip().strip("`")
            return html.unescape(re.sub(r"\\(.)", r"\1", t))
    return fallback


def safe(name: str) -> str:
    name = name.replace("&", "and").replace("+", " Plus").replace("/", " ").replace(":", " ")
    name = re.sub(r"[^A-Za-z0-9 ()._'-]", "", name)
    name = re.sub(r"\s+", "-", name.strip())
    return name.strip("-") or "Page"


class WikiBuilder:
    def __init__(self, docs: str, out: str, site_url: str):
        self.docs = docs
        self.out = out
        self.site_url = site_url.rstrip("/")
        self.mod_names = {m["slug"]: m["name"] for m in MODS}
        self.pages = {}   # docs path -> wiki name
        self.used = {}

    def collect(self):
        paths = []
        for dp, _d, files in os.walk(self.docs):
            for fn in files:
                if fn.endswith(".md"):
                    full = os.path.join(dp, fn)
                    paths.append(os.path.relpath(full, self.docs).replace(os.sep, "/"))
        # stable order: shallow pages first so they win the plain names
        paths.sort(key=lambda p: (p.count("/"), p))
        for p in paths:
            with open(os.path.join(self.docs, p), encoding="utf-8") as fh:
                md = fh.read()
            self.pages[p] = self.name_for(p, md)

    def name_for(self, p, md):
        parts = p[:-3].split("/")
        if p == "index.md":
            return self._unique("Home")
        title = title_of(md, parts[-1])
        mod = self.mod_names.get(parts[0])
        if mod is None:
            return self._unique(safe(title))
        if len(parts) == 2 and parts[1] == "index":
            return self._unique(safe(mod))
        if parts[-1] == "index":
            # category or group index
            return self._unique(safe("%s %s" % (mod, title)))
        if parts[1] == "configs":
            return self._unique(safe("%s config %s" % (mod, title.split("/")[-1].replace(".toml", ""))))
        base = safe("%s (%s)" % (title, mod))
        if base in self.used:
            base = safe("%s (%s %s)" % (title, mod, parts[1].rstrip("s")))
        return self._unique(base)

    def _unique(self, name):
        n = name
        i = 2
        while n.lower() in self.used:
            n = "%s-%d" % (name, i)
            i += 1
        self.used[n.lower()] = True
        self.used[n] = True
        return n

    # --------------------------------------------------------- convert
    def convert(self, p, md):
        base = posixpath.dirname(p)

        def fix(m):
            bang, text, target, title = m.group(1), m.group(2), m.group(3), m.group(4) or ""
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                return m.group(0)
            path, _, anchor = target.partition("#")
            resolved = posixpath.normpath(posixpath.join(base, path)) if path else p
            if bang:
                if resolved.startswith("assets/"):
                    return "%s[%s](%s%s)" % (bang, text, resolved, title)
                return m.group(0)
            if resolved.endswith("/"):
                resolved += "index.md"
            if not resolved.endswith(".md"):
                if resolved.startswith("assets/"):
                    return "[%s](%s%s)" % (text, resolved, title)
                return m.group(0)
            name = self.pages.get(resolved)
            if name is None:
                return text
            return "[%s](%s%s)" % (text, name, ("#" + anchor) if anchor else "")

        out = []
        in_fence = False
        for line in md.split("\n"):
            if line.startswith("```"):
                in_fence = not in_fence
                out.append(line)
                continue
            if in_fence:
                out.append(line)
                continue
            line = LINK.sub(fix, line)
            line = re.sub(r"^> \[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$", lambda mm: "> **%s**" % mm.group(1).title(), line)
            line = line.replace(" markdown>", ">").replace("<details markdown>", "<details>")
            out.append(line)
        text = "\n".join(out)
        site = self.site_page_url(p)
        if site:
            text = text.rstrip() + "\n\n---\n<sub>Also on the website: [%s](%s)</sub>\n" % (site, site)
        return text

    def site_page_url(self, p):
        if not self.site_url:
            return None
        if p == "index.md":
            return self.site_url + "/"
        if p.endswith("/index.md"):
            return "%s/%s/" % (self.site_url, p[: -len("/index.md")])
        return "%s/%s/" % (self.site_url, p[:-3])

    def sidebar(self):
        lines = ["**[Home](Home)** &middot; [Pack notes](%s) &middot; [About](%s)" % (self.pages.get("pack-notes.md", "Home"), self.pages.get("about.md", "Home")), ""]
        for group in GROUPS:
            lines.append("**%s**" % group)
            lines.append("")
            for m in MODS:
                if m["group"] != group:
                    continue
                idx = "%s/index.md" % m["slug"]
                if idx not in self.pages:
                    continue
                cats = []
                for cat in ("abilities", "races", "items", "blocks", "mobs", "effects", "enchantments", "biomes", "dimensions",
                            "structures", "gateways", "perks", "advancements", "mechanics", "commands", "configs"):
                    cp = "%s/%s/index.md" % (m["slug"], cat)
                    if cp in self.pages:
                        cats.append("[%s](%s)" % (cat.title(), self.pages[cp]))
                lines.append("- [%s](%s)" % (m["name"], self.pages[idx]))
                if cats:
                    lines.append("  <br><sub>%s</sub>" % " &middot; ".join(cats))
            lines.append("")
        return "\n".join(lines)

    def run(self):
        if os.path.isdir(self.out):
            shutil.rmtree(self.out)
        os.makedirs(self.out)
        self.collect()
        for p, name in self.pages.items():
            with open(os.path.join(self.docs, p), encoding="utf-8") as fh:
                md = fh.read()
            with open(os.path.join(self.out, name + ".md"), "w", encoding="utf-8") as fh:
                fh.write(self.convert(p, md))
        src_assets = os.path.join(self.docs, "assets")
        if os.path.isdir(src_assets):
            shutil.copytree(src_assets, os.path.join(self.out, "assets"), ignore=shutil.ignore_patterns("*.css", "*.js"))
        with open(os.path.join(self.out, "_Sidebar.md"), "w", encoding="utf-8") as fh:
            fh.write(self.sidebar())
        with open(os.path.join(self.out, "_Footer.md"), "w", encoding="utf-8") as fh:
            foot = "Generated from the pack's mod files by `tools/wikigen`. Edit `content/` or the generator in the main repository, not these pages."
            if self.site_url:
                foot += " Browse the searchable website at %s." % self.site_url
            fh.write(foot + "\n")
        print("wrote %d wiki pages to %s" % (len(self.pages), self.out))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--out", default="wiki-out")
    ap.add_argument("--site-url", default="")
    a = ap.parse_args(argv)
    WikiBuilder(a.docs, a.out, a.site_url).run()


if __name__ == "__main__":
    main()
