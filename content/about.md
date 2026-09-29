# About this wiki

This wiki is generated from the mod jars in the pack, so it can be rebuilt whenever mods update.

## How it's made

1. `tools/wikigen/extract.py` unzips each mod jar, decompiles it with [Vineflower](https://github.com/Vineflower/vineflower) and reads the language files, data packs (recipes, loot tables, tags, worldgen, advancements), textures and code (skill and race classes, config definitions, commands).
2. The results are saved as JSON in `data/`.
3. `tools/wikigen/render.py` turns that JSON (plus the hand-written guides in `content/`) into the Markdown pages in `docs/`.
4. GitHub Actions builds the website with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and publishes the same pages to the repository's Wiki tab.

## Updating after a mod update

```bash
pip install -r requirements.txt -r tools/requirements-extract.txt   # extraction also needs Java 21
python -m tools.wikigen.extract --mods /path/to/instance/mods --work .work --data data --icons docs/assets/icons
python -m tools.wikigen.render --data data --docs docs --content content --pack pack
mkdocs serve
```

The extract step only needs to run when mods change. Editing the guides in `content/` only needs the render step, and GitHub Actions runs that automatically on every push.

## Adding the pack's config values

Copy the instance's `config/` folder (and `defaultconfigs/` if the pack uses it) into `pack/`, then run the render step again. Every value that differs from a mod's default shows up as a **Pack note** on the matching page, in the config tables and on the [Pack notes](pack-notes.md) page.

## Accuracy

Values are the mods' defaults unless a pack note says otherwise. Some numbers depend on things that only exist while playing (your EP, mastery, or the target), so those are shown as formulas such as `max MP × 0.05`. Mods keep all rights to their names, text and textures; they are shown here to document the pack.
