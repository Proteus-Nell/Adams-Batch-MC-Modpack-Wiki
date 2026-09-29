# `config/nightmare/ability/skill/nightmare_intrinsic.toml`

<small>[TR: Nightmares](../index.md) &rsaquo; [Configs](index.md)</small>

## Top level

| Option | Default | Range | Description |
|---|---|---|---|
| `goddessAllowedUniqueSkills` | - |  |  |

## `[Hellblaze]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 1,000 |  | EP / magicule obtainment cost to learn Hellblaze. |
| `toggleOnHitMagiculeCost` | 5 |  | Magicule cost per black-burn proc while toggled (on hit). |
| `blackBurnDurationTicks` | 200 |  | Black burn duration on hit (ticks). |
| `blackBurnLevel` | 0 |  | Black burn amplifier when not mastered. |
| `blackBurnLevelMastered` | 1 |  | Black burn amplifier when mastered. |
| `hellFlareLearnThreshold` | 100 |  | Learn point threshold for Hell Flare mode. |
| `hellFlareMasteryThreshold` | 200 |  | Mastery point threshold for Hell Flare. |
| `hellFlareLearnCooldownTicks` | 10 |  | Cooldown (ticks) while gaining learn points on Hell Flare. |
| `hellFlareSpamCooldownTicks` | 1 |  | Cooldown (ticks) between Hell Flare casts while building mastery. |
| `limitedHellFlareCooldownTicks` | 2 |  | Cooldown (ticks) for Limited Hell Flare. |

## `[Hellblaze.breath]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 0 |  | Current MP (magicule) cost to use this mode or segment. |
| `durationTicks` | 0 |  | Duration in ticks (effects, zones, projectiles) when applicable. |
| `level` | 0 |  | Effect amplifier level (0 = I) when applicable. |
| `cooldownTicks` | 0 |  | Cooldown in ticks after this mode activates. |
| `damage` | 0 |  | Primary damage when this mode deals damage. |
| `damageMastered` | 0 |  | Damage when mastered; if 0, 'damage' is used for both. |
| `scalar` | 0 |  | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `scalar2` | 0 |  | Second scalar (e.g. secondary radius) when applicable. |

## `[Hellblaze.ball]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 0 |  | Current MP (magicule) cost to use this mode or segment. |
| `durationTicks` | 0 |  | Duration in ticks (effects, zones, projectiles) when applicable. |
| `level` | 0 |  | Effect amplifier level (0 = I) when applicable. |
| `cooldownTicks` | 0 |  | Cooldown in ticks after this mode activates. |
| `damage` | 0 |  | Primary damage when this mode deals damage. |
| `damageMastered` | 0 |  | Damage when mastered; if 0, 'damage' is used for both. |
| `scalar` | 0 |  | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `scalar2` | 0 |  | Second scalar (e.g. secondary radius) when applicable. |

## `[Hellblaze.hellFlareArea]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 0 |  | Current MP (magicule) cost to use this mode or segment. |
| `durationTicks` | 0 |  | Duration in ticks (effects, zones, projectiles) when applicable. |
| `level` | 0 |  | Effect amplifier level (0 = I) when applicable. |
| `cooldownTicks` | 0 |  | Cooldown in ticks after this mode activates. |
| `damage` | 0 |  | Primary damage when this mode deals damage. |
| `damageMastered` | 0 |  | Damage when mastered; if 0, 'damage' is used for both. |
| `scalar` | 0 |  | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `scalar2` | 0 |  | Second scalar (e.g. secondary radius) when applicable. |

## `[Hellblaze.limitedHellFlare]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 0 |  | Current MP (magicule) cost to use this mode or segment. |
| `durationTicks` | 0 |  | Duration in ticks (effects, zones, projectiles) when applicable. |
| `level` | 0 |  | Effect amplifier level (0 = I) when applicable. |
| `cooldownTicks` | 0 |  | Cooldown in ticks after this mode activates. |
| `damage` | 0 |  | Primary damage when this mode deals damage. |
| `damageMastered` | 0 |  | Damage when mastered; if 0, 'damage' is used for both. |
| `scalar` | 0 |  | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `scalar2` | 0 |  | Second scalar (e.g. secondary radius) when applicable. |

