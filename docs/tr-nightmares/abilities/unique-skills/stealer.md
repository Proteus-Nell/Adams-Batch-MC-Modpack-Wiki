# Stealer

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Stealer](../../../assets/icons/tensura/skill/usurper.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:stealer` |
| **Acquisition cost (MP)** | 95,000 |
| **Max mastery** | 1,000 |
| **Activation** | Press |

</div>

> Steal energy from your foes on hit and plunder compatible skills from targets, copying them when direct theft is disallowed.

## How it works

- Activated by pressing the skill key
- Triggers when you damage a target
- Triggers when you die

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Stealer.mpAcquirement` | 95,000 |  |
| `Stealer.maxMastery` | 1,000 |  |
| `Stealer.energyTheftChance` | 0.1 |  |
| `Stealer.energyTheftFraction` | 0.005 |  |
| `Stealer.plunderCooldownTicks` | 300 |  |
| `Stealer.plunderMaxSkills` | 10 |  |

## In-game messages

<details markdown><summary>Show 7 messages</summary>

- Target a creature to plunder.
- No compatible skills could be plundered from the target.
- You stole %s from %s.
- You copied %s from %s.
- You bulk-stole %s from %s.
- You bulk-copied %s from %s.
- Plunder is on cooldown.

</details>
