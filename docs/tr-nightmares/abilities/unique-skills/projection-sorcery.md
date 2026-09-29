# Projection Sorcery

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Projection Sorcery](../../../assets/icons/trnightmare/skill/projection_sorcery.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:projection_sorcery` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 100,000 |
| **Max mastery** | 1,000 |
| **Cooldowns (s)** | 1, 2 |
| **Activation** | Toggle, Press |

</div>

> Manipulate projected frames, afterimages, and glassed strikes.

## Modes

| # | Mode |
|---|---|
| 1 | 360 Barrage |
| 2 | Speed Blitz |
| 3 | Projection Breaker |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| 360 Barrage | 75 |  |
| Speed Blitz | 125 |  |
| Projection Breaker | 40 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Triggers when you damage a target

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| asp | 1.5 | multiply total |
| speed | delta | multiply total |
| step | step boost | add |
| step | surge | add |

## Related

- **Related skills:** [Pain Resistance](../../../tensura-reincarnated/abilities/resistance-skills/pain-resistance.md), [Pain Nullification](../../../tensura-reincarnated/abilities/resistance-skills/pain-nullification.md)
- **Effects:** [Projection Glass](../../effects/projection-glass.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `projectionSorcery.epAcquirement` | 100,000 | EP / magicule obtainment cost to acquire Projection Sorcery. |
| `projectionSorcery.learningCost` | 1,000 | Learning / mastery cost. |
| `projectionSorcery.maxMastery` | 1,000 | Max mastery. |
| `projectionSorcery.framesUpkeepMagiculeCost` | 6 | Magicule cost each upkeep check while toggled on. |
| `projectionSorcery.framesUpkeepIntervalTicks` | 20 | Ticks between energy upkeep checks while toggled. |
| `projectionSorcery.barrageCooldownSeconds` | 10 | Cooldown in seconds for 360 Barrage (mode 0). |
| `projectionSorcery.speedBlitzCooldownSeconds` | 15 | Cooldown in seconds for Speed Blitz (mode 1). |
| `projectionSorcery.breakerCooldownSeconds` | 2 | Cooldown in seconds for Breaker (mode 2). |
| `projectionSorcery.failCooldownSeconds` | 1 | Cooldown in seconds when an aimed mode fails (no valid target). |
| `projectionSorcery.sprintBuildupTicks` | 200 | Sprint ticks to fully charge projection speed multiplier. |
| `projectionSorcery.speedRampMaxBonus` | 4 | Bonus to speed multiplier at full sprint charge (max mult = 1 + this). |
| `projectionSorcery.stepHeightFromSprintMax` | 5 | Step height from sprint (ADD_VALUE) at full charge = progress \* this. |
| `projectionSorcery.toggledAttackSpeedMultBonus` | 1.5 | Attack speed bonus while toggled |
| `projectionSorcery.highSpeedThreshold` | 2 | Speed mult at/above which step surge apply |
| `projectionSorcery.stepSurgeMin` | 0.35 | Minimum extra step height at the high-speed threshold. |
| `projectionSorcery.stepSurgeExtra` | 1.65 | Extra step height added from threshold to max projection speed. |
| `projectionSorcery.barrageStrikes` | 60 | 360 Barrage: strike count. |
| `projectionSorcery.barrageDurationTicks` | 100 | 360 Barrage: total session duration in ticks (timing spread across strikes). |
| `projectionSorcery.barrageOrbitLoops` | 8 | 360 Barrage: full orbit loops around target over all strikes. |
| `projectionSorcery.barrageOrbitRadius` | 1.6 | 360 Barrage: orbit radius in blocks. |
| `projectionSorcery.combatModeTargetRange` | 24 | 360 Barrage / Speed Blitz: raycast targeting range. |
| `projectionSorcery.barrageDamageMultNormal` | 2.5 | 360 Barrage: total damage multiplier vs base punch when not mastered. |
| `projectionSorcery.barrageDamageMultMastered` | 5 | 360 Barrage: total damage multiplier vs base punch when mastered. |
| `projectionSorcery.speedBlitzDamageMultNormal` | 4 | Speed Blitz: total damage multiplier vs base punch when not mastered. |
| `projectionSorcery.speedBlitzDamageMultMastered` | 8 | Speed Blitz: total damage multiplier vs base punch when mastered. |
| `projectionSorcery.speedBlitzStrikes` | 18 | Speed Blitz: strike count. |
| `projectionSorcery.speedBlitzDurationTicks` | 80 | Speed Blitz: total session duration in ticks. |
| `projectionSorcery.speedBlitzPasses` | 6 | Speed Blitz: number of approach directions (theta slots). |
| `projectionSorcery.speedBlitzHitsPerPass` | 3 | Hits per pass before advancing theta. |
| `projectionSorcery.speedBlitzApproachBlocks` | 11 | Speed Blitz: approach distance from target along pass axis (blocks). |
| `projectionSorcery.speedBlitzFinisherKnockXZ` | 1.6 | Speed Blitz: horizontal knock on finisher. |
| `projectionSorcery.speedBlitzFinisherKnockY` | 0.45 | Speed Blitz: vertical knock on finisher. |
| `projectionSorcery.breakerTargetRange` | 12 | Breaker: targeting range (blocks). |
| `projectionSorcery.breakerSlapFraction` | 0.25 | Breaker: first hit uses min(baseMelee \* this, cap). |
| `projectionSorcery.breakerSlapDamageCap` | 6 | Breaker: cap on first slap damage. |
| `projectionSorcery.breakerSecondHitDamage` | 30 | Breaker: second hit flat damage. |
| `projectionSorcery.breakerKnockXZ` | 1.35 | Breaker: knockback XZ scale on target. |
| `projectionSorcery.breakerKnockY` | 0.4 | Breaker: knockback Y on target. |
| `projectionSorcery.breakerExplosionSpeedScale` | 2 | Breaker: explosion size = clamp(this \* (speedMult - 1), min, max). |
| `projectionSorcery.breakerExplosionMin` | 0.5 | Breaker: minimum explosion radius. |
| `projectionSorcery.breakerExplosionMax` | 8 | Breaker: maximum explosion radius. |
| `projectionSorcery.projectionGlassDurationTicks` | 20 | Projection Glass duration from Breaker / on-hit (ticks), not mastered. |
| `projectionSorcery.projectionGlassDurationTicksMastered` | 60 | Projection Glass duration when mastered (ticks). |
| `projectionSorcery.projectionGlassOnReceiveDurationTicks` | 60 | Projection Glass duration when you take damage while toggled (ticks). |
| `projectionSorcery.ramMinSprintTicks` | 50 | Ram hits: minimum sprint buildup ticks before ram damage can proc. |
| `projectionSorcery.ramSearchInflate` | 1 | Ram: AABB inflation for finding targets (blocks). |
| `projectionSorcery.ramDamageMultiplier` | 0.875 | Ram: damage multiplier vs base melee. |
| `projectionSorcery.onAttackGlassProcRoll` | 20 | On-attack Projection Glass proc: roll 1 in this (higher = rarer). |
| `projectionSorcery.perTargetCollisionCooldownTicks` | 4 | Per-entity cooldown for ram hits, on-hit glass proc, etc. (ticks). |
| `projectionSorcery.glassOnReceiveChanceBase` | 30 | Chance (0-100) to apply Projection Glass when damaged while toggled (base). |
| `projectionSorcery.glassOnReceiveChancePainRes` | 15 | Chance when target has Pain Resistance. |
| `projectionSorcery.glassOnReceiveChancePainNull` | 5 | Chance when target has Pain Nullification. |
| `projectionSorcery.trailCatchupTicks` | 96 | Trail: ticks of visual catch-up after sprint stops. |
| `projectionSorcery.framePhasePerTick` | 24 | Trail: frame phase added per tick while trail runs. |
| `projectionSorcery.trailChimeSpeedClampMin` | 1.05 | Trail chime interval clamps: minimum speed mult. |
| `projectionSorcery.solarBurstParticleMinSpeed` | 2.1 | Solar burst particles: minimum speed mult. |
| `projectionSorcery.solarBurstParticleRoll` | 30 | Solar burst: roll 1 in this each ambient tick when above min speed. |
| `projectionSorcery.waterTreadMinHorizontalSpeedSq` | 0.06 | Water skim: minimum horizontal speed squared to engage. |
| `projectionSorcery.waterTreadSurfaceBandTop` | 0.15 | Water skim: max feet above fluid surface (blocks). |
| `projectionSorcery.waterTreadSurfaceBandBottom` | 0.65 | Water skim: max feet below fluid surface (blocks). |
| `projectionSorcery.waterTreadNudgeFactor` | 0.4 | Water skim: nudge toward surface (blocks per tick factor). |
| `projectionSorcery.waterTreadOnGroundEpsilon` | 0.22 | Water skim: treat as on-ground when feet within this of surface (blocks). |
| `projectionSorcery.meleePocketRange` | 2.5 | Fallback melee target search radius when raycast misses (blocks). |
| `projectionSorcery.magiculeCostBarrage` | 75 | Magicule cost: 360 Barrage (mode 0). |
| `projectionSorcery.magiculeCostSpeedBlitz` | 125 | Magicule cost: Speed Blitz (mode 1). |
| `projectionSorcery.magiculeCostBreaker` | 40 | Magicule cost: Breaker (mode 2). |
| `projectionSorcery.trailVisibleMinSpeedMult` | 1.25 | Trail: minimum speed mult before any afterimage slots appear. |
| `projectionSorcery.trailVisibleMaxSpeedMult` | 3 | Trail: upper speed mult for scaling slot count (pairs with speedRamp max). |
| `projectionSorcery.trailHistoryStrideStep` | 0.5 | Trail: history stride step per 0.5 speed above trailVisibleMinSpeedMult. |
| `projectionSorcery.trailHistoryStrideMaxExtra` | 4 | Trail: max extra history indices to skip (0-4). |
