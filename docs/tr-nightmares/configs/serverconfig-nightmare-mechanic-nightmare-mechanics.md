# `serverconfig/nightmare/mechanic/nightmare_mechanics.toml`

<small>[TR: Nightmares](../index.md) &rsaquo; [Configs](index.md)</small>

## `[damageCapSettings]`

| Option | Default | Range | Description |
|---|---|---|---|
| `UniversalDamageCap` | 20,000 |  | Maximum damage any entity can receive at once. Set to 0 to disable. |

## `[godOwnerAmount]`

| Option | Default | Range | Description |
|---|---|---|---|
| `GodOwnerAmount` | 1 | 0 to no limit | How many people may own the same God-Class Ultimate at once. Set to 0 to disable ownership slots. |

## `[godSkillsOwned]`

| Option | Default | Range | Description |
|---|---|---|---|
| `GodSkillsOwned` | 1 | 0 to no limit | How many God-Class skills a player may own at once. Set to 0 to disable the slot limit. |

## `[demonicSkillsConfig]`

| Option | Default | Range | Description |
|---|---|---|---|
| `DemonicSkillsList` | "tensura:pride", "tensura:wrath", "tensura:gluttony", "tensura:sloth", "tensura:lust", "tensura:greed", "tensura:envy", "tensura:reaper", "tensura:thrower", "trnightmare:fallen_one" |  | List of Demonic skills registry names that can be created via Demon Essence consumption. Format: modid:skill_name |

## `[angelicSkillsConfig]`

| Option | Default | Range | Description |
|---|---|---|---|
| `AngelicSkillsList` | "trnightmare:inversion", "trnightmare:rigor", "tensura:murderer", "tensura:infinity_prison", "tensura:great_sage", "tensura:degenerate", "tensura:unyielding", "trnightmare:stasis" |  | List of Angelic skills registry names that can be created via Holy Essence consumption. Format: modid:skill_name |

## `[demonicUltconfig]`

| Option | Default | Range | Description |
|---|---|---|---|
| `AngelicSkillsList` | "trnightmare:lucifer", "trnightmare:asmodeus", "trnightmare:mammon", "trnightmare:leviathan", "trnightmare:bael" |  | List of Angelic skills registry names that can be created via Holy Essence consumption. Format: modid:skill_name |

## `[virtueSkillsConfig]`

| Option | Default | Range | Description |
|---|---|---|---|
| `VirtueSkillsList` | "tensura:great_sage", "tensura:murderer", "tensura:infinity_prison", "trnightmare:stasis", "trnightmare:cadence", "tensura:degenerate", "tensura:unyielding" |  | Virtue unique skill ids for Michael Ultimate Dominion. |

## `[globalSkillsBlacklist]`

| Option | Default | Range | Description |
|---|---|---|---|
| `globalSkillsBlacklist` | "trnightmare:lore_hunter", "trnightmare:dominator", "trnightmare:michael", "trnightmare:alternative", "trnightmare:sariel" |  | List of Skill registry names that cannot be copied. Format: modid:skill_name |
