# Reaper

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Reaper](../../../assets/icons/tensura/skill/reaper.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:reaper` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 60,000 |
| **Cooldowns (s)** | 5 mastered, 10 otherwise, 10 |
| **Activation** | Toggle, Press, Hold |

</div>

> Do recon by becoming smaller and more agile while seeing all enemies nearby. Spawn clones, or consume the essence of your enemies to obliterate them in a single strike.

## Modes

| # | Mode |
|---|---|
| 1 | Attack |
| 2 | Infinite Eater |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Triggers when you die

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| size | -0.5 | add x base |
| sense | 1 | add |
| senseRadius | 20 mastered, 10 otherwise | add |
| melee | melee amount | add |
| projectile | projectile amount | add |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.
- Listed in the `DemonicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Demonic skills registry names that can be created via Demon Essence consumption. Format: modid:skill_name

## Related

- **Summons / entities:** Tensura, [Clone](../../mobs/clone.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Reaper.mpAcquirement` | 60,000 | Magicule Acquirement Cost. |
| `Reaper.size` | 0.5 | The size when activated Recon. |
| `Reaper.bonusSenseLevel` | 1 | The bonus Presence Sense Level when activated Recon. |
| `Reaper.bonusSenseRadius` | 10 | The bonus Presence Sense Radius when activated Recon. |
| `Reaper.bonusSenseRadiusMastered` | 20 | The bonus Presence Sense Radius when activated Recon with mastery. |
| `Reaper.meleeDodge` | 15 | Melee Dodge Chance when toggled. |
| `Reaper.meleeDodgeMastered` | 30 | Melee Dodge Chance when toggled with mastered. |
| `Reaper.projectileDodge` | 15 | Projectile Dodge Chance when toggled. |
| `Reaper.projectileDodgeMastered` | 30 | Projectile Dodge Chance when toggled with mastered. |
| `Reaper.attackMultiplier` | 0.5 | The multiplier of size/aura/magicule when activated the Attack Mode. |
| `Reaper.attackNumber` | 5 | The max number of clones when activated the Attack Mode. |
| `Reaper.attackCooldown` | 10 | The cooldown in second of the Attack Mode. |
| `Reaper.eaterBonusRange` | 3 | The bonus range in block of the Infinite Eater Mode. |
| `Reaper.eaterEPSteal` | 0.5 | The multiplier of the target's EP to be turned into the user's EP when killed with the Infinite Eater Mode. |
| `Reaper.eaterCooldown` | 10 | The cooldown in second of the Infinite Eater Mode. |
| `Reaper.eaterCooldownMastered` | 5 | The cooldown in second of the Infinite Eater Mode when mastered. |

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

`tensura:skills/unique_skills`
