# Unyielding

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Unyielding](../../../assets/icons/tensura/skill/unyielding.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:unyielding` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 60,000 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Press |

</div>

> Draw power from loyal allies. Fortify subordinates and seamlessly switch to a backup body to stay in the fight.

## Modes

| # | Mode |
|---|---|
| 1 | Default |
| 2 | Backup |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you die
- Triggers when one of your subordinates dies

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.
- Listed in the `AngelicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Angelic skills registry names that can be created via Holy Essence consumption. Format: modid:skill_name
- Listed in the `VirtueSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): Virtue unique skill ids for Michael Ultimate Dominion.

## Related

- **Referenced by:** [｢ Yog-Sothoth, Lord of Space-Time ｣](../../../tr-nightmares/abilities/ultimate-skills/yog-sothoth.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Unyielding.mpAcquirement` | 60,000 | Magicule Acquirement Cost. |
| `Unyielding.magiculeBackupCost` | 0.25 | Magicule Cost multiplier of the user's maximum Magicule required to spawn a backup. |
| `Unyielding.unyieldingRadius` | 30 | The radius in block that subordinates need to stay within the user to increase Unyielding point. |
| `Unyielding.unyieldingPointGain` | 1 | The number of Unyielding points that a subordinate gains every 5 seconds while in required radius. |
| `Unyielding.unyieldingPointGainMastered` | 2 | The number of Unyielding points that a subordinate gains every 5 seconds while in required radius when mastered. |
| `Unyielding.unyieldingPointEP` | 120 | The number of Unyielding points needed to gain each 10% of the EP of a fallen subordinate. |
| `Unyielding.unyieldingPointSkill` | 120 | The number of Unyielding points needed to gain skills from a fallen subordinate. |
| `Unyielding.unyieldingPointSkillUnique` | 600 | The number of Unyielding points needed to gain Unique skills from a fallen subordinate. |
| `Unyielding.backupCooldown` | 5 | The cooldown in second to spawn/swap a backup. |
| `Unyielding.backupCooldownMastered` | 3 | The cooldown in second to spawn/swap a backup when mastered. |

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

`tensura:skills/hopeful`, `tensura:skills/unique_skills`, `tensura:skills/virtue_skills`
