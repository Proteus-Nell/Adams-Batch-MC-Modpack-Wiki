# `config/tensura/EliteTensura/UltimateSkillConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[RaphealSkill]`

| Option | Default | Range | Description |
|---|---|---|---|
| `IsEnabled` | true |  | Is this Skill Enabled? |
| `chantSpeed` | 4 |  | The chant speed multiplier when toggled. |
| `learningPoint` | 16 |  | The bonus number of learning point to gain when toggled. |
| `masteryPoint` | 16 |  | The bonus number of mastery point to gain when toggled. |
| `analysisLevel` | 18 |  | The Analysis Level when activated. |
| `analysisLevelMastered` | 32 |  | The Analysis Level when activated with Mastery. |
| `analysisRadius` | 25 |  | The Analysis Radius when activated. |
| `analysisRadiusMastered` | 64 |  | The Analysis Radius when activated with Mastery. |
| `copyRange` | 20 |  | The range in block of Analyze / Reverse-Engineer targeting on mobs. |
| `copyRangeMagic` | 32 |  | The range in block of Reverse-Engineer on magic projectiles. |
| `copyCooldownSuccess` | 10 |  | The cooldown in second when the user successfully copied a skill from targets. |
| `copyCooldownFail` | 5 |  | The cooldown in second when the user failed to copy a skill from targets. |
| `analysisDurationSeconds` | 300 |  | How long (seconds) a target stays analyzed after Analyze marks it. |
| `maxAnalyzedTargets` | 16 |  | Maximum number of simultaneously analyzed targets. |
| `analyzeMagiculeCost` | 500 |  | Magicule cost of Analyze (mode 0). |
| `reverseEngineerChannelSeconds` | 5 |  | Observation channel length (seconds) for Reverse-Engineer. |
| `reverseEngineerMagiculeCost` | 5,000 |  | Magicule cost to start a Reverse-Engineer channel (mode 1). |
| `predictionNegateCooldownSeconds` | 30 |  | Seconds between Prediction hit-negations against analyzed attackers. |
| `predictionNegateMagiculeCost` | 2,000 |  | Magicule cost per Prediction hit-negation. |
| `predictionCritMultiplier` | 1.5 |  | Damage multiplier of Prediction's computed strike against analyzed targets. |
| `predictionCritCooldownSeconds` | 10 |  | Seconds between Prediction computed strikes. |
| `barrierDamageReduction` | 0.25 |  | Multilayer Barrier damage reduction (0-1) against unanalyzed attackers. |
| `barrierDamageReductionAnalyzed` | 0.5 |  | Multilayer Barrier damage reduction (0-1) against analyzed attackers. |
| `barrierUpkeepMagiculePerSecond` | 100 |  | Magicule upkeep per second while Multilayer Barrier is active (charged as 5× this once per 5 s skill tick). |
| `counselEnabled` | true |  | Enable Independent Counsel proposals. |
| `counselProposalExpirySeconds` | 10 |  | Seconds a Counsel proposal stays pending before it expires. |
| `counselTriggerCooldownSeconds` | 60 |  | Per-trigger cooldown (seconds) between Counsel proposals. |
| `counselLowHealthPercent` | 0.35 |  | Health fraction (0-1) below which Counsel proposes the barrier. |
| `emergencyDefenseEnabled` | true |  | Enable autonomous Emergency Defense against lethal hits. |
| `emergencyDefenseCooldownSeconds` | 300 |  | Cooldown (seconds) between Emergency Defense activations. |
| `emergencyDefenseMagiculeCost` | 20,000 |  | Magicule cost of an Emergency Defense activation. |
| `arsMagnaRequiresAnalysis` | true |  | If true, Ars Magna benefits (instant cast, chant annulment, half MP) require a computed situation (live analysis / Prediction / Barrier). If false, plain toggle is enough. |
| `maxBonusLevel` | 4 |  | How many levels that Rapheal can go above the maximum level of an enchantment. |
| `enchantmentBlacklist` | "tensura:dead_end_rainbow", "tensura:tsukumogami" |  | Lists of enchantments that Godly Craftsman cannot learn or add. |
| `maxBonusBlacklist` | - |  | Lists of enchantments that Godly Craftsman cannot learn or add above the enchantment's maximum level. |
| `curseChance` | - |  | The percentage chance to obtain a Curse Engraving per Engraving on the item. |
| `storageSlots` | 54 |  | Spatial storage slots (Tensura: Great Sage 20, Researcher 45, Predator 63). Shrinking on a live world silently drops items in the removed slots. |
| `storageStackSize` | 256 |  | Max stack size per spatial storage slot (Tensura: 128). |

