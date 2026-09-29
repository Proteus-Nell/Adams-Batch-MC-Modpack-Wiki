# `config/tensuramoreskills-races.toml`

<small>[TensuraMoreSkills](../index.md) &rsaquo; [Configs](index.md)</small>

## Top level

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | If true, Crimson Progenitors can use Black Communion. |
| `maxMastery` | 1,000 | 1 to no limit | Maximum mastery for Black Communion. |
| `maxMastery` | 1,000 | 1 to no limit | Maximum mastery for Blood Arts. |

## `[activation]`

| Option | Default | Range | Description |
|---|---|---|---|
| `activationBloodCost` | 140 | 0 to no limit | Blood cost paid by the Crimson Progenitor when the communion starts. |
| `duration` | 2,400 | 20 to no limit | Maximum active duration in ticks. 2400 ticks = 2 minutes. |
| `pulseInterval` | 40 | 1 to no limit | How often the network pulses. 40 ticks = 2 seconds. |
| `collapseCooldown` | 90 | 0 to no limit | Cooldown in seconds after manually collapsing Black Communion. |

## `[radius]`

| Option | Default | Range | Description |
|---|---|---|---|
| `baseRadius` | 24 | 1 to 512 | Starting ritual radius. |
| `maxRadius` | 96 | 1 to 512 | Maximum ritual radius after power scaling. |
| `radiusPerPower` | 0.08 | 0 to 16 | Radius gained per stored communion power. |

## `[power]`

| Option | Default | Range | Description |
|---|---|---|---|
| `maxPower` | 800 | 1 to no limit | Maximum stored communion power. |
| `bloodfiendWeight` | 1 | 0 to 1,024 | Power weight for Bloodfiend participants. |
| `elderBloodfiendWeight` | 2 | 0 to 1,024 | Power weight for Elder Bloodfiend participants. |
| `bloodNobleWeight` | 4 | 0 to 1,024 | Power weight for Blood Noble participants. |
| `bloodMonarchWeight` | 7 | 0 to 1,024 | Power weight for Blood Monarch participants. |
| `crimsonProgenitorWeight` | 12 | 0 to 1,024 | Power weight for Crimson Progenitor participants. |
| `generationContributionPenalty` | 0.04 | 0 to 1 | Power contribution penalty per generation after generation 1. |
| `minGenerationContribution` | 0.45 | 0 to 1 | Minimum generation contribution multiplier. |
| `emptyBloodContribution` | 0.25 | 0 to 1,024 | Minimum contribution even if a linked Bloodfiend is low on blood. |
| `fullBloodContribution` | 1 | 0 to 1,024 | Contribution added based on stored blood ratio. |
| `bloodDrainedPowerMultiplier` | 0.0008 | 0 to 1,024 | Extra power per total blood drained by the participant. |
| `thrallPowerMultiplier` | 0.08 | 0 to 1,024 | Extra power per total thrall turned by the participant. |
| `maxProgressContribution` | 10 | 0 to 1,024 | Maximum extra power from progress stats per participant per pulse. |
| `powerGainMultiplier` | 0.08 | 0 to 1,024 | Final multiplier for communion power gained per pulse. |
| `nodeOfferingBloodCost` | 0.35 | 0 to 1,024 | Blood paid per participant weight each pulse. |

## `[shared_bloodline]`

| Option | Default | Range | Description |
|---|---|---|---|
| `sharedBloodTransferPerPulse` | 6 | 0 to no limit | Blood moved from high-blood nodes to low-blood nodes per pulse. |
| `sharedBloodLowRatio` | 0.35 | 0 to 1 | A linked Bloodfiend below this blood ratio can receive shared blood. |
| `sharedBloodDonorMinRatio` | 0.45 | 0 to 1 | A linked Bloodfiend must stay above this blood ratio to donate shared blood. |
| `progenitorBloodGainPerPulse` | 4 | 0 to no limit | Blood gained by the Progenitor every pulse. |
| `linkedBloodGainPerPulse` | 2 | 0 to no limit | Blood gained by every linked Bloodfiend every pulse. |
| `linkedHealPerPulse` | 2,000 | 0 to no limit | Health restored to every linked Bloodfiend every pulse. |
| `linkedSpiritualRestorePerPulse` | 6,000 | 0 to no limit | Spiritual health restored to every linked Bloodfiend every pulse. |
| `linkedMagiculeRestorePerPulse` | 120,000 | 0 to no limit | Magicules restored to every linked Bloodfiend every pulse. |

## `[combat]`

| Option | Default | Range | Description |
|---|---|---|---|
| `baseDamageReduction` | 0.1 | 0 to 1 | Base damage reduction for linked Bloodfiends. |
| `damageReductionPerPower` | 0.0008 | 0 to 1 | Extra damage reduction per communion power. |
| `maxDamageReduction` | 0.75 | 0 to 1 | Maximum damage reduction for linked Bloodfiends. |
| `damageBoostPerPower` | 0.0009 | 0 to 1,024 | Damage boost per communion power for linked Bloodfiends. |
| `maxDamageBoost` | 1.5 | 0 to 1,024 | Maximum damage boost from communion power. |

## `[infection]`

| Option | Default | Range | Description |
|---|---|---|---|
| `infectionStacksPerPulse` | 1 | 0 to no limit | Black infection stacks applied to enemies per pulse. |
| `maxInfectionStacks` | 12 | 1 to no limit | Maximum black infection stacks. |
| `infectionDuration` | 500 | 1 to no limit | Black infection duration in ticks. |
| `infectionBrandDuration` | 160 | 1 to no limit | Blood Brand duration applied by black infection. |
| `infectionDamageInterval` | 60 | 1 to no limit | How often infection deals damage. |
| `infectionPulseDamage` | 0.75 | 0 to no limit | Damage per infection stack per infection pulse. |
| `infectionMaxPulseDamage` | 45 | 0 to no limit | Maximum infection pulse damage. |
| `infectionBloodLeak` | 1 | 0 to no limit | Blood gained by linked Bloodfiends per infection stack per pulse. |
| `infectionHealLeak` | 0.25 | 0 to no limit | Healing gained by linked Bloodfiends per infection stack per pulse. |
| `infectionDamageBoostPerStack` | 0.035 | 0 to 1,024 | Extra damage linked Bloodfiends deal per infection stack on the target. |
| `maxInfectionDamageBoost` | 1.2 | 0 to 1,024 | Maximum damage boost from infection stacks. |
| `skipBloodlessInfection` | true |  | If true, black infection ignores bloodless entities. |
| `deathSpreadRadius` | 10 | 0 to 128 | Radius where infection spreads when an infected target dies. |
| `killBloodGain` | 8 | 0 to no limit | Blood gained by linked Bloodfiends when infected enemies die. |
| `killHeal` | 4 | 0 to no limit | Healing gained by linked Bloodfiends when infected enemies die. |
| `killPowerGain` | 8 | 0 to no limit | Communion power gained when infected enemies die. |

## `[death_prevention]`

| Option | Default | Range | Description |
|---|---|---|---|
| `preventDeathBloodCost` | 80 | 1 to no limit | Total shared network blood cost to prevent a linked Bloodfiend death. |
| `preventDeathHealthRatio` | 0.18 | 0.01 to 1 | Health ratio restored when death is prevented. |
| `preventDeathInvulnerabilityTicks` | 80 | 0 to no limit | Invulnerability ticks after death prevention. |
| `preventDeathCooldownTicks` | 120 | 0 to no limit | Cooldown ticks before the network can prevent another death. |
| `preventDeathSpiritualRestore` | 250 | 0 to no limit | Spiritual health restored on death prevention. |
| `preventDeathMagiculeRestore` | 500,000 | 0 to no limit | Magicules restored on death prevention. |
| `preventDeathInfectionRadius` | 12 | 0 to 128 | Black infection burst radius when death is prevented. |
| `preventDeathInfectionStacks` | 3 | 0 to no limit | Infection stacks applied by death prevention burst. |

## `[collapse]`

| Option | Default | Range | Description |
|---|---|---|---|
| `collapseBaseDamage` | 1,000 | 0 to no limit | Base damage dealt by Black Eucharist collapse. |
| `collapseDamagePerPower` | 0.32 | 0 to no limit | Extra collapse damage per communion power. |
| `collapseMaxDamage` | 35,000 | 0 to no limit | Maximum collapse damage. |
| `collapseHeal` | 60,000 | 0 to no limit | Health restored to linked Bloodfiends on collapse. |
| `collapseSpiritualHeal` | 1,200,000 | 0 to no limit | Spiritual health restored to linked Bloodfiends on collapse. |
| `collapseMagiculeRestore` | 2,500,000 | 0 to no limit | Magicules restored to linked Bloodfiends on collapse. |
| `collapseBloodRestore` | 120 | 0 to no limit | Blood restored to linked Bloodfiends on collapse. |
| `collapseBrandDuration` | 700 | 1 to no limit | Blood Brand duration applied during collapse. |
| `collapseMobTurnHealthThreshold` | 0.25 | 0 to 1 | Infected mobs below this health ratio can be turned by collapse. |

## `[black_blood_domain]`

| Option | Default | Range | Description |
|---|---|---|---|
| `blockInfectionEnabled` | false |  | If true, Black Communion can infect blocks and create Black Blood Domains. |
| `blockInfectionAttempts` | 96 | 0 to no limit | Random block infection attempts per active communion pulse. |
| `blockInfectionBlocksPerPulse` | 14 | 0 to no limit | Fast spread blocks per communion pulse before power scaling. |
| `blockInfectionMaxBlocksPerPulse` | 42 | 0 to no limit | Maximum blocks infected by the progenitor per communion pulse. |
| `blockInfectionBlocksPerPower` | 0.035 | 0 to 1,024 | Extra fast spread blocks per stored communion power. |
| `blockInfectionMaxRadius` | 72 | 1 to 512 | Maximum radius used by active communion block infection. |
| `blockInfectionVerticalRange` | 5 | 1 to 64 | Vertical random spread range for block infection. |
| `linkedBloodfiendsSpreadBlocks` | 2 | 0 to no limit | Extra block spread from each linked Bloodfiend during active communion. |
| `linkedBloodfiendSpreadAttempts` | 16 | 0 to no limit | Random spread attempts around each linked Bloodfiend. |
| `linkedBloodfiendSpreadRadius` | 18 | 1 to 512 | Spread radius around linked Bloodfiends. |
| `domainChunkValuePerBlock` | 1 | 0 to no limit | Virtual domain value added to a chunk per infected block. Buffs use this instead of scanning blocks. |
| `domainChunkValueSacrificeBonus` | 18 | 0 to no limit | Extra virtual domain value added to the altar chunk per blood sacrifice. |
| `domainChunkMaxValue` | 1,000 | 1 to no limit | Maximum virtual black blood domain value per chunk. |
| `domainBiomeChunkValueRequired` | 36 | 1 to no limit | Chunk value required for the area to count as a Black Blood Domain biome for buffs. |

## `[black_blood_domain_buffs]`

| Option | Default | Range | Description |
|---|---|---|---|
| `domainBiomeBuffsEnabled` | true |  | If true, Bloodfiends receive buffs in infected domain chunks. |
| `domainBiomeBuffInterval` | 80 | 1 to no limit | How often domain biome buffs pulse. 80 ticks = 4 seconds. |
| `domainBiomeBloodfiendHeal` | 250 | 0 to no limit | Health restored to Bloodfiends standing in infected domain chunks. |
| `domainBiomeBloodfiendSpiritualRestore` | 450 | 0 to no limit | Spiritual health restored to Bloodfiends in infected domain chunks. |
| `domainBiomeBloodfiendMagiculeRestore` | 900,000 | 0 to no limit | Magicules restored to Bloodfiends in infected domain chunks. |
| `domainBiomeBloodfiendBloodGain` | 3 | 0 to no limit | Blood gained by Bloodfiends in infected domain chunks. |
| `domainBiomeBloodfiendBloodGainPerAltarLevel` | 2 | 0 to no limit | Extra blood gained per nearby altar level. |
| `domainBiomeBuffPerAltarLevel` | 0.2 | 0 to 1,024 | Multiplier bonus per nearby altar level for domain healing/restoration. |
| `domainBiomeAltarLevelSearchRadius` | 96 | 1 to 512 | Radius used to find nearby altar level for stronger domain buffs. |
| `domainBiomeDamagesEnemies` | true |  | If true, non-Bloodfiends take light damage in infected domain chunks. |
| `domainBiomeEnemyDamage` | 80 | 0 to no limit | Light damage dealt to non-Bloodfiends in infected domain chunks per buff interval. |
| `domainBiomeKillBloodGain` | 2 | 0 to no limit | Fuel blood generated into the nearest Blood Altar when black blood domain biome damage kills a non-Bloodfiend. This also counts as lifetime altar blood. |

## `[blood_altar]`

