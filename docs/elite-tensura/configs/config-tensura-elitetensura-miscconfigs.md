# `config/tensura/EliteTensura/MiscConfigs.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[ULTIMATE_SKILLS]`

| Option | Default | Range | Description |
|---|---|---|---|
| `requirementsEnabled` | true |  | Enable ultimate skill unlock requirements (mastered prerequisites, EP, Awakened). DEFAULT: true |

## `[CHATEVENTS]`

| Option | Default | Range | Description |
|---|---|---|---|
| `chatEvents` | true |  | Are chat events enabled? DEFAULT: true |
| `PlayersNeeded` | 6 |  | Players needed on the server to enable this event? Default: 6 |
| `PlayersWinCommon` | 2 |  | COMMON Tier Wins Required DEFAULT: 2 |
| `PlayersWinUnCommon` | 8 |  | UNCOMMON Tier Wins Required DEFAULT: 8 |
| `PlayersWinRARE` | 16 |  | RARE Tier Wins Required DEFAULT: 16 |
| `PlayersWinEPIC` | 25 |  | EPIC Tier Wins Required DEFAULT: 25 |
| `PlayersWinLEGENDARY` | 30 |  | LEGENDARY Tier Wins Required DEFAULT: 30 |
| `INTERVAL_MINS` | 15 |  | How many Mins before the checks are done? |
| `ANSWER_TIMEOUT` | 30 |  | Answer timeout in seconds |
| `questions` | "How did Goku defeat Master Carrot?\|moon", "What is Goku's biological Mother's name?\|gine", "What is the name of Goku's wife?\|chi chi", "Which character is Uub a reincarnation of?\|buu", "Who is the 7th God of Destruction?\|beerus", "Who is God of Destruction in Universe 6?\|champa", "What is Vegeta's brother name?\|tarble", "What Universe is Jiren in?\|11", "Who is Trunk's mother?\|bulma", "What is the business Bulma helps develop for?\|capsule corp", "What is the name of Goku's father?\|bardock", "What planet are Saiyans originally from?\|sadala", "What is Gohan's daughter's name?\|pan", "Who trained Goku as a child?\|roshi", "What is the name of Vegeta's home planet?\|vegeta", "Who is the Supreme Kai of Universe 7?\|shin", "What transformation comes after Super Saiyan 2?\|super saiyan 3", "What is the name of Beerus's angel?\|whis", "Who killed Krillin causing Goku to go Super Saiyan?\|frieza", "What form does Goku use Ultra Instinct in?\|mastered ultra instinct" ... (40 total) |  | QnA questions, one per entry, format 'question\|answer' (answer lowercase). DEFAULT: built-in trivia list |

## `[TITLESSystem]`

| Option | Default | Range | Description |
|---|---|---|---|
| `maxActiveSynergies` | 3 |  | Maximum number of title synergies that can be active simultaneously. DEFAULT: 3 |
| `maxTitleSlots` | 10 |  | Maximum number of titles that can be active simultaneously. DEFAULT: 10 |
| `resets_per_slot` | 2 |  | Number of resets to gain more slots. DEFAULT: 2 |
| `base_slots` | 3 |  | Number of base slots you have before the Resets Per Slots. DEFAULT: 3 |

## `[BANKING]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mobCashDropAlerts` | false |  | Show the Ultimate Banking System popup alert when a mob drops cash. DEFAULT: true |
| `balanceChangeAlerts` | false |  | Show the Ultimate Banking System 'Balance' popup on every account gain/loss (auto-pickup makes this per-kill spam). DEFAULT: false |