## `[OuroborosSkill]`

| Option | Default | Range | Description |
|---|---|---|---|
| `IsEnabled` | true |  | Is this Skill Enabled? |
| `renewalHealFraction` | 0.15 |  | Fraction of dealt damage returned as healing while toggled. |
| `renewalShpHealFraction` | 0.15 |  | Fraction of dealt damage returned as spiritual health while toggled (0 disables). |
| `renewalMagiculeFraction` | 0.1 |  | Fraction of dealt damage returned as magicule while toggled. |
| `renewalDamagePenalty` | 0.2 |  | Outgoing damage penalty while toggled. Keeps returned value below sacrificed value (the loop leaks). |
| `fangsCost` | 3,000 |  | Magicule cost to prime the fangs. |
| `fangsPrimeTicks` | 100 |  | Ticks the prime lasts waiting for a hit. |
| `fangsEchoBonusPerStep` | 0.25 |  | Bonus per successive echo (echo 1 = 1x+bonus, echo 2 = 1x+2xbonus). |
| `fangsEchoDelayTicks` | 20 |  | Ticks between the strikes (hit, +delay, +2xdelay). |
| `fangsCooldown` | 8 |  | Cooldown in seconds of Timeless Fangs. |
| `moltCostPerDebuff` | 2,000 |  | Magicule cost per harmful effect shed. |
| `moltBaseAbsorption` | 4 |  | Base absorption granted on any successful molt (2.0 = 1 heart). |
| `moltAbsorptionPerDebuff` | 2 |  | Absorption granted per debuff shed. |
| `moltCooldown` | 30 |  | Cooldown in seconds of Molt. |
| `moltCooldownMastered` | 15 |  | Cooldown in seconds of Molt when mastered. |
| `coilBackCost` | 20,000 |  | Magicule cost of the rewind. |
| `coilBackRewindTicks` | 100 |  | How far back the rewind reaches, in ticks. |
| `coilBackHealFraction` | 0.5 |  | Fraction of HP lost over the window that the rewind restores. |
| `coilBackCooldown` | 60 |  | Cooldown in seconds of Coil Back. |
| `coilBackShockwaveRadius` | 4 |  | Radius in blocks of the arrival shockwave (set base and fraction to 0 to disable). |
| `coilBackShockwaveBase` | 50 |  | Flat base damage of the arrival shockwave. |
| `coilBackShockwaveFraction` | 5 |  | Extra shockwave damage per point of HP restored by the rewind. |
| `cycleArmCostFraction` | 0.5 |  | Fraction of MAX magicule paid to arm the cycle. |
| `cycleArmedDurationTicks` | 6,000 |  | Duration in ticks of the armed state (the visible effect icon). |
| `rebirthHealthFraction` | 0.3 |  | Fraction of max HP restored on rebirth. |
| `cycleDebtDurationTicks` | 12,000 |  | Duration in ticks of one Cycle Debt application. |
| `cycleCooldown` | 600 |  | Cooldown in seconds of arming Cycle's End. |
| `mawCost` | 10,000 |  | Magicule cost of the bite. |
| `mawRange` | 6 |  | Cone reach in blocks. |
| `mawAngle` | 90 |  | Full cone angle in degrees. |
| `mawBaseDamage` | 100 |  | Flat damage per target. |
| `mawMaxHpFraction` | 0.1 |  | Fraction of target max HP added as damage. |
| `mawHealFraction` | 0.25 |  | Fraction of total damage dealt returned as healing. |
| `mawCooldown` | 12 |  | Cooldown in seconds of Serpent's Maw. |
| `friendlyFire` | false |  | If true, Coil Back's shockwave and Serpent's Maw also hit players in the user's own nation or hunt party. |