| Option | Default | Range | Description |
|---|---|---|---|
| `bloodAltarEnabled` | true |  | If true, Black Communion can create Blood Altars. |
| `allowMultipleBloodAltars` | false |  | If false, only one Blood Altar can exist globally in this world for all Bloodfiends. If true, unlimited altars can exist. |
| `altarRequiredPower` | 25 | 0 to no limit | Communion power required before an altar can spawn. |
| `altarRequiredChunkValue` | 28 | 0 to no limit | Virtual domain chunk value required before an altar can spawn near the progenitor. |
| `altarSpawnSearchRadius` | 8 | 1 to 128 | Search radius for altar spawn positions around the progenitor. |
| `altarNoSpawnNearRadius` | 160 | 0 to no limit | Prevents a new altar from spawning this close to another altar. |
| `altarSacrificeEnabled` | true |  | If true, Bloodfiends can sacrifice blood into Blood Altars. |
| `altarFuelPerBlock` | 30 | 1 to no limit | Fuel blood consumed per infected block created by altar and vein-node spread. 30 means 30 stored blood = 1 infected block. |
| `altarMaxStoredBlood` | 10,000 | 1 to no limit | Maximum fuel blood inside a Blood Altar. |
| `altarMaxLevel` | 5 | 0 to 5 | Maximum Blood Altar level. |
| `altarLevel1Blood` | 1,000 | 0 to no limit | Stored blood required for altar level 1. |
| `altarLevel2Blood` | 2,500 | 0 to no limit | Stored blood required for altar level 2. |
| `altarLevel3Blood` | 5,000 | 0 to no limit | Stored blood required for altar level 3. |
| `altarLevel4Blood` | 7,500 | 0 to no limit | Stored blood required for altar level 4. |
| `altarLevel5Blood` | 10,000 | 0 to no limit | Stored blood required for altar level 5. |
| `altarPassiveSpreadEnabled` | true |  | If true, Blood Altars passively spread infection after communion ends. |
| `altarSpreadInterval` | 100 | 1 to no limit | Altar spread interval when the altar has at least level 1. |
| `altarSpreadAttempts` | 48 | 0 to no limit | Random spread attempts per altar passive spread pulse. |
| `altarSpreadBlocksPerPulse` | 3 | 0 to no limit | Blocks spread by a powered altar per passive pulse. |
| `altarSpreadBlocksPerLevel` | 2 | 0 to no limit | Extra altar passive spread blocks per altar level. |
| `altarBaseRadius` | 24 | 1 to 512 | Base altar spread and buff radius. |
| `altarRadiusPerLevel` | 4 | 0 to 512 | Extra altar radius per altar level. Level 1 makes the radius +4 by default. |
| `altarSacrificeBurstAttempts` | 128 | 0 to no limit | Random spread attempts immediately after a blood sacrifice. |
| `altarSacrificeBurstBlocks` | 18 | 0 to no limit | Blocks infected immediately after a blood sacrifice. |
| `altarSacrificeBurstBlocksPerLevel` | 10 | 0 to no limit | Extra sacrifice burst blocks per altar level. |
| `dormantSpreadInterval` | 1,200 | 1 to no limit | Very slow spread interval for a level 0 altar. 1200 ticks = 60 seconds. |
| `dormantSpreadBlocksPerPulse` | 1 | 0 to no limit | Very slow dormant spread blocks for an unpowered altar. |

## `[black_blood_conquest]`

| Option | Default | Range | Description |
|---|---|---|---|
| `conquestEnabled` | true |  | If true, Blood Altars can run the long-term world conquest system: player/base memory, World Roots, Blood Flower Blooms, and World Heart. |
| `conquestRequiredAltarLevel` | 5 | 0 to 5 | Minimum real Blood Altar level required before conquest ticks at all. This also disables player/base tracking unless a valid altar exists. |
| `conquestRequiredWorldStageForRoots` | 1 | 0 to no limit | Minimum world conquest stage required before new World Roots can start. Stage 1 is reached from a powerful altar, so roots do not begin immediately at fresh worlds. |
| `conquestPlayerMemoryInterval` | 200 | 20 to no limit | How often player/base memory samples run. 200 ticks = 10 seconds. |
| `conquestBaseScanRadius` | 10 | 1 to 64 | Sparse radius around sampled players used to score artificial/base blocks. |
| `conquestMemoryPruneTicks` | 864,000 | 1,200 to no limit | Old non-infected player/base chunk memory is removed after this many ticks. 864000 ticks = 12 hours. |
| `conquestMinPlayerHeatTarget` | 80 | 1 to no limit | Minimum long-term player presence score for a chunk to be targetable by roots. |
| `conquestMinBaseHeatTarget` | 140 | 1 to no limit | Minimum artificial/base block score for a chunk to count as a base-like root target. |
| `conquestMaxActiveRoots` | 10 | 0 to 256 | Maximum active underground World Roots before World Heart multiplier. |
| `conquestRequiredDomainLevel` | 5 | 0 to 100 | Minimum single Domain Level required before conquest ticks at all. |
| `conquestRequiredDomainLevelForRoots` | 5 | 0 to 100 | Minimum single Domain Level required before World Root tunnels start. |
| `conquestWorldHeartRequiredDomainLevel` | 10 | 1 to 100 | Single Domain Level required to form the World Heart. |
| `conquestRootMaxTargetDistanceBlocks` | 8,192 | 16 to 30,000,000 | Maximum distance a World Root tunnel may target. 8192 allows thousands of blocks without force-loading chunks. |
| `conquestRootBlocksPerTick` | 100 | 1 to 256 | How many tunnel blocks each active World Root may grow per root tick. Higher means thousand-block targets are reached faster. |
| `conquestMaxRootsProcessedPerTick` | 8 | 1 to 256 | Hard budget for active roots processed per root tick. |
| `conquestRootTickInterval` | 10 | 1 to no limit | How often roots move. 40 ticks = 2 seconds. |
| `conquestRootStartCost` | 180 | 0 to no limit | Blood Altar fuel cost to start one World Root. |
| `conquestRootStepCost` | 35 | 0 to no limit | Blood Altar fuel cost per World Root step. |
| `conquestRootMaxAge` | 72,000 | 20 to no limit | Maximum root age in root ticks before it dies. |
| `conquestRootReachDistanceChunks` | 1 | 0 to 64 | Root completes when it reaches this chunk distance from its target. |
| `conquestBloomTickInterval` | 100 | 1 to no limit | How often Blood Flower Blooms tick. 100 ticks = 5 seconds. |
| `conquestBloomStartBlood` | 2,500 | 0 to no limit | Stored conquest blood given to normal blooms when they spawn. |
| `conquestBaseBloomBloodMultiplier` | 3 | 1 to no limit | Multiplier for starting blood when a bloom erupts from a player-base target. |
| `conquestBloomMaxStoredBlood` | 250,000 | 1 to no limit | Maximum stored conquest blood inside one Blood Flower Bloom. |
| `conquestBloomFeedInterval` | 200 | 1 to no limit | Bloom age interval used to feed stored blood to the main altar. |
| `conquestBloomFeedAmount` | 750 | 0 to no limit | Blood sent from a bloom to the main altar per feed interval, multiplied by bloom tier. |
| `conquestBloomSpreadBlocks` | 45 | 0 to no limit | Block spread budget for normal bloom spread pulses. |
| `conquestBloomBurstSpreadBlocks` | 140 | 0 to no limit | Initial infection burst blocks for normal Bloom creation. |
| `conquestBaseBloomBurstSpreadBlocks` | 260 | 0 to no limit | Initial infection burst blocks for base-breach Bloom creation. |
| `conquestBloomDrainMaxBlood` | 2,500 | 1 to no limit | Max stored bloom blood a Bloodfiend can drain per interaction. |
| `conquestBloomGrowthDivisor` | 250 | 1 to no limit | Bloom blood divided by this becomes permanent Black Blood Growth. |
| `conquestBloomBloodDivisor` | 100 | 1 to no limit | Bloom blood divided by this becomes normal stored Bloodfiend blood. |
| `conquestBloomHealMultiplier` | 0.05 | 0 to no limit | Health restored per drained bloom blood. |
| `conquestBloomSpiritualMultiplier` | 0.25 | 0 to no limit | Spiritual health restored per drained bloom blood. |
| `conquestBloomMagiculeMultiplier` | 150 | 0 to no limit | Magicules restored per drained bloom blood. |
| `conquestHeartTickInterval` | 200 | 1 to no limit | How often the World Heart ticks. 200 ticks = 10 seconds. |
| `conquestWorldHeartStage` | 6 | 1 to no limit | World conquest stage number used for the final World Heart state. |
| `conquestWorldHeartSpreadBlocks` | 180 | 0 to no limit | Block spread budget for each World Heart pulse. |
| `conquestWorldHeartMinGrowth` | 100 | 0 to no limit | Minimum permanent growth gained from drinking the active World Heart. |
| `conquestWorldHeartHealMultiplier` | 12 | 0 to no limit | Health restored per World Heart growth point. |
| `conquestWorldHeartSpiritualMultiplier` | 85 | 0 to no limit | Spiritual health restored per World Heart growth point. |
| `conquestWorldHeartMagiculeMultiplier` | 75,000 | 0 to no limit | Magicules restored per World Heart growth point. |
| `conquestConqueredThreshold` | 1,800 | 1 to no limit | Infection pressure required for a chunk to count as conquered. |
| `conquestBlockBreakPressure` | 25 | 0 to no limit | Infection pressure added when a conquest/infected block is broken while conquest is active. |
| `conquestStage1RequiredAltarLevel` | 3 | 0 to 5 | Stage 1 requirement: minimum active altar level. |
| `conquestStage1RequiredTotalBlood` | 20,000 | 0 to no limit | Stage 1 requirement: lifetime blood in the best active altar. |
| `conquestStage2RequiredBlooms` | 3 | 0 to no limit | Stage 2 requirement: created blooms. |
| `conquestStage2RequiredCompletedRoots` | 2 | 0 to no limit | Stage 2 requirement: completed roots. |
| `conquestStage3RequiredBlooms` | 8 | 0 to no limit | Stage 3 requirement: created blooms. |
| `conquestStage3RequiredBaseBreaches` | 1 | 0 to no limit | Stage 3 requirement: base breaches. |
| `conquestStage3RequiredConqueredChunks` | 12 | 0 to no limit | Stage 3 requirement: conquered chunks. |
| `conquestStage4RequiredBlooms` | 14 | 0 to no limit | Stage 4 requirement: created blooms. |
| `conquestStage4RequiredBaseBreaches` | 3 | 0 to no limit | Stage 4 requirement: base breaches. |
| `conquestStage4RequiredConqueredChunks` | 35 | 0 to no limit | Stage 4 requirement: conquered chunks. |
| `conquestStage5RequiredBlooms` | 20 | 0 to no limit | Stage 5 requirement: created blooms. |
| `conquestStage5RequiredBaseBreaches` | 4 | 0 to no limit | Stage 5 requirement: base breaches. |
| `conquestStage5RequiredCompletedRoots` | 14 | 0 to no limit | Stage 5 requirement: completed roots. |
| `conquestStage5RequiredConqueredChunks` | 60 | 0 to no limit | Stage 5 requirement: conquered chunks. |
| `conquestWorldHeartRequiredBlooms` | 24 | 0 to no limit | World Heart requirement: created blooms. |
| `conquestWorldHeartRequiredBaseBreaches` | 5 | 0 to no limit | World Heart requirement: base breaches. |
| `conquestWorldHeartRequiredConqueredChunks` | 80 | 0 to no limit | World Heart requirement: conquered chunks. |
| `conquestWorldHeartRequiredCompletedRoots` | 18 | 0 to no limit | World Heart requirement: completed roots. |
| `conquestGrowthHealthPerPoint` | 2 | 0 to no limit | Max health attribute gained per permanent Black Blood Growth point. |
| `conquestGrowthAttackPerPoint` | 0.35 | 0 to no limit | Attack damage attribute gained per permanent Black Blood Growth point. |
| `conquestGrowthSpeedPerPoint` | 0 | 0 to no limit | Movement speed attribute gained per permanent Black Blood Growth point. |
| `conquestGrowthMaxHealthCap` | 1,000,000 | 0 to no limit | Maximum max-health attribute gained from Black Blood Growth. |
| `conquestGrowthMaxAttackCap` | 250,000 | 0 to no limit | Maximum attack attribute gained from Black Blood Growth. |
| `conquestGrowthMaxSpeedCap` | 1.5 | 0 to no limit | Maximum movement-speed attribute gained from Black Blood Growth. |

## `[black_blood_conquest.black_blood_domain_level]`

