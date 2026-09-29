# Reinforced Barrier

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Reinforced Barrier](../../../assets/icons/tensura/skill/reinforced_barrier.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:reinforced_barrier` |
| **Element** | Barrier |
| **Modes** | 3 |
| **Max mastery** | 300 |
| **Cooldowns (s)** | 45 |
| **Activation** | Hold |

</div>

> Coat the caster with reinforced Barriers with the strength based on Health.

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Magic Defense |
| 3 | Physical Defense |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | max(5,000, base max MP × 0.05) |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Arch Daemon](../../mobs/arch-daemon.md)
- Sold by dwarf traders (medium rare tome)
- Can appear in rare tomes in buried wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Related skills:** [Barrier](barrier.md), [Magic Barrier](magic-barrier.md)
- **Effects:** [Physical Barrier](../../effects/physical-barrier.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `ReinforcedBarrier.castTime` | 160 | Cast time in tick. |
| `ReinforcedBarrier.magiculeMultiplierCost` | 0.05 | The multiplier of the caster's Max Magicule to be calculated for the Magicule Cost to cast. |
| `ReinforcedBarrier.minCost` | 5,000 | Minimum Magicule Cost to cast. |
| `ReinforcedBarrier.barrierThreshold` | 0.2 | The multiplier of the caster's HP to be the damage threshold for the Barrier effect. |
| `ReinforcedBarrier.belowReduction` | 0.2 | The multiplier of the caster's HP to be reduced from the damage taken when the damage is below the threshold. |
| `ReinforcedBarrier.aboveReduction` | 0.1 | The multiplier of the caster's HP to be reduced from the damage taken when the damage is above the threshold. |
| `ReinforcedBarrier.barrierDuration` | 600 | The duration in tick of the Barrier effect. |
| `ReinforcedBarrier.barrierThresholdMagic` | 0.25 | The multiplier of the caster's HP to be the magic damage threshold for the Barrier effect of the Magic Defense mode. |
| `ReinforcedBarrier.belowReductionMagic` | 0.25 | The multiplier of the caster's HP to be reduced from the magic damage taken when the damage is below the threshold with the Magic Defense mode. |
| `ReinforcedBarrier.aboveReductionMagic` | 0.125 | The multiplier of the caster's HP to be reduced from the magic damage taken when the damage is above the threshold with the Magic Defense mode. |
| `ReinforcedBarrier.barrierDurationMagic` | 300 | The duration in tick of the Barrier effect of the Magic Defense mode. |
| `ReinforcedBarrier.cooldownMagic` | 45 | The cooldown in second of the Magic Defense mode. |
| `ReinforcedBarrier.barrierThresholdPhysical` | 0.25 | The multiplier of the caster's HP to be the physical damage threshold for the Barrier effect of the Physical Defense mode. |
| `ReinforcedBarrier.belowReductionPhysical` | 0.25 | The multiplier of the caster's HP to be reduced from the physical damage taken when the damage is below the threshold with the Physical Defense mode. |
| `ReinforcedBarrier.aboveReductionPhysical` | 0.125 | The multiplier of the caster's HP to be reduced from the physical damage taken when the damage is above the threshold with the Physical Defense mode. |
| `ReinforcedBarrier.barrierDurationPhysical` | 300 | The duration in tick of the Barrier effect of the Physical Defense mode. |
| `ReinforcedBarrier.cooldownPhysical` | 45 | The cooldown in second of the Physical Defense mode. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Learning.learningFailCooldown` | 3 | The number of seconds of cooldown when a new ability fails to gain a learning point. |
| `Learning.learningPoint` | 1 | The base value of how many learning points the player gains when learning an ability. |
| `Learning.minBonus` | 0 | The min bonus learning points the player can gain when learning an ability. |
| `Learning.maxBonus` | 4 | The max bonus learning points the player can gain when learning an ability. |
| `Learning.learningCostMultiplier` | 5 | The multiplier of energy cost compared to normal cost when learning a new ability. |
| `Learning.learningPointRequirement` | 100 | The number of learning points a new ability need to get to become fully learnt. |
| `Learning.learningCooldown` | 10 | The number of seconds of cooldown when a new ability gains a learning point. |
| `Learning.learningFailCooldown` | 3 | The number of seconds of cooldown when a new ability fails to gain a learning point. |
| `Learning.failingPenaltyChance` | 0.1 | The chance to the failing penalty to apply. |
| `Learning.failingPenaltyLevel` | 1 | The level of the misfire status effect when failing penalty applies. |
| `Learning.failingPenaltyDuration` | 200 | The duration in ticks of the misfire status effect when failing penalty applies. |
| `Learning.failingPenaltyMin` | 1 | The min learning points the player can lose when failing to learn an ability. |
| `Learning.failingPenaltyMax` | 3 | The max learning points the player can lose when failing to learn an ability. |
| `battlewillManualList` | "tensura:aura_slash", "tensura:aura_sword", "tensura:earthshatter_kick", "tensura:ogre_sword_guillotine", "tensura:roaring_lion_punch", "tensura:dark_eight_palms", "tensura:elephant_stampede", "tensura:magic_bullet", "tensura:ogre_flame", "tensura:air_flight", "tensura:aura_shield", "tensura:battlewill", "tensura:diamond_path", "tensura:formhide", "tensura:instant_move", "tensura:violent_break" | List of Battlewills that can be randomly obtained from using the Battlewill Manual. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/medium_rare_tome_dwarf_trade`, `tensura:skills/rare_tome_buried_wizard_tower`
