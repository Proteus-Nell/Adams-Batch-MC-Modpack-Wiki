# Gravity Flux

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `mysticism:gravity_flux` |
| **Modes** | 2 |
| **Activation** | Press |

</div>

> Utilise the power of gravity to disrupt the target's movement and hamper their ability to move.

## Modes

| # | Mode |
|---|---|
| 1 | Fluctuate |
| 2 | Hamper |

## How it works

- Activated by pressing the skill key

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/scorpion_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Burden](../../../tensura-reincarnated/abilities/aspectual-magic/burden.md)
- **Effects:** [Gravity Fluctuation](../../effects/gravity-fluctuation.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/extra_config.toml`](../../configs/config-mysticism-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `GravityFlux.range` | 15 | The targeting range of the skill. |
| `GravityFlux.rangeMastered` | 20 | The targeting range of the skill when mastered. |
| `GravityFlux.gravityDuration` | 200 | The duration of the gravity fluctuation effect from the Fluctuate mode in ticks. (Multiply seconds by 20.) |
| `GravityFlux.gravityDurationMastered` | 200 | The duration of the gravity fluctuation effect from the Fluctuate mode when mastered, in ticks. (Multiply seconds by 20.) |
| `GravityFlux.gravityLevel` | 1 | The level of the gravity fluctuation effect from the Fluctuate mode. |
| `GravityFlux.gravityLevelMastered` | 2 | The level of the gravity fluctuation effect from the Fluctuate mode when the skill is mastered. |
| `GravityFlux.nauseaDuration` | 200 | The duration of the nausea effect from the Fluctuate mode in ticks. (Multiply seconds by 20.) |
| `GravityFlux.nauseaDurationMastered` | 200 | The duration of the nausea effect from the Fluctuate mode when mastered, in ticks. (Multiply seconds by 20.) |
| `GravityFlux.nauseaLevel` | 1 | The level of the nausea effect from the Fluctuate mode. |
| `GravityFlux.nauseaLevelMastered` | 2 | The level of the nausea effect from the Fluctuate mode when the skill is mastered. |
| `GravityFlux.burdenDuration` | 200 | The duration of the burden effect from the Hamper mode in ticks. (Multiply seconds by 20.) |
| `GravityFlux.burdenDurationMastered` | 200 | The duration of the burden effect from the Hamper mode when mastered, in ticks. (Multiply seconds by 20.) |
| `GravityFlux.burdenLevel` | 1 | The level of the burden effect from the Hamper mode. |
| `GravityFlux.burdenLevelMastered` | 2 | The level of the burden effect from the Hamper mode when the skill is mastered. |

## Tags

`tensura:skills/extra_skills`
