# ｢ Mammon, Lord of Greed ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Mammon, Lord of Greed ｣](../../../assets/icons/trnightmare/skill/mammon.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:mammon` |
| **Modes** | 6 |
| **Acquisition cost (MP)** | 1,250,000 |
| **Max mastery** | 15,000 |
| **Cooldowns (s)** | 1,200 |
| **Activation** | Toggle, Press, Hold |

</div>

> Mammon, Lord of Greed is the ultimate evolved Skill of Greed. This powerful skill is capable of stealing even the Life from its victims. This is truly the manifestation of Greed

## Modes

| # | Mode |
|---|---|
| 1 | Control Heart |
| 2 | Feed Desire |
| 3 | Desire Manifestation |
| 4 | Mammon Flare |
| 5 | Death Wish |
| 6 | Skill Steal |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you die

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| atk | bonus | add |
| arm | bonus | add |
| atk | boost | add |
| barrier | max HP × 2 | add |

## Obtaining

- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Listed in the `AngelicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Angelic skills registry names that can be created via Holy Essence consumption. Format: modid:skill_name
- Acquisition checks: [Greed](../../../tensura-reincarnated/abilities/unique-skills/greed.md), [｢ Mammon, Lord of Greed ｣](mammon.md)
- In-game message: *You're filled with an overwhelming Desire.... Your Greed has evolved into the Ultimate Skill: Mammon*

## Related

- **Related skills:** [Greed](../../../tensura-reincarnated/abilities/unique-skills/greed.md), [Burden](../../../tensura-reincarnated/abilities/aspectual-magic/burden.md), [Curse](../../../tensura-reincarnated/abilities/spiritual-magic/curse.md), [｢ Astral Light, Lord of Creation ｣](astral-light.md), [｢ Akashic Records, God of Origin ｣](akashic-records.md)
- **Effects:** [Mind Control](../../../tensura-reincarnated/effects/mind-control.md), [Movement Interference](../../../tensura-reincarnated/effects/movement-interference.md), [Fragility](../../../tensura-reincarnated/effects/fragility.md), [Fatal Poison](../../../tensura-reincarnated/effects/fatal-poison.md), [Paralysis](../../../tensura-reincarnated/effects/paralysis.md), [Petrification](../../../tensura-reincarnated/effects/petrification.md), [Hypnosis](../../../tensura-reincarnated/effects/hypnosis.md), [Anti-Skill](../../../tensura-reincarnated/effects/anti-skill.md)
- **Items:** [Magic Ore](../../../tensura-reincarnated/items/materials/magic-ore-shard.md)
- **Referenced by:** [Divine Wisdom Core](../intrinsic-skills/divine-wisdom-core.md), [Greedy Manas](greedy-manas.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Mammon.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Mammon.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Mammon.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Mammon.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Mammon.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Mammon.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Mammon.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Mammon.mpAcquirement` | 1,250,000 | The Cost for the Ultimate Skill: Mammon. |
| `Mammon.magiculeCostControlHeart` | 5,000 | Magicule cost of Control Heart. |
| `Mammon.magiculeCostFeedDesire` | 100 | Magicule cost of Feed Desire. |
| `Mammon.magiculeCostManifestation` | 2,500 | Magicule cost of Manifestation. |
| `Mammon.magiculeCostFlare` | 25,000 | Magicule cost of Mammon Flare. |
| `Mammon.magiculeCostDeathWish` | 100,000 | Magicule cost of Death Wish. |
| `Mammon.magiculeCostSkillSteal` | 1,850,000 | Magicule cost of Skill Steal. |
| `Mammon.flareCooldown` | 20 | Cooldown of Mammon Flare in seconds. |
| `Mammon.flareCooldownMastered` | 10 | Cooldown of Mammon Flare in seconds when mastered. |
| `Mammon.skillStealCooldown` | 1,200 | Cooldown of Skill Steal (in ticks). |
| `Mammon.absorbLifeBarrierSteal` | 1 | Amount of Barrier Points stolen per hit by Absorb Life. |
| `Mammon.skillStealAnalysisTime` | 12,000 | Time (in ticks) required to analyze a stolen skill. |
| `Mammon.desireCostCommon` | 5 | Desire cost to steal a Common skill. |
| `Mammon.desireCostExtra` | 40 | Desire cost to steal an Extra skill. |
| `Mammon.desireCostIntrinsic` | 15 | Desire cost to steal an Intrinsic skill. |
| `Mammon.desireCostResistance` | 30 | Desire cost to steal a Resistance skill. |
| `Mammon.desireCostUnique` | 5,000 | Desire cost to steal a Unique skill. |
| `Mammon.desireCostUltimate` | 10,000 | Desire cost to steal an Ultimate skill. |
| `Mammon.mammonVillagerTrades` | 100 | The Villager Trades to gather the Desire for Mammon. |
| `Mammon.mammonRaidVictories` | 10 | The amount of raids to win to collect Desire for Mammon |
| `Mammon.mammonGoldBlocks` | 7 | The Gold Blocks used as material for Greed's Desire to become Mammon. |
| `Mammon.skillTheftBlacklist` | "trnightmare:nodens", "trnightmare:azathoth", "trnightmare:zehirete", "trnightmare:shub_niggurath", "trnightmare:cthulhu", "trnightmare:cthugha", "trnightmare:nyarlathotep", "trnightmare:true_hero", "trnightmare:astaroth", "trnightmare:surya", "trnightmare:hamiel", "trnightmare:abaddon", "trnightmare:belial", "trnightmare:samael", "trnightmare:deal_maker", "trnightmare:carnation", "trnightmare:designer", "trnightmare:tempter", "tensura:gourmet", "tensura:guardian" ... (52 total) | Skill IDs that Mammon cannot copy or steal. |
| `Mammon.mammonMP` | 1,250,000 | Magicules required to evolve Greed into Mammon. |
| `Mammon.enableUltimateEvolution` | true | Whether Mammon evolution is allowed. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## In-game messages

<details markdown><summary>Show 10 messages</summary>

- Desire Points: %s
- Mammon has temporarily stolen %s!
- Mammon has permanently copied %s!
- Analyzing stolen skill: %s (%s seconds)
- Skill Theft is analyzing: %s. Shift-use to cancel.
- Cancelled Skill Theft for %s. Desire Points were not refunded.
- There is no active Skill Theft to cancel.
- Mammon started copying your %s. Kill the user before analysis finishes to prevent it.
- Skill analysis complete: %s
- Skill analysis failed. Desire Points were spent.

</details>

## Tags

`tensura:skills/ultimate_skills`