## `[BeelzebuthSkill]`

| Option | Default | Range | Description |
|---|---|---|---|
| `IsEnabled` | true |  | Is this Skill Enabled? |
| `predationRange` | 12 |  | The max range in blocks of the Predation mist. |
| `predationRangeMastered` | 18 |  | The max range in blocks of the Predation mist when mastered. |
| `predationDamage` | 300 |  | The attack damage of the Predation mist. |
| `predationEPSteal` | 0.8 |  | The multiplier of the target's EP turned into the user's EP when killed by the Predation mist. |
| `predationEPDrain` | 5,000 |  | The amount of magicule the mist drains from targets per hit. |
| `predationSkillChance` | 80 |  | The chance (percent) to steal skills from targets without killing them. |
| `predationSkillNumber` | 3 |  | The number of skills stolen from a target at a time without killing it. |
| `predationUniqueDevourLimit` | 4 |  | The max number of Unique skills the kill-devour (devour all skills) can steal from a single target. Non-unique skills are not capped. |
| `predationMagicCopyChance` | 1 |  | The chance (0.0-1.0) for the kill-devour (devour all skills) to copy a target's Magic. 0 disables Magic copying. |
| `predationCorrosionDuration` | 200 |  | The duration in ticks of the Corrosion effect applied by the Predation mist. |
| `predationCorrosionLevel` | 4 |  | The level of the Corrosion effect applied by the Predation mist. |
| `stomachSlots` | 108 |  | Number of slots in the Stomach spatial storage. |
| `stomachStackSize` | 999 |  | Max stack size per slot in the Stomach spatial storage. |
| `isolateCleanseCostPerEffect` | 2,000 |  | Magicule Cost to absorb each of your own harmful status effects into the Isolate pool. |
| `isolateEffectCredit` | 250 |  | Magicule credited to the Isolate pool per absorbed harmful effect. |
| `isolateConversionMultiplier` | 3 |  | Multiplier applied to an item's dissolving registry value when converting quarantined items. |
| `isolateFallbackMagicule` | 50 |  | Flat magicule value per quarantined item with no dissolving registry entry. |
| `isolateMaxStacks` | 54 |  | Max number of quarantined item stacks the Isolate can hold. |
| `isolateConvertCooldownSeconds` | 8 |  | Cooldown in seconds of the Isolate batch conversion. |
| `isolateConvertCooldownMasteredSeconds` | 2 |  | Cooldown in seconds of the Isolate batch conversion when mastered. |
| `absorbProjectileCost` | 500 |  | Magicule Cost per hostile projectile swallowed while toggled. |
| `isolateProjectileCredit` | 500 |  | Magicule credited to the Isolate pool per swallowed projectile. |
| `isolateProjectileCooldown` | 60 |  | Internal cooldown in ticks between projectile absorbs. |
| `provideRange` | 5 |  | The range in blocks for targeting a subordinate in Provide/Receive Mode. |
| `provideCostPercentage` | 0.9 |  | Cost of Provide % 0.9 = 90% magicules. |
| `provideCooldownSeconds` | 120 |  | Cooldown in seconds of Provide Mode (applied when the copy succeeds). |
| `provideCooldownMasteredSeconds` | 60 |  | Cooldown in seconds of Provide Mode when mastered. |
| `receiveCostPercentage` | 0.9 |  | Cost of Receive % 0.9 = 90% magicules. |
| `receiveCooldownSeconds` | 120 |  | Cooldown in seconds of Receive Mode (applied when the copy succeeds). |
| `receiveCooldownMasteredSeconds` | 60 |  | Cooldown in seconds of Receive Mode when mastered. |
| `soulConsumeMagiculeCost` | 60,000 |  | Magicule Cost of Soul Consume, charged once per second while the aura is held. |
| `drainDuration` | 200 |  | The duration in tick of the Soul Drain effect applied on targets hit while Soul Consume is slotted. |
| `drainLevel` | 3 |  | The level of the Soul Drain effect applied on targets hit while Soul Consume is slotted. |
| `stealRadius` | 32 |  | The radius in blocks of the held Soul Steal aura. |
| `stealMaxTargets` | 10 |  | Max targets the Soul Steal aura reaps per second. |
| `stealHP` | 0.4 |  | HP fraction a target must be below to be instakilled by the Soul Steal aura. |
| `stealEP` | 0.6 |  | Fraction of the user's max EP a target must be below to be instakilled by the Soul Steal aura. |
| `stealFear` | 2 |  | Fear level a target must have to be instakilled by the Soul Steal aura. |
| `stealDamageMultiplier` | 10 |  | Multiplier of the target's max health dealt as Soul Steal instakill damage. |
| `friendlyFire` | false |  | If true, the Predation mist and Soul Steal aura also affect players in the user's own nation or hunt party. |

