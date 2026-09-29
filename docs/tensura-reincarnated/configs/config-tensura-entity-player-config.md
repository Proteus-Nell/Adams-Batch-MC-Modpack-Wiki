# `config/tensura/entity/player_config.toml`

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Configs](index.md)</small>

## `[ResetScroll]`

| Option | Default | Range | Description |
|---|---|---|---|
| `raceCounter` | true |  | Whether Reset Counter should require Final Evolution of the player's race. |
| `awakenCounter` | true |  | Whether Reset Counter should require Awakening (True Hero/Demon Lord). |
| `bossesCounter` | "tensura:orc_disaster", "tensura:ifrit", "tensura:charybdis", "tensura:elemental_colossus", "tensura:hinata_sakaguchi", "tensura:gazel_dwargo" |  | The list of bosses required for Reset Counter. |
| `maxCounterBonus` | 1,024 |  | The maximum number of bonus Unique Skills that resetCounterBonusUnique gamerule can give to a player. |
| `counterPenaltyNonCharScroll` | false |  | Apply the reset counter Penalty when a player uses a Race/Skill Reset Scroll even when they meet all of their reset requirements<br>Only applies when the resetIncompletePenalty gamerule is higher than 1. |
| `resetScrolls` | "tensura:race_reset_scroll", "tensura:skill_reset_scroll", "tensura:character_reset_scroll" |  | List of Reset Scroll that can be used. |

## `[Naming]`

| Option | Default | Range | Description |
|---|---|---|---|
| `lowHPToName` | 25 |  | The percentage of max Health that the target need to be under to submit to the namer |
| `maximumEPToName` | 1 |  | The percentage of EP of the namer that the target needs to be under to submit to the namer |
| `subdueGain` | 0.5 |  | The multiplier of EP that the target will gain from the Subdue option. |
| `evolveGain` | 1.5 |  | The multiplier of EP that the target will gain from the Evolve option. |
| `endowGain` | 9 |  | The multiplier of EP that the target will gain from the Endow option. |
| `maxEPGain` | 1,000,000 |  | The maximum amount of EP that an entity can gain from being named. |
| `subdueLostChance` | 0 |  | The percentage chance that the namer will lose maximum Magicule when choosing the Subdue option. |
| `evolveLostChance` | 20 |  | The percentage chance that the namer will lose maximum Magicule when choosing the Evolve option. |
| `endowLostChance` | 50 |  | The percentage chance that the namer will lose maximum Magicule when choosing the Endow option. |
| `maxCost` | 3,000,000 |  | The maximum amount of Magicule that the namer can lose from naming a target. |
| `randomNames` | "Subordinate", "Pet", "MinhEragon", "Arthur", "Chris", "Nightishaman", "Gen", "Burack", "JustSomebody", "Noii", "Stewy", "Leo", "Onyx", "Nie", "Hunter", "Gold", "Alex", "Steve", "Viciel", "Sen" ... (69 total) |  | Random names for Subordinate Naming. |

## `[Reputation]`

| Option | Default | Range | Description |
|---|---|---|---|
| `maxReputation` | 100 |  | The maximum amount of reputation the player can get from dwarves. |
| `minReputation` | -100 |  | The minimum amount of reputation the player can get from dwarves. |
| `sellingTradePoint` | 0.01 |  | How much reputation that the player gains after each selling trade with a dwarf (selling items for coins). |
| `buyingTradePoint` | 0.05 |  | How much reputation that the player gains after each buying trade with a dwarf (buying items with coins). |
| `levelTradePoint` | 0.1 |  | How much reputation that the player gains after increasing a dwarf's trader level. |
| `saveHelpPoint` | 1 |  | How much reputation that the player gains after saving a dwarf from a monster targeting them. |
| `hurtLostPoint` | 0.1 |  | How much reputation that the player loses after hitting a dwarf while having witnesses. |
| `killLostPoint` | 1 |  | How much reputation that the player loses after killing a dwarf while having witnesses. |
| `discountPercentage` | 0.005 |  | The price percentage of trade that the player get discounted for each positive reputation point. |
| `chargePercentage` | 0.02 |  | The price percentage of trade that the player get charged more for each negative reputation point. |
| `hostileReputation` | -50 |  | The amount of negative reputation that the player needs to reach for the dwarves to stop trading and guards to attack. |
