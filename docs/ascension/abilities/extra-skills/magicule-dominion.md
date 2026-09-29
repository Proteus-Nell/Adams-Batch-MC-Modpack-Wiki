# Magicule Dominion

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Magicule Dominion](../../../assets/icons/ascension/skill/magicule_dominion.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `ascension:magicule_dominion` |
| **Activation** | Toggle |

</div>

> Toggle: +25% magicule regen (+50% mastered). Auto-learned once Magicule Resonance is mastered.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `magicule_dominion.bonusMastered` | 0.5 (0 to 10) | Regen multiplier bonus while toggled, mastered. |
| `magicule_dominion.bonus` | 0.25 (0 to 10) | Regen multiplier bonus while toggled, unmastered. |
| `magicule_dominion.enabled` | true | Enable Magicule Dominion. |
| `magicule_attunement.bonusMastered` | 0.1 (0 to 10) | Regen multiplier bonus while toggled, mastered. |
| `magicule_attunement.bonus` | 0.05 (0 to 10) | Regen multiplier bonus while toggled, unmastered. |
| `magicule_attunement.enabled` | true | Enable Magicule Attunement. |

## Tags

`tensura:skills/extra_skills`
