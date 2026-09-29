# Blood Domination

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Blood Domination](../../../assets/icons/ascension/skill/blood_domination.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `ascension:blood_domination` |
| **Activation** | Toggle |

</div>

> Toggle: +60% outgoing blood damage (+100% mastered). Evolved form of Blood Manipulation.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Triggers when you damage a target

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `blood_domination.bonusMastered` | 1 (0 to 10) | Outgoing blood-damage multiplier bonus while toggled, mastered. |
| `blood_domination.bonus` | 0.6 (0 to 10) | Outgoing blood-damage multiplier bonus while toggled, unmastered. |
| `blood_domination.enabled` | true | Enable Blood Domination. |
| `blood_manipulation.bonusMastered` | 0.4 (0 to 10) | Outgoing blood-damage multiplier bonus while toggled, mastered. |
| `blood_manipulation.bonus` | 0.2 (0 to 10) | Outgoing blood-damage multiplier bonus while toggled, unmastered (0.20 = +20%). |
| `blood_manipulation.enabled` | true | Enable Blood Manipulation. |

## Tags

`tensura:skills/extra_skills`
