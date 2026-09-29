# Envy

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Envy](../../../assets/icons/tensura/skill/envy.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:envy` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 100,000 |
| **Max mastery** | 1,500 |
| **Cooldowns (s)** | 10 mastered, 30 otherwise |
| **Activation** | Toggle, Press, Hold |

</div>

> Absorb strength from enemies, buff yourself and debilitate your enemies.

## Modes

| # | Mode |
|---|---|
| 1 | Absorb |
| 2 | Strength Sap |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 or 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when an effect is applied to you

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| melee | 10 | add |
| projectile | 10 | add |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `DemonicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Demonic skills registry names that can be created via Demon Essence consumption. Format: modid:skill_name

## Related

- **Effects:** [Insanity](../../effects/insanity.md)
- **Summons / entities:** Tensura
- **Referenced by:** [｢ Gabriel, Lord of Patience ｣](../../../tr-nightmares/abilities/ultimate-skills/gabriel.md), [｢ Leviathan, Lord of Envy ｣](../../../tr-nightmares/abilities/ultimate-skills/leviathan.md), [｢ Michael, Lord of Justice ｣](../../../tr-nightmares/abilities/ultimate-skills/michael.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Envy.mpAcquirement` | 100,000 | Magicule Acquirement Cost. |
| `Envy.magiculeCostSap` | 1,000 | Magicule Cost to activate Strength Sap. |
| `Envy.luckLevel` | 3 | The level of the Luck effect when toggled. |
| `Envy.meleeDodge` | 10 | Melee Dodge Chance when toggled. |
| `Envy.projectileDodge` | 10 | Projectile Dodge Chance when toggled. |
| `Envy.insanityChance` | 20 | The chance for the user to be applied with Insanity when using Strength Sap every 10 second. |
| `Envy.insanityLevel` | 1 | The increasing level of the Insanity effect when the user is applied by Strength Sap. |
| `Envy.insanityDuration` | 240 | The duration in tick of the Insanity effect when the user is applied by Strength Sap. |
| `Envy.sapRadius` | 15 | The radius in block of the Strength Sap effect. |
| `Envy.sapEP` | 0.6 | The multiplier of EP that an entity needs to have below to be affected by the Strength Sap. |
| `Envy.sapEPMastered` | 0.8 | The multiplier of EP that an entity needs to have below to be affected by the Strength Sap when mastered. |
| `Envy.epDifferenceMultiplier` | 0.1 | The EP difference multiplier for each Slowness/Weakness Level. |
| `Envy.sapDuration` | 200 | The duration in tick of the Slowness/Weakness effect when targets are applied by Strength Sap. |
| `Envy.epDrain` | 0.001 | The multiplier of EP that the user drains from targets each second. |

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

`tensura:skills/envy`, `tensura:skills/sin_skills`, `tensura:skills/unique_skills`
