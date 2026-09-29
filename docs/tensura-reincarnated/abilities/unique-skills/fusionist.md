# Fusionist

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Fusionist](../../../assets/icons/tensura/skill/fusionist.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:fusionist` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 50,000 |
| **Activation** | Press |

</div>

> Turn the world into a weapon, absorb the environment to create powerful mines and grenades.

## Modes

| # | Mode |
|---|---|
| 1 | Disassemble |
| 2 | Fuse |
| 3 | Stone |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Fuse | 1,000 |  |
| Stone | 200 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Fusionist.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Fusionist.magiculeCostFuse` | 1,000 | Magicule Cost to activate Fuse mode. |
| `Fusionist.magiculeCostProjectile` | 200 | Magicule Cost to activate Projectile mode. |
| `Fusionist.range` | 5 | The minimum range in block of the skill. |
| `Fusionist.fuseMatterCost` | 5 | The amount of disassembled matter points needed to activate Fuse. |
| `Fusionist.fuseBlastDamage` | 300 | The blast damage of the landmine from Fuse. |
| `Fusionist.fuseBlastDamageMastered` | 500 | The blast damage of the landmine from Fuse. |
| `Fusionist.fuseBlastRadius` | 25 | The blast size of the landmine from Fuse. |
| `Fusionist.bonusBlastCost` | 10 | The amount of disassembled matter points needed to add charge more power on a landmine with mastery. |
| `Fusionist.bonusBlastDamage` | 50 | The blast damage to charge on a landmine with mastery. |
| `Fusionist.bonusBlastRadius` | 5 | The blast size to charge on a landmine with mastery. |
| `Fusionist.maxBlastRadius` | 50 | The max size the landmine can reach when charged. |
| `Fusionist.projectileMatterCost` | 1 | The amount of disassembled matter points needed to activate Projectile. |
| `Fusionist.projectileBlastRadius` | 6 | The blast radius of the Projectile shot. |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- Fusionist Matters: %s
- Out of matters to fuse.

</details>

## Tags

`tensura:skills/unique_skills`
