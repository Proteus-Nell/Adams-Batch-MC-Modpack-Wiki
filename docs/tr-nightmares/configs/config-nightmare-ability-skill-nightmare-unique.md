# `config/nightmare/ability/skill/nightmare_unique.toml`

<small>[TR: Nightmares](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Sunshine]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `epAcquirement` | 100,000 | |  | EP / magicule obtainment cost to acquire Sunshine. |
| `stormLearnThreshold` | 100 | |  | Learn threshold for Fire Storm. |
| `stormMasteryThreshold` | 200 | |  | Mastery threshold for Fire Storm. |
| `stormRange` | 30 | |  | Maximum targeting range for Storm mode. |
| `stormHitInterval` | 10 | |  | Ticks between each Fire Storm hit. |
| `stormSurgeInterval` | 20 | |  | Ticks between each Fire Storm surge. |
| `stormMagicDamage` | 10 | |  | Secondary magic damage per Fire Storm hit. |
| `stormFireSurgeDamage` | 30 | |  | Fire Storm surge damage. |
| `stormMagicSurgeDamage` | 15 | |  | Secondary surge magic damage. |
| `stormBurnTicks` | 100 | |  | Burn ticks applied by Storm. |
| `spiralHeight` | 5 | |  | Spiral barrier height. |
| `attackBonusSunrise` | 4 | |  | Attack bonus: sunrise |
| `attackBonusDay` | 6 | |  | Attack bonus: day |
| `attackBonusNoon` | 10 | |  | Attack bonus: noon |
| `attackBonusAfternoon` | 6 | |  | Attack bonus: afternoon |
| `attackBonusMoonrise` | -2 | |  | Attack bonus: moonrise |
| `attackBonusNight` | -4 | |  | Attack bonus: night |
| `speedBonusSunrise` | 0.05 | |  | Speed bonus (ADD_MULTIPLIED_TOTAL): sunrise |
| `speedBonusDay` | 0.1 | |  | Speed bonus: day |
| `speedBonusNoon` | 0.2 | |  | Speed bonus: noon |
| `speedBonusAfternoon` | 0.1 | |  | Speed bonus: afternoon |
| `speedBonusMoonrise` | -0.05 | |  | Speed bonus: moonrise |
| `speedBonusNight` | -0.1 | |  | Speed bonus: night |
| `healthBonusSunrise` | 4 | |  | Max health bonus: sunrise |
| `healthBonusDay` | 8 | |  | Max health bonus: day |
| `healthBonusNoon` | 16 | |  | Max health bonus: noon |
| `healthBonusAfternoon` | 8 | |  | Max health bonus: afternoon |
| `healthBonusMoonrise` | -2 | |  | Max health bonus: moonrise |
| `healthBonusNight` | -4 | |  | Max health bonus: night |
| `armorBonusSunrise` | 2 | |  | Armor bonus: sunrise |
| `armorBonusDay` | 4 | |  | Armor bonus: day |
| `armorBonusNoon` | 6 | |  | Armor bonus: noon |
| `armorBonusAfternoon` | 4 | |  | Armor bonus: afternoon |
| `armorBonusMoonrise` | -1 | |  | Armor bonus: moonrise |
| `armorBonusNight` | -2 | |  | Armor bonus: night |
| `rhittaFireResistDuration` | 1,400 | |  | Fire resistance duration when toggled on (ticks). |
| `rhittaFireResistRefresh` | 600 | |  | Fire resistance refresh duration (ticks). |
| `glowingDuration` | 500 | |  | Glowing duration (ticks). |
| `noRhittaDamagePercentage` | 10 | |  | Damage boost percent to Heat, Light and Fire while toggled (no Rhitta). |
| `hasRhittaDamagePercentage` | 25 | |  | Damage boost percent with Rhitta. |

## `[Sunshine.Roar]`

Roar mode: MP, damage, explosion radius (scalar), cooldown (seconds).

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `magiculeCost` | 35 | 50 |  | Current MP (magicule) cost to use this mode or segment. |
| `durationTicks` | 0 | |  | Duration in ticks (effects, zones, projectiles) when applicable. |
| `level` | 0 | |  | Effect amplifier level (0 = I) when applicable. |
| `cooldownTicks` | 3 | 100 |  | Cooldown in ticks after this mode activates. |
| `damage` | 20 | |  | Primary damage when this mode deals damage. |
| `damageMastered` | 0 | |  | Damage when mastered; if 0, 'damage' is used for both. |
| `scalar` | 2 | |  | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `scalar2` | 0 | |  | Second scalar (e.g. secondary radius) when applicable. |

## `[Sunshine.Sun]`

Sun mode: MP, damage, explosion radius (scalar), cooldown (seconds).

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `magiculeCost` | 60 | 80 |  | Current MP (magicule) cost to use this mode or segment. |
| `durationTicks` | 0 | |  | Duration in ticks (effects, zones, projectiles) when applicable. |
| `level` | 0 | |  | Effect amplifier level (0 = I) when applicable. |
| `cooldownTicks` | 5 | 160 |  | Cooldown in ticks after this mode activates. |
| `damage` | 40 | |  | Primary damage when this mode deals damage. |
| `damageMastered` | 0 | |  | Damage when mastered; if 0, 'damage' is used for both. |
| `scalar` | 5 | |  | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `scalar2` | 0 | |  | Second scalar (e.g. secondary radius) when applicable. |

## `[Sunshine.FireStorm]`

Fire Storm mode: MP, primary hit damage, cloud duration (ticks), width/height (scalars), cooldown (seconds).

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `magiculeCost` | 75 | 100 |  | Current MP (magicule) cost to use this mode or segment. |
| `durationTicks` | 200 | |  | Duration in ticks (effects, zones, projectiles) when applicable. |
| `level` | 0 | |  | Effect amplifier level (0 = I) when applicable. |
| `cooldownTicks` | 8 | 200 |  | Cooldown in ticks after this mode activates. |
| `damage` | 20 | |  | Primary damage when this mode deals damage. |
| `damageMastered` | 0 | |  | Damage when mastered; if 0, 'damage' is used for both. |
| `scalar` | 6 | |  | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `scalar2` | 8 | |  | Second scalar (e.g. secondary radius) when applicable. |

## `[Sunshine.Spiral]`

Spiral mode: MP, barrier damage, size (scalar), cooldown (seconds).

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `magiculeCost` | 110 | 150 |  | Current MP (magicule) cost to use this mode or segment. |
| `durationTicks` | 0 | |  | Duration in ticks (effects, zones, projectiles) when applicable. |
| `level` | 0 | |  | Effect amplifier level (0 = I) when applicable. |
| `cooldownTicks` | 25 | 800 |  | Cooldown in ticks after this mode activates. |
| `damage` | 200 | |  | Primary damage when this mode deals damage. |
| `damageMastered` | 0 | |  | Damage when mastered; if 0, 'damage' is used for both. |
| `scalar` | 4.5 | |  | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `scalar2` | 0 | |  | Second scalar (e.g. secondary radius) when applicable. |

