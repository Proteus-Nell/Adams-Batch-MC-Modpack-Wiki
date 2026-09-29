# `config/tensura/entity/entity_config.toml`

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Configs](index.md)</small>

## Top level

| Option | Default | Range | Description |
|---|---|---|---|
| `tamedWanderRadius` | 20 |  | The maximum radius that a tamed mobs can wander away from the position where it was set to wander. |
| `tamedSleepRadius` | 12 |  | The maximum radius that a tamed mobs can sleep away from the owner's position when set to follow. |
| `hostileHPMultiplier` | 0.9 |  | The multiplier of max HP that a hostile tensura mob needs to be below to start targeting passive animals. |
| `successKillHeal` | 1 |  | The amount of HP that an entity heal whenever it kills an enemy and gains EP. |
| `xpDropMultiplier` | 0.001 |  | Multiplier applied to the mob's EP to determine the amount of XP dropped on death. |

## `[Boss]`

| Option | Default | Range | Description |
|---|---|---|---|
| `bossAreaName` | false |  | Allow players to name entities in the Boss Area dimension. |
| `bossAreaMindControl` | false |  | Allow players to mind control entities in the Boss Area dimension. |
| `bossAreaPossess` | false |  | Allow players to possess entities in the Boss Area dimension. |
| `bossAreaSkillPlunder` | false |  | Allow players to copy/steal abilities in the Boss Area dimension. |
| `bossAreaSkillGrief` | false |  | Allow players to grief the environment using abilities in the Boss Area dimension. |

## `[Dwarf]`

| Option | Default | Range | Description |
|---|---|---|---|
| `armorerPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Armorer dwarves. |
| `butcherPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Butcher dwarves. |
| `battlewillTrainerPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Battlewill Trainer dwarves. |
| `cartographerPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Cartographer dwarves. |
| `alchemistPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Alchemist dwarves. |
| `farmerPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Farmer dwarves. |
| `fishermanPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Fisherman dwarves. |
| `fletcherPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Fletcher dwarves. |
| `leatherWorkerPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Leatherworker dwarves. |
| `librarianPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Librarian dwarves. |
| `lumberjackPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Lumberjack dwarves. |
| `magicTrainerPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Magic Trainer dwarves. |
| `masonPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Mason dwarves. |
| `merchantPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Merchant dwarves. |
| `minerPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Miner dwarves. |
| `shepherdPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Shepherd dwarves. |
| `toolSmithPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Toolsmith dwarves. |
| `weaponSmithPriceMultiplier` | 1 |  | Dwarf's trade price multiplier to apply to most trades from Weaponsmith dwarves. |
| `scarChance` | 0.02 |  | The chance for the dwarf to spawn with a scarred eye. |
| `dwarfHairColors` | -7,558, -6,260,652, -1,326,982, -9,418,704, -12,966,368, -1,052,689 |  | Random colors for dwarves' hair. |
| `dwarfTopClothesColors` | -13,738,962, -10,867,110, -5,010,688, -14,540,254, -1, -9,560,289, -6,533,601, -11,184,811, -2,239,048, -7,640,241 |  | Random colors for dwarves' top clothes. |
| `dwarfBottomClothesColors` | -14,540,254, -11,184,811, -2,239,048, -11,850,209, -7,640,241 |  | Random colors for dwarves' bottom clothes. |
| `dwarfBootsColors` | -11,850,209, -15,066,598 |  | Random colors for dwarves' boots. |
| `dwarfNames` | "Ana", "Anrietta", "Colette", "Dord", "Dorf", "Dyna", "Fio", "Inga", "Garm", "Jaine", "Johann", "Kaidou", "Kaijin", "Kaine", "Marche", "Mite", "Myrd", "Tosca", "Uhura", "Vaughn" ... (59 total) |  | Random names for Dwarves. |

## `[Goblin]`

| Option | Default | Range | Description |
|---|---|---|---|
| `goblinHairColors` | -14,869,219, -11,849,440, -10,855,846, -12,961,222, -1, -4,741,456, -1,326,982 |  | Random colors for Goblins' hair. |
| `goblinHeadColors` | -1, -11,184,811, -2,239,048, -7,640,241, -11,850,209 |  | Random colors for Goblins' headband. |
| `goblinClothingColors` | -14,513,374, -14,540,254, -1, -11,184,811, -2,239,048, -7,640,241, -8,388,480, -7,650,029, -16,763,765 |  | Random colors for Goblins' top clothes. |
| `goblinBottomClothesColors` | -14,540,254, -11,184,811, -2,239,048, -11,850,209, -7,640,241 |  | Random colors for Goblins' bottom clothes. |

## `[Lizardman]`

| Option | Default | Range | Description |
|---|---|---|---|
| `lizardmanHairColors` | -8,760,265, -3,893,419, -11,062,239, -14,477,549, -2,565,928, -14,472,113, -13,164,473 |  | Random colors for Lizardmen's hair. |
| `lizardmanTopClothesColors` | -14,540,254, -1, -11,184,811, -2,239,048, -7,640,241 |  | Random colors for Lizardmen's top clothes. |
| `lizardmanBottomClothesColors` | -14,540,254, -11,184,811, -2,239,048, -11,850,209, -7,640,241 |  | Random colors for Lizardmen's bottom clothes. |
| `lizardmanMiscClothesColors` | -14,540,254, -11,184,811, -11,850,209, -7,640,241 |  | Random colors for Lizardmen's cape/helmet/hood. |

## `[Orc]`

| Option | Default | Range | Description |
|---|---|---|---|
| `orcTopClothesColors` | -14,540,254, -1, -11,184,811, -2,239,048, -7,640,241 |  | Random colors for Orcs' top clothes. |
| `orcBottomClothesColors` | -14,540,254, -11,184,811, -2,239,048, -11,850,209, -7,640,241 |  | Random colors for Orcs' bottom clothes. |
| `orcLeatherColors` | -14,540,254, -11,184,811, -11,850,209, -7,640,241 |  | Random colors for Orcs' boots/capes/belts. |

## `[MobSpecific]`

| Option | Default | Range | Description |
|---|---|---|---|
| `charybdisSize` | 1 |  | The normal size multiplier for Charybdis. |
| `elementalCoreCost` | 1,000 |  | The amount of EP that an empty elemental core will take from the spirit when used. |
| `otherworlderSkillDrop` | 0 |  | The chance in percentage for otherworlders to drop their Unique skills to the attacker - Range 0 -&gt; 100. |