## `[Hellblaze.hellFlarePlasma]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 0 |  | Current MP (magicule) cost to use this mode or segment. |
| `durationTicks` | 0 |  | Duration in ticks (effects, zones, projectiles) when applicable. |
| `level` | 0 |  | Effect amplifier level (0 = I) when applicable. |
| `cooldownTicks` | 0 |  | Cooldown in ticks after this mode activates. |
| `damage` | 0 |  | Primary damage when this mode deals damage. |
| `damageMastered` | 0 |  | Damage when mastered; if 0, 'damage' is used for both. |
| `scalar` | 0 |  | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `scalar2` | 0 |  | Second scalar (e.g. secondary radius) when applicable. |

## `[GiantDance]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 5,000 |  | Magicule cost to transform. |
| `effectDurationTicks` | 3,600 |  | Giant Dance effect duration (ticks) when not mastered. |
| `effectDurationMasteredTicks` | 7,200 |  | Giant Dance effect duration (ticks) when mastered. |
| `removeEarlyCooldownTicks` | 600 |  | Cooldown (ticks) after removing the transformation early. |
| `applyCooldownTicks` | 780 |  | Cooldown (ticks) after applying transformation. |
| `applyCooldownMasteredTicks` | 960 |  | Cooldown (ticks) after applying transformation when mastered. |
| `effectLevel` | 0 |  | Mob effect amplifier for Giant Dance (usually 0). |

## `[HeavyMetal]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 5,000 |  | Magicule cost to transform. |
| `effectDurationTicks` | 3,600 |  | Heavy Metal effect duration (ticks) when not mastered. |
| `effectDurationMasteredTicks` | 7,200 |  | Heavy Metal effect duration (ticks) when mastered. |
| `removeEarlyCooldownTicks` | 600 |  | Cooldown (ticks) after removing the transformation early. |
| `applyCooldownTicks` | 780 |  | Cooldown (ticks) after applying transformation. |
| `applyCooldownMasteredTicks` | 960 |  | Cooldown (ticks) after applying transformation when mastered. |
| `effectLevel` | 0 |  | Heavy Metal mob effect amplifier. |
| `resistanceLevelNormal` | 0 |  | Resistance amplifier when not mastered (0 = I). |
| `resistanceLevelMastered` | 2 |  | Resistance amplifier when mastered. |

## `[AssaultMode]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 20,000 |  | EP obtainment cost. |
| `applyCooldownTicks` | 1,200 |  | Cooldown (ticks) after activating burst. |
| `effectDurationTicks` | 3,600 |  | Effect duration (ticks) when not mastered. |
| `effectDurationMasteredTicks` | 7,200 |  | Effect duration (ticks) when mastered. |
| `effectAmplifier` | 1 |  | Mob effect amplifier for burst state. |
| `masteryPointEveryTicks` | 6 |  | Grant mastery every N ticks while active. |

## `[Apotheosis]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 20,000 |  | EP obtainment cost. |
| `applyCooldownTicks` | 1,200 |  | Cooldown (ticks) after activating burst. |
| `effectDurationTicks` | 3,600 |  | Effect duration (ticks) when not mastered. |
| `effectDurationMasteredTicks` | 7,200 |  | Effect duration (ticks) when mastered. |
| `effectAmplifier` | 1 |  | Mob effect amplifier for burst state. |
| `masteryPointEveryTicks` | 6 |  | Grant mastery every N ticks while active. |

## `[DarkMagicRelease]`

| Option | Default | Range | Description |
|---|---|---|---|
| `elementDamageMultiplier` | 2 |  | Multiplier on matching elemental damage while released. |
| `battlewillFlatBonus` | 200 |  | Flat bonus when battlewill + released (not mastered). |
| `battlewillFlatBonusMastered` | 400 |  | Flat bonus when battlewill + released (mastered). |
| `durabilityFromDamageDivisor` | 6 |  | Durability break uses max(1, damage / this). |
| `durabilityBreakBaseMultiplier` | 4 |  | Multiplier after divisor for durability loss. |
| `durabilityMasterMultiplier` | 2 |  | Extra durability multiplier when mastered (multiplicative). |
| `itemEpBypassThreshold` | 1,000,000 |  | Skip durability break if stack custom EP is at least this. |

## `[HolyMagicRelease]`

| Option | Default | Range | Description |
|---|---|---|---|
| `elementDamageMultiplier` | 2 |  | Multiplier on matching elemental damage while released. |
| `battlewillFlatBonus` | 200 |  | Flat bonus when battlewill + released (not mastered). |
| `battlewillFlatBonusMastered` | 400 |  | Flat bonus when battlewill + released (mastered). |
| `durabilityFromDamageDivisor` | 6 |  | Durability break uses max(1, damage / this). |
| `durabilityBreakBaseMultiplier` | 4 |  | Multiplier after divisor for durability loss. |
| `durabilityMasterMultiplier` | 2 |  | Extra durability multiplier when mastered (multiplicative). |
| `itemEpBypassThreshold` | 1,000,000 |  | Skip durability break if stack custom EP is at least this. |

