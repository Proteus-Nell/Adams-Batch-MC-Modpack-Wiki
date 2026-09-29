# Suppressor

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Suppressor](../../../assets/icons/tensura/skill/suppressor.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:suppressor` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 30,000 |
| **Cooldowns (s)** | 2 mastered, 5 otherwise |
| **Activation** | Toggle, Press |

</div>

> Restrict teleportation, confuse enemies by swapping places, and use your blink as well as the spatial gate to cross large distances.

## Modes

| # | Mode |
|---|---|
| 1 | Spatial Suppression |
| 2 | Swap |
| 3 | Spatial Motion |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Spatial Suppression | 300 |  |
| Swap | 100 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Effects:** [Spatial Blockade](../../effects/spatial-blockade.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Suppressor.mpAcquirement` | 30,000 | Magicule Acquirement Cost. |
| `Suppressor.magiculeCostSwap` | 100 | Magicule Cost to activate Swap. |
| `Suppressor.magiculeCostBlockade` | 300 | Magicule Cost to activate Spatial Blockade. |
| `Suppressor.magiculeCostMotion` | 10 | Magicule Cost per block to use Spatial Motion. |
| `Suppressor.magiculeCostPortal` | 50 | Magicule Cost per block to use Spatial Motion per block using Portal. |
| `Suppressor.chantSpeed` | 2 | The chant speed multiplier when toggled. |
| `Suppressor.blockadeDuration` | 1,200 | The duration in tick of the Spatial Blockade when activated. |
| `Suppressor.swapRange` | 30 | The max range in block of the Swap mode. |
| `Suppressor.motionRange` | 30 | The max range in block of the Spatial Motion mode. |
| `Suppressor.motionRangeMastered` | 50 | The max range in block of the Spatial Motion mode when mastered. |
| `Suppressor.warpChargeTick` | 0 | The charge tick of the Teleport mode before warping any entity. |
| `Suppressor.motionCooldown` | 5 | The cooldown in second of the Spatial Motion mode. |
| `Suppressor.motionCooldownMastered` | 2 | The cooldown in second of the Spatial Motion mode when mastered. |

## Tags

`tensura:skills/space_skills`, `tensura:skills/unique_skills`
