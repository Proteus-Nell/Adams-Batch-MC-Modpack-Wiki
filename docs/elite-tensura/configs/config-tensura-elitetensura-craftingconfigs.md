# `config/tensura/EliteTensura/CraftingConfigs.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[GENERAL]`

| Option | Default | Range | Description |
|---|---|---|---|
| `sessionTimeoutTicks` | 1,200 |  | Ticks before an idle craft session is aborted and inputs refunded. DEFAULT: 1200 (60s) |
| `refundOnAbort` | true |  | Refund consumed inputs when the player aborts a craft. DEFAULT: true |
| `punishImplausibleResult` | "consume_damage" |  | What to do when a minigame result fails plausibility checks: 'poor' = give POOR-quality result, 'abort' = cancel and refund, 'consume' = cancel and BURN inputs (no refund), 'damage' = keep going as POOR but hurt the player, 'consume_damage' = burn inputs AND hurt the player. DEFAULT: consume_damage |
| `implausibleDamage` | 10 |  | Damage dealt to the player for 'damage'/'consume_damage' punishments (magic damage, bypasses armor). DEFAULT: 6.0 |
| `maxStationRange` | 8 |  | Maximum distance (blocks) the player may move from the station mid-craft. DEFAULT: 8.0 |

## `[QUALITY]`

| Option | Default | Range | Description |
|---|---|---|---|
| `critUpgradeBaseChance` | 0.05 |  | Base chance (0-1) per craft of a critical quality upgrade (+1 rank). Only path to LEGENDARY/MYTHICAL. DEFAULT: 0.05 |
| `maxCritUpgrades` | 2 |  | Maximum number of consecutive critical upgrades per craft. DEFAULT: 2 |
| `hiddenPotentialBaseChance` | 0.1 |  | Base chance (0-1) of a forged item rolling hidden potential. DEFAULT: 0.10 |
| `qualityPointsPerScore` | 0.5 |  | Quality points granted per minigame score point above 50 (shifts roll weights upward). DEFAULT: 0.5 |
| `scoreNeutralPoint` | 50 |  | Minigame score below which weights shift DOWN instead of up. DEFAULT: 50.0 |
| `critChancePerScoreOverNeutral` | 0.003 |  | Extra critical-upgrade chance per minigame score point above the neutral point — the only way skilled play improves LEGENDARY/MYTHICAL odds. Score below neutral adds nothing (the weight table already punishes it). Hephaestus Reforge is exempt: its score is random, not earned. Set 0 to disable. DEFAULT: 0.003 (+15% crit at score 100) |
| `fineFloorScore` | 90 |  | Minigame score at or above which the craft cannot come out below FINE. Reforge is exempt. Set above 100 to disable. DEFAULT: 90.0 |
| `superiorFloorScore` | 98 |  | Minigame score at or above which the craft cannot come out below SUPERIOR. Reforge is exempt. Set above 100 to disable. DEFAULT: 98.0 |
| `poorEngravingSlots` | 0 |  | Base craft-engraving slots per quality rank (extra slots from skills/titles/spec add on top). DEFAULTS: 0 / 0 / 0 / 1 / 2 / 3 / 4 |
| `commonEngravingSlots` | 0 |  |  |
| `fineEngravingSlots` | 0 |  |  |
| `superiorEngravingSlots` | 1 |  |  |
| `masterworkEngravingSlots` | 2 |  |  |
| `legendaryEngravingSlots` | 3 |  |  |
| `mythicalEngravingSlots` | 4 |  |  |

## `[MINIGAMES]`

