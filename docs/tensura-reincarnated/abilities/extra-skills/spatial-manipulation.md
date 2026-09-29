# Spatial Manipulation

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Spatial Manipulation](../../../assets/icons/tensura/skill/spatial_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:spatial_manipulation` |
| **Activation** | Toggle, Press |

</div>

> Boosts Space abilities by a decent amount and manipulate space to empower your ranged attacks.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Does something when mastered

## Obtaining

- Can be learned by: [Ender Dragonewt](../../../ascension/races/ender-dragonewt.md), [Void Dragonewt](../../../ascension/races/void-dragonewt.md), [Abyssal Dragonewt](../../../ascension/races/abyssal-dragonewt.md), [Chaos Dragon](../../../ascension/races/chaos-dragon.md), [Lich](../../../ascension/races/lich.md), [Lich King](../../../ascension/races/lich-king.md)
- Innate to mobs: [Akash](../../mobs/akash.md), [Winged Cat](../../mobs/winged-cat.md)
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill IDs granted by Elfaria. Includes Albis so old Ars Weiss clones stay compatible, magic basics, transforms, senses, chant annulment,...
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/direwolf_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/special_direwolf_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/centipede_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Spatial Domination](spatial-domination.md)
- **Summons / entities:** Tensura
- **Referenced by:** [Spatial Domination](spatial-domination.md), [Spatial Motion](spatial-motion.md), [Elegy](../../../tr-nightmares/abilities/unique-skills/elegy.md), [｢ Uriel, Lord of Oaths ｣](../../../tr-nightmares/abilities/ultimate-skills/uriel-lord-of-oath.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `SpatialManipulation.magiculeCostWarpShot` | 50 | Magicule Cost to activate Warp Shot. |
| `SpatialManipulation.spaceSkillAcquirement` | 3 | The number of mastered space skills needed to learn Space Manipulation. |
| `SpatialManipulation.dominationEpAcquirement` | 400,000 | EP Requirement for to learn Domination. |
| `SpatialManipulation.resistDegradationAcquirement` | 800,000 | EP Requirement for to use Resist Degradation when mastered. |
| `SpatialManipulation.manipulationBoost` | 1.5 | The Spatial Damage Boost when activated Manipulation. |
| `SpatialManipulation.dominationBoost` | 3 | The Spatial Damage Boost when activated Domination. |
| `SpatialManipulation.magiculeCostWarpShot` | 50 | Magicule Cost to activate Warp Shot. |
| `SpatialManipulation.magiculeCostCleanse` | 100 | Magicule Cost to activate Spatial Cleanse per Severance value. |
| `SpatialManipulation.magiculeCostRay` | 5,000 | Magicule Cost to activate Dimension Ray. |
| `SpatialManipulation.magiculeCostStorm` | 50,000 | Magicule Cost to activate Dimension Storm. |
| `SpatialManipulation.magiculeCostField` | 2,000 | Magicule Cost to activate Fault Field. |
| `SpatialManipulation.magiculeCostFieldDamage` | 50 | Magicule Cost to block damage with Fault Field per damage point. |
| `SpatialManipulation.warpShotManipulation` | 0.5 | The warp shot level when activated Spatial Manipulation's Warp Shot. |
| `SpatialManipulation.warpShotDomination` | 0.5 | The warp shot level when activated Spatial Domination's Warp Shot (stackable with Spatial Manipulation). |
| `SpatialManipulation.warpShotDistance` | 50 | The maximum distance in block that warp shot can work with. |
| `SpatialManipulation.cleanseCooldown` | 2 | The cooldown for Spatial Cleanse. |
| `SpatialManipulation.rayRange` | 30 | The range in block of the Dimension Ray. |
| `SpatialManipulation.rayDamage` | 50 | The damage of the Dimension Ray. |
| `SpatialManipulation.rayDamageMastered` | 200 | The damage of the Dimension Ray when mastered. |
| `SpatialManipulation.rayDuration` | 60 | The maximum activate time at once for Dimension Ray. |
| `SpatialManipulation.rayCooldown` | 10 | The cooldown for Dimension Ray. |
| `SpatialManipulation.rayCooldownMastered` | 7 | The cooldown for Dimension Ray when mastered. |
| `SpatialManipulation.stormRange` | 30 | The activation range of the Dimension Storm. |
| `SpatialManipulation.stormDamage` | 50 | The damage of each of Dimension Ray in a Dimension Storm. |
| `SpatialManipulation.stormDamageMastered` | 100 | The damage of each of Dimension Ray in a Dimension Storm when mastered. |
| `SpatialManipulation.stormAmount` | 20 | The number of Rays in a Dimension Storm. |
| `SpatialManipulation.stormAmountMastered` | 30 | The number of Rays in a Dimension Storm when mastered. |
| `SpatialManipulation.stormCooldown` | 20 | The cooldown for Dimension Storm. |
| `SpatialManipulation.stormCooldownMastered` | 10 | The cooldown for Dimension Storm when mastered. |
| `SpatialManipulation.faultFieldSpeed` | 0.5 | The speed multiplier when using Fault Field or Dimension Ray. |

## Tags

`tensura:skills/elemental_manipulation`, `tensura:skills/extra_skills`, `tensura:skills/space_skills`
