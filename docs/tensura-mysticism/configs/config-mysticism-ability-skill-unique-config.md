# `config/mysticism/ability/skill/unique_config.toml`

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Butcher]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 80,000 | |  | Magicule Acquirement Cost. |
| `heightenCost` | 1,500 | |  | The magicule cost of the Heighten mode. |
| `ruptureCost` | 2,500 | |  | The magicule cost of the Rupture mode. |
| `ruptureMarkRequirement` | 15 | |  | The number of marks required on an entity to trigger the Rupture mode. |
| `ruptureCooldown` | 30 | |  | The cooldown of the Rupture mode in seconds. |
| `ruptureCooldownMode` | true | |  | Should the cooldown be per target or flat? TRUE for "per target", FALSE for flat cooldown. |
| `血淋林的爱Cost` | 3,000 | |  | The magicule cost of 血淋林的爱. |
| `血淋林的爱Cooldown` | 120 | |  | The cooldown of the 血淋林的爱 Art in seconds. |
| `血淋林的爱MarkRequirement` | 20 | |  | The number of marks required to gain a charge of the 血淋林的爱 Art. |
| `chargesGained` | 1 | |  | The amount of charges you gain when killing an enemy that meets the above threshold defined. |

## `[Captivator]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 60,000 | |  | Magicule Acquirement Cost. |
| `mpPerformanceCost` | 250 | |  | Magicule cost of Performance mode. |
| `performanceCooldown` | 60 | |  | The cooldown of the Performance mode in seconds. |
| `performanceRange` | 20 | |  | The range for the Performance mode in blocks. |
| `mpMasqueradeCost` | 300 | |  | Magicule cost of Masquerade mode. |
| `masqueradeCooldown` | 30 | |  | The cooldown of the Masquerade mode in seconds. |
| `masqueradeRange` | 15 | |  | The range for the Masquerade mode in blocks. |
| `mpUnveilCost` | 500 | |  | Magicule cost of Unveil mode. |
| `unveilCooldown` | 30 | |  | The cooldown of the Unveil mode in seconds. |
| `unveilRange` | 15 | |  | The range in blocks for Unveil |
| `mpStarPowerCost` | 1,000 | |  | Magicule cost of Star Power Mode. |
| `starPowerCooldown` | 40 | |  | The cooldown of the Star Power mode in seconds. |

## `[Coalescence]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 90,000 | |  | Magicule Acquirement Cost. |
| `fixationCost` | 1,000 | |  | The magicule cost of the Fixation mode. |
| `fixationRange` | 10 | |  | The range of the Fixation mode in blocks. |
| `fixationRangeMastery` | 15 | |  | The range of the Fixation mode in blocks when the skill is mastered. |
| `fixationDuration` | 200 | |  | The duration of the Fixation effect in ticks (seconds x 20). |
| `fixationDurationMastered` | 400 | |  | The duration of the Fixation effect in ticks (seconds x 20). |
| `fixationCooldown` | 30 | |  | The cooldown of the Fixation mode in seconds. |
| `fixationCooldownMastered` | 15 | |  | The cooldown of the Fixation mode in seconds when the skill is mastered. |
| `fixationMissCooldown` | 5 | |  | The cooldown of the Fixation mode when the user misses. |
| `fixationMissCooldownMastered` | 5 | |  | The cooldown of the Fixation mode when the user misses and the skill is mastered. |
| `solidificationCost` | 1,000 | |  | The magicule cost of the Solidification mode. |
| `solidificationCooldown` | 20 | |  | The cooldown of the solidification mode in seconds. |
| `solidificationCooldownMastered` | 10 | |  | The cooldown of the solidification mode in seconds when the skill is mastered. |
| `solidificationShieldDuration` | 400 | |  | The cooldown of the solidification shield in ticks. |
| `solidificationShieldDurationMastered` | 800 | |  | The cooldown of the solidification shield in ticks when the skill is mastered. |
| `eternalDomainCost` | 10,000 | |  | The magiule cost of the Eternal Domain art. |
| `eternalDomainRange` | 8 | |  | The radius of Eternal Domain in blocks. |
| `eternalDomainRangeMastered` | 16 | |  | The radius of Eternal Domain in blocks when the skill is mastered. |
| `eternalDomainLife` | 400 | |  | How long in ticks (seconds x 20) the Eternal Domain should last. |
| `eternalDomainLifeMastered` | 800 | |  | How long in ticks (seconds x 20) the Eternal Domain should last when the skill is mastered. |
| `eternalDomainCooldown` | 180 | |  | The cooldown of the Eternal Domain art in seconds. |
| `eternalDomainCooldownMastered` | 90 | |  | The cooldown of the Eternal Domain art in seconds when the skill is mastered. |

## `[Constant]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 40,000 | |  | Magicule Acquirement Cost. |
| `constantHealthCost` | 1,000 | |  | Magicule cost of the Constant: Health mode. |
| `constantHealthTickCost` | 1,000 | |  | Magicule cost of the Constant: Health mode that drains every second (20 ticks). |
| `constantHealthHeldTicks` | 300 | |  | The maximum amount of time in ticks (multiply seconds by 20) that you can hold down Constant: Health for. |
| `constantHealthHeldTicksMastered` | 300 | |  | The maximum amount of time in ticks (multiply seconds by 20) that you can hold down Constant: Health for when the skill is mastered. |
| `constantHealthCooldown` | 15 | |  | The cooldown of the Constant: Health mode. |
| `constantHealthCooldownMastered` | 15 | |  | The cooldown of the Constant: Health mode when the skill is mastered. |
| `constantPhysicalCost` | 0 | |  | Magicule cost of the Constant: Physical mode. |
| `constantPhysicalTimer` | 100 | |  | How long should the timer for Constant: Physical run for in ticks. |
| `constantPhysicalCooldown` | 10 | |  | The cooldown of the Constant: Physical mode. |
| `constantPhysicalCooldownMastered` | 10 | |  | The cooldown of the Constant: Physical mode. |
| `constantDestructionCost` | 3,000 | |  | Magicule cost of the Constant: Destruction mode. |
| `constantDestructionHeldTicks` | 200 | |  | The maximum amount of time in ticks (multiply seconds by 20) that you can hold down Constant: Destruction for. |
| `constantDestructionHeldTicksMastered` | 200 | |  | The maximum amount of time in ticks (multiply seconds by 20) that you can hold down Constant: Destruction for when the skill is mastered. |
| `constantDestructionMaxDamage` | 5,000 | |  | The maximum damage that Constant: Destruction can have. (Default: 5000) |
| `constantDestructionCooldown` | 20 | |  | The cooldown of the Constant: Destruction mode. |
| `constantDestructionCooldownMastered` | 20 | |  | The cooldown of the Constant: Destruction mode when the skill is mastered. |
| `constantEnergyCost` | 1,000 | |  | Magicule cost of the Constant: Energy mode. |
| `constantEnergyDuration` | 10 | |  | The duration, in seconds, of the Constant: Energy effect. |
| `constantEnergyDebuffDuration` | 180 | |  | The duration, in seconds, of the debuff of the Constant: Energy effect. |
| `constantEnergyCooldown` | 120 | |  | The cooldown of the Constant: Energy mode. |

