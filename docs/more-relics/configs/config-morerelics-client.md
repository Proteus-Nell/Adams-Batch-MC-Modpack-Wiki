# `config/morerelics-client.toml`

<small>[More Relics](../index.md) &rsaquo; [Configs](index.md)</small>

## `[General]`

IMPORTANT, This is not where you change relic stats.  
To do that you need to enable enabledExtendedConfigs in relic.yaml and it will auto generate relic config files in config/morerelics/relics upon running the game once. You can change the values from there.  
Although I DO NOT RECOMMEND doing that because it is a very buggy system. If you enable it, when I update the mod it will still try to fetch values from those files.  
This means when I change stat values those won't affect your game and if I change/add an ability to a relic it will crash with "data is null".  
To fix this you would need to delete the updated relics config file in config/morerelics/relics so it can regenerate correctly on your next launch.

| Option | Default | Range | Description |
|---|---|---|---|
| `blockWearingCopies` | `List::of` |  | The relics included here cannot have multiple copies worn.<br>Some relics (e.g. Made in Heaven, Gravitum Gloves) are hardcoded to be that way due to interactions, bugs and cannot be changed.<br>This config only works with More Relics relics.<br>Format Example:["morerelics:guts_orb","morerelics:mass_gauntlet"] |
| `specialEffectIcons` | true |  | Renders some special effects from relics as icons above the food bar. This does not include SwiftEdge and RunicPlate icons. |

## `[VertebraX]`

| Option | Default | Range | Description |
|---|---|---|---|
| `excludedEffects` | "minecraft:levitation" |  | List of effects which can't be filtered/reduced by vertebrax. |
| `oppositeEffectMappings` | "minecraft:weakness\|minecraft:strength", "minecraft:slowness\|minecraft:speed", "minecraft:unluck\|minecraft:luck", "minecraft:blindness\|minecraft:night_vision", "minecraft:mining_fatigue\|minecraft:haste", "morerelics:vulnerability\|minecraft:resistance" |  | Pairs of effects which will grant the opposite version upon filtration.<br>Format: 'modid:original_effect\|modid:opposite_effect' Example: minecraft:weakness\|minecraft:strength<br>You can include modded effects here but first effect should be harmful and second effect should be beneficial or it won't work. |

## `[Mass Gauntlet]`

| Option | Default | Range | Description |
|---|---|---|---|
| `massGauntletCooldown` | 0.2 | 0 to no limit | Cooldown of mass gauntlets damage boost. Seconds. |
| `massGauntletDamageCap` | no limit | 0 to no limit | Maximum damage mass gauntlet can deal. |
| `massGauntletOnlyMelee` | false |  | Makes it so only default attacks will be boosted by mass gauntlet. |

## `[Moodworm]`

| Option | Default | Range | Description |
|---|---|---|---|
| `moodwormMoodChangeDuration` | 600 | 0 to no limit | Cooldown of Moodworm mood changes. Seconds. |
| `moodwormIcon` | true |  | Renders a little icon to show ability status above the food bar when enabled. |

## `[Bionic Eye]`

| Option | Default | Range | Description |
|---|---|---|---|
| `bionicVulLevel` | 0 | 0 to no limit | Level of applied Vulnerability by bionic eye. 0 means the first level. |
| `bionicIncreasedVulLevel` | 1 | 0 to no limit | Level of applied Vulnerability by bionic eye under cyberpsychosis. 0 means the first level. |

## `[Eject Button]`

| Option | Default | Range | Description |
|---|---|---|---|
| `ejectButtonHealthPerch` | 20 | 0 to 100 | Percentage of health under which eject button will activate. |

## `[Weaver's Spool]`

| Option | Default | Range | Description |
|---|---|---|---|
| `silkBarCorner` | "BOTTOM_RIGHT" | one of: TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT | The corner which the silk bar is rendered at. |

## `[Cyberpsychosis]`

| Option | Default | Range | Description |
|---|---|---|---|
| `cyberpsychosisDisguiseEffect` | true |  | Disguises some passive and neutral mobs as hostile entities while the Cyberpsychosis effect is active. |

## `[Wonder of U]`

| Option | Default | Range | Description |
|---|---|---|---|
| `nullificationVisualEffect` | true |  | The black and white + outline effect of nullification. |

## `[Swiftedge]`

| Option | Default | Range | Description |
|---|---|---|---|
| `swiftedgeStackIcons` | true |  | Renders sword icons above the food bar to show current stacks. |

## `[Runic Plate]`

| Option | Default | Range | Description |
|---|---|---|---|
| `runicPlateStackIcons` | true |  | Renders shield icons above the food bar to show current stacks. |

## `[Guts Orb]`

| Option | Default | Range | Description |
|---|---|---|---|
| `gutsOrbIcon` | true |  | Renders a little icon to show ability status above the food bar when enabled. |

## `[Opal Necklace]`

| Option | Default | Range | Description |
|---|---|---|---|
| `opalNecklaceIcon` | true |  | Renders a little icon to show ability status above the food bar when enabled. |

## `[Made in Heaven]`

| Option | Default | Range | Description |
|---|---|---|---|
| `heavenIcon` | true |  | Renders a little icon to show ability status above the food bar when enabled. |
