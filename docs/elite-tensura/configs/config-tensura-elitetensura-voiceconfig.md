# `config/tensura/EliteTensura/VoiceConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Voice]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enableGui` | true |  | Show the Voice of the World GUI overlay for skill, title, and event messages. |
| `enableChat` | false |  | Echo Voice messages to the chat window in addition to the overlay. |
| `enableSounds` | true |  | Play sounds when Voice messages appear. |
| `enableNarrator` | false |  | Use the Minecraft narrator to read Voice messages aloud (accessibility). |
| `durationScale` | 1 |  | Global multiplier on every Voice message's display time. 1.0 = default per-type timing; 2.0 = twice as long; 0.5 = half. Clamped to [0.25, 5.0]. |
| `mergeSameTier` | true |  | Merge Voice messages of the same tier + header that arrive close together into one scrolling banner instead of showing them one after another. |
| `mergeWindowMs` | 1,000 |  | Coalescing window in milliseconds. Same-tier messages arriving within this window of the first one merge into a single banner. Note: each Voice message is delayed by up to this long before showing. 0 disables merging. |
| `mergeMaxLines` | 5 |  | Maximum body lines a merged banner cycles through (the ticker scrolls the most recent this-many). The xN count in the header still reflects the full total. |
| `mergeWindowLines` | 2 |  | How many body lines are visible at once in the scrolling viewport. When a banner holds more lines than this, they scroll past one at a time (vertical ticker). |
| `mergeScrollMs` | 800 |  | Scroll speed of the merged ticker, in milliseconds per line. Lower = faster scrolling. |
| `globalSkillAnnouncements` | false |  | Announce skill unlocks to all online players (false = only the player who earned it). |
| `skillAnnouncementBlacklist` | [] (empty) |  | Skill registry IDs that will NOT trigger a Voice announcement when gained (e.g. "elitetensura:meditation", "tensura:sage"). Other Voice events (mastery, evolution, transfer) are unaffected. |
| `announceResistanceSkills` | true |  | Announce RESISTANCE skill unlocks. Only affects the unlock announcement; mastery, evolution, and transfer messages are unaffected. |
| `announceIntrinsicSkills` | true |  | Announce INTRINSIC skill unlocks. |
| `announceCommonSkills` | true |  | Announce COMMON skill unlocks. |
| `announceExtraSkills` | true |  | Announce EXTRA skill unlocks. |
| `announceUniqueSkills` | true |  | Announce UNIQUE skill unlocks. |
| `announceUltimateSkills` | true |  | Announce ULTIMATE skill unlocks. |
| `globalTitleAnnouncements` | false |  | Announce title unlocks to all online players (false = only the player who earned it). |
| `enableMilestones` | true |  | Enable milestone announcements (first skill, kill counts, evolution, etc.). |
| `enableWorldEvents` | true |  | Enable world event announcements (dungeons, monsters, calamities). |
| `debug` | false |  | Log all Voice events to the server console for debugging. |
