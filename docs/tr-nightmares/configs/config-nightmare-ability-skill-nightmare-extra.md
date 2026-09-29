# `config/nightmare/ability/skill/nightmare_extra.toml`

<small>[TR: Nightmares](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Concentrator]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 10,000 |  | Magicule Acquirement Cost. |
| `magiculeRegenPercent` | 0.5 |  | Percentage of Magicules regenerated every 5 seconds. |
| `epRequirement` | 1,000,000 |  | Number of Existence Points the player must have to meet the natural requirements. |

## `[Smelter]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 10,000 |  | Magicule Acquirement Cost. |
| `epRequirement` | 100,000 |  | Number of magicules for the player to be capable of learning it. |
| `doubleChance` | 80 |  | Chance for it to double gained items out of 100. |

## `[MysticAura]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 1,000 |  | Magicule Acquirement Cost. |
| `mpCost` | 500 |  | Percentage of Magicules regenerated every 5 seconds. |
| `requiredMagics` | 20 |  | Number of Mastered Spells required to obtain. |
| `requiredBattlewills` | 10 |  | Number of Mastered Battlewills required to obtain. |
| `durationUnmastered` | 30 |  | Duration in Seconds the effect will last when unmastered. |

## `[SpacetimeDomination]`

| Option | Default | Range | Description |
|---|---|---|---|
| `compatibleUltimateSkillIds` | "nightmareutils:sentient", "trnightmare:azathoth", "trnightmare:azazel", "trnightmare:nodens", "trnightmare:samael", "trnightmare:yog-sotohort" |  | Ultimate (or skill) resource ids that enable learning Spacetime Domination when possessed. Empty = unobtainable. Designer fill-in, e.g. trnightmare:example_spacetime_ultimate |
| `timeStopRadiusBlocks` | 32 |  | Time Stop radius in blocks (centered on caster). |
| `timeStopDurationTicks` | 180 |  | Time Stop duration in ticks when unmastered (9s = 180). |
| `timeStopDurationTicksMastered` | 840 |  | Time Stop duration in ticks when mastered (11s = 220). |
| `timeStopMagiculeCost` | 250,000 |  | Magicule cost per Time Stop use. |
| `timeStopLearnPoints` | 100 |  | Learn points required for Time Stop mode. |
| `timeStopCooldownSeconds` | 120 |  | Time Stop cooldown in seconds. |
| `timeStopSnowflakesPerTick` | 16 |  | Snowflake particles per tick while Time Stop is active. |

## `[LawDomination]`

| Option | Default | Range | Description |
|---|---|---|---|
| `immuneEffectIds` | "tensura:infinite_inprisonment", "tensura:spatial_blockade" |  | Effects this skill grants immunity to while toggled. Use &lt;namespace:path&gt; IDs. |

## `[PseudoDragonBody]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule acquirement cost. |
| `mpDrainPerTick` | 500 |  | Magicule drained each skill tick (~1 per second) while toggled on. |

## `[SpacetimeManipulation]`

| Option | Default | Range | Description |
|---|---|---|---|
| `spacetimeInflictionBoost` | 4 |  | Space damage multiplier while Spacetime Infliction is toggled (Spatial Domination uses 3.0). |
| `magiculeCostCleansePerSeverance` | 100 |  | Magicule per severance point for Space-Time Cleanse. |
| `cleanseCooldown` | 3 |  | Cooldown in seconds for Space-Time Cleanse. |
| `shortTeleportRange` | 60 |  | Maximum blocks for short Spatial Transfer blink. |
| `warpMpPerBlock` | 5 |  | Magicule per block for coordinate warp (Spatial Transfer shift). |
| `requiredUltimateSkillIds` | "trnightmare:azathoth", "trnightmare:yog-sotohort" |  | Ultimate skill ids that satisfy the learn gate (§3 may mirror into SpacetimeManipulationCompat). |