## `[Corroder]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 25,000 | |  | Magicule Acquirement Cost. |
| `meleeCorrosionLevel` | 2 | |  | The level of Corrosion you apply when performing a melee attack when the skill is in slot. |
| `meleeCorrosionLevelMastered` | 3 | |  | The level of Corrosion you apply when performing a melee attack when the skill is mastered and in slot. |
| `meleeCorrosionDuration` | 200 | |  | The amount of time in ticks of the the Corrosion effect when performing a melee attack when the skill is in slot. (Take seconds times 20.) |
| `meleeCorrosionDurationMastered` | 300 | |  | The amount of time in ticks of the Corrosion effect when performing a melee attack when the skill is mastered and in slot. (Take seconds times 20.) |
| `dissolveCost` | 100 | |  | The magicule cost of the Dissolve mode, taken every 10 ticks. |
| `dissolveRadius` | 10 | |  | The radius of your corrosion damage from the Dissolve mode. |
| `dissolveRadiusMastered` | 15 | |  | The radius of your corrosion damage from the Dissolve mode when the skill is mastered. |
| `dissolveDamage` | 10 | |  | The damage of your corrosion from the Dissolve mode. |
| `dissolveDamageMastered` | 15 | |  | The damage of your corrosion from the Dissolve mode when the skill is mastered. |
| `dissolveCorrosionLevel` | 1 | |  | The level of Corrosion you apply from the Dissolve mode. |
| `dissolveCorrosionLevelMastered` | 2 | |  | The level of Corrosion you apply from the Dissolve mode. |
| `dissolveCorrosionDuration` | 200 | |  | The amount of time in ticks of the Corrosion effect from the Dissolve mode. (Take seconds times 20.) |
| `dissolveCorrosionDurationMastered` | 300 | |  | The amount of time in ticks of the Corrosion effect from the Dissolve mode when the skill is mastered. (Take seconds times 20.) |
| `crossCorrosionCost` | 1,000 | |  | The magicule cost of the Cross Corrosion mode. |
| `crossCorrosionMultiplier` | 2 | |  | The damage multiplier of your next attack when Cross Corrosion is used. |
| `crossCorrosionCooldown` | 20 | |  | The cooldown of Cross Corrosion in seconds. |
| `crossCorrosionCooldownMastered` | 15 | |  | The cooldown of Cross Corrosion in seconds when the skill is mastered. |

## `[Crasher]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 45,000 | |  | Magicule Acquirement Cost. |
| `destroyerHakiCost` | 250 | |  | The magicule cost of the Destroyer Haki mode, taken every 10 ticks. |
| `destroyerHakiRadius` | 15 | |  | The radius in blocks of the Destroyer Haki mode. |
| `destroyerHakiEP` | 0.6 | |  | The multiplier of EP that an entity needs to have below to be affected by the Destroyer Haki's movement speed reduction. |
| `destroyerHakiEPMastered` | 0.8 | |  | The multiplier of EP that an entity needs to have below to be affected by Destroyer Haki's movement speed reduction when mastered. |
| `epDifferenceMultiplier` | 0.1 | |  | The EP difference multiplier for each Slowness Level when applied by Destroyer Haki. |
| `destroyerHakiDamage` | 25 | |  | The damage that Destroyer Haki will deal every 20 ticks (one second). |
| `destroyerHakiDamageMastered` | 50 | |  | The damage that Destroyer Haki will deal every 20 ticks (one second) when the skill is mastered. |
| `insanityChance` | 20 | |  | The chance that Insanity is applied to the USER every 60 ticks when Destroyer Haki is used. |
| `insanityLevel` | 1 | |  | The increasing level of Insanity when it is applied to the USER when Destroyer Haki is used. |
| `insanityDuration` | 200 | |  | The duration in tick of the Insanity effect when the USER is affected by Destroyer Haki. |
| `slowDuration` | 200 | |  | The duration in tick of the Slowness effect when targets are affected by Destroyer Haki. |
| `slowDurationMastered` | 250 | |  | The duration in tick of the Slowness effect when targets are affected by Destroyer Haki when [Crasher] is mastered.. |
| `dimensionHopperCost` | 1,000 | |  | The magicule cost of the Dimension Hopper mode. |
| `dimensionHopperCooldown` | 600 | |  | The cooldown of the Dimension Hopper mode. |
| `dimensionHopperCooldownMastered` | 300 | |  | The cooldown of the Dimension Hopper mode when the skill is mastered. |

## `[Cultivator]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 80,000 | |  | Magicule Acquirement Cost. |
| `attackBoost` | 50 | |  | The physical attack damage boost when in Slot. |
| `attackBoostMastered` | 100 | |  | The physical attack damage boost when in Slot with mastery. |
| `mobKillsNeeded` | 1,000 | |  | The ammount of mob kills needed to start Cultivation. |
| `breakthroughCooldown` | 3,600 | |  | The cooldown on Breakthrough when it completes. |
| `cultivationTimer` | 6,000 | |  | How long cultivation lasts in ticks (seconds x 20). |
| `breakthroughMasteryGain` | 100 | |  | The amount of mastery the user gains when successfully breaking through. |
| `magiculePercentage` | 10 | |  | The bonus Magicule percentage the user gains. |
| `magiculePercentageMastered` | 15 | |  | The bonus Magicule percentage the user gains with Mastery. |
| `cultivationMPMultiplier` | 3 | |  | The multiplicative magicule gain the user receives while in the middle of Breaking Through. |

## `[Disintegration]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `disintegrationCost` | 250,000 | |  | The Magicule cost of the Disintegration mode. |
| `survivalUsable` | false | |  | Can this skill be used in survival? (True for yes, false for no). |
| `haveCooldown` | false | |  | Should this skill have a cooldown? |
| `disintegrationCooldown` | 1,800 | |  | The cooldown of the Disintegration mode if the user successfully hits a target in seconds. |
| `disintegrationCooldownMastered` | 1,200 | |  | The cooldown of the Disintegration mode if the user successfully hits a target in seconds, when the skill is mastered. |
| `disintegrationCooldownMiss` | 30 | |  | The cooldown incurred on the Disintegration mode if the user does not hit a target. |
| `disintegrationCooldownMissMastered` | 15 | |  | The cooldown incurred on the Disintegration mode if the user does not hit a target, when the skill is mastered. |

