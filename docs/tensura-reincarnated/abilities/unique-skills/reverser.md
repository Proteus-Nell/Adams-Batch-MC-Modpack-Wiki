# Reverser

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Reverser](../../../assets/icons/tensura/skill/reverser.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:reverser` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 30,000 |
| **Activation** | Toggle, Press |

</div>

> Flip the rules. Change alignments, invert buffs and debuffs while shifting strengths and weaknesses to your benefit.

## Modes

| # | Mode |
|---|---|
| 1 | Alignment Reverse |
| 2 | Inverted Fusion [Buff] |
| 3 | Inverted Fusion [Debuff] |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Triggers when an effect is applied to you

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Related skills:** [Burden](../aspectual-magic/burden.md)
- **Effects:** [Magicule Poison](../../effects/magicule-poison.md), [Paralysis](../../effects/paralysis.md), [Corrosion](../../effects/corrosion.md), [Fatal Poison](../../effects/fatal-poison.md), [Fragility](../../effects/fragility.md), [Hypnosis](../../effects/hypnosis.md), [Illusion Boost](../../effects/illusion-boost.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Reverser.mpAcquirement` | 30,000 | Magicule Acquirement Cost. |
| `Reverser.magiculeCostCurse` | 10,000 | Magicule Cost to reverse each Curses on the equipped items when mastered. |

## Tags

`tensura:skills/unique_skills`
