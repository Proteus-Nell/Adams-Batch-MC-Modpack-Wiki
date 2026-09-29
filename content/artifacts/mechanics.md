# Mechanics

> [!NOTE]
> **Pack note:** this pack includes **RAR-Compat**, so every artifact is also a **relic** that levels up and unlocks abilities. See the *In this pack* section on each artifact's page and the [Relics guide](@/relics/mechanics/index.md) for how levelling works.

## Finding artifacts

- **Chests:** artifacts appear in dungeon and structure chests. The `artifactRarity` config (**{{cfg:config/artifacts/general.toml|artifactRarity}}**) scales how common they are (higher is rarer).
- **Campsites:** small underground camps between Y **{{cfg:config/artifacts/general.toml|campsite.minY}}** and **{{cfg:config/artifacts/general.toml|campsite.maxY}}**. A campsite has a **{{cfg:config/artifacts/general.toml|campsite.mimicChance}}** chance to hold a **Mimic** instead of a chest.
- **Mimics:** chest-shaped mobs that drop artifacts. See [Mobs](@/artifacts/mobs/index.md).
- **Mobs:** skeletons, zombies and piglins have a **{{cfg:config/artifacts/general.toml|entityEquipmentChance}}** chance to spawn wearing an artifact.
- **Archaeology:** suspicious sand and gravel have a **{{cfg:config/artifacts/general.toml|archaeologyChance}}** chance to contain one.

## Wearing artifacts

Artifacts go into Curios slots (head, necklace, belt, hands, feet and so on). Every artifact's page lists its slot and its config values from [`items.toml`](@/artifacts/configs/config-artifacts-items.md).