## `[Dreamer]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 60,000 | |  | Magicule Acquirement Cost. |
| `magiculeRecovery` | 0.5 | |  | The percentage of magicules that will be recovered every 5 seconds. |
| `magiculeRecoveryMastered` | 1 | |  | The percentage of magicules that will be recovered every 5 seconds when the skill is mastered. |
| `drainMode` | false | |  | The draining mode of magicules when the Dream mode is used. FALSE for percentage cost. TRUE for flat cost. |
| `dreamSetPercentageCost` | 25 | |  | The percentage of magicules that will be drained from the user to set a dream, IF drainMode above is set to false. |
| `dreamSetFlatCost` | 750 | |  | The flat cost of magicules that will be drained from the user to set a dream, IF drainMode above is set to true. |
| `dreamActivateCost` | 0 | |  | The amount of magicules used when a dream is activated. |
| `hypnosisCost` | 150 | |  | The amount of magicules that the Hypnosis mode drains every second it is active. |
| `dreamEaterCost` | 300 | |  | The amount of magicules that the Dream Eater mode drains when it is used. |
| `dreamCooldown` | 300 | |  | The cooldown of the Dream mode after it has been activated. |
| `dreamCooldownMastered` | 120 | |  | The cooldown of the Dream mode after it has been activated, when the skill is mastered. |
| `hypnosisRadius` | 10 | |  | The radius of the Hypnosis mode in blocks. |
| `hypnosisRadiusMastered` | 15 | |  | The radius of the Hypnosis mode in blocks when the skill is mastered. |
| `hypnosisDuration` | 200 | |  | The duration of the Drowsiness effect in ticks (seconds x 20). |
| `hypnosisDurationMastered` | 300 | |  | The duration of the Drowsiness effect in ticks when the skill is mastered (seconds x 20). |
| `hypnosisLevel` | 1 | |  | The effect level of the Drowsiness effect when applied by Hypnosis. |
| `hypnosisLevelMastered` | 2 | |  | The effect level of the Drowsiness effect when applied by Hypnosis when the skill is mastered. |
| `dreamEaterRange` | 15 | |  | The range of the Dream Eater mode in blocks. |
| `dreamEaterRangeMastered` | 20 | |  | The range of the Dream Eater mode in blocks when the skill is mastered. |
| `dreamEaterDamage` | 30 | |  | The range of the Dream Eater mode in blocks. |
| `dreamEaterDamageMastered` | 50 | |  | The range of the Dream Eater mode in blocks when the skill is mastered. |
| `dreamEaterSpiritualDamage` | 30 | |  | The range of the Dream Eater mode in blocks. |
| `dreamEaterSpiritualDamageMastered` | 50 | |  | The range of the Dream Eater mode in blocks when the skill is mastered. |
| `dreamEaterDreamCooldownReduction` | 15 | |  | The number of seconds that Dream Eater reduces the cooldown of Dream by. |
| `dreamEaterDreamCooldownReductionMastered` | 15 | |  | The number of seconds that Dream Eater reduces the cooldown of Dream by when the skill is mastered. |

## `[Engineer]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 50,000 | |  | Magicule Acquirement Cost. |
| `buildSentryCost` | 500 | |  | The magicule cost of the Build mode when placing a Sentry. |
| `buildSentryCostMastered` | 500 | |  | The magicule cost of the Build mode when placing a Sentry, when the skill is mastered. |
| `sentryLevel1FireRate` | 10 | |  | The fire rate of a Level 1 Sentry. |
| `sentryLevel2LevelUpTime` | 2,400 | |  | The time taken (in ticks) for a Level 1 Sentry to evolve to Level 2. |
| `sentryLevel2FireRate` | 5 | |  | The fire rate of a Level 2 Sentry. |
| `sentryLevel3LevelUpTime` | 6,000 | |  | The time taken (in ticks) for a Level 2 Sentry to evolve to Level 3. |
| `sentryLevel3FireRate` | 10 | |  | The fire rate of a Level 3 Sentry. |
| `buildDispenserCost` | 500 | |  | The magicule cost of the Build mode when placing a Dispenser. |
| `buildDispenserCostMastered` | 500 | |  | The magicule cost of the Build mode when placing a Dispenser, when the skill is mastered. |
| `buildCooldown` | 30 | |  | The cooldown of the Build mode in seconds. |
| `buildCooldownMastered` | 15 | |  | The cooldown of the Build mode in seconds, when the skill is mastered. |
| `bubbleShieldCost` | 1,000 | |  | The magicule cost of the Bubble Shield mode. |
| `bubbleShieldCostMastered` | 1,000 | |  | The magicule cost of the Bubble Shield mode when the skill is mastered. |
| `bubbleShieldShouldHurt` | false | |  | Should the Bubble Shield be able to be destroyed from within? ("true" = yes/"false" = no) |
| `bubbleShieldSize` | 7 | |  | The size of the Bubble Shield in radius. Decimal values will crash your game. |
| `bubbleShieldCooldown` | 25 | |  | The cooldown in seconds of the Bubble Shield mode. |
| `bubbleShieldCooldownMastered` | 15 | |  | The cooldown in seconds of the Bubble Shield mode when the skill is mastered. |
| `bubbleShieldLifespan` | 300 | |  | The lifespan of the Bubble Shield, in ticks (seconds x 20. 600 = 30 seconds). |
| `bubbleShieldLifespanMastered` | 600 | |  | The lifespan of the Bubble Shield when the skill is mastered, in ticks (seconds x 20. 600 = 30 seconds). |
| `percentageDispenserEPRegenLevel1` | 0.5 | |  | The percentage of EP regenerated to a Dipsenser's allies when it's activated when it is level one. |
| `percentageDispenserEPRegenLevel2` | 1 | |  | The percentage of EP regenerated to a Dipsenser's allies when it's activated when it is level two. |
| `percentageDispenserEPRegenLevel3` | 3 | |  | The percentage of EP regenerated to a Dipsenser's allies when it's activated when it is level three. |
| `healthDispenserRegenLevel2` | 10 | |  | The amount of HP regenerated to a Dipsenser's allies when it's activated when it is level two. |
| `healthDispenserRegenLevel3` | 5 | |  | The percentage of HP regenerated to a Dipsenser's allies when it's activated when it is level three. |
| `foodDispenserRegenLevel1` | 1 | |  | The amount of food regenerated to a Dipsenser's allies when it's activated when it is level one. |
| `foodDispenserRegenLevel2` | 2 | |  | The amount of food regenerated to a Dipsenser's allies when it's activated when it is level two. |
| `foodDispenserRegenLevel3` | 3 | |  | The amount of food regenerated to a Dipsenser's allies when it's activated when it is level three. |

