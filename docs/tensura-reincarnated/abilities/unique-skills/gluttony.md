# Gluttony

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Gluttony](../../../assets/icons/tensura/skill/gluttony.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:gluttony` |
| **Modes** | 7 |
| **Acquisition cost (MP)** | 100,000 |
| **Max mastery** | 1,500 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Press, Hold |

</div>

> Absorb all in your path. None can win. Receive and provide skills, gain access to a spatial storage and mimic entities.

## Modes

| # | Mode |
|---|---|
| 1 | Predation |
| 2 | Stomach |
| 3 | Mimicry |
| 4 | Isolation |
| 5 | Corrosion |
| 6 | Receive |
| 7 | Provide |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Isolation | 200 |  |
| Corrosion | 200 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Adjusted by scrolling while active
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.5 | multiply total |

## Obtaining

- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are allowed to mimic.
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can use Food Chain.
- Listed in the `resistanceAllowedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer resistance skills through Food Chain.
- Listed in the `extraAllowedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer extra skills through Food Chain.
- Listed in the `commonAllowdIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer common skills through Food Chain.
- Listed in the `intrinsicAllowedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer intrinsic skills through Food Chain.
- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.
- Listed in the `DemonicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Demonic skills registry names that can be created via Demon Essence consumption. Format: modid:skill_name
- Acquisition checks: [Starved](starved.md), [Predator](predator.md)

## Related

- **Related skills:** [Starved](starved.md), [Predator](predator.md)
- **Effects:** [Corrosion](../../effects/corrosion.md)
- **Referenced by:** [Predator](predator.md), [Starved](starved.md), [Carnation](../../../tr-nightmares/abilities/unique-skills/carnation.md), [Food Chain](../../../tr-nightmares/abilities/extra-skills/food-chain.md), [Mimicry](../../../tr-nightmares/abilities/extra-skills/mimicry.md), [Universal Shapeshift](../../../tr-nightmares/abilities/extra-skills/universal-shapeshift.md), [Alteration](../../../tr-nightmares/abilities/extra-skills/alteration.md), [｢ Beelzebuth, Lord of Gluttony ｣](../../../tr-nightmares/abilities/ultimate-skills/beelzebuth.md), [｢ Michael, Lord of Justice ｣](../../../tr-nightmares/abilities/ultimate-skills/michael.md), [Beelzebuth, Lord of Gluttony](../../../elite-tensura/abilities/ultimate-skills/beelzebuth.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Gluttony.mpAcquirement` | 100,000 | Magicule Acquirement Cost. |
| `Gluttony.magiculeCostIsolation` | 200 | Magicule Cost to remove each harmful status effect with Isolation. |
| `Gluttony.magiculeCostCorrosion` | 200 | Magicule Cost to activate Corrosion. |
| `Gluttony.predationRange` | 10 | The max range in block of the Predation Mode. |
| `Gluttony.predationRangeMastered` | 15 | The max range in block of the Predation Mode when mastered. |
| `Gluttony.predationDamage` | 50 | The attack damage of the Predation Mode. |
| `Gluttony.predationEPDrain` | 1,000 | The amount of EP that the user drains from target using the Predation Mode. |
| `Gluttony.predationSkillChance` | 30 | The chance to obtain skills from targets without killing them with the Predation Mode. |
| `Gluttony.predationSkillNumber` | 3 | The number of skills to gain from targets at a time without killing them with the Predation Mode. |
| `Gluttony.predationCorrosionDuration` | 100 | The duration in tick of the Corrosion effect applied by the Predation Mode. |
| `Gluttony.predationCorrosionLevel` | 2 | The level of the Corrosion effect applied by the Predation Mode. |
| `Gluttony.predationEPSteal` | 0.5 | The multiplier of the target's EP to be turned into the user's EP when killed with the Predation Mode. |
| `Gluttony.magiculeMultiplier` | 2 | The multiplier of magicule gained from dissolving items with the Isolation Mode. |
| `Gluttony.healthMultiplier` | 2 | The multiplier of health healed from dissolving items with the Isolation Mode.. |
| `Gluttony.isolationCooldown` | 5 | The cooldown in second of the Isolation Mode. |
| `Gluttony.isolationCooldownMastered` | 3 | The cooldown in second of the Isolation Mode when mastered. |
| `Gluttony.corrosionSpeedMultiplier` | 0.5 | Activation Speed Multiplier when activating the Corrosion Mode. |
| `Gluttony.corrosionRadius` | 5 | The radius in block of the Corrosion Mode. |
| `Gluttony.corrosionDamage` | 10 | The amount of damage dealt onto targets every 10 tick using the Corrosion Mode. |
| `Gluttony.corrosionEPSteal` | 0.4 | The EP multiplier of targets killed by the Corrosion Mode to be added to the user's Each of Aura and Magicule. |
| `Gluttony.waterCapacity` | 3,000 | The bonus water capacity when the skill is acquired. |
| `Gluttony.lavaCapacity` | 3,000 | The bonus lava capacity when the skill is acquired. |

Set in [`config/tensura/ability/skill_config.toml`](../../configs/config-tensura-ability-skill-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryUniqueSin` | 1,500 | The max amount of mastery point for Unique Skills of Sins. |
| `Mastery.masteryIntrinsic` | 100 | The max amount of mastery point for Intrinsic Skills. |
| `Mastery.masteryExtra` | 500 | The max amount of mastery point for Extra Skills. |
| `Mastery.masteryUnique` | 1,000 | The max amount of mastery point for Unique Skills. |
| `Mastery.masteryUniqueSin` | 1,500 | The max amount of mastery point for Unique Skills of Sins. |
| `Mastery.masteryUltimate` | 10,000 | The max amount of mastery point for Ultimate Skills. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

Set in [`config/tensura/energy_config.toml`](../../configs/config-tensura-energy-config.md).

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

`tensura:skills/gluttony`, `tensura:skills/sin_skills`, `tensura:skills/unique_skills`