## `[SteelKiRelease]`

| Option | Default | Range | Description |
|---|---|---|---|
| `elementDamageMultiplier` | 2 |  | Multiplier on matching elemental damage while released. |
| `battlewillFlatBonus` | 200 |  | Flat bonus when battlewill + released (not mastered). |
| `battlewillFlatBonusMastered` | 400 |  | Flat bonus when battlewill + released (mastered). |
| `durabilityFromDamageDivisor` | 6 |  | Durability break uses max(1, damage / this). |
| `durabilityBreakBaseMultiplier` | 4 |  | Multiplier after divisor for durability loss. |
| `durabilityMasterMultiplier` | 2 |  | Extra durability multiplier when mastered (multiplicative). |
| `itemEpBypassThreshold` | 1,000,000 |  | Skip durability break if stack custom EP is at least this. |

## `[WaterKiRelease]`

| Option | Default | Range | Description |
|---|---|---|---|
| `elementDamageMultiplier` | 2 |  | Multiplier on matching elemental damage while released. |
| `battlewillFlatBonus` | 200 |  | Flat bonus when battlewill + released (not mastered). |
| `battlewillFlatBonusMastered` | 400 |  | Flat bonus when battlewill + released (mastered). |
| `durabilityFromDamageDivisor` | 6 |  | Durability break uses max(1, damage / this). |
| `durabilityBreakBaseMultiplier` | 4 |  | Multiplier after divisor for durability loss. |
| `durabilityMasterMultiplier` | 2 |  | Extra durability multiplier when mastered (multiplicative). |
| `itemEpBypassThreshold` | 1,000,000 |  | Skip durability break if stack custom EP is at least this. |

## `[PoisonKiRelease]`

| Option | Default | Range | Description |
|---|---|---|---|
| `elementDamageMultiplier` | 2 |  | Multiplier on matching elemental damage while released. |
| `battlewillFlatBonus` | 200 |  | Flat bonus when battlewill + released (not mastered). |
| `battlewillFlatBonusMastered` | 400 |  | Flat bonus when battlewill + released (mastered). |
| `durabilityFromDamageDivisor` | 6 |  | Durability break uses max(1, damage / this). |
| `durabilityBreakBaseMultiplier` | 4 |  | Multiplier after divisor for durability loss. |
| `durabilityMasterMultiplier` | 2 |  | Extra durability multiplier when mastered (multiplicative). |
| `itemEpBypassThreshold` | 1,000,000 |  | Skip durability break if stack custom EP is at least this. |

## `[FireKiRelease]`

| Option | Default | Range | Description |
|---|---|---|---|
| `elementDamageMultiplier` | 2 |  | Multiplier on matching elemental damage while released. |
| `battlewillFlatBonus` | 200 |  | Flat bonus when battlewill + released (not mastered). |
| `battlewillFlatBonusMastered` | 400 |  | Flat bonus when battlewill + released (mastered). |
| `durabilityFromDamageDivisor` | 6 |  | Durability break uses max(1, damage / this). |
| `durabilityBreakBaseMultiplier` | 4 |  | Multiplier after divisor for durability loss. |
| `durabilityMasterMultiplier` | 2 |  | Extra durability multiplier when mastered (multiplicative). |
| `itemEpBypassThreshold` | 1,000,000 |  | Skip durability break if stack custom EP is at least this. |

## `[SaintChiRelease]`

| Option | Default | Range | Description |
|---|---|---|---|
| `elementDamageMultiplier` | 2 |  | Multiplier on matching elemental damage while released. |
| `battlewillFlatBonus` | 200 |  | Flat bonus when battlewill + released (not mastered). |
| `battlewillFlatBonusMastered` | 400 |  | Flat bonus when battlewill + released (mastered). |
| `durabilityFromDamageDivisor` | 6 |  | Durability break uses max(1, damage / this). |
| `durabilityBreakBaseMultiplier` | 4 |  | Multiplier after divisor for durability loss. |
| `durabilityMasterMultiplier` | 2 |  | Extra durability multiplier when mastered (multiplicative). |
| `itemEpBypassThreshold` | 1,000,000 |  | Skip durability break if stack custom EP is at least this. |