## `[Gardener]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 40,000 | |  | Magicule Acquirement Cost. |
| `cropMasteryCost` | 100 | |  | The magicules taken every 5 seconds for the Crop Mastery passive. |
| `cropMasteryChance` | 50 | |  | The chance for a crop to grow to the next stage every 5 seconds when Crop Mastery is triggered. |
| `cropMasteryChanceHipokute` | 10 | |  | The chance for a Hipokute plant to grow to the next stage every 5 seconds when Crop Mastery is triggered. |
| `cropMasteryChanceMastered` | 75 | |  | The chance for a crop to grow to the next stage every 5 seconds when Crop Mastery is triggered. |
| `cropMasteryChanceHipokuteMastered` | 20 | |  | The chance for a Hipokute plant to grow to the next stage every 5 seconds when Crop Mastery is triggered. |
| `overgrowCropRequirement` | 25 | |  | The amount of crops you need to grow to gain a charge for Overgrow. |
| `blessingCost` | 250 | |  | The magicule cost of the Blessing mode, for each item in the stack (blessingCost \* stack amount = MP cost). |
| `blessingCostMastered` | 500 | |  | The magicule cost of the Blessing mode when the skill is mastered, for each item in the stack (blessingCostMastered \* stack amount = MP cost). |
| `blessingCooldown` | 3 | |  | The cooldown of the Blessing mode in seconds. |
| `blessingCooldownMastered` | 1 | |  | The cooldown of the Blessing mode in seconds when the skill is mastered. |
| `dawnBlessingEffect` | "tensura:strengthen" | |  | The effect granted to the food stack when Blessing is used at dawn. |
| `dawnEffectLevel` | 3 | |  | The effect level granted to the consumer of the food stack when Blessing is used at dawn. |
| `dawnDuration` | 3,600 | |  | The duration of the effect granted to the consumer of the food stack when Blessing is used at dawn. |
| `dawnEffectLevelMastered` | 5 | |  | The effect level granted to the consumer of the food stack when Blessing is used at dawn when Gardener is mastered. |
| `dawnDurationMastered` | 6,000 | |  | The duration of the effect granted to the consumer of the food stack when Blessing is used at dawn when Gardener is mastered. |
| `noonBlessingEffect` | "minecraft:resistance" | |  | The effect granted to the food stack when Blessing is used at noon. |
| `noonEffectLevel` | 1 | |  | The effect level granted to the consumer of the food stack when Blessing is used at noon. |
| `noonDuration` | 3,600 | |  | The duration of the effect granted to the consumer of the food stack when Blessing is used at noon. |
| `noonEffectLevelMastered` | 2 | |  | The effect level granted to the consumer of the food stack when Blessing is used at noon when Gardener is mastered. |
| `noonDurationMastered` | 3,600 | |  | The duration of the effect granted to the consumer of the food stack when Blessing is used at noon when Gardener is mastered. |
| `nightBlessingEffect` | "minecraft:speed" | |  | The effect granted to the food stack when Blessing is used at night. |
| `nightEffectLevel` | 3 | |  | The effect level granted to the consumer of the food stack when Blessing is used at night. |
| `nightDuration` | 3,600 | |  | The duration of the effect granted to the consumer of the food stack when Blessing is used at night. |
| `nightEffectLevelMastered` | 5 | |  | The effect level granted to the consumer of the food stack when Blessing is used at night when Gardener is mastered. |
| `nightDurationMastered` | 6,000 | |  | The duration of the effect granted to the consumer of the food stack when Blessing is used at night when Gardener is mastered. |
| `overgrowCooldown` | 300 | |  | The cooldown of the Overgrow mode in seconds. |
| `overgrowDuration` | 500 | |  | The duration that Overgrow lasts for, in ticks (seconds x 20). |

## `[HiddenRuler]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 50,000 | |  | Magicule Acquirement Cost. |
| `vanishMagiculeCost` | 50 | |  | The Magicule cost of Hidden Ruler's toggled passive. |
| `vanishAuraCost` | 0 | |  | The Aura cost of Hidden Ruler's toggled passive. |
| `inspireRadius` | 15 | |  | The radius in blocks of the Inspiration effect provided by Hidden Ruler to nearby allies. |
| `noTargetCooldown` | 5 | |  | The cooldown that is applied if there is no target for either Copy or Paste. |
| `copyCost` | 1,000 | |  | The FLAT cost of the Copy mode when attempting to copy a skill from the target. |
| `copyCooldown` | 10 | |  | The cooldown of the Copy mode. |
| `copyCooldownMastered` | 10 | |  | The cooldown of the Copy mode when the skill is mastered. |
| `copyChance` | 25 | |  | The chance for the Copy mode to pass. |
| `copyChanceMastered` | 50 | |  | The chance for the Copy mode to pass when the skill is mastered. |
| `copyFailedCooldown` | 10 | |  | The cooldown of the Copy mode when a failure is encountered. |
| `failureThreshold` | 2 | |  | The EP threshold that is checked when the user is weaker than the target when the Copy mode is used. |
| `failureThresholdMastered` | 2.5 | |  | The EP threshold that is checked when the user is weaker than the target when the Copy mode is used and the skill is mastered. |
| `pasteCost` | 1,000 | |  | The FLAT cost of the Paste mode when attempting to paste a skill onto the target. |
| `pasteCooldown` | 10 | |  | The cooldown of the Paste mode. |
| `pasteCooldownMastered` | 10 | |  | The cooldown of the Paste mode when the skill is mastered. |
| `pasteChance` | 25 | |  | The chance for the Paste mode to pass. |
| `pasteChanceMastered` | 50 | |  | The chance for the Paste mode to pass when the skill is mastered. |
| `pasteFailedCooldown` | 10 | |  | The cooldown of the Paste mode when a failure is encountered. |
| `darknessConscriptionCost` | 1,000 | |  | How many magicules should be taken from the user when attempting to Charm a target?. |
| `lightLevel` | 5 | |  | The light level that both the target AND user MUST be under to successfully charm the target with Darkness Conscription. |
| `darknessConscriptionCooldown` | 10 | |  | The cooldown of the Darkness Conscription mode. |
| `darknessConscriptionCooldownMastery` | 10 | |  | The cooldown of the Darkness Conscription mode when the skill is mastered. |

## `[Jinchuriki]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 95,000 | |  | Magicule Acquirement Cost. |
| `epGainIncrease` | 6 | |  | The EP gain increase the user receives while the skill is toggled on. |
| `epGainIncreaseMastered` | 11 | |  | The EP gain increase the user receives while the skill is toggled on when the skill is mastered. |
| `cloakPreControlLifespan` | 30 | |  | The time that the Tailed Beast Cloak lasts before gaining control over it, in seconds. |
| `tailedBeastCloakCooldown` | 60 | |  | The cooldown of the Tailed Beast Cloak mode, in seconds. |
| `tailedBeastCloakCooldownMastered` | 30 | |  | The cooldown of the Tailed Beast Cloak mode when the skill is mastered, in seconds. |
| `v1Cloak` | 10 | |  | The number of uses to progress to the v1 Cloak. |
| `v2Cloak` | 100 | |  | The number of uses to progress to the v2 Cloak. |
| `controlledState` | 250 | |  | The number of uses to progress to the Controlled State. |
| `perfectControlledState` | 1,000 | |  | The number of uses to achieve Perfect Control State. |
| `mpCostPerCharge` | 800 | |  | Magicule cost for each 1.0 of charge for the Tailed Beast Bomb. |
| `apCostPerCharge` | 200 | |  | Aura cost for each 1.0 of charge for the Tailed Beast Bomb. |
| `maxMultiplier` | 100 | |  | The Max Charge of the Tailed Beast Bomb. |
| `maxMultiplierMastered` | 150 | |  | The Max Charge of the Tailed Beast Bomb when Mastered. |
| `holdTime` | 20 | |  | Ticks the user must hold to gain 1.0 charge (20 = 1 second). |
| `holdTimeMastered` | 10 | |  | Ticks the user must hold to gain 1.0 charge when Mastered (10 = 0.5 second). |
| `baseDamage` | 6 | |  | Damage dealt per 1.0 charge (6 per 1.0 = 30 per 5.0). |
| `explosionThreshold` | 3 | |  | The bomb explodes on impact only if charged past this amount. |
| `explosionDamage` | 150 | |  | Damage of the explosion at the impact zone. |
| `explosionBaseRadius` | 3 | |  | Base explosion radius once the explosion threshold is passed. |
| `explosionRadiusPer10Charge` | 2 | |  | Explosion radius increase for each 10.0 of charge. |