## `[Imaginator]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 99,000 | |  | Magicule cost to acquire Imaginator. |
| `kpPerAdvancement` | 1 | |  | Curiosity: knowledge points per completed advancement (unmastered / mastered). |
| `kpPerAdvancementMastered` | 2 | |  |  |
| `analyzeGrantsKp` | true | |  | Analyze: whether analyzing a new entity type grants knowledge points. |
| `analyzeKpDipInterval` | 5 | |  | Analyze: the Nth new entity type grants N knowledge points; every Nth-interval type is a dip instead. |
| `analyzeKpDipMultiplier` | 0.5 | |  | Analyze: multiplier applied on dip types (0.5 = the 5th, 10th, 15th... type gives half). |
| `potencyPerKp` | 0.01 | |  | Vast Imagination: potency gained per knowledge point (0.01 = +1%). |
| `maxPotency` | 3 | |  | Vast Imagination: maximum potency multiplier. |
| `steelArmorPerKp` | 0.5 | |  | Steel Body: armor per knowledge point, and the cap. |
| `steelMaxArmor` | 40 | |  |  |
| `steelReductionPerKp` | 0.5 | |  | Steel Body: physical damage reduction percent per knowledge point, and the cap. |
| `steelMaxReduction` | 60 | |  |  |
| `steelBreakHealthFraction` | 0.3 | |  | Steel Body (mastered): health fraction at which hardening breaks into regeneration. |
| `steelBreakMpFraction` | 0.2 | |  | Steel Body (mastered): fraction of max MP consumed when hardening breaks. |
| `steelUltraspeedKp` | 25 | |  | Steel Body (mastered): knowledge points for Ultraspeed / Infinite Regeneration. |
| `steelInfiniteKp` | 50 | |  |  |
| `steelRegenSeconds` | 60 | |  | Steel Body (mastered): seconds the regeneration skill lasts. |
| `steelBreakCooldown` | 300 | |  | Steel Body (mastered): cooldown in seconds before hardening can break into regeneration again. |
| `cloneBase` | 5 | |  | Clone Creation: base clone cap, +1 per this many knowledge points, and caps (unmastered / mastered). |
| `cloneKpPerExtra` | 10 | |  |  |
| `cloneCap` | 10 | |  |  |
| `cloneCapMastered` | 15 | |  |  |
| `cloneMpFraction` | 0.1 | |  | Clone Creation: fraction of max MP consumed per clone (Body Double uses a tenth). |
| `cloneDeathHealFraction` | 0.1 | |  | Clone Creation: fraction of a clone's max health healed to the user when it dies. |
| `cloneCooldown` | 5 | |  | Clone Creation / Control cooldowns (seconds). |
| `cloneControlCooldown` | 1 | |  |  |
| `analyzeIntrinsicKp` | 5 | |  | Analyze: knowledge points required per skill category. |
| `analyzeCommonKp` | 10 | |  |  |
| `analyzeExtraKp` | 20 | |  |  |
| `analyzeUniqueKp` | 50 | |  |  |
| `analyzeMpCost` | 1,000 | |  | Analyze: magicule cost, cooldown (seconds) and range. |
| `analyzeCooldown` | 20 | |  |  |
| `analyzeRange` | 20 | |  |  |
| `analyzeMinChance` | 0.1 | |  | Analyze: minimum success chance against much stronger targets. |
| `copyMpCost` | 2,500 | |  | Ability Copy: magicule cost per copy, seconds a temporary copy lasts, and cooldown (seconds). |
| `copyDurationSeconds` | 600 | |  |  |
| `copyCooldown` | 3 | |  |  |
| `envWaterSmallKp` | 5 | |  | Environmental Control: knowledge points for each stage (water 3x3, water 5x5, airless, spatial lock). |
| `envWaterLargeKp` | 10 | |  |  |
| `envAirlessKp` | 15 | |  |  |
| `envSpatialLockKp` | 20 | |  |  |
| `envMpPerSecond` | 500 | |  | Environmental Control: magicule cost per second held, range, and cooldown (seconds) after release. |
| `envRange` | 20 | |  |  |
| `envCooldown` | 15 | |  |  |
| `envAirlessDamage` | 6 | |  | Environmental Control: suffocation damage per second in the airless stage (scaled by potency). |
| `envWaterLifetimeTicks` | 100 | |  | Environmental Control: ticks conjured water lingers after it is placed. |

## `[infinitySettings]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `epAcquirement` | 150,000 | |  | EP obtainment cost to acquire Infinity. |
| `magicDamageBoostPercent` | 10 | |  | Magic Damage boost % while Infinity is in-slot (reserved / attribute hooks). |
| `magicDamageBoostId` | "d1a3e2b1-8f2a-4c9b-9f1a-123456789abc" | |  | UUID for Magic Damage boost attribute modifier (TOML has no UUID type; use string). |
| `cancelRange` | 20 | |  | Range for Absolute Cancel targeting. |
| `cancelRadius` | 12 | |  | Radius for AoE Absolute Cancel when shift-used. |
| `learnChance` | 0.15 | |  | Chance to learn magic when exposed to it. |
| `learnChanceMastered` | 0.35 | |  | Chance to learn magic when Infinity is mastered. |
| `copyRangeMagic` | 20 | |  | Range for learning magic from projectiles. |
| `copyCooldownSuccess` | 40 | |  | Cooldown after successfully learning magic from a projectile. |
| `copyCooldownFail` | 20 | |  | Cooldown after failing to learn magic from a projectile. |
| `tensuraMagicFlatBonus` | 20 | |  | Flat bonus damage when using Tensura magic while toggled. |
| `absoluteCancelMagiculeCost` | 0 | |  | Magicule cost for Absolute Cancel (mode 1); 0 = no cost. |
| `absoluteCancelCooldownTicks` | 0 | |  | Cooldown in ticks for Absolute Cancel after use. |

## `[Gift]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `epAcquirement` | 75,000 | |  | EP / magicule obtainment cost to acquire Gift. |
| `giftCreationCooldownTicks` | 100 | |  | Cooldown in ticks after adding a divine protection (Gift Creation, mode 0). |
| `giftCreationMagiculeCost` | 0 | |  | Magicule cost to use Gift Creation (mode 0); 0 disables. |

## `[Stripes]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 40,000 | |  | Magicule Acquirement Cost. |
| `magiculeCostForce` | 2,000 | |  | Magicule Cost to activate or deactivate Force. |
| `magiculeCostObject` | 2,000 | |  | Magicule Cost to activate or deactivate Object. |
| `effectImmunities` | "tensura:disintegration", "tensura:chill", "tensura:frost", "tensura:burden", "tensura:webbed", "minecraft:slowness", "miencraft:mining_fatigue", "minecraft:slow_falling" | |  | List of effects stopped by Force. |
| `forceCooldown` | 10 | |  | Cooldown for activating and deactivating Force in seconds. |
| `objectCooldown` | 10 | |  | Cooldown for activating and deactivating Object in seconds. |
| `objectBlockPercentage` | 50 | |  | Percentage of damage stopped by Object. |
| `forceDamage` | 30 | |  | Damage multiplier for a physical attack to force. |

