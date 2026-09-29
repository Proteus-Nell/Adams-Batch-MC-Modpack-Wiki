# Magicule Resonance

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Magicule Resonance](../../../assets/icons/ascension/skill/magicule_resonance.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `ascension:magicule_resonance` |
| **Activation** | Toggle |

</div>

> Toggle: +10% magicule regen (+20% mastered). Auto-learned once Magicule Attunement is mastered.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `magicule_resonance.bonusMastered` | 0.2 (0 to 10) | Regen multiplier bonus while toggled, mastered. |
| `magicule_resonance.bonus` | 0.1 (0 to 10) | Regen multiplier bonus while toggled, unmastered. |
| `magicule_resonance.enabled` | true | Enable Magicule Resonance. |
| `magicule_attunement.bonusMastered` | 0.1 (0 to 10) | Regen multiplier bonus while toggled, mastered. |
| `magicule_attunement.bonus` | 0.05 (0 to 10) | Regen multiplier bonus while toggled, unmastered. |
| `magicule_attunement.enabled` | true | Enable Magicule Attunement. |

## Tags

`tensura:skills/extra_skills`