| Option | Default | Range | Description |
|---|---|---|---|
| `domainMaxLevel` | 10 | 1 to 100 | Single visible Black Blood Domain level cap. Altar blood and conquest stats both feed this one system. |
| `domainLevel6Xp` | 25,000 | 0 to no limit | Domain XP required for level 6. |
| `domainLevel7Xp` | 60,000 | 0 to no limit | Domain XP required for level 7. |
| `domainLevel8Xp` | 150,000 | 0 to no limit | Domain XP required for level 8. |
| `domainLevel9Xp` | 350,000 | 0 to no limit | Domain XP required for level 9. |
| `domainLevel10Xp` | 900,000 | 0 to no limit | Domain XP required for level 10, the World Heart tier. |
| `domainXpPerBloom` | 10,000 | 0 to no limit | Domain XP gained per created Blood Flower Bloom. |
| `domainXpPerCompletedRoot` | 6,000 | 0 to no limit | Domain XP gained per completed World Root tunnel. |
| `domainXpPerBaseBreach` | 30,000 | 0 to no limit | Domain XP gained per player/base breach. |
| `domainXpPerConqueredChunk` | 450 | 0 to no limit | Domain XP gained per conquered chunk. |

## `[black_blood_conquest.black_blood_ecology]`

| Option | Default | Range | Description |
|---|---|---|---|
| `ecologyEnabled` | true |  | Enables the additive slow ecology, structures, converted mobs, fusion, and unloaded virtual frontier. |
| `ecologyMinimumWorldStage` | 2 | 1 to no limit | The stage needed for ecology to start. |
| `ecologyVirtualStepInterval` | 1,200 | 200 to no limit | Ticks between unloaded virtual conquest pulses. 1200 ticks is 1 minute. |
| `ecologyVirtualClaimSteps` | 4 | 2 to 127 | Paid virtual steps required to claim one unloaded chunk. |
| `ecologyVirtualStepBloodCost` | 50 | 1 to no limit | Altar fuel cost for one virtual conquest step. |
| `ecologyMaterializeInterval` | 200 | 100 to no limit | Ticks between checking naturally loaded player chunks for virtual infection materialization. |
| `ecologyBuildInterval` | 2,000 | 1,200 to no limit | Ticks between attempts to queue one autonomous infection structure. 6000 ticks is 5 minutes. |
| `ecologyTickInterval` | 200 | 40 to no limit | Base ecology structure processing interval. |
| `ecologyMaxStructures` | 150 | 1 to 512 | Maximum autonomous infection structures per dimension. |
| `ecologyBuildBloodCost` | 300 | 1 to no limit | Fuel blood reserved by a pending autonomous structure before it forms. |
| `ecologyStructureMinSpacing` | 48 | 16 to 512 | Minimum block spacing between autonomous structures. |
| `ecologySpireSpreadInterval` | 3,600 | 1,200 to no limit | Ticks between a Vein Spire adding a tiny normal loaded-chunk spread pulse. |
| `ecologySpireSpreadBlocks` | 1 | 1 to 2 | Normal infection blocks requested by each Vein Spire pulse. |
| `ecologyNestPulseInterval` | 2,400 | 1,200 to no limit | Ticks between Conversion Nest corruption pulses. |
| `ecologyNestRadius` | 14 | 6 to 64 | Loaded radius used by Conversion Nests. |
| `ecologyNestPulseDamage` | 1 | 0 to 1,000 | Very small damage dealt by a Conversion Nest while slowly corrupting a mob. |
| `ecologyCorruptionDecayTicks` | 2,400 | 400 to no limit | Corruption disappears after no converted-minion or nest contact for this long. |
| `ecologyConversionMarks` | 4 | 1 to 100 | Corruption marks required before a weakened mob can be converted. |
| `ecologyConversionHealthRatio` | 0.35 | 0.01 to 1 | Mob health ratio required for conversion. |
| `ecologyMinionCapPerNest` | 8 | 1 to 64 | Nearby converted mob cap supported by one nest. |
| `ecologyConversionBloodCost` | 45 | 1 to no limit | Structure or altar blood paid for each successful mob conversion. |
| `ecologyMinionThinkInterval` | 40 | 20 to 400 | Ticks between converted mob targeting and movement decisions. |
| `ecologyMinionTargetRadius` | 16 | 6 to 64 | Loaded targeting radius for converted mobs. |
| `ecologyMinionMoveSpeed` | 0.95 | 0.1 to 3 | Navigation speed used by converted mobs. |
| `ecologyMinionAttackInterval` | 30 | 20 to 400 | Ticks between handler-driven attacks from converted mobs. |
| `ecologyMinionDamage` | 10.5 | 0.1 to 1,000 | Base handler-driven magic damage from a tier 1 converted mob. |
| `ecologyFusionInterval` | 4,800 | 2,400 to no limit | Ticks between Fusion Pit attempts. 4800 ticks is 4 minutes. |
| `ecologyFusionRadius` | 10 | 6 to 32 | Loaded radius used by a Fusion Pit. |
| `ecologyFusionBloodCost` | 120 | 1 to no limit | Structure or altar blood spent when three equal-tier minions fuse. |
| `ecologyMaxFusionTier` | 8 | 2 to 8 | Maximum fusion tier. Tier 2 needs three tier 1 mobs and tier 3 needs three tier 2 mobs. |
| `ecologyReservoirFeedInterval` | 6,000 | 1,200 to no limit | Ticks between Blood Reservoir feed attempts. 6000 ticks is 5 minutes. |
| `ecologyReservoirFeedAmount` | 400 | 1 to no limit | Maximum blood a reservoir can forward per feed attempt. |
| `ecologyBloodCollectionRadius` | 96 | 32 to 512 | Radius used to route blood earned by converted mob kills into structures. |
| `ecologyStructureBloodCapacity` | 10,000 | 100 to no limit | Maximum kill-earned blood stored by one autonomous structure. |
| `ecologyBloodHealthDivisor` | 20 | 1 to no limit | Killed target max health divided by this becomes collected blood before the cap. |
| `ecologyMaxBloodPerKill` | 50 | 1 to no limit | Maximum structure blood earned from one converted mob kill. |
| `ecologyVirtualStepsPerPulse` | 2 | 1 to 16 | Base number of frontier entries processed per virtual pulse. Additional structures increase this up to a hard handler cap. |
| `ecologyMaxPendingBuilds` | 24 | 1 to 128 | Maximum persisted pending structures and remote altars waiting for fuel or a loaded valid site. |
| `ecologyPendingProcessInterval` | 200 | 40 to no limit | Ticks between attempts to complete pending builds. |
| `ecologyRemoteAltarsEnabled` | true |  | Allows the ecology to establish distant colony altars even when normal multiple altars are disabled. |
| `ecologyRemoteAltarMinDistance` | 400 | 128 to 30,000,000 | Minimum distance in blocks from every existing altar before a remote ecology altar may be queued. |
| `ecologyRemoteAltarRequiredChunkValue` | 120 | 1 to no limit | Required infected chunk value for a distant ecology altar site. |
| `ecologyRemoteAltarBloodCost` | 400 | 1 to no limit | Fuel blood required by a pending distant ecology altar. |
| `ecologyRemoteAltarSeedFuel` | 800 | 0 to no limit | Part of the remote altar cost transferred into the new altar as starting fuel. |
| `ecologyRemoteAltarAttemptEvery` | 4 | 1 to 64 | Every Nth five-minute build attempt prefers a distant ecology altar when a valid far infection site exists. |
| `ecologyWorldHeartRootCount` | 40 | 1 to 12 | Number of ecology World Roots maintained from infection nodes toward the current target. |
| `ecologyWorldHeartRootInterval` | 6,000 | 1,200 to no limit | Ticks between ecology attempts to queue or launch World Roots from the nearest infection source. |
| `ecologySummonerInterval` | 1,200 | 1,200 to no limit | Ticks between Summoner Bloom attempts. |
| `ecologySummonerBloodCost` | 20 | 1 to no limit | Structure or altar blood spent for one summoned blood minion. |
| `ecologySummonerCap` | 30 | 1 to 64 | Nearby converted minion cap supported by one Summoner Bloom. |
| `ecologyRelayInterval` | 2,400 | 600 to no limit | Ticks between Root Relay virtual expansion pulses. |
| `ecologyRelayBloodCost` | 60 | 1 to no limit | Blood spent by a Root Relay for one local virtual expansion pulse. |
| `ecologyRelaySteps` | 2 | 1 to 8 | Local frontier steps attempted by a Root Relay per paid pulse. |
| `ecologySanctuaryInterval` | 400 | 100 to no limit | Ticks between Blood Sanctuary healing pulses. |
| `ecologySanctuaryRadius` | 20 | 6 to 64 | Loaded healing radius of a Blood Sanctuary. |
| `ecologySanctuaryHeal` | 25 | 0 to no limit | Health restored to Bloodfiends and converted blood minions per Sanctuary pulse. |
| `ecologyHuntingBeaconInterval` | 600 | 100 to no limit | Ticks between Hunting Beacon target assignments. |
| `ecologyHuntingBeaconRadius` | 32 | 8 to 96 | Loaded radius used by Hunting Beacons to coordinate minions. |
| `ecologyFusionPowerPerConqueredChunk` | 3 | 0 to 1,000 | Internal infection power granted per conquered chunk before fusion scaling. |
| `ecologyFusionHealthPerPower` | 0.08 | 0 to 1,000 | Tier-scaled max-health multiplier gained per infection power. |
| `ecologyFusionAttackPerPower` | 0.012 | 0 to 1,000 | Tier-scaled attack multiplier gained per infection power. |
| `ecologyFusionMaxHealthMultiplier` | 250 | 0 to 100,000 | Maximum infection-based fused-minion max-health multiplier. 250 allows ordinary mobs to reach several thousand health late-game. |
| `ecologyFusionMaxAttackMultiplier` | 2,400 | 0 to 100,000 | Maximum infection-based fused-minion attack multiplier. |
| `ecologyFusionMaxArmor` | 800 | 0 to 100,000 | Maximum flat armor added to fused minions from infection strength. |

## `[kindred]`

| Option | Default | Range | Description |
|---|---|---|---|
| `defaultNaturalGeneration` | 1 | 1 to no limit | Generation assigned to naturally selected Bloodfiend players. Natural Bloodfiends should usually be generation 1. |
| `maxGeneration` | 12 | 1 to no limit | Maximum allowed kindred generation. |
| `bloodCapacityPenaltyPerGeneration` | 0.025 | 0 to 1 | Blood capacity penalty per generation after generation 1. |
| `bloodArtPenaltyPerGeneration` | 0.02 | 0 to 1 | Blood Arts power penalty per generation after generation 1. |
| `waterWeaknessPerGeneration` | 0.04 | 0 to 16 | Water weakness increase per generation after generation 1. |
| `minimumPowerMultiplier` | 0.55 | 0 to 1 | Minimum multiplier after generation penalties. |

## `[passive_regeneration]`

| Option | Default | Range | Description |
|---|---|---|---|
| `passiveInterval` | 240 | 1 to no limit | How often passive blood regeneration checks. 240 ticks = 12 seconds. Blood is only consumed if health, spiritual health, or magicules are missing. |
| `passiveBloodCost` | 1 | 0 to no limit | Blood consumed per passive regeneration pulse. |
| `passiveHeal` | 2 | 0 to no limit | Health healed per passive regeneration pulse. |
| `passiveSpiritualHeal` | 35 | 0 to no limit | Spiritual health restored per passive regeneration pulse. |
| `passiveMagiculeRestore` | 75 | 0 to no limit | Magicules restored per passive regeneration pulse. |

## `[water_weakness]`

| Option | Default | Range | Description |
|---|---|---|---|
| `waterCheckInterval` | 160 | 1 to no limit | How often water and rain weakness checks. 160 ticks = 8 seconds. |
| `waterBloodDrain` | 1 | 0 to no limit | Blood drained when touching water. |
| `rainBloodDrain` | 0 | 0 to no limit | Blood drained when standing in rain. |
| `waterDamage` | 0.75 | 0 to no limit | Damage dealt when touching water. |
| `rainDamage` | 0.1 | 0 to no limit | Damage dealt when standing in rain. |
| `waterMagiculeDrain` | 15 | 0 to no limit | Magicules drained when touching water. |

## `[blood_hunger]`

| Option | Default | Range | Description |
|---|---|---|---|
| `hungerInterval` | 300 | 1 to no limit | How often Bloodfiends convert stored blood into hunger. 300 ticks = 15 seconds. |
| `hungerBloodCost` | 1 | 0 to no limit | Blood consumed whenever hunger is restored. |
| `hungerFoodRestore` | 4 | 0 to 20 | Food points restored from blood. 2 food points = 1 hunger shank. |
| `hungerSaturationRestore` | 2 | 0 to 20 | Saturation restored from blood feeding. |
| `minimumFoodLevelFromBlood` | 18 | 0 to 20 | If the player has blood, their hunger is kept at least this high. |

## `[master_bond]`

| Option | Default | Range | Description |
|---|---|---|---|
| `masterBondInterval` | 200 | 1 to no limit | How often kindred with a living Bloodfiend master receive a bond pulse. |
| `masterBondBloodGain` | 1 | 0 to no limit | Blood gained by kindred near their living master. |
| `masterBondRange` | 32 | 0 to 512 | Range required for master bond blood pulse. |
| `masterBondBloodArtMultiplier` | 1.12 | 1 to 16 | Blood Arts power multiplier for kindred with a living Bloodfiend master. |
| `masterBondBloodCapacityMultiplier` | 1.15 | 1 to 16 | Max blood multiplier for kindred with a living Bloodfiend master. |
| `masterBondBloodCostMultiplier` | 0.75 | 0 to 1 | Blood cost multiplier for kindred with a living Bloodfiend master. |
| `masterBondWaterWeaknessMultiplier` | 0.75 | 0 to 1 | Water weakness multiplier for kindred with a living Bloodfiend master. |

