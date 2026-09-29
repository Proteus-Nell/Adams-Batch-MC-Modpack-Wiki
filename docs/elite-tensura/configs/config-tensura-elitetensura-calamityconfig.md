# `config/tensura/EliteTensura/CalamityConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[CalamityCore]`

| Option | Default | Range | Description |
|---|---|---|---|
| `bossEntityIds` | "tensura:orc_lord,tensura:arch_daemon,elitetensura:lich_boss,elitetensura:gravebound_colossus,elitetensura:choir_heart" |  | Comma-separated entity IDs eligible to spawn as a calamity boss |
| `hpMultiplier` | 3 |  | Boss max health multiplier |
| `damageMultiplier` | 2 |  | Boss attack damage multiplier |
| `minIntervalHours` | 2 |  | Minimum hours between automatic calamity events |
| `maxIntervalHours` | 6 |  | Maximum hours between automatic calamity events |
| `maxDurationMinutes` | 30 |  | Minutes before an undefeated calamity recedes |
| `rewardContributionPercent` | 10 |  | Percent of boss max HP a player must deal to qualify for rewards |
| `crateRewardsEnabled` | true |  | Grant crate keys to qualifying contributors on calamity defeat |
| `contributorCrateId` | "rare" |  | Crate id whose keys qualifying contributors receive |
| `contributorRareKeys` | 1 |  | Rare crate keys given to each qualifying contributor |
| `topContributorCrateId` | "elite" |  | Crate id whose keys the top damage dealer receives |
| `topContributorEliteKeys` | 1 |  | Elite crate keys given to the top damage dealer |
| `damagerPotentialCatalysts` | 1 |  | Potential Catalysts given to every player who damaged the calamity |
| `eventTitleId` | "calamity_slayer" |  | Title awarded to qualifying contributors on calamity defeat |
| `bossBarRadius` | 96 |  | Radius in blocks within which players see the calamity boss bar |
| `maxDamagePerHit` | 50 |  | Max damage a calamity boss can take from a single player hit (0 = no cap) |
| `playerShareCapPercent` | 25 |  | Percent of boss max HP one player may deal in total (0 = no cap) |
| `shareCapMinPlayers` | 4 |  | Minimum online players for the share cap to apply |
| `minQualifiedPlayers` | 2 |  | Minimum online players meeting qualifyingPlayerEP for an automatic calamity to start (0 = no gate). Admin /etadmin calamity start bypasses this. |
| `qualifyingPlayerEP` | 100,000 |  | Max EP a player must have to count toward minQualifiedPlayers |
| `spawnExclusionHalfExtent` | 125 |  | Blocks from 0,0 on both axes where a calamity may not spawn — 125 excludes a 250x250 box centred on origin (0 = no exclusion). Applies in every dimension. |
| `spawnMode` | "TERRITORY" |  | Spawn mode: TERRITORY (Walpurgis claims, then random player), FIXED (spawnDimension at spawnX/spawnZ), PLAYER (near a random online player), TEAM_BASE (random FTB team claim with a player standing in it) |
| `spawnDimension` | "minecraft:overworld" |  | FIXED mode: dimension id, e.g. minecraft:overworld |
| `spawnX` | 0 |  | FIXED mode: X block coordinate |
| `spawnZ` | 0 |  | FIXED mode: Z block coordinate |
| `shieldEnabled` | true |  | Resonance shield master switch (requires 2+ computed breakers to activate) |
| `shieldPlayerDivisor` | 2 |  | Required shield breakers = ceil(onlinePlayers / this), clamped to shieldMaxPlayers |
| `shieldMaxPlayers` | 5 |  | Upper clamp on required shield breakers |
| `shieldBreakWindowSeconds` | 15 |  | Seconds within which distinct players must all land a hit to shatter the shield |
| `vulnerabilitySeconds` | 20 |  | Seconds the boss stays vulnerable after a shield shatter |
| `shieldDecayMinutes` | 5 |  | Minutes of unbroken shield before the required breaker count drops by 1 |
| `bossHealMultiplier` | 0.25 |  | Multiplier on all calamity boss healing (1.0 = unchanged, 0 = no healing) |
| `lootDespawnMinutes` | 10 |  | Minutes before instanced victory drops despawn |

## `[LichBoss]`