## `[Lemegeton]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 35,000 | |  | Magicule Acquirement Cost. |
| `magiculeCostSeal` | 50,000 | |  | Magicule Cost to activate Demon Seal. |
| `magiculeStartCostKey` | 5,000 | |  | Magicule Cost to activate Key's Defense. |
| `magiculeCostCancel` | 5,000 | |  | Magicule Cost to activate Magic Cancel. |
| `magiculeCostKey` | 50 | |  | Magicule Cost multiplier for Key's Defense (eg, 50 magicule for 1 damage). |
| `sealCooldown` | 300 | |  | Cooldown for activating Demon Seal. |
| `keyCooldown` | 0 | |  | Cooldown for activating Key's Defense. |
| `cancelCooldown` | 60 | |  | Cooldown for activating Magic Cancel. |
| `cancelDuration` | 300 | |  | Duration of cooldown inflicted by Magic Cancel. |
| `sealMobPercentage` | 80 | |  | What percentage of the user's EP must be greater than the targeted mob for Demon Seal. |
| `sealPlayerPercentage` | 40 | |  | What percentage of the user's EP must be greater than the targeted player for Demon Seal. |
| `damageMultiplier` | 2 | |  | How much are Magic and Holy damage multiplied by the toggle. |
| `learningPoint` | 1,000 | |  | Learning point boost for spells |
| `masteryPoint` | 1,000 | |  | Mastery point gain for Spells |

## `[Ending]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 44,444 | |  | Magicule Acquirement Cost. |
| `magiculeCostPull` | 4,444 | |  | Magicule Cost to activate No Escape. |
| `magiculeCostDoor` | 4,444 | |  | Magicule Cost to activate Death's Door. |
| `pullDamage` | 44 | |  | Damage dealt by no escape. |
| `pullCooldown` | 44 | |  | Cooldown for activating No Escape. |
| `doorCooldown` | 444 | |  | Cooldown for activating Death's Door. |
| `healCooldown` | 1 | |  | Cooldown for removing cook and altered cooked damage automatically. |

## `[Processor]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 40,000 | |  | Magicule Acquirement Cost. |
| `magiculeCostAllocate` | 1,000 | |  | Magicule Cost to activate Allocate. |
| `magiculeCostClock` | 15,000 | |  | Magicule Cost to activate Overclock. |
| `defaultThreads` | 2 | |  | Base number of Threads |
| `masteryThreads` | 3 | |  | Number of Threads on Mastery. |
| `allocateCooldown` | 10 | |  | Cooldown for activating Allocate. |
| `clockBuffTime` | 40 | |  | How long overclock buffs user at base. |
| `clockBuffPerc` | 30 | |  | The base percentage of the overclock buff. |
| `clockCooldown` | 300 | |  | How long the skill is disabled after using overclock in seconds. |
| `iFrameBuff` | 1 | |  | How many frames of invulnerability dodging is buffed by per thread. |
| `castBuff` | 2 | |  | CastingTime buff per thread. |

## `[SoulShrine]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 75,000 | |  | Magicule Acquirement Cost. |
| `magiculeCostFist` | 100 | |  | Magicule Cost to Divergent Fist or Cursed Energy reinforcement. |
| `magiculeCostSimple` | 2,000 | |  | Magicule Cost to activate Simple Domain. |
| `divergentDamage` | 1.5 | |  | Damage multiplier dealt by divergent unmastered. |
| `reinforcementDamage` | 2 | |  | Damage dealt by reinforcement mastered. |
| `divergentCooldown` | 2 | |  | Cooldown for activating Divergent Fist minus one. |
| `reinforcementCooldown` | 0 | |  | Cooldown for activating Reinforcement minus one. |
| `simpleDuration` | 30 | |  | How long simple domain lasts in seconds. |
| `simpleDurationMastered` | 60 | |  | How long simple domain lasts in seconds with mastery. |
| `simpleCooldown` | 120 | |  | Cooldown for Simple Domain. |
| `flashChance` | 1 | |  | Chance out of 100 for a physical attack to trigger a black flash without mastery. |
| `flashChanceMastered` | 5 | |  | Chance out of 100 for a physical attack to trigger a black flash with mastery. |
| `flashZoneChance` | 20 | |  | How much having Zone effect increases chances out of 100. |
| `effectImmunities` | "tensura:black_burn", "tensura:spatial_blockade", "tensura:soul_drain" | |  | List of effects User is immune to. |
| `simpleResistance` | 50 | |  | Percentage of magical and spiritual damage resisted when in simple domain. |
| `flashMultiplier` | 2.5 | |  | Damage multiplier on an attack with black flash. |

## `[Handler]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 75,000 | |  | Magicule Acquirement Cost. |
| `magiculeAttributes` | 100 | |  | Magicule Cost to upgrade attributes. |
| `magiculeCostUpgrade` | 2,000 | |  | Magicule Cost to upgrade a skill. |
| `attributeCooldown` | 30 | |  | Cooldown for upgrading attributes. |
| `upgradeCooldown` | 120 | |  | Cooldown for upgrading a skill mode. |
| `attributeMultiplier` | 0.5 | |  | Multiplier buff applied to base attributes (0.5 is 1.5x base, 1.5 is 2.5x base). |
| `allowedSkills` | "tensura:cook", "trnightmare:concentrator", "trnightmare:ideal", "trnightmare:avalon", "tensura:gravity_field", "tensura:water_blade", "tensura:hero_haki" | |  | List of skills Handler is allowed to upgrade. (is every skill it can by default) |
| `masteryGainMultiplier` | 2 | |  | Mastery gained per skill altered. |

## `[Robotnic]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 65,000 | |  | Magicule Acquirement Cost. |
| `magiculeCostItem` | 100 | |  | Magicule Cost to take apart an item. |
| `magiculeCostData` | 2,000 | |  | Magicule Cost to take apart a skill. |
| `mpGain` | 0.3 | |  | Magicule gain multiplier for deconstructing skills. |
| `mpGainMastered` | 0.5 | |  | Magicule gain multiplier for deconstructing skills on mastery. |
| `apGain` | 0.5 | |  | Aura gain multiplier for deconstructing itemss. |
| `apGainMastered` | 0.75 | |  | Aura gain multiplier for deconstructing items on mastery. |
| `itemCooldown` | 30 | |  | Cooldown for deconstructing Items. |
| `skillCooldown` | 120 | |  | Cooldown for deconstructing skills. |

## `[CoffinOfDarkness]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 100,000 | |  | Magicule Acquirement Cost. |
| `magiculeCostCounter` | 50,000 | |  | Magicule Cost to activate Full Counter. |
| `magiculeCostSlayer` | 5,000 | |  | Magicule Cost to activate Divine Slater. |
| `counterCooldown` | 5 | |  | Cooldown for activating Full Counter. |
| `slayerCooldown` | 60 | |  | Cooldown for activating Divine Slayer. |
| `assaultCooldown` | 1,200 | |  | Cooldown for reviving with Assault Mode. |
| `assaultDuration` | 400 | |  | Duration of Assault Mode after revival. |
| `reflectMultiplierUnmastered` | 2 | |  | Damage multiplier on reflected attacks when not mastered. |
| `reflectMultiplierMastered` | 4 | |  | Damage multiplier on reflected attacks when mastered. |

## `[Snatch]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 100,000 | |  | Magicule Acquirement Cost. |
| `presenceLevel` | 11 | |  | Level of Presence Concealment. |
| `foxCooldown` | 40 | |  | Cooldown for Fox Hunt Unmastered. |
| `foxCooldownMastered` | 20 | |  | Cooldown for Fox Hunt Mastered. |
| `foxRange` | 10 | |  | Range of Fox Hunt in blocks. |
| `maxAbsorbPercentage` | 50 | |  | What percentage of an enemy's max magicules are absorbed when they are eaten. |
| `multiPhysCooldown` | 30 | |  | Cooldown for multi target Physical Hunt. |
| `singlePhysCooldown` | 10 | |  | Cooldown for single target Physical hunt. |
| `physicalRange` | 20 | |  | Range of Physical Hunt in blocks. |
| `touchAbsorbPercentage` | 1 | |  | What percentage of an enemy's magicules are absorbed when they are touched. |
| `attackPercentage` | 75 | |  | What percentage of the enemy's attack damage does the user gain from Physical Hunt. |

