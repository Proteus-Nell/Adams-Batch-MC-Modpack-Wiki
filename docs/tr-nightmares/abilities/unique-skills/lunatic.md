# Lunatic

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:lunatic` |
| **Modes** | 4 |
| **Max mastery** | 1,000 |
| **Cooldowns (s)** | 10 |
| **Activation** | Toggle, Press, Hold |

</div>

> A fractured Unique Skill that turns Insanity into strength, clarity, and contagious madness.

## Modes

| # | Mode |
|---|---|
| 1 | Hysterical Strength |
| 2 | Lucid Mind |
| 3 | Induce Delirium |
| 4 | Psychosis |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target

## Related

- **Related skills:** [Confusion](../../../tensura-reincarnated/abilities/aspectual-magic/confusion.md)
- **Effects:** [Insanity](../../../tensura-reincarnated/effects/insanity.md), [Strengthen](../../../tensura-reincarnated/effects/strengthen.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `lunatic.mpAcquirement` | 85,000 | MP cost to obtain Lunatic. |
| `lunatic.maxMastery` | 1,000 | Max mastery. |
| `lunatic.fracturedMindInsanityLevel` | 3 | Fractured Mind: Insanity level applied while toggled. |
| `lunatic.fracturedMindMasteredInsanityLevel` | 5 | Fractured Mind: Insanity level applied while toggled when mastered. |
| `lunatic.hystericalStrengthPerInsanity` | 1 | Hysterical Strength: Strengthened levels gained per Insanity level. |
| `lunatic.hystericalStrengthMasteredPerInsanity` | 2 | Hysterical Strength: Strengthened levels gained per Insanity level when mastered. |
| `lunatic.lucidMindHpPerInsanity` | 50 | Lucid Mind: HP restored per consumed Insanity level. |
| `lunatic.lucidMindShpPerInsanity` | 100 | Lucid Mind: SHP restored per consumed Insanity level. |
| `lunatic.lucidMindMasteredHpPerInsanity` | 100 | Lucid Mind: HP restored per consumed Insanity level when mastered. |
| `lunatic.lucidMindMasteredShpPerInsanity` | 200 | Lucid Mind: SHP restored per consumed Insanity level when mastered. |
| `lunatic.lucidMindCooldownSeconds` | 10 | Lucid Mind cooldown in seconds. |
| `lunatic.induceDeliriumChance` | 0.25 | Induce Delirium: chance to apply Delirium on hit while the user has Insanity. |
| `lunatic.induceDeliriumDurationTicks` | 600 | Induce Delirium: Delirium duration in ticks. |
| `lunatic.induceDeliriumAmplifier` | 0 | Induce Delirium: Delirium amplifier. |
| `lunatic.induceDeliriumMasteredAmplifier` | 1 | Induce Delirium: Delirium amplifier when mastered. |
| `lunatic.psychosisRange` | 12 | Psychosis: radius in blocks. |
| `lunatic.psychosisIntervalTicks` | 600 | Psychosis: ticks between Insanity pulses while held. |
| `lunatic.psychosisMaxInsanityLevel` | 5 | Psychosis: maximum Insanity level it can build targets to. |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- You consume %s Insanity and reclaim a fleeting moment of clarity.
- %s has been afflicted with Delirium.

</details>