## `[ENGRAVING]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable replacing natural Rare/Epic engraving rolls with Elite Tensura custom engravings. DEFAULT: true |
| `replaceChance` | 25 |  | Percent chance a natural Rare/Epic engraving roll is replaced by a custom engraving. DEFAULT: 25.0 |
| `cursedEnabled` | true |  | Enable the cursed engravings (strong buff + real drawback): both acquisition paths — native curse-roll substitution and forge critical outcomes. DEFAULT: true |
| `cursedSubstituteChance` | 50 |  | Percent of Tensura's native curse rolls substituted with an Elite Tensura cursed engraving. DEFAULT: 50.0 |
| `cursedForgeCritChance` | 15 |  | Percent chance a forge craft whose quality roll fired at least one critical upgrade also gains a cursed engraving. DEFAULT: 15.0 |

## `[PVP]`

| Option | Default | Range | Description |
|---|---|---|---|
| `blockEpTransfer` | true |  | Block EP transfer on player-vs-player kills: killer gains no EP, victim loses no EP/soul points. PvE deaths are unaffected. DEFAULT: true |

## `[DEATHRECAP]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Show a damage recap panel on the death screen: the last few hits taken, with what the damage event chain did to each. DEFAULT: true |
| `historySize` | 8 |  | How many recent damage instances to keep per player. DEFAULT: 8 |

## `[BOSS_CONTRIBUTION]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Send the live boss-contribution HUD panel (your damage + share vs the top three) to contributors during calamities, nation raids and finale sieges. DEFAULT: true |
| `intervalTicks` | 40 |  | Ticks between contribution updates, clamped to 1-120 (the client drops the panel 120 ticks after the last update). All three events only check once a second, so the effective cadence is the next multiple of 20 at or above this value. DEFAULT: 40 |

## `[CHRONICLE]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable the server chronicle feed (Codex Events tab): world-firsts, wars, calamities, awakenings, nation lifecycle, season closes, Walpurgis motions. DEFAULT: true |
| `maxEntries` | 150 |  | Maximum feed entries kept in the world save; the oldest is evicted past the cap. DEFAULT: 150 |