## `[DemonicPower]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 30 |  | Learning / obtainment cost. |
| `meetEpThreshold` | 20,000 |  | Minimum EP to meet requirement. |
| `magiculeCost` | 30 |  | Magicule cost per tick / toggle use. |
| `strengthenTickDuration` | 240 |  | Strengthen duration (ticks) while toggled drain path. |
| `strengthenTickAmplifier` | 2 |  | Strengthen amplifier while toggled. |
| `pressDurationNormal` | 1,200 |  | Strengthen duration (ticks) on press when not mastered. |
| `pressDurationMastered` | 2,400 |  | Strengthen duration (ticks) on press when mastered. |
| `pressAmplifierNormal` | 2 |  | Strengthen amplifier on press when not mastered. |
| `pressAmplifierMastered` | 4 |  | Strengthen amplifier on press when mastered. |
| `toggleOffStripMaxAmplifier` | 2 |  | Strip strengthen on toggle off if amplifier at most this. |

## `[MagicRegeneration]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 30 |  | Learning cost. |
| `meetEpThreshold` | 20,000 |  | Minimum EP for requirement. |
| `regenAmount` | 10,000,000 |  | Magicule restored when not mastered. |
| `regenAmountMastered` | 500,000,000 |  | Magicule restored when mastered. |
| `cooldownTicks` | 1,800 |  | Cooldown (ticks) after use. |

## `[MagicalEye]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 20,000 |  | EP obtainment cost. |
| `learningCost` | 1,000 |  | Learning cost. |
| `dodgeChanceNormal` | 0.5 |  | Dodge chance when not mastered (0–1). |
| `dodgeChanceMastered` | 0.7 |  | Dodge chance when mastered. |
| `takenDamageMultiplierNormal` | 0.7 |  | Incoming damage multiplier when not mastered (retain this fraction). |
| `takenDamageMultiplierMastered` | 0.5 |  | Incoming damage multiplier when mastered. |
| `criticalChanceBonusNormal` | 33 |  | Critical chance attribute bonus when not mastered. |
| `criticalChanceBonusMastered` | 50 |  | Critical chance attribute bonus when mastered. |
| `futureVisionDurationNormal` | 200 |  | Future Vision duration (ticks) when not mastered. |
| `futureVisionDurationMastered` | 400 |  | Future Vision duration (ticks) when mastered. |
| `analysisLevelNormal` | 1 |  | Analysis level when not mastered. |
| `analysisLevelMastered` | 2 |  | Analysis level when mastered. |
| `analysisDistanceNormal` | 5 |  | Analysis distance when not mastered. |
| `analysisDistanceMastered` | 10 |  | Analysis distance when mastered. |
| `masteryTickInterval` | 6 |  | Mastery tick interval while analyzing. |
| `canTickMinAnalysisDistance` | 5 |  | Minimum analysis distance for canTick check. |

## `[BlackFlameThunder]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 500 |  | EP obtainment cost. |
| `learningCost` | 500 |  | Learning cost. |
| `maxMastery` | 5,000 |  | Max mastery. |
| `physicalHitMultiplier` | 1.5 |  | Physical hit damage multiplier while toggled (non-fire). |
| `igniteTicks` | 60 |  | Fire ticks applied on physical proc. |
| `elementalBoostMultiplier` | 10 |  | Multiplier for fire/lightning/light while flame+thunder. |
| `touchOnHitMagiculeCost` | 5 |  | Magicule cost per on-touch proc. |
| `blackBurnDurationTicks` | 200 |  | Black burn duration (ticks). |
| `blackBurnLevelNormal` | 1 |  | Black burn amplifier when not mastered. |
| `blackBurnLevelMastered` | 2 |  | Black burn amplifier when mastered. |

## `[SteelDragonArmor]`

| Option | Default | Range | Description |
|---|---|---|---|
| `armorNormal` | 50 |  | Armor bonus when not mastered. |
| `armorMastered` | 100 |  | Armor bonus when mastered. |
| `toughnessNormal` | 8 |  | Toughness when not mastered. |
| `toughnessMastered` | 16 |  | Toughness when mastered. |
| `masteryTickInterval` | 10 |  | Mastery tick interval while toggled. |

## `[WaterDragonArmor]`

| Option | Default | Range | Description |
|---|---|---|---|
| `armorNormal` | 50 |  | Armor bonus when not mastered. |
| `armorMastered` | 100 |  | Armor bonus when mastered. |
| `toughnessNormal` | 8 |  | Toughness when not mastered. |
| `toughnessMastered` | 16 |  | Toughness when mastered. |
| `masteryTickInterval` | 10 |  | Mastery tick interval while toggled. |

## `[FireDragonArmor]`