## `[drain_blood]`

| Option | Default | Range | Description |
|---|---|---|---|
| `drainRange` | 10 | 0 to 128 | Target range for held Drain Blood. |
| `drainTickInterval` | 14 | 1 to 200 | How often held Drain Blood pulses. 14 ticks is a little slower than twice per second. |
| `drainPulseCooldown` | 0 | 0 to no limit | Tiny cooldown after each drain pulse. Usually keep this at 0 because the held interval already controls pacing. |
| `drainBloodGain` | 8 | 0 to no limit | Blood gained per Drain Blood pulse before generation modifiers. |
| `drainDamage` | 1 | 0 to no limit | Damage dealt per Drain Blood pulse. Kept low so Kindred Rite can be used before targets die. |
| `drainCooldown` | 0 | 0 to no limit | Unused legacy cooldown for older press-drain behavior. |
| `bloodBrandDrainMultiplier` | 3 | 1 to no limit | Drain Blood gain multiplier against Blood Branded targets. |
| `lowHealthDrainBonusThreshold` | 0.35 | 0 to 1 | Targets at or below this health ratio give bonus blood. |
| `lowHealthDrainBonusMultiplier` | 1.75 | 1 to 64 | Blood gain multiplier against low-health targets. |

## `[blood_surge]`

| Option | Default | Range | Description |
|---|---|---|---|
| `bloodSurgeCost` | 1 | 0 to no limit | Blood consumed by Blood Surge per cost interval while Blood Arts is toggled and damage is boosted. |
| `bloodSurgeCostInterval` | 40 | 1 to no limit | Minimum ticks between Blood Surge blood payments. 40 ticks = 2 seconds. |
| `bloodSurgeDamageMultiplier` | 0.45 | 0 to 1,024 | Damage multiplier added by Blood Surge. 0.45 means +45% before generation and master scaling. |

## `[crimson_guard]`

| Option | Default | Range | Description |
|---|---|---|---|
| `crimsonGuardCost` | 12 | 0 to no limit | Blood cost to activate Crimson Guard. |
| `crimsonGuardDuration` | 200 | 1 to no limit | Duration of Crimson Guard in ticks. |
| `crimsonGuardCooldown` | 10 | 0 to no limit | Cooldown for Crimson Guard in seconds. |
| `crimsonGuardHitBloodCost` | 1 | 0 to no limit | Extra blood consumed when Crimson Guard reduces incoming damage. |
| `crimsonGuardHitCostInterval` | 40 | 1 to no limit | Minimum ticks between Crimson Guard hit blood costs. 40 ticks = 2 seconds. |
| `crimsonGuardDamageTakenMultiplier` | 0.45 | 0 to 1 | Incoming damage multiplier while Crimson Guard is active. 0.45 means 55% reduction. |

## `[blood_brand]`

| Option | Default | Range | Description |
|---|---|---|---|
| `bloodBrandCost` | 8 | 0 to no limit | Blood cost to brand a target. |
| `bloodBrandDuration` | 600 | 1 to no limit | Duration of Blood Brand in ticks. |
| `bloodBrandCooldown` | 5 | 0 to no limit | Cooldown for Blood Brand in seconds. |

## `[kindred_rite]`

| Option | Default | Range | Description |
|---|---|---|---|
| `kindredRiteCost` | 90 | 0 to no limit | Blood cost to use Kindred Rite. |
| `kindredRiteCooldown` | 45 | 0 to no limit | Cooldown for Kindred Rite in seconds. |
| `kindredRiteRange` | 8 | 0 to 128 | Target range for Kindred Rite. |
| `mobTurnHealthThreshold` | 0.35 | 0 to 1 | Target mob must be at or below this health ratio to be turned unless EP ratio allows instant turning. |
| `playerTurnHealthThreshold` | 0.3 | 0 to 1 | Target player must be at or below this health ratio unless EP ratio allows instant turning. Consent is still required. |
| `instantTurnEpRatio` | 0.01 | 0 to 1 | If target EP is below this ratio of owner EP, Kindred Rite ignores the health threshold. 0.01 means below 1 percent. |
| `playerTurnConsentTicks` | 1,200 | 20 to no limit | Player turning consent window in ticks. The target must be prompted first, then sneak during a second Kindred Rite attempt. 1200 ticks = 60 seconds. |
| `kindredRiteSuccessBloodGain` | 35 | 0 to no limit | Blood gained by the owner after a successful Kindred Rite. |
| `maxActiveBloodThralls` | 6 | 0 to no limit | Maximum active blood thralls. |
| `allowMobTurning` | true |  | If true, Kindred Rite can turn weakened mobs. |
| `allowPlayerTurning` | true |  | If true, Kindred Rite can turn consenting weakened players into Bloodfiends. |

## `[evolution]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epRequirement` | 1,500,000 | 0 to no limit | EP required to evolve into this race. The base Bloodfiend value is unused for normal starting race selection. |
| `bossRequirement` | 0 | 0 to no limit | Boss kills required to evolve into this race. Set to 0 to disable this requirement. |
| `bloodRequirement` | 5,500 | 0 to no limit | Total blood drained required to evolve into this race. Set to 0 to disable this requirement. |
| `mobTurnRequirement` | 50 | 0 to no limit | Total mobs or players turned into kindred required to evolve into this race. Set to 0 to disable this requirement. |

## `[base_energy]`

| Option | Default | Range | Description |
|---|---|---|---|
| `minAura` | 700,000 | 0 to no limit | Minimum base aura for this race. |
| `maxAura` | 950,000 | 0 to no limit | Maximum base aura for this race. |
| `minMagicule` | 850,000 | 0 to no limit | Minimum base magicule for this race. |
| `maxMagicule` | 1,200,000 | 0 to no limit | Maximum base magicule for this race. |
| `minAura` | 100 | 0 to no limit |  |
| `maxAura` | 200 | 0 to no limit |  |
| `minMagicule` | 100 | 0 to no limit |  |
| `maxMagicule` | 200 | 0 to no limit |  |

## `[attributes]`

| Option | Default | Range | Description |
|---|---|---|---|
| `size` | 0.05 | -0.9 to 16 | Scale modifier for this race. 0 means normal size. |
| `maxHealth` | 700 | 0 to no limit | Max health bonus/value used by the race config. |
| `maxSpiritualHealth` | 5,000 | 0 to no limit | Max spiritual health bonus/value used by the race config. |
| `attack` | 6.5 | 0 to no limit | Attack damage bonus/value used by the race config. |
| `attackSpeed` | 0.42 | -1 to no limit | Attack speed modifier used by the race config. |
| `knockbackResistance` | 0.28 | 0 to 1 | Knockback resistance modifier used by the race config. |
| `movementSpeed` | 0.055 | -1 to no limit | Movement speed modifier used by the race config. |
| `swimSpeed` | -0.15 | -1 to no limit | Swim speed modifier. Negative values make Bloodfiends worse in water. |
| `size` | -0.9 | -0.9 to 16 |  |
| `maxHealth` | 5 | -1,024 to no limit |  |
| `maxSpiritualHealth` | 5 | 0 to no limit |  |
| `attack` | 0 | 0 to no limit |  |
| `attackSpeed` | 0 | -1 to no limit |  |
| `knockbackResistance` | 0 | 0 to 1 |  |
| `movementSpeed` | 0 | -1 to no limit |  |
| `swimSpeed` | 0 | -1 to no limit |  |

## `[blood]`

| Option | Default | Range | Description |
|---|---|---|---|
| `maxBlood` | 240 | 1 to no limit | Maximum stored blood for this race before generation penalties. |
| `bloodRegenThreshold` | 80 | 0 to no limit | Blood amount required before passive blood regeneration can activate. |

## `[bloodfiend.evolution]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epRequirement` | 0 | 0 to no limit | EP required to evolve into this race. The base Bloodfiend value is unused for normal starting race selection. |
| `bossRequirement` | 0 | 0 to no limit | Boss kills required to evolve into this race. Set to 0 to disable this requirement. |
| `bloodRequirement` | 0 | 0 to no limit | Total blood drained required to evolve into this race. Set to 0 to disable this requirement. |
| `mobTurnRequirement` | 0 | 0 to no limit | Total mobs or players turned into kindred required to evolve into this race. Set to 0 to disable this requirement. |

## `[bloodfiend.base_energy]`

| Option | Default | Range | Description |
|---|---|---|---|
| `minAura` | 7,500 | 0 to no limit | Minimum base aura for this race. |
| `maxAura` | 12,000 | 0 to no limit | Maximum base aura for this race. |
| `minMagicule` | 9,000 | 0 to no limit | Minimum base magicule for this race. |
| `maxMagicule` | 16,000 | 0 to no limit | Maximum base magicule for this race. |

## `[bloodfiend.attributes]`

| Option | Default | Range | Description |
|---|---|---|---|
| `size` | 0 | -0.9 to 16 | Scale modifier for this race. 0 means normal size. |
| `maxHealth` | 20 | 0 to no limit | Max health bonus/value used by the race config. |
| `maxSpiritualHealth` | 120 | 0 to no limit | Max spiritual health bonus/value used by the race config. |
| `attack` | 1.5 | 0 to no limit | Attack damage bonus/value used by the race config. |
| `attackSpeed` | 0.1 | -1 to no limit | Attack speed modifier used by the race config. |
| `knockbackResistance` | 0.05 | 0 to 1 | Knockback resistance modifier used by the race config. |
| `movementSpeed` | 0.025 | -1 to no limit | Movement speed modifier used by the race config. |
| `swimSpeed` | -0.35 | -1 to no limit | Swim speed modifier. Negative values make Bloodfiends worse in water. |

## `[bloodfiend.blood]`

| Option | Default | Range | Description |
|---|---|---|---|
| `maxBlood` | 100 | 1 to no limit | Maximum stored blood for this race before generation penalties. |
| `bloodRegenThreshold` | 45 | 0 to no limit | Blood amount required before passive blood regeneration can activate. |

## `[elder_bloodfiend.evolution]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epRequirement` | 120,000 | 0 to no limit | EP required to evolve into this race. The base Bloodfiend value is unused for normal starting race selection. |
| `bossRequirement` | 0 | 0 to no limit | Boss kills required to evolve into this race. Set to 0 to disable this requirement. |
| `bloodRequirement` | 400 | 0 to no limit | Total blood drained required to evolve into this race. Set to 0 to disable this requirement. |
| `mobTurnRequirement` | 5 | 0 to no limit | Total mobs or players turned into kindred required to evolve into this race. Set to 0 to disable this requirement. |

## `[elder_bloodfiend.base_energy]`

| Option | Default | Range | Description |
|---|---|---|---|
| `minAura` | 40,000 | 0 to no limit | Minimum base aura for this race. |
| `maxAura` | 65,000 | 0 to no limit | Maximum base aura for this race. |
| `minMagicule` | 50,000 | 0 to no limit | Minimum base magicule for this race. |
| `maxMagicule` | 85,000 | 0 to no limit | Maximum base magicule for this race. |

## `[elder_bloodfiend.attributes]`

| Option | Default | Range | Description |
|---|---|---|---|
| `size` | 0 | -0.9 to 16 | Scale modifier for this race. 0 means normal size. |
| `maxHealth` | 80 | 0 to no limit | Max health bonus/value used by the race config. |
| `maxSpiritualHealth` | 900 | 0 to no limit | Max spiritual health bonus/value used by the race config. |
| `attack` | 2.5 | 0 to no limit | Attack damage bonus/value used by the race config. |
| `attackSpeed` | 0.18 | -1 to no limit | Attack speed modifier used by the race config. |
| `knockbackResistance` | 0.1 | 0 to 1 | Knockback resistance modifier used by the race config. |
| `movementSpeed` | 0.035 | -1 to no limit | Movement speed modifier used by the race config. |
| `swimSpeed` | -0.28 | -1 to no limit | Swim speed modifier. Negative values make Bloodfiends worse in water. |

## `[elder_bloodfiend.blood]`

| Option | Default | Range | Description |
|---|---|---|---|
| `maxBlood` | 140 | 1 to no limit | Maximum stored blood for this race before generation penalties. |
| `bloodRegenThreshold` | 55 | 0 to no limit | Blood amount required before passive blood regeneration can activate. |

## `[blood_noble.evolution]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epRequirement` | 450,000 | 0 to no limit | EP required to evolve into this race. The base Bloodfiend value is unused for normal starting race selection. |
| `bossRequirement` | 0 | 0 to no limit | Boss kills required to evolve into this race. Set to 0 to disable this requirement. |
| `bloodRequirement` | 1,500 | 0 to no limit | Total blood drained required to evolve into this race. Set to 0 to disable this requirement. |
| `mobTurnRequirement` | 18 | 0 to no limit | Total mobs or players turned into kindred required to evolve into this race. Set to 0 to disable this requirement. |