## `[Glorious]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 75,000 | |  | Magicule Acquirement Cost. |
| `regenCostMultiplier` | 0.5 | |  | Magicule Cost multiplier for ultraspeed regen. |
| `dodgeChanceIgnore` | 50 | |  | Dodge ignoring chance. |
| `presenceSense` | 2 | |  | Level of Presence Sense. |
| `learningPoint` | 4 | |  | Learning point boost for skills |
| `masteryPoint` | 4 | |  | Mastery point gain for Skills |

## `[Elegy]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 90,000 | |  | Magicule Acquirement Cost. |
| `refinementMultiplier` | 2 | |  | Multiplier for Barrier Refinement. |
| `magiculeCostCounter` | 100 | |  | Magicule Cost to activate Counter Barrier. |
| `barrierCostCounter` | 100 | |  | Barrier Cost to activate Counter Barrier. |
| `stabilityMagicule` | 100 | |  | Magicules per Barrier point from Stability. |
| `stabilityHealth` | 5 | |  | Health per Barrier point from Stability. |
| `counterCooldown` | 10 | |  | Cooldown for activating Counter Barrier. |
| `stabilityCooldown` | 60 | |  | Cooldown for activating Stability. |

## `[SentientBeing]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 95,000 | |  | Magicule Acquirement Cost. |
| `abundanceMultiplier` | 2 | |  | Multiplier for Magicule Regeneration via Abundance. |
| `snackmultiplier` | 5 | |  | Multiplier for Magicule Regeneration via Snack For Later (doubled on mastery). |
| `bondsCooldown` | 120 | |  | Cooldown for activating Family Bonds!. |

## `[Breaker]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 90,000 | |  | Magicule Acquirement Cost for Breaker. |
| `BreakerMPRegenMulti` | 20 | |  | Magicule regen multiplier while Boundary Breaker is active (mode 0). |
| `BreakerAPRegenMulti` | 20 | |  | Aura regen multiplier while Boundary Breaker is active (mode 0). |

## `[Investigator]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 75,000 | |  | Magicule Acquirement Cost. |
| `appraisalLevel` | 5 | |  | Level of Analytical Appraisal. |
| `appraisalLevelMastered` | 15 | |  | Level of Analytical Appraisal when Mastered. |
| `critChance` | 30 | |  | Critical Attack chance. |
| `dodgeChanceIgnore` | 40 | |  | Dodge ignoring chance. |
| `dodgeChance` | 50 | |  | Dodge chance. |
| `dodgeChanceProjectile` | 25 | |  | Projectile dodge chance. |
| `surpriseBlocks` | "minecraft:tnt", "minecraft:tnt_minecart", "minecraft:end_crystal", "minecraft:trapped_chest", "minecraft:powdered_snow", "minecraft:sculk_sensor" | |  | List of blocks highlighted by Pursuit of Surprise. |
| `treasureBlocks` | "tensura:charybdis_core", "minecraft:chest", "minecraft:barrel", "minecraft:dragon_egg", "minecraft:ancient_debris", "tensura:magic_ore" | |  | List of blocks highlighted by Pursuit of Treasure. |
| `tutelageCooldown` | 60 | |  | Cooldown for Pursuit of Tutelage. |
| `presenceSense` | 3 | |  | The level of Presence Sense when activated. |
| `presenceRadius` | 20 | |  | The bonus Presence Sense Radius when activated. |
| `learningPoint` | 10 | |  | Learning point boost for skills |
| `masteryPoint` | 10 | |  | Mastery point gain for Skills |

## `[Carnation]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 295,000 | |  | Magicule Acquirement Cost. |
| `essenceRequirementDragon` | 10 | |  | Dragon Essence requirement. |
| `abundanceMultiplier` | 2 | |  | Multiplier for Magicule Regeneration via Abundance. |
| `snackmultiplier` | 5 | |  | Multiplier for Magicule Regeneration via Snack For Later (doubled on mastery). |
| `recoveryCooldown` | 10 | |  | Cooldown for activating Recovery. |
| `bondsCooldown` | 120 | |  | Cooldown for activating Family Bonds!. |
| `recoveryCost` | 90 | |  | Magicule cost of Recovery per HP healed while unmastered. |
| `recoveryCostMastered` | 45 | |  | Magicule cost of Recovery per HP healed while mastered. |
| `recoveryCostSHP` | 70 | |  | Magicule cost of Recovery per SHP healed. |
| `predationRange` | 10 | |  | The max range in block of the Predation Mode. |
| `predationRangeMastered` | 15 | |  | The max range in block of the Predation Mode when mastered. |
| `predationDamage` | 100 | |  | The attack damage of the Predation Mode. |
| `corrosionSpeedMultiplier` | 0.5 | |  | Activation Speed Multiplier when activating the Corrosion Mode. |
| `predationEPDrain` | 1,000 | |  | The amount of EP that the user drains from target using the Predation Mode. |
| `predationSkillChance` | 30 | |  | The chance to obtain skills from targets without killing them with the Predation Mode. |
| `predationSkillNumber` | 3 | |  | The number of skills to gain from targets at a time without killing them with the Predation Mode. |
| `predationCorrosionDuration` | 100 | |  | The duration in tick of the Corrosion effect applied by the Predation Mode. |
| `predationCorrosionLevel` | 2 | |  | The level of the Corrosion effect applied by the Predation Mode. |
| `predationEPSteal` | 0.5 | |  | The multiplier of the target's EP to be turned into the user's EP when killed with the Predation Mode. |

## `[Saint]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 95,000 | |  | Magicule Acquirement Cost. |
| `spiritronReqPercent` | 90 | |  | Percentage of magicules required to generate Spiritron Points. |
| `spGenerationDefault` | 1 | |  | Number of Spiritrons generated (Unmastered). |
| `spGenerationMastered` | 5 | |  | Number of Spiritrons generated (Mastered). |
| `spPurifyRequirement` | 50 | |  | Spiritron Points required to purify attacks. |
| `purifyDamage` | 20 | |  | Amount of Holy Damage dealt by physical attacks (Doubled on mastery). |
| `miracleBuff` | 25 | |  | Amount Holy damage is buffed by Holy Miracle. |
| `miracleBuffMastered` | 75 | |  | Amount Holy damage is buffed by Holy Miracle when mastered. |
| `miracleDebuff` | 50 | |  | Amount of damage dealt to user by Holy Miracle. |
| `miracleDebuffMastered` | 25 | |  | Amount of damage dealt to user by Holy Miracle when mastered. |
| `spDisintegrationRequirement` | 75 | |  | Spiritron Points required to cast Disintegration. |
| `mpDisintegrationRequirement` | 25,000 | |  | Magicules required to cast Disintegration. |
| `disintegrationDamage` | 150 | |  | Amount of damage dealt by disintegration. |
| `meltDamage` | 75 | |  | Amount of Holy damage dealt by Melt Cut. |
| `meltCooldown` | 1 | |  | Cooldown of Melt Cut. |

