# `config/tensura/block_config.toml`

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Configs](index.md)</small>

## Top level

| Option | Default | Range | Description |
|---|---|---|---|
| `specialBiomeFireSpread` | false |  | Enable/Disable fire spread inside Biomes with disabled fire tag (Ancient Forest, Miasmic Plains by default). |

## `[Baffledil]`

| Option | Default | Range | Description |
|---|---|---|---|
| `hypnosisRadius` | 8 |  | The radius in block around the Baffledil flower that players get Hypnosis effect. |
| `hypnosisDuration` | 160 |  | The duration in tick of Hypnosis effect applied by the flower. |
| `hypnosisLevel` | 1 |  | The level of Hypnosis effect applied by the flower. |

## `[CharybdisCore]`

| Option | Default | Range | Description |
|---|---|---|---|
| `charybdisCoreActiveEP` | 100,000 |  | The amount of EP needed for Inactive Charybdis Core to turn Active. |
| `charybdisCoreSkills` | "tensura:gravity_manipulation", "tensura:magic_jamming" |  | List of Skills that can be obtained from right-clicking Inert Charybdis Core. |
| `charybdisCoreFusingEP` | 200,000 |  | The amount of EP that can be obtained from fusing with Inert Charybdis Core using Degenerate and similar abilities. |
| `charybdisCoreFusingSkills` | "tensura:gravity_manipulation", "tensura:magic_jamming", "tensura:magic_sense", "tensura:ultraspeed_regeneration" |  | List of Skills that can be obtained from fusing with Inert Charybdis Core using Degenerate and similar abilities. |
| `charybdisCoreFusingSkillsActive` | "tensura:gravity_manipulation", "tensura:magic_sense" |  | List of Skills that can be obtained from fusing with Active Charybdis Core using Degenerate and similar abilities. |
| `charybdisCoreFusingSkillsInactive` | "tensura:gravity_manipulation" |  | List of Skills that can be obtained from fusing with Inactive Charybdis Core using Degenerate and similar abilities. |

## `[Kiln]`

| Option | Default | Range | Description |
|---|---|---|---|
| `moltenDefault` | 144 |  | The max molten amount of a Default Kiln. |
| `moltenMithril` | 288 |  | The max molten amount of a Mithril Kiln. |
| `moltenOrichalcum` | 576 |  | The max molten amount of a Orichalcum Kiln. |
| `fireCoreCost` | 100 |  | The amount of durability to take from a Fire Elemental Core to charge a kiln each time. |
| `chargeDuration` | 2,400 |  | The charged duration in tick that a kiln gets each time its used with a Fire Elemental Core. |
