# Eye Of Balor

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Eye Of Balor](../../../assets/icons/trnightmare/skill/magical_eye.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:magical_eye` |
| **Activation** | Toggle, Press |

</div>

> The Magical Eye is a specialized magical ability that allows one to see the rhythm of ones soul.

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you are attacked
- Triggers when you take damage
- Triggers when a projectile hits you

## Obtaining

- Intrinsic skill of: [Mutant Giant](../../races/mutant-giant.md)

## Related

- **Effects:** [Future Vision](../../../tensura-reincarnated/effects/future-vision.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `MagicalEye.epAcquirement` | 20,000 | EP obtainment cost. |
| `MagicalEye.learningCost` | 1,000 | Learning cost. |
| `MagicalEye.dodgeChanceNormal` | 0.5 | Dodge chance when not mastered (0–1). |
| `MagicalEye.dodgeChanceMastered` | 0.7 | Dodge chance when mastered. |
| `MagicalEye.takenDamageMultiplierNormal` | 0.7 | Incoming damage multiplier when not mastered (retain this fraction). |
| `MagicalEye.takenDamageMultiplierMastered` | 0.5 | Incoming damage multiplier when mastered. |
| `MagicalEye.criticalChanceBonusNormal` | 33 | Critical chance attribute bonus when not mastered. |
| `MagicalEye.criticalChanceBonusMastered` | 50 | Critical chance attribute bonus when mastered. |
| `MagicalEye.futureVisionDurationNormal` | 200 | Future Vision duration (ticks) when not mastered. |
| `MagicalEye.futureVisionDurationMastered` | 400 | Future Vision duration (ticks) when mastered. |
| `MagicalEye.analysisLevelNormal` | 1 | Analysis level when not mastered. |
| `MagicalEye.analysisLevelMastered` | 2 | Analysis level when mastered. |
| `MagicalEye.analysisDistanceNormal` | 5 | Analysis distance when not mastered. |
| `MagicalEye.analysisDistanceMastered` | 10 | Analysis distance when mastered. |
| `MagicalEye.masteryTickInterval` | 6 | Mastery tick interval while analyzing. |
| `MagicalEye.canTickMinAnalysisDistance` | 5 | Minimum analysis distance for canTick check. |