## `[freezingFlame]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 90,000 | |  |  |
| `maxMastery` | 1,000 | |  |  |
| `coatingDamage` | 50 | |  |  |
| `coatingDamageMastered` | 100 | |  |  |
| `magiculeCostAfterWorld` | 5,000 | |  |  |
| `magiculeCostWhiteFlame` | 0 | |  |  |

## `[Tempter]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 90,000 | |  |  |
| `seekerMasteredSkills` | 50 | |  |  |
| `tempterMasteredSpells` | 50 | |  |  |
| `solicitationLearnPoints` | 300 | |  |  |
| `endOfWorldLearnPoints` | 500 | |  |  |
| `copyChance` | 35 | |  |  |
| `copyChanceMastered` | 75 | |  |  |
| `copyCooldown` | 15 | |  |  |

## `[Ruler]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 100,000 | |  |  |
| `maxMastery` | 1,000 | |  |  |
| `maxCurseSeals` | 16 | |  |  |

## `[Summoner]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 90,000 | |  |  |
| `maxMastery` | 1,000 | |  |  |
| `maxSummonEntries` | 12 | |  |  |
| `summonRange` | 16 | |  |  |

## `[Stealer]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 95,000 | |  |  |
| `maxMastery` | 1,000 | |  |  |
| `energyTheftChance` | 0.1 | |  |  |
| `energyTheftFraction` | 0.005 | |  |  |
| `plunderCooldownTicks` | 300 | |  |  |
| `plunderMaxSkills` | 10 | |  |  |

## `[Designer]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 95,000 | |  |  |
| `slothMasteredSkillsRequired` | 100 | |  | Mastered skills required for the alternate Sloth path to obtain Designer. |
| `slothBedMinutesRequired` | 60 | |  | Minutes spent standing still on a bed for the alternate Sloth path to obtain Designer. |
| `byDesignLearningBonus` | 6 | |  |  |
| `copyRange` | 12 | |  |  |
| `copyChance` | 35 | |  |  |
| `copyChanceMastered` | 65 | |  |  |
| `copyCooldown` | 60 | |  |  |
| `recycleBonusChance` | 0.05 | |  |  |
| `recycleBonusChanceMastered` | 0.1 | |  |  |
| `recycleBonusMpFraction` | 0.1 | |  |  |
| `recycleBonusMpFractionMastered` | 0.2 | |  |  |
| `furnaceRestorePercent` | 0.03 | |  | Magicule Furnace: fraction of max MP restored per second (normal / mastered). |
| `furnaceRestorePercentMastered` | 0.05 | |  |  |
| `furnaceMaxMpPercent` | 2.25 | |  | Magicule Furnace: max MP the furnace can charge to, as a multiple of the user's max MP (2.25 = 225%). |
| `apocryphaDrainPercent` | 0.08 | |  | Apocrypha: fraction of max MP drained every 2 seconds (normal / mastered). |
| `apocryphaDrainPercentMastered` | 0.06 | |  |  |
| `apocryphaAtkBonus` | 10 | |  | Apocrypha: flat attack damage bonus (normal / mastered). |
| `apocryphaAtkBonusMastered` | 30 | |  |  |
| `apocryphaArmorBonus` | 15 | |  | Apocrypha: flat armor bonus (normal / mastered). |
| `apocryphaArmorBonusMastered` | 30 | |  |  |
| `divineDarknessDamage` | 50 | |  | Divine Darkness: Holy + Darkness damage per second (normal / mastered). |
| `divineDarknessDamageMastered` | 100 | |  |  |
| `divineDarknessMpCostPercent` | 0.035 | |  | Divine Darkness: fraction of max MP drained per second. |

## `[DeadlyPoison]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 90,000 | |  |  |
| `detectWeaknessPerHit` | 1 | |  |  |
| `weaknessThresholdLow` | 30 | |  |  |
| `weaknessThresholdMid` | 50 | |  |  |
| `weaknessThresholdHigh` | 80 | |  |  |
| `bloodyBiteMpCost` | 500 | |  |  |
| `bloodyBiteRange` | 4 | |  |  |
| `bloodyBitePhysicalDamage` | 40 | |  |  |
| `bloodyBiteSpiritualDamage` | 40 | |  |  |
| `refinementPercentPerSecond` | 2.5 | |  |  |
| `refinementPercentPerSecondMastered` | 5 | |  |  |
| `refinementMpPerSecond` | 80 | |  |  |
| `domainShpDamage` | 500 | |  |  |
| `domainShpDamageMastered` | 1,000 | |  |  |
| `domainNonSpiritualDamage` | 500 | |  |  |
| `domainNonSpiritualDamageMastered` | 1,000 | |  |  |
| `cursedPoisonRange` | 6 | |  |  |
| `cursedPoisonLearnPoints` | 300 | |  |  |
| `cursedPoisonDurationTicks` | 6,000 | |  |  |
| `cursedPoisonCooldownSeconds` | 120 | |  |  |
| `cursedKillEpBonusFraction` | 0.1 | |  |  |

## `[lunatic]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 85,000 | |  | MP cost to obtain Lunatic. |
| `maxMastery` | 1,000 | |  | Max mastery. |
| `fracturedMindInsanityLevel` | 3 | |  | Fractured Mind: Insanity level applied while toggled. |
| `fracturedMindMasteredInsanityLevel` | 5 | |  | Fractured Mind: Insanity level applied while toggled when mastered. |
| `hystericalStrengthPerInsanity` | 1 | |  | Hysterical Strength: Strengthened levels gained per Insanity level. |
| `hystericalStrengthMasteredPerInsanity` | 2 | |  | Hysterical Strength: Strengthened levels gained per Insanity level when mastered. |
| `lucidMindHpPerInsanity` | 50 | |  | Lucid Mind: HP restored per consumed Insanity level. |
| `lucidMindShpPerInsanity` | 100 | |  | Lucid Mind: SHP restored per consumed Insanity level. |
| `lucidMindMasteredHpPerInsanity` | 100 | |  | Lucid Mind: HP restored per consumed Insanity level when mastered. |
| `lucidMindMasteredShpPerInsanity` | 200 | |  | Lucid Mind: SHP restored per consumed Insanity level when mastered. |
| `lucidMindCooldownSeconds` | 10 | |  | Lucid Mind cooldown in seconds. |
| `induceDeliriumChance` | 0.25 | |  | Induce Delirium: chance to apply Delirium on hit while the user has Insanity. |
| `induceDeliriumDurationTicks` | 600 | |  | Induce Delirium: Delirium duration in ticks. |
| `induceDeliriumAmplifier` | 0 | |  | Induce Delirium: Delirium amplifier. |
| `induceDeliriumMasteredAmplifier` | 1 | |  | Induce Delirium: Delirium amplifier when mastered. |
| `psychosisRange` | 12 | |  | Psychosis: radius in blocks. |
| `psychosisIntervalTicks` | 600 | |  | Psychosis: ticks between Insanity pulses while held. |
| `psychosisMaxInsanityLevel` | 5 | |  | Psychosis: maximum Insanity level it can build targets to. |