## `[VoidSovereign]`

| Option | Default | Range | Description |
|---|---|---|---|
| `IsEnabled` | true |  | Is this Skill Enabled? |
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `domainAuraDrainPerTick` | 5 |  |  |
| `domainConcealmentLevel` | 3 |  |  |
| `domainConcealmentLevelMastered` | 5 |  |  |
| `domainDodgeBonus` | 25 |  |  |
| `domainDodgeInvulnerabilityBonus` | 3 |  |  |
| `domainChantSpeedMultiplier` | 2 |  |  |
| `domainPassiveDamage` | 8 |  |  |
| `domainPassiveDamageMastered` | 16 |  |  |
| `nullSlashMagiculeCost` | 1,500 |  |  |
| `nullSlashDamage` | 150 |  |  |
| `nullSlashDamageMastered` | 300 |  |  |
| `nullSlashSize` | 1.4 |  |  |
| `nullSlashSizeMastered` | 2 |  |  |
| `nullSlashDuration` | 80 |  |  |
| `nullSlashDurationMastered` | 120 |  |  |
| `nullSlashCooldownSeconds` | 1 |  |  |
| `nullSlashCooldownMasteredSeconds` | 1 |  |  |
| `eventHorizonAuraCost` | 3,000 |  |  |
| `eventHorizonRange` | 20 |  |  |
| `eventHorizonRangeMastered` | 35 |  |  |
| `eventHorizonDamageBonus` | 100 |  |  |
| `eventHorizonDamageBonusMastered` | 555 |  |  |
| `eventHorizonDebuffDuration` | 120 |  |  |
| `eventHorizonCooldown` | 30 |  |  |
| `eventHorizonCooldownMastered` | 20 |  |  |
| `soulCollapseMagiculeCost` | 5,000 |  |  |
| `soulCollapseBaseDamage` | 60 |  |  |
| `soulCollapseBaseDamageMastered` | 100 |  |  |
| `soulCollapseChargeMultiplier` | 1.5 |  |  |
| `soulCollapseChargeMultiplierMastered` | 2.5 |  |  |
| `soulCollapseMaxChargeTicks` | 60 |  |  |
| `soulCollapseHitRadius` | 3 |  |  |
| `soulCollapseHitRadiusMastered` | 5 |  |  |
| `soulCollapseCooldown` | 400 |  |  |
| `soulCollapseCooldownMastered` | 260 |  |  |
| `friendlyFire` | false |  | If true, Event Horizon and Soul Collapse also hit players in the user's own nation or hunt party. |

## `[HephaestusSkill]`

