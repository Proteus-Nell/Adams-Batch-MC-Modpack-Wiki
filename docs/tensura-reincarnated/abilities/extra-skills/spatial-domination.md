# Spatial Domination

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Spatial Domination](../../../assets/icons/tensura/skill/spatial_domination.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:spatial_domination` |
| **Modes** | 5 |
| **Cooldowns (s)** | 2, 10 mastered, 20 otherwise, 10 mastered, 7 otherwise |
| **Activation** | Toggle, Press, Hold |

</div>

> Boosts Space abilities by a large amount and deals massive damage by splitting a target with dimensional attacks.

## Modes

| # | Mode |
|---|---|
| 1 | Warp Shot |
| 2 | Spatial Cleanse |
| 3 | Dimension Ray |
| 4 | Dimension Storm |
| 5 | Fault Field |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Warp Shot | 50 |  |
| Spatial Cleanse | 100 |  |
| Dimension Ray | 5,000 |  |
| Dimension Storm | 50,000 |  |
| Fault Field | 2,000 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you take damage

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.5 | multiply total |

## Obtaining

- Can be learned by: [Ender Dragonewt](../../../ascension/races/ender-dragonewt.md), [Void Dragonewt](../../../ascension/races/void-dragonewt.md), [Abyssal Dragonewt](../../../ascension/races/abyssal-dragonewt.md), [Chaos Dragon](../../../ascension/races/chaos-dragon.md), [Lich King](../../../ascension/races/lich-king.md)
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill IDs granted by Elfaria. Includes Albis so old Ars Weiss clones stay compatible, magic basics, transforms, senses, chant annulment,...
- Acquisition checks: [Spatial Manipulation](spatial-manipulation.md)

## Related

- **Related skills:** [Spatial Manipulation](spatial-manipulation.md)
- **Summons / entities:** Tensura, Spatial Ray
- **Referenced by:** [Spatial Manipulation](spatial-manipulation.md), [Spacetime Manipulation](../../../tr-nightmares/abilities/extra-skills/spacetime-manipulation.md), [Spacetime Domination](../../../tr-nightmares/abilities/extra-skills/spacetime-domination.md), [｢ Hastur, Lord of Starwind ｣](../../../tr-nightmares/abilities/ultimate-skills/hastur.md), [｢ Uriel, Lord of Oaths ｣](../../../tr-nightmares/abilities/ultimate-skills/uriel-lord-of-oath.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
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

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Learning.learningPointRequirement` | 100 | The number of learning points a new ability need to get to become fully learnt. |
| `Learning.learningPoint` | 1 | The base value of how many learning points the player gains when learning an ability. |
| `Learning.minBonus` | 0 | The min bonus learning points the player can gain when learning an ability. |
| `Learning.maxBonus` | 4 | The max bonus learning points the player can gain when learning an ability. |
| `Learning.learningCostMultiplier` | 5 | The multiplier of energy cost compared to normal cost when learning a new ability. |
| `Learning.learningPointRequirement` | 100 | The number of learning points a new ability need to get to become fully learnt. |
| `Learning.learningCooldown` | 10 | The number of seconds of cooldown when a new ability gains a learning point. |
| `Learning.learningFailCooldown` | 3 | The number of seconds of cooldown when a new ability fails to gain a learning point. |
| `Learning.failingPenaltyChance` | 0.1 | The chance to the failing penalty to apply. |
| `Learning.failingPenaltyLevel` | 1 | The level of the misfire status effect when failing penalty applies. |
| `Learning.failingPenaltyDuration` | 200 | The duration in ticks of the misfire status effect when failing penalty applies. |
| `Learning.failingPenaltyMin` | 1 | The min learning points the player can lose when failing to learn an ability. |
| `Learning.failingPenaltyMax` | 3 | The max learning points the player can lose when failing to learn an ability. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/elemental_domination`, `tensura:skills/extra_skills`, `tensura:skills/space_skills`