## `[blood_noble.base_energy]`

| Option | Default | Range | Description |
|---|---|---|---|
| `minAura` | 160,000 | 0 to no limit | Minimum base aura for this race. |
| `maxAura` | 240,000 | 0 to no limit | Maximum base aura for this race. |
| `minMagicule` | 180,000 | 0 to no limit | Minimum base magicule for this race. |
| `maxMagicule` | 300,000 | 0 to no limit | Maximum base magicule for this race. |

## `[blood_noble.attributes]`

| Option | Default | Range | Description |
|---|---|---|---|
| `size` | 0 | -0.9 to 16 | Scale modifier for this race. 0 means normal size. |
| `maxHealth` | 300 | 0 to no limit | Max health bonus/value used by the race config. |
| `maxSpiritualHealth` | 2,500 | 0 to no limit | Max spiritual health bonus/value used by the race config. |
| `attack` | 4 | 0 to no limit | Attack damage bonus/value used by the race config. |
| `attackSpeed` | 0.28 | -1 to no limit | Attack speed modifier used by the race config. |
| `knockbackResistance` | 0.18 | 0 to 1 | Knockback resistance modifier used by the race config. |
| `movementSpeed` | 0.045 | -1 to no limit | Movement speed modifier used by the race config. |
| `swimSpeed` | -0.22 | -1 to no limit | Swim speed modifier. Negative values make Bloodfiends worse in water. |

## `[blood_noble.blood]`

| Option | Default | Range | Description |
|---|---|---|---|
| `maxBlood` | 185 | 1 to no limit | Maximum stored blood for this race before generation penalties. |
| `bloodRegenThreshold` | 65 | 0 to no limit | Blood amount required before passive blood regeneration can activate. |

## `[blood_monarch.black_communion]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | If true, Crimson Progenitors can use Black Communion. |
| `maxMastery` | 1,000 | 1 to no limit | Maximum mastery for Black Communion. |

## `[blood_monarch.black_communion.activation]`

| Option | Default | Range | Description |
|---|---|---|---|
| `activationBloodCost` | 140 | 0 to no limit | Blood cost paid by the Crimson Progenitor when the communion starts. |
| `duration` | 2,400 | 20 to no limit | Maximum active duration in ticks. 2400 ticks = 2 minutes. |
| `pulseInterval` | 40 | 1 to no limit | How often the network pulses. 40 ticks = 2 seconds. |
| `collapseCooldown` | 90 | 0 to no limit | Cooldown in seconds after manually collapsing Black Communion. |

## `[blood_monarch.black_communion.radius]`

| Option | Default | Range | Description |
|---|---|---|---|
| `baseRadius` | 24 | 1 to 512 | Starting ritual radius. |
| `maxRadius` | 96 | 1 to 512 | Maximum ritual radius after power scaling. |
| `radiusPerPower` | 0.08 | 0 to 16 | Radius gained per stored communion power. |

## `[blood_monarch.black_communion.power]`

| Option | Default | Range | Description |
|---|---|---|---|
| `maxPower` | 800 | 1 to no limit | Maximum stored communion power. |
| `bloodfiendWeight` | 1 | 0 to 1,024 | Power weight for Bloodfiend participants. |
| `elderBloodfiendWeight` | 2 | 0 to 1,024 | Power weight for Elder Bloodfiend participants. |
| `bloodNobleWeight` | 4 | 0 to 1,024 | Power weight for Blood Noble participants. |
| `bloodMonarchWeight` | 7 | 0 to 1,024 | Power weight for Blood Monarch participants. |
| `crimsonProgenitorWeight` | 12 | 0 to 1,024 | Power weight for Crimson Progenitor participants. |
| `generationContributionPenalty` | 0.04 | 0 to 1 | Power contribution penalty per generation after generation 1. |
| `minGenerationContribution` | 0.45 | 0 to 1 | Minimum generation contribution multiplier. |
| `emptyBloodContribution` | 0.25 | 0 to 1,024 | Minimum contribution even if a linked Bloodfiend is low on blood. |
| `fullBloodContribution` | 1 | 0 to 1,024 | Contribution added based on stored blood ratio. |
| `bloodDrainedPowerMultiplier` | 0.0008 | 0 to 1,024 | Extra power per total blood drained by the participant. |
| `thrallPowerMultiplier` | 0.08 | 0 to 1,024 | Extra power per total thrall turned by the participant. |
| `maxProgressContribution` | 10 | 0 to 1,024 | Maximum extra power from progress stats per participant per pulse. |
| `powerGainMultiplier` | 0.08 | 0 to 1,024 | Final multiplier for communion power gained per pulse. |
| `nodeOfferingBloodCost` | 0.35 | 0 to 1,024 | Blood paid per participant weight each pulse. |

## `[blood_monarch.black_communion.shared_bloodline]`

| Option | Default | Range | Description |
|---|---|---|---|
| `sharedBloodTransferPerPulse` | 6 | 0 to no limit | Blood moved from high-blood nodes to low-blood nodes per pulse. |
| `sharedBloodLowRatio` | 0.35 | 0 to 1 | A linked Bloodfiend below this blood ratio can receive shared blood. |
| `sharedBloodDonorMinRatio` | 0.45 | 0 to 1 | A linked Bloodfiend must stay above this blood ratio to donate shared blood. |
| `progenitorBloodGainPerPulse` | 4 | 0 to no limit | Blood gained by the Progenitor every pulse. |
| `linkedBloodGainPerPulse` | 2 | 0 to no limit | Blood gained by every linked Bloodfiend every pulse. |
| `linkedHealPerPulse` | 2,000 | 0 to no limit | Health restored to every linked Bloodfiend every pulse. |
| `linkedSpiritualRestorePerPulse` | 6,000 | 0 to no limit | Spiritual health restored to every linked Bloodfiend every pulse. |
| `linkedMagiculeRestorePerPulse` | 120,000 | 0 to no limit | Magicules restored to every linked Bloodfiend every pulse. |

## `[blood_monarch.black_communion.combat]`

| Option | Default | Range | Description |
|---|---|---|---|
| `baseDamageReduction` | 0.1 | 0 to 1 | Base damage reduction for linked Bloodfiends. |
| `damageReductionPerPower` | 0.0008 | 0 to 1 | Extra damage reduction per communion power. |
| `maxDamageReduction` | 0.75 | 0 to 1 | Maximum damage reduction for linked Bloodfiends. |
| `damageBoostPerPower` | 0.0009 | 0 to 1,024 | Damage boost per communion power for linked Bloodfiends. |
| `maxDamageBoost` | 1.5 | 0 to 1,024 | Maximum damage boost from communion power. |

## `[blood_monarch.black_communion.infection]`

| Option | Default | Range | Description |
|---|---|---|---|
| `infectionStacksPerPulse` | 1 | 0 to no limit | Black infection stacks applied to enemies per pulse. |
| `maxInfectionStacks` | 12 | 1 to no limit | Maximum black infection stacks. |
| `infectionDuration` | 500 | 1 to no limit | Black infection duration in ticks. |
| `infectionBrandDuration` | 160 | 1 to no limit | Blood Brand duration applied by black infection. |
| `infectionDamageInterval` | 60 | 1 to no limit | How often infection deals damage. |
| `infectionPulseDamage` | 0.75 | 0 to no limit | Damage per infection stack per infection pulse. |
| `infectionMaxPulseDamage` | 45 | 0 to no limit | Maximum infection pulse damage. |
| `infectionBloodLeak` | 1 | 0 to no limit | Blood gained by linked Bloodfiends per infection stack per pulse. |
| `infectionHealLeak` | 0.25 | 0 to no limit | Healing gained by linked Bloodfiends per infection stack per pulse. |
| `infectionDamageBoostPerStack` | 0.035 | 0 to 1,024 | Extra damage linked Bloodfiends deal per infection stack on the target. |
| `maxInfectionDamageBoost` | 1.2 | 0 to 1,024 | Maximum damage boost from infection stacks. |
| `skipBloodlessInfection` | true |  | If true, black infection ignores bloodless entities. |
| `deathSpreadRadius` | 10 | 0 to 128 | Radius where infection spreads when an infected target dies. |
| `killBloodGain` | 8 | 0 to no limit | Blood gained by linked Bloodfiends when infected enemies die. |
| `killHeal` | 4 | 0 to no limit | Healing gained by linked Bloodfiends when infected enemies die. |
| `killPowerGain` | 8 | 0 to no limit | Communion power gained when infected enemies die. |

## `[blood_monarch.black_communion.death_prevention]`

| Option | Default | Range | Description |
|---|---|---|---|
| `preventDeathBloodCost` | 80 | 1 to no limit | Total shared network blood cost to prevent a linked Bloodfiend death. |
| `preventDeathHealthRatio` | 0.18 | 0.01 to 1 | Health ratio restored when death is prevented. |
| `preventDeathInvulnerabilityTicks` | 80 | 0 to no limit | Invulnerability ticks after death prevention. |
| `preventDeathCooldownTicks` | 120 | 0 to no limit | Cooldown ticks before the network can prevent another death. |
| `preventDeathSpiritualRestore` | 250 | 0 to no limit | Spiritual health restored on death prevention. |
| `preventDeathMagiculeRestore` | 500,000 | 0 to no limit | Magicules restored on death prevention. |
| `preventDeathInfectionRadius` | 12 | 0 to 128 | Black infection burst radius when death is prevented. |
| `preventDeathInfectionStacks` | 3 | 0 to no limit | Infection stacks applied by death prevention burst. |

## `[blood_monarch.black_communion.collapse]`

| Option | Default | Range | Description |
|---|---|---|---|
| `collapseBaseDamage` | 1,000 | 0 to no limit | Base damage dealt by Black Eucharist collapse. |
| `collapseDamagePerPower` | 0.32 | 0 to no limit | Extra collapse damage per communion power. |
| `collapseMaxDamage` | 35,000 | 0 to no limit | Maximum collapse damage. |
| `collapseHeal` | 60,000 | 0 to no limit | Health restored to linked Bloodfiends on collapse. |
| `collapseSpiritualHeal` | 1,200,000 | 0 to no limit | Spiritual health restored to linked Bloodfiends on collapse. |
| `collapseMagiculeRestore` | 2,500,000 | 0 to no limit | Magicules restored to linked Bloodfiends on collapse. |
| `collapseBloodRestore` | 120 | 0 to no limit | Blood restored to linked Bloodfiends on collapse. |
| `collapseBrandDuration` | 700 | 1 to no limit | Blood Brand duration applied during collapse. |
| `collapseMobTurnHealthThreshold` | 0.25 | 0 to 1 | Infected mobs below this health ratio can be turned by collapse. |

## `[blood_monarch.black_communion.black_blood_domain]`

| Option | Default | Range | Description |
|---|---|---|---|
| `blockInfectionEnabled` | false |  | If true, Black Communion can infect blocks and create Black Blood Domains. |
| `blockInfectionAttempts` | 96 | 0 to no limit | Random block infection attempts per active communion pulse. |
| `blockInfectionBlocksPerPulse` | 14 | 0 to no limit | Fast spread blocks per communion pulse before power scaling. |
| `blockInfectionMaxBlocksPerPulse` | 42 | 0 to no limit | Maximum blocks infected by the progenitor per communion pulse. |
| `blockInfectionBlocksPerPower` | 0.035 | 0 to 1,024 | Extra fast spread blocks per stored communion power. |
| `blockInfectionMaxRadius` | 72 | 1 to 512 | Maximum radius used by active communion block infection. |
| `blockInfectionVerticalRange` | 5 | 1 to 64 | Vertical random spread range for block infection. |
| `linkedBloodfiendsSpreadBlocks` | 2 | 0 to no limit | Extra block spread from each linked Bloodfiend during active communion. |
| `linkedBloodfiendSpreadAttempts` | 16 | 0 to no limit | Random spread attempts around each linked Bloodfiend. |
| `linkedBloodfiendSpreadRadius` | 18 | 1 to 512 | Spread radius around linked Bloodfiends. |
| `domainChunkValuePerBlock` | 1 | 0 to no limit | Virtual domain value added to a chunk per infected block. Buffs use this instead of scanning blocks. |
| `domainChunkValueSacrificeBonus` | 18 | 0 to no limit | Extra virtual domain value added to the altar chunk per blood sacrifice. |
| `domainChunkMaxValue` | 1,000 | 1 to no limit | Maximum virtual black blood domain value per chunk. |
| `domainBiomeChunkValueRequired` | 36 | 1 to no limit | Chunk value required for the area to count as a Black Blood Domain biome for buffs. |

## `[blood_monarch.black_communion.black_blood_domain_buffs]`

