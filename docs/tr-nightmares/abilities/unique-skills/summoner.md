# Summoner

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:summoner` |
| **Acquisition cost (MP)** | 90,000 |
| **Max mastery** | 1,000 |
| **Activation** | Press, Hold |

</div>

> Build a summon roster, command your chosen targets, and banish them back to their origin.

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Does something when first learned

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Summoner.mpAcquirement` | 90,000 |  |
| `Summoner.maxMastery` | 1,000 |  |
| `Summoner.maxSummonEntries` | 12 |  |
| `Summoner.summonRange` | 16 |  |

## In-game messages

<details markdown><summary>Show 9 messages</summary>

- Summon
- Summon Menu
- Look at a target to add it to your summon roster.
- %s is already in your summon roster.
- Added %s to your summon roster.
- You summoned %s.
- You banished %s back to their origin.
- No summon targets are currently registered.
- The selected target is no longer available.

</details>
