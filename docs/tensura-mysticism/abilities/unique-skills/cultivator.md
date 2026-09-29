# Cultivator

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Cultivator](../../../assets/icons/mysticism/skill/cultivator.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:cultivator` |
| **Modes** | 1 |
| **Cooldowns (s)** | 3,600 |
| **Activation** | Toggle, Press |

</div>

> Embody the relentless pursuit of ascension, gathering and refining energy to reach unparalleled heights. A Cultivator walks the path of self-perfection and dominion over all.

## Modes

| # | Mode |
|---|---|
| 1 | Breakthrough |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Triggers when you damage a target
- Triggers when you die
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| magicule | bonus magicule | add |

## Related

- **Effects:** [Cultivating](../../effects/cultivating.md)
- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Cultivator.mpAcquirement` | 80,000 | Magicule Acquirement Cost. |
| `Cultivator.attackBoost` | 50 | The physical attack damage boost when in Slot. |
| `Cultivator.attackBoostMastered` | 100 | The physical attack damage boost when in Slot with mastery. |
| `Cultivator.mobKillsNeeded` | 1,000 | The ammount of mob kills needed to start Cultivation. |
| `Cultivator.breakthroughCooldown` | 3,600 | The cooldown on Breakthrough when it completes. |
| `Cultivator.cultivationTimer` | 6,000 | How long cultivation lasts in ticks (seconds x 20). |
| `Cultivator.breakthroughMasteryGain` | 100 | The amount of mastery the user gains when successfully breaking through. |
| `Cultivator.magiculePercentage` | 10 | The bonus Magicule percentage the user gains. |
| `Cultivator.magiculePercentageMastered` | 15 | The bonus Magicule percentage the user gains with Mastery. |
| `Cultivator.cultivationMPMultiplier` | 3 | The multiplicative magicule gain the user receives while in the middle of Breaking Through. |

## Tags

`tensura:skills/unique_skills`