## `[Prayer]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 10,000 |  | Magicule Acquirement Cost. |
| `mpCost` | 1,000 |  | Magicule Cost per second. |
| `spPerSub` | 1 |  | Number of Spiritrons generated per subordinate. |
| `spMax` | 8 |  | Maximum number of Spiritrons that can be generated per 5 seconds. |

## `[ForbiddenKnowledge]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 10,000 |  | Magicule Acquirement Cost. |
| `epRequirement` | 1,000,000 |  | Number of Existence Points the player must have to meet the natural requirements. |
| `learningPoint` | 8 |  | Number of Learning Points gained from Forbidden Knowledge. |
| `masteryPoint` | 8 |  | Number of Mastery Points gained from Forbidden Knowledge. |

## `[Mimicry]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mimicryEpMaxDifference` | 0.3 |  | Maximum EP difference allowed between you and the target to analyze/mimic (fraction). |
| `mimicryAllowUniqueAndUltimate` | false |  | Allow Mimicry to copy Unique and Ultimate skills when enabled. |
| `learnRequired` | 100 |  | Number of learn points required to fully analyze a target (matches other imitator/artist configs). |
| `allowedSkillIds` | "tensura:predator", "tensura:gluttony", "tensura:beelzebuth" |  | Skill ids that are allowed to mimic. |

## `[UniversalShapeshift]`

| Option | Default | Range | Description |
|---|---|---|---|
| `learnRequired` | 5 |  | Learn-progress required per discover pulse. |
| `allowUniqueAndUltimate` | false |  | Whether unique/ultimate skills can be copied. |
| `chimeraDuration` | 6,000 |  | Chimera Transformation duration in ticks (non-mastered). |
| `chimeraDurationMastered` | 7,200 |  | Chimera Transformation duration in ticks (mastered). |
| `chimeraCooldown` | 24,000 |  | Chimera Transformation cooldown in ticks. |

## `[FoodChain]`

| Option | Default | Range | Description |
|---|---|---|---|
| `allowedSkillIds` | "tensura:starved", "tensura:gourmet", "tensura:gluttony", "trnightmare:beelzebub", "trnightmare:beelzebuth" |  | Skill ids that can use Food Chain. |
| `resistanceAllowedIds` | "tensura:starved", "tensura:gourmet", "tensura:gluttony", "trnightmare:beelzebub", "trnightmare:beelzebuth" |  | Skill ids that can transfer resistance skills through Food Chain. |
| `extraAllowedIds` | "tensura:gourmet", "tensura:gluttony", "trnightmare:beelzebub", "trnightmare:beelzebuth" |  | Skill ids that can transfer extra skills through Food Chain. |
| `commonAllowdIds` | "tensura:starved", "tensura:gourmet", "tensura:gluttony", "trnightmare:beelzebub", "trnightmare:beelzebuth" |  | Skill ids that can transfer common skills through Food Chain. |
| `intrinsicAllowedIds` | "tensura:starved", "tensura:gourmet", "tensura:gluttony", "trnightmare:beelzebub", "trnightmare:beelzebuth" |  | Skill ids that can transfer intrinsic skills through Food Chain. |
| `uniqueAllowedIds` | [] (empty) |  | Skill ids that can transfer unique skills through Food Chain. |
| `ultimateAllowedIds` | [] (empty) |  | Skill ids that can transfer ultimate skills through Food Chain. |
| `blacklistedIds` | "tensura:starved", "tensura:gourmet", "tensura:gluttony", "trnightmare:beelzebub", "trnightmare:beelzebuth", "trnightmare:witches_envy", "trnightmare:time_traveler", "trnightmare:yog_sothoth", "trnightmare:yog-sotohort", "trnightmare:conceptual_existence", "trnightmare:manas_host", "trnightmare:rebirth", "trnightmare:mimicry", "trnightmare:food_chain", "trnightmare:ultimate_arroganz", "trnightmare:skill_storage", "nightmareutils:sentient", "trnightmare:alteration", "nightmareutils:sentientdisintegrate", "nightmareutils:charm_test" ... (28 total) |  | Skill ids that are banned from being transferred through Food Chain. |

