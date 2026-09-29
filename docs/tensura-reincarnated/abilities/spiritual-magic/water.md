# Water

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Water](../../../assets/icons/tensura/skill/water.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:water` |
| **Element** | Water |
| **Modes** | 4 |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Hold |

</div>

> Call forth or manipulate small amounts of water.

## Modes

| # | Mode |
|---|---|
| 1 | 10x10 Water |
| 2 | 1x1 Water |
| 3 | 3x3 Water |
| 4 | 5x5 Water |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Removed and re-rolled when you change race
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill registry IDs automatically granted with Albis Vina.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `Water.castTime` | 20 | Cast time in tick. |
| `Water.castTimeMastered` | 1 | Cast time in tick when mastered. |
| `Water.magiculeCost` | 50 | Magicule Cost to cast. |
| `Water.range` | 4 | The range in block of the magic. |

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
