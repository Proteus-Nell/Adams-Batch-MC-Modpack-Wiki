# Chef

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Chef](../../../assets/icons/tensura/skill/chef.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:chef` |
| **Acquisition cost (MP)** | 10,000 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Press |

</div>

> Purify and renew. Remove all negative effects and restore vitality to those under your care.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Chef.mpAcquirement` | 10,000 | Magicule Acquirement Cost. |
| `Chef.magiculeCostEffect` | 100 | Magicule Cost to remove each harmful status effect. |
| `Chef.magiculeCostHP` | 60 | Magicule Cost to heal each HP. |
| `Chef.magiculeCostHPMastered` | 40 | Magicule Cost to heal each HP when mastered. |
| `Chef.cooldown` | 5 | The cooldown in second when activated. |
| `Chef.cooldownMastered` | 3 | The cooldown in second when activated with mastery. |

## Tags

`tensura:skills/unique_skills`
