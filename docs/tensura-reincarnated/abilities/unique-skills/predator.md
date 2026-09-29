# Predator

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Predator](../../../assets/icons/tensura/skill/predator.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:predator` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 50,000 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Press |

</div>

> Become the monster you were meant to be. Eat all. Analyze, craft and refine items, gain access to a spatial storage and mimic entities.

## Modes

| # | Mode |
|---|---|
| 1 | Predation |
| 2 | Analysis |
| 3 | Stomach |
| 4 | Mimicry |
| 5 | Isolation |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Isolation | 200 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Does something when first learned
- Does something when mastered

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are allowed to mimic.

## Related

- **Related skills:** [Starved](starved.md), [Gluttony](gluttony.md)
- **Referenced by:** [Gluttony](gluttony.md), [Starved](starved.md), [Mimicry](../../../tr-nightmares/abilities/extra-skills/mimicry.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Predator.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Predator.magiculeCostIsolation` | 200 | Magicule Cost to remove each harmful status effect with Isolation. |
| `Predator.predationRange` | 3 | The max range in block of the Predation Mode. |
| `Predator.predationDamage` | 10 | The attack damage of the Predation Mode. |
| `Predator.predationEPDrain` | 100 | The amount of EP that the user drains from target using the Predation Mode. |
| `Predator.predationSkillChance` | 10 | The chance to obtain skills from targets without killing them with the Predation Mode. |
| `Predator.predationSkillNumber` | 1 | The number of skills to gain from targets at a time without killing them with the Predation Mode. |
| `Predator.predationEPSteal` | 0.3 | The multiplier of the target's EP to be turned into the user's EP when killed with the Predation Mode. |
| `Predator.predationMagicCopy` | 0.5 | The chance multiplier for each of the target's learnable magic to be obtained by the user when killed with the Predation Mode. |
| `Predator.magiculeMultiplier` | 2 | The multiplier of magicule gained from dissolving items with the Isolation Mode. |
| `Predator.healthMultiplier` | 2 | The multiplier of health healed from dissolving items with the Isolation Mode.. |
| `Predator.isolationCooldown` | 5 | The cooldown in second of the Isolation Mode. |
| `Predator.isolationCooldownMastered` | 3 | The cooldown in second of the Isolation Mode when mastered. |
| `Predator.waterCapacity` | 3,000 | The bonus water capacity when the skill is acquired. |
| `Predator.lavaCapacity` | 3,000 | The bonus lava capacity when the skill is acquired. |

## In-game messages

<details markdown><summary>Show 5 messages</summary>

- Changed %s's Block Consuming to All.
- Changed %s's Block Consuming to Blocks.
- Changed %s's Block Consuming to Fluid.
- Changed %s's Block Consuming to None.
- Soul Gluttony Range: %s

</details>

## Tags

`tensura:skills/gluttony`, `tensura:skills/unique_skills`