| Option | Default | Range | Description |
|---|---|---|---|
| `armorNormal` | 50 |  | Armor bonus when not mastered. |
| `armorMastered` | 100 |  | Armor bonus when mastered. |
| `toughnessNormal` | 8 |  | Toughness when not mastered. |
| `toughnessMastered` | 16 |  | Toughness when mastered. |
| `masteryTickInterval` | 10 |  | Mastery tick interval while toggled. |

## `[PoisonDragonArmor]`

| Option | Default | Range | Description |
|---|---|---|---|
| `armorNormal` | 50 |  | Armor bonus when not mastered. |
| `armorMastered` | 100 |  | Armor bonus when mastered. |
| `toughnessNormal` | 8 |  | Toughness when not mastered. |
| `toughnessMastered` | 16 |  | Toughness when mastered. |
| `masteryTickInterval` | 10 |  | Mastery tick interval while toggled. |

## `[HellblazeDragonArmor]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 25,000 |  | Learning cost. |
| `armorNormal` | 40 |  | Armor when not mastered. |
| `armorMastered` | 80 |  | Armor when mastered. |
| `toughnessNormal` | 50 |  | Toughness when not mastered. |
| `toughnessMastered` | 500 |  | Toughness when mastered. |
| `attackBonusNormal` | 30 |  | Attack damage bonus when not mastered. |
| `attackBonusMastered` | 300 |  | Attack damage bonus when mastered. |
| `masteryTickInterval` | 10 |  | Mastery tick interval while toggled. |

## `[LockSkill]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 30 |  | Learning cost. |
| `meetEpThreshold` | 10,000 |  | Minimum EP with plunder gamerule. |
| `magiculeCost` | 30 |  | Magicule cost. |

## `[HiddenVoid]`

| Option | Default | Range | Description |
|---|---|---|---|
| `heldMagiculeCheckInterval` | 20 |  | Held tick interval for magicule check. |
| `concealmentDurationTicks` | 5 |  | Presence concealment duration (ticks) per refresh. |
| `concealmentAmplifier` | 1 |  | Concealment amplifier. |

## `[ChaosStrikes]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 5,000 |  | EP obtainment cost. |
| `maxScaledDamage` | 500 |  | Max extra damage from EP scaling. |
| `scalingReferenceEp` | 5,000,000 |  | Target EP reference for scaling. |
| `hitsPerCycle` | 3 |  | Hits per toggle cycle. |
| `procMagiculeMin` | 5,000 |  | Minimum magicule spent per proc. |
| `procMagiculeFromBaseDivisor` | 100 |  | Magicule cost divisor from base magicule. |
| `procMagiculeMax` | 1,000,000 |  | Maximum magicule spent per proc. |

## `[AnchorWave]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castMagiculeCost` | 50,000 |  | Magicule cost to cast. |
| `radius` | 20 |  | Effect radius (blocks). |
| `blockadeDurationTicks` | 1,200 |  | Spatial blockade duration (ticks) on entities. |
| `cooldownTicks` | 60 |  | Cooldown (ticks) after cast. |

## `[DarkChiRelease.equipmentBreak]`

| Option | Default | Range | Description |
|---|---|---|---|
| `elementDamageMultiplier` | 2 |  | Multiplier on matching elemental damage while released. |
| `battlewillFlatBonus` | 200 |  | Flat bonus when battlewill + released (not mastered). |
| `battlewillFlatBonusMastered` | 400 |  | Flat bonus when battlewill + released (mastered). |
| `durabilityFromDamageDivisor` | 6 |  | Durability break uses max(1, damage / this). |
| `durabilityBreakBaseMultiplier` | 4 |  | Multiplier after divisor for durability loss. |
| `durabilityMasterMultiplier` | 2 |  | Extra durability multiplier when mastered (multiplicative). |
| `itemEpBypassThreshold` | 1,000,000 |  | Skip durability break if stack custom EP is at least this. |

## `[DarkChiRelease]`

| Option | Default | Range | Description |
|---|---|---|---|
| `armorFromAuraMultiplierNormal` | 0.01 |  | Armor from aura multiplier when not mastered. |
| `armorFromAuraMultiplierMastered` | 0.015 |  | Armor from aura multiplier when mastered. |
| `auraDrainMastered` | 0.5 |  | Aura drain per tick when mastered. |
| `auraDrainNormal` | 1 |  | Aura drain per tick when not mastered. |
| `soulStrikeRange` | 8 |  | Targeting range for soul strike. |
| `executeEpFraction` | 0.3 |  | Execute when target EP below this fraction of max. |
| `pierceDamageHealthFraction` | 1.2 |  | Non-execute damage as fraction of target max health. |
| `cooldownTicksNormal` | 300 |  | Cooldown (ticks) when not mastered. |
| `cooldownTicksMastered` | 200 |  | Cooldown (ticks) when mastered. |

