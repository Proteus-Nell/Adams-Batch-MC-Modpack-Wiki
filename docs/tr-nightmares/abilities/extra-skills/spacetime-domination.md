# Spacetime Domination

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:spacetime_domination` |
| **Modes** | 6 |
| **Cooldowns (s)** | 120 |
| **Activation** | Toggle, Press, Hold |

</div>

> An upgraded spacetime package requiring mastered Spatial Domination and a compatible ultimate. Grants Spacetime Infliction, Warp Shot, Dimension Ray, Dimension Storm, Fault Field, Space-Time Cleanse, Spatial Transfer, and a learnable local Time Stop.

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Mode 2 |
| 3 | Mode 3 |
| 4 | Mode 4 |
| 5 | Mode 5 |
| 6 | Mode 6 |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 250,000 or base cost |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you take damage
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.5 | multiply total |

## Related

- **Related skills:** [Spacetime Manipulation](spacetime-manipulation.md), [Spatial Domination](../../../tensura-reincarnated/abilities/extra-skills/spatial-domination.md)
- **Referenced by:** [Witch's Greed](../unique-skills/witches-greed.md), [｢ Azathoth, God of The Void ｣](../ultimate-skills/azathoth.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `SpacetimeDomination.compatibleUltimateSkillIds` | "nightmareutils:sentient", "trnightmare:azathoth", "trnightmare:azazel", "trnightmare:nodens", "trnightmare:samael", "trnightmare:yog-sotohort" | Ultimate (or skill) resource ids that enable learning Spacetime Domination when possessed. Empty = unobtainable. Designer fill-in, e.g. trnightmare:example_spacetime_ultimate |
| `SpacetimeDomination.timeStopRadiusBlocks` | 32 | Time Stop radius in blocks (centered on caster). |
| `SpacetimeDomination.timeStopDurationTicks` | 180 | Time Stop duration in ticks when unmastered (9s = 180). |
| `SpacetimeDomination.timeStopDurationTicksMastered` | 840 | Time Stop duration in ticks when mastered (11s = 220). |
| `SpacetimeDomination.timeStopMagiculeCost` | 250,000 | Magicule cost per Time Stop use. |
| `SpacetimeDomination.timeStopLearnPoints` | 100 | Learn points required for Time Stop mode. |
| `SpacetimeDomination.timeStopCooldownSeconds` | 120 | Time Stop cooldown in seconds. |
| `SpacetimeDomination.timeStopSnowflakesPerTick` | 16 | Snowflake particles per tick while Time Stop is active. |
| `SpacetimeManipulation.spacetimeInflictionBoost` | 4 | Space damage multiplier while Spacetime Infliction is toggled (Spatial Domination uses 3.0). |
| `SpacetimeManipulation.magiculeCostCleansePerSeverance` | 100 | Magicule per severance point for Space-Time Cleanse. |
| `SpacetimeManipulation.cleanseCooldown` | 3 | Cooldown in seconds for Space-Time Cleanse. |
| `SpacetimeManipulation.shortTeleportRange` | 60 | Maximum blocks for short Spatial Transfer blink. |
| `SpacetimeManipulation.warpMpPerBlock` | 5 | Magicule per block for coordinate warp (Spatial Transfer shift). |
| `SpacetimeManipulation.requiredUltimateSkillIds` | "trnightmare:azathoth", "trnightmare:yog-sotohort" | Ultimate skill ids that satisfy the learn gate (§3 may mirror into SpacetimeManipulationCompat). |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

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

Set in [`config/tensura/ability/skill/extra_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-extra-config.md).

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