## `[cultist]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 75,000 | |  | MP cost to obtain Cultist. |
| `maxMastery` | 1,000 | |  | Max mastery. |
| `joySpiritualDamageMultiplier` | 0.5 | |  | Joy In Service: spiritual damage multiplier while in slot. |
| `joyKillSacrificePoints` | 1 | |  | Joy In Service: sacrifice points gained for mob kills while insane. |
| `insanityToggleLevel` | 3 | |  | Insanity toggle: Insanity level applied. |
| `greaterGoodEpFraction` | 0.15 | |  | Greater Good: EP fraction gained from subordinates killed by outside sources when mastered. |
| `praiseHpCost` | 10 | |  | Praise: HP damage to self. |
| `praiseShpCost` | 20 | |  | Praise: SHP damage to self. |
| `praiseSacrificePoints` | 4 | |  | Praise: sacrifice points generated. |
| `praiseCooldownSeconds` | 5 | |  | Praise cooldown in seconds. |
| `carnageDamagePerPoint` | 2 | |  | Carnage: spiritual damage dealt per sacrifice point. |
| `carnageDamageCap` | 100 | |  | Carnage: maximum spiritual damage added per hit. |

## `[elementalist]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 60,000 | |  | EP / magicule obtainment cost. |
| `passiveBoost` | 0.3 | |  | Passive elemental damage boost while toggled (not mastered). |
| `passiveBoostMastered` | 0.4 | |  | Passive elemental damage boost while toggled (mastered). |
| `connectionBoost` | 20 | |  | Connection boost per stack (not mastered). |
| `connectionBoostMastered` | 40 | |  | Connection boost per stack (mastered). |

## `[lordOfMagewolves]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 55,000 | |  | Magicule obtainment cost. |
| `maxMastery` | 1,000 | |  | Max mastery. |

## `[dominator]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 90,000 | |  | Magicule obtainment cost. |
| `maxMastery` | 1,000 | |  | Max mastery. |

## `[endorse]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 90,000 | |  | Magicule obtainment cost. |
| `maxMastery` | 1,000 | |  | Max mastery. |
| `stockpileCooldownSeconds` | 5 | |  | Stockpile mode cooldown (Tensura seconds). |

## `[imitator]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 75,000 | |  | Magicule obtainment cost. |
| `learnRequired` | 100 | |  | Learn progress required before disguise is available. |
| `epGateRatio` | 0.5 | |  | Maximum target EP ratio allowed for player disguises (target EP must be &lt;= user EP \* ratio). |
| `mimicryEpMaxDifference` | 0.3 | |  | When learning via Mimicry pulses, block learning if the target's EP is greater than the user's EP by this fraction (e.g., 0.3 = 30% higher -&gt; block). |
| `mimicryAllowUniqueAndUltimate` | false | |  | Allow Mimicry learning pulses to include Unique and Ultimate skills when true. Default false for balance. |

## `[babylon]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 80,000 | |  | Magicule obtainment cost. |
| `maxMastery` | 1,000 | |  | Max mastery. |

## `[changingStar]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 120,000 | |  | Magicule obtainment cost. |
| `maxMastery` | 1,000 | |  | Max mastery. |
| `radiantRestorationMagiculeCost` | 500 | |  | Magicule cost per tick for Radiant Restoration when active. |
| `auraOfInspirationMagiculeCost` | 500 | |  | Magicule cost for Aura of Inspiration pulses. |
| `incandescentActivationMagiculeCost` | 10,000 | |  | Activation cost for Incandescent Augment. |
| `incandescentDamageBonus` | 10 | |  | Base melee damage bonus from Incandescent Augment. |
| `incandescentDamageBonusMastered` | 15 | |  | Mastered melee damage bonus from Incandescent Augment. |
| `incandescentAttackSpeedBonus` | 1 | |  | Base attack speed bonus from Incandescent Augment. |
| `incandescentAttackSpeedBonusMastered` | 1.5 | |  | Mastered attack speed bonus from Incandescent Augment. |
| `incandescentKnockbackBonus` | 0.3 | |  | Base knockback bonus from Incandescent Augment. |
| `incandescentKnockbackBonusMastered` | 0.5 | |  | Mastered knockback bonus from Incandescent Augment. |
| `auraRadius` | 12 | |  | Radius for Aura of Inspiration. |
| `inspirationDurationTicks` | 200 | |  | Duration in ticks for the inspiration aura effect. |
| `flameOfLongingConversion` | 0.5 | |  | Flame of Longing half-damage conversion factor. |

## `[Laguna]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `bannedSkills` | [] (empty) | |  | List of banned Laguna Skills. |
| `allowedSkills` | "trnightmare:dark_blessing", "trnightmare:earth_blessing", "trnightmare:fire_blessing", "trnightmare:gathering_spirits_blessing", "trnightmare:judgement_blessing", "trnightmare:lakes_blessing", "trnightmare:light_blessing", "trnightmare:sandplay_blessing", "trnightmare:shedding_blood_blessing", "trnightmare:time_blessing", "trnightmare:water_blessing", "trnightmare:wind_blessing", "trnightmare:unarmed_combat_blessing", "trnightmare:wind_reading", "trnightmare:wind_evasion", "trnightmare:sky_enjoyer", "trnightmare:insensitivity", "trnightmare:durability", "trnightmare:food_lover" | |  | Permitted Laguna Skills. |
| `swordSaintEpAcquirement` | 100,000 | |  | EP obtainment cost for Laguna Sword Saint. |
| `phoenixEpAcquirement` | 100,000 | |  | EP obtainment cost for Laguna Phoenix. |
| `deathGodEpAcquirement` | 500,000 | |  | EP obtainment cost for Laguna Death God ultimate. |
| `deathGodLearningCost` | 2,000 | |  | Learning cost for Laguna Death God. |
| `phoenixNextEpAcquirement` | 250,000 | |  | EP obtainment cost for Laguna Phoenix Next ultimate. |
| `phoenixNextLearningCost` | 2,000 | |  | Learning cost for Laguna Phoenix Next. |

