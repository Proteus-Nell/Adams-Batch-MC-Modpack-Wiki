# `config/tensura/race/race_config.toml`

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Configs](index.md)</small>

## Top level

| Option | Default | Range | Description |
|---|---|---|---|
| `massNamingRaid` | 25 |  | The number of raids needed for Mass Naming. |
| `massNamingHuman` | 1,000 |  | The number of human kills needed for Mass Naming. |
| `majinPercentage` | 1 |  | The percentage to become Majin when dying of Magicule Poison. |
| `epToSoulRate` | 50 |  | The percentage of fallen targets' EP getting added into the attacker's soul points. |
| `limitedSpiritualAura` | 40,000 |  | The max aura that a spiritual-originated being gets limited at when moving to a physical world. |
| `limitedSpiritualMagicule` | 100,000 |  | The max magicule that a spiritual-originated being gets limited at when moving to a physical world. |

## `[Spirit]`

| Option | Default | Range | Description |
|---|---|---|---|
| `prayingTime` | 200 |  | The number of ticks that players need to pray for spirits. |
| `prayingCooldown` | 1,200 |  | The number of seconds of cooldown between each time of Spirit Praying. |
| `blessedPercentage` | 5 |  | The percentage to be blessed on reincarnation by 6 Greater Spirits when praying. |
| `lesserSpiritPercentage` | 40 |  | The percentage to get a Lesser Spirit when praying in the labyrinth. |
| `mediumSpiritPercentage` | 30 |  | The percentage to get a Medium Spirit when praying in the labyrinth. |
| `greaterSpiritPercentage` | 20 |  | The percentage to get a Greater Spirit when praying in the labyrinth. |
| `lordSpiritPercentage` | 1 |  | The percentage to get a Spirit Lord when praying in the labyrinth. |
| `mediumSpiritTamePercentage` | 15 |  | The percentage to get a Medium Spirit contract when taming a Medium Spirit in the wild. |
| `greaterSpiritTamePercentage` | 5 |  | The percentage to get a Greater Spirit contract when taming a Greater Spirit in the wild. |

## `[Hero]`

| Option | Default | Range | Description |
|---|---|---|---|
| `heroSpiritLevel` | 3 |  | The level of each Spirit needed to be counted for Hero Egg. |
| `heroSpiritNumber` | 1 |  | The number of Hero Spirits needed to be a Hero Egg (Darkness &amp; Light). |
| `heroCommonSpiritNumber` | 5 |  | The number of Non-Hero Spirits needed to be a Hero Egg. |
| `bossHPMultiplier` | 0.25 |  | The max HP multiplier that a boss needs to have below for the Hero Egg to hatch. |
| `epMultiplierHero` | 3 |  | The multiplier in EP that the entity gets when awakening as a true hero. |

## `[DemonLord]`

| Option | Default | Range | Description |
|---|---|---|---|
| `harvestFestivalTick` | 3,600 |  | The duration in tick of the Harvest Festival. |
| `epMultiplierDemonLord` | 3 |  | The multiplier in EP that the entity gets when awakening as a true demon lord. |
| `harvestFestivalRange` | 30 |  | The range in block of harvest festival boost on subordinates when their owner awakens as a true demon lord. |
