# Starved

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Starved](../../../assets/icons/tensura/skill/starved.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:starved` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 50,000 |
| **Activation** | Press, Hold |

</div>

> Consume all in your path or have your rampaging subordinates do it. Corrode your enemies, devour their strength, and adding their abilities to your own.

## Modes

| # | Mode |
|---|---|
| 1 | Corrosion |
| 2 | Stomach |
| 3 | Receive |
| 4 | Provide |
| 5 | Spiritual Domination |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Stomach | 200 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers on melee contact
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.5 | multiply total |

## Obtaining

- Intrinsic skill of: [Orc Lord](../../races/orc-lord.md), [Orc Disaster](../../races/orc-disaster.md)
- Innate to mobs: [Orc Disaster](../../mobs/orc-disaster.md), [Orc Lord](../../mobs/orc-lord.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can use Food Chain.
- Listed in the `resistanceAllowedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer resistance skills through Food Chain.
- Listed in the `commonAllowdIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer common skills through Food Chain.
- Listed in the `intrinsicAllowedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer intrinsic skills through Food Chain.
- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.

## Related

- **Related skills:** [Gluttony](gluttony.md), [Predator](predator.md)
- **Effects:** [Corrosion](../../effects/corrosion.md), [Rampage](../../effects/rampage.md)
- **Summons / entities:** Tensura
- **Referenced by:** [Gluttony](gluttony.md), [Predator](predator.md), [Food Chain](../../../tr-nightmares/abilities/extra-skills/food-chain.md), [｢ Tenebrosum, God of Souls ｣](../../../tr-nightmares/abilities/ultimate-skills/tenebrosum.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Starved.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Starved.magiculeCostCorrosion` | 200 | Magicule Cost to activate Corrosion. |
| `Starved.corrosionDuration` | 200 | The duration in tick of the Corrosion effect when attacking targets. |
| `Starved.corrosionLevel` | 2 | The level of the Corrosion effect when attacking targets. |
| `Starved.corrosionSpeedMultiplier` | 0.5 | Activation Speed Multiplier when activating the Corrosion Mode. |
| `Starved.corrosionRadius` | 5 | The radius in block of the Corrosion Mode. |
| `Starved.corrosionDamage` | 5 | The amount of damage dealt onto targets every 10 tick using the Corrosion Mode. |
| `Starved.corrosionEPSteal` | 0.2 | The EP multiplier of targets killed by the Corrosion Mode to be added to the user's Each of Aura and Magicule. |
| `Starved.dominationRadius` | 15 | The radius of the Spiritual Domination mode. |
| `Starved.waterCapacity` | 3,000 | The bonus water capacity when the skill is acquired. |
| `Starved.lavaCapacity` | 3,000 | The bonus lava capacity when the skill is acquired. |

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

`tensura:skills/gluttony`, `tensura:skills/unique_skills`