| Option | Default | Range | Description |
|---|---|---|---|
| `minReactionTicks` | 3 |  | Minimum ticks between two minigame inputs; faster is rejected as implausible. Input times are now measured to sub-tick precision instead of being rounded to a whole tick, so this gate bites exactly rather than approximately — lowered from 4 to keep the effective strictness the same and avoid voiding fast legitimate play. DEFAULT: 3 |
| `hammerBaseStrikes` | 4 |  | Hammer: base number of strikes at difficulty 1. DEFAULT: 4 |
| `hammerStrikesPerDifficulty` | 1 |  | Hammer: extra strikes per difficulty level. DEFAULT: 1 |
| `hammerBasePeriodTicks` | 80 |  | Hammer: bar sweep period in ticks at difficulty 1 (one full left-right-left cycle). This is the real difficulty knob: it sets how far the cursor travels per unit of human timing error. DEFAULT: 80 |
| `hammerPeriodReductionPerDifficulty` | 6 |  | Hammer: ticks removed from the sweep period per difficulty level. DEFAULT: 6 |
| `hammerBaseSweetSpotWidth` | 0.18 |  | Hammer: sweet spot width (fraction of bar, 0-1) at difficulty 1. DEFAULT: 0.18 |
| `hammerSweetSpotReductionPerDifficulty` | 0.02 |  | Hammer: sweet spot width reduction per difficulty level. DEFAULT: 0.02 |
| `hammerMinSweetSpotWidth` | 0.06 |  | Hammer: minimum sweet spot width regardless of difficulty. DEFAULT: 0.06 |
| `hammerTicksPerStrike` | 100 |  | Hammer: ticks allowed per strike before the stage times out. DEFAULT: 100 |
| `flowBaseDurationTicks` | 200 |  | Flow: stage duration in ticks at difficulty 1. DEFAULT: 200 |
| `flowDurationPerDifficulty` | 40 |  | Flow: ticks added to duration per difficulty level. DEFAULT: 40 |
| `flowSampleInterval` | 1 |  | Flow: ticks between gauge samples. 1 = score every tick (finest). Raising this coarsens scoring and shrinks the packet. DEFAULT: 1 |
| `flowBaseKeyframes` | 4 |  | Flow: number of band-center keyframes (drift waypoints) at difficulty 1. DEFAULT: 4 |
| `flowKeyframesPerDifficulty` | 1 |  | Flow: extra keyframes per difficulty level (faster drift). DEFAULT: 1 |
| `flowBaseBandHalfWidth` | 0.14 |  | Flow: target band half-width (fraction of gauge, 0-1) at difficulty 1. DEFAULT: 0.14 |
| `flowBandReductionPerDifficulty` | 0.02 |  | Flow: band half-width reduction per difficulty level. DEFAULT: 0.02 |
| `flowMinBandHalfWidth` | 0.05 |  | Flow: minimum band half-width regardless of difficulty. DEFAULT: 0.05 |
| `flowMaxSlew` | 0.08 |  | Flow: maximum plausible gauge change per TICK (anti-cheat); the validator multiplies by flowSampleInterval. The needle really moves 0.05/tick, so this leaves headroom for rounding. DEFAULT: 0.08 |
| `flowMagiculeDrainPerTick` | 1 |  | Flow: magicule drained per duration tick (cost = this x durationTicks x difficulty). DEFAULT: 1.0 |
| `runeBaseGridSize` | 4 |  | Rune: number of rune tiles at difficulty 1. DEFAULT: 4 |
| `runeTilesPerDifficulty` | 1 |  | Rune: extra tiles per difficulty level. DEFAULT: 1 |
| `runeMoveBudgetMultiplier` | 3 |  | Rune: move budget = gridSize x this multiplier. DEFAULT: 3 |
| `runeBaseTimeLimitTicks` | 300 |  | Rune: time limit in ticks at difficulty 1. DEFAULT: 300 |
| `runeTimeLimitReductionPerDifficulty` | 30 |  | Rune: ticks removed from the time limit per difficulty level. DEFAULT: 30 |
| `runeSolveScoreShare` | 0.7 |  | Rune: base score share for solved fraction (0-1; remainder split between efficiency+time). DEFAULT: 0.7 |
| `tempDecayPerTick` | 0.012 |  | Temp: temperature lost per tick (0-1 scale). DEFAULT: 0.012 |
| `tempBellowsRaise` | 0.22 |  | Temp: temperature gained per bellows press (0-1 scale). DEFAULT: 0.22 |
| `tempHotBandLow` | 0.5 |  | Temp: lower bound of the hot band (strikes below score 0). DEFAULT: 0.5 |
| `tempHotBandHigh` | 0.85 |  | Temp: upper bound of the hot band. DEFAULT: 0.85 |
| `tempMaxBellows` | 200 |  | Temp: maximum bellows presses allowed (anti-cheat). DEFAULT: 200 |

## `[PROGRESSION]`

