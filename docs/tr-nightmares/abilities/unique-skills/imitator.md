# Imitator

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:imitator` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 75,000 |
| **Activation** | Press |

</div>

> Learn others through observation, then wear their face, stats, and skills. Imprint your disguise onto loyal clones as sentient stage crew.

## Modes

| # | Mode |
|---|---|
| 1 | Actor |
| 2 | Stage Crew |

## How it works

- Activated by pressing the skill key

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `imitator.mpAcquirement` | 75,000 | Magicule obtainment cost. |
| `imitator.learnRequired` | 100 | Learn progress required before disguise is available. |
| `imitator.epGateRatio` | 0.5 | Maximum target EP ratio allowed for player disguises (target EP must be &lt;= user EP \* ratio). |
| `imitator.mimicryEpMaxDifference` | 0.3 | When learning via Mimicry pulses, block learning if the target's EP is greater than the user's EP by this fraction (e.g., 0.3 = 30% higher -&gt; block). |
| `imitator.mimicryAllowUniqueAndUltimate` | false | Allow Mimicry learning pulses to include Unique and Ultimate skills when true. Default false for balance. |