## `[PROCLAMATIONS]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable /etproclaim — players pay to push a message into the chronicle feed, the Voice banner and Discord. DEFAULT: true |
| `feeDollars` | 10,000 |  | Fee in whole dollars, charged from the poster's own bank. 0 = free (and works without Ultimate Banking System installed). DEFAULT: 10000 |
| `cooldownHours` | 6 |  | Hours a player must wait between proclamations (game time — survives restarts). 0 or less = no cooldown. DEFAULT: 6 |
| `maxLength` | 200 |  | Maximum message length in characters after formatting codes are stripped. 0 or less = no cap. DEFAULT: 200 |
| `sovereignsOnly` | false |  | Restrict proclamations to nation sovereigns. DEFAULT: false |
| `announceVoice` | true |  | Also announce each proclamation as a Voice of the World banner (still subject to the Voice system's own enableWorldEvents). DEFAULT: true |
| `announceDiscord` | true |  | Also post each proclamation to the Discord WORLD webhook. DEFAULT: true |

## `[AETHERFORGED_PLATE]`

| Option | Default | Range | Description |
|---|---|---|---|
| `maxReductionPercent` | 25 |  | Max damage reduction % from wearing the full 4-piece Aetherforged Plate set, scaled by wearer EP up to Refs.ultimateUnlockEPCost (linear ramp, 0% at 0 EP to this value at ultimateUnlockEPCost+). DEFAULT: 25.0 |

## `[CRATES]`

| Option | Default | Range | Description |
|---|---|---|---|
| `pityEnabled` | true |  | Enable crate pity: at most N opens of one crate without a reward at/above pityFloor — the Nth consecutive dry open rolls only from that pool. DEFAULT: true |
| `pityFloor` | "RARE" |  | Rarity that counts as a pity hit and forms the forced pool. One of COMMON, UNCOMMON, RARE, EPIC, LEGENDARY. DEFAULT: RARE |
| `pityThresholds` | "common=15,rare=0,elite=0" |  | Per-crate hard pity thresholds as crateId=N pairs. 0 disables pity for that crate. Rare/Elite default off — their natural Rare+ rate (29% / 62%) makes a guarantee meaningless. DEFAULT: common=15,rare=0,elite=0 |
| `pityDefaultThreshold` | 10 |  | Threshold for any crate id not listed in pityThresholds. 0 disables. DEFAULT: 10 |
| `fxFloor` | "RARE" |  | Minimum reward rarity for totem particles + level-up sound at the crate block. DEFAULT: RARE |
| `fireworkFloor` | "EPIC" |  | Minimum reward rarity for a firework burst at the crate block. DEFAULT: EPIC |

## `[NAMEPLATE]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch for showcase titles (the line above player nameplates and the tab-list suffix). DEFAULT: true |
| `nameplate` | true |  | Draw each player's showcase title as a line above their nameplate. DEFAULT: true |
| `tabList` | true |  | Append the showcase title after the name in the tab list: Name [Title]. DEFAULT: true |
| `nameplateScale` | 0.85 |  | Scale of the nameplate title line relative to the name text. DEFAULT: 0.85 |

## `[SCHEDULES]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch for /etadmin schedule. Off: nothing fires; the list can still be edited. DEFAULT: true |
| `announceLeadMinutes` | 10 |  | Minutes before a scheduled event to announce it. DEFAULT: 10 |
| `announceVoice` | true |  | Announce upcoming scheduled events through the Voice of the World banner. DEFAULT: true |
| `announceDiscord` | true |  | Announce upcoming scheduled events (and skipped fires) on the Discord WORLD webhook. DEFAULT: true |

## `[WORLD_LEDGER]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch for the World Ledger (server-wide lifetime counters with tier rewards). Off: no polling, no Codex Stats group, /etadmin ledger reports disabled. DEFAULT: true |
| `pollIntervalTicks` | 1,200 |  | Ticks between ledger polls (each poll sums every player's counters). Clamped to &gt;= 200. DEFAULT: 1200 |
| `minLegacy` | 1 |  | Minimum Legacy points paid to any contributor with a non-zero count when a tier completes, even if their share rounds to 0. DEFAULT: 1 |
| `announceVoice` | true |  | Announce tier completions through the Voice of the World banner. DEFAULT: true |
| `announceDiscord` | true |  | Announce tier completions on the Discord WORLD webhook. DEFAULT: true |
| `killsTiers` | "10000,100000,1000000" |  | Kills tier thresholds. DEFAULT: 10000,100000,1000000 |
| `killsLegacy` | "50,150,500" |  | Legacy pool split among contributors per kills tier. DEFAULT: 50,150,500 |
| `killsLadder` | "25,75,250" |  | Nation-ladder pool split among contributing nations per kills tier (active season only). DEFAULT: 25,75,250 |
| `calamitiesTiers` | "10,50,200" |  | Calamities-slain tier thresholds. DEFAULT: 10,50,200 |
| `calamitiesLegacy` | "50,150,500" |  | Legacy pool per calamities tier. DEFAULT: 50,150,500 |
| `calamitiesLadder` | "25,75,250" |  | Nation-ladder pool per calamities tier. DEFAULT: 25,75,250 |
| `forgeCraftsTiers` | "500,5000,50000" |  | Items-forged tier thresholds. DEFAULT: 500,5000,50000 |
| `forgeCraftsLegacy` | "50,150,500" |  | Legacy pool per forge tier. DEFAULT: 50,150,500 |
| `forgeCraftsLadder` | "25,75,250" |  | Nation-ladder pool per forge tier. DEFAULT: 25,75,250 |
| `titlesTiers` | "200,1000,5000" |  | Titles-unlocked tier thresholds (sum of every player's earned titles). DEFAULT: 200,1000,5000 |
| `titlesLegacy` | "50,150,500" |  | Legacy pool per titles tier. DEFAULT: 50,150,500 |
| `titlesLadder` | "25,75,250" |  | Nation-ladder pool per titles tier. DEFAULT: 25,75,250 |
