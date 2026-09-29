# Provider

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Provider](../../../assets/icons/mysticism/skill/provider.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:provider` |
| **Modes** | 2 |
| **Cooldowns (s)** | 5 |
| **Activation** | Press |

</div>

> The more you give away, the more you feel closer to yourself. Perhaps it even strengthens you along the way.

## Modes

| # | Mode |
|---|---|
| 1 | Generosity |
| 2 | Pay It Forward |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Generosity | 1,000 |  |
| Pay It Forward | 750 |  |
| other modes | 500 |  |

## How it works

- Activated by pressing the skill key
- Triggers when you damage a target

## Related

- **Effects:** [Pay it Forward](../../effects/pay-it-forward.md)
- **Summons / entities:** Provider Halo

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Provider.mpAcquirement` | 85,000 | Magicule Acquirement Cost. |
| `Provider.generosityHaloCost` | 1,000 | The initial magicule cost of Provider's Generosity Halo when it is summoned. |
| `Provider.generosityHaloCostSecond` | 500 | The magicule cost of Provider's Generosity Halo every subsequent second it is summoned. |
| `Provider.generosityHaloLifespan` | 72,000 | The lifespan of the Generosity Halo entity in ticks. |
| `Provider.generosityBoost` | 3 | The damage multiplier that all projectiles receive when passing through Provider's Generosity Halo. |
| `Provider.generosityEntityDamageBoost` | 3 | The damage multiplier that all entities receive when gaining the Provider Boost effect from passing through Provider's Generosity Halo. |
| `Provider.generosityEntitySpeedBoost` | 3 | The speed multiplier that all entities receive when gaining the Provider Boost effect from passing through Provider's Generosity Halo. |
| `Provider.generosityEntityStepHeightBoost` | 3 | The step height that all entities receive when gaining the Provider Boost effect from passing through Provider's Generosity Halo. |
| `Provider.generosityCooldown` | 5 | The cooldown for the Generosity mode in seconds. |
| `Provider.generosityCooldownMastery` | 5 | The cooldown for the Generosity mode in seconds when the skill is mastered.. |
| `Provider.payItForwardCooldown` | 300 | The cooldown of the Pay It Forward mode in seconds. |
| `Provider.payItForwardCooldownMastered` | 300 | The cooldown of the Pay It Forward mode in seconds when the skill is mastered. |
| `Provider.payItForwardCost` | 1,500 | The magicule cost to turn on Provider's Pay It Forward mode. |
| `Provider.payItForwardCostTicking` | 750 | The magicule cost of Provider's Pay It Forward mode every subsequent second it is toggled. |
| `Provider.contributionsTier1` | 1,000 | The following values are the contributions required to reach the next tier. |
| `Provider.contributionsTier2` | 2,500 |  |
| `Provider.contributionsTier3` | 5,000 |  |
| `Provider.contributionsTier4` | 25,000 |  |
| `Provider.contributionsTier5` | 100,000 |  |

## Tags

`tensura:skills/unique_skills`, `tensura:skills/virtue_skills`
