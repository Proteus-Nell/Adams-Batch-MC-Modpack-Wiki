# Magicule Attunement

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Magicule Attunement](../../../assets/icons/ascension/skill/magicule_attunement.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `ascension:magicule_attunement` |
| **Activation** | Toggle |

</div>

> Toggle: +5% magicule regen (+10% mastered). Masters slowly while toggled on. Auto-learned once Energy Charge is mastered and Haki is acquired.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `magicule_attunement.bonusMastered` | 0.1 (0 to 10) | Regen multiplier bonus while toggled, mastered. |
| `magicule_attunement.bonus` | 0.05 (0 to 10) | Regen multiplier bonus while toggled, unmastered. |
| `magicule_attunement.enabled` | true | Enable Magicule Attunement. |

## Tags

`tensura:skills/extra_skills`
