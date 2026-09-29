# Food Chain

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:food_chain` |
| **Activation** | Press |

</div>

> Transfer skills between you and your subordinates, or teach a subordinate one of your skills.

## How it works

- Activated by pressing the skill key
- Does something when first learned

## Obtaining

- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.
- Acquisition checks: [Gourmet](../../../tensura-reincarnated/abilities/unique-skills/gourmet.md), [Gluttony](../../../tensura-reincarnated/abilities/unique-skills/gluttony.md), [Starved](../../../tensura-reincarnated/abilities/unique-skills/starved.md)

## Related

- **Related skills:** [Gluttony](../../../tensura-reincarnated/abilities/unique-skills/gluttony.md), [Starved](../../../tensura-reincarnated/abilities/unique-skills/starved.md), [Gourmet](../../../tensura-reincarnated/abilities/unique-skills/gourmet.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `FoodChain.allowedSkillIds` | "tensura:starved", "tensura:gourmet", "tensura:gluttony", "trnightmare:beelzebub", "trnightmare:beelzebuth" | Skill ids that can use Food Chain. |
| `FoodChain.resistanceAllowedIds` | "tensura:starved", "tensura:gourmet", "tensura:gluttony", "trnightmare:beelzebub", "trnightmare:beelzebuth" | Skill ids that can transfer resistance skills through Food Chain. |
| `FoodChain.extraAllowedIds` | "tensura:gourmet", "tensura:gluttony", "trnightmare:beelzebub", "trnightmare:beelzebuth" | Skill ids that can transfer extra skills through Food Chain. |
| `FoodChain.commonAllowdIds` | "tensura:starved", "tensura:gourmet", "tensura:gluttony", "trnightmare:beelzebub", "trnightmare:beelzebuth" | Skill ids that can transfer common skills through Food Chain. |
| `FoodChain.intrinsicAllowedIds` | "tensura:starved", "tensura:gourmet", "tensura:gluttony", "trnightmare:beelzebub", "trnightmare:beelzebuth" | Skill ids that can transfer intrinsic skills through Food Chain. |
| `FoodChain.uniqueAllowedIds` | [] (empty) | Skill ids that can transfer unique skills through Food Chain. |
| `FoodChain.ultimateAllowedIds` | [] (empty) | Skill ids that can transfer ultimate skills through Food Chain. |
| `FoodChain.blacklistedIds` | "tensura:starved", "tensura:gourmet", "tensura:gluttony", "trnightmare:beelzebub", "trnightmare:beelzebuth", "trnightmare:witches_envy", "trnightmare:time_traveler", "trnightmare:yog_sothoth", "trnightmare:yog-sotohort", "trnightmare:conceptual_existence", "trnightmare:manas_host", "trnightmare:rebirth", "trnightmare:mimicry", "trnightmare:food_chain", "trnightmare:ultimate_arroganz", "trnightmare:skill_storage", "nightmareutils:sentient", "trnightmare:alteration", "nightmareutils:sentientdisintegrate", "nightmareutils:charm_test" ... (28 total) | Skill ids that are banned from being transferred through Food Chain. |

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Beelzebuth.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Beelzebuth.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Beelzebuth.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Beelzebuth.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Beelzebuth.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Beelzebuth.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Beelzebuth.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Beelzebuth.mpAcquirement` | 1,500,000 | Magicule cost required to acquire Beelzebuth. |
| `Beelzebuth.costSoulDevour` | 25,000 | Magicule cost of Soul Devour. |
| `Beelzebuth.costPredation` | 8,000 | Magicule cost of Predation. |
| `Beelzebuth.predationRange` | 15 | Base Predation range. |
| `Beelzebuth.predationRangeMastered` | 30 | Predation range when mastered. |
| `Beelzebuth.predationDamage` | 150 | Predation damage per tick. |
| `Beelzebuth.predationEPDrain` | 25 | EP drained per tick of Beelzebuth's predation. |
| `Beelzebuth.predationSkillChance` | 30 | Chance (%) to steal a random skill on hit. |
| `Beelzebuth.predationSkillNumber` | 3 | Maximum number of random skills stolen when predation triggers. |
| `Beelzebuth.predationCorrosionDuration` | 300 | Duration (ticks) of Corrosion applied by Predation. |
| `Beelzebuth.predationCorrosionLevel` | 1 | Level of Corrosion applied by Predation. |
| `Beelzebuth.predationEPSteal` | 1 | EP steal multiplier applied on kill. |
| `Beelzebuth.costGluttonousDarkness` | 24,000 | Magicule cost of Gluttonous Darkness. |
| `Beelzebuth.darknessRadius` | 12 | Darkness radius. |
| `Beelzebuth.darknessRadiusMastered` | 18 | Darkness radius when mastered. |
| `Beelzebuth.darknessPullStrength` | 1 | Pull strength of Gluttonous Darkness. |
| `Beelzebuth.darknessDamage` | 50 | Physical damage of Gluttonous Darkness. |
| `Beelzebuth.darknessSpiritualDamage` | 20 | Spiritual damage of Gluttonous Darkness. |
| `Beelzebuth.darknessMaxSoulDamage` | 200 | Maximum soul damage scaling. |
| `Beelzebuth.costImaginarySpace` | 500 | Magicule cost of Imaginary Space. |
| `Beelzebuth.costMimicry` | 0 | Magicule cost of Mimicry. |
| `Beelzebuth.costCorrosion` | 500 | Magicule cost of Corrosion. |
| `Beelzebuth.corrosionRadius` | 12 | Corrosion radius. |
| `Beelzebuth.corrosionDamage` | 50 | Corrosion damage per tick. |
| `Beelzebuth.corrosionEPSteal` | 1 | EP steal multiplier for Corrosion. |
| `Beelzebuth.costSoulSteal` | 50,000 | Magicule cost of Soul Steal. |
| `Beelzebuth.costFoodChain` | 15,000 | Magicule cost of Food Chain. |
| `Beelzebuth.foodChainEnabled` | true | Food Chain (mode 7): master switch. |
| `Beelzebuth.foodChainAllowLearnFromSubordinate` | true | Food Chain: when not sneaking, open menu to learn a skill FROM a lined-up Subordinate. |
| `Beelzebuth.foodChainAllowTeach` | true | Food Chain: when sneaking, open menu to TEACH one of your skills TO a lined-up Subordinate. |
| `Beelzebuth.foodChainCommon` | true | Food Chain transfers: COMMON skills allowed. |
| `Beelzebuth.foodChainExtra` | true | Food Chain transfers: EXTRA skills allowed. |
| `Beelzebuth.foodChainIntrinsic` | true | Food Chain transfers: INTRINSIC skills allowed. |
| `Beelzebuth.foodChainResistance` | true | Food Chain transfers: RESISTANCE skills allowed. |
| `Beelzebuth.foodChainUnique` | false | Food Chain transfers: UNIQUE skills allowed on Beelzebuth baseline (also see raphaelBonusUnique). |
| `Beelzebuth.foodChainUltimate` | false | Food Chain transfers: ULTIMATE skills allowed on Beelzebuth baseline (also see raphaelBonusUltimate). |
| `Beelzebuth.raphaelBonusUnique` | false | If true and you fully know Raphael Wisdom (trnightmare), UNIQUE is allowed without foodChainUnique. |
| `Beelzebuth.raphaelBonusUltimate` | false | If true and you fully know Raphael Wisdom, ULTIMATE is allowed without foodChainUltimate. |
| `Beelzebuth.foodChainRange` | 8 | Food Chain targeting range. |
| `Beelzebuth.foodChainCooldownSeconds` | 5 | Cooldown (Seconds) on Beelzebuth mode 7 after a successful transfer. |
| `Beelzebuth.foodChainAllowTemporarySubordinates` | false | Food Chain: if true, temporary/summoner-only links count (IExistence temporaryOwner/summoner path in SubordinateHelper). If false, only permanent ownership (getPermanentOwner chain or ISubordinate owner) may connect you to the target. |
| `Beelzebuth.beelzebuthMobKills` | 1,500 | Mob kills required to evolve Gluttony into Beelzebuth. |
| `Beelzebuth.beelzebuthCakeSlices` | 10 | Cake slices eaten required to evolve Gluttony into Beelzebuth. |
| `Beelzebuth.beelzebuthMP` | 1,750,000 | Magicules required to evolve Gluttony into Beelzebuth. |
| `Beelzebuth.beelzebuthHPThreshold` | 0.5 | HP percentage threshold for evolution (0.50 = 50%). |
| `Beelzebuth.enableUltimateEvolution` | true | Whether Beelzebuth evolution is allowed. |

## Tags

`tensura:skills/no_plundering`
