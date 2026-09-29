# Oppressor

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Oppressor](../../../assets/icons/tensura/skill/oppressor.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:oppressor` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 50,000 |
| **Cooldowns (s)** | 5 mastered, 10 otherwise |
| **Activation** | Press, Hold |

</div>

> Dominate gravity yourself, control attractive and repulsive forces or unleash devastating ranged attacks which will crush anyone unfortunate enough to be in your path.

## Modes

| # | Mode |
|---|---|
| 1 | Repel |
| 2 | Attract |
| 3 | Oppress |
| 4 | Bleve |
| 5 | Flicker |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Repel | 50 |  |
| Attract | 50 |  |
| Oppress | 350 |  |
| Bleve | 1,000 |  |
| Flicker | 50 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you are attacked
- Triggers when you respawn
- Does something when first learned
- Uses number keys for extra actions

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Related skills:** [Gravity Manipulation](../extra-skills/gravity-manipulation.md), [Burden](../aspectual-magic/burden.md)
- **Effects:** [Oppression](../../effects/oppression.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Oppressor.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Oppressor.magiculeCostRepel` | 50 | Magicule Cost to activate Repel. |
| `Oppressor.magiculeCostAttract` | 50 | Magicule Cost to activate Attract. |
| `Oppressor.magiculeCostOppress` | 350 | Magicule Cost to activate Oppress. |
| `Oppressor.magiculeCostBleve` | 1,000 | Magicule Cost to activate Bleve. |
| `Oppressor.magiculeCostFlicker` | 50 | Magicule Cost to activate Flicker. |
| `Oppressor.repelRange` | 10 | The max range in block of the Repel mode. |
| `Oppressor.attractRange` | 30 | The max range in block of the Attract mode. |
| `Oppressor.maxScale` | 10 | The max power scale of the Repel/Attract/Flicker mode. |
| `Oppressor.oppressRange` | 20 | The max range in block of the Oppress mode. |
| `Oppressor.oppressBurden` | 2 | The level of the Burden effect from the Oppress mode. |
| `Oppressor.oppressDuration` | 600 | The duration in tick of the Oppression effect from the Oppress mode. |
| `Oppressor.oppressDamage` | 100 | The oppress damage of the Oppress mode. |
| `Oppressor.oppressDamageMastered` | 200 | The oppress damage of the Oppress mode with mastery. |
| `Oppressor.oppressCooldown` | 10 | The cooldown in second of the Oppress mode. |
| `Oppressor.oppressCooldownMastered` | 5 | The cooldown in second of the Oppress mode with mastery. |
| `Oppressor.bleveRange` | 20 | The max range in block of the Bleve mode. |
| `Oppressor.bleveDamage` | 100 | The bleve damage of the Bleve mode. |
| `Oppressor.bleveDamageMastery` | 200 | The bleve damage of the Bleve mode with mastery. |
| `Oppressor.bleveCooldown` | 10 | The cooldown in second of the Bleve mode. |
| `Oppressor.bleveCooldownMastered` | 5 | The cooldown in second of the Bleve mode with mastery. |

## Tags

`tensura:skills/gravity_skills`, `tensura:skills/unique_skills`
