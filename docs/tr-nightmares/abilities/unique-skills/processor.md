# Processor

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Processor](../../../assets/icons/trnightmare/skill/processor.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:processor` |
| **Modes** | 2 |
| **Activation** | Toggle, Press |

</div>

> Layer multiple tasks together for either greater power or True Parallel Processing, Burn yourself out to go even farther.

## Modes

| # | Mode |
|---|---|
| 1 | Allocate Threads |
| 2 | Overclock |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (magicule cost allocate)* |  |
| Always | *set by config (magicule cost clock)* |  |
| Always | 50 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| chantSpeed | cast buff × threads allocated × perc multiplier | add |
| invulnerability | i frame buff × threads allocated × perc multiplier | add |

## Related

- **Related skills:** [Heat Nullification](../../../tensura-reincarnated/abilities/resistance-skills/heat-nullification.md), [Heat Resistance](../../../tensura-reincarnated/abilities/resistance-skills/heat-resistance.md)
- **Effects:** [Overclock](../../effects/overclock.md)
- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Processor.mpAcquirement` | 40,000 | Magicule Acquirement Cost. |
| `Processor.magiculeCostAllocate` | 1,000 | Magicule Cost to activate Allocate. |
| `Processor.magiculeCostClock` | 15,000 | Magicule Cost to activate Overclock. |
| `Processor.defaultThreads` | 2 | Base number of Threads |
| `Processor.masteryThreads` | 3 | Number of Threads on Mastery. |
| `Processor.allocateCooldown` | 10 | Cooldown for activating Allocate. |
| `Processor.clockBuffTime` | 40 | How long overclock buffs user at base. |
| `Processor.clockBuffPerc` | 30 | The base percentage of the overclock buff. |
| `Processor.clockCooldown` | 300 | How long the skill is disabled after using overclock in seconds. |
| `Processor.iFrameBuff` | 1 | How many frames of invulnerability dodging is buffed by per thread. |
| `Processor.castBuff` | 2 | CastingTime buff per thread. |

## Tags

`tensura:skills/neutral`