| Option | Default | Range | Description |
|---|---|---|---|
| `maxHealth` | 5,000 |  | Max health. |
| `attackDamage` | 80 |  | Attack damage. |
| `armor` | 280 |  | Armor. |
| `maxMagicule` | 250,000 |  | Base magicule/aura pools (kill EP payout derives from these). |
| `maxAura` | 250,000 |  |  |
| `minionWallDamageMultiplier` | 0.1 |  | Damage multiplier while &gt;=1 tethered minion is alive (0.1 = 90% reduction). |
| `siphonPercent` | 0.8 |  | Fraction of damage dealt returned as healing (phase 1-2). |
| `siphonPercentP3` | 0.8 |  | Siphon fraction in phase 3 and during Last Rites. |
| `hitCapPercent` | 0.04 |  | Single-hit damage cap as a fraction of max HP. |
| `holyFireVulnerability` | 1.25 |  | Bonus damage multiplier taken from HOLY-element and fire sources. |
| `anchorMaxRegenPerSecond` | 15 |  | Max HP/s regen from chunk magicule at full saturation (ETMagiculeWorldSystem on). |
| `anchorMagiculePerHp` | 10 |  | Chunk magicule consumed per HP regenerated. |
| `anchorFallbackRegen` | 5 |  | Flat HP/s regen when the Magicule World system is off. |
| `waveSizeMin` | 4 |  | Minions per wave (min/max). |
| `waveSizeMax` | 6 |  |  |
| `waveCooldownSeconds` | 60 |  | Seconds between minion waves once the previous wave is dead (phase 2+). |
| `lastRitesEnabled` | true |  | Enable the one-time Last Rites death defiance. |
| `targetEpGate` | 10,000 |  | Only initiates attacks on targets with at least this max EP. |

## `[GraveboundColossus]`

| Option | Default | Range | Description |
|---|---|---|---|
| `maxHealth` | 8,000 |  | Max health. |
| `attackDamage` | 60 |  | Attack damage. |
| `armor` | 200 |  | Armor. |
| `maxMagicule` | 250,000 |  | Base magicule/aura pools (kill EP payout derives from these). |
| `maxAura` | 250,000 |  |  |
| `targetEpGate` | 10,000 |  | Only initiates attacks on targets with at least this max EP. |
| `engageRange` | 48 |  | Blocks within which the Colossus engages. It never moves, so this is its whole reach. |
| `sigilHealth` | 400 |  | Health of each of the three Sigils. |
| `sigilBossDamageFraction` | 0.2 |  | Fraction of incoming damage the boss takes while any Sigil stands (rest hits the Sigil). |
| `exposedSeconds` | 12 |  | Seconds the Exposed burn window lasts once all three Sigils break. |
| `exposedDamageMultiplier` | 2 |  | Damage multiplier taken while Exposed. |
| `slamCooldownSeconds` | 6 |  | Slam Shockwave: seconds between casts. |
| `slamRadius` | 12 |  | Slam Shockwave: max ring radius in blocks. |
| `spireCooldownSeconds` | 8 |  | Grave Spire: seconds between casts (the answer to ranged attackers). |
| `spireRadius` | 1.5 |  | Grave Spire: column radius in blocks. |
| `spireDamageMultiplier` | 1.5 |  | Grave Spire: damage as a multiple of attack damage. |
| `wellCooldownSeconds` | 14 |  | Gravity Well: seconds between casts (phase 2+). |
| `wellDurationSeconds` | 3 |  | Gravity Well: seconds the pull lasts. |
| `wellRadius` | 24 |  | Gravity Well: pull radius in blocks. |
| `wellPullStrength` | 0.08 |  | Gravity Well: per-tick pull strength. |
| `zoneCooldownSeconds` | 10 |  | Sunder Zones: seconds between casts (phase 2+). |
| `zoneDurationSeconds` | 12 |  | Sunder Zones: seconds each zone persists. |
| `zoneRadius` | 3 |  | Sunder Zones: radius in blocks. |
| `zoneDamageMultiplier` | 0.5 |  | Sunder Zones: damage per second as a multiple of attack damage. |
| `resistanceBypassLevel` | 1 |  | Resistance bypass level stamped on every attack. 1.0 demotes a Nullification to a plain Resistance, 2.0 ignores resistances entirely, 0 disables. |
| `barrierBypassLevel` | 1 |  | Barrier bypass level stamped on every attack. 0 disables. |
| `enrageAfterSeconds` | 30 |  | Seconds with no engaged target before the Colossus starts regenerating. |
| `enrageRegenPercent` | 2 |  | Percent of max HP regenerated per second once unengaged. |

## `[HollowChoir]`

