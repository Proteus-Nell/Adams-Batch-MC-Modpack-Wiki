# Space

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Space](../../../assets/icons/tensura/skill/space.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:space` |
| **Element** | Space |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Hold |

</div>

> Form invisible platforms to create footholds midair.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50 |  |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Removed and re-rolled when you change race

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `Space.castTime` | 20 | Cast time in tick. |
| `Space.castTimeMastered` | 1 | Cast time in tick when mastered. |
| `Space.magiculeCost` | 50 | Magicule Cost to cast. |
| `Space.range` | 4 | The range in block of the magic. |
| `Space.duration` | 1,200 | The duration in tick of the solid space block before removing itself. |

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
