# Degenerate

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Degenerate](../../../assets/icons/tensura/skill/degenerate.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:degenerate` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 35,000 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Press |

</div>

> Craft, decraft, customize items and absorb strength from weakened enemies.

## Modes

| # | Mode |
|---|---|
| 1 | Crafting |
| 2 | Synthesise |
| 3 | Separate |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Innate to mobs: [Shizu](../../mobs/shizu.md)
- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...
- Listed in the `AngelicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Angelic skills registry names that can be created via Holy Essence consumption. Format: modid:skill_name
- Listed in the `VirtueSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): Virtue unique skill ids for Michael Ultimate Dominion.

## Related

- **Effects:** [Anti-Skill](../../effects/anti-skill.md)
- **Referenced by:** [｢ Raphael, Lord of Wisdom ｣](../../../tr-nightmares/abilities/ultimate-skills/raphael-wisdom.md), [Pride Manas](../../../tr-nightmares/abilities/ultimate-skills/pride-manas.md), [Wise Manas](../../../tr-nightmares/abilities/ultimate-skills/wise-manas.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Degenerate.mpAcquirement` | 35,000 | Magicule Acquirement Cost. |
| `Degenerate.coreEPReduction` | false | Whether EP gained from Charybdis Core using Degenerate will follow the EP reduction calculation |
| `Degenerate.spiritualEntityHP` | 0.25 | The multiplier of Max Health that a Spiritual entity needs to have below to be affected by the Synthesize mode. |
| `Degenerate.spiritualEntityEP` | 1 | The multiplier of the Synthesized Spiritual entity's EP to be added to the user's Each of Aura and Magicule. |
| `Degenerate.synthesizeCooldown` | 5 | The cooldown in second of the Synthesize mode. |
| `Degenerate.synthesizeCooldownMastered` | 3 | The cooldown in second of the Synthesize mode when mastered. |
| `Degenerate.separateEP` | 0.75 | The multiplier of EP that an entity needs to have below to be affected by the Separate mode. |
| `Degenerate.magiculeCostEffect` | 100 | Magicule Cost to remove each harmful status effect from Allies using the Separate Mode. |
| `Degenerate.separateCooldown` | 5 | The cooldown in second of the Synthesize mode. |
| `Degenerate.separateCooldownMastered` | 3 | The cooldown in second of the Synthesize mode when mastered. |
| `Degenerate.maxBonusLevel` | 2 | How many levels that Degenerate can go above the maximum level of an enchantment. |
| `Degenerate.separateBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:barrier_piercing", "tensura:breathing_support", "tensura:crushing", "tensura:energy_steal", "tensura:elemental_boost", "tensura:elemental_resistance", "tensura:energy_protection", "tensura:holy_weapon", "tensura:intangibility", "tensura:magic_weapon", "tensura:magicule_absorption", "tensura:magic_capacity", "tensura:magic_protection", "tensura:severance", "tensura:slotting", "tensura:soul_eater" ... (34 total) | Lists of enchantments that Degenerate cannot separate. |
| `Degenerate.synthesisBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:barrier_piercing", "tensura:breathing_support", "tensura:crushing", "tensura:energy_steal", "tensura:elemental_boost", "tensura:elemental_resistance", "tensura:energy_protection", "tensura:holy_weapon", "tensura:intangibility", "tensura:magic_weapon", "tensura:magicule_absorption", "tensura:magic_capacity", "tensura:magic_protection", "tensura:severance", "tensura:slotting", "tensura:soul_eater" ... (34 total) | Lists of enchantments that Degenerate cannot synthesis to increase the enchantment's current level. |
| `Degenerate.maxBonusBlacklist` | "minecraft:aqua_affinity", "minecraft:channeling", "minecraft:flame", "minecraft:infinity", "minecraft:mending", "minecraft:silk_touch", "minecraft:binding_curse", "minecraft:vanishing_curse", "tensura:enervation", "tensura:lethargy", "tensura:sealing", "tensura:stagnation", "tensura:ruination", "tensura:vitality", "tensura:vigor", "tensura:transcendence", "tensura:growth", "tensura:restoration" | Lists of enchantments that Degenerate cannot synthesis above the enchantment's maximum level. |

Set in [`config/tensura/block_config.toml`](../../configs/config-tensura-block-config.md).

| Option | Default | Description |
|---|---|---|
| `CharybdisCore.charybdisCoreFusingSkillsInactive` | "tensura:gravity_manipulation" | List of Skills that can be obtained from fusing with Inactive Charybdis Core using Degenerate and similar abilities. |
| `CharybdisCore.charybdisCoreActiveEP` | 100,000 | The amount of EP needed for Inactive Charybdis Core to turn Active. |
| `CharybdisCore.charybdisCoreSkills` | "tensura:gravity_manipulation", "tensura:magic_jamming" | List of Skills that can be obtained from right-clicking Inert Charybdis Core. |
| `CharybdisCore.charybdisCoreFusingEP` | 200,000 | The amount of EP that can be obtained from fusing with Inert Charybdis Core using Degenerate and similar abilities. |
| `CharybdisCore.charybdisCoreFusingSkills` | "tensura:gravity_manipulation", "tensura:magic_jamming", "tensura:magic_sense", "tensura:ultraspeed_regeneration" | List of Skills that can be obtained from fusing with Inert Charybdis Core using Degenerate and similar abilities. |
| `CharybdisCore.charybdisCoreFusingSkillsActive` | "tensura:gravity_manipulation", "tensura:magic_sense" | List of Skills that can be obtained from fusing with Active Charybdis Core using Degenerate and similar abilities. |
| `CharybdisCore.charybdisCoreFusingSkillsInactive` | "tensura:gravity_manipulation" | List of Skills that can be obtained from fusing with Inactive Charybdis Core using Degenerate and similar abilities. |
| `specialBiomeFireSpread` | false | Enable/Disable fire spread inside Biomes with disabled fire tag (Ancient Forest, Miasmic Plains by default). |

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
