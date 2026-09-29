# Intimidating Roar

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Intimidating Roar](../../../assets/icons/ascension/skill/intimidating_roar.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `ascension:intimidating_roar` |
| **Cooldowns (s)** | 20 |
| **Activation** | Press |

</div>

> Active: roar to inflict Fear and Weakness on all enemies within 8 blocks for 6s (10s mastered). 20s cooldown.

## How it works

- Activated by pressing the skill key

## Obtaining

- Can be learned by: [Monkey](../../races/monkey.md), [Monkey Warrior](../../races/monkey-warrior.md), [Monkey Martial Artist](../../races/monkey-martial-artist.md), [Monkey King](../../races/monkey-king.md), [Divine King](../../races/divine-king.md), [Sun Wukong](../../races/sun-wukong.md)

## Related

- **Effects:** [Fear](../../../tensura-reincarnated/effects/fear.md)

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `intimidating_roar.enabled` | true | Enable Intimidating Roar. |
| `intimidating_roar.durationSecondsMastered` | 10 (1 to 600) | Effect duration, mastered (seconds). |
| `intimidating_roar.durationSeconds` | 6 (1 to 600) | Effect duration, unmastered (seconds). |
| `intimidating_roar.radius` | 8 (0 to 64) | AoE radius in blocks. |
| `intimidating_roar.cooldownSeconds` | 20 (0 to 3,600) | Cooldown (seconds). |

## Tags

`tensura:skills/extra_skills`