## `[projectionSorcery]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `epAcquirement` | 100,000 | |  | EP / magicule obtainment cost to acquire Projection Sorcery. |
| `learningCost` | 1,000 | |  | Learning / mastery cost. |
| `maxMastery` | 1,000 | |  | Max mastery. |
| `framesUpkeepMagiculeCost` | 6 | |  | Magicule cost each upkeep check while toggled on. |
| `framesUpkeepIntervalTicks` | 20 | |  | Ticks between energy upkeep checks while toggled. |
| `barrageCooldownSeconds` | 10 | |  | Cooldown in seconds for 360 Barrage (mode 0). |
| `speedBlitzCooldownSeconds` | 15 | |  | Cooldown in seconds for Speed Blitz (mode 1). |
| `breakerCooldownSeconds` | 2 | |  | Cooldown in seconds for Breaker (mode 2). |
| `failCooldownSeconds` | 1 | |  | Cooldown in seconds when an aimed mode fails (no valid target). |
| `sprintBuildupTicks` | 200 | |  | Sprint ticks to fully charge projection speed multiplier. |
| `speedRampMaxBonus` | 4 | |  | Bonus to speed multiplier at full sprint charge (max mult = 1 + this). |
| `stepHeightFromSprintMax` | 5 | |  | Step height from sprint (ADD_VALUE) at full charge = progress \* this. |
| `toggledAttackSpeedMultBonus` | 1.5 | |  | Attack speed bonus while toggled |
| `highSpeedThreshold` | 2 | |  | Speed mult at/above which step surge apply |
| `stepSurgeMin` | 0.35 | |  | Minimum extra step height at the high-speed threshold. |
| `stepSurgeExtra` | 1.65 | |  | Extra step height added from threshold to max projection speed. |
| `barrageStrikes` | 60 | |  | 360 Barrage: strike count. |
| `barrageDurationTicks` | 100 | |  | 360 Barrage: total session duration in ticks (timing spread across strikes). |
| `barrageOrbitLoops` | 8 | |  | 360 Barrage: full orbit loops around target over all strikes. |
| `barrageOrbitRadius` | 1.6 | |  | 360 Barrage: orbit radius in blocks. |
| `combatModeTargetRange` | 24 | |  | 360 Barrage / Speed Blitz: raycast targeting range. |
| `barrageDamageMultNormal` | 2.5 | |  | 360 Barrage: total damage multiplier vs base punch when not mastered. |
| `barrageDamageMultMastered` | 5 | |  | 360 Barrage: total damage multiplier vs base punch when mastered. |
| `speedBlitzDamageMultNormal` | 4 | |  | Speed Blitz: total damage multiplier vs base punch when not mastered. |
| `speedBlitzDamageMultMastered` | 8 | |  | Speed Blitz: total damage multiplier vs base punch when mastered. |
| `speedBlitzStrikes` | 18 | |  | Speed Blitz: strike count. |
| `speedBlitzDurationTicks` | 80 | |  | Speed Blitz: total session duration in ticks. |
| `speedBlitzPasses` | 6 | |  | Speed Blitz: number of approach directions (theta slots). |
| `speedBlitzHitsPerPass` | 3 | |  | Hits per pass before advancing theta. |
| `speedBlitzApproachBlocks` | 11 | |  | Speed Blitz: approach distance from target along pass axis (blocks). |
| `speedBlitzFinisherKnockXZ` | 1.6 | |  | Speed Blitz: horizontal knock on finisher. |
| `speedBlitzFinisherKnockY` | 0.45 | |  | Speed Blitz: vertical knock on finisher. |
| `breakerTargetRange` | 12 | |  | Breaker: targeting range (blocks). |
| `breakerSlapFraction` | 0.25 | |  | Breaker: first hit uses min(baseMelee \* this, cap). |
| `breakerSlapDamageCap` | 6 | |  | Breaker: cap on first slap damage. |
| `breakerSecondHitDamage` | 30 | |  | Breaker: second hit flat damage. |
| `breakerKnockXZ` | 1.35 | |  | Breaker: knockback XZ scale on target. |
| `breakerKnockY` | 0.4 | |  | Breaker: knockback Y on target. |
| `breakerExplosionSpeedScale` | 2 | |  | Breaker: explosion size = clamp(this \* (speedMult - 1), min, max). |
| `breakerExplosionMin` | 0.5 | |  | Breaker: minimum explosion radius. |
| `breakerExplosionMax` | 8 | |  | Breaker: maximum explosion radius. |
| `projectionGlassDurationTicks` | 20 | |  | Projection Glass duration from Breaker / on-hit (ticks), not mastered. |
| `projectionGlassDurationTicksMastered` | 60 | |  | Projection Glass duration when mastered (ticks). |
| `projectionGlassOnReceiveDurationTicks` | 60 | |  | Projection Glass duration when you take damage while toggled (ticks). |
| `ramMinSprintTicks` | 50 | |  | Ram hits: minimum sprint buildup ticks before ram damage can proc. |
| `ramSearchInflate` | 1 | |  | Ram: AABB inflation for finding targets (blocks). |
| `ramDamageMultiplier` | 0.875 | |  | Ram: damage multiplier vs base melee. |
| `onAttackGlassProcRoll` | 20 | |  | On-attack Projection Glass proc: roll 1 in this (higher = rarer). |
| `perTargetCollisionCooldownTicks` | 4 | |  | Per-entity cooldown for ram hits, on-hit glass proc, etc. (ticks). |
| `glassOnReceiveChanceBase` | 30 | |  | Chance (0-100) to apply Projection Glass when damaged while toggled (base). |
| `glassOnReceiveChancePainRes` | 15 | |  | Chance when target has Pain Resistance. |
| `glassOnReceiveChancePainNull` | 5 | |  | Chance when target has Pain Nullification. |
| `trailCatchupTicks` | 96 | |  | Trail: ticks of visual catch-up after sprint stops. |
| `framePhasePerTick` | 24 | |  | Trail: frame phase added per tick while trail runs. |
| `trailChimeSpeedClampMin` | 1.05 | |  | Trail chime interval clamps: minimum speed mult. |
| `solarBurstParticleMinSpeed` | 2.1 | |  | Solar burst particles: minimum speed mult. |
| `solarBurstParticleRoll` | 30 | |  | Solar burst: roll 1 in this each ambient tick when above min speed. |
| `waterTreadMinHorizontalSpeedSq` | 0.06 | |  | Water skim: minimum horizontal speed squared to engage. |
| `waterTreadSurfaceBandTop` | 0.15 | |  | Water skim: max feet above fluid surface (blocks). |
| `waterTreadSurfaceBandBottom` | 0.65 | |  | Water skim: max feet below fluid surface (blocks). |
| `waterTreadNudgeFactor` | 0.4 | |  | Water skim: nudge toward surface (blocks per tick factor). |
| `waterTreadOnGroundEpsilon` | 0.22 | |  | Water skim: treat as on-ground when feet within this of surface (blocks). |
| `meleePocketRange` | 2.5 | |  | Fallback melee target search radius when raycast misses (blocks). |
| `magiculeCostBarrage` | 75 | |  | Magicule cost: 360 Barrage (mode 0). |
| `magiculeCostSpeedBlitz` | 125 | |  | Magicule cost: Speed Blitz (mode 1). |
| `magiculeCostBreaker` | 40 | |  | Magicule cost: Breaker (mode 2). |
| `trailVisibleMinSpeedMult` | 1.25 | |  | Trail: minimum speed mult before any afterimage slots appear. |
| `trailVisibleMaxSpeedMult` | 3 | |  | Trail: upper speed mult for scaling slot count (pairs with speedRamp max). |
| `trailHistoryStrideStep` | 0.5 | |  | Trail: history stride step per 0.5 speed above trailVisibleMinSpeedMult. |
| `trailHistoryStrideMaxExtra` | 4 | |  | Trail: max extra history indices to skip (0-4). |

## `[stasis]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `epAcquirement` | 70,000 | |  | EP / magicule obtainment cost to acquire Stasis. |
| `learningCost` | 1,000 | |  | Learning / mastery point cost. |
| `maxMastery` | 1,000 | |  | Max mastery. |
| `fixedStateCooldownSeconds` | 60 | |  | Fixed State: cooldown in seconds |
| `fixedStateDurationTicks` | 600 | |  | Fixed State: effect duration (ticks) |
| `airWallMagiculePerSecond` | 1,000 | |  | Air Wall: magicules drained per second while held. |
| `airWallHalfSize` | 2.5 | |  | Air Wall: horizontal half-size of the wall (blocks) |
| `airWallCenterDistance` | 2.75 | |  | Air Wall: distance in front of the caster (blocks) |
| `airWallThickness` | 0.35 | |  | Air Wall: thickness along the facing axis (blocks). |