## `[Kyurem]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `epRequirement` | 100,000 | |  | EP Needed to Obtain. |
| `canAcquireWithOtherSkills` | true | |  | Should this skill be acquirable if you have [Reshiram] or [Zekrom]? |
| `iceEssenceAmount` | 10 | |  | Amount of Ice Essence needed to be consumed for acquisition. |
| `dragonEssenceAmount` | 10 | |  | Amount of Dragon Essence needed to be consumed for acquisition. |
| `mpAcquirement` | 64,600 | |  | Magicule Acquirement Cost. |
| `pressureEffectDuration` | 30 | |  | Pressure Effect Duration in Seconds |
| `pressureCostMultiplier` | 2 | |  | Pressure Cost Multiplier. |
| `glaciateMPCost` | 900 | |  | Magicule cost for the Glaciate Mode. |
| `glaciateRange` | 15 | |  | Range of Glaciate Mode in blocks |
| `glaciateDamageIncrement` | 10 | |  | The amount of incremented damage for Glaciate mode per 10 seconds |
| `glaciateMaxDamageMastered` | 200 | |  | The Max Damage Glaciate can deal when Mastered. |
| `glaciateMaxDamage` | 100 | |  | The Max Damage Glaciate can deal. |
| `glaciateCooldown` | 30 | |  | Cooldown of Glaciate Mode. |
| `draconicPulseMPCost` | 700 | |  | Magicule cost for the Draconic Pulse Mode. |
| `draconicPulseDamage` | 40 | |  | Draconic Pulse Damage. |
| `draconicPulseExplosionRadius` | 7.5 | |  | Draconic Pulse Explosion Radius. |
| `draconicPulseCooldown` | 10 | |  | Draconic Pulse Cooldown. |
| `draconicPulseCooldownMastered` | 5 | |  | Draconic Pulse Cooldown Mastered. |
| `freezeDryMPCost` | 800 | |  | Magicule cost for the Freeze Dry Mode. |
| `freezeDryDamage` | 20 | |  | Damage of Freeze Dry Mode. |
| `freezeDryCooldown` | 20 | |  | Cooldown of Freeze Dry Mode. |
| `freezeDryCooldownMastered` | 10 | |  | Cooldown of Freeze Dry Mode when Mastered. |
| `blizzardMPCost` | 900 | |  | Magicule cost for the Blizzard Mode. |
| `blizzardDamage` | 40 | |  | Blizzard Damage. |
| `blizzardCooldown` | 10 | |  | Cooldown of Blizzard. |
| `blizzardRadius` | 7.5 | |  | Radius of Blizzard |

## `[Looter]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 50,000 | |  | Magicule Acquirement Cost. |
| `range` | 5 | |  | Targeting range in blocks for turning a soul into a shadow. |
| `radiusReturn` | 15 | |  | The radius in blocks of the Return mode of Shadow Storage. |

## `[Malleable]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 50,000 | |  | Magicule Acquirement Cost. |
| `learningPoint` | 4 | |  | The bonus learning points gained towards Earth-type abilities AND Resist-type skills when the skill is toggled on. |
| `masteryPoint` | 4 | |  | The bonus mastery points gained towards Earth-type abilities AND Resist-type skills when the skill is toggled on. |
| `alchemyDuration` | 200 | |  | The duration of the Alchemy mode in ticks when the skill is NOT mastered. |
| `alchemyCooldown` | 10 | |  | The cooldown of the Alchemy mode in seconds. |
| `alchemyToggleableMastery` | true | |  | If true, Alchemy becomes toggleable on mastery. If false, it follows a cooldown that you can change below. |
| `alchemyCooldownMastered` | 10 | |  | The cooldown of the Alchemy mode in seconds when the skill is mastered. |
| `hardenCooldown` | 120 | |  | The cooldown of the Harden mode in seconds. |
| `hardenCooldownMastered` | 60 | |  | The cooldown of the Harden mode in seconds when the skill is mastered. |
| `maximumHardenDuration` | 200 | |  | The maximum duration the Harden mode can be used for in ticks (seconds multiplied by 20.) |
| `regenerationLevel` | 5 | |  | The level of the respective effects you gain while Harden is active. |
| `resistanceLevel` | 2 | |  |  |
| `maximumHardenDurationMastery` | 300 | |  | The maximum duration the Harden mode can be used for in ticks (seconds multiplied by 20.) |
| `hardenShouldDisableAttack` | true | |  | Should the Harden mode disable attack/movement speed? False if they should not. |
| `hardenShouldDisableMovement` | true | |  |  |
| `hardenArmorPoints` | 10 | |  | The amount of armor points that should be granted to the user when the Harden mode is used. |
| `vesselCooldown` | 60 | |  | The cooldown of the Vessel mode in seconds. |
| `vesselCooldownMastered` | 30 | |  | The cooldown of the Vessel mode in seconds. |
| `vesselHP` | 50 | |  | The health points given to the Vessel created. |
| `vesselArmor` | 10 | |  | The armor points given to the Vessel created. |
| `vesselHPMastered` | 200 | |  | The health points given to the Vessel created when the skill is mastered. |
| `vesselArmorMastered` | 30 | |  | The armor points given to the Vessel created when the skill is mastered. |

## `[Melancholy]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 100,000 | |  | Magicule Acquirement Cost. |
| `magiculeCost` | 750 | |  | Flat magicule cost when using Melancholy (per press/activation). |
| `defaultRange` | 15 | |  | Default targeting range in blocks for Gust. |
| `ishaRange` | 10 | |  | Range of Ishtar's Tear. |
| `ishaRangeMastered` | 15 | |  | Range of Ishtar's Tear when the skill is mastered. |
| `ishaLevel` | 4 | |  | Level of slowness given to entities other than the user. |
| `ishaLevelUser` | 2 | |  | Level of slowness given to the user. |
| `ishaResistLevel` | 2 | |  | Level of resistance given to the user. |
| `veilKnockbackRadius` | 12 | |  | Radius of the Veil mode. |
| `veilSlownessLevel` | 10 | |  | Level of slowness given to entities when Veil is used. |
| `veilBurdenLevel` | 4 | |  | Level of slowness given to entities when Veil is used. |
| `griefKnockbackRadius` | 8 | |  | Radius of the Grief mode. |
| `griefEffectLevel` | 2 | |  | Level of blindness and weakness given to entities when Grief is used. |
| `maxRange` | 50 | |  | Maximum adjustable targeting range in blocks. |
| `pushEntity` | 1.4 | |  | Base push velocity scale applied to entities when using Gust. |
| `pullEntity` | 1.1 | |  | Base pull velocity scale applied to entities when using Gust while sneaking. |
| `pushEntityManipulation` | 0.25 | |  | Additional push scale when Gravity Manipulation is toggled. |
| `pushEntityDomination` | 0.45 | |  | Additional push scale when Gravity Domination is toggled. |
| `pullEntityManipulation` | 0.2 | |  | Additional pull scale when Gravity Manipulation is toggled. |
| `pullEntityDomination` | 0.4 | |  | Additional pull scale when Gravity Domination is toggled. |
| `airThrowDamage` | 75 | 4 |  | The base damage of thrown air. |
| `airThrowDamageMastered` | 100 | 6 |  | The base damage of thrown air when mastered. |
| `itemThrowDamage` | 125 | 6 |  | The base damage of thrown items. |
| `itemThrowDamageMastered` | 175 | 9 |  | The base damage of thrown items when mastered. |
| `itemThrowManipulation` | 1.25 | |  | Damage multiplier applied to thrown items when Gravity Manipulation is toggled. |
| `itemThrowDomination` | 1.5 | |  | Damage multiplier applied to thrown items when Gravity Domination is toggled. |