## `[CalamityChiRelease]`

| Option | Default | Range | Description |
|---|---|---|---|
| `attackFromAuraFractionNormal` | 0.01 |  | Attack bonus from aura fraction when not mastered. |
| `attackFromAuraFractionMastered` | 0.02 |  | Attack bonus from aura fraction when mastered. |
| `auraDrainNormal` | 2 |  | Aura drain per tick when not mastered. |
| `auraDrainMastered` | 1 |  | Aura drain per tick when mastered. |
| `onDamageHealAuraFractionNormal` | 0.02 |  | Heal on damage dealt: aura \* this when not mastered. |
| `onDamageHealAuraFractionMastered` | 0.04 |  | Heal on damage dealt when mastered. |
| `masteryTickInterval` | 6 |  | Mastery tick interval. |

## `[SaintChiExtras]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraTickBase` | 5 |  | Flat aura added per tick (scaled by mastered 2x on regen line). |
| `auraPassiveRegenFraction` | 0.01 |  | Multiplier on aura for passive regen component. |
| `masterDoublesPassiveRegen` | true |  | Master doubles passive regen. |
| `pressShpFromAuraNormal` | 0.02 |  | SHP heal from aura fraction press when not mastered. |
| `pressShpFromAuraMastered` | 0.03 |  | SHP heal from aura fraction when mastered. |
| `pressHpFromAuraNormal` | 0.01 |  | HP heal from aura fraction when not mastered. |
| `pressHpFromAuraMastered` | 0.02 |  | HP heal from aura fraction when mastered. |
| `pressAllyRadius` | 10 |  | Ally radius for press heal. |
| `pressCooldownNormal` | 80 |  | Cooldown ticks when not mastered. |
| `pressCooldownMastered` | 40 |  | Cooldown ticks when mastered. |
| `masteryTickInterval` | 6 |  | Mastery tick interval while toggled. |

## `[DreamManipulation]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 5,000 |  | Magicule cost while channeling. |
| `particleIntervalTicks` | 10 |  | Particle burst every N held ticks (server). |
| `particleCount` | 8 |  | Particles per burst. |
| `masteryIntervalTicks` | 100 |  | Mastery point every N held ticks (after first tick). |
| `channelTickInterval` | 20 |  | Heal / MP-AP regen / drowsiness stack tick interval. |
| `hpHealFlat` | 10 |  | Flat HP heal each channel tick. |
| `hpHealMaxHealthFractionMastered` | 0.01 |  | Extra HP heal as fraction of max health when mastered (each channel tick). |
| `shpHealFlat` | 10 |  | Flat SHP heal each channel tick. |
| `shpHealMaxFractionMastered` | 0.01 |  | Extra SHP heal as fraction of max SHP when mastered (each channel tick). |
| `mpApRegenRate` | 20 |  | Regen rate passed to mpRegen / apRegen helpers. |
| `debuffRadiusNormal` | 5 |  | Drowsiness application radius when not mastered. |
| `debuffRadiusMastered` | 10 |  | Drowsiness application radius when mastered. |
| `drowsinessDurationTicksNormal` | 200 |  | Initial drowsiness duration (ticks) when not mastered. |
| `drowsinessDurationTicksMastered` | 400 |  | Initial drowsiness duration (ticks) when mastered. |
| `drowsinessExtendTicks` | 20 |  | Ticks added to existing drowsiness each channel tick. |

## `[CNPCLock]`

| Option | Default | Range | Description |
|---|---|---|---|
| `learningCost` | 30 |  | Learning cost. |
| `magiculeCost` | 30 |  | Magicule cost. |
| `meetEpThreshold` | 1000000000000000 |  | Minimum EP when plunder gamerule is on. |

## `[Avalon]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 10,000 |  | Magicule Acquirement Cost. |
| `dodgeChance` | 50 |  | Dodge chance for Non-Magical attacks out of 100. |
| `projectileChance` | 50 |  | Dodge chance for Projectile attacks out of 100. |

## `[Ideal]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 10,000 |  | Magicule Acquirement Cost. |
| `critChance` | 60 |  | Critical Attack Chance. |
| `luckMultiplier` | 1 |  | Level of Luck granted passively by ideal. |

