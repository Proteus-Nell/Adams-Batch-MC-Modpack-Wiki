# `config/tensura/area_magicule_config.toml`

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Configs](index.md)</small>

## Top level

| Option | Default | Range | Description |
|---|---|---|---|
| `baseMagicule` | 500 |  | Base magicule value for a chunk. |
| `maximumMagicule` | 1,000,000 |  | The maximum amount of magicule value a chunk can get. |
| `baseMagiculeRegeneration` | 10 |  | Base magicule regeneration per second for a chunk. |
| `modifierUpdateInterval` | 200 |  | How often maxMagiculeModifier are updated in ticks. |
| `magiculeSeed` | "UUID.randomUUID().getLeastSignificantBits()" |  | Seed for magicule generation", "Changing this will change the magicule values for all chunks. |
| `magicEngineReduction` | 1,000 |  | The amount that a magic engine will reduce from surrounding chunks (replace the blocks to apply the new value). |
| `magicEngineRange` | 16 |  | The radius in block that a magic engine will affect on entities (replace the blocks to apply the new value). |
| `labyrinthMagicEngineReduction` | 10,000 |  | The amount that a labyrinth magic engine will reduce from surrounding chunks (replace the blocks to apply the new value). |
| `labyrinthMagicEngineRange` | 32 |  | The radius in block that a labyrinth magic engine will affect on entities (replace the blocks to apply the new value). |
| `minimalMagiculeSpawn` | 10 |  | The minimal amount of Magicule in a chunk to allow mob spawn. |