## `[Phaser]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 72,000 | |  | Magicule Acquirement Cost. |
| `presenceSense` | 2 | |  | The level of presence sense gained when toggling on the skill. |
| `eyeOfInsightCost` | 50 | |  | The Magicule cost of the Eye of Insight passive. |
| `overuseCap` | 10 | |  | The maximum number of abilities you can use without rest before you are forced on cooldowns from overuse. |
| `intangibilityPassiveCooldown` | 15 | |  | The cooldown of the Intangibility passive in seconds. |
| `intangibilityActiveCooldown` | 15 | |  | The cooldown of the Intangibility active in seconds, which only becomes available when the skill is mastered. |
| `intangibilityDuration` | 100 | |  | How long should the player phase through all attacks in ticks (seconds x 20). |
| `intangibilityActiveCost` | 100 | |  | The magicule cost of the Intangibility active mode. |
| `intangibilityPassiveCost` | 100 | |  | The magicule cost of the Intangibility passive mode. |
| `itemEjectDamage` | 20 | |  | The amount of damage that an ejected item from Phaser's portals should deal. |
| `itemEjectDamageMastered` | 30 | |  | The amount of damage that an ejected item from Phaser's portals should deal when the skill is mastered. |
| `ejectChargeTicks` | 60 | |  | The time taken for the portals to prime before you can shoot in ticks (seconds x 20). |
| `ejectChargeTicksMastered` | 30 | |  | The time taken for the portals to prime before you can shoot in ticks when the skill is mastered (seconds x 20). |
| `ejectCost` | 200 | |  | The magicule cost of each portal that is opened when the Eject mode is used. |
| `kamuiWarpTicks` | 60 | |  | The time in ticks (seconds x 20) that it takes for the user to warp into the Kamui dimension. |
| `kamuiCooldown` | 5 | |  | The cooldown of the Authority Of The Gods mode in seconds. |
| `kamuiCost` | 1,500 | |  | The magicule cost of the Authority Of The Gods mode. |

## `[Provider]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 85,000 | |  | Magicule Acquirement Cost. |
| `generosityHaloCost` | 1,000 | |  | The initial magicule cost of Provider's Generosity Halo when it is summoned. |
| `generosityHaloCostSecond` | 500 | |  | The magicule cost of Provider's Generosity Halo every subsequent second it is summoned. |
| `generosityHaloLifespan` | 72,000 | |  | The lifespan of the Generosity Halo entity in ticks. |
| `generosityBoost` | 3 | |  | The damage multiplier that all projectiles receive when passing through Provider's Generosity Halo. |
| `generosityEntityDamageBoost` | 3 | |  | The damage multiplier that all entities receive when gaining the Provider Boost effect from passing through Provider's Generosity Halo. |
| `generosityEntitySpeedBoost` | 3 | |  | The speed multiplier that all entities receive when gaining the Provider Boost effect from passing through Provider's Generosity Halo. |
| `generosityEntityStepHeightBoost` | 3 | |  | The step height that all entities receive when gaining the Provider Boost effect from passing through Provider's Generosity Halo. |
| `generosityCooldown` | 5 | |  | The cooldown for the Generosity mode in seconds. |
| `generosityCooldownMastery` | 5 | |  | The cooldown for the Generosity mode in seconds when the skill is mastered.. |
| `payItForwardCooldown` | 300 | |  | The cooldown of the Pay It Forward mode in seconds. |
| `payItForwardCooldownMastered` | 300 | |  | The cooldown of the Pay It Forward mode in seconds when the skill is mastered. |
| `payItForwardCost` | 1,500 | |  | The magicule cost to turn on Provider's Pay It Forward mode. |
| `payItForwardCostTicking` | 750 | |  | The magicule cost of Provider's Pay It Forward mode every subsequent second it is toggled. |
| `contributionsTier1` | 1,000 | |  | The following values are the contributions required to reach the next tier. |
| `contributionsTier2` | 2,500 | |  |  |
| `contributionsTier3` | 5,000 | |  |  |
| `contributionsTier4` | 25,000 | |  |  |
| `contributionsTier5` | 100,000 | |  |  |

## `[Reducer]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquisition` | 90,000 | |  | Magicule Acquirement Cost. |
| `purificationReduction` | 0.5 | |  | The percentage of energy cost reduction you receive when Reducer is toggled on. |
| `purificationReductionMastered` | 0.33 | |  | The percentage of energy cost reduction you receive when Reducer is toggled on, when the skill is mastered. |
| `magiculeRegenerationMultiplierBuff` | 9 | |  | The ADDITIONAL multiplier (base 1) of magicule regeneration you receive when Reducer is in slot. |
| `auraRegenerationMultiplierBuff` | 9 | |  | The ADDITIONAL multiplier (base 1) of aura regeneration you receive when Reducer is in slot. |
| `emancipationCost` | 2,000 | |  | The magicule cost to toggle on the Emancipation mode. |
| `emancipationMaintainCost` | 300 | |  | The magicule cost to maintain the Emancipation mode. |
| `emancipationMultiplier` | 1.75 | |  | The multiplier of Holy Damage the user will deal when Emancipation is toggled on. |
| `purityEdgeCost` | 10,000 | |  | The magicule cost of the Purity Edge mode. |
| `purityEdgeDamagePercentage` | 0.25 | |  | The percentage of health that will be drained from the target on connecting with Purity Edge. |
| `purityEdgeDamagePercentageMastered` | 0.5 | |  | The percentage of health that will be drained from the target on connecting with Purity Edge when the skill is mastered. |
| `purityEdgeRecoilTime` | 60 | |  | The time you have to connect a hit before suffering the recoil damage in ticks. |
| `purityEdgeRecoilTimeMastered` | 100 | |  | The time you have to connect a hit before suffering the recoil damage in ticks when the skill is mastered. |
| `purityEdgeCooldown` | 120 | |  | The cooldown of the Purity Edge mode in seconds. |
| `purityEdgeCooldownMastered` | 60 | |  | The cooldown of the Purity Edge mode in seconds when the skill is mastered. |
| `purityEdgeRecoil` | 0.75 | |  | The recoil of the Purity Edge mode if you do not land a hit in time. |
| `purityEdgeRecoilMastered` | 0.25 | |  | The recoil of the Purity Edge mode if you do not land a hit in time when the skill is mastered. |

## `[Repeater]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 75,000 | |  | Magicule Acquirement Cost |
| `recursionDepthTimer` | 100 | |  | How long should Recursion Depth last, in ticks (seconds x 20). |
| `recursionDepthCooldown` | 30 | |  | The cooldown of the Recursion Depth mode. |
| `recursionDepthCooldownMastered` | 15 | |  | The cooldown of the Recursion Depth mode when the skill is mastered. |

