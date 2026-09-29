# `config/tensura/EliteTensura/WarConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[War]`

| Option | Default | Range | Description |
|---|---|---|---|
| `warCooldownTicks` | 144,000 |  | Ticks a war stays in COOLDOWN (blocking re-declaration) after it ends (144000 = 2 hours). |
| `maxActiveWarsPerNation` | 1 |  | Hard cap on how many wars one nation may be involved in at once (counting both principal and ally roles). |
| `allianceBreakCooldownTicks` | 144,000 |  | Ticks before two nations may re-ally after breaking an alliance (144000 = 2 hours). |
| `warmupTicks` | 1,728,000 |  | Ticks a declared war spends in WARMUP before hostilities begin (1728000 = 24 hours). |
| `warDurationTicks` | 5,184,000 |  | Ticks a war spends in its ACTIVE phase; whichever side has the higher score at the deadline wins (5184000 = 72 hours). |
| `loserGraceTicks` | 1,728,000 |  | Ticks after a war loss during which the losing nation cannot be declared on by anyone (1728000 = 24 hours). |
| `killPoints` | 10 |  | Base war-score points awarded per enemy kill. |
| `enemyTerritoryMultiplier` | 2 |  | Kill-point multiplier applied when the victim dies inside their own side's claimed territory. |
| `craftPointsMasterwork` | 1 |  | War-score points a member earns by forging a MASTERWORK item during an active war. 0 disables craft points. |
| `craftPointsLegendary` | 2 |  | War-score points for forging a LEGENDARY item during an active war. |
| `craftPointsMythical` | 3 |  | War-score points for forging a MYTHICAL item during an active war. |
| `crateRewardsEnabled` | true |  | Grant crate keys to the winning nation when a war resolves (surrender/forced end; peace and cancel grant nothing). |
| `victorMemberCrateId` | "rare" |  | Crate id whose key every online member of the winning nation receives. Empty = none. |
| `victorTopCrateId` | "elite" |  | Crate id whose key the winning side's top war-point scorer receives on top. Empty = none. |
| `secondKillMultiplier` | 0.5 |  | Kill-point multiplier for the same killer's 2nd kill of the same victim within the diminishing-returns window. |
| `thirdKillMultiplier` | 0.25 |  | Kill-point multiplier for the same killer's 3rd and later kills of the same victim within the diminishing-returns window. |
| `killWindowTicks` | 72,000 |  | Rolling window during which repeat kills of the same victim by the same killer have diminishing returns (72000 = 1 hour). |
| `warningGap` | 100 |  | War-score gap between sides that fires the one-time 'brink of defeat' announcement. |
| `bountyRotationTicks` | 288,000 |  | Period between automatic bounty objective rotations (288000 = 4 hours). |
| `leaderBountyPoints` | 50 |  | War-score points awarded for the Regicide bounty: killing the enemy nation's Sovereign. |
| `firstBloodPoints` | 15 |  | War-score points awarded for the First Blood bounty: the first kill of the current rotation. |
| `rampagePoints` | 30 |  | War-score points awarded for the Rampage bounty: killing 3 distinct enemy victims within one rotation. |
| `playerBountyPoints` | 20 |  | Side war-score points awarded for claiming a leader-placed player bounty. |
| `minPlayerBountyCents` | 100,000 |  | Minimum amount, in cents, a nation leader may place as a bounty on a player (100000 = $1000). |
| `declareLevelGapPenalty` | 0.25 |  | Extra fraction added to the war declaration cost per nation level the attacker is above the defender (0.25 = +25% per level gap). |
| `debug` | false |  | Log war evaluation to the server log. |
| `mapOverlayEnabled` | true |  | Server kill switch for the FTB Chunks map war overlay: enemy claim tint + Nation Core pins. DEFAULT: true |
| `mapEnemyColor` | "#D62828" |  | Hex colour (#RRGGBB) used to tint enemy-nation claims on the FTB map while at war. DEFAULT: #D62828 |
| `nexusEnabled` | true |  | Ley Nexus war-front objectives: spawn contested sites between the belligerents while a war is ACTIVE. DEFAULT: true |
| `nexusSiteThresholds` | "40,120" |  | Combined claim count of both principals needed for a 2nd and a 3rd Nexus site (comma list). DEFAULT: 40,120 |
| `nexusRadiusBlocks` | 16 |  | Radius in blocks around a Nexus that counts as standing on it. DEFAULT: 16 |
| `nexusCaptureSeconds` | 60 |  | Seconds of uncontested majority presence to capture (or fully flip) a Nexus. DEFAULT: 60 |
| `nexusPointsPerMinute` | 2 |  | War points a held Nexus pays per minute while a holder stands inside (a kill is killPoints). DEFAULT: 2 |
| `nexusMinClaimDistanceChunks` | 2 |  | Chunk halo around a candidate site that must be free of FTB claims. DEFAULT: 2 |
| `nexusSpacingBlocks` | 160 |  | Minimum distance in blocks between two Nexus sites. DEFAULT: 160 |
| `nexusScatterMinBlocks` | 32 |  | Random scatter of a site around its target point on the line between territories: minimum blocks. DEFAULT: 32 |
| `nexusScatterMaxBlocks` | 128 |  | Random scatter of a site around its target point: maximum blocks. DEFAULT: 128 |
| `nexusSpawnExclusionBlocks` | 128 |  | Never place a Nexus within this many blocks of world spawn (square box). DEFAULT: 128 |
| `nexusAnnounceVoice` | true |  | Announce Nexus reveal / capture / loss through the Voice of the World (the Chronicle always records). DEFAULT: true |
| `nexusAnnounceDiscord` | true |  | Post Nexus reveal / capture to the Discord nation webhook. DEFAULT: true |
| `termsEnabled` | true |  | Peace terms: the victor of a resolved war picks lasting terms (pact / tribute / vassalage) capped by the score margin. DEFAULT: true |
| `termsPickHours` | 24 |  | Real hours the victor's sovereign has to pick terms after a war resolves; unpicked = non-aggression pact. DEFAULT: 24 |
| `termsDays` | 7 |  | Real days peace terms last once chosen. DEFAULT: 7 |
| `termsTributeRatio` | 1.25 |  | Winner/loser score ratio that unlocks tribute. DEFAULT: 1.25 |
| `termsVassalRatio` | 2 |  | Winner/loser score ratio that unlocks vassalage (a voluntary surrender always does). DEFAULT: 2.0 |
| `termsTributePercent` | 10 |  | Daily tribute as a percent of the vanquished nation's projected hourly income x 24, frozen when the tier is chosen. DEFAULT: 10.0 |
| `termsTributeMinDailyCents` | 20,000 |  | Floor for daily tribute in cents (20000 = $200). DEFAULT: 20000 |
| `termsTributeCatchUpDays` | 1 |  | Tribute days settled per minute-tick after downtime; days beyond the budget are still marked settled (forfeit). DEFAULT: 1 |
| `termsVassalAutoJoin` | true |  | Vassals auto-join their liege's wars and a liege auto-joins wars declared on its vassal (skipped at the war cap). DEFAULT: true |
| `termsAnnounceVoice` | true |  | Announce imposed / expired terms and vassal releases through the Voice of the World (the Chronicle always records). DEFAULT: true |
| `termsAnnounceDiscord` | true |  | Post imposed / expired terms to the Discord nation webhook. DEFAULT: true |