| Option | Default | Range | Description |
|---|---|---|---|
| `domainBiomeBuffsEnabled` | true |  | If true, Bloodfiends receive buffs in infected domain chunks. |
| `domainBiomeBuffInterval` | 80 | 1 to no limit | How often domain biome buffs pulse. 80 ticks = 4 seconds. |
| `domainBiomeBloodfiendHeal` | 250 | 0 to no limit | Health restored to Bloodfiends standing in infected domain chunks. |
| `domainBiomeBloodfiendSpiritualRestore` | 450 | 0 to no limit | Spiritual health restored to Bloodfiends in infected domain chunks. |
| `domainBiomeBloodfiendMagiculeRestore` | 900,000 | 0 to no limit | Magicules restored to Bloodfiends in infected domain chunks. |
| `domainBiomeBloodfiendBloodGain` | 3 | 0 to no limit | Blood gained by Bloodfiends in infected domain chunks. |
| `domainBiomeBloodfiendBloodGainPerAltarLevel` | 2 | 0 to no limit | Extra blood gained per nearby altar level. |
| `domainBiomeBuffPerAltarLevel` | 0.2 | 0 to 1,024 | Multiplier bonus per nearby altar level for domain healing/restoration. |
| `domainBiomeAltarLevelSearchRadius` | 96 | 1 to 512 | Radius used to find nearby altar level for stronger domain buffs. |
| `domainBiomeDamagesEnemies` | true |  | If true, non-Bloodfiends take light damage in infected domain chunks. |
| `domainBiomeEnemyDamage` | 80 | 0 to no limit | Light damage dealt to non-Bloodfiends in infected domain chunks per buff interval. |
| `domainBiomeKillBloodGain` | 2 | 0 to no limit | Fuel blood generated into the nearest Blood Altar when black blood domain biome damage kills a non-Bloodfiend. This also counts as lifetime altar blood. |

## `[blood_monarch.black_communion.blood_altar]`

| Option | Default | Range | Description |
|---|---|---|---|
| `bloodAltarEnabled` | true |  | If true, Black Communion can create Blood Altars. |
| `allowMultipleBloodAltars` | false |  | If false, only one Blood Altar can exist globally in this world for all Bloodfiends. If true, unlimited altars can exist. |
| `altarRequiredPower` | 25 | 0 to no limit | Communion power required before an altar can spawn. |
| `altarRequiredChunkValue` | 28 | 0 to no limit | Virtual domain chunk value required before an altar can spawn near the progenitor. |
| `altarSpawnSearchRadius` | 8 | 1 to 128 | Search radius for altar spawn positions around the progenitor. |
| `altarNoSpawnNearRadius` | 160 | 0 to no limit | Prevents a new altar from spawning this close to another altar. |
| `altarSacrificeEnabled` | true |  | If true, Bloodfiends can sacrifice blood into Blood Altars. |
| `altarFuelPerBlock` | 30 | 1 to no limit | Fuel blood consumed per infected block created by altar and vein-node spread. 30 means 30 stored blood = 1 infected block. |
| `altarMaxStoredBlood` | 10,000 | 1 to no limit | Maximum fuel blood inside a Blood Altar. |
| `altarMaxLevel` | 5 | 0 to 5 | Maximum Blood Altar level. |
| `altarLevel1Blood` | 1,000 | 0 to no limit | Stored blood required for altar level 1. |
| `altarLevel2Blood` | 2,500 | 0 to no limit | Stored blood required for altar level 2. |
| `altarLevel3Blood` | 5,000 | 0 to no limit | Stored blood required for altar level 3. |
| `altarLevel4Blood` | 7,500 | 0 to no limit | Stored blood required for altar level 4. |
| `altarLevel5Blood` | 10,000 | 0 to no limit | Stored blood required for altar level 5. |
| `altarPassiveSpreadEnabled` | true |  | If true, Blood Altars passively spread infection after communion ends. |
| `altarSpreadInterval` | 100 | 1 to no limit | Altar spread interval when the altar has at least level 1. |
| `altarSpreadAttempts` | 48 | 0 to no limit | Random spread attempts per altar passive spread pulse. |
| `altarSpreadBlocksPerPulse` | 3 | 0 to no limit | Blocks spread by a powered altar per passive pulse. |
| `altarSpreadBlocksPerLevel` | 2 | 0 to no limit | Extra altar passive spread blocks per altar level. |
| `altarBaseRadius` | 24 | 1 to 512 | Base altar spread and buff radius. |
| `altarRadiusPerLevel` | 4 | 0 to 512 | Extra altar radius per altar level. Level 1 makes the radius +4 by default. |
| `altarSacrificeBurstAttempts` | 128 | 0 to no limit | Random spread attempts immediately after a blood sacrifice. |
| `altarSacrificeBurstBlocks` | 18 | 0 to no limit | Blocks infected immediately after a blood sacrifice. |
| `altarSacrificeBurstBlocksPerLevel` | 10 | 0 to no limit | Extra sacrifice burst blocks per altar level. |
| `dormantSpreadInterval` | 1,200 | 1 to no limit | Very slow spread interval for a level 0 altar. 1200 ticks = 60 seconds. |
| `dormantSpreadBlocksPerPulse` | 1 | 0 to no limit | Very slow dormant spread blocks for an unpowered altar. |

## `[blood_monarch.black_communion.black_blood_conquest]`

| Option | Default | Range | Description |
|---|---|---|---|
| `conquestEnabled` | true |  | If true, Blood Altars can run the long-term world conquest system: player/base memory, World Roots, Blood Flower Blooms, and World Heart. |
| `conquestRequiredAltarLevel` | 5 | 0 to 5 | Minimum real Blood Altar level required before conquest ticks at all. This also disables player/base tracking unless a valid altar exists. |
| `conquestRequiredWorldStageForRoots` | 1 | 0 to no limit | Minimum world conquest stage required before new World Roots can start. Stage 1 is reached from a powerful altar, so roots do not begin immediately at fresh worlds. |
| `conquestPlayerMemoryInterval` | 200 | 20 to no limit | How often player/base memory samples run. 200 ticks = 10 seconds. |
| `conquestBaseScanRadius` | 10 | 1 to 64 | Sparse radius around sampled players used to score artificial/base blocks. |
| `conquestMemoryPruneTicks` | 864,000 | 1,200 to no limit | Old non-infected player/base chunk memory is removed after this many ticks. 864000 ticks = 12 hours. |
| `conquestMinPlayerHeatTarget` | 80 | 1 to no limit | Minimum long-term player presence score for a chunk to be targetable by roots. |
| `conquestMinBaseHeatTarget` | 140 | 1 to no limit | Minimum artificial/base block score for a chunk to count as a base-like root target. |
| `conquestMaxActiveRoots` | 10 | 0 to 256 | Maximum active underground World Roots before World Heart multiplier. |
| `conquestRequiredDomainLevel` | 5 | 0 to 100 | Minimum single Domain Level required before conquest ticks at all. |
| `conquestRequiredDomainLevelForRoots` | 5 | 0 to 100 | Minimum single Domain Level required before World Root tunnels start. |
| `conquestWorldHeartRequiredDomainLevel` | 10 | 1 to 100 | Single Domain Level required to form the World Heart. |
| `conquestRootMaxTargetDistanceBlocks` | 8,192 | 16 to 30,000,000 | Maximum distance a World Root tunnel may target. 8192 allows thousands of blocks without force-loading chunks. |
| `conquestRootBlocksPerTick` | 100 | 1 to 256 | How many tunnel blocks each active World Root may grow per root tick. Higher means thousand-block targets are reached faster. |
| `conquestMaxRootsProcessedPerTick` | 8 | 1 to 256 | Hard budget for active roots processed per root tick. |
| `conquestRootTickInterval` | 10 | 1 to no limit | How often roots move. 40 ticks = 2 seconds. |
| `conquestRootStartCost` | 180 | 0 to no limit | Blood Altar fuel cost to start one World Root. |
| `conquestRootStepCost` | 35 | 0 to no limit | Blood Altar fuel cost per World Root step. |
| `conquestRootMaxAge` | 72,000 | 20 to no limit | Maximum root age in root ticks before it dies. |
| `conquestRootReachDistanceChunks` | 1 | 0 to 64 | Root completes when it reaches this chunk distance from its target. |
| `conquestBloomTickInterval` | 100 | 1 to no limit | How often Blood Flower Blooms tick. 100 ticks = 5 seconds. |
| `conquestBloomStartBlood` | 2,500 | 0 to no limit | Stored conquest blood given to normal blooms when they spawn. |
| `conquestBaseBloomBloodMultiplier` | 3 | 1 to no limit | Multiplier for starting blood when a bloom erupts from a player-base target. |
| `conquestBloomMaxStoredBlood` | 250,000 | 1 to no limit | Maximum stored conquest blood inside one Blood Flower Bloom. |
| `conquestBloomFeedInterval` | 200 | 1 to no limit | Bloom age interval used to feed stored blood to the main altar. |
| `conquestBloomFeedAmount` | 750 | 0 to no limit | Blood sent from a bloom to the main altar per feed interval, multiplied by bloom tier. |
| `conquestBloomSpreadBlocks` | 45 | 0 to no limit | Block spread budget for normal bloom spread pulses. |
| `conquestBloomBurstSpreadBlocks` | 140 | 0 to no limit | Initial infection burst blocks for normal Bloom creation. |
| `conquestBaseBloomBurstSpreadBlocks` | 260 | 0 to no limit | Initial infection burst blocks for base-breach Bloom creation. |
| `conquestBloomDrainMaxBlood` | 2,500 | 1 to no limit | Max stored bloom blood a Bloodfiend can drain per interaction. |
| `conquestBloomGrowthDivisor` | 250 | 1 to no limit | Bloom blood divided by this becomes permanent Black Blood Growth. |
| `conquestBloomBloodDivisor` | 100 | 1 to no limit | Bloom blood divided by this becomes normal stored Bloodfiend blood. |
| `conquestBloomHealMultiplier` | 0.05 | 0 to no limit | Health restored per drained bloom blood. |
| `conquestBloomSpiritualMultiplier` | 0.25 | 0 to no limit | Spiritual health restored per drained bloom blood. |
| `conquestBloomMagiculeMultiplier` | 150 | 0 to no limit | Magicules restored per drained bloom blood. |
| `conquestHeartTickInterval` | 200 | 1 to no limit | How often the World Heart ticks. 200 ticks = 10 seconds. |
| `conquestWorldHeartStage` | 6 | 1 to no limit | World conquest stage number used for the final World Heart state. |
| `conquestWorldHeartSpreadBlocks` | 180 | 0 to no limit | Block spread budget for each World Heart pulse. |
| `conquestWorldHeartMinGrowth` | 100 | 0 to no limit | Minimum permanent growth gained from drinking the active World Heart. |
| `conquestWorldHeartHealMultiplier` | 12 | 0 to no limit | Health restored per World Heart growth point. |
| `conquestWorldHeartSpiritualMultiplier` | 85 | 0 to no limit | Spiritual health restored per World Heart growth point. |
| `conquestWorldHeartMagiculeMultiplier` | 75,000 | 0 to no limit | Magicules restored per World Heart growth point. |
| `conquestConqueredThreshold` | 1,800 | 1 to no limit | Infection pressure required for a chunk to count as conquered. |
| `conquestBlockBreakPressure` | 25 | 0 to no limit | Infection pressure added when a conquest/infected block is broken while conquest is active. |
| `conquestStage1RequiredAltarLevel` | 3 | 0 to 5 | Stage 1 requirement: minimum active altar level. |
| `conquestStage1RequiredTotalBlood` | 20,000 | 0 to no limit | Stage 1 requirement: lifetime blood in the best active altar. |
| `conquestStage2RequiredBlooms` | 3 | 0 to no limit | Stage 2 requirement: created blooms. |
| `conquestStage2RequiredCompletedRoots` | 2 | 0 to no limit | Stage 2 requirement: completed roots. |
| `conquestStage3RequiredBlooms` | 8 | 0 to no limit | Stage 3 requirement: created blooms. |
| `conquestStage3RequiredBaseBreaches` | 1 | 0 to no limit | Stage 3 requirement: base breaches. |
| `conquestStage3RequiredConqueredChunks` | 12 | 0 to no limit | Stage 3 requirement: conquered chunks. |
| `conquestStage4RequiredBlooms` | 14 | 0 to no limit | Stage 4 requirement: created blooms. |
| `conquestStage4RequiredBaseBreaches` | 3 | 0 to no limit | Stage 4 requirement: base breaches. |
| `conquestStage4RequiredConqueredChunks` | 35 | 0 to no limit | Stage 4 requirement: conquered chunks. |
| `conquestStage5RequiredBlooms` | 20 | 0 to no limit | Stage 5 requirement: created blooms. |
| `conquestStage5RequiredBaseBreaches` | 4 | 0 to no limit | Stage 5 requirement: base breaches. |
| `conquestStage5RequiredCompletedRoots` | 14 | 0 to no limit | Stage 5 requirement: completed roots. |
| `conquestStage5RequiredConqueredChunks` | 60 | 0 to no limit | Stage 5 requirement: conquered chunks. |
| `conquestWorldHeartRequiredBlooms` | 24 | 0 to no limit | World Heart requirement: created blooms. |
| `conquestWorldHeartRequiredBaseBreaches` | 5 | 0 to no limit | World Heart requirement: base breaches. |
| `conquestWorldHeartRequiredConqueredChunks` | 80 | 0 to no limit | World Heart requirement: conquered chunks. |
| `conquestWorldHeartRequiredCompletedRoots` | 18 | 0 to no limit | World Heart requirement: completed roots. |
| `conquestGrowthHealthPerPoint` | 2 | 0 to no limit | Max health attribute gained per permanent Black Blood Growth point. |
| `conquestGrowthAttackPerPoint` | 0.35 | 0 to no limit | Attack damage attribute gained per permanent Black Blood Growth point. |
| `conquestGrowthSpeedPerPoint` | 0 | 0 to no limit | Movement speed attribute gained per permanent Black Blood Growth point. |
| `conquestGrowthMaxHealthCap` | 1,000,000 | 0 to no limit | Maximum max-health attribute gained from Black Blood Growth. |
| `conquestGrowthMaxAttackCap` | 250,000 | 0 to no limit | Maximum attack attribute gained from Black Blood Growth. |
| `conquestGrowthMaxSpeedCap` | 1.5 | 0 to no limit | Maximum movement-speed attribute gained from Black Blood Growth. |