## `[cadence]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `epAcquirement` | 170,000 | |  | EP / magicule obtainment cost to acquire Cadence (evolution of Stasis). |
| `learningCost` | 1,000 | |  | Learning / mastery point cost. |
| `maxMastery` | 1,000 | |  | Max mastery. |
| `fixedStateCooldownSeconds` | 60 | |  | Fixed State: cooldown in seconds. |
| `fixedStateDurationTicks` | 600 | |  | Fixed State: effect duration (ticks). |
| `airWallMagiculePerSecond` | 1,000 | |  | Air Wall: magicules drained per second while held. |
| `airWallHalfSize` | 2.5 | |  | Air Wall: horizontal half-size of the wall (blocks). |
| `airWallCenterDistance` | 2.75 | |  | Air Wall: distance in front of the caster (blocks). |
| `airWallThickness` | 0.35 | |  | Air Wall: thickness along the facing axis (blocks). |
| `timeControlMagiculePerSecond` | 2,000 | |  | Time Control (hold): magicules per second. |
| `timeControlHalfWidth` | 4 | |  | Half-width (blocks) of Time Control / Time Freeze field around the user (4 =&gt; 8 blocks wide). |
| `learnPointsTimeFreeze` | 100 | |  | Learn points required for Time Freeze mode. |
| `learnPointsWhiteLock` | 250 | |  | Learn points required for White Lock mode. |
| `learnPointsBlockAccel` | 2,000 | |  | Learn points required for Block Acceleration mode. |
| `timeFreezeCooldownSeconds` | 30 | |  | Cooldown in seconds for Time Freeze. |
| `timeFreezePulseDurationTicks` | 60 | |  | Duration in ticks for one Time Freeze pulse. |
| `whiteLockCooldownSeconds` | 45 | |  | Cooldown in seconds for White Lock. |
| `blockAccelCooldownSeconds` | 20 | |  | Cooldown in seconds for placing Block Acceleration. |
| `blockAccelBonusRandomTicks` | 19 | |  | Block accel bonus random ticks |
| `timeControlSnowflakesPerTick` | 8 | |  | Time Control snowflake spawn density (0 disables) |
| `timeFreezeSnowflakesPerTick` | 12 | |  | Time Freeze: snowflake spawn density (0 disables) |

## `[cessation]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 150,000 | |  |  |
| `maxMastery` | 1,000 | |  |  |
| `freezeAllHalfWidth` | 4 | |  |  |
| `freezeAllCooldownSeconds` | 30 | |  |  |
| `iceWallHeight` | 8 | |  |  |
| `iceWallThickness` | 3 | |  |  |
| `snowCrystalHalfSize` | 5 | |  |  |
| `snowCrystalInteriorHalf` | 3 | |  |  |

## `[divide]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 150,000 | |  |  |
| `maxMastery` | 1,000 | |  |  |
| `dragonClawCooldownSeconds` | 1 | |  |  |
| `dragonClawReachBonus` | 7 | |  |  |
| `dragonClawSlashWidth` | 8 | |  |  |

## `[acceleration]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 150,000 | |  |  |
| `maxMastery` | 3,000 | |  |  |
| `scorchingFlameDamage` | 25 | |  |  |
| `scorchingFlameDamageMastered` | 50 | |  |  |
| `burningBreathFlameDamage` | 25 | |  |  |
| `burningBreathFlameDamageMastered` | 50 | |  |  |
| `burningBreathSpiritDamage` | 50 | |  |  |
| `burningBreathSpiritDamageMastered` | 100 | |  |  |
| `burningBreathRange` | 105 | |  |  |
| `bloodyLavaFlameDamage` | 50 | |  |  |
| `bloodyLavaRadius` | 12 | |  |  |
| `superheatMpRegenMultiplier` | 4 | |  |  |
| `superheatMpRegenMultiplierMastered` | 8 | |  |  |

## `[witchesEnvy]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `epAcquirement` | 120,000 | |  | EP / magicule obtainment cost. |
| `learningCost` | 1,500 | |  | Learning / mastery point cost. |
| `maxMastery` | 1,000 | |  | Max mastery. |
| `learningByDeathMaxStacks` | 20 | |  | Learning By Death: max bonus stacks (+1 learning &amp; mastery gain each). |
| `learningByDeathCooldownTicks` | 1,200 | |  | Learning By Death: cooldown between stack gains (ticks). |
| `curseMaxStacks` | 5 | |  | Witch's Curse: max stacks without mastery. |
| `curseMaxStacksMastered` | 10 | |  | Witch's Curse: max stacks when mastered. |
| `curseStacksPerKill` | 1 | |  | Witch's Curse: stacks added when the user is killed. |
| `curseDurationTicks` | 6,000 | |  | Witch's Curse: effect duration (ticks). |
| `curseOnHitChance` | 0.1 | |  | Witch's Curse: chance on hit when mastered. |
| `wrathRange` | 12 | |  | Witch's Wrath: targeting range. |
| `wrathDamage` | 10 | |  | Witch's Wrath: corrosion + spiritual damage per stack. |
| `wrathDamageMastered` | 25 | |  | Witch's Wrath: damage per stack when mastered. |
| `rambleRadius` | 30 | |  | Deadly Ramble: radius in blocks. |
| `rambleOthersShpFraction` | 0.2 | |  | Deadly Ramble: fraction of max SHP drained from others per second. |
| `rambleSelfShpFraction` | 0.15 | |  | Deadly Ramble: fraction of max SHP drained from self per second. |

## `[timeTraveler]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `epAcquirement` | 65,000 | |  | EP / magicule obtainment cost. |
| `learningCost` | 1,500 | |  | Learning / mastery point cost. |
| `maxMastery` | 1,000 | |  | Max mastery. |
| `timeLeapCooldownSeconds` | 600 | |  | Time Leap: cooldown between automatic saves (Tensura seconds). |
| `deathHealHpFraction` | 0.1 | |  | Time Leap: fraction of max HP restored on death rewind. |
| `reverseFateLearnPoints` | 500 | |  | Reverse Fate: learn points required. |
| `reverseFateRadius` | 60 | |  | Reverse Fate: snapshot radius in blocks. |
| `reverseFateCooldownSeconds` | 300 | |  | Reverse Fate: cooldown after rewind (Tensura seconds). |

## `[dealMaker]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 50,000 | |  | Magicule cost to acquire Deal Maker. |
| `magiculeCost` | 500 | |  | Magicule cost to activate. |
| `cooldown` | 30 | |  | Cooldown in seconds after activation. |
| `maxActiveDeals` | 50 | |  | Maximum number of active deals a player can have. |
| `maxDealDistance` | 100 | |  | Maximum distance in blocks for deal creation. |

## `[naming]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `subdueCost` | 1,000 | |  | Magicule cost for 'subdue' tier naming. |
| `evolveCost` | 5,000 | |  | Magicule cost for 'evolve' tier naming. |
| `endowCost` | 25,000 | |  | Magicule cost for 'endow' tier naming. |
| `customCost` | 50,000 | |  | Magicule cost for 'custom' tier naming. |
| `maxNameLength` | 64 | |  | Maximum length of a custom naming string. |

## `[devilHost]`

| Option | Default | This pack | Range | Description |
|---|---|---|---|---|
| `mpAcquirement` | 30,000 | |  | Magicule cost to acquire Devil Host. |
| `magiculeCost` | 200 | |  | Magicule cost to activate. |
| `cooldown` | 10 | |  | Cooldown in seconds after activation. |
| `endDealHoldTicks` | 1,200 | |  | Ticks required to hold the skill to end a deal (20 ticks = 1 second). |
