# Repeater

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Repeater](../../../assets/icons/mysticism/skill/repeater.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:repeater` |
| **Modes** | 2 |
| **Cooldowns (s)** | 15 mastered, 30 otherwise |
| **Activation** | Press |

</div>

> Through the lens, you trap light. You do something special, and you feel like you’ve already done it in millions of realities. Like the things you’ve done and led up to this moment were predestined. Maybe you can change that.

## Modes

| # | Mode |
|---|---|
| 1 | Recursion Depth |
| 2 | Flarefrost Storehouse |

## How it works

- Activated by pressing the skill key
- Triggers when you damage a target

## Obtaining

- Innate to mobs: [Memoires](../../mobs/memoires.md)

## Related

- **Items:** [Axiom](../../items/weapons/axiom.md), [Waltz](../../items/weapons/waltz.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Repeater.mpAcquirement` | 75,000 | Magicule Acquirement Cost |
| `Repeater.recursionDepthTimer` | 100 | How long should Recursion Depth last, in ticks (seconds x 20). |
| `Repeater.recursionDepthCooldown` | 30 | The cooldown of the Recursion Depth mode. |
| `Repeater.recursionDepthCooldownMastered` | 15 | The cooldown of the Recursion Depth mode when the skill is mastered. |

## Tags

`tensura:skills/unique_skills`