## `[blood_monarch.black_communion.black_blood_conquest.black_blood_domain_level]`

| Option | Default | Range | Description |
|---|---|---|---|
| `domainMaxLevel` | 10 | 1 to 100 | Single visible Black Blood Domain level cap. Altar blood and conquest stats both feed this one system. |
| `domainLevel6Xp` | 25,000 | 0 to no limit | Domain XP required for level 6. |
| `domainLevel7Xp` | 60,000 | 0 to no limit | Domain XP required for level 7. |
| `domainLevel8Xp` | 150,000 | 0 to no limit | Domain XP required for level 8. |
| `domainLevel9Xp` | 350,000 | 0 to no limit | Domain XP required for level 9. |
| `domainLevel10Xp` | 900,000 | 0 to no limit | Domain XP required for level 10, the World Heart tier. |
| `domainXpPerBloom` | 10,000 | 0 to no limit | Domain XP gained per created Blood Flower Bloom. |
| `domainXpPerCompletedRoot` | 6,000 | 0 to no limit | Domain XP gained per completed World Root tunnel. |
| `domainXpPerBaseBreach` | 30,000 | 0 to no limit | Domain XP gained per player/base breach. |
| `domainXpPerConqueredChunk` | 450 | 0 to no limit | Domain XP gained per conquered chunk. |

## `[blood_monarch.black_communion.black_blood_conquest.black_blood_ecology]`

| Option | Default | Range | Description |
|---|---|---|---|
| `ecologyEnabled` | true |  | Enables the additive slow ecology, structures, converted mobs, fusion, and unloaded virtual frontier. |
| `ecologyMinimumWorldStage` | 2 | 1 to no limit | The stage needed for ecology to start. |
| `ecologyVirtualStepInterval` | 1,200 | 200 to no limit | Ticks between unloaded virtual conquest pulses. 1200 ticks is 1 minute. |
| `ecologyVirtualClaimSteps` | 4 | 2 to 127 | Paid virtual steps required to claim one unloaded chunk. |
| `ecologyVirtualStepBloodCost` | 50 | 1 to no limit | Altar fuel cost for one virtual conquest step. |
| `ecologyMaterializeInterval` | 200 | 100 to no limit | Ticks between checking naturally loaded player chunks for virtual infection materialization. |
| `ecologyBuildInterval` | 2,000 | 1,200 to no limit | Ticks between attempts to queue one autonomous infection structure. 6000 ticks is 5 minutes. |
| `ecologyTickInterval` | 200 | 40 to no limit | Base ecology structure processing interval. |
| `ecologyMaxStructures` | 150 | 1 to 512 | Maximum autonomous infection structures per dimension. |
| `ecologyBuildBloodCost` | 300 | 1 to no limit | Fuel blood reserved by a pending autonomous structure before it forms. |
| `ecologyStructureMinSpacing` | 48 | 16 to 512 | Minimum block spacing between autonomous structures. |
| `ecologySpireSpreadInterval` | 3,600 | 1,200 to no limit | Ticks between a Vein Spire adding a tiny normal loaded-chunk spread pulse. |
| `ecologySpireSpreadBlocks` | 1 | 1 to 2 | Normal infection blocks requested by each Vein Spire pulse. |
| `ecologyNestPulseInterval` | 2,400 | 1,200 to no limit | Ticks between Conversion Nest corruption pulses. |
| `ecologyNestRadius` | 14 | 6 to 64 | Loaded radius used by Conversion Nests. |
| `ecologyNestPulseDamage` | 1 | 0 to 1,000 | Very small damage dealt by a Conversion Nest while slowly corrupting a mob. |
| `ecologyCorruptionDecayTicks` | 2,400 | 400 to no limit | Corruption disappears after no converted-minion or nest contact for this long. |
| `ecologyConversionMarks` | 4 | 1 to 100 | Corruption marks required before a weakened mob can be converted. |
| `ecologyConversionHealthRatio` | 0.35 | 0.01 to 1 | Mob health ratio required for conversion. |
| `ecologyMinionCapPerNest` | 8 | 1 to 64 | Nearby converted mob cap supported by one nest. |
| `ecologyConversionBloodCost` | 45 | 1 to no limit | Structure or altar blood paid for each successful mob conversion. |
| `ecologyMinionThinkInterval` | 40 | 20 to 400 | Ticks between converted mob targeting and movement decisions. |
| `ecologyMinionTargetRadius` | 16 | 6 to 64 | Loaded targeting radius for converted mobs. |
| `ecologyMinionMoveSpeed` | 0.95 | 0.1 to 3 | Navigation speed used by converted mobs. |
| `ecologyMinionAttackInterval` | 30 | 20 to 400 | Ticks between handler-driven attacks from converted mobs. |
| `ecologyMinionDamage` | 10.5 | 0.1 to 1,000 | Base handler-driven magic damage from a tier 1 converted mob. |
| `ecologyFusionInterval` | 4,800 | 2,400 to no limit | Ticks between Fusion Pit attempts. 4800 ticks is 4 minutes. |
| `ecologyFusionRadius` | 10 | 6 to 32 | Loaded radius used by a Fusion Pit. |
| `ecologyFusionBloodCost` | 120 | 1 to no limit | Structure or altar blood spent when three equal-tier minions fuse. |
| `ecologyMaxFusionTier` | 8 | 2 to 8 | Maximum fusion tier. Tier 2 needs three tier 1 mobs and tier 3 needs three tier 2 mobs. |
| `ecologyReservoirFeedInterval` | 6,000 | 1,200 to no limit | Ticks between Blood Reservoir feed attempts. 6000 ticks is 5 minutes. |
| `ecologyReservoirFeedAmount` | 400 | 1 to no limit | Maximum blood a reservoir can forward per feed attempt. |
| `ecologyBloodCollectionRadius` | 96 | 32 to 512 | Radius used to route blood earned by converted mob kills into structures. |
| `ecologyStructureBloodCapacity` | 10,000 | 100 to no limit | Maximum kill-earned blood stored by one autonomous structure. |
| `ecologyBloodHealthDivisor` | 20 | 1 to no limit | Killed target max health divided by this becomes collected blood before the cap. |
| `ecologyMaxBloodPerKill` | 50 | 1 to no limit | Maximum structure blood earned from one converted mob kill. |
| `ecologyVirtualStepsPerPulse` | 2 | 1 to 16 | Base number of frontier entries processed per virtual pulse. Additional structures increase this up to a hard handler cap. |
| `ecologyMaxPendingBuilds` | 24 | 1 to 128 | Maximum persisted pending structures and remote altars waiting for fuel or a loaded valid site. |
| `ecologyPendingProcessInterval` | 200 | 40 to no limit | Ticks between attempts to complete pending builds. |
| `ecologyRemoteAltarsEnabled` | true |  | Allows the ecology to establish distant colony altars even when normal multiple altars are disabled. |
| `ecologyRemoteAltarMinDistance` | 400 | 128 to 30,000,000 | Minimum distance in blocks from every existing altar before a remote ecology altar may be queued. |
| `ecologyRemoteAltarRequiredChunkValue` | 120 | 1 to no limit | Required infected chunk value for a distant ecology altar site. |
| `ecologyRemoteAltarBloodCost` | 400 | 1 to no limit | Fuel blood required by a pending distant ecology altar. |
| `ecologyRemoteAltarSeedFuel` | 800 | 0 to no limit | Part of the remote altar cost transferred into the new altar as starting fuel. |
| `ecologyRemoteAltarAttemptEvery` | 4 | 1 to 64 | Every Nth five-minute build attempt prefers a distant ecology altar when a valid far infection site exists. |
| `ecologyWorldHeartRootCount` | 40 | 1 to 12 | Number of ecology World Roots maintained from infection nodes toward the current target. |
| `ecologyWorldHeartRootInterval` | 6,000 | 1,200 to no limit | Ticks between ecology attempts to queue or launch World Roots from the nearest infection source. |
| `ecologySummonerInterval` | 1,200 | 1,200 to no limit | Ticks between Summoner Bloom attempts. |
| `ecologySummonerBloodCost` | 20 | 1 to no limit | Structure or altar blood spent for one summoned blood minion. |
| `ecologySummonerCap` | 30 | 1 to 64 | Nearby converted minion cap supported by one Summoner Bloom. |
| `ecologyRelayInterval` | 2,400 | 600 to no limit | Ticks between Root Relay virtual expansion pulses. |
| `ecologyRelayBloodCost` | 60 | 1 to no limit | Blood spent by a Root Relay for one local virtual expansion pulse. |
| `ecologyRelaySteps` | 2 | 1 to 8 | Local frontier steps attempted by a Root Relay per paid pulse. |
| `ecologySanctuaryInterval` | 400 | 100 to no limit | Ticks between Blood Sanctuary healing pulses. |
| `ecologySanctuaryRadius` | 20 | 6 to 64 | Loaded healing radius of a Blood Sanctuary. |
| `ecologySanctuaryHeal` | 25 | 0 to no limit | Health restored to Bloodfiends and converted blood minions per Sanctuary pulse. |
| `ecologyHuntingBeaconInterval` | 600 | 100 to no limit | Ticks between Hunting Beacon target assignments. |
| `ecologyHuntingBeaconRadius` | 32 | 8 to 96 | Loaded radius used by Hunting Beacons to coordinate minions. |
| `ecologyFusionPowerPerConqueredChunk` | 3 | 0 to 1,000 | Internal infection power granted per conquered chunk before fusion scaling. |
| `ecologyFusionHealthPerPower` | 0.08 | 0 to 1,000 | Tier-scaled max-health multiplier gained per infection power. |
| `ecologyFusionAttackPerPower` | 0.012 | 0 to 1,000 | Tier-scaled attack multiplier gained per infection power. |
| `ecologyFusionMaxHealthMultiplier` | 250 | 0 to 100,000 | Maximum infection-based fused-minion max-health multiplier. 250 allows ordinary mobs to reach several thousand health late-game. |
| `ecologyFusionMaxAttackMultiplier` | 2,400 | 0 to 100,000 | Maximum infection-based fused-minion attack multiplier. |
| `ecologyFusionMaxArmor` | 800 | 0 to 100,000 | Maximum flat armor added to fused minions from infection strength. |

## `[blood_monarch.evolution]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epRequirement` | 1,500,000 | 0 to no limit | EP required to evolve into this race. The base Bloodfiend value is unused for normal starting race selection. |
| `bossRequirement` | 0 | 0 to no limit | Boss kills required to evolve into this race. Set to 0 to disable this requirement. |
| `bloodRequirement` | 5,500 | 0 to no limit | Total blood drained required to evolve into this race. Set to 0 to disable this requirement. |
| `mobTurnRequirement` | 50 | 0 to no limit | Total mobs or players turned into kindred required to evolve into this race. Set to 0 to disable this requirement. |

## `[blood_monarch.base_energy]`

| Option | Default | Range | Description |
|---|---|---|---|
| `minAura` | 700,000 | 0 to no limit | Minimum base aura for this race. |
| `maxAura` | 950,000 | 0 to no limit | Maximum base aura for this race. |
| `minMagicule` | 850,000 | 0 to no limit | Minimum base magicule for this race. |
| `maxMagicule` | 1,200,000 | 0 to no limit | Maximum base magicule for this race. |

## `[blood_monarch.attributes]`

