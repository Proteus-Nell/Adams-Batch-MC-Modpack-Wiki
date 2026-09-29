# Earth Storm

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Earth Storm](../../../assets/icons/tensura/skill/earth_storm.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:earth_storm` |
| **Element** | Earth |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Hold |

</div>

> Summons a viscous sandstorm and falling rocks around you.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5,000 |  |

## How it works

- Charged or channelled by holding the skill key

## Obtaining

- Innate to mobs: [Gazel Dwargo](../../mobs/gazel-dwargo.md)
- Removed and re-rolled when you change race

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `EarthStorm.castTime` | 120 | Cast time in tick. |
| `EarthStorm.castTimeMastered` | 120 | Cast time in tick when mastered. |
| `EarthStorm.magiculeCost` | 5,000 | Magicule Cost to cast. |
| `EarthStorm.radius` | 5 | The radius in block of the magic. |
| `EarthStorm.stormDamage` | 20 | The damage of the magic. |
| `EarthStorm.levitationChance` | 0.3 | The chance for targets to be affected by Levitation. |
| `EarthStorm.levitationLevel` | 1 | The level of the Levitation effect. |
| `EarthStorm.levitationDuration` | 40 | The duration in tick of the Levitation effect. |
| `EarthStorm.stormDuration` | 300 | The max duration in tick that the magic can be used. |
| `EarthStorm.stormDurationMastered` | 600 | The max duration in tick that the magic can be used with mastery. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryMedium` | 500 | The max amount of mastery point for Medium Spiritual Magic. |
| `SpiritualMagic.masteryGreater` | 1,000 | The max amount of mastery point for Greater Spiritual Magic. |
| `SpiritualMagic.masteryLord` | 10,000 | The max amount of mastery point for Lord Spiritual Magic. |

## Tags

`tensura:skills/reset_with_race`, `tensura:skills/spiritual_magic`
