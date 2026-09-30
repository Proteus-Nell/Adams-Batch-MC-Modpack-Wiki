# ｢ Hastur, Lord of Starwind ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:hastur` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 550,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 10 |
| **Activation** | Toggle, Press, Hold |

</div>

> Ultimate authority over wind, sound, and star tempest. Toggle Thought Acceleration; sonic/wind domination while slotted; turbulence black wind; Uriel-style barriers; and Apocalypse Howling.

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Mode 2 |
| 3 | Mode 3 |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| barrier | left | add |
| barrier | points | add |
| chant | 2 | add |
| move | move bonus | add |
| attack | attack bonus | add |
| degrade | 1 | add |

## Obtaining

- Listed in the `astralMasteredCreationUltimates` config option (config/nightmare/ability/skill/nightmare_ult.toml): Ultimate skill IDs only offered from Astral Light Skill Creation when Astral Light is mastered.

## Related

- **Related skills:** [Multilayer Barrier](../../../tensura-reincarnated/abilities/extra-skills/multilayer-barrier.md), [Black Flame](../../../tensura-reincarnated/abilities/extra-skills/black-flame.md), [Wind Domination](../../../tensura-reincarnated/abilities/extra-skills/wind-domination.md), [Sound Domination](../../../tensura-reincarnated/abilities/extra-skills/sound-domination.md), [Thought Acceleration](../../../tensura-reincarnated/abilities/extra-skills/thought-acceleration.md), [Universal Perception](../../../tensura-reincarnated/abilities/extra-skills/universal-perception.md), [Demon Lord Haki](../../../tensura-reincarnated/abilities/extra-skills/demon-lord-haki.md), [Weather Domination](../../../tensura-reincarnated/abilities/extra-skills/weather-domination.md), [Spatial Domination](../../../tensura-reincarnated/abilities/extra-skills/spatial-domination.md), [Voice Cannon](../../../tensura-reincarnated/abilities/common-skills/voice-cannon.md)
- **Effects:** [Black Burn](../../../tensura-reincarnated/effects/black-burn.md)
- **Summons / entities:** Tensura, Black Lightning Bolt

## Stats (config defaults)

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

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Hastur.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Hastur.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Hastur.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Hastur.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Hastur.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Hastur.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Hastur.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Hastur.mpAcquirement` | 550,000 | Magicule cost to acquire Hastur, Lord of Star Wind. |
| `Hastur.chantSpeedBonus` | 2 | Chant speed bonus while Thought Acceleration mode is toggled (Tensura Thought Accel uses +2 for x3). |
| `Hastur.movementSpeed` | 0.02 | Movement speed bonus while Thought Acceleration is toggled. |
| `Hastur.movementSpeedMastered` | 0.04 | Movement speed bonus when Thought Acceleration is toggled and mastered. |
| `Hastur.attackSpeed` | 0.4 | Attack speed bonus while Thought Acceleration is toggled. |
| `Hastur.attackSpeedMastered` | 0.6 | Attack speed bonus when Thought Acceleration is toggled and mastered. |
| `Hastur.sonicWindDominationBoost` | 3.5 | Wind and sound damage multiplier while Sound &amp; Wind mode is in slot (domination-style boost level). |
| `Hastur.windResistDegradationEp` | 100,000 | EP requirement for wind resist degradation while Sound &amp; Wind is in slot. |
| `Hastur.resistanceDegradation` | 1 | Resistance degradation while Sound &amp; Wind is in slot. |
| `Hastur.turbulenceStacksForBlackWind` | 3 | Sprint stacks required before black wind activates. |
| `Hastur.apocalypseExtraTurbulenceStacks` | 5 | Extra max sprint stacks while Apocalypse Howling is held. |
| `Hastur.apocalypseDeathStormStacks` | 5 | Sprint stacks to trigger Death Storm while Apocalypse Howling is held. |
| `Hastur.sprintTicksPerStack` | 20 | Player ticks of sprinting required per turbulence stack (20 = one second). |
| `Hastur.turbulenceSpeedRampMax` | 1.15 | Max movement speed ramp from turbulence stacks (ADD_MULTIPLIED_TOTAL). |
| `Hastur.apocalypseExtraSpeedRamp` | 0.45 | Extra speed ramp while Apocalypse Howling is held (added to turbulence ramp). |
| `Hastur.apocalypseMaxSpeedRamp` | 1.65 | Hard cap on total speed multiplier while Apocalypse Howling is held (1.0 + this). |
| `Hastur.apocalypseStrikeCooldownTicks` | 12 | Ticks between apocalypse lightning collision strikes per target. |
| `Hastur.apocalypsePresenceConcealmentLevel` | 3 | Presence concealment amplifier while Apocalypse Howling has black-wind stacks (level = value, effect amp = value - 1). |
| `Hastur.barrierSelfMultiplier` | 3.5 | Self multilayer barrier points multiplier (max HP). |
| `Hastur.barrierAllyMultiplier` | 0.75 | Ally multilayer barrier points multiplier (max HP). |
| `Hastur.barrierCooldown` | 10 | Multilayer barrier cooldown in seconds. |
| `Hastur.barrierMpPerDamage` | 5 | Magicule drained per 1 HP absorbed by multilayer barrier. |
| `Hastur.blackWindRadius` | 4 | Black wind aura radius. |
| `Hastur.blackWindHitIntervalTicks` | 5 | Ticks between black wind aura hits per target. |
| `Hastur.blackWindAuraDamageScale` | 1 | Scale on black wind aura damage (attack + BPS formula). |
| `Hastur.apocalypseAuraRadius` | 6 | Apocalypse aura radius while held. |
| `Hastur.apocalypseHitIntervalTicks` | 4 | Ticks between apocalypse aura hits. |
| `Hastur.apocalypseAuraDamageScale` | 1.25 | Scale on apocalypse aura damage. |
| `Hastur.apocalypseReleaseDamage` | 150 | Black lightning damage on Apocalypse release. |
| `Hastur.apocalypseReleaseRadius` | 12 | Radius for Apocalypse release black lightning. |
| `Hastur.ramMinSprintTicks` | 3 | Sprint stacks before collision ram damage applies. |
| `Hastur.ramSearchInflate` | 0.65 | Entity search inflate for collision ram. |
| `Hastur.perTargetCollisionCooldownTicks` | 8 | Per-target collision cooldown (ticks). |
| `Hastur.stepHeightFromSprintMax` | 2.5 | Max step height bonus at full sprint stacks. |
| `Hastur.stepSurgeMin` | 0.5 | Extra step surge when speed multiplier exceeds highSpeedThreshold. |
| `Hastur.stepSurgeExtra` | 1.5 | Additional step surge at max speed ramp. |
| `Hastur.highSpeedThreshold` | 1.35 | Speed multiplier threshold for step surge. |
| `Hastur.blackWindCollisionDamageScale` | 1 | Scale on black-wind collision damage (turbulence). |
| `Hastur.apocalypseCollisionDamageScale` | 1 | Scale on apocalypse collision black lightning damage. |
| `Hastur.speedModifierId` | "trnightmare:hastur_turbulence_speed" |  |
| `Hastur.hasturSubs` | 30 | Named subordinates required for Hastur. |
| `Hastur.hasturSkills` | 35 | Mastered Skills required for Hastur. |
| `Hastur.enableUltimateEvolution` | true | Whether Hastur can be obtained naturally |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

## In-game messages

<details markdown><summary>Show 3 messages</summary>

- Turbulence
- Multilayer Barrier
- Apocalypse Howling

</details>
