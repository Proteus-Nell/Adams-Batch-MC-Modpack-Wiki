# `config/tensura/EliteTensura/TournamentConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Tournament]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch — no gamerule: tournaments only run when an admin schedules one |
| `maxPlayers` | 16 |  | Default signup cap when the schedule command gives none (hard cap 32) |
| `matchTimeCapSeconds` | 300 |  | Seconds a match may run before the damage-dealt tiebreak decides it |
| `arenaRadius` | 24 |  | Blocks from the arena anchor a fighter may stray before the boundary grace countdown starts |
| `spawnDistance` | 8 |  | Blocks from the anchor each fighter is placed at match start (opposing sides) |
| `boundaryGraceSeconds` | 5 |  | Seconds a fighter has to return inside the arena before forfeiting |
| `preMatchCountdownSeconds` | 5 |  | Seconds of pre-match countdown before fighter-vs-fighter damage is allowed |
| `betweenMatchSeconds` | 20 |  | Seconds between one match ending and the next starting |
| `respawnGraceSeconds` | 30 |  | Seconds a dead fighter has to respawn at match start before their opponent walks over |
| `nationLadderPoints` | 50 |  | Nation season-ladder points banked for the champion's nation (0 = none) |
| `announceDiscord` | true |  | Post the scheduled and champion announcements to the Discord world-event webhook |
| `squadSizeDefault` | 3 |  | Nation-format squad size when the schedule command gives none |

## `[Wagers]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Champion wager pool during signups (needs Ultimate Banking System installed) |
| `minBet` | 100 |  | Minimum single bet, whole dollars |
| `maxBet` | 100,000 |  | Maximum total stake per bettor, whole dollars |
| `houseCutPercent` | 10 |  | Percent of the losing stakes kept by the house (central bank reserve) at settlement |