| Option | Default | Range | Description |
|---|---|---|---|
| `IsEnabled` | true |  | Is this Skill Enabled? |
| `reforgeCost` | 8,000 |  | Magicule cost to reforge, flat portion. |
| `reforgeCostPerDamage` | 4 |  | Extra magicule per point of durability missing. |
| `reforgeCooldown` | 120 |  | Reforge cooldown in SECONDS. |
| `reforgeScoreMin` | 35 |  | Lowest score a reforge can roll (0-100). Reforge does NOT inherit the item's old score. |
| `reforgeScoreMax` | 95 |  | Highest score a reforge can roll (0-100). |
| `engraveCostPerLevel` | 6,000 |  | Magicule cost per level of the chosen engraving. |
| `engraveCooldown` | 90 |  | Engrave cooldown in SECONDS. |
| `conjureRecipeId` | "forged_high_magisteel_sword" |  | Forge recipe id used as the conjured weapon template. |
| `conjureCost` | 25,000 |  | Magicule cost to conjure. |
| `conjureCooldown` | 600 |  | Conjure cooldown in SECONDS. |
| `conjureDurationTicks` | 6,000 |  | How long a conjured weapon lasts, in ticks (20 ticks = 1 second). |
| `conjureMasteryPerRank` | 8 |  | Forge mastery levels required per quality rank above POOR for the conjured weapon. |
| `hammerBaseDamage` | 12 |  | Base damage of the hammer strike. |
| `hammerDamagePerMastery` | 0.8 |  | Bonus damage per forge mastery level (mastery caps at 50). |
| `hammerDamagePerQualityRank` | 6 |  | Bonus damage per quality rank of the best item ever crafted (0-6). |
| `hammerRange` | 5 |  | Hammer reach in blocks. |
| `hammerAngle` | 60 |  | Hammer cone half-angle in degrees. |
| `hammerCost` | 4,000 |  | Magicule cost per hammer swing. |
| `hammerCooldown` | 4 |  | Hammer cooldown in SECONDS. |
| `chainsRange` | 12 |  | Chains range in blocks. |
| `chainsDurationTicks` | 120 |  | Bound effect duration in ticks. |
| `chainsAmplifier` | 1 |  | Bound effect amplifier (0 = level I). |
| `chainsCost` | 10,000 |  | Magicule cost to cast Chains. |
| `chainsCooldown` | 30 |  | Chains cooldown in SECONDS. |
| `oreSenseRadius` | 24 |  | Ore Sense scan radius in blocks. |
| `oreSenseScanIntervalTicks` | 40 |  | Ticks between Ore Sense rescans. Lower = more responsive, more CPU. |
| `oreSenseDrainPerTick` | 150 |  | Magicule drained per skill tick callback while Ore Sense is toggled on. |
| `divineHandEnabled` | true |  | Enable the once-per-day free minigame stage. |
| `nationBoonQualityFlat` | 3 |  | Flat forge quality points granted to every member of the holder's nation. |
| `friendlyFire` | false |  | If true, Hammer of Creation and Chains of Hephaestus also hit players in the user's own nation or hunt party. |

## `[GaiaSkill]`

