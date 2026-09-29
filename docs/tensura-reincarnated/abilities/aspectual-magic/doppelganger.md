# Doppelganger

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Doppelganger](../../../assets/icons/tensura/skill/doppelganger.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:doppelganger` |
| **Element** | Misc |
| **Max mastery** | 300 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Hold |

</div>

> Use percentages of the user's magical power to create identical clones around them.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | base max MP × 0.1 ÷ 5 |  |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when one of your subordinates dies

## Obtaining

- Can appear in rare tomes in burnt wizard towers

## Related

- **Effects:** [Fragility](../../effects/fragility.md), [Energy Blockade](../../effects/energy-blockade.md)
- **Referenced by:** [Body Double](../extra-skills/body-double.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Doppelganger.castTime` | 100 | Cast time in tick. |
| `Doppelganger.castTimeMastered` | 80 | Cast time in tick when mastered. |
| `Doppelganger.magiculeCost` | 0.1 | The multiplier of the user's maximum Magicule to be calculated for the magicule cost of the magic. |
| `Doppelganger.cloneNumber` | 2 | The number of clones can the magic create each cast. |
| `Doppelganger.cloneNumberMastered` | 4 | The number of clones can the magic create each cast when mastered while sneaking. |
| `Doppelganger.cloneHeal` | 2 | The amount of HP that a clone heals each second. |
| `Doppelganger.cloneHealEnergy` | 20 | The amount of Energy that a clone uses each second when healing. |
| `Doppelganger.cloneFragility` | 2 | The level of Fragility that each clone has. |
| `Doppelganger.cooldown` | 5 | The cooldown in second to spawn a clone. |
| `Doppelganger.cooldownMastered` | 3 | The cooldown in second to spawn a clone when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/rare_tome_burnt_wizard_tower`
