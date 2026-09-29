# Barrier

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Barrier](../../../assets/icons/tensura/skill/barrier.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:barrier` |
| **Element** | Barrier |
| **Max mastery** | 300 |
| **Activation** | Hold |

</div>

> Coat the caster with a Physical Barrier with the strength based on Health.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | max(2,000, base max MP × 0.05) |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (medium rare tome)
- Can appear in rare tomes in buried wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Effects:** [Physical Barrier](../../effects/physical-barrier.md)
- **Referenced by:** [Reinforced Barrier](reinforced-barrier.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Barrier.castTime` | 160 | Cast time in tick. |
| `Barrier.magiculeMultiplierCost` | 0.05 | The multiplier of the caster's Max Magicule to be calculated for the Magicule Cost to cast. |
| `Barrier.minCost` | 2,000 | Minimum Magicule Cost to cast. |
| `Barrier.barrierThreshold` | 0.1667 | The multiplier of the caster's HP to be the physical damage threshold for the Barrier effect. |
| `Barrier.belowReduction` | 0.1667 | The multiplier of the caster's HP to be reduced from the physical damage taken when the damage is below the threshold. |
| `Barrier.aboveReduction` | 0.0833 | The multiplier of the caster's HP to be reduced from the physical damage taken when the damage is above the threshold. |
| `Barrier.barrierThresholdMastered` | 0.2 | The multiplier of the caster's HP to be the physical damage threshold for the Barrier effect when mastered. |
| `Barrier.belowReductionMastered` | 0.2 | The multiplier of the caster's HP to be reduced from the physical damage taken when the damage is below the threshold when mastered. |
| `Barrier.aboveReductionMastered` | 0.1 | The multiplier of the caster's HP to be reduced from the physical damage taken when the damage is above the threshold when mastered. |
| `Barrier.barrierDuration` | 200 | The duration in tick of the Barrier effect. |
| `Barrier.barrierDurationMastered` | 400 | The duration in tick of the Barrier effect when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/medium_rare_tome_dwarf_trade`, `tensura:skills/rare_tome_buried_wizard_tower`
