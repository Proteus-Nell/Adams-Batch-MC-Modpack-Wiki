# Water Cutter

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Water Cutter](../../../assets/icons/tensura/skill/water_cutter.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:water_cutter` |
| **Element** | Water |
| **Modes** | 1 |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Hold |

</div>

> Fires a concentrated blade to cut your enemies with the power of water.

## Modes

| # | Mode |
|---|---|
| 1 | Repeat |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Undine](../../mobs/undine.md)
- Removed and re-rolled when you change race
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill registry IDs automatically granted with Albis Vina.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `WaterCutter.castTime` | 30 | Cast time in tick. |
| `WaterCutter.castTimeMastered` | 10 | Cast time in tick when mastered. |
| `WaterCutter.magiculeCost` | 500 | Magicule Cost to cast. |
| `WaterCutter.damage` | 30 | The damage of the water cutter. |

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