## `[Reshiram]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `epRequirement` | 100,000 | |  | EP Needed to Obtain. |
| `canAcquireWithOtherSkills` | true | |  | Should this skill be acquirable if you have [Zekrom] or [Kyurem]? |
| `blazeEssenceAmount` | 10 | |  | Amount of Blaze Essence needed to be consumed for acquisition. |
| `dragonEssenceAmount` | 10 | |  | Amount of Dragon Essence needed to be consumed for acquisition. |
| `mpAcquirement` | 64,300 | |  | Magicule Acquirement Cost. |
| `flameBoostAmount` | 1.5 | |  | The amount to boost Flame Damage by. |
| `blueFlareMPCost` | 800 | |  | MP Cost of Blue Flare. |
| `blueFlareDamage` | 60 | |  | Damage of Blue Flare. |
| `blueFlareRadius` | 20 | |  | Radius of Blue Flare. |
| `blueFlareCooldown` | 10 | |  | Cooldown of Blue Flare. |
| `blueFlareCooldownMastered` | 5 | |  | Cooldown of Blue Flare when Mastered. |
| `fusionFlareMPCost` | 700 | |  | MP Cost of Fusion Flare. |
| `fusionFlareZekromMPCostBoost` | 2 | |  | MP Cost of Fusion Flare with Zekrom boosted from Original Cost. |
| `fusionFlareDamage` | 200 | |  | Damage of Fusion Flare. |
| `fusionFlareRadius` | 5 | |  | Radius of Fusion Flare. |
| `fusionFlareZekromBonus` | 40 | |  | Damage of Fusion Flare Zekrom Bonus |
| `fusionFlareCooldown` | 20 | |  | Cooldown of Fusion Flare. |
| `draconicMeteorMPCost` | 1,000 | |  | MP Cost of Draconic Meteor. |
| `draconicMeteorDamage` | 70 | |  | Damage of Draconic Meteor. |
| `draconicMeteorExplosionRadius` | 10 | |  | Explosion Radius of Draconic Meteor. |
| `draconicMeteorKnockbackForce` | 5 | |  | Knockback Force of Draconic Meteor. |
| `draconicMeteorCooldown` | 20 | |  | Cooldown of Draconic Meteor. |
| `flamethrowerMPCost` | 400 | |  | MP Cost of Flamethrower. |
| `flamethrowerDamage` | 30 | |  | Damage of Flamethrower. |
| `flamethrowerCooldown` | 10 | |  | Cooldown of Flamethrower. |

## `[Restricted]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 20,000 | |  | Magicule Acquirement Cost. |
| `battlewillMultiplier` | 5 | |  | Damage multiplier of Battlewills. |
| `physicalAttackMultiplier` | 3 | |  | Damage multiplier of Physical Attacks. |
| `maximumStatBoost` | 2 | |  | Maximum additional multiplier that your stats can be boosted to depending on the skill's mastery. |
| `maximumFlatStatBoost` | 20 | |  | Maximum additional flat boost that your armor stat can be boosted to depending on the skill's mastery. |
| `decimateDistance` | 12 | |  | The distance traveled when performing an attack using Decimate. |
| `decimateDistanceMastered` | 16 | |  | The distance traveled when performing an attack using Decimate when the skill is mastered. |
| `decimateDamage` | 25 | |  | The amount of bonus damage dealt when performing an attack using Decimate. |
| `decimateDamageMastered` | 75 | |  | The amount of bonus damage dealt when performing an attack using Decimate when the skill is mastered. |
| `counterStateDuration` | 60 | |  | The duration that your Counter state lasts in ticks (seconds x 20). |
| `counterStateDurationMastered` | 100 | |  | The duration that your Counter state lasts in ticks (seconds x 20) when the skill is mastered. |
| `counterImbalanceDuration` | 100 | |  | The duration that enemies become Imbalanced for when striking you while you are Countering. |
| `counterImbalanceDurationMastered` | 100 | |  | The duration that enemies become Imbalanced for when striking you while you are Countering, when the skill is mastered. |
| `counterCooldown` | 15 | |  | The cooldown of the Counter mode in seconds. |
| `counterCooldownMastered` | 15 | |  | The cooldown of the Counter mode in seconds when the skill is mastered. |

## `[Saint]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 75,000 | |  | Magicule Acquirement Cost. |
| `compassionCost` | 10,000 | |  | The Magicule cost of the Compassion passive. |

## `[Scholar]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 35,000 | |  | Magicule Acquirement Cost. |
| `learningPoint` | 6 | |  | The bonus number of learning point to gain when toggled. |
| `masteryPoint` | 6 | |  | The bonus number of mastery point to gain when toggled. |
| `studyChance` | 20 | |  | The chance to study the opponent when they attack you. |
| `studyDodgeBase` | 0 | |  | The base dodge chance without studying the opponent. |
| `studyDodgePerPoint` | 1 | |  | The study points that translate into dodge chance you gain towards that entity type whenever you successfully study them. |
| `studyDodgePlayerMax` | 50 | |  | The maximum amount of dodge chance you can gain against players. |
| `studyDodgePlayerMaxMastered` | 70 | |  | The maximum amount of dodge chance you can gain against players when the skill is mastered. |
| `studyDodgeEntityMax` | 75 | |  | The maximum amount of dodge chance you can gain against a specific entity type. |
| `studyDodgeEntityMaxMastered` | 100 | |  | The maximum amount of dodge chance you can gain against a specific entity type when the skill is mastered. |
| `enchantmentBlacklist` | - | |  | Lists of enchantments that Scholar cannot learn or enchant. |
| `maxBonusBlacklist` | - | |  | Lists of enchantments that Scholar cannot learn or enchant above the enchantment's maximum level. |
| `maxBonusLevel` | 5 | |  | The maximum bonus of level that the player can increase. |

## `[Schrodinger]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `poisonEffectDuration` | 160 | |  | The duration in tick of the poison effect on target when touching them. |

## `[Spiritualist]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 80,000 | |  | Magicule Acquirement Cost. |
| `summonScytheCost` | 500 | |  | Magicule cost of the Summon Scythe mode. |
| `carveCost` | 500 | |  | Magicule cost of the Carve mode. |
| `enhanceCost` | 1,500 | |  | Magicule cost of the Enhance mode. |
| `carveRange` | 5 | |  | The Range of the Carve mode. |
| `chantSpeed` | 2 | |  | The chant speed multiplier when toggled. |

## `[Stagnator]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 50,000 | |  | Magicule Acquirement Cost. |
| `stagnateAuraCost` | 250 | |  | The magicule cost of the Stagnate Aura mode, taken every 10 ticks. |
| `stagnateAuraRadius` | 25 | |  | The radius in blocks of the Stagnate Aura mode. |
| `stagnateAuraCooldown` | 5 | |  | The cooldown of the Stagnate Aura mode in seconds. |
| `stagnateAuraCooldownMastered` | 3 | |  | The cooldown of the Stagnate Aura mode in seconds, when the skill is mastered. |
| `inactionCost` | 50 | |  | The Magicule cost of the Inaction mode, taken every 10 ticks. |
| `inactionCooldown` | 5 | |  | The cooldown of the Inaction mode in seconds. |
| `inactionCooldownMastered` | 3 | |  | The cooldown of the Inaction mode in seconds, when the skill is mastered. |
| `stasisShotCost` | 1,000 | |  | The Magicule Cost of the Stasis Shot mode. |
| `stasisShotDamage` | 50 | |  | The Damage of Stasis Shot projectile. |
| `stasisShotMasteredDamage` | 100 | |  | The Damage of Stasis Shot Projectile when Mastered |
| `stasisShotCooldown` | 10 | |  | The cooldown of Stasis Shot Mode in seconds. |
| `stasisShotCooldownMastered` | 5 | |  | The cooldown of Stasis Shot Mode in seconds, when the skill is mastered. |

