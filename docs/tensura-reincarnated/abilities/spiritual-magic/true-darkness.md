# True Darkness

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![True Darkness](../../../assets/icons/tensura/skill/true_darkness.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:true_darkness` |
| **Element** | Darkness |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Press, Hold |

</div>

> Inflict Blindness on all entities and deal massive spiritual damage.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 30,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Removed and re-rolled when you change race

## Related

- **Related skills:** [Dark Cube](dark-cube.md)
- **Referenced by:** [Witch of Envy, Satella](../../../tensura-more-skills/abilities/ultimate-skills/witch-of-envy-satella.md), [Satella](../../../tensura-more-skills/abilities/unique-skills/satella.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `TrueDarkness.castTime` | 120 | Cast time in tick. |
| `TrueDarkness.castTimeMastered` | 120 | Cast time in tick when mastered. |
| `TrueDarkness.magiculeCost` | 30,000 | Magicule Cost to cast. |
| `TrueDarkness.radius` | 7.5 | The radius in block of the magic. |
| `TrueDarkness.damage` | 100 | The spiritual damage each second of the magic. |
| `TrueDarkness.darknessLevel` | 10 | The level of Darkness effect when attacked by the magic. |
| `TrueDarkness.insanityDuration` | 200 | The duration in tick of Insanity effect when attacked by the magic. |
| `TrueDarkness.trueDuration` | 200 | The max duration in tick that the magic can be used. |
| `TrueDarkness.trueDurationMastered` | 400 | The max duration in tick that the magic can be used with mastery. |

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
