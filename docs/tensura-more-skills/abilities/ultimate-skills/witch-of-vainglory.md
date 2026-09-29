# Witch of Vainglory

<small>[TensuraMoreSkills](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Witch of Vainglory](../../../assets/icons/tensuramoreskills/skill/witch_of_vainglory.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `tensuramoreskills:witch_of_vainglory` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 300,000 |
| **Cooldowns (s)** | 120, 20, 160, 240, 1,800 |
| **Activation** | Toggle, Press |

</div>

> I always come back.

## Modes

| # | Mode |
|---|---|
| 1 | Reality Change |
| 2 | Deleted Timeline |
| 3 | False Perception |
| 4 | You Were Never Here |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Reality Change | 60,000 |  |
| Deleted Timeline | 40,000 |  |
| False Perception | 50,000 |  |
| You Were Never Here | 70,000 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you take damage
- Triggers when a projectile hits you
- Triggers when you die

## Related

- **Related skills:** [Confusion](../../../tensura-reincarnated/abilities/aspectual-magic/confusion.md), [Abnormal Condition Nullification](../../../tensura-reincarnated/abilities/resistance-skills/abnormal-condition-nullification.md)
- **Effects:** [Movement Interference](../../../tensura-reincarnated/effects/movement-interference.md), [Self-Regeneration](../../../tensura-reincarnated/effects/self-regeneration.md), [Flashed Blindness](../../../tensura-reincarnated/effects/flashed-blindness.md), [Haki Coat](../../../tensura-reincarnated/effects/haki-coat.md), [Infinite Imprisonment](../../../tensura-reincarnated/effects/infinite-imprisonment.md), [Black Burn](../../../tensura-reincarnated/effects/black-burn.md), [Magic Interference](../../../tensura-reincarnated/effects/magic-interference.md), [Magicule Poison](../../../tensura-reincarnated/effects/magicule-poison.md), [Anti-Skill](../../../tensura-reincarnated/effects/anti-skill.md), [Spatial Blockade](../../../tensura-reincarnated/effects/spatial-blockade.md), [Energy Blockade](../../../tensura-reincarnated/effects/energy-blockade.md)

## Stats (config defaults)

Set in [`config/tensuramoreskills-grand.toml`](../../configs/config-tensuramoreskills-grand.md).

| Option | Default | Description |
|---|---|---|
| `obtainment.acquirementMagiculeCost` | 300,000 (0 to no limit) | Magicule cost required to naturally acquire the skill. Set to 0 for no MP cost. |
| `obtainment.acquirementMastery` | 0 (-1 to no limit) | Starting mastery value when acquired. 0 means no starting mastery. |
| `obtainment.requiredSkillId` | "tensura:tuner" | Required skill registry ID for obtainment. Empty string disables the required skill check. |
| `obtainment.requiredSkillMustBeMastered` | true | If true, the required skill must be mastered before Witch of Vainglory can be acquired. |
| `costs.realityChangeCost` | 60,000 (0 to no limit) | Magicule cost for Reality Change. |
| `costs.deletedTimelineCost` | 40,000 (0 to no limit) | Magicule cost for Deleted Timeline. |
| `costs.falsePerceptionCost` | 50,000 (0 to no limit) | Magicule cost for False Perception. |
| `costs.neverHereCost` | 70,000 (0 to no limit) | Magicule cost for You Were Never Here. |
| `general.realityAuraRadius` | 4 (0 to 128) | Radius of the toggled reality aura around the user. |
| `general.auraEffectRefreshIntervalTicks` | 80 (1 to 72,000) | How often the toggled aura reapplies its effect. Higher is better for performance. 80 ticks = 4 seconds. |
| `general.auraEffectDurationTicks` | 100 (1 to 72,000) | Duration applied to enemies hit by the toggled aura. 20 ticks = 1 second. |
| `reality_change.realityCoatEffectRefreshIntervalTicks` | 80 (1 to no limit) | How often Reality Coat refreshes its buffs. Higher is better for performance. |
| `durations.realityCoatDurationTicks` | 200 (1 to no limit) | Duration of Reality Change's self-buff state. |
| `ranges.falsePerceptionRadius` | 16 (0 to 128) | Radius of False Perception around the caster. |
| `false_perception.falsePerceptionYawRotation` | 22.5 (-360 to 360) | Yaw rotation applied while a target remains under False Perception. |
| `reality_change.realityCoatEffectDurationTicks` | 100 (1 to no limit) | Duration of each refreshed Reality Coat effect application. |
| `reality_change.realityCoatResistanceAmplifier` | 2 (0 to 255) | Resistance amplifier during Reality Coat. 0 means level 1. |
| `reality_change.realityCoatStrengthAmplifier` | 1 (0 to 255) | Strength amplifier during Reality Coat. 0 means level 1. |
| `reality_change.realityCoatSpeedAmplifier` | 1 (0 to 255) | Speed amplifier during Reality Coat. 0 means level 1. |
| `reality_change.realityCoatRegenerationAmplifier` | 1 (0 to 255) | Self Regeneration amplifier during Reality Coat. 0 means level 1. |
| `ranges.realityChangeBurstRadius` | 5 (0 to 128) | Radius of the Reality Change burst knockback and confusion. |
| `reality_change.realityChangeKnockback` | 1.4 (0 to 64) | Knockback strength applied by the Reality Change burst. |
| `reality_change.realityChangeConfusionTicks` | 80 (1 to no limit) | Confusion duration applied by Reality Change. |
| `reality_change.realityChangeConfusionAmplifier` | 0 (0 to 255) | Confusion amplifier applied by Reality Change. 0 means level 1. |
| `ranges.realityChangeProjectileClearRadius` | 5 (0 to 128) | Radius where Reality Change deletes nearby projectiles. |
| `cooldowns.realityChangeCooldownTicks` | 120 (0 to no limit) | Cooldown after casting Reality Change. |
| `durations.counterDurationTicks` | 60 (1 to no limit) | Duration of Deleted Timeline's counter window. |
| `deleted_timeline.counterResistanceAmplifier` | 1 (0 to 255) | Resistance amplifier while Deleted Timeline is waiting to counter. 0 means level 1. |
| `cooldowns.deletedTimelineReadyCooldownTicks` | 20 (0 to no limit) | Small cooldown after preparing Deleted Timeline before it reflects damage. |
| `deleted_timeline.counterReflectMinimumDamage` | 1 (0 to 340282349999999991754788743781432688640) | Minimum reflected damage dealt by Deleted Timeline. |
| `deleted_timeline.counterReflectMultiplier` | 1.75 (0 to 1,024) | Damage reflection multiplier. Reflected damage = incoming damage multiplied by this value. |
| `cooldowns.deletedTimelineTriggeredCooldownTicks` | 160 (0 to no limit) | Cooldown after Deleted Timeline successfully reflects damage or reverses a projectile. |
| `deleted_timeline.projectileReverseFallbackSpeed` | 1.5 (0 to 128) | Speed used when a projectile has almost no movement and needs a fallback direction. |
| `deleted_timeline.projectileReverseMinimumSpeed` | 1.5 (0 to 128) | Minimum speed given to a reversed projectile. |
| `durations.falsePerceptionDurationTicks` | 160 (1 to no limit) | Duration of False Perception effects. |
| `false_perception.falsePerceptionBlindnessAmplifier` | 0 (0 to 255) | Flashed Blindness amplifier. 0 means level 1. |
| `false_perception.falsePerceptionConfusionAmplifier` | 0 (0 to 255) | Confusion amplifier. 0 means level 1. |
| `false_perception.falsePerceptionMovementInterferenceAmplifier` | 0 (0 to 255) | Movement Interference amplifier. 0 means level 1. |
| `false_perception.falsePerceptionTeleportSpread` | 2.5 (0 to 64) | Random teleport spread for affected targets. Higher values scatter targets further. |
| `cooldowns.falsePerceptionCooldownTicks` | 120 (0 to no limit) | Cooldown after casting False Perception. |
| `ranges.neverHereRadius` | 24 (0 to 128) | Radius of You Were Never Here around the caster. |
| `cooldowns.neverHereCooldownTicks` | 240 (0 to no limit) | Cooldown after casting You Were Never Here. |
| `rewritten_death.maxRevivesPerDay` | 3 (0 to no limit) | Maximum number of death rewrites per Minecraft day. |
| `rewritten_death.reviveHealthRatio` | 0.6 (0 to 1) | Health restored on revive as a percentage of max health. 0.6 = 60%. |
| `rewritten_death.reviveMinimumHealth` | 20 (0 to 340282349999999991754788743781432688640) | Minimum health restored by revive, even if the percentage would be lower. |
| `rewritten_death.reviveInvulnerabilityTicks` | 80 (0 to no limit) | Invulnerability ticks after revive. |
| `rewritten_death.reviveResistanceTicks` | 100 (1 to no limit) | Resistance duration after revive. |
| `rewritten_death.reviveResistanceAmplifier` | 4 (0 to 255) | Resistance amplifier after revive. 0 means level 1. |
| `rewritten_death.reviveRegenerationTicks` | 200 (1 to no limit) | Self Regeneration duration after revive. |
| `rewritten_death.reviveRegenerationAmplifier` | 1 (0 to 255) | Self Regeneration amplifier after revive. 0 means level 1. |
| `rewritten_death.reviveHakiCoatTicks` | 120 (1 to no limit) | Haki Coat duration after revive. |
| `rewritten_death.reviveHakiCoatAmplifier` | 0 (0 to 255) | Haki Coat amplifier after revive. 0 means level 1. |
| `rewritten_death.reviveSpiritualHealthRatio` | 0.5 (0 to 1) | Minimum spiritual health restored on revive as a percentage of max spiritual health. |
| `rewritten_death.reviveAuraRatio` | 0.4 (0 to 1) | Minimum aura restored on revive as a percentage of max aura. |
| `rewritten_death.reviveMagiculeRatio` | 0.4 (0 to 1) | Minimum magicules restored on revive as a percentage of max magicules. |
| `cooldowns.rewrittenCooldownTicks` | 1,800 (0 to no limit) | Cooldown applied to all modes after the death rewrite revive triggers. |

## In-game messages

<details markdown><summary>Show 11 messages</summary>

- Reality twists around you.
- The world snaps back into place.
- Your arms are coated in impossible reality.
- The coating of reality fades.
- The timeline around you fractures and becomes soft.
- The deleted damage rewinds—reality pays back your suffering.
- Everyone’s senses twist. Nothing feels real anymore.
- The world remembers the place they belong.
- Reality is rewritten. Your death is denied.
- Reality refuses to be rewritten again today.
- Reality corrects your existence. You were never here.

</details>