| Option | Default | Range | Description |
|---|---|---|---|
| `xpCurveBase` | 100 |  | XP required for mastery level 1. Level N costs base \* N^exponent. DEFAULT: 100.0 |
| `xpCurveExponent` | 1.6 |  | Exponent of the mastery XP curve. DEFAULT: 1.6 |
| `maxMasteryLevel` | 50 |  | Maximum crafting mastery level. DEFAULT: 50 |
| `qualityPointsPerMasteryLevel` | 0.4 |  | Quality points granted per mastery level. DEFAULT: 0.4 |

## `[SKILL_BONUSES]`

| Option | Default | Range | Description |
|---|---|---|---|
| `godlyCraftsmanOwned` | 6 |  | Quality points for owning / having toggled on / having mastered Godly Craftsman. DEFAULTS: 6 / 6 / 6 |
| `godlyCraftsmanToggled` | 6 |  |  |
| `godlyCraftsmanMastered` | 6 |  |  |
| `godlyCraftsmanCritChance` | 0.05 |  | Godly Craftsman bonus crit upgrade chance (0-1) when owned. DEFAULT: 0.05 |
| `researcherOwned` | 3 |  | Quality points for Researcher: owned / toggled / mastered. DEFAULTS: 3 / 3 / 3 |
| `researcherToggled` | 3 |  |  |
| `researcherMastered` | 3 |  |  |
| `analystHiddenPotentialChance` | 0.1 |  | Analyst hidden potential bonus chance (0-1) when owned. DEFAULT: 0.10 |
| `analystOwned` | 2 |  | Quality points for Analyst: owned / mastered. DEFAULTS: 2 / 2 |
| `analystMastered` | 2 |  |  |
| `creatorOwnedEngravingRolls` | 0 |  | Creator: extra craft-engraving rolls when owned / mastered. DEFAULTS: 0 / 1 |
| `creatorMasteredEngravingRolls` | 1 |  |  |
| `creatorOwned` | 2 |  | Quality points for Creator when owned. DEFAULT: 2 |
| `degenerateFailureReduction` | 10 |  | Degenerate: POOR weight reduction points when owned. DEFAULT: 10 |
| `mercilessWeaponCritChance` | 0.04 |  | Merciless: bonus crit upgrade chance (0-1) on WEAPON recipes when owned. DEFAULT: 0.04 |
| `chefFoodQuality` | 8 |  | Chef/Cook: quality points on FOOD recipes when owned. DEFAULT: 8 |
| `greatSageToggled` | 4 |  | Quality points for Great Sage / Raphael (ET) when toggled on. DEFAULT: 4 |
| `runesmithInsightForgesRequired` | 25 |  | Runesmith's Insight: successful forges required to auto-learn the skill. 0 disables the grant. DEFAULT: 25 |
| `runesmithInsightSweetSpotMult` | 1.25 |  | Runesmith's Insight: hammer sweet-spot width multiplier while owned (HAMMER_TIMING + TEMPERATURE_HAMMER). DEFAULT: 1.25 |
| `runesmithInsightTempDecayMult` | 0.75 |  | Runesmith's Insight: temperature decay multiplier while owned (TEMPERATURE_HAMMER; lower = slower drift). DEFAULT: 0.75 |
| `runesmithInsightMasteredSlotChance` | 0.25 |  | Runesmith's Insight: chance (0-1) of +1 craft-engraving slot per craft when mastered. DEFAULT: 0.25 |

## `[POTENTIAL_CATALYST]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable the Potential Catalyst item (unlocks a forged item's hidden potential). DEFAULT: true |
| `weakScale` | 4 |  | Weak tier (potential 0.30-0.50): primary attribute bonus = potential x this. DEFAULT: 4.0 |
| `moderateScale` | 8 |  | Moderate tier (potential 0.50-0.75): primary attribute bonus = potential x this. DEFAULT: 8.0 |
| `strongScale` | 14 |  | Strong tier (potential 0.75-1.00): primary attribute bonus = potential x this. DEFAULT: 14.0 |
| `bonusHealth` | 2 |  | Moderate/Strong tier: flat MAX_HEALTH bonus added to the item. DEFAULT: 2.0 |
| `strongLuckSeconds` | 300 |  | Strong tier: duration (seconds) of Luck I granted to the holder on unlock. DEFAULT: 300 |

