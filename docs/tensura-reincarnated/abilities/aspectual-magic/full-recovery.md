# Full Recovery

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Full Recovery](../../../assets/icons/tensura/skill/full_recovery.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:full_recovery` |
| **Element** | Recovery |
| **Max mastery** | 700 |
| **Cooldowns (s)** | 10 mastered, 15 otherwise |
| **Activation** | Hold |

</div>

> Recover a living being's health and food points to the maximum as well as Absorption.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 30,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (high rare tome)
- Can appear in rare tomes in frozen wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Related skills:** [Recovery](recovery.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `FullRecovery.castTime` | 120 | Cast time in tick. |
| `FullRecovery.castTimeMastered` | 80 | Cast time in tick when mastered. |
| `FullRecovery.minCost` | 30,000 | Minimal Magicule Cost to cast. |
| `FullRecovery.magiculeCost` | 100 | Magicule Cost  to heal each HP. |
| `FullRecovery.range` | 6 | The range in block of the magic. |
| `FullRecovery.hpHealPercentage` | 1 | The percentage of max HP that the magic heals. |
| `FullRecovery.foodPoint` | 20 | The amount of food point that the magic gives. |
| `FullRecovery.saturationPoint` | 20 | The amount of saturation point that the magic gives. |
| `FullRecovery.absorptionLevel` | 4 | The level of Absorption that the magic gives. |
| `FullRecovery.absorptionDuration` | 2,400 | The duration in second of Absorption that the magic gives. |
| `FullRecovery.absorptionDurationMastered` | 4,800 | The duration in second of Absorption that the magic gives when mastered. |
| `FullRecovery.cooldown` | 15 | The cooldown in second when activated Healing. |
| `FullRecovery.cooldownMastered` | 10 | The cooldown in second when activated Healing with mastery. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
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

`tensura:skills/aspectual_magic`, `tensura:skills/high_rare_tome_dwarf_trade`, `tensura:skills/rare_tome_frozen_wizard_tower`
