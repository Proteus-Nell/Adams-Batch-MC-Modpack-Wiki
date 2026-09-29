# `config/tensura/EliteTensura/SeasonConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Chronicle]`

| Option | Default | Range | Description |
|---|---|---|---|
| `dailiesPerDay` | 2 |  | Daily objectives rolled per player per real day. |
| `dailyCrateId` | "common" |  | Crate id whose key a completed daily grants. Empty = none. |
| `dailyCrateCount` | 1 |  | Keys per completed daily. |
| `dailyMagiculeRefill` | 0 |  | Magicule restored per completed daily (clamped at max). 0 disables. |
| `announceTiers` | true |  | Broadcast tier completions in server chat. |

## `[SeasonClose]`

| Option | Default | Range | Description |
|---|---|---|---|
| `leaderboardTopN` | 3 |  | Players per leaderboard board rewarded at season end. |
| `topCrateId` | "elite" |  | Crate id whose keys season-close leaderboard winners receive. |
| `topCrateCount` | 1 |  | Keys per winning board slot. |
| `seasonTitleId` | "" |  | Fallback title id for leaderboard winners when the track JSON defines none. Empty = no title. |

## `[Legacy]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch for the Legacy Carry-Over system (cross-season cosmetic points). |
| `pointsPerChronicleTier` | 10 |  | Legacy Points awarded per chronicle tier completed during the season. |
| `pointsPerLeaderboardSlot` | 25 |  | Legacy Points awarded per top-N leaderboard slot held at season close. |
| `pointsPerNationLevel` | 2 |  | Legacy Points awarded per level of the player's nation at season close. 0 if nationless. |
| `announceTopEarners` | true |  | Broadcast the season's top Legacy Point earners in server chat at season close. |

## `[Mutators]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch for season mutators. Off = no roll at season start, all effects neutral. |
| `epGainMultiplier` | 1.5 |  | Surge of Souls: kill-EP gain multiplier for players. |
| `dailyRewardMultiplier` | 2 |  | Generous World: daily objective reward multiplier (crates + magicule refill). |
| `extraDailySlots` | 1 |  | Restless Ambition: extra daily objective slots. |
| `missionContractMultiplier` | 1.5 |  | Prosperous Trade: nation mission + contract payout multiplier. |
| `magiculeBloomMultiplier` | 1.5 |  | Magicule Bloom: magicule-world chunk regen multiplier. |
| `masteryMultiplier` | 1.5 |  | Enlightened Age: skill/magic mastery gain multiplier. |
| `cashDropMultiplier` | 2 |  | Golden Age: UBS tag-driven mob cash drop multiplier. |
| `magiculeDroughtMultiplier` | 0.5 |  | Magicule Drought: magicule-world chunk regen multiplier. |
| `calamityHpMultiplier` | 1.5 |  | Wrathful Calamities: extra multiplier on calamity boss HP (stacks on ETCalamityConfig.hpMultiplier). |
| `calamityDamageMultiplier` | 1.25 |  | Wrathful Calamities: extra multiplier on calamity boss damage. |
| `upkeepMultiplier` | 1.25 |  | Heavy Crown: nation upkeep multiplier. |
| `cruelWorldHpBonus` | 0.15 |  | Cruel World: hostile mob max-health bonus fraction on spawn (0.15 = +15%). |
| `cruelWorldDamageBonus` | 0.1 |  | Cruel World: hostile mob attack-damage bonus fraction on spawn. |
| `dailyTargetMultiplier` | 1.5 |  | Demanding Chronicle: daily objective target multiplier. |
| `calamityIntervalFactor` | 0.5 |  | Age of Calamity: calamity auto-start interval factor (0.5 = twice as often). |
| `minQualifiedReduction` | 1 |  | Age of Calamity: reduction of minQualifiedPlayers (floor 1). |
| `energyCostMultiplier` | 1.15 |  | Taxing Weave: skill/magic energy cost multiplier. |

## `[SeasonTitles]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch for season title grants (Chronicler thresholds + twist titles). |
| `bronzeTier` | 5 |  | Chronicle tier count for Chronicler (Bronze). |
| `silverTier` | 10 |  | Chronicle tier count for Chronicler (Silver). |
| `goldTier` | 15 |  | Chronicle tier count for Chronicler (Gold). |
| `droughtDailies` | 10 |  | Drought-Blessed: daily objectives completed during Magicule Drought. |
| `upkeepClears` | 7 |  | Iron Steward: clean upkeep payments by the nation during Heavy Crown. |
| `cruelWorldKills` | 500 |  | Worldbreaker: kills during Cruel World (delta from twist start). |
| `fullClearDays` | 5 |  | Relentless: full daily-clear days during Demanding Chronicle. |
| `baneBossKills` | 2 |  | Calamity's Bane: qualified calamity boss kills during Age of Calamity. |

## `[Finale]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch: season end runs the finale siege before closing. |
| `countdownMinutes` | 10 |  | Minutes between the siege announcement and wave 1. |
| `waveCount` | 4 |  | Number of mob waves before the boss. |
| `waveTimerMinutes` | 5 |  | Minutes before an unfinished wave force-advances. |
| `siegeTimeoutMinutes` | 45 |  | Minutes from siege start until the whole siege times out (loss). |
| `waveSizeBase` | 8 |  | Mobs in wave 1. |
| `waveSizePerWave` | 4 |  | Extra mobs per subsequent wave. |
| `waveMobIds` | "minecraft:zombie,minecraft:skeleton,minecraft:husk,minecraft:stray,minecraft:wither_skeleton" |  | Comma-separated wave mob entity ids. |
| `waveHpPerWave` | 0.25 |  | Extra HP multiplier applied to wave mobs, per wave index (wave 1 = base 1.0). |
| `bossIds` | "elitetensura:lich_boss,elitetensura:gravebound_colossus" |  | Comma-separated boss entity ids — one is picked at random for the final wave. |
| `bossHpMultiplier` | 3 |  | Siege boss max-health multiplier. |
| `bossDamageMultiplier` | 2 |  | Siege boss attack-damage multiplier. |
| `siegeBonusPool` | 100 |  | Legacy Points pool split pro-rata by damage on a siege win. |
| `siegeMinBonus` | 2 |  | Minimum Legacy Points for any player with tracked siege damage on a win. |
| `waveAdvanceFraction` | 0.9 |  | Fraction of a wave that must be dead to advance early (0.9 = 90%). |

