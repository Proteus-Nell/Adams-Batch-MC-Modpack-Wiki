# Ruler

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Ruler](../../../assets/icons/trnightmare/skill/ruler.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:ruler` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 100,000 |
| **Max mastery** | 1,000 |
| **Activation** | Press |

</div>

> Grants absolute control over all effects directed at the userharm becomes healing, weakness becomes strength, and reality bends to their will.

## Modes

| # | Mode |
|---|---|
| 1 | Curse Crystal |
| 2 | Thought Guidance |
| 3 | Thought Manipulation |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you die
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| attribute | multiplier | multiply total |

## Related

- **Related skills:** [Sentient Being](sentient-being.md)
- **Effects:** [Inspiration](../../../tensura-reincarnated/effects/inspiration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Ruler.mpAcquirement` | 100,000 |  |
| `Ruler.maxMastery` | 1,000 |  |
| `Ruler.maxCurseSeals` | 16 |  |

## In-game messages

<details markdown><summary>Show 8 messages</summary>

- Target a creature to place under your curse seal control.
- You need %s curse seals, but only %s are available.
- You have placed %s under your control with %s curse seals.
- You have released %s from your curse seal control.
- No subordinates are under your control to guide.
- Thought Guidance has cleansed your subordinates and granted Inspiration.
- Thought Manipulation: Meat Shield mode
- Thought Manipulation: Rampage mode

</details>
