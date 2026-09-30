# Coalescence

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Coalescence](../../../assets/icons/mysticism/skill/coalescence.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:coalescence` |
| **Modes** | 3 |
| **Cooldowns (s)** | 5, 15 mastered, 30 otherwise, 90 mastered, 180 otherwise |
| **Activation** | Toggle, Press |

</div>

> Freeze, stop and stagnate. Prevent hindering effects from applying to you and cause others to halt and solidify.

## Modes

| # | Mode |
|---|---|
| 1 | Fixation |
| 2 | Solidification |
| 3 | Eternal Domain |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Fixation | 1,000 |  |
| Solidification | 1,000 |  |
| Eternal Domain | 10,000 |  |
| other modes | 500 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Triggers when an effect is applied to you

## Related

- **Related skills:** [Burden](../../../tensura-reincarnated/abilities/aspectual-magic/burden.md)
- **Effects:** [Fixation](../../effects/fixation.md)
- **Summons / entities:** Solidification Shield, Eternal Domain

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Coalescence.mpAcquirement` | 90,000 | Magicule Acquirement Cost. |
| `Coalescence.fixationCost` | 1,000 | The magicule cost of the Fixation mode. |
| `Coalescence.fixationRange` | 10 | The range of the Fixation mode in blocks. |
| `Coalescence.fixationRangeMastery` | 15 | The range of the Fixation mode in blocks when the skill is mastered. |
| `Coalescence.fixationDuration` | 200 | The duration of the Fixation effect in ticks (seconds x 20). |
| `Coalescence.fixationDurationMastered` | 400 | The duration of the Fixation effect in ticks (seconds x 20). |
| `Coalescence.fixationCooldown` | 30 | The cooldown of the Fixation mode in seconds. |
| `Coalescence.fixationCooldownMastered` | 15 | The cooldown of the Fixation mode in seconds when the skill is mastered. |
| `Coalescence.fixationMissCooldown` | 5 | The cooldown of the Fixation mode when the user misses. |
| `Coalescence.fixationMissCooldownMastered` | 5 | The cooldown of the Fixation mode when the user misses and the skill is mastered. |
| `Coalescence.solidificationCost` | 1,000 | The magicule cost of the Solidification mode. |
| `Coalescence.solidificationCooldown` | 20 | The cooldown of the solidification mode in seconds. |
| `Coalescence.solidificationCooldownMastered` | 10 | The cooldown of the solidification mode in seconds when the skill is mastered. |
| `Coalescence.solidificationShieldDuration` | 400 | The cooldown of the solidification shield in ticks. |
| `Coalescence.solidificationShieldDurationMastered` | 800 | The cooldown of the solidification shield in ticks when the skill is mastered. |
| `Coalescence.eternalDomainCost` | 10,000 | The magiule cost of the Eternal Domain art. |
| `Coalescence.eternalDomainRange` | 8 | The radius of Eternal Domain in blocks. |
| `Coalescence.eternalDomainRangeMastered` | 16 | The radius of Eternal Domain in blocks when the skill is mastered. |
| `Coalescence.eternalDomainLife` | 400 | How long in ticks (seconds x 20) the Eternal Domain should last. |
| `Coalescence.eternalDomainLifeMastered` | 800 | How long in ticks (seconds x 20) the Eternal Domain should last when the skill is mastered. |
| `Coalescence.eternalDomainCooldown` | 180 | The cooldown of the Eternal Domain art in seconds. |
| `Coalescence.eternalDomainCooldownMastered` | 90 | The cooldown of the Eternal Domain art in seconds when the skill is mastered. |

## Tags

`tensura:skills/unique_skills`, `tensura:skills/virtue_skills`
