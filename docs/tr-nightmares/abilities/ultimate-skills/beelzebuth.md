# ｢ Beelzebuth, Lord of Gluttony ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Beelzebuth, Lord of Gluttony ｣](../../../assets/icons/trnightmare/skill/beelzebuth.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:beelzebuth` |
| **Modes** | 9 |
| **Max mastery** | 15,000 |
| **Activation** | Press, Hold |

</div>

> Beelzebuth, Lord of Gluttony is the ultimate evolved Skill of Gluttony. Devour all in your path

## Modes

| # | Mode |
|---|---|
| 1 | Soul Devour |
| 2 | Predation |
| 3 | Gluttonous Darkness |
| 4 | Imaginary Space |
| 5 | Mimicry |
| 6 | Corrosion |
| 7 | Soul Steal |
| 8 | Food Chain |
| 9 | Imaginary Space: Isolation |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Does something when first learned

## Obtaining

- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can use Food Chain.
- Listed in the `resistanceAllowedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer resistance skills through Food Chain.
- Listed in the `extraAllowedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer extra skills through Food Chain.
- Listed in the `commonAllowdIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer common skills through Food Chain.
- Listed in the `intrinsicAllowedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer intrinsic skills through Food Chain.
- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can be affected by Raphael-style alteration by default.
- Acquisition checks: [Gluttony](../../../tensura-reincarnated/abilities/unique-skills/gluttony.md), [Merciless](../../../tensura-reincarnated/abilities/unique-skills/merciless.md), [｢ Beelzebuth, Lord of Gluttony ｣](beelzebuth.md)
- In-game message: *Your Unique Skill Gluttony is full, yet your Hunger is not yet sated... Attempting Evolution of the Unique Skill: Gluttony... The Unique Skill: Gluttony has evolved into the Ultimate Skill: Beelzebuth by consuming the Unique Skill: Merciless.*

## Related

- **Related skills:** [Gluttony](../../../tensura-reincarnated/abilities/unique-skills/gluttony.md), [Merciless](../../../tensura-reincarnated/abilities/unique-skills/merciless.md)
- **Effects:** [Soul Drain](../../../tensura-reincarnated/effects/soul-drain.md), [Corrosion](../../../tensura-reincarnated/effects/corrosion.md), [Fear](../../../tensura-reincarnated/effects/fear.md)
- **Summons / entities:** Beelzebuth Mist, Beelzebuth Black Hole
- **Referenced by:** [Mimicry](../extra-skills/mimicry.md), [Universal Shapeshift](../extra-skills/universal-shapeshift.md), [Alteration](../extra-skills/alteration.md), [｢ Azathoth, God of The Void ｣](azathoth.md), [Gluttony Manas](gluttony-manas.md)

## Stats (config defaults)

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

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

Set in [`config/tensura/energy_config.toml`](../../../tensura-reincarnated/configs/config-tensura-energy-config.md).

| Option | Default | Description |
|---|---|---|
| `maximumEPSteal` | 1,000,000 | The maximum amount of EP that an EP stealing ability can take. |
| `minAura` | 10 | The Minimum amount of Aura an entity can have. |
| `maxAura` | 1,000,000,000 | The Maximum amount of Aura an entity can have. |
| `baseAuraGain` | 1 | The Base percentage of Aura an entity can gain from slain enemies' EP. |
| `maxAuraGain` | 10 | The Max percentage of Aura an entity can gain from slain enemies' EP. |
| `minMagicule` | 10 | The Minimum amount of Magicule an entity can have. |
| `maxMagicule` | 1,000,000,000 | The Maximum amount of Magicule an entity can have. |
| `baseMagiculeGain` | 1 | The Base percentage of Magicule an entity can gain from slain enemies' EP. |
| `maxMagiculeGain` | 10 | The Max percentage of Magicule an entity can gain from slain enemies' EP. |
| `baseAuraRegen` | 5 | The base amount of Aura that entities regenerate each 10 ticks (half a second). |
| `areaMagiculeRegen` | 0.01 | The percentage of the current chunk's Magicule gets turned into players' MP within the chunk each 10 ticks (half a second). |
| `minimumMagiculePoison` | 1,000 | The minimum amount of Magicule the current chunk needs to have to apply Magicule Poison on players if applicable. |
| `sleepModeTick` | 180 | The number of seconds will the entity be in sleep mode when Magicule reaches 0. |
| `sleepModeAura` | 0.003 | The bonus multiplier of Max Aura that the entity regenerates each 10 ticks during Sleep Mode. |
| `sleepModeMagicule` | 0.003 | The bonus multiplier of Max Magicule that the entity regenerates each 10 ticks during Sleep Mode. |
| `wakeUpAura` | 0.16 | The multiplier of Max Aura that the entity regenerates after waking up naturally. |
| `wakeUpMagicule` | 0.16 | The multiplier of Max Magicule that the entity regenerates after waking up naturally. |
| `spiritualMagiculeLost` | 115 | Amount of Magicule that an entity in Spiritual Form loses each 10 ticks (half a second) while in unsuitable area. |
| `exceedMaxLost` | 5 | Amount of Aura/Magicule that an entity loses each 10 ticks when exceeding the max Aura/Magicule. |
| `auraMultiplierForInsanity` | 0.25 | Multiplier of max aura an entity needs to exceed for each level of Insanity.<br>Example: By default, Aura = 125% Max Aura -&gt; Insanity I, Aura = 150% Max Aura -&gt; Insanity II |
| `magiculeMultiplierForPoison` | 0.25 | Multiplier of max magicule an entity needs to exceed for each level of Magicule Poison.<br>Example: By default, Magicule = 125% Max Magicule -&gt; Poison I, Magicule = 150% Max Magicule -&gt; Poison II |
| `maximumEPSteal` | 1,000,000 | The maximum amount of EP that an EP stealing ability can take. |
| `maxEPReductionPercentage` | 90 | The maximum percentage of EP reduction when used in calculation for EP gain after killing mobs. |
| `penaltyLimitGain` | true | Whether the EP Gain from killing Players limit by the EP death Penalty gamerule. |

## Tags

`tensura:skills/ultimate_skills`