| Option | Default | Range | Description |
|---|---|---|---|
| `size` | 0.05 | -0.9 to 16 | Scale modifier for this race. 0 means normal size. |
| `maxHealth` | 700 | 0 to no limit | Max health bonus/value used by the race config. |
| `maxSpiritualHealth` | 5,000 | 0 to no limit | Max spiritual health bonus/value used by the race config. |
| `attack` | 6.5 | 0 to no limit | Attack damage bonus/value used by the race config. |
| `attackSpeed` | 0.42 | -1 to no limit | Attack speed modifier used by the race config. |
| `knockbackResistance` | 0.28 | 0 to 1 | Knockback resistance modifier used by the race config. |
| `movementSpeed` | 0.055 | -1 to no limit | Movement speed modifier used by the race config. |
| `swimSpeed` | -0.15 | -1 to no limit | Swim speed modifier. Negative values make Bloodfiends worse in water. |

## `[blood_monarch.blood]`

| Option | Default | Range | Description |
|---|---|---|---|
| `maxBlood` | 240 | 1 to no limit | Maximum stored blood for this race before generation penalties. |
| `bloodRegenThreshold` | 80 | 0 to no limit | Blood amount required before passive blood regeneration can activate. |

## `[crimson_progenitor.evolution]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epRequirement` | 3,500,000 | 0 to no limit | EP required to evolve into this race. The base Bloodfiend value is unused for normal starting race selection. |
| `bossRequirement` | 2 | 0 to no limit | Boss kills required to evolve into this race. Set to 0 to disable this requirement. |
| `bloodRequirement` | 15,000 | 0 to no limit | Total blood drained required to evolve into this race. Set to 0 to disable this requirement. |
| `mobTurnRequirement` | 120 | 0 to no limit | Total mobs or players turned into kindred required to evolve into this race. Set to 0 to disable this requirement. |

## `[crimson_progenitor.base_energy]`

| Option | Default | Range | Description |
|---|---|---|---|
| `minAura` | 1,800,000 | 0 to no limit | Minimum base aura for this race. |
| `maxAura` | 2,400,000 | 0 to no limit | Maximum base aura for this race. |
| `minMagicule` | 2,200,000 | 0 to no limit | Minimum base magicule for this race. |
| `maxMagicule` | 3,000,000 | 0 to no limit | Maximum base magicule for this race. |

## `[crimson_progenitor.attributes]`

| Option | Default | Range | Description |
|---|---|---|---|
| `size` | 0.08 | -0.9 to 16 | Scale modifier for this race. 0 means normal size. |
| `maxHealth` | 1,100 | 0 to no limit | Max health bonus/value used by the race config. |
| `maxSpiritualHealth` | 10,000 | 0 to no limit | Max spiritual health bonus/value used by the race config. |
| `attack` | 9 | 0 to no limit | Attack damage bonus/value used by the race config. |
| `attackSpeed` | 0.65 | -1 to no limit | Attack speed modifier used by the race config. |
| `knockbackResistance` | 0.4 | 0 to 1 | Knockback resistance modifier used by the race config. |
| `movementSpeed` | 0.07 | -1 to no limit | Movement speed modifier used by the race config. |
| `swimSpeed` | -0.05 | -1 to no limit | Swim speed modifier. Negative values make Bloodfiends worse in water. |

## `[crimson_progenitor.blood]`

| Option | Default | Range | Description |
|---|---|---|---|
| `maxBlood` | 320 | 1 to no limit | Maximum stored blood for this race before generation penalties. |
| `bloodRegenThreshold` | 110 | 0 to no limit | Blood amount required before passive blood regeneration can activate. |

## `[blood.kindred]`

| Option | Default | Range | Description |
|---|---|---|---|
| `defaultNaturalGeneration` | 1 | 1 to no limit | Generation assigned to naturally selected Bloodfiend players. Natural Bloodfiends should usually be generation 1. |
| `maxGeneration` | 12 | 1 to no limit | Maximum allowed kindred generation. |
| `bloodCapacityPenaltyPerGeneration` | 0.025 | 0 to 1 | Blood capacity penalty per generation after generation 1. |
| `bloodArtPenaltyPerGeneration` | 0.02 | 0 to 1 | Blood Arts power penalty per generation after generation 1. |
| `waterWeaknessPerGeneration` | 0.04 | 0 to 16 | Water weakness increase per generation after generation 1. |
| `minimumPowerMultiplier` | 0.55 | 0 to 1 | Minimum multiplier after generation penalties. |

## `[blood.passive_regeneration]`

| Option | Default | Range | Description |
|---|---|---|---|
| `passiveInterval` | 240 | 1 to no limit | How often passive blood regeneration checks. 240 ticks = 12 seconds. Blood is only consumed if health, spiritual health, or magicules are missing. |
| `passiveBloodCost` | 1 | 0 to no limit | Blood consumed per passive regeneration pulse. |
| `passiveHeal` | 2 | 0 to no limit | Health healed per passive regeneration pulse. |
| `passiveSpiritualHeal` | 35 | 0 to no limit | Spiritual health restored per passive regeneration pulse. |
| `passiveMagiculeRestore` | 75 | 0 to no limit | Magicules restored per passive regeneration pulse. |

## `[blood.water_weakness]`

| Option | Default | Range | Description |
|---|---|---|---|
| `waterCheckInterval` | 160 | 1 to no limit | How often water and rain weakness checks. 160 ticks = 8 seconds. |
| `waterBloodDrain` | 1 | 0 to no limit | Blood drained when touching water. |
| `rainBloodDrain` | 0 | 0 to no limit | Blood drained when standing in rain. |
| `waterDamage` | 0.75 | 0 to no limit | Damage dealt when touching water. |
| `rainDamage` | 0.1 | 0 to no limit | Damage dealt when standing in rain. |
| `waterMagiculeDrain` | 15 | 0 to no limit | Magicules drained when touching water. |

## `[blood.blood_hunger]`

| Option | Default | Range | Description |
|---|---|---|---|
| `hungerInterval` | 300 | 1 to no limit | How often Bloodfiends convert stored blood into hunger. 300 ticks = 15 seconds. |
| `hungerBloodCost` | 1 | 0 to no limit | Blood consumed whenever hunger is restored. |
| `hungerFoodRestore` | 4 | 0 to 20 | Food points restored from blood. 2 food points = 1 hunger shank. |
| `hungerSaturationRestore` | 2 | 0 to 20 | Saturation restored from blood feeding. |
| `minimumFoodLevelFromBlood` | 18 | 0 to 20 | If the player has blood, their hunger is kept at least this high. |

## `[blood.master_bond]`

| Option | Default | Range | Description |
|---|---|---|---|
| `masterBondInterval` | 200 | 1 to no limit | How often kindred with a living Bloodfiend master receive a bond pulse. |
| `masterBondBloodGain` | 1 | 0 to no limit | Blood gained by kindred near their living master. |
| `masterBondRange` | 32 | 0 to 512 | Range required for master bond blood pulse. |
| `masterBondBloodArtMultiplier` | 1.12 | 1 to 16 | Blood Arts power multiplier for kindred with a living Bloodfiend master. |
| `masterBondBloodCapacityMultiplier` | 1.15 | 1 to 16 | Max blood multiplier for kindred with a living Bloodfiend master. |
| `masterBondBloodCostMultiplier` | 0.75 | 0 to 1 | Blood cost multiplier for kindred with a living Bloodfiend master. |
| `masterBondWaterWeaknessMultiplier` | 0.75 | 0 to 1 | Water weakness multiplier for kindred with a living Bloodfiend master. |

## `[blood_arts]`

| Option | Default | Range | Description |
|---|---|---|---|
| `maxMastery` | 1,000 | 1 to no limit | Maximum mastery for Blood Arts. |

## `[blood_arts.drain_blood]`

| Option | Default | Range | Description |
|---|---|---|---|
| `drainRange` | 10 | 0 to 128 | Target range for held Drain Blood. |
| `drainTickInterval` | 14 | 1 to 200 | How often held Drain Blood pulses. 14 ticks is a little slower than twice per second. |
| `drainPulseCooldown` | 0 | 0 to no limit | Tiny cooldown after each drain pulse. Usually keep this at 0 because the held interval already controls pacing. |
| `drainBloodGain` | 8 | 0 to no limit | Blood gained per Drain Blood pulse before generation modifiers. |
| `drainDamage` | 1 | 0 to no limit | Damage dealt per Drain Blood pulse. Kept low so Kindred Rite can be used before targets die. |
| `drainCooldown` | 0 | 0 to no limit | Unused legacy cooldown for older press-drain behavior. |
| `bloodBrandDrainMultiplier` | 3 | 1 to no limit | Drain Blood gain multiplier against Blood Branded targets. |
| `lowHealthDrainBonusThreshold` | 0.35 | 0 to 1 | Targets at or below this health ratio give bonus blood. |
| `lowHealthDrainBonusMultiplier` | 1.75 | 1 to 64 | Blood gain multiplier against low-health targets. |

## `[blood_arts.blood_surge]`

| Option | Default | Range | Description |
|---|---|---|---|
| `bloodSurgeCost` | 1 | 0 to no limit | Blood consumed by Blood Surge per cost interval while Blood Arts is toggled and damage is boosted. |
| `bloodSurgeCostInterval` | 40 | 1 to no limit | Minimum ticks between Blood Surge blood payments. 40 ticks = 2 seconds. |
| `bloodSurgeDamageMultiplier` | 0.45 | 0 to 1,024 | Damage multiplier added by Blood Surge. 0.45 means +45% before generation and master scaling. |

## `[blood_arts.crimson_guard]`

| Option | Default | Range | Description |
|---|---|---|---|
| `crimsonGuardCost` | 12 | 0 to no limit | Blood cost to activate Crimson Guard. |
| `crimsonGuardDuration` | 200 | 1 to no limit | Duration of Crimson Guard in ticks. |
| `crimsonGuardCooldown` | 10 | 0 to no limit | Cooldown for Crimson Guard in seconds. |
| `crimsonGuardHitBloodCost` | 1 | 0 to no limit | Extra blood consumed when Crimson Guard reduces incoming damage. |
| `crimsonGuardHitCostInterval` | 40 | 1 to no limit | Minimum ticks between Crimson Guard hit blood costs. 40 ticks = 2 seconds. |
| `crimsonGuardDamageTakenMultiplier` | 0.45 | 0 to 1 | Incoming damage multiplier while Crimson Guard is active. 0.45 means 55% reduction. |

## `[blood_arts.blood_brand]`

| Option | Default | Range | Description |
|---|---|---|---|
| `bloodBrandCost` | 8 | 0 to no limit | Blood cost to brand a target. |
| `bloodBrandDuration` | 600 | 1 to no limit | Duration of Blood Brand in ticks. |
| `bloodBrandCooldown` | 5 | 0 to no limit | Cooldown for Blood Brand in seconds. |

## `[blood_arts.kindred_rite]`

| Option | Default | Range | Description |
|---|---|---|---|
| `kindredRiteCost` | 90 | 0 to no limit | Blood cost to use Kindred Rite. |
| `kindredRiteCooldown` | 45 | 0 to no limit | Cooldown for Kindred Rite in seconds. |
| `kindredRiteRange` | 8 | 0 to 128 | Target range for Kindred Rite. |
| `mobTurnHealthThreshold` | 0.35 | 0 to 1 | Target mob must be at or below this health ratio to be turned unless EP ratio allows instant turning. |
| `playerTurnHealthThreshold` | 0.3 | 0 to 1 | Target player must be at or below this health ratio unless EP ratio allows instant turning. Consent is still required. |
| `instantTurnEpRatio` | 0.01 | 0 to 1 | If target EP is below this ratio of owner EP, Kindred Rite ignores the health threshold. 0.01 means below 1 percent. |
| `playerTurnConsentTicks` | 1,200 | 20 to no limit | Player turning consent window in ticks. The target must be prompted first, then sneak during a second Kindred Rite attempt. 1200 ticks = 60 seconds. |
| `kindredRiteSuccessBloodGain` | 35 | 0 to no limit | Blood gained by the owner after a successful Kindred Rite. |
| `maxActiveBloodThralls` | 6 | 0 to no limit | Maximum active blood thralls. |
| `allowMobTurning` | true |  | If true, Kindred Rite can turn weakened mobs. |
| `allowPlayerTurning` | true |  | If true, Kindred Rite can turn consenting weakened players into Bloodfiends. |

## `[parasite.base_energy]`

| Option | Default | Range | Description |
|---|---|---|---|
| `minAura` | 100 | 0 to no limit |  |
| `maxAura` | 200 | 0 to no limit |  |
| `minMagicule` | 100 | 0 to no limit |  |
| `maxMagicule` | 200 | 0 to no limit |  |

## `[parasite.attributes]`

| Option | Default | Range | Description |
|---|---|---|---|
| `size` | -0.9 | -0.9 to 16 |  |
| `maxHealth` | 5 | -1,024 to no limit |  |
| `maxSpiritualHealth` | 5 | 0 to no limit |  |
| `attack` | 0 | 0 to no limit |  |
| `attackSpeed` | 0 | -1 to no limit |  |
| `knockbackResistance` | 0 | 0 to 1 |  |
| `movementSpeed` | 0 | -1 to no limit |  |
| `swimSpeed` | 0 | -1 to no limit |  |
