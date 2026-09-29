# Commands

<small>[Ascension](../index.md)</small>

`<value>` is a required argument, `[value]` is optional. The permission column shows who can run it by default.

## `/tascension checkultprogress`

| Syntax | Permission |
|---|---|
| `/tascension checkultprogress <ultimate> <player>` | Operator (level 2) |

## `/tascension cooldown`

| Syntax | Permission |
|---|---|
| `/tascension cooldown reset <targets>` | Operator (level 2) |

## Game rules

Change these with `/gamerule <name> <value>`.

| Game rule | Default | Description |
|---|---|---|
| `doAscensionUltimate` | true | If false, the Awakening Altar refuses to absorb catalysts and the awakening ritual cannot be started. Default: true. |

## Command feedback messages

<details markdown><summary>Show 15 messages</summary>

| Key | Message |
|---|---|
| `ascension.command.cooldown.reset.target` | Your awakening cooldown has been reset. |
| `ascension.command.cooldown.reset.success` | Reset awakening cooldown for %s player(s). |
| `ascension.command.checkult.bad_id` | Could not parse '%s' as an Ultimate id. |
| `ascension.command.checkult.unknown` | No registered awakening for '%s'. |
| `ascension.command.checkult.title` | Awakening Progress: %s |
| `ascension.command.checkult.already_awakened` | Already awakened — nothing left to check. |
| `ascension.command.checkult.gamerule` | Master switch (doAscensionUltimate): %s |
| `ascension.command.checkult.ep` | Max EP: %s / %s |
| `ascension.command.checkult.status` | Awakened status: %s |
| `ascension.command.checkult.prereq` | %s mastered: %s |
| `ascension.command.checkult.cooldown` | Cooldown: %s |
| `ascension.command.checkult.gate` | Per-Ultimate gate: %s |
| `ascension.command.checkult.no_gate` | Per-Ultimate gate: none |
| `ascension.command.checkult.ready` | All gates clear — ready to awaken! |
| `ascension.command.checkult.not_ready` | Not yet ready. |

</details>
