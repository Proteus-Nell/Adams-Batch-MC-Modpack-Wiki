# `config/nightmare/ability/skill/ego/general_config.toml`

<small>[TR: Nightmares](../index.md) &rsaquo; [Configs](index.md)</small>

## `[General]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enableWhitelist` | true |  | Whether it uses a blacklist or whitelist, true means whitelist, false means blacklist |
| `maxEgos` | 3 |  | Maximum number of egos a person may have |
| `nameCostMultiplier` | 2 |  | Multiplier for mp cost to named (twice the skill's obtainment cost by default) |
| `masteryPercentage` | 0.3 |  | Percentage of mastery to have a chance at Ego (Default: 30%) |
| `egoChance` | 0.02 |  | Chance of obtaining ego after meeting requirements (Default: 10%) |
| `egoBlacklist` | [] (empty) |  | Skills blacklisted from developing egos if in blacklist mode |
| `egoWhitelist` | "tensura:pride", "tensura:gluttony", "tensura:sloth", "tensura:envy", "tensura:greed", "tensura:lust", "tensura:wrath", "tensura:great_sage", "tensura:infinity_prison", "tensura:unyielding", "trnightmare:cadence", "trnightmare:saint", "trnightmare:endorse", "trnightmare:dominator", "trnightmare:astral_light" |  | Skills allowed to develop ego if in whitelist mode |
