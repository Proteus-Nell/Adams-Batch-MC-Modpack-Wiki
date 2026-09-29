# Captivator

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:captivator` |
| **Modes** | 4 |
| **Cooldowns (s)** | 30, 40, 60 |
| **Activation** | Press, Hold |

</div>

> Your previous life, you were the brightest, shining star. Your ability to turn lies into truths… Perhaps it’s the other way around? Whatever it may be, your eyes shine brilliantly in response to being on the biggest stage.

## Modes

| # | Mode |
|---|---|
| 1 | Performance |
| 2 | Masquerade |
| 3 | Unveil |
| 4 | Star Power |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Performance | 250 |  |
| Masquerade | 300 |  |
| Unveil | 500 |  |
| Star Power | 1,000 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Related

- **Related skills:** [Spiritual Attack Nullification](../../../tensura-reincarnated/abilities/resistance-skills/spiritual-attack-nullification.md), [Spiritual Attack Resistance](../../../tensura-reincarnated/abilities/resistance-skills/spiritual-attack-resistance.md)
- **Effects:** [Strengthen](../../../tensura-reincarnated/effects/strengthen.md), [Paralysis](../../../tensura-reincarnated/effects/paralysis.md), [Marked for Death](../../effects/marked-for-death.md), [Dazzled](../../effects/dazzled.md), [Inspiration](../../../tensura-reincarnated/effects/inspiration.md), [Rampage](../../../tensura-reincarnated/effects/rampage.md), [Mind Control](../../../tensura-reincarnated/effects/mind-control.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Captivator.mpAcquirement` | 60,000 | Magicule Acquirement Cost. |
| `Captivator.mpPerformanceCost` | 250 | Magicule cost of Performance mode. |
| `Captivator.performanceCooldown` | 60 | The cooldown of the Performance mode in seconds. |
| `Captivator.performanceRange` | 20 | The range for the Performance mode in blocks. |
| `Captivator.mpMasqueradeCost` | 300 | Magicule cost of Masquerade mode. |
| `Captivator.masqueradeCooldown` | 30 | The cooldown of the Masquerade mode in seconds. |
| `Captivator.masqueradeRange` | 15 | The range for the Masquerade mode in blocks. |
| `Captivator.mpUnveilCost` | 500 | Magicule cost of Unveil mode. |
| `Captivator.unveilCooldown` | 30 | The cooldown of the Unveil mode in seconds. |
| `Captivator.unveilRange` | 15 | The range in blocks for Unveil |
| `Captivator.mpStarPowerCost` | 1,000 | Magicule cost of Star Power Mode. |
| `Captivator.starPowerCooldown` | 40 | The cooldown of the Star Power mode in seconds. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- Target %s is immune to the effects of this mode.

</details>

## Tags

`tensura:skills/unique_skills`