| Option | Default | Range | Description |
|---|---|---|---|
| `IsEnabled` | true |  | Is this Skill Enabled? |
| `homeMultiplier` | 1.6 |  | Power multiplier inside your own nation's claimed chunks. |
| `wildMultiplier` | 0.6 |  | Power multiplier on unclaimed land, or when the nation system is off. |
| `hostileMultiplier` | 0.3 |  | Power multiplier inside another nation's claimed chunks. |
| `hostileAtWarMultiplier` | 1 |  | Power multiplier in an enemy claim while at war with that nation. |
| `warLiftsPenalty` | true |  | If false, a declared war does NOT lift the hostile-claim penalty. |
| `friendlyFire` | false |  | Whether Tectonic Spikes and Stone Grasp can hit members of the caster's own nation.<br>False (default) skips them: Bulwark already shields nation allies, so spiking the<br>same teammate the toggle is protecting reads as a bug. Set true for the older<br>behaviour where the cone hits everything except the caster. |
| `spikesCost` | 3,000 |  | Magicule cost of Tectonic Spikes. |
| `spikesCooldown` | 8 |  | Cooldown of Tectonic Spikes, in SECONDS. |
| `spikesDamage` | 45 |  | Base damage per spike hit, before the zone multiplier. |
| `spikesRange` | 12 |  | Base cone length in blocks, before the zone multiplier. |
| `graspCost` | 12,000 |  | Magicule cost of Stone Grasp. |
| `graspCooldown` | 35 |  | Cooldown of Stone Grasp, in SECONDS. |
| `graspRootSeconds` | 5 |  | Base root duration in SECONDS, before the zone multiplier. |
| `graspDamagePerSecond` | 12 |  | Damage dealt per second while rooted, before the zone multiplier. |
| `graspReach` | 32 |  | Maximum targeting distance in blocks. |
| `sculptCost` | 800 |  | Magicule cost of one Sculpt use. |
| `sculptCooldown` | 2 |  | Cooldown of Sculpt, in SECONDS. |
| `veinBloomCost` | 5,000 |  | Magicule cost paid by the caster for one Vein Bloom. |
| `veinBloomCooldown` | 60 |  | Cooldown of Vein Bloom, in SECONDS. |
| `veinBloomSamples` | 24 |  | Random block positions sampled in the chunk per use. |
| `veinBloomChance` | 0.35 |  | Chance each sampled stone block converts to ore. |
| `veinBloomChunkCostPerOre` | 400 |  | Chunk magicule consumed per converted block. |
| `veinBloomDailyCapPerChunk` | 12 |  | Maximum ore blocks Vein Bloom may create in one chunk per in-game day. |
| `veinBloomOreWeights` | "new ArrayList&lt;&gt;(<br>         List.of(<br>            "minecraft:iron_ore\|40",<br>            "minecraft:copper_ore\|30",<br>            "minecraft:coal_ore\|20",<br>            "minecraft:gold_ore\|7",<br>            "minecraft:redstone_ore\|2",<br>            "minecraft:diamond_ore\|1"<br>         )<br>      )" |  | Ore weight table, one entry per line as 'blockid\|weight'. |
| `geomancyCooldown` | 10 |  | Cooldown of Geomancy, in SECONDS. |
| `geomancyTransferAmount` | 2,000 |  | Magicule moved per Geomancy use, clamped by whichever side has less. |
| `geomancyMaxRaisePerUse` | 250 |  | How much one Geomancy use shifts the chunk's magicule CEILING: seeding raises it,<br>draining (sneak) lowers it by the same figure. Hard-capped by the Magicule World<br>entityMagiculeInfluenceChunkCap, and it decays naturally once the chunk stops being<br>seeded. Moves capacity only — never income. |
| `geomancyStripCostPercent` | 0.2 |  | Fraction of the caster's MAXIMUM magicule burned to strip capacity out of a chunk<br>(sneak-Geomancy). Charged per successful strip, on top of nothing being refunded.<br>Deliberately steep: stripping is not claim-gated, so raiding a rival's cultivated<br>ground should cost far more than seeding your own. 0 = free. |
| `bulwarkDrainPerTick` | 1,000 |  | Magicule drained per skill tick (ManasCore ticks skills every 100 game ticks = 5 s) while Bulwark is lit, even when suppressed. |
| `bulwarkRadius` | 12 |  | Radius in blocks within which nation allies share the Bulwark buff. |
| `bulwarkResistanceAmplifier` | 1 |  | Damage-resistance amplifier granted by Bulwark (0 = Resistance I). |
| `reshapeBlockBudget` | 96 |  | Hard cap on blocks a single skill use may change. Safety valve. |
| `reshapeRevertSeconds` | 10 |  | How long raised combat pillars stand, in SECONDS. |
| `requiredNationLevel` | 10 |  | Nation level required to learn Gaia. Ignored when the nation system is off. |
| `requiredClaimedChunks` | 32 |  | Claimed chunks required to learn Gaia, as an alternative to nation level. |

## `[BasiliskSkin]`

| Option | Default | Range | Description |
|---|---|---|---|
| `IsEnabled` | true |  | Is this Skill Enabled? When false it can never be acquired. |
| `epTierPureMagisteel` | 200,000 |  | Max EP at which the armour becomes Pure Magisteel (below: High Magisteel). |
| `epTierAdamantite` | 800,000 |  | Max EP at which the armour becomes Adamantite. |
| `epTierHihiirokane` | 1,000,000 |  | Max EP at which the armour becomes Hihiirokane. |
