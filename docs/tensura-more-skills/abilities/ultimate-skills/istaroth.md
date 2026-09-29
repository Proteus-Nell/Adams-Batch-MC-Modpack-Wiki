# Istaroth

<small>[TensuraMoreSkills](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `tensuramoreskills:istaroth` |
| **Modes** | 10 |
| **Cooldowns (s)** | 24, 8, 11, 6, 55, 42 |
| **Activation** | Toggle, Press, Hold |

</div>

> Time abides no reason—  
> For it deprives us all equally.  
> Yet brooks not a second to be reclaimed.

## Modes

| # | Mode |
|---|---|
| 1 | Chronicle |
| 2 | Time Skip |
| 3 | Duration |
| 4 | Stasis |
| 5 | Rewind |
| 6 | Causality |
| 7 | Loop |
| 8 | Temporal Banishment |
| 9 | World of Still Seconds |
| 10 | The Last Second of Creation |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Chronicle | 650 |  |
| Time Skip | 2,200 mastered, 3,200 otherwise |  |
| Duration | 3,600 mastered, 5,200 otherwise |  |
| Stasis | 4,600 mastered, 6,800 otherwise |  |
| Rewind | 7,000 mastered, 9,500 otherwise |  |
| Causality | 6,500 mastered, 9,000 otherwise |  |
| Loop | 16,000 mastered, 23,000 otherwise |  |
| Temporal Banishment | 12,500 mastered, 18,000 otherwise |  |
| World of Still Seconds | 1,200 mastered, 1,700 otherwise |  |
| The Last Second of Creation | 110,000 mastered, 190,000 otherwise |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you are attacked
- Triggers when an effect is applied to you
- Does something when first learned

## Related

- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/tensuramoreskills-grand.toml`](../../configs/config-tensuramoreskills-grand.md).

| Option | Default | Description |
|---|---|---|
| `costs.chronicleCost` | 650 (0 to no limit) | Magicule cost for Chronicle, the information/status reading mode. |
| `costs.timeSkipCostMastered` | 2,200 (0 to no limit) | Magicule cost for Time Skip after mastery. |
| `costs.timeSkipCost` | 3,200 (0 to no limit) | Magicule cost for Time Skip before mastery. |
| `costs.durationCostMastered` | 3,600 (0 to no limit) | Magicule cost for duration-manipulation moves after mastery. |
| `costs.durationCost` | 5,200 (0 to no limit) | Magicule cost for duration-manipulation moves like Borrowed Seconds and Eternal Moment before mastery. |
| `costs.stasisCostMastered` | 4,600 (0 to no limit) | Magicule cost for Object Permanence / stasis style moves after mastery. |
| `costs.stasisCost` | 6,800 (0 to no limit) | Magicule cost for Object Permanence / stasis style moves before mastery. |
| `costs.rewindCostMastered` | 7,000 (0 to no limit) | Magicule cost for rewind effects after mastery. |
| `costs.rewindCost` | 9,500 (0 to no limit) | Magicule cost for rewind effects before mastery. |
| `costs.causalityCostMastered` | 6,500 (0 to no limit) | Magicule cost for causality attacks after mastery. |
| `costs.causalityCost` | 9,000 (0 to no limit) | Magicule cost for causality attacks like Delayed Verdict, Effect Before Cause, and Condemned Repeat before mastery. |
| `costs.loopCostMastered` | 16,000 (0 to no limit) | Magicule cost for Twenty-Second Causality Loop after mastery. |
| `costs.loopCost` | 23,000 (0 to no limit) | Magicule cost for Twenty-Second Causality Loop before mastery. |
| `costs.banishmentCostMastered` | 12,500 (0 to no limit) | Magicule cost for Future Exile / Past Burial after mastery. |
| `costs.banishmentCost` | 18,000 (0 to no limit) | Magicule cost for Future Exile / Past Burial before mastery. |
| `costs.worldOfStillSecondsCostMastered` | 1,200 (0 to no limit) | Magicule cost per use/tick cycle for World of Still Seconds after mastery. |
| `costs.worldOfStillSecondsCost` | 1,700 (0 to no limit) | Magicule cost per use/tick cycle for World of Still Seconds before mastery. |
| `costs.lastSecondCostMastered` | 110,000 (0 to no limit) | Magicule cost for Last Second of Creation after mastery. |
| `costs.lastSecondCost` | 190,000 (0 to no limit) | Magicule cost for Last Second of Creation before mastery. |
| `cooldowns.chronicleAnchorCooldownTicks` | 24 (0 to no limit) | Cooldown for manually saving a rewind anchor in ticks. |
| `cooldowns.chronicleCooldownTicks` | 8 (0 to no limit) | Cooldown for Chronicle in ticks. |
| `cooldowns.momentumTheftCooldownTicks` | 11 (0 to no limit) | Cooldown for Momentum Theft in ticks. |
| `cooldowns.timeSkipCooldownTicks` | 6 (0 to no limit) | Cooldown for Time Skip in ticks. |
| `cooldowns.eternalMomentCooldownTicks` | 55 (0 to no limit) | Cooldown for Eternal Moment in ticks. |
| `cooldowns.borrowedSecondsCooldownTicks` | 24 (0 to no limit) | Cooldown for Borrowed Seconds in ticks. |
| `cooldowns.objectPermanenceCooldownTicks` | 42 (0 to no limit) | Cooldown for Object Permanence in ticks. |
| `cooldowns.stasisCooldownTicks` | 30 (0 to no limit) | Cooldown for stasis-category moves in ticks. |
| `cooldowns.rewindTargetCooldownTicks` | 55 (0 to no limit) | Cooldown for target rewind in ticks. |
| `cooldowns.rewindSelfCooldownTicks` | 38 (0 to no limit) | Cooldown for self rewind in ticks. |
| `cooldowns.effectBeforeCauseCooldownTicks` | 24 (0 to no limit) | Cooldown for Effect Before Cause in ticks. |
| `cooldowns.delayedVerdictCooldownTicks` | 34 (0 to no limit) | Cooldown for Delayed Verdict in ticks. |
| `cooldowns.condemnedRepeatCooldownTicks` | 70 (0 to no limit) | Cooldown for Condemned Repeat in ticks. |
| `cooldowns.loopCooldownTicks` | 100 (0 to no limit) | Cooldown for Twenty-Second Causality Loop in ticks. |
| `cooldowns.pastBurialCooldownTicks` | 42 (0 to no limit) | Cooldown for Past Burial in ticks. |
| `cooldowns.futureExileCooldownTicks` | 75 (0 to no limit) | Cooldown for Future Exile in ticks. |
| `cooldowns.worldStopReleaseCooldownTicksMastered` | 48 (0 to no limit) | Cooldown for Clockbreak Release after mastery. |
| `cooldowns.worldStopReleaseCooldownTicks` | 70 (0 to no limit) | Cooldown for Clockbreak Release before mastery. |
| `world_stop.worldStopMaxHeldTicksMastered` | 230 (1 to no limit) | Maximum hold duration for World of Still Seconds after mastery. |
| `world_stop.worldStopMaxHeldTicks` | 150 (1 to no limit) | Maximum hold duration for World of Still Seconds before mastery. |
| `chrono_divinity.chronoMoveSpeedMastered` | 0.34 (-1 to 100) | Passive movement speed modifier after mastery. |
| `chrono_divinity.chronoMoveSpeed` | 0.24 (-1 to 100) | Passive movement speed modifier before mastery. |
| `chrono_divinity.chronoAttackSpeedMastered` | 0.48 (-1 to 100) | Passive attack speed modifier after mastery. |
| `chrono_divinity.chronoAttackSpeed` | 0.34 (-1 to 100) | Passive attack speed modifier before mastery. |
| `chrono_divinity.chronoFlyingSpeedMastered` | 0.32 (-1 to 100) | Passive flying speed modifier after mastery. |
| `chrono_divinity.chronoFlyingSpeed` | 0.2 (-1 to 100) | Passive flying speed modifier before mastery. |
| `chrono_divinity.chronoChantSpeedMastered` | 0.75 (-1,000 to 1,000) | Chant speed bonus after mastery. |
| `chrono_divinity.chronoChantSpeed` | 0.48 (-1,000 to 1,000) | Chant speed bonus before mastery. |
| `chrono_divinity.chronoPresenceSenseMastered` | 4 (-1,000 to 1,000) | Presence sensing bonus after mastery. |
| `chrono_divinity.chronoPresenceSense` | 2.5 (-1,000 to 1,000) | Presence sensing bonus before mastery. |
| `chrono_divinity.chronoDodgeInvulnerabilityMastered` | 0.6 (-1,000 to 1,000) | Extra dodge / invulnerability strength after mastery. |
| `chrono_divinity.chronoDodgeInvulnerability` | 0.36 (-1,000 to 1,000) | Extra dodge / invulnerability strength before mastery. |
| `chrono_divinity.chronoResistanceDegradationMastered` | 2.25 (-1,000 to 1,000) | How strongly Istaroth degrades enemy resistance after mastery. |
| `chrono_divinity.chronoResistanceDegradation` | 1.25 (-1,000 to 1,000) | How strongly Istaroth degrades enemy resistance before mastery. |
| `chrono_divinity.predictionMeleeDodgeMastered` | 24 (-1,000 to 1,000) | Melee prediction dodge strength after mastery. |
| `chrono_divinity.predictionMeleeDodge` | 13 (-1,000 to 1,000) | Melee prediction dodge strength before mastery. |
| `chrono_divinity.predictionProjectileDodgeMastered` | 40 (-1,000 to 1,000) | Projectile prediction dodge strength after mastery. |
| `chrono_divinity.predictionProjectileDodge` | 22 (-1,000 to 1,000) | Projectile prediction dodge strength before mastery. |
| `chrono_divinity.outsideStreamLawDegradation` | 1.5 (-1,000 to 1,000) | Law resistance degradation applied by Outside the Stream. |
| `chrono_divinity.outsideStreamSpaceDegradation` | 1.5 (-1,000 to 1,000) | Space resistance degradation applied by Outside the Stream. |
