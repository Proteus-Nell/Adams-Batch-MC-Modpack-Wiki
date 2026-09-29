# Blood Manipulation

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Blood Manipulation](../../../assets/icons/ascension/skill/blood_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `ascension:blood_manipulation` |
| **Activation** | Toggle |

</div>

> Toggle: +20% outgoing blood damage (+40% mastered). Masters slowly while toggled on.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Triggers when you damage a target

## Obtaining

- Can be learned by: [Blood Noble](../../races/blood-noble.md), [Elder Bloodfiend](../../races/elder-bloodfiend.md), [Progenitor Bloodfiend](../../races/progenitor-bloodfiend.md)

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `blood_manipulation.bonusMastered` | 0.4 (0 to 10) | Outgoing blood-damage multiplier bonus while toggled, mastered. |
| `blood_manipulation.bonus` | 0.2 (0 to 10) | Outgoing blood-damage multiplier bonus while toggled, unmastered (0.20 = +20%). |
| `blood_manipulation.enabled` | true | Enable Blood Manipulation. |

## Tags

`tensura:skills/extra_skills`
