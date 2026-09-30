# Gourmet

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Gourmet](../../../assets/icons/tensura/skill/gourmet.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:gourmet` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 50,000 |
| **Cooldowns (s)** | 1 mastered, 5 otherwise |
| **Activation** | Press, Hold |

</div>

> Absorb your enemies, gain new powers, and break down anything that stands in your way.

## Modes

| # | Mode |
|---|---|
| 1 | Predation |
| 2 | Corrosion |
| 3 | Stomach |
| 4 | Receive |
| 5 | Provide |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Corrosion | 200 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.5 | multiply total |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can use Food Chain.
- Listed in the `resistanceAllowedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer resistance skills through Food Chain.
- Listed in the `extraAllowedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer extra skills through Food Chain.
- Listed in the `commonAllowdIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer common skills through Food Chain.
- Listed in the `intrinsicAllowedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer intrinsic skills through Food Chain.
- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.

## Related

- **Effects:** [Corrosion](../../effects/corrosion.md)
- **Summons / entities:** Gourmet Mist, Tensura
- **Referenced by:** [Food Chain](../../../tr-nightmares/abilities/extra-skills/food-chain.md), [｢ Beelzebub, Lord of Gourmet ｣](../../../tr-nightmares/abilities/ultimate-skills/beelzebub.md), [Ouroboros, Lord of Eternity](../../../elite-tensura/abilities/ultimate-skills/ouroboros.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Gourmet.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Gourmet.magiculeCostCorrosion` | 200 | Magicule Cost to activate Corrosion. |
| `Gourmet.predationRange` | 3 | The range in block of the Predation Mode. |
| `Gourmet.predationDamage` | 25 | The attack damage of the Predation Mode. |
| `Gourmet.predationCooldown` | 5 | The cooldown in second of the Predation Mode. |
| `Gourmet.predationCooldownMastered` | 1 | The cooldown in second of the Predation Mode when mastered. |
| `Gourmet.corrosionSpeedMultiplier` | 0.5 | Activation Speed Multiplier when activating the Corrosion Mode. |
| `Gourmet.corrosionRadius` | 5 | The radius in block of the Corrosion Mode. |
| `Gourmet.corrosionDamage` | 5 | The amount of damage dealt onto targets every 10 tick using the Corrosion Mode. |
| `Gourmet.corrosionEPSteal` | 0.3 | The EP multiplier of targets killed by the Corrosion Mode to be added to the user's Each of Aura and Magicule. |
| `Gourmet.waterCapacity` | 6,000 | The bonus water capacity when the skill is acquired. |
| `Gourmet.lavaCapacity` | 6,000 | The bonus lava capacity when the skill is acquired. |

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