## `[MaterialCreation]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 10,000 |  | EP obtainment cost (intrinsic skill parity). |
| `researchHitsToLearn` | 100 |  | Total research points needed on one item/block identity before it is learned (Understanding mode). |
| `destroyChance` | 0.15 |  | Chance to destroy the researched stack or block each pulse. |
| `understandingCooldownTicks` | 600 |  | Cooldown in Minecraft ticks after each Understanding pulse (skill UI uses seconds → stored value / 20). |
| `reachDistance` | 6 |  | Ray trace reach when main hand is empty. |
| `refundFraction` | 0.5 |  | Refund fraction when inserting daemon-bound stacks into the bench refund slot. |
| `softMagiculeThreshold` | 4,096 |  | EMC at or below this value spends current magicules only and is not daemon-bound. |

## `[ConceptualExistence]`

| Option | Default | Range | Description |
|---|---|---|---|
| `unityRange` | 12 |  | Targeting range for Unity possession on non-player bodies. |
| `hostRange` | 32 |  | Targeting range for binding to a player host. |
| `unityResistanceMultiplier` | 0.5 |  | Resistance multiplier passed to Tensura possession checks for Unity. |
| `unityHpMultiplier` | 0.35 |  | Health multiplier passed to Tensura possession checks for Unity. |
| `unityShpMultiplier` | 0.35 |  | Spiritual-health multiplier passed to Tensura possession checks for Unity. |
| `unityEpMultiplier` | 0.5 |  | EP multiplier passed to Tensura possession checks for Unity. |
| `unityMaxAttack` | 5,000 |  | Maximum attack copied into a borrowed Unity body. |
| `unityMaxHealth` | 5,000 |  | Maximum health copied into a borrowed Unity body. |
| `unityMinMinutes` | 5 |  | Minimum Unity possession duration in minutes before mastery. |
| `unityMaxMinutes` | 20 |  | Maximum Unity possession duration in minutes before mastery. |
| `unityMinMinutesMastered` | 10 |  | Minimum Unity possession duration in minutes after mastery. |
| `unityMaxMinutesMastered` | 40 |  | Maximum Unity possession duration in minutes after mastery. |
| `optimizeMinimumMagiculePerSecond` | 100 |  | Minimum magicule transferred per second while Optimize Energy is channeled. |
| `optimizeMagiculePercentPerSecond` | 0.01 |  | Additional percent of the user's max magicule transferred per second while Optimize Energy is channeled. |

## `[DivineWisdomCore]`

| Option | Default | Range | Description |
|---|---|---|---|
| `informationalDrainPercent` | 0.01 |  | Percent of max magicule drained every 5s while unbound (informational body). |
| `passiveMasteryBonus` | 14 |  | Passive mastery speed bonus while Divine Wisdom Core is active. |
| `passiveLearningBonus` | 14 |  | Passive learning speed bonus while Divine Wisdom Core is active. |
| `hostMasteryBonus` | 14 |  | Mastery speed granted to the host while attached. |
| `hostLearningBonus` | 14 |  | Learning speed granted to the host while attached. |
| `hostCastSpeedBonus` | 0.4 |  | Cast speed multiplier bonus for the host (chant speed attribute). |
| `hijackResistanceMultiplier` | 0.5 |  |  |
| `hijackHpMultiplier` | 0.35 |  |  |
| `hijackShpMultiplier` | 0.35 |  |  |
| `hijackEpMultiplier` | 0.5 |  |  |
| `hijackMaxAttack` | 5,000 |  |  |
| `hijackMaxHealth` | 5,000 |  |  |
| `hijackRange` | 12 |  |  |
| `hijackMinMinutes` | 5 |  |  |
| `hijackMaxHours` | 5 |  |  |
| `bodyDespawnTicks` | 6,000 |  |  |
| `hostRange` | 32 |  |  |
| `egoBoostCooldownSeconds` | 300 |  | Cooldown (seconds) after locking an ego boost before you can pick again. |
| `energyOptimizationMinimumMagiculePerSecond` | 500 |  | Minimum MP transferred per second while Energy Optimization is set to Magicule. |
| `energyOptimizationMagiculePercentPerSecond` | 0.01 |  | Percent of max MP transferred per second while Energy Optimization is set to Magicule. |
| `energyOptimizationMinimumAuraPerSecond` | 100 |  | Minimum AP transferred per second while Energy Optimization is set to Aura. |
| `energyOptimizationAuraPercentPerSecond` | 0.01 |  | Percent of max AP transferred per second while Energy Optimization is set to Aura. |
| `energyOptimizationSpiritronsPerSecond` | 50 |  | Holy Power (Spiritrons) generated per second while Energy Optimization is set to Holy Power. |
| `energyOptimizationNihilityPerSecond` | 100 |  | Nihility generated per second while Energy Optimization is set to Nihility. |