## `[NationLadder]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch. Off = no points banked and no ladder shown; the nation system's own gamerule still applies on top. |
| `pointsPerTier` | 10 |  | Ladder points banked for the player's nation per chronicle tier they complete. |
| `pointsPerDaily` | 2 |  | Ladder points banked per daily objective completed. |
| `pointsPerWarWin` | 100 |  | Ladder points banked for the winning nation when a war resolves. |
| `siegePointPool` | 200 |  | Total ladder points split across nations by damage share at the finale siege. |
| `topN` | 5 |  | Nations shown in the ladder and paid siege spoils. |
| `siegeSpoilsCents` | 5,000,000 |  | Treasury pool (in CENTS) split among the top siege nations pro-rata by damage. Requires the nation economy (UBS). 0 disables the payout. |

## `[Raid]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch for /etnation raid summon (admin 'season raid start' ignores this). |
| `summonCostCents` | 50,000,000 |  | Treasury fee to summon, in cents. Ignored when the nation economy is inactive. |
| `maxRaidsPerSeason` | 1 |  | Nation summons allowed per season (admin start does not count). |
| `minOnlinePlayers` | 2 |  | Online players required to summon. |
| `countdownMinutes` | 5 |  | Minutes between the announcement and the Leviathan emerging. |
| `raidTimeoutMinutes` | 45 |  | Minutes from emerge until the raid times out (loss). |
| `enrageMinutes` | 15 |  | Minutes from emerge until soft enrage (regrow halves, Coil CD 12s, twin bolts). |
| `raidLegacyPool` | 60 |  | Legacy Points pool split pro-rata by damage on a win. |
| `raidMinLegacy` | 2 |  | Minimum Legacy Points for any player with tracked damage on a win. |
| `raidLadderPool` | 120 |  | Nation ladder points pool split pro-rata by nation damage share on a win. |
| `segmentCount` | 8 |  | Body segments (armour plates). |
| `segmentSpacing` | 1.2 |  | Distance in blocks between consecutive plate centres (plates are ~1.5 wide; &lt;1.5 overlaps like scales). |
| `segmentHp` | 1,000 |  | Plate HP. |
| `regrowSeconds` | 60 |  | Seconds for a shattered plate to regrow (halved when enraged; paused while the head is exposed). |
| `nonPlayerPlateDamageMult` | 0 |  | Plate damage multiplier for non-player sources (pets, summons). |
| `exposeIntactMax` | 4 |  | Head is vulnerable while intact plates &lt;= this. |
| `headHp` | 16,000 |  | Head attributes. |
| `headArmor` | 150 |  |  |
| `headDamage` | 140 |  |  |
| `headMagicule` | 8,000,000 |  | Base magicule/aura pools (kill EP payout derives from these). |
| `headAura` | 2,000,000 |  |  |
| `headSpiritualHealth` | 88,666 |  | Head spiritual health. |
| `spiritualDamageMult` | 0.15 |  | Multiplier on spiritual-health damage the head takes (Tensura SPIRITUAL_HURT_EVENT; 0 = immune). |
| `armorDamageMult` | 0 |  | Multiplier on armour durability loss from Leviathan hits (vanilla = damage/4 per piece; 1.0 = vanilla). |
| `submergeHealPercent` | 15 |  | Percent of max HP healed on each submerge. Submerges trigger at 75/50/25% HP. |
| `targetEpGate` | 400,000 |  | Only initiates attacks on targets with at least this max EP. |
| `abilityDamageMult` | 1.8 |  | Multiplier on every special-ability hit (whip, slam, bolt, wave, pressure/undertow dps, depth charge, coil, maw); the Bite uses headDamage unscaled. |
| `mawDrainFraction` | 0.5 |  | Fraction of CURRENT magicule and aura the Abyssal Maw drains from everyone inside its 12-block pull on the bite tick. |
| `segmentContactDamage` | 80 |  | Body-contact damage from a moving segment. |
| `maelstromDps` | 88 |  | Maelstrom damage per second. |
| `coilRadius` | 5 |  | Coil Lock radius (blocks). |
| `degradationLevel` | 2.5 |  | Value applied to every Tensura \*_DEGRADATION attribute on the head (law, resistance, physical + 9 elements). |
| `resistanceBypassLevel` | 3 |  | Tensura bypass levels stamped on every Leviathan damage source (0 = off). Resistance: &gt;=1.0 bypasses Resistance skills, &gt;=2.0 bypasses Nullification skills (Anti-Skill still blocks unless barrier &gt;=3.0). Barrier: 1.0 Reflector, 1.5 Guardian, 1.75 Pride/Instant Regen, 2.0 Infinity Prison/Falsifier/shield block, 3.0 Anti-Skill/Tuner. The \*_DEGRADATION attributes are capped at 1.0 by Tensura and only ever grant resistance level 1.0. |
| `barrierBypassLevel` | 3 |  |  |