## `[SkillStorage]`

| Option | Default | Range | Description |
|---|---|---|---|
| `excludedSkillIds` | "trnightmare:shub-niggurath", "trnightmare:nodens", "trnightmare:ultimate_arroganz" |  | Skill ids that Skill Storage will NOT store when obtained (blacklist). |
| `allowedSkillIds` | [] (empty) |  | Skill ids that are allowed to be stored (empty = allow all not in exclusion list). |

## `[UltimateArroganz]`

| Option | Default | Range | Description |
|---|---|---|---|
| `allowedSkillIds` | [] (empty) |  | Skill ids or options related to Ultimate Arroganz. Empty = default behavior. |

## `[Alteration]`

| Option | Default | Range | Description |
|---|---|---|---|
| `allowedUserIds` | "trnightmare:raphael_knowledge", "trnightmare:raphael_wisdom", "trnightmare:azathoth" |  | Skill ids that can use Raphael-style alteration by default. |
| `allowedSkillIds` | "trnightmare:beelzebub", "trnightmare:beelzebuth", "trnightmare:raphael_wisdom", "trnightmare:susanoo", "trnightmare:uriel_lord_of_oath", "trnightmare:tsukiyomi", "trnightmare:samael", "trnightmare:belial", "trnightmare:azazel", "trnightmare:amaterasu", "trnightmare:law_domination", "trnightmare:mood_maker", "trnightmare:cthugha", "trnightmare:nodens" |  | Skill ids that can be affected by Raphael-style alteration by default. |

## `[FaithBlessing]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magicNumber` | 5 |  | Number of Holy Magics that must be mastered to learn this skill. |

## `[HandOfCreation]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `furnaceRestorePercent` | 0.05 |  | Percentage of max Magicules restored per second by Energy Engine (unmastered). |
| `furnaceRestorePercentMastered` | 0.07 |  | Percentage of max Magicules restored per second by Energy Engine (mastered). |
| `furnaceMaxMpPercent` | 2.5 |  | Maximum Magicules Energy Engine can generate, as a multiplier of max Magicules. |
| `spiritronRegen` | 50 |  | Spiritrons generated per second by Energy Engine (unmastered). |
| `spiritronRegenMastered` | 100 |  | Spiritrons generated per second by Energy Engine (mastered). |

## `[HandOfDestruction]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `divineDarknessDamage` | 100 |  | Divine Darkness damage per hit (unmastered). |
| `divineDarknessDamageMastered` | 250 |  | Divine Darkness damage per hit (mastered). |
| `divineDarknessMpCostPercent` | 0.035 |  | Fraction of max MP drained per Divine Darkness use. |

## `[Leader]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `subordinateRequirement` | 10 |  | Number of subordinates required to learn this skill. |
| `subordinateDetectRange` | 24 |  | Range in blocks to detect nearby subordinates. |
| `maxSubordinatesInMenu` | 12 |  | Maximum number of subordinates to show in menus. |
| `maxGroups` | 10 |  | Maximum number of subordinate groups. |

## `[MultidimensionalBarrier]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 2,500 |  | Magicule Acquirement Cost. |
| `mpCost` | 250 |  | Magicule cost per activation. |
| `pointMultiplier` | 1.5 |  | Barrier points multiplier based on the user's max health. |
| `allyPointMultiplier` | 0.75 |  | Barrier points multiplier for ally targets based on their max health. |
| `cooldown` | 10 |  | Cooldown in seconds before the barrier can be reactivated. |
| `barrierEPThreshold` | 0.5 |  | Legacy barrier strength threshold used for the multilayer barrier base value. |
| `barrierNormal` | 1 |  | Legacy barrier strength multiplier while the skill is not mastered. |
| `barrierMastered` | 1.5 |  | Legacy barrier strength multiplier while the skill is mastered. |
