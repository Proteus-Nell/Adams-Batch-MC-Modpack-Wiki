# `config/tensura/EliteTensura/DiscordConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Discord]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | false |  | Master switch. When false, no Discord traffic is sent or received at all. |
| `defaultWebhookUrl` | "" |  | Default webhook URL used by every enabled category that has no override below. Blank = no default. |
| `worldUrl` | "" |  | Override webhook URL for world events (calamity, dungeon, awakenings). Blank = use default. |
| `nationUrl` | "" |  | Override webhook URL for nation / diplomacy events. Blank = use default. |
| `milestoneUrl` | "" |  | Override webhook URL for player milestones (records, achievements). Blank = use default. |
| `chatUrl` | "" |  | Override webhook URL for in-game chat relay (MC -&gt; Discord). Blank = use default. |
| `deathUrl` | "" |  | Override webhook URL for player death messages. Blank = use default. |
| `worldEnabled` | true |  | Send world-event posts to Discord. |
| `nationEnabled` | true |  | Send nation/diplomacy posts to Discord. |
| `milestoneEnabled` | true |  | Send milestone posts to Discord. |
| `chatEnabled` | true |  | Relay in-game chat to Discord. |
| `deathEnabled` | true |  | Send player death messages to Discord. |
| `serverStatusEnabled` | true |  | Post the server online/offline announcements (started / stopping). Master 'enabled' still applies on top. |
| `joinLeaveEnabled` | true |  | Post player join/leave messages to the world channel (with the player's head avatar). Master 'enabled' + worldEnabled still apply. |
| `milestoneTitleRarityFloor` | "LEGENDARY" |  | Minimum title rarity posted to the milestone channel: COMMON, UNCOMMON, RARE, EPIC, LEGENDARY, MYTHIC, UNIQUE, HARDCORE, CURSED. Blank disables title posts entirely. Without a floor every common title would post and drown the channel. |
| `milestoneCrateIds` | "elite" |  | Comma-separated crate ids whose opened reward is posted to the milestone channel. Blank = none. |
| `tensuraRaceEvolutionEnabled` | true |  | Post race evolutions (e.g. Ogre -&gt; Kijin) to the milestone channel. |
| `tensuraSkillMasteryEnabled` | true |  | Post Unique / Ultimate skill masteries to the milestone channel. |
| `tensuraSpiritLevelEnabled` | true |  | Post spirit contract upgrades to the milestone channel. |
| `tensuraSpiritLevelFloor` | "GREATER" |  | Minimum spirit level posted: LESSER, MEDIUM, GREATER, LORD. Blank posts every upgrade. |
| `tensuraHarvestFestivalEnabled` | true |  | Post Harvest Festival entry (the Demon Lord awakening feast) to the world channel. |
| `tensuraPossessionEnabled` | true |  | Post Possession skill takeovers to the world channel. |
| `tensuraNamingEnabled` | true |  | Post player-to-player namings to the milestone channel. |
| `tensuraAwakeningEnabled` | true |  | Post Demon Lord / True Hero awakenings to the milestone channel. |
| `useEmbeds` | true |  | Use rich embeds. When false, posts plain text content instead. |
| `worldColor` | 15,224,141 |  | Embed accent color for world events (decimal RGB, e.g. 0xE84D4D = 15224141). |
| `nationColor` | 3,447,003 |  | Embed accent color for nation events (decimal RGB). |
| `milestoneColor` | 15,844,367 |  | Embed accent color for milestones (decimal RGB). |
| `chatColor` | 9,807,270 |  | Embed accent color for chat relay (decimal RGB). |
| `deathColor` | 2,829,617 |  | Embed accent color for deaths (decimal RGB). |
| `webhookUsername` | "" |  | Optional display name for outbound webhook posts. Blank = Discord uses the webhook's configured name. |
| `webhookAvatarUrl` | "" |  | Optional avatar image URL for outbound webhook posts. Blank = webhook default. |
| `botEnabled` | false |  | Enable the two-way bot (Discord -&gt; MC chat relay). Requires botToken and relayChannelId. |
| `botToken` | "" |  | Discord bot token. KEEP SECRET. The MESSAGE_CONTENT privileged intent must be enabled in the Developer Portal. |
| `relayChannelId` | "" |  | Numeric Discord channel ID whose messages relay into in-game chat. |
| `relayPrefix` | "[Discord] " |  | Prefix shown before relayed Discord messages in MC chat. Include any trailing space you want. |
| `relayUseServerDisplayName` | true |  | Name shown for relayed Discord users. true = server display name (guild nickname, falls back to global name then username); false = global display name (falls back to username). |
| `commandsEnabled` | true |  | Answer read-only commands (e.g. !list, !tps, !uptime, !leaderboard, !nation, !season, !player, !help) typed in the relay channel. Requires the bot. |
| `commandPrefix` | "!" |  | Prefix that marks a relay-channel message as a bot command. |
| `commandLeaderboard` | true |  | Answer !leaderboard [board] [n] (all boards when no board is given). |
| `commandNation` | true |  | Answer !nation &lt;name&gt;. |
| `commandSeason` | true |  | Answer !season. |
| `commandPlayer` | true |  | Answer !player &lt;name&gt;. |
| `leaderboardAllTopN` | 5 |  | Rows per board shown by a bare !leaderboard (all boards). Clamped 1..10. |
| `commandCooldownSeconds` | 3 |  | Minimum seconds between answered relay commands (all commands, all users). 0 = none. |
| `presenceEnabled` | true |  | Update the bot's Discord presence with the live player count. Requires the bot. |
| `presenceUpdateSeconds` | 60 |  | How often (seconds) to refresh the bot presence. Floored at 15s. |
| `presenceTemplate` | "{online}/{max} online" |  | Presence text. {online} and {max} are substituted; shown in Discord as 'Watching &lt;text&gt;'. |
| `debug` | false |  | Log every payload and gateway opcode to the server console. |
