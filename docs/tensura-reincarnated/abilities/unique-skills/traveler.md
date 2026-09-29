# Traveler

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Traveler](../../../assets/icons/tensura/skill/traveler.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:traveler` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 50,000 |
| **Cooldowns (s)** | 2 mastered, 5 otherwise, 4 mastered, 5 otherwise |
| **Activation** | Toggle, Press |

</div>

> Move freely through space, teleport large distances or create spatial gates. Manipulate stardust to immense damage.

## Modes

| # | Mode |
|---|---|
| 1 | Instant Motion |
| 2 | Teleport |
| 3 | Spatial Manipulation |
| 4 | Stardust Arrow |
| 5 | Stardust Rain |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Stardust Arrow | 150 | 150 |
| Stardust Rain | 5,000 | 5,000 |
| other modes | 0 | 0 |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Does something when first learned

## Obtaining

- Innate to mobs: [Mai Furuki](../../mobs/mai-furuki.md)
- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Referenced by:** [Pride Manas](../../../tr-nightmares/abilities/ultimate-skills/pride-manas.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Traveler.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Traveler.magiculeCostMotion` | 5 | Magicule Cost per block to use Instant Motion. |
| `Traveler.magiculeCostTeleport` | 5 | Magicule Cost per block to use Teleport per block. |
| `Traveler.magiculeCostPortal` | 25 | Magicule Cost per block to use Teleport per block using Portal. |
| `Traveler.magiculeCostArrow` | 150 | Magicule Cost to activate Stardust Arrow. |
| `Traveler.auraCostArrow` | 150 | Aura Cost to activate Stardust Arrow. |
| `Traveler.magiculeCostRain` | 5,000 | Magicule Cost to activate Stardust Rain. |
| `Traveler.auraCostRain` | 5,000 | Aura Cost to activate Stardust Rain. |
| `Traveler.manipulationBoost` | 2 | The Spatial Damage Boost when activated Manipulation. |
| `Traveler.warpShot` | 0.5 | The warp shot level when activated Spatial Manipulation's Warp Shot. |
| `Traveler.motionRange` | 200 | The max range in block of the Instant Motion mode. |
| `Traveler.motionCooldown` | 5 | The cooldown in second of the Instant Motion mode. |
| `Traveler.motionCooldownMastered` | 2 | The cooldown in second of the Instant Motion mode when mastered. |
| `Traveler.warpChargeTick` | 0 | The charge tick of the Teleport mode before warping any entity. |
| `Traveler.teleportCooldown` | 10 | The cooldown in second of the Teleport mode. |
| `Traveler.teleportCooldownMastered` | 5 | The cooldown in second of the Teleport mode when mastered. |
| `Traveler.arrowDamage` | 30 | The damage of an arrow when using Stardust Arrow. |
| `Traveler.rainRange` | 20 | The max range in block of Stardust Rain. |
| `Traveler.rainNumber` | 12 | The number of arrows in Stardust Rain. |
| `Traveler.rainDamage` | 30 | The damage of an arrow when using Stardust Rain. |
| `Traveler.rainCooldown` | 5 | The cooldown for Stardust Rain. |
| `Traveler.rainCooldownMastered` | 4 | The cooldown for Stardust Rain when mastered. |

## Tags

`tensura:skills/space_skills`, `tensura:skills/unique_skills`
