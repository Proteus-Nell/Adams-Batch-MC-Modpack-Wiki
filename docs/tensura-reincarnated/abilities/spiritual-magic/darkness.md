# Darkness

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Darkness](../../../assets/icons/tensura/skill/darkness.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:darkness` |
| **Element** | Darkness |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Hold |

</div>

> Call on your spirit to reduce the enemy's vision in a wide area.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Removed and re-rolled when you change race

## Related

- **Referenced by:** [Witch of Envy, Satella](../../../tensura-more-skills/abilities/ultimate-skills/witch-of-envy-satella.md), [Satella](../../../tensura-more-skills/abilities/unique-skills/satella.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `Darkness.castTime` | 40 | Cast time in tick. |
| `Darkness.castTimeMastered` | 40 | Cast time in tick when mastered. |
| `Darkness.magiculeCost` | 100 | Magicule Cost to cast. |
| `Darkness.radius` | 7.5 | The radius in block of the magic. |
| `Darkness.radiusMastered` | 15 | The radius in block of the magic when mastered. |
| `Darkness.darknessLevel` | 5 | The level of the Darkness effect when casted. |
| `Darkness.darknessDuration` | 1,800 | The duration of the Darkness effect when casted. |
| `Darkness.darknessDurationMastered` | 3,600 | The duration of the Darkness effect when casted with mastery. |

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