## `[DragonFactorHaki]`

| Option | Default | Range | Description |
|---|---|---|---|
| `factorBonusEpThreshold` | 1,200,000 |  | EP required for Factor Bonus effects. |
| `earthFactorBonusMaxEp` | 2,000,000 |  | Max EP counted for Earth HP scaling. |
| `boonFlatDamage` | 50 |  | Elemental Boon flat damage for non-corrosion elements. |
| `bloodFactorFlatBonus` | 75 |  | Flat bonus applied to Blood Ray and Blood Drain damage for Vampiric Factor. |
| `boonCorrosionMultiplier` | 3 |  | Elemental Boon multiplier for Corrosion. |
| `corrosionRegenLockTicks` | 200 |  | Infinite Regeneration lock cooldown ticks applied by Corrosion Factor Bonus. |
| `fireDurabilityDamageMultiplier` | 4 |  | Fire Factor Bonus durability damage multiplier. |
| `waterMagicCostMultiplier` | -0.5 |  | Water Factor Bonus: MAGIC_COST_MULTIPLIER additive multiplier. |
| `earthHpPer100k` | 50 |  | Earth Factor Bonus HP per 100k EP over threshold. |
| `windMeleeDodgeBonus` | 35 |  | Wind Factor Bonus auto-melee dodge chance bonus. |
| `windProjectileDodgeBonus` | 35 |  | Wind Factor Bonus auto-projectile dodge chance bonus. |
| `windDodgeNegateBonus` | 35 |  | Wind Factor Bonus dodge negate bonus. |
| `lightMagiculeRegenBonus` | 4 |  | Light Factor Bonus magicule regeneration bonus. |
| `darknessSpiritualResistDegradation` | 1 |  | Darkness Factor Bonus spiritual resistance/nullification degradation value. |
| `corrosionResistDegradation` | 1 |  | Corrosion mastery Factor Bonus corrosion resistance/nullification degradation value. |
| `enderWeight` | 10 |  | Random roll weight for Ender. |
| `netherWeight` | 10 |  | Random roll weight for Nether. |
| `holyWeight` | 10 |  | Random roll weight for Holy. |
| `daemonicWeight` | 10 |  | Random roll weight for Daemonic. |
| `guardDamageMultiplier` | 0.5 |  | Elemental Guard damage multiplier for matching element. |
| `releasePulseIntervalTicks` | 20 |  | Dragon Haki Release pulse interval ticks. |
| `releaseRadius` | 5 |  | Dragon Haki Release target search radius. |
| `releaseEpDifferenceStepFraction` | 0.2 |  | EP difference step fraction for Dragon Haki Release (0.2 = per 20%). |
| `releaseDamagePerStep` | 25 |  | Element damage added by Dragon Haki Release per EP step. |
| `releaseConfusionDurationTicks` | 60 |  | Confusion duration from Dragon Haki Release. |
| `releaseConfusionMaxAmplifier` | 3 |  | Max confusion amplifier from Dragon Haki Release. |
| `spaceAuraIntervalTicks` | 20 |  | Space Factor Bonus aura interval ticks. |
| `spaceAuraRadius` | 6 |  | Space Factor Bonus aura range. |
| `spaceAuraTargetEpFraction` | 0.5 |  | Space Factor Bonus applies blockade when target EP is below this owner fraction. |
| `spaceAuraDurationTicks` | 60 |  | Space Factor Bonus spatial blockade duration ticks. |
| `fireWeight` | 30 |  | Random roll weight for Fire. |
| `waterWeight` | 30 |  | Random roll weight for Water. |
| `earthWeight` | 30 |  | Random roll weight for Earth. |
| `windWeight` | 30 |  | Random roll weight for Wind. |
| `spaceWeight` | 15 |  | Random roll weight for Space. |
| `lightWeight` | 10 |  | Random roll weight for Light. |
| `darknessWeight` | 10 |  | Random roll weight for Darkness. |

## `[DragonPossession]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 1,000 |  | EP cost to acquire Dragon Possession. |

## `[AquaticRegeneration]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 100 |  | Base Magicule Cost to activate. |
| `regenLevel` | 3 |  | The level of the self-regeneration effect. |
| `regenLevelMastered` | 4 |  | The level of the self-regeneration effect when mastered. |