| Option | Default | Range | Description |
|---|---|---|---|
| `heartMaxHealth` | 6,000 |  | Choir Heart max health. |
| `heartArmor` | 220 |  | Choir Heart armor. |
| `attackDamage` | 45 |  | Dirge pulse base damage (scaled by the calamity damage multiplier). |
| `maxMagicule` | 250,000 |  | Choir Heart max magicule (drives Tensura EP reward). |
| `maxAura` | 250,000 |  | Choir Heart max aura (drives Tensura EP reward). |
| `voiceMaxHealth` | 300 |  | Voice max health at an unbuffed Heart; scales with the calamity HP multiplier. |
| `voicesPhase1` | 6 |  | Voices spawned when phase 1 begins (spawn). |
| `voicesPhase2` | 5 |  | Voices respawned at the 66% health re-split. |
| `voicesPhase3` | 4 |  | Voices respawned at the 33% health re-split. |
| `voiceOrbitRadius` | 5 |  | Orbit radius (blocks) of the Voices around the Heart. |
| `voiceSummonedSeconds` | 900 |  | Tensura summon-timer seconds on each Voice — a leak guard inside the event cap. |
| `voiceTransferPercent` | 0.35 |  | Fraction of damage dealt to a Voice mirrored onto the Heart, credited to the attacker. |
| `wardMinVoices` | 3 |  | Living Voices needed for the Choir Ward: below this, the Heart takes full direct damage. |
| `wardPassthroughFraction` | 0.15 |  | Fraction of direct damage that still reaches the warded Heart (the rest deflects). |
| `respawnImmunitySeconds` | 2 |  | Seconds of Heart damage immunity covering each re-split swap. |
| `songRadius` | 14 |  | Song aura radius (blocks); requires line of sight from the Voice. |
| `songEscalateSeconds` | 8 |  | Seconds of continuous exposure per extra song amplifier step (halved in phase 3). |
| `songAmpCap` | 2 |  | Maximum song effect amplifier (0-indexed). |
| `dirgeCooldownSeconds` | 8 |  | Dirge pulse cooldown in seconds (x0.7 in phase 3). |
| `dirgeRadius` | 8 |  | Dirge pulse radius (blocks) around the Heart. |
| `dirgeDamageMultiplier` | 1 |  | Dirge damage as a multiplier of the Heart's attack damage. |

## `[Starfall]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch. Off: no automatic starfalls, scheduler/admin starts refused, any live event is swept. DEFAULT: true |
| `minIntervalHours` | 3 |  | Minimum hours between automatic starfalls. DEFAULT: 3.0 |
| `maxIntervalHours` | 8 |  | Maximum hours between automatic starfalls. DEFAULT: 8.0 |
| `minOnlinePlayers` | 3 |  | Online players required for an automatic starfall (admin/scheduler starts bypass this). DEFAULT: 3 |
| `siteMode` | "NEAR_PLAYER" |  | Where the star lands: SPAWN_RING (ring around world spawn), NEAR_PLAYER (offset from a random overworld player), PLAYER_CENTROID (offset from the players' centre). DEFAULT: NEAR_PLAYER |
| `spawnRingMinBlocks` | 300 |  | SPAWN_RING: minimum distance from world spawn in blocks. DEFAULT: 300 |
| `spawnRingMaxBlocks` | 800 |  | SPAWN_RING: maximum distance from world spawn in blocks. DEFAULT: 800 |
| `playerMinBlocks` | 150 |  | NEAR_PLAYER / PLAYER_CENTROID: minimum offset in blocks. DEFAULT: 150 |
| `playerMaxBlocks` | 500 |  | NEAR_PLAYER / PLAYER_CENTROID: maximum offset in blocks. DEFAULT: 500 |
| `spawnExclusionBlocks` | 128 |  | Never land within this many blocks of world spawn (square box). DEFAULT: 128 |
| `avoidClaims` | true |  | Reject sites where any chunk in the 3x3 around the impact is FTB-claimed or a Walpurgis territory. DEFAULT: true |
| `foreshadowMinutes` | 5 |  | Minutes between the Voice foreshadow and the impact. DEFAULT: 5 |
| `descentSeconds` | 8 |  | Seconds the meteor is visible falling before impact. DEFAULT: 8 |
| `clusterSize` | "MEDIUM" |  | Ore cluster size: SMALL (3), MEDIUM (6), LARGE (10). DEFAULT: MEDIUM |
| `oreDespawnMinutes` | 20 |  | Minutes after impact before unmined Starfall Ore evaporates. DEFAULT: 20 |
| `witnessRadius` | 96 |  | Players within this many blocks of the impact count as witnesses (title/record counter). DEFAULT: 96 |
| `announceVoice` | true |  | Announce foreshadow and impact through the Voice of the World banner. DEFAULT: true |
| `announceDiscord` | true |  | Announce foreshadow and impact on the Discord WORLD webhook. DEFAULT: true |
| `mapMarkers` | true |  | Send the Starfall foreshadow wedge and post-impact pin to players' FTB maps. DEFAULT: true |
