# Axiom, Lord of Reflected Judgment

<small>[TensuraMoreSkills](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Axiom, Lord of Reflected Judgment](../../../assets/icons/tensuramoreskills/skill/axiom_lord_of_reflected_judgment.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `tensuramoreskills:axiom_lord_of_reflected_judgment` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 500,000 |
| **Max mastery** | 4,500 |
| **Cooldowns (s)** | 6, 35, 140 mastered, 180 otherwise |
| **Activation** | Toggle, Press, Hold |

</div>

> The perfected evolution of Reflector.

## Modes

| # | Mode |
|---|---|
| 1 | Glass Prophecy |
| 2 | Mirrorfield |
| 3 | Moment of Truth |
| 4 | Planetfall |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Glass Prophecy | 90,000 |  |
| Mirrorfield | 70,000 |  |
| Moment of Truth | 500,000 |  |
| Planetfall | 600,000 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage
- Triggers when a projectile hits you
- Triggers when you die
- Does something when first learned

## Related

- **Related skills:** [Magic Barrier](../../../tensura-reincarnated/abilities/aspectual-magic/magic-barrier.md), [Reinforcement](../../../tensura-reincarnated/abilities/aspectual-magic/reinforcement.md), [Weather Manipulation](../../../tensura-reincarnated/abilities/extra-skills/weather-manipulation.md)
- **Effects:** [Self-Regeneration](../../../tensura-reincarnated/effects/self-regeneration.md), [Movement Interference](../../../tensura-reincarnated/effects/movement-interference.md), [True Blindness](../../../tensura-reincarnated/effects/true-blindness.md), [Fragility](../../../tensura-reincarnated/effects/fragility.md)

## Stats (config defaults)

Set in [`config/tensuramoreskills-grand.toml`](../../configs/config-tensuramoreskills-grand.md).

| Option | Default | Description |
|---|---|---|
| `obtainment.maxMastery` | 4,500 (1 to no limit) | Maximum mastery for Axiom. |
| `obtainment.acquirementMagiculeCost` | 500,000 (0 to no limit) | Magicule cost required to naturally acquire Axiom. |
| `obtainment.acquirementMastery` | 0 (-1 to no limit) | Starting mastery when Axiom is obtained. |
| `obtainment.requiredSkillId` | "tensura:reflector" | Required skill registry ID. Empty string disables the required skill check if the skill code supports it. |
| `obtainment.requiredSkillMustBeMastered` | true | If true, the required skill must be mastered before Axiom can be acquired. |
| `costs.rippleScriptCost` | 90,000 (0 to no limit) |  |
| `costs.mirrorfieldCost` | 70,000 (0 to no limit) |  |
| `costs.truthCost` | 500,000 (0 to no limit) |  |
| `costs.planetfallCost` | 600,000 (0 to no limit) |  |
| `planetfall.planetfallAmplifier` | 4 (0 to 255) | Amplifier for Planetfall self buffs. |
| `ripple_script.rippleScriptRange` | 40 (1 to 512) |  |
| `ripple_script.rippleScriptDurationTicksMastered` | 600 (1 to no limit) |  |
| `ripple_script.rippleScriptDurationTicks` | 360 (1 to no limit) |  |
| `cooldowns.rippleScriptCooldownTicks` | 6 (0 to no limit) |  |
| `cooldowns.truthCooldownTicks` | 35 (0 to no limit) |  |
| `cooldowns.planetfallCooldownTicksMastered` | 140 (0 to no limit) |  |
| `cooldowns.planetfallCooldownTicks` | 180 (0 to no limit) |  |
| `mirrorfield.mirrorfieldRefreshTicks` | 10 (1 to no limit) | How often holding Mirrorfield refreshes the active field. |
| `mirrorfield.mirrorfieldActiveTicks` | 30 (1 to no limit) | How long each Mirrorfield refresh keeps the field active. |
| `passive_counter.passiveDamageReduction` | 0.4 (0 to 1) | Damage reduction while Axiom is toggled. 0.40 = 40 percent reduction. |
| `passive_counter.counterIgnoresBypassInvulnerability` | true | If true, Axiom can counter even bypass-invulnerability damage. The skill code must check this value. |
| `passive_counter.counterCooldownTicksMastered` | 3 (0 to no limit) |  |
| `passive_counter.counterCooldownTicks` | 5 (0 to no limit) |  |
| `passive_counter.counterMultiplierMastered` | 3 (0 to 1,024) | Counter damage multiplier when mastered. |
| `passive_counter.counterMultiplier` | 2.5 (0 to 1,024) | Counter damage multiplier before mastery. |
| `ripple_script.rippleScriptBonusMultiplierMastered` | 1.25 (0 to 1,024) | Bonus damage multiplier when mastered. |
| `ripple_script.rippleScriptBonusMultiplier` | 0.95 (0 to 1,024) | Bonus damage multiplier before mastery. 0.95 = 95 percent of dealt damage added again. |
| `passive_counter.projectileReflectionEnabled` | true | If false, projectile reflection should be disabled in the skill code. |
| `passive_counter.projectileReflectSpeed` | 2 (0 to 64) | Speed applied to reflected projectiles. |
| `passive_counter.projectileArrowDamageMultiplierMastered` | 3 (0 to 1,024) | Arrow damage multiplier when reflected while mastered. |
| `passive_counter.projectileArrowDamageMultiplier` | 2.5 (0 to 1,024) | Arrow damage multiplier when reflected before mastery. |
| `inversion.inversionMinimumHealth` | 20 (0 to 340282349999999991754788743781432688640) | Minimum health restored by Inversion. |
| `inversion.inversionHealthRatio` | 0.5 (0 to 1) | Health restored when Inversion prevents death. 0.5 = 50 percent of max health. |
| `inversion.inversionBarrierTicks` | 100 (1 to no limit) | Magic Barrier duration after Inversion triggers. |
| `inversion.inversionBarrierAmplifier` | 3 (0 to 255) | Magic Barrier amplifier after Inversion triggers. |
| `inversion.inversionRegenTicks` | 100 (1 to no limit) | Self Regeneration duration after Inversion triggers. |
| `inversion.inversionRegenAmplifier` | 3 (0 to 255) | Self Regeneration amplifier after Inversion triggers. |
| `mirrorfield.mirrorfieldRadius` | 26 (1 to 512) |  |
| `mirrorfield.mirrorfieldDamage` | 100 (0 to 340282349999999991754788743781432688640) | Direct damage dealt each Mirrorfield tick to enemies in range. |
| `mirrorfield.mirrorfieldMemoryDamageMastered` | 60 (0 to 340282349999999991754788743781432688640) | Memory damage recorded per Mirrorfield hit when mastered. |
| `mirrorfield.mirrorfieldMemoryDamage` | 35 (0 to 340282349999999991754788743781432688640) | Memory damage recorded per Mirrorfield hit before mastery. |
| `mirrorfield.mirrorfieldMovementInterferenceTicks` | 30 (1 to no limit) |  |
| `mirrorfield.mirrorfieldMovementInterferenceAmplifierMastered` | 2 (0 to 255) |  |
| `mirrorfield.mirrorfieldMovementInterferenceAmplifier` | 1 (0 to 255) |  |
| `planetfall.planetfallRadiusMastered` | 85 (1 to 512) |  |
| `planetfall.planetfallRadius` | 60 (1 to 512) |  |
| `planetfall.planetfallBaseDamageMastered` | 720 (0 to 340282349999999991754788743781432688640) |  |
| `planetfall.planetfallBaseDamage` | 420 (0 to 340282349999999991754788743781432688640) |  |
| `planetfall.planetfallHpPercentMastered` | 0.65 (0 to 100) | Extra Planetfall damage from target max health when mastered. |
| `planetfall.planetfallHpPercent` | 0.45 (0 to 100) | Extra Planetfall damage from target max health before mastery. 0.45 = 45 percent. |
| `planetfall.planetfallMaxDamageMastered` | 3,200 (0 to 340282349999999991754788743781432688640) |  |
| `planetfall.planetfallMaxDamage` | 1,800 (0 to 340282349999999991754788743781432688640) |  |
| `planetfall.planetfallBuffTicks` | 200 (1 to no limit) |  |
| `planetfall.planetfallExplosions` | true | If false, Planetfall should skip visual/non-grief explosions if the skill code checks this. |
| `planetfall.planetfallCenterExplosionPowerMastered` | 6 (0 to 128) |  |
| `planetfall.planetfallCenterExplosionPower` | 4.5 (0 to 128) |  |
| `planetfall.planetfallRingExplosionPowerMastered` | 4 (0 to 128) |  |
| `planetfall.planetfallRingExplosionPower` | 3 (0 to 128) |  |
| `planetfall.planetfallMinDamage` | 40 (0 to 340282349999999991754788743781432688640) |  |
| `planetfall.planetfallBlindnessTicksMastered` | 90 (1 to no limit) |  |
| `planetfall.planetfallBlindnessTicks` | 60 (1 to no limit) |  |
| `planetfall.planetfallMovementTicksMastered` | 140 (1 to no limit) |  |
| `planetfall.planetfallMovementTicks` | 110 (1 to no limit) |  |
| `planetfall.planetfallMovementAmplifierMastered` | 4 (0 to 255) |  |
| `planetfall.planetfallMovementAmplifier` | 3 (0 to 255) |  |
| `planetfall.planetfallFragilityTicksMastered` | 140 (1 to no limit) |  |
| `planetfall.planetfallFragilityTicks` | 110 (1 to no limit) |  |
| `planetfall.planetfallFragilityAmplifierMastered` | 3 (0 to 255) |  |
| `planetfall.planetfallFragilityAmplifier` | 2 (0 to 255) |  |
| `planetfall.planetfallKnockbackMastered` | 1.25 (0 to 64) |  |
| `planetfall.planetfallKnockback` | 0.95 (0 to 64) |  |
| `planetfall.planetfallVerticalKnockbackMastered` | 0.65 (0 to 64) |  |
| `planetfall.planetfallVerticalKnockback` | 0.45 (0 to 64) |  |
| `truth.truthConsumeMemoriesMastered` | 100 (1 to 10,000) | Maximum memories consumed by Truth when mastered. |
| `truth.truthConsumeMemories` | 70 (1 to 10,000) | Maximum memories consumed by Truth before mastery. |
| `truth.truthInversionMultiplier` | 1.35 (0 to 1,024) | Extra multiplier when Truth is triggered by Inversion. |
| `truth.truthRadiusMastered` | 32 (1 to 512) |  |
| `truth.truthRadius` | 26 (1 to 512) |  |
| `truth.truthFalloffMinimum` | 0.25 (0 to 1) | Minimum falloff multiplier at the edge of Truth radius. |
| `truth.truthMinDamage` | 12 (0 to 340282349999999991754788743781432688640) |  |
| `truth.truthMaxDamageMastered` | 5,000 (0 to 340282349999999991754788743781432688640) |  |
| `truth.truthMaxDamage` | 3,200 (0 to 340282349999999991754788743781432688640) |  |
| `truth.truthBlindnessTicks` | 40 (1 to no limit) |  |
| `memory.maxMemoryMastered` | 360 (1 to 10,000) | Maximum stored memories when mastered. |
| `memory.maxMemory` | 220 (1 to 10,000) | Maximum stored memories before mastery. |
