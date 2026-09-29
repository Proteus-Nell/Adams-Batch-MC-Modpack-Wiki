# Magnetized Vacuum

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

![Magnetized Vacuum](../../../assets/icons/ascension/skill/magnetized_vacuum.png)

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `ascension:magnetized_vacuum` |
| **Cooldowns (s)** | 10 mastered, 20 otherwise |
| **Activation** | Press |

</div>

> Active: pull nearby items and XP orbs to you within 8 blocks for 5s (12 blocks / 10s mastered). Costs 2000 magicule (1000 mastered). 20s cooldown (10s mastered). Obtained by using a plunderer skill on an Iron Golem.

## How it works

- Activated by pressing the skill key

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `magnetized_vacuum.enabled` | true | Enable Magnetized Vacuum (also skips the Iron Golem skill grant when false). |
| `magnetized_vacuum.costMastered` | 1,000 (0 to 1,000,000,000) | Flat magicule cost per activation, mastered. |
| `magnetized_vacuum.cost` | 2,000 (0 to 1,000,000,000) | Flat magicule cost per activation, unmastered. |
| `magnetized_vacuum.durationSecondsMastered` | 10 (1 to 600) | Aura duration, mastered (seconds). |
| `magnetized_vacuum.durationSeconds` | 5 (1 to 600) | Aura duration, unmastered (seconds). |
| `magnetized_vacuum.cooldownSecondsMastered` | 10 (0 to 3,600) | Cooldown, mastered (seconds). |
| `magnetized_vacuum.cooldownSeconds` | 20 (0 to 3,600) | Cooldown, unmastered (seconds). |
| `magnetized_vacuum.radiusMastered` | 12 (0 to 64) | Pull radius in blocks, mastered. |
| `magnetized_vacuum.radius` | 8 (0 to 64) | Pull radius in blocks, unmastered. |

## Tags

`tensura:skills/common_skills`
