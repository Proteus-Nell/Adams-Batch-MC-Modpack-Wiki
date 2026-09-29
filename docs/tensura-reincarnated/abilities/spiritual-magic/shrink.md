# Shrink

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Shrink](../../../assets/icons/tensura/skill/shrink.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:shrink` |
| **Element** | Space |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Toggle, Hold |

</div>

> Reduce your size to enhance your evasion but increase your vulnerability

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 300 |  |

## How it works

- Can be toggled on and off
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Obtaining

- Removed and re-rolled when you change race

## Related

- **Effects:** [Fragility](../../effects/fragility.md)
- **Referenced by:** [Size Condense](../../../tr-nightmares/abilities/intrinsic-skills/size-condense.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `Shrink.castTime` | 60 | Cast time in tick. |
| `Shrink.castTimeMastered` | 60 | Cast time in tick when mastered. |
| `Shrink.magiculeCost` | 300 | Magicule Cost to cast. |
| `Shrink.shrinkDuration` | 60 | The duration in second of the Shrink effect. |
| `Shrink.shrinkDurationMastered` | 120 | The duration in second of the Shrink effect when mastered. |
| `Shrink.shrinkSize` | 0.2 | The size multiplier when casted. |
| `Shrink.fragilityLevel` | 5 | The level of the Fragility effect when shrunk. |
| `Shrink.fragilityLevelMastered` | 3 | The level of the Fragility effect when shrunk with mastery. |

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