## `[Subjugator]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 95,000 | |  | Magicule Acquirement Cost. |
| `unbreakableDefenseStep` | 2,000 | |  | The step in loyalty points that is accounted for whenever the user is to gain more damage reduction from the passive. |
| `unbreakableDefenseGain` | 0.02 | |  | The percentage of damage reduction you gain every time you gain a multiple of the above value. (Please do it in decimal notation and not percentage notation.) |
| `loyaltyRange` | 8 | |  | The range of the Undying Loyalty passive in blocks. |
| `loyaltyPointGain` | 2 | |  | The amount of loyalty points gained from nearby subordinates every five seconds. |
| `loyaltyRangeMastery` | 16 | |  | The range of the Undying Loyalty passive in blocks when the skill is mastered. |
| `loyaltyPointGainMastery` | 4 | |  | The amount of loyalty points gained from nearby subordinates every five seconds when the skill is mastered. |
| `loyaltyResistance` | 1 | |  | The resistance level granted to subordinates in your vicinity. |
| `loyaltyResistanceMastered` | 2 | |  | The resistance level granted to subordinates in your vicinity when the skill is mastered. |
| `inspirationLevel` | 1 | |  | The level of inspiration granted to subordinates when changing their movement mode. |
| `inspirationDuration` | 30 | |  | The duration of the inspiration effect bestowed onto subordinates when changing their movement mode, in seconds. |
| `inspirationLevelMastery` | 2 | |  | The level of inspiration granted to subordinates when changing their movement mode when the skill is mastered. |
| `inspirationDurationMastery` | 60 | |  | The duration of the inspiration effect bestowed onto subordinates when changing their movement mode when the skill is mastered, in seconds. |
| `maximumTotalLoyaltyPoints` | 50,000 | |  | The maximum gainable loyalty points that will cap out the user's Damage Reduction. |
| `takeoverDistance` | 5 | |  | The distance in blocks that Takeover can be used from. |
| `takeoverDistanceMastery` | 10 | |  | The distance in blocks that Takeover can be used from when the skill is mastered. |
| `takeoverEPMultiplierRequirement` | 1 | |  | The multiplier of EP the player needs to meet in order to convert the target. |
| `takeoverEPMultiplierRequirementMastered` | 2 | |  | The multiplier of EP the player needs to meet in order to convert the target. |
| `takeoverCooldown` | 300 | |  | The cooldown of the Takeover mode in seconds. |
| `takeoverCooldownMastered` | 120 | |  | The cooldown of the Takeover mode in seconds when the skill is mastered. |
| `casualConversationChance` | 0.02 | |  | The chance that a conversation is started every 5 seconds. |
| `allyRadius` | 20 | |  | The radius in block to apply skill effect on Allies. |
| `baseMaxEPForMindControl` | 600,000 | |  | The base max amount of EP that the target can have for Takeover can work |

## `[TheBalance]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 35,000 | |  | Magicule Acquirement Cost. |
| `magiculeCost` | 500 | |  | Flat magicule cost per activation. |
| `range` | 8 | |  | Targeting range in blocks for TheBalance activation. |
| `heavyDamage` | 10,000 | |  | Damage dealt when points are at or under the threshold. |
| `perPointDamage` | 1,000 | |  | Damage per MisfortunePoint when points exceed the threshold. |
| `thresholdPoints` | 10 | |  | Threshold of MisfortunePoint used by TheBalance. |

## `[VictoriousHarbinger]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 80,000 | |  | Magicule Acquirement Cost. |
| `mightCost` | 2,000 | |  | The magicule cost of the Might mode, taken every 10 ticks. |
| `mightCooldown` | 40 | |  | The Cooldown of the Might mode |
| `tenaciousResolveCost` | 500 | |  | The Magicule cost of the Tenacious Resolve mode |
| `effectLevel` | 1 | |  | The Level of effect to reduce by |
| `immunityList` | "new ArrayList&lt;&gt;()" | |  | List of effects the holder of this skill is immune to |

## `[Zekrom]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `epRequirement` | 100,000 | |  | EP Needed to Obtain. |
| `canAcquireWithOtherSkills` | true | |  | Should this skill be acquirable if you have [Reshiram] or [Kyurem]? |
| `dragonEssenceAmount` | 10 | |  | Amount of Dragon Essence needed to be consumed for acquisition. |
| `lightningEssenceAmount` | 10 | |  | Amount of Lightning Strikes needed to be consumed for acquisition. |
| `mpAcquirement` | 64,400 | |  | Magicule Acquirement Cost. |
| `lightningBoostAmount` | 1.5 | |  | Amount to boost Lightning Damage by. |
| `boltStrikeMPCost` | 800 | |  | MP Cost of Bolt Strike Mode. |
| `boltStrikeDamage` | 150 | |  | Damage of Bolt Strike Mode. |
| `boltStrikeRadius` | 7.5 | |  | Radius of Bolt Strike Mode.. |
| `boltStrikeAdditionalVisual` | 8 | |  | Additional Visual of Bolt Strike. |
| `boltStrikeCooldown` | 20 | |  | Cooldown of Bolt Strike Mode. |
| `boltStrikeCooldownMastered` | 10 | |  | Cooldown of Bolt Strike Mode when Mastered. |
| `fusionBoltMPCost` | 800 | |  | MP Cost of Fusion Bolt Mode. |
| `fusionBoltDamage` | 60 | |  | Damage of Fusion Bolt Mode. |
| `fusionBoltReshiramBonus` | 40 | |  | Bonus Damage if Reshiram in slot. |
| `fusionboltReshiramMPCost` | 2 | |  | MP Cost of Fusion Bolt Mode with Reshiram boosted from Original Cost. |
| `fusionBoltRange` | 15 | |  | Range of Fusion Bolt. |
| `fusionBoltFireDuration` | 5 | |  | Duration of Fire on Target in seconds. |
| `fusionBoltCooldown` | 20 | |  | Fusion Bolt Cooldown. |
| `draconicBreathMPCost` | 800 | |  | MP Cost of Draconic Breath Mode. |
| `draconicBreathDamage` | 60 | |  | Damage of Draconic Breath. |
| `draconicBreathCooldown` | 10 | |  | Cooldown of Draconic Breath Mode. |
| `thunderboltMPCost` | 1,000 | |  | MP Cost of Thunderbolt Mode. |
| `thunderboltDamage` | 100 | |  | Damage of Thunderbolt Mode. |
| `thunderboltRange` | 30 | |  | Range of Thunderbolt in blocks. |

## `[Gatekeeper]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 85,000 | |  | Magicule Acquirement Cost. |
| `enkiduRange` | 10 | |  | The range in blocks of the Enkidu mode. |
| `enkiduCost` | 25,000 | |  | The magicule cost of the Enkidu mode. |
| `enkiduDuration` | 120 | |  | The duration in seconds of the Enkidu mode. |
| `enkiduDurationMastered` | 240 | |  | The duration in seconds of the Enkidu mode when Gatekeeper is mastered. |
| `enkiduCooldown` | 20 | |  | The cooldown of the Enkidu mode in seconds. |
| `babylonCost` | 25,000 | |  | The initial magicule cost of the Gate of Babylon mode. |
| `babylonContinousCost` | 25,000 | |  | The continuous magicule cost of the Gate of Babylon mode. |
