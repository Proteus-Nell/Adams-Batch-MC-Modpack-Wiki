# `serverconfig/nightmare/mechanic/UltimateSlotConfig.toml`

<small>[TR: Nightmares](../index.md) &rsaquo; [Configs](index.md)</small>

## `[ultimateSlotSettings]`

| Option | Default | Range | Description |
|---|---|---|---|
| `DefaultUltimateSlot` | 1 | 0 to no limit | Default amount of ultimate slots each player starts with. |
| `UltimateSlotRandomizer` | false |  | If true, the initial slot count is randomized instead of the default value. |
| `UltimateSlotRandomizerMaxValue` | 4 | 1 to no limit | Maximum value for randomized initial ultimate slots. |
| `UltimateSlotResetGain` | true |  | If true, reset counters can grant additional ultimate slots. |
| `UltimateSlotResetEarn` | 1 | 0 to no limit | How many ultimate slots are granted by each reset counter reward. |
| `UltimateSlotResetMaxEarned` | 4 | 0 to no limit | Maximum ultimate slots that can be earned through reset counters. |
| `UltimateSlotResetEarnRate` | 1 | 1 to no limit | How many reset counters are needed before an extra slot reward is granted. |
| `EnableUltimateSlotRewards` | true |  | If true, bosses can grant additional ultimate slots on defeat. |
| `UltimateSlotRewardChance` | 0.25 | 0 to 1 | Chance for a boss reward to grant an additional ultimate slot. |
| `UltimateSlotRewardBosses` | "trnightmare:sentient_boss_veldora", "trnightmare:sentient_boss_velgrynd", "trnightmare:sentient_boss_velzard", "trnightmare:sentient_boss_yuuki_desire", "trnightmare:sentient_boss_milim_wrath", "trnightmare:sentient_boss_primordial_daemon", "trnightmare:sentient_boss_masayuuki" |  | Boss entity IDs that can grant an extra ultimate slot. |
| `EnableSelfNamingSlot` | true |  | If true, completing self-naming grants an extra ultimate slot. |
| `SelfNamingSlotAmount` | 1 | 0 to no limit | How many ultimate slots self-naming grants. |
| `EnableAwakeningSlot` | true |  | If true, awakening grants an extra ultimate slot. |
| `AwakeningSlotAmount` | 1 | 0 to no limit | How many ultimate slots awakening grants. |
