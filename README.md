# Adam's Batch Modpack Wiki

A wiki for the **Adam's Batch** modpack (Minecraft 1.21.1, NeoForge), generated straight from the pack's mod files.

- **Website:** https://proteus-nell.github.io/Adams-Batch-MC-Modpack-Wiki/ (searchable, light/dark mode)
- **Wiki tab:** https://github.com/Proteus-Nell/Adams-Batch-MC-Modpack-Wiki/wiki (the same pages)
- **In the repo:** browse [`docs/`](docs/index.md)

## What's documented

| Mod | Version | Pages |
|---|---|---|
| Tensura: Reincarnated | 2.0.1.3 | abilities, races, items, blocks, mobs, effects, enchantments, biomes, dimensions, structures, advancements, mechanics, commands, configs |
| TR: Nightmares | 1.0.5.0 | abilities, races, items, blocks, mobs, effects, enchantments, dimensions, mechanics, commands, configs |
| Elite Tensura | 1.0.2.2 | abilities, races, items, blocks, mobs, effects, enchantments, biomes, dimensions, Codex guide book, configs |
| TensuraMoreSkills | 0.0.4.9.2 | abilities, races, items, blocks, mobs, effects, biomes, dimensions, structures, mechanics, commands, configs |
| Tensura: Mysticism | 2.2.1 | abilities, races, items, mobs, effects, biomes, dimensions, structures, mechanics, commands, configs |
| Ascension | 2.1.2 | abilities, races, items, blocks, effects, enchantments, dimensions, mechanics, commands, configs |
| Nightmare Utils | 0.1.2 | abilities, mechanics, commands |
| EnigmaticLegacy+ | 1.1.1 | items, blocks, mobs, effects, enchantments, advancements, guide book, commands, configs |
| Relics | 0.10.7.8 | relics with levelled abilities, effects, commands |
| More Relics | 1.7.7 | relics with levelled abilities, effects, configs |
| Artifacts | 13.2.5 | artifacts (with their RAR-Compat relic versions), configs |
| Gateways To Eternity | 5.1.0 | gateways with waves and rewards |
| Corail Tombstone | 9.5.6 | items, blocks, mobs, effects, enchantments, perks, advancements, mechanics, configs |

Each mod is split into the same kinds of sections the [Tensura: Reincarnated wiki](https://tensura.wiki.gg/) uses (Abilities, Races, Items, Blocks, Mobs, Biomes, Structures, Configs, Commands, Mechanics), and each section is split further into groups (Unique Skills, Extra Skills, Weapons, Armor, Head/Necklace/Feet slots, and so on).

## One-time setup on GitHub

1. **Website:** Settings → Pages → *Build and deployment* → Source: **GitHub Actions**. The `Build and deploy website` workflow publishes the site on every push to `main`.
2. **Wiki tab:** open the repository's **Wiki** tab and create any first page (GitHub only creates the wiki's git repository after that). After that, the `Sync the Wiki tab` workflow overwrites it with the generated pages on every push to `main`, or when you run it by hand from the Actions tab.

## How it works

```
mod jars ──extract──▶ data/*.json ──render──▶ docs/*.md ──mkdocs──▶ website
                       content/*.md ──┘            └──wiki_sync──▶ Wiki tab
```

- `tools/wikigen/extract.py` unzips each jar, decompiles it with Vineflower and reads language files, recipes, loot tables, tags, worldgen, advancements, textures, and the code for skills, races, configs, game rules and commands. The results go into `data/`.
- `tools/wikigen/render.py` builds every page in `docs/` from `data/` and the hand-written guides in `content/`. It also writes `mkdocs.yml` from `mkdocs.base.yml`.
- `tools/wikigen/wiki_sync.py` flattens `docs/` into GitHub Wiki pages.

### Updating after mods change

```bash
pip install -r requirements.txt -r tools/requirements-extract.txt   # extraction also needs Java 21
python -m tools.wikigen.extract --mods /path/to/instance/mods --work .work --data data --icons docs/assets/icons
python -m tools.wikigen.render --data data --docs docs --content content --pack pack
mkdocs serve   # preview at http://127.0.0.1:8000
```

The mod list lives in `tools/wikigen/mods.py`.

### Pack notes

Copy the instance's `config/` folder into `pack/config/` and re-render. Every value that differs from a mod default then shows up as a **Pack note** on the matching page, in the config tables, and on the Pack notes page.

### Editing

- Guides and the home, about and pack-notes pages: edit files in `content/`.
- Anything else: the pages are generated, so change the generator in `tools/wikigen/` (or the data) rather than editing `docs/` by hand.