## `[STATION_UPGRADE]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Allow forge stations to auto-upgrade to the next tier after enough crafts are completed on them. DEFAULT: true |
| `basicToMagisteel` | 20 |  | Crafts on a BASIC station before it upgrades to MAGISTEEL. 0 disables. DEFAULT: 20 |
| `magisteelToMythril` | 40 |  | Crafts on a MAGISTEEL station before it upgrades to MYTHRIL. 0 disables. DEFAULT: 40 |
| `mythrilToDragonforge` | 80 |  | Crafts on a MYTHRIL station before it upgrades to DRAGONFORGE. 0 disables. DEFAULT: 80 |

## `[SPECIALIZATION]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable forge specializations (player picks a smithing focus for matching-recipe bonuses). DEFAULT: true |
| `unlockMasteryLevel` | 10 |  | Crafting mastery level required before a player may choose a specialization. DEFAULT: 10 |
| `respecMagiculeCost` | 1,000 |  | Magicule drained to change an already-chosen specialization (the first pick is free). DEFAULT: 1000.0 |
| `weaponsmithCritChance` | 0.08 |  | Weaponsmith: bonus critical-upgrade chance (0-1) on matching recipes. DEFAULT: 0.08 |
| `armorsmithQualityFlat` | 4 |  | Armorsmith: bonus quality points on matching recipes. DEFAULT: 4.0 |
| `armorsmithDurabilityMult` | 0.25 |  | Armorsmith: bonus durability fraction on matching recipes (0.25 = +25% max durability). DEFAULT: 0.25 |
| `runesmithEngravingSlots` | 1 |  | Runesmith: extra craft-engraving slots on matching recipes. DEFAULT: 1 |
| `artificerHiddenPotentialChance` | 0.15 |  | Artificer: bonus hidden-potential chance (0-1) on matching recipes. DEFAULT: 0.15 |

## `[NATION_BONUSES]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable nation-driven forge bonuses (Forge Boon perk, station-upgrade discount). DEFAULT: true |
| `boonQualityFlat` | 2 |  | Forge Boon perk: bonus quality points while active. DEFAULT: 2.0 |
| `boonCritChance` | 0.05 |  | Forge Boon perk: bonus critical-upgrade chance (0-1) while active. DEFAULT: 0.05 |
| `requireOwnTerritory` | true |  | Forge Boon only applies when the station is inside the nation's own claimed territory. DEFAULT: true |
| `upgradeDiscountPerLevel` | 0.05 |  | Station-upgrade craft threshold reduction per nation level for stations in the crafter's own claim (0.05 = -5%/level, floored at 50% of the base threshold). 0 disables. DEFAULT: 0.05 |

## `[WEAPON_LEGEND]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Count kills on forged items and show tier flair. DEFAULT: true |
| `tier1Kills` | 100 |  | Kills for tier 1 (Blooded — lore line appears). DEFAULT: 100 |
| `tier2Kills` | 1,000 |  | Kills for tier 2 (Renowned — ✯ name suffix). DEFAULT: 1000 |
| `tier3Kills` | 10,000 |  | Kills for tier 3 (Legendary — gold name + ✯✯). DEFAULT: 10000 |
| `bossKillsForEngraving` | 25 |  | Boss kills that grant the one-time extra engraving. DEFAULT: 25 |
| `countPvp` | true |  | Player kills count toward the tally. DEFAULT: true |

## `[SALVAGE]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable the Salvage button on the Forge Station menu (dismantle + engraving reroll). DEFAULT: true |
| `refundPercentByRank` | "20,25,30,40,50,60,75" |  | Percent of each item ingredient refunded on salvage, per quality rank POOR..MYTHICAL (7 comma-separated entries; floored per ingredient; tag ingredients never refund). DEFAULT: 20,25,30,40,50,60,75 |
| `scrollChancePercent` | 25 |  | Percent chance, rolled per engraving on the salvaged item until one hits, that an Engraving Scroll capturing it drops. Max one scroll per salvage. DEFAULT: 25 |
| `rerollCap` | 3 |  | Maximum engraving rerolls per forged item (stored on the item, survives Reforge). DEFAULT: 3 |
| `rerollMaterialPercent` | 25 |  | Percent of each recipe ingredient charged per reroll (ceil, minimum 1 of each). Creative players pay no materials. DEFAULT: 25 |
| `rerollDollarsByRank` | "0,0,0,2500,7500,20000,50000" |  | Cash charged per reroll in whole dollars, per quality rank POOR..MYTHICAL (7 entries). Requires Ultimate Banking System; skipped entirely without it. DEFAULT: 0,0,0,2500,7500,20000,50000 |
