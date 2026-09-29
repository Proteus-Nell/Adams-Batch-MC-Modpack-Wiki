# `config/tensura/ability/skill/unique_config.toml`

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Configs](index.md)</small>

## `[AbsoluteSeverance]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 60,000 |  | Magicule Acquirement Cost. |
| `magiculeCostCoating` | 1,000 |  | Magicule Cost to activate Coating. |
| `magiculeCostProjectile` | 20,000 |  | Magicule Cost to activate Severance Projectile. |
| `coatingDuration` | 12,000 |  | The duration in tick of the Severance Blade effect (Coating). |
| `coatingLevel` | 5 |  | The level of the Severance Blade effect (+ 10 Damage Boost each level). |
| `coatingLevelMastered` | 20 |  | The level of the Severance Blade effect when mastered. |
| `projectileDamage` | 50 |  | The damage of the Severance Projectile. |
| `projectileDamageMastered` | 300 |  | The damage of the Severance Projectile when mastered. |
| `projectileSize` | 5 |  | The size of the Severance Projectile. |
| `projectileSizeMastered` | 8 |  | The size of the Severance Projectile when mastered. |
| `projectileDuration` | 20 |  | The duration in tick of the Severance Projectile. |
| `projectileDurationMastered` | 40 |  | The duration in tick of the Severance Projectile when mastered. |
| `projectileCooldown` | 3 |  | The cooldown in second of the Severance Projectile. |

## `[Analyst]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 30,000 |  | Magicule Acquirement Cost. |
| `analysisLevel` | 18 |  | The Analysis Level when activated. |
| `analysisLevelMastered` | 28 |  | The Analysis Level when activated with Mastery. |
| `analysisRadius` | 20 |  | The Analysis Radius when activated. |
| `analysisRadiusMastered` | 25 |  | The Analysis Radius when activated with Mastery. |
| `analyzeRange` | 30 |  | The range in block of Analyze. |
| `analyzeTime` | 100 |  | The hold time in tick of Analyze to copy a Magic. |
| `analyzeTimeMastered` | 60 |  | The hold time in tick of Analyze to copy a Magic. |
| `learningPoint` | 2 |  | The bonus number of learning point to gain when toggled. |
| `masteryPoint` | 2 |  | The bonus number of mastery point to gain when toggled. |
| `chantSpeed` | 2 |  | The chant speed multiplier when toggled. |

## `[AntiSkill]`

| Option | Default | Range | Description |
|---|---|---|---|
| `antiDuration` | 100 |  | The duration in tick of the Anti-skill effect to apply on targets when used. |

## `[Berserker]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 40,000 |  | Magicule Acquirement Cost. |
| `auraPercentage` | 2 |  | The bonus Aura percentage the user gains when toggled on. |
| `magiculePercentage` | 2 |  | The bonus Magicule percentage the user gains when toggled on. |
| `armorDurability` | 0.25 |  | How much of the attack damage that Berserker will inflict on targets' armor durability. |
| `weaponDurability` | 5 |  | How much durability that Berserker will take from attackers' weapon when attacking the user. |
| `holdTime` | 40 |  | The Hold Time in Tick to activate Berserker. |
| `armorEP` | 20,000 |  | How much EP the user needs to have for each armor point. |
| `armorMax` | 100 |  | The maximum amount of armor point that the user can gain. |
| `attackBase` | 5 |  | The base attack point the user gain when activated. |
| `attackEP` | 40,000 |  | How much EP the user needs to have for each additional attack point. |
| `attackMax` | 55 |  | The maximum amount of armor point that the user can gain (every bonus attack point is doubled with mastery). |
| `speedEP` | 25,000 |  | How much EP the user needs to have for each additional speed point. |
| `speedMax` | 40 |  | The maximum amount of armor point that the user can gain. |

## `[Berserk]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 20,000 |  | Magicule Acquirement Cost. |
| `magiculeCostFlameAura` | 200 |  | Magicule Cost to each attack while toggled Flame Aura. |
| `magiculeCostRage` | 300 |  | Magicule Cost to activate Rage. |
| `magiculeCostMadOgre` | 5,000 |  | Magicule Cost to activate Mad Ogre. |
| `masteryGainMultiplier` | 5 |  | The multiplier for mastery point gaining when activating Mad Ogre. |
| `rageDuration` | 6,000 |  | The duration in tick of the Strengthen effect when activated Rage. |
| `rageLevel` | 5 |  | The level of the Strengthen effect when activated Rage (+3 Attack Damage per level). |
| `rageLevelMastered` | 10 |  | The level of the Strengthen effect when activated Rage with Mastered. |
| `madOgreDuration` | 12,000 |  | The duration in tick of the Mad Ogre effect when activated. |
| `madOgreLevel` | 1 |  | The level of the Mad Ogre effect when activated. |
| `madOgreLevelMastered` | 2 |  | The level of the Mad Ogre effect when activated with Mastered. |
| `orbDamage` | 100 |  | The damage of each flame orb shot by Mad Ogres when mastered. |
| `orbBlast` | 4 |  | The blast radius of each flame orb when triggered when mastered. |
| `defenceMultiplier` | 0.5 |  | The input damage multiplier that the user takes when in defence mode of Mad Ogres. |
| `cooldown` | 600 |  | The Cooldown in second after Mad Ogre runs out. |
| `flameAuraBoost` | 2 |  | The Flame Damage Boost when toggled Flame Aura. |
| `flameAuraBurnTick` | 200 |  | How long in tick that the target will be set on fire when attacked with Flame Aura toggled. |
| `flameAuraDamage` | 0.5 |  | How Flame damage multiplied based on the user's physical/battlewill attack with Flame Aura toggled. |

## `[Bewilder]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 30,000 |  | Magicule Acquirement Cost. |
| `magiculeCostTarget` | 50 |  | Magicule Cost to activate Target Mode. |
| `magiculeCostArea` | 80 |  | Magicule Cost to activate Area Mode. |
| `magiculeCostCharm` | 200 |  | Magicule Cost to activate Charm Mode. |
| `magiculeCostKill` | 100 |  | Magicule Cost to activate Kill Mode. |
| `controlDuration` | 12,000 |  | The duration in tick of the Mind Control effect (-1 = permanent). |
| `controlResistedDuration` | 6,000 |  | The duration in tick of the Mind Control effect when the target has Spiritual Attack Resistance (-1 = permanent). |
| `areaRadius` | 10 |  | The radius in block of the Area/Kill Mode. |
| `areaRadiusMastered` | 15 |  | The radius in block of the Area/Kill Mode when mastered. |
| `controlAreaDuration` | 6,000 |  | The duration in tick of the Mind Control effect when using Area Mode (-1 = permanent). |
| `controlAreaResistedDuration` | 3,000 |  | The duration in tick of the Mind Control effect when using Area Mode while the target has Spiritual Attack Resistance (-1 = permanent). |
| `heroDuration` | 2,400 |  | The duration in tick of the Hero of the Village effect when activating Charm Mode. |
| `heroLevel` | 5 |  | The level of the Hero of the Village effect when activating Charm Mode. |
| `killHPMultiplier` | 1 |  | The multiplier of targets' current HP to deal when activating Kill Mode. |
| `killHPResistedMultiplier` | 0.5 |  | The multiplier of targets' current HP to deal when activating Kill Mode while the target has Spiritual Attack Resistance. |
| `killCooldown` | 5 |  | The cooldown in second of the Kill Mode. |
| `killCooldownMastered` | 3 |  | The cooldown in second of the Kill Mode when mastered. |

## `[Chef]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 10,000 |  | Magicule Acquirement Cost. |
| `magiculeCostEffect` | 100 |  | Magicule Cost to remove each harmful status effect. |
| `magiculeCostHP` | 60 |  | Magicule Cost to heal each HP. |
| `magiculeCostHPMastered` | 40 |  | Magicule Cost to heal each HP when mastered. |
| `cooldown` | 5 |  | The cooldown in second when activated. |
| `cooldownMastered` | 3 |  | The cooldown in second when activated with mastery. |

## `[ChosenOne]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 90,000 |  | Magicule Acquirement Cost. |
| `magiculeCostHaki` | 25 |  | Magicule Cost to activate Hero Haki. |
| `magiculeCostCharisma` | 200 |  | Magicule Cost to activate Hero's Charisma. |
| `heroLevel` | 5 |  | The level of the Hero of the Village effect. |
| `luckLevel` | 5 |  | The level of the Luck effect. |
| `allyCritChance` | 50 |  | The amount of Critical Chance of the Ally Boost each level.<br>Chosen One has Ally Boost II, Villain has Ally Boost I |
| `meleeDodge` | 10 |  | Melee Dodge Chance for the user and allies when activated. |
| `projectileDodge` | 10 |  | Projectile Dodge Chance for the user and allies when activated. |
| `blessingRadius` | 15 |  | The radius in block of the Hero's Blessing's effect on allies. |
| `controlRadius` | 10 |  | The radius in block of the Hero's Charisma's effect. |
| `controlDuration` | 2,400 |  | The duration in tick of the Mind Control effect when activating Hero's Charisma (-1 = permanent). |
| `controlResistedDuration` | 1,200 |  | The duration in tick of the Mind Control effect when activating Hero's Charisma while the target has Spiritual Attack Resistance (-1 = permanent). |
| `hpMultiplier` | 0.5 |  | The multiplier of Max Health when an entity is revived as Ally with Hero's Charisma. |
| `shpMultiplier` | 0.5 |  | The multiplier of Max Spiritual Health when an entity is revived as Ally with Hero's Charisma. |

## `[Commander]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 30,000 |  | Magicule Acquirement Cost. |
| `chantSpeed` | 2 |  | The chant speed multiplier when toggled. |
| `meleeDodge` | 10 |  | Melee Dodge Chance when toggled. |
| `projectileDodge` | 10 |  | Projectile Dodge Chance when toggled. |
| `dodgeNegation` | 50 |  | Dodge Negation Chance when toggled. |
| `inspireRadius` | 30 |  | The radius in block for Inspire Force's effect on allies. |
| `inspireMultiplier` | 0.3 |  | The multiplier of boost on each physical stats of allies when applied with Inspire Force (doubled with mastery). |
| `inspireCritChance` | 30 |  | The Critical Attack Chance for allies when applied with Inspire Force (doubled with mastery). |

## `[Cook]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 60,000 |  | Magicule Acquirement Cost. |
| `critChance` | 100 |  | Critical Attack Chance when toggled. |
| `dodgeNegation` | 100 |  | Dodge Negation Chance when toggled. |
| `learningPoint` | 4 |  | The bonus number of learning point to gain when toggled. |
| `masteryPoint` | 4 |  | The bonus number of mastery point to gain when toggled. |
| `barrierEP` | 2 |  | The multiplier of the user's EP that the target to have above to ignore Barrier shattering when attacked by the user. |
| `hpReducedMultiplier` | 1 |  | The multiplier of the user's damage dealt that the target's Max Health get reduced by. |

## `[Creator]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 75,000 |  | Magicule Acquirement Cost. |
| `analysisLevel` | 2 |  | The Analysis Level when activated. |
| `analysisLevelMastered` | 6 |  | The Analysis Level when activated with Mastery. |
| `analysisRadius` | 0 |  | The Analysis Radius when activated. |
| `analysisRadiusMastered` | 5 |  | The Analysis Radius when activated with Mastery. |
| `creationCooldown` | 1,200 |  | The cooldown in second after creating a Skill. |
| `creationVanishTimer` | 1,200 |  | The cooldown in second before the created skill vanishes. |
| `masteryGainMultiplier` | 5 |  | The multiplier for mastery point gaining when created a Skill. |
| `uniqueSkills` | "tensura:anti_skill", "tensura:analyst", "tensura:absolute_severance", "tensura:berserk", "tensura:berserker", "tensura:bewilder", "tensura:chef", "tensura:commander", "tensura:cook", "tensura:falsifier", "tensura:fighter", "tensura:fusionist", "tensura:gourmand", "tensura:guardian", "tensura:healer", "tensura:martial_master", "tensura:mathematician", "tensura:murderer", "tensura:musician", "tensura:observer" ... (39 total) |  | List of Unique skills that can be created by Creator. |

## `[Degenerate]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 35,000 |  | Magicule Acquirement Cost. |
| `coreEPReduction` | false |  | Whether EP gained from Charybdis Core using Degenerate will follow the EP reduction calculation |
| `spiritualEntityHP` | 0.25 |  | The multiplier of Max Health that a Spiritual entity needs to have below to be affected by the Synthesize mode. |
| `spiritualEntityEP` | 1 |  | The multiplier of the Synthesized Spiritual entity's EP to be added to the user's Each of Aura and Magicule. |
| `synthesizeCooldown` | 5 |  | The cooldown in second of the Synthesize mode. |
| `synthesizeCooldownMastered` | 3 |  | The cooldown in second of the Synthesize mode when mastered. |
| `separateEP` | 0.75 |  | The multiplier of EP that an entity needs to have below to be affected by the Separate mode. |
| `magiculeCostEffect` | 100 |  | Magicule Cost to remove each harmful status effect from Allies using the Separate Mode. |
| `separateCooldown` | 5 |  | The cooldown in second of the Synthesize mode. |
| `separateCooldownMastered` | 3 |  | The cooldown in second of the Synthesize mode when mastered. |
| `maxBonusLevel` | 2 |  | How many levels that Degenerate can go above the maximum level of an enchantment. |
| `separateBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:barrier_piercing", "tensura:breathing_support", "tensura:crushing", "tensura:energy_steal", "tensura:elemental_boost", "tensura:elemental_resistance", "tensura:energy_protection", "tensura:holy_weapon", "tensura:intangibility", "tensura:magic_weapon", "tensura:magicule_absorption", "tensura:magic_capacity", "tensura:magic_protection", "tensura:severance", "tensura:slotting", "tensura:soul_eater" ... (34 total) |  | Lists of enchantments that Degenerate cannot separate. |
| `synthesisBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:barrier_piercing", "tensura:breathing_support", "tensura:crushing", "tensura:energy_steal", "tensura:elemental_boost", "tensura:elemental_resistance", "tensura:energy_protection", "tensura:holy_weapon", "tensura:intangibility", "tensura:magic_weapon", "tensura:magicule_absorption", "tensura:magic_capacity", "tensura:magic_protection", "tensura:severance", "tensura:slotting", "tensura:soul_eater" ... (34 total) |  | Lists of enchantments that Degenerate cannot synthesis to increase the enchantment's current level. |
| `maxBonusBlacklist` | "minecraft:aqua_affinity", "minecraft:channeling", "minecraft:flame", "minecraft:infinity", "minecraft:mending", "minecraft:silk_touch", "minecraft:binding_curse", "minecraft:vanishing_curse", "tensura:enervation", "tensura:lethargy", "tensura:sealing", "tensura:stagnation", "tensura:ruination", "tensura:vitality", "tensura:vigor", "tensura:transcendence", "tensura:growth", "tensura:restoration" |  | Lists of enchantments that Degenerate cannot synthesis above the enchantment's maximum level. |

## `[DivineBerserker]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 30,000 |  | Magicule Acquirement Cost. |
| `magiculeCost` | 10,000 |  | Magicule Cost to activate. |
| `battlewillMultiplier` | 1.5 |  | The Battlewill damage multiplier that the user does when activated. |
| `battlewillMultiplierMastered` | 2 |  | The Battlewill damage multiplier that the user does when activated with mastery. |
| `transformationDuration` | 3,600 |  | The duration in tick of the Transformation. |
| `transformationDurationMastered` | 7,200 |  | The duration in tick of the Transformation. |
| `cooldown` | 600 |  | The Cooldown in second after activation. |

## `[Engorger]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 30,000 |  | Magicule Acquirement Cost. |
| `magiculeCost` | 300 |  | Magicule Cost to activate. |
| `armor` | 10 |  | The amount of armor point from Engorgement. |
| `attack` | 10 |  | The amount of attack point from Engorgement. |
| `attackKnock` | 1 |  | The amount of attack knockback from Engorgement. |
| `knockResistance` | 0.4 |  | The amount of knockback resistance from Engorgement. |
| `speed` | 0.1 |  | The amount of speed from Engorgement. |
| `jumpBoost` | 0.1 |  | The amount of jump boost from Engorgement. |
| `range` | 2.5 |  | The amount of range from Engorgement. |
| `size` | 1.5 |  | The amount of size from Engorgement. |
| `heal` | 1 |  | The amount of HP the user regenerates from Engorgement each second. |
| `dashLevel` | 3 |  | The level of the dash boost when activated (similar to Riptide). |
| `dashDuration` | 15 |  | The duration in tick of the dash boost when activated. |
| `dashAttackMultiplier` | 1 |  | The damage multiplier compared to the user's attack damage when hit target during Dash boost. |
| `dashAttackBonus` | 50 |  | The Bonus attack damage of the dash boost on top of the user's attack damage. |
| `dashAttackBonusMastered` | 100 |  | The Bonus attack damage of the dash boost on top of the user's attack damage when mastered. |

## `[Envy]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 100,000 |  | Magicule Acquirement Cost. |
| `magiculeCostSap` | 1,000 |  | Magicule Cost to activate Strength Sap. |
| `luckLevel` | 3 |  | The level of the Luck effect when toggled. |
| `meleeDodge` | 10 |  | Melee Dodge Chance when toggled. |
| `projectileDodge` | 10 |  | Projectile Dodge Chance when toggled. |
| `insanityChance` | 20 |  | The chance for the user to be applied with Insanity when using Strength Sap every 10 second. |
| `insanityLevel` | 1 |  | The increasing level of the Insanity effect when the user is applied by Strength Sap. |
| `insanityDuration` | 240 |  | The duration in tick of the Insanity effect when the user is applied by Strength Sap. |
| `sapRadius` | 15 |  | The radius in block of the Strength Sap effect. |
| `sapEP` | 0.6 |  | The multiplier of EP that an entity needs to have below to be affected by the Strength Sap. |
| `sapEPMastered` | 0.8 |  | The multiplier of EP that an entity needs to have below to be affected by the Strength Sap when mastered. |
| `epDifferenceMultiplier` | 0.1 |  | The EP difference multiplier for each Slowness/Weakness Level. |
| `sapDuration` | 200 |  | The duration in tick of the Slowness/Weakness effect when targets are applied by Strength Sap. |
| `epDrain` | 0.001 |  | The multiplier of EP that the user drains from targets each second. |

## `[Falsifier]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 15,000 |  | Magicule Acquirement Cost. |
| `magiculeCost` | 200 |  | Magicule Cost to activate Concealment. |
| `concealmentDuration` | 2,400 |  | The duration in tick of the Concealment effect when activated. |
| `concealmentCooldown` | 20 |  | The cooldown in second of the Concealment Mode. |
| `concealmentCooldownMastered` | 0 |  | The cooldown in second of the Concealment Mode when mastered. |
| `fakeSpeedMultiplier` | 0.6 |  | Activation Speed Multiplier when activating Fake Death. |
| `fakeSpeedMultiplierMastered` | 0.8 |  | Activation Speed Multiplier when activating Fake Death with mastery. |
| `fakeMaxTime` | 600 |  | The maximum time in tick that the user can hold down Fake Death. |
| `fakeInputMultiplier` | 0.5 |  | The input damage multiplier that the user takes when Fake Death is triggered. |
| `fakeConcealmentDuration` | 60 |  | The duration in tick of the Concealment effect after Fake Death is triggered. |

## `[Fighter]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `attackBoost` | 75 |  | The physical attack damage boost when in Slot. |
| `attackBoostMastered` | 150 |  | The physical attack damage boost when in Slot with mastery. |
| `masteryPoint` | 2 |  | The bonus number of mastery point to gain when toggled. |
| `dodgeStrength` | 0.25 |  | The bonus dodge strength when toggled. |
| `dodgeInvulnerability` | 2 |  | The bonus dodge invulnerability when toggled. |

## `[Fusionist]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `magiculeCostFuse` | 1,000 |  | Magicule Cost to activate Fuse mode. |
| `magiculeCostProjectile` | 200 |  | Magicule Cost to activate Projectile mode. |
| `range` | 5 |  | The minimum range in block of the skill. |
| `fuseMatterCost` | 5 |  | The amount of disassembled matter points needed to activate Fuse. |
| `fuseBlastDamage` | 300 |  | The blast damage of the landmine from Fuse. |
| `fuseBlastDamageMastered` | 500 |  | The blast damage of the landmine from Fuse. |
| `fuseBlastRadius` | 25 |  | The blast size of the landmine from Fuse. |
| `bonusBlastCost` | 10 |  | The amount of disassembled matter points needed to add charge more power on a landmine with mastery. |
| `bonusBlastDamage` | 50 |  | The blast damage to charge on a landmine with mastery. |
| `bonusBlastRadius` | 5 |  | The blast size to charge on a landmine with mastery. |
| `maxBlastRadius` | 50 |  | The max size the landmine can reach when charged. |
| `projectileMatterCost` | 1 |  | The amount of disassembled matter points needed to activate Projectile. |
| `projectileBlastRadius` | 6 |  | The blast radius of the Projectile shot. |

## `[Gluttony]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 100,000 |  | Magicule Acquirement Cost. |
| `magiculeCostIsolation` | 200 |  | Magicule Cost to remove each harmful status effect with Isolation. |
| `magiculeCostCorrosion` | 200 |  | Magicule Cost to activate Corrosion. |
| `predationRange` | 10 |  | The max range in block of the Predation Mode. |
| `predationRangeMastered` | 15 |  | The max range in block of the Predation Mode when mastered. |
| `predationDamage` | 50 |  | The attack damage of the Predation Mode. |
| `predationEPDrain` | 1,000 |  | The amount of EP that the user drains from target using the Predation Mode. |
| `predationSkillChance` | 30 |  | The chance to obtain skills from targets without killing them with the Predation Mode. |
| `predationSkillNumber` | 3 |  | The number of skills to gain from targets at a time without killing them with the Predation Mode. |
| `predationCorrosionDuration` | 100 |  | The duration in tick of the Corrosion effect applied by the Predation Mode. |
| `predationCorrosionLevel` | 2 |  | The level of the Corrosion effect applied by the Predation Mode. |
| `predationEPSteal` | 0.5 |  | The multiplier of the target's EP to be turned into the user's EP when killed with the Predation Mode. |
| `magiculeMultiplier` | 2 |  | The multiplier of magicule gained from dissolving items with the Isolation Mode. |
| `healthMultiplier` | 2 |  | The multiplier of health healed from dissolving items with the Isolation Mode.. |
| `isolationCooldown` | 5 |  | The cooldown in second of the Isolation Mode. |
| `isolationCooldownMastered` | 3 |  | The cooldown in second of the Isolation Mode when mastered. |
| `corrosionSpeedMultiplier` | 0.5 |  | Activation Speed Multiplier when activating the Corrosion Mode. |
| `corrosionRadius` | 5 |  | The radius in block of the Corrosion Mode. |
| `corrosionDamage` | 10 |  | The amount of damage dealt onto targets every 10 tick using the Corrosion Mode. |
| `corrosionEPSteal` | 0.4 |  | The EP multiplier of targets killed by the Corrosion Mode to be added to the user's Each of Aura and Magicule. |
| `waterCapacity` | 3,000 |  | The bonus water capacity when the skill is acquired. |
| `lavaCapacity` | 3,000 |  | The bonus lava capacity when the skill is acquired. |

## `[GodlyCraftsman]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 60,000 |  | Magicule Acquirement Cost. |
| `maxBonusLevel` | 2 |  | How many levels that GodlyCraftsman can go above the maximum level of an enchantment. |
| `enchantmentBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:enervation", "tensura:lethargy", "tensura:sealing", "tensura:stagnation", "tensura:ruination", "tensura:vitality", "tensura:vigor", "tensura:transcendence", "tensura:growth", "tensura:restoration" |  | Lists of enchantments that Godly Craftsman cannot learn or add. |
| `maxBonusBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:barrier_piercing", "tensura:breathing_support", "tensura:crushing", "tensura:energy_steal", "tensura:elemental_boost", "tensura:elemental_resistance", "tensura:energy_protection", "tensura:holy_weapon", "tensura:intangibility", "tensura:magic_weapon", "tensura:magicule_absorption", "tensura:magic_capacity", "tensura:magic_protection", "tensura:severance", "tensura:slotting", "tensura:soul_eater" ... (34 total) |  | Lists of enchantments that Godly Craftsman cannot learn or add above the enchantment's maximum level. |
| `curseChance` | 0.03 |  | The percentage chance to obtain a Curse Engraving per Engraving on the item. |

## `[Gourmand]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 70,000 |  | Magicule Acquirement Cost. |
| `auraPercentage` | 3 |  | The bonus Aura percentage the user gains when toggled on. |
| `auraPercentageMastered` | 7.5 |  | The bonus Aura percentage the user gains when toggled on with Mastery. |
| `magiculePercentage` | 3 |  | The bonus Magicule percentage the user gains when toggled on. |
| `magiculePercentageMastered` | 7.5 |  | The bonus Magicule percentage the user gains when toggled on with Mastery. |
| `epStealChance` | 50 |  | The chance to steal MP from targets when the user attack them with Gourmand. |
| `epStealChanceMastered` | 75 |  | The chance to steal MP from targets when the user attack them with Gourmand when mastered. |
| `epStealPercentage` | 0.01 |  | The multiplier of MP to steal from targets when the user attack them with Gourmand. |
| `fearHeartEat` | 5 |  | The optional level of Fear that the target needs to have to be affected by Heart Eat. |
| `epHeartEat` | 0.1 |  | The optional multiplier of the user's EP that the target needs to have below to be affected by Heart Eat. |
| `heartEatEpMultiplier` | 1 |  | The multiplier of the target's EP that the user will recover with once activated Heart Eat (Split bewteen MP and AP). |

## `[Gourmet]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `magiculeCostCorrosion` | 200 |  | Magicule Cost to activate Corrosion. |
| `predationRange` | 3 |  | The range in block of the Predation Mode. |
| `predationDamage` | 25 |  | The attack damage of the Predation Mode. |
| `predationCooldown` | 5 |  | The cooldown in second of the Predation Mode. |
| `predationCooldownMastered` | 1 |  | The cooldown in second of the Predation Mode when mastered. |
| `corrosionSpeedMultiplier` | 0.5 |  | Activation Speed Multiplier when activating the Corrosion Mode. |
| `corrosionRadius` | 5 |  | The radius in block of the Corrosion Mode. |
| `corrosionDamage` | 5 |  | The amount of damage dealt onto targets every 10 tick using the Corrosion Mode. |
| `corrosionEPSteal` | 0.3 |  | The EP multiplier of targets killed by the Corrosion Mode to be added to the user's Each of Aura and Magicule. |
| `waterCapacity` | 6,000 |  | The bonus water capacity when the skill is acquired. |
| `lavaCapacity` | 6,000 |  | The bonus lava capacity when the skill is acquired. |

## `[GreatSage]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 75,000 |  | Magicule Acquirement Cost. |
| `chantSpeed` | 2 |  | The chant speed multiplier when toggled. |
| `learningPoint` | 9 |  | The bonus number of learning point to gain when toggled. |
| `masteryPoint` | 9 |  | The bonus number of mastery point to gain when toggled. |
| `analysisLevel` | 8 |  | The Analysis Level when activated. |
| `analysisLevelMastered` | 18 |  | The Analysis Level when activated with Mastery. |
| `analysisRadius` | 15 |  | The Analysis Radius when activated. |
| `analysisRadiusMastered` | 25 |  | The Analysis Radius when activated with Mastery. |
| `copyRange` | 10 |  | The range in block of Analysis's Copy on mobs. |
| `copyRangeMagic` | 30 |  | The range in block of Analysis's Copy on magic circles. |
| `copyChance` | 25 |  | The chance to success copying skills from targets. |
| `copyChanceMastered` | 50 |  | The chance to success copying skills from targets when mastered. |
| `copyCooldownSuccess` | 10 |  | The cooldown in second when the user successfully copied a skill from targets. |
| `copyCooldownFail` | 5 |  | The cooldown in second when the user failed to copy a skill from targets. |

## `[Greed]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 100,000 |  | Magicule Acquirement Cost. |
| `magiculeCostFlare` | 10 |  | Base Magicule Cost to activate Greed Flare's buff. |
| `magiculeCostFlareAlly` | 50 |  | Base Magicule Cost to activate Greed Flare's ally buff. |
| `magiculeCostFlareAttack` | 20 |  | Base Magicule Cost to activate Greed Flare's attack. |
| `magiculeCostWish` | 1,000 |  | Base Magicule Cost to activate Death Wish. |
| `maxDistance` | 30 |  | The max distance in block for Spiritual Domination. |
| `playerControl` | 60 |  | The base time in second to control a player with Spiritual Domination. |
| `entityControl` | 90 |  | The base time in second to control a non-player entity with Spiritual Domination. |
| `closeDistance` | 5 |  | The distance in block to be considered close-range for Spiritual Domination. |
| `closeControl` | 30 |  | The reduced time in second to control a player with Spiritual Domination when in close range. |
| `farDistance` | 20 |  | The distance in block to be considered far-range for Spiritual Domination. |
| `farControl` | 30 |  | The increased time in second to control a player with Spiritual Domination when in far range. |
| `playerTradeControl` | 10 |  | The number of Villager Trade that the targeted player needed to do to reduce 1 second in control time for Spiritual Domination. |
| `mobTradeControl` | 2 |  | The amount of second to reduce from control time of Spiritual Domination for each merchant trade of a trader mob. |
| `deathTime` | 10 |  | The activation time in second needed to activate Death Wish. |
| `deathInterference` | 6 |  | The level of movement interference when the target is being casted with Death Wish (-10% speed each level). |
| `flareRange` | 20 |  | The range in block of Greed Flare. |
| `flareBuff` | 0.05 |  | The multiplier of the user's current SHP when using Greed Flare's Buff. |
| `flareBuffMastery` | 0.1 |  | The multiplier of the user's current SHP when using Greed Flare's Buff with Mastery. |
| `flareAllyBuff` | 0.025 |  | The multiplier of the ally's current SHP when using Greed Flare's Buff on allies. |
| `flareAllyBuffMastery` | 0.05 |  | The multiplier of the ally's current SHP when using Greed Flare's Buff on allies with Mastery. |
| `flareAttack` | 0.025 |  | The multiplier of the user's current SHP when using Greed Flare's Attack. |
| `flareAttackMastery` | 0.05 |  | The multiplier of the user's current SHP when using Greed Flare's Attack with Mastery. |
| `flareCooldown` | 20 |  | The cooldown in second of Greed Flare's Buff activate. |
| `flareCooldownMastered` | 10 |  | The cooldown in second of Greed Flare's Buff activate when mastered. |
| `flareAttackCooldown` | 20 |  | The cooldown in second of Greed Flare's Attack. |
| `flareAttackCooldownMastered` | 10 |  | The cooldown in second of Greed Flare's Attack when mastered. |

## `[Guardian]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `magiculeCost` | 100 |  | Base Magicule Cost to activate. |
| `protectionRadius` | 25 |  | The radius of the Grant Protection Mode. |
| `protectionDuration` | 3,600 |  | The duration in tick of the Protection effect to apply on Allies. |
| `protectionArmor` | 10 |  | The amount of armor point gained when applied with Protection. |
| `protectionBarrier` | 30 |  | The amount of barrier point gained when applied with Protection. |
| `wallArmor` | 15 |  | The amount of armor point gained when activated Iron Wall. |
| `wallArmorMastered` | 40 |  | The amount of armor point gained when activated Iron Wall with mastery. |
| `wallKnockResist` | 0.4 |  | The amount of knockback resistance gained when activated Iron Wall. |
| `wallKnockResistMastered` | 1 |  | The amount of knockback resistance gained when activated Iron Wall with mastery. |

## `[Healer]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `magiculeCostInfection` | 200 |  | Magicule Cost to apply/remove Infection for other entities. |
| `magiculeCostHP` | 80 |  | Magicule Cost to heal each HP. |
| `magiculeCostHPMastered` | 40 |  | Magicule Cost to heal each HP when mastered. |
| `magiculeCostSHP` | 60 |  | Magicule Cost to heal each SHP when mastered. |
| `cooldown` | 5 |  | The cooldown in second when activated Heal. |
| `cooldownMastered` | 3 |  | The cooldown in second when activated Heal with mastery. |
| `infectionDuration` | 900 |  | The duration in tick of the Infection effect when applied on targets. |
| `plagueRadius` | 7 |  | The radius in block of the Plague Mode. |
| `cooldownInfection` | 3 |  | The cooldown in second when activated Infection. |
| `cooldownInfectionMastered` | 1 |  | The cooldown in second when activated Infection with mastery. |

## `[InfinityPrison]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 90,000 |  | Magicule Acquirement Cost. |
| `magiculeCostGuard` | 25 |  | The base magicule cost to block per damage point with Absolute Guard. |
| `magiculeCostImprison` | 50,000 |  | The Minimal Magicule Cost to activate Imprison. |
| `magiculeCostImprisonTarget` | 0.5 |  | The multiplier of the target's EP to be added as Magicule Cost for the user to imprison the target. |
| `guardEP` | 0.75 |  | The multiplier of the user's EP that an attacker needs to have above to bypass Absolute Guard. |
| `imprisonRange` | 30 |  | The max range in block to Imprison an target. |
| `imprisonDuration` | 6,000 |  | The duration in tick of the Imprison effect. |
| `imprisonDurationMastered` | 12,000 |  | The duration in tick of the Imprison effect when mastered. |
| `cooldownImprison` | 20 |  | The cooldown in second when activated Imprison. |
| `cooldownImprisonMastered` | 10 |  | The cooldown in second when activated Imprison with mastery. |
| `waterCapacity` | 9,000 |  | The bonus water capacity when the skill is acquired. |
| `lavaCapacity` | 9,000 |  | The bonus lava capacity when the skill is acquired. |

## `[Lust]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 100,000 |  | Magicule Acquirement Cost. |
| `magiculeCostDrain` | 100 |  | Magicule Cost to activate Drain. |
| `magiculeCostRebirth` | 3,000 |  | Magicule Cost to activate Rebirth. |
| `magiculeCostEmbrace` | 500 |  | Magicule Cost to activate Embracing Drain. |
| `magiculeCostBless` | 7,500 |  | Magicule Cost to activate Death Blessing. |
| `magiculeCostHP` | 80 |  | Magicule Cost to heal each HP with Invigorate. |
| `magiculeCostHPMastered` | 40 |  | Magicule Cost to heal each HP with Invigorate with Mastery. |
| `drainEP` | 200 |  | The amount of EP drained from targets when using Drain. |
| `drainEPMastered` | 0.005 |  | The multiplier of EP drained from targets when using Drain with mastery. |
| `drainDuration` | 200 |  | The duration in tick of the Lust Drain effect applied on the user's attack when activated Drain. |
| `cooldownDrain` | 1 |  | The cooldown in second of the Drain Mode. |
| `cooldownInvigorate` | 5 |  | The cooldown in second when activated Invigorate. |
| `cooldownInvigorateMastered` | 3 |  | The cooldown in second when activated Invigorate with mastery. |
| `embraceDuration` | 100 |  | The duration in tick of the Embracing Drain effect. |
| `embraceEP` | 200 |  | The amount of EP drained from targets when using Embracing Drain. |
| `embraceEPMastered` | 0.005 |  | The multiplier of EP drained from targets when using Embracing Drain with mastery. |
| `blessRange` | 10 |  | The max range in block of the Death Blessing attack. |
| `blessRadius` | 3 |  | The radius in block of the Death Blessing attack. |
| `blessTime` | 100 |  | The amount of time in tick needed to activate the Death Blessing attack. |
| `blessInterference` | 6 |  | The level of movement interference when the target is being casted with Death Wish (-10% speed each level). |
| `blessEP` | 0.5 |  | The multiplier of the user's EP that the target needs to have below to take full effect of Death Blessing. |
| `blessHalfEP` | 0.75 |  | The multiplier of the user's EP that the target needs to have below to take half effect of Death Blessing. |
| `blessFullRestore` | 1 |  | The multiplier of the target's EP that the user will use for energy restoring when killed with full-effect Death Blessing. |
| `blessHalfDamage` | 0.5 |  | The multiplier of the target's HP that it takes when applied with half-effect Death Blessing. |
| `blessHalfRestore` | 0.25 |  | The multiplier of the target's EP that the user will use for energy restoring when killed with half-effect Death Blessing. |
| `blessMinimalEP` | 1 |  | The multiplier of the user's EP that the target needs to have below to take minimal effect of Death Blessing. |
| `blessMinimalDamage` | 0.25 |  | The multiplier of the target's HP that it takes when applied with minimal-effect Death Blessing. |
| `blessMinimalRestore` | 0.05 |  | The multiplier of the target's EP that the user will use for energy restoring when killed with minimal-effect Death Blessing. |
| `blessMPHeal` | 0.75 |  | The multiplier of the target's EP that the player will use to restore Magicule when killed with Death Blessing (the other half used for restoring Aura). |
| `cooldownBless` | 5 |  | The cooldown in second of the Death Bless mode. |

## `[MartialMaster]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 40,000 |  | Magicule Acquirement Cost. |
| `auraCost` | 100 |  | Aura Cost to activate Ultra Acceleration. |
| `damageMultiplier` | 1.5 |  | The melee/battlewill damage multiplier when using Secret. |
| `ultraDistance` | 15 |  | The Ultra Acceleration distance when activated. |
| `ultraDistanceMastered` | 20 |  | The Ultra Acceleration distance when activated with mastery. |
| `ultraDamage` | 15 |  | The bonus attack when using Ultra Acceleration on a target. |
| `ultraDamageMastered` | 75 |  | The bonus attack when using Ultra Acceleration on a target when mastered. |
| `chantSpeed` | 2 |  | The chant speed multiplier when toggled. |
| `meleeDodge` | 25 |  | Melee Dodge Chance when toggled. |
| `projectileDodge` | 100 |  | Projectile Dodge Chance when toggled. |
| `dodgeStrength` | 0.25 |  | The bonus dodge strength when toggled. |
| `dodgeInvulnerability` | 2 |  | The bonus dodge invulnerability when toggled. |
| `learningPoint` | 4 |  | The bonus number of bonus art-learning point to gain when toggled. |
| `masteryPoint` | 4 |  | The bonus number of bonus art-mastery point to gain when toggled. |

## `[Mathematician]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 40,000 |  | Magicule Acquirement Cost. |
| `analysisLevel` | 8 |  | The Analysis Level when activated. |
| `analysisLevelMastered` | 12 |  | The Analysis Level when activated with Mastery. |
| `analysisRadius` | 5 |  | The Analysis Radius when activated. |
| `analysisRadiusMastered` | 15 |  | The Analysis Radius when activated with Mastery. |
| `chantSpeed` | 2 |  | The chant speed multiplier when toggled. |
| `meleeDodge` | 10 |  | Melee Dodge Chance when toggled. |
| `projectileDodge` | 10 |  | Projectile Dodge Chance when toggled. |
| `dodgeNegation` | 50 |  | Dodge Negation Chance when toggled. |
| `critChance` | 75 |  | Critical Attack Chance when toggled. |
| `learningPoint` | 2 |  | The bonus number of learning point to gain when toggled. |
| `masteryPoint` | 2 |  | The bonus number of mastery point to gain when toggled. |

## `[Merciless]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 70,000 |  | Magicule Acquirement Cost. |
| `magiculeCostSteal` | 100 |  | Magicule Cost to activate Soul Steal. |
| `magiculeCostConsume` | 100 |  | Magicule Cost to activate Soul Consume. |
| `stealRadius` | 15 |  | The radius in block of the Soul Steal mode. |
| `stealHP` | 0.1 |  | The multiplier of HP that the target needs to have below to be affected by the Soul Steal mode. |
| `stealEP` | 0.1 |  | The multiplier of user's EP that the target needs to have below to be affected by the Soul Steal mode. |
| `stealFear` | 5 |  | The level of Fear that the target needs to have to be affected by the Soul Steal mode. |
| `drainDuration` | 100 |  | The duration in tick of the Soul Drain effect applied on targets with Soul Consume. |
| `drainLevel` | 1 |  | The level of the Soul Drain effect applied on targets with Soul Consume. |

## `[Murderer]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `magiculeCost` | 50 |  | Magicule Cost to activate. |
| `concealmentLevel` | 3 |  | The level of the Presence Conceal when hold down the skill. |
| `damageBoost` | 50 |  | The amount of bonus physical damage when hold down the skill. |
| `damageBoostMastery` | 150 |  | The amount of bonus physical damage when hold down the skill with mastery. |

## `[Musician]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 70,000 |  | Magicule Acquirement Cost. |
| `magiculeCostBlast` | 50 |  | Magicule Cost to activate Sonic Blast. |
| `magiculeCostWave` | 100 |  | Magicule Cost to activate Sonic Wave. |
| `magiculeCostRequiem` | 200 |  | Magicule Cost to activate Mind Requiem. |
| `blastRange` | 8 |  | The range in block of the Sonic Blast mode. |
| `blastRangeMastered` | 12 |  | The range in block of the Sonic Blast mode when mastered. |
| `blastDamage` | 75 |  | The damage of the Sonic Blast mode. |
| `blastDamageMastered` | 150 |  | The damage of the Sonic Blast mode when mastered. |
| `blastCooldown` | 1 |  | The cooldown in second of the Sonic Blast mode. |
| `waveRadius` | 5 |  | The radius in block of the Sonic Wave mode. |
| `waveDamage` | 40 |  | The damage of the Sonic Wave mode. |
| `waveDamageMastered` | 75 |  | The damage of the Sonic Wave mode when mastered. |
| `waveCooldown` | 1 |  | The cooldown in second of the Sonic Wave mode. |
| `requiemRange` | 10 |  | The range in block of the Mind Requiem mode. |
| `requiemDamage` | 150 |  | The damage of the Mind Requiem mode. |
| `requiemSpiritualDamage` | 100 |  | The spiritual damage of the Mind Requiem mode. |
| `requiemCooldown` | 3 |  | The cooldown in second of the Mind Requiem mode. |

## `[Observer]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 30,000 |  | Magicule Acquirement Cost. |
| `bonusSenseLevel` | 1 |  | The Bonus Presence Sense Level when activated. |
| `bonusSenseRadius` | 20 |  | The Bonus Presence Sense Radius when activated. |
| `meleeDodge` | 20 |  | Melee Dodge Chance when toggled. |
| `projectileDodge` | 100 |  | Projectile Dodge Chance when toggled. |

## `[Oppressor]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `magiculeCostRepel` | 50 |  | Magicule Cost to activate Repel. |
| `magiculeCostAttract` | 50 |  | Magicule Cost to activate Attract. |
| `magiculeCostOppress` | 350 |  | Magicule Cost to activate Oppress. |
| `magiculeCostBleve` | 1,000 |  | Magicule Cost to activate Bleve. |
| `magiculeCostFlicker` | 50 |  | Magicule Cost to activate Flicker. |
| `repelRange` | 10 |  | The max range in block of the Repel mode. |
| `attractRange` | 30 |  | The max range in block of the Attract mode. |
| `maxScale` | 10 |  | The max power scale of the Repel/Attract/Flicker mode. |
| `oppressRange` | 20 |  | The max range in block of the Oppress mode. |
| `oppressBurden` | 2 |  | The level of the Burden effect from the Oppress mode. |
| `oppressDuration` | 600 |  | The duration in tick of the Oppression effect from the Oppress mode. |
| `oppressDamage` | 100 |  | The oppress damage of the Oppress mode. |
| `oppressDamageMastered` | 200 |  | The oppress damage of the Oppress mode with mastery. |
| `oppressCooldown` | 10 |  | The cooldown in second of the Oppress mode. |
| `oppressCooldownMastered` | 5 |  | The cooldown in second of the Oppress mode with mastery. |
| `bleveRange` | 20 |  | The max range in block of the Bleve mode. |
| `bleveDamage` | 100 |  | The bleve damage of the Bleve mode. |
| `bleveDamageMastery` | 200 |  | The bleve damage of the Bleve mode with mastery. |
| `bleveCooldown` | 10 |  | The cooldown in second of the Bleve mode. |
| `bleveCooldownMastered` | 5 |  | The cooldown in second of the Bleve mode with mastery. |

## `[Predator]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `magiculeCostIsolation` | 200 |  | Magicule Cost to remove each harmful status effect with Isolation. |
| `predationRange` | 3 |  | The max range in block of the Predation Mode. |
| `predationDamage` | 10 |  | The attack damage of the Predation Mode. |
| `predationEPDrain` | 100 |  | The amount of EP that the user drains from target using the Predation Mode. |
| `predationSkillChance` | 10 |  | The chance to obtain skills from targets without killing them with the Predation Mode. |
| `predationSkillNumber` | 1 |  | The number of skills to gain from targets at a time without killing them with the Predation Mode. |
| `predationEPSteal` | 0.3 |  | The multiplier of the target's EP to be turned into the user's EP when killed with the Predation Mode. |
| `predationMagicCopy` | 0.5 |  | The chance multiplier for each of the target's learnable magic to be obtained by the user when killed with the Predation Mode. |
| `magiculeMultiplier` | 2 |  | The multiplier of magicule gained from dissolving items with the Isolation Mode. |
| `healthMultiplier` | 2 |  | The multiplier of health healed from dissolving items with the Isolation Mode.. |
| `isolationCooldown` | 5 |  | The cooldown in second of the Isolation Mode. |
| `isolationCooldownMastered` | 3 |  | The cooldown in second of the Isolation Mode when mastered. |
| `waterCapacity` | 3,000 |  | The bonus water capacity when the skill is acquired. |
| `lavaCapacity` | 3,000 |  | The bonus lava capacity when the skill is acquired. |

## `[Pride]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 100,000 |  | Magicule Acquirement Cost. |
| `copyChance` | 20 |  | The skill copy chance when attacked. |
| `copyChanceMastered` | 100 |  | The skill copy chance when attacked with mastery. |
| `copyMastery` | 0.0004 |  | The amount of mastery that Pride gains per Magicule Cost of the successfully copied ability. |
| `copyMasteryFail` | 0 |  | The multiplier of mastery that Pride gains per Magicule Cost of the failed ability. |
| `copyCooldown` | 45 |  | The cooldown in second that Pride gets per Mastery gained from successfully copying an ability. |
| `copyCooldownFail` | 4.5 |  | The cooldown in second that Pride gets per Mastery gained from failing to copy an ability. |

## `[Reaper]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 60,000 |  | Magicule Acquirement Cost. |
| `size` | 0.5 |  | The size when activated Recon. |
| `bonusSenseLevel` | 1 |  | The bonus Presence Sense Level when activated Recon. |
| `bonusSenseRadius` | 10 |  | The bonus Presence Sense Radius when activated Recon. |
| `bonusSenseRadiusMastered` | 20 |  | The bonus Presence Sense Radius when activated Recon with mastery. |
| `meleeDodge` | 15 |  | Melee Dodge Chance when toggled. |
| `meleeDodgeMastered` | 30 |  | Melee Dodge Chance when toggled with mastered. |
| `projectileDodge` | 15 |  | Projectile Dodge Chance when toggled. |
| `projectileDodgeMastered` | 30 |  | Projectile Dodge Chance when toggled with mastered. |
| `attackMultiplier` | 0.5 |  | The multiplier of size/aura/magicule when activated the Attack Mode. |
| `attackNumber` | 5 |  | The max number of clones when activated the Attack Mode. |
| `attackCooldown` | 10 |  | The cooldown in second of the Attack Mode. |
| `eaterBonusRange` | 3 |  | The bonus range in block of the Infinite Eater Mode. |
| `eaterEPSteal` | 0.5 |  | The multiplier of the target's EP to be turned into the user's EP when killed with the Infinite Eater Mode. |
| `eaterCooldown` | 10 |  | The cooldown in second of the Infinite Eater Mode. |
| `eaterCooldownMastered` | 5 |  | The cooldown in second of the Infinite Eater Mode when mastered. |

## `[Reflector]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 30,000 |  | Magicule Acquirement Cost. |
| `counterSpeedMultiplier` | 0 |  | The speed multiplier when activating the Echo Counter mode. |
| `counterSpeedMultiplierMastered` | 1 |  | The speed multiplier when activating the Echo Counter mode with mastery. |
| `counterDamageMultiplier` | 2.5 |  | The reflected damage when using Echo Counter. |
| `counterProjectileSpeedMultiplier` | 2 |  | The reflected projectile speed when using Echo Counter. |
| `counterCooldown` | 5 |  | The cooldown in second of the Echo Counter mode. |
| `maximumPoint` | 100 |  | The base maximum echo point to store. |
| `bonusPointMultiplier` | 0.001 |  | The multiplier of user's EP to be calculated for bonus echo point. |
| `reflectionDamageMultiplier` | 3 |  | The projectile damage multiplier when using Echo Reflection. |
| `reflectionDamageMultiplierMastered` | 5 |  | The projectile damage multiplier when using Echo Reflection with mastery. |

## `[Researcher]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 30,000 |  | Magicule Acquirement Cost. |
| `maxBonusLevel` | 1 |  | How many levels that Researcher can go above the maximum level of an enchantment. |
| `enchantmentBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:barrier_piercing", "tensura:breathing_support", "tensura:crushing", "tensura:energy_steal", "tensura:elemental_boost", "tensura:elemental_resistance", "tensura:energy_protection", "tensura:holy_weapon", "tensura:intangibility", "tensura:magic_weapon", "tensura:magicule_absorption", "tensura:magic_capacity", "tensura:magic_protection", "tensura:severance", "tensura:slotting", "tensura:soul_eater" ... (34 total) |  | Lists of enchantments that Researcher cannot learn or add. |
| `maxBonusBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:barrier_piercing", "tensura:breathing_support", "tensura:crushing", "tensura:energy_steal", "tensura:elemental_boost", "tensura:elemental_resistance", "tensura:energy_protection", "tensura:holy_weapon", "tensura:intangibility", "tensura:magic_weapon", "tensura:magicule_absorption", "tensura:magic_capacity", "tensura:magic_protection", "tensura:severance", "tensura:slotting", "tensura:soul_eater" ... (34 total) |  | Lists of enchantments that Researcher cannot learn or add above the enchantment's maximum level. |
| `curseChance` | 0.03 |  | The percentage chance to obtain a Curse Engraving per Engraving on the item. |

## `[Reverser]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 30,000 |  | Magicule Acquirement Cost. |
| `magiculeCostCurse` | 10,000 |  | Magicule Cost to reverse each Curses on the equipped items when mastered. |

## `[RoyalBeast]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 30,000 |  | Magicule Acquirement Cost. |
| `transformationDuration` | 3,600 |  | The duration in tick of the Transformation. |
| `transformationDurationMastered` | 7,200 |  | The duration in tick of the Transformation. |
| `cooldown` | 1,200 |  | The Cooldown in second after activation. |

## `[Seeker]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 40,000 |  | Magicule Acquirement Cost. |
| `analyzeRange` | 15 |  | The range in block of Analyze. |
| `analyzeTime` | 60 |  | The hold time in tick of Analyze to copy a Magic. |
| `analyzeTimeMastered` | 20 |  | The hold time in tick of Analyze to copy a Magic. |
| `chantSpeed` | 2 |  | The chant speed multiplier when toggled. |
| `learningPoint` | 4 |  | The bonus number of bonus magic-learning point to gain when toggled. |
| `masteryPoint` | 4 |  | The bonus number of bonus magic-mastery point to gain when toggled. |

## `[Seer]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 20,000 |  | Magicule Acquirement Cost. |
| `meleeDodge` | 25 |  | Melee Dodge Chance when toggled. |
| `meleeDodgeMastered` | 50 |  | Melee Dodge Chance when toggled with mastered. |
| `projectileDodge` | 25 |  | Projectile Dodge Chance when toggled. |
| `projectileDodgeMastered` | 50 |  | Projectile Dodge Chance when toggled with mastered. |
| `criticalChance` | 33 |  | Critical Attack Chance when toggled. |
| `criticalChanceMastered` | 50 |  | Critical Attack Chance when toggled with mastered. |
| `inputMultiplier` | 0.7 |  | The input damage multiplier when toggled. |
| `inputMultiplierMastered` | 0.5 |  | The input damage multiplier when toggled with mastery. |
| `visionDuration` | 200 |  | The duration in tick of the Future Vision effect. |
| `visionDurationMastered` | 400 |  | The duration in tick of the Future Vision effect when mastered. |
| `visionCooldown` | 10 |  | The cooldown in second of the Future Vision effect. |

## `[Severer]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 30,000 |  | Magicule Acquirement Cost. |
| `magiculeCostDummy` | 100 |  | Magicule Cost to activate Dummy Sword. |
| `magiculeCostStorm` | 2,000 |  | Magicule Cost to activate Blade Storm. |
| `magiculeCostSeverance` | 200 |  | Magicule Cost to activate Severance. |
| `engravingLevel` | 5 |  | The level of the Severance engraving of the Dummy Sword. |
| `engravingLevelMastered` | 10 |  | The level of the Severance engraving of the Dummy Sword when mastered. |
| `stormNumber` | 5 |  | The number of blades of the Blade Storm. |
| `stormNumberMastered` | 10 |  | The number of blades of the Blade Storm when mastered. |
| `stormCooldown` | 3 |  | The cooldown in second of the Blade Storm. |
| `stormCooldownMastered` | 1 |  | The cooldown in second of the Blade Storm when mastered. |
| `severanceLevel` | 1 |  | The level of the Severance effect when activating the Severance mode. |
| `severanceLevelMastered` | 2 |  | The level of the Severance effect when activating the Severance mode with mastery. |
| `severanceDuration` | 2,400 |  | The duration in tick of the Severance effect when activating the Severance mode. |

## `[ShadowStriker]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 60,000 |  | Magicule Acquirement Cost. |
| `magiculeCostKill` | 3,000 |  | Magicule Cost to activate Insta-kill. |
| `auraCost` | 100 |  | Aura Cost to activate Ultra Acceleration. |
| `chantSpeed` | 2 |  | The chant speed multiplier when toggled. |
| `dodgeStrength` | 0.25 |  | The bonus dodge strength when toggled. |
| `dodgeInvulnerability` | 2 |  | The bonus dodge invulnerability when toggled. |
| `ultraDistance` | 15 |  | The Ultra Acceleration distance when activated. |
| `ultraDistanceMastered` | 20 |  | The Ultra Acceleration distance when activated with mastery. |
| `ultraDamage` | 0 |  | The bonus attack when using Ultra Acceleration on a target. |
| `ultraDamageMastered` | 70 |  | The bonus attack when using Ultra Acceleration on a target when mastered. |
| `killDamage` | 500 |  | The amount of spiritual damage on target when using Insta-Kill. |
| `killDamageMastered` | 1,000 |  | The amount of spiritual damage on target when using Insta-Kill with mastery. |
| `killCooldown` | 10 |  | The cooldown in second of the Insta-Kill. |
| `killCooldownMastered` | 5 |  | The cooldown in second of the Insta-Kill when mastered. |
| `concealmentLevel` | 1 |  | The level of Presence Concealment when using Espionage. |
| `concealmentLevelMastered` | 2 |  | The level of Presence Concealment when using Espionage with mastery. |

## `[Sloth]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 100,000 |  | Magicule Acquirement Cost. |
| `magiculeCostDeprive` | 200 |  | Magicule Cost to activate Deprive. |
| `magiculeCostFallen` | 5,000 |  | Magicule Cost to activate Fallen Strike. |
| `deepRange` | 10 |  | The range in block of the Deep Hypno mode when used on a living target. |
| `deepRangeMagic` | 30 |  | The range in block of the Deep Hypno mode when used on a magic circle. |
| `deepDuration` | 100 |  | The base duration of the Drowsiness effect when using the Deep Hypno mode. |
| `deepDurationMastered` | 200 |  | The base duration of the Drowsiness effect when using the Deep Hypno mode with mastery. |
| `deepIncreaseTick` | 200 |  | The amount of tick activated needed to increase 1 level of Drowsiness when using the Deep Hypno. |
| `deepMagicCooldown` | 3 |  | The cooldown in second of the magic circle destroyed by Deep Hypno for the targeted caster. |
| `deepMagicCooldownMastered` | 5 |  | The cooldown in second of the magic circle destroyed by Deep Hypno for the targeted caster when mastered. |
| `fallenRadius` | 5 |  | The radius in block of the Fallen Hypno mode. |
| `fallenRadiusMastered` | 10 |  | The radius in block of the Fallen Hypno mode when mastered. |
| `fallenDuration` | 100 |  | The base duration of the Drowsiness effect when using the Fallen Hypno mode. |
| `fallenDurationMastered` | 200 |  | The base duration of the Drowsiness effect when using the Fallen Hypno mode with mastery. |
| `fallenIncreaseTick` | 200 |  | The amount of tick activated needed to increase 1 level of Drowsiness when using the Fallen Hypno. |
| `depriveRadius` | 5 |  | The radius in block of the Deprive mode. |
| `depriveRadiusMastered` | 15 |  | The radius in block of the Deprive mode when mastered. |
| `depriveEP` | 1,000 |  | The amount of EP to drain from targets when using Deprive. |
| `depriveEPMastered` | 0.003 |  | The multiplier of targets' EP to drain from targets when using Deprive with mastery. |
| `depriveSHP` | 10 |  | The amount of Spiritual damage dealt on targets when using Deprive. |
| `depriveSHPMastered` | 0.01 |  | The multiplier of Spiritual damage dealt on targets when using Deprive with mastery. |
| `restHP` | 10 |  | The amount of SHP to heal each second when using Rest. |
| `restHPMastered` | 0.01 |  | The multiplier of SHP to heal each second when using Rest with mastery. |
| `restSHP` | 10 |  | The amount of HP to heal each second when using Rest. |
| `restSHPMastered` | 0.01 |  | The multiplier of HP to heal each second when using Rest with mastery. |
| `restAP` | 10 |  | The multiplier of Aura Regeneration when using Rest. |
| `restMP` | 10 |  | The multiplier of Magicule Regeneration when using Rest. |
| `restAllyRadius` | 15 |  | The radius in block of ally heal area when using Rest. |
| `restAllyCost` | 1,000 |  | The Stored Magicule cost to heal each Ally. |
| `restAllyHP` | 50 |  | The amount of HP to heal Allies each second when using Rest. |
| `restAllySHP` | 10 |  | The amount of SHP to heal Allies each second when using Rest. |
| `restAllyEP` | 1,000 |  | The amount of Aura/Magicule each to heal Allies each second when using Rest. |
| `phantasmalSHP` | 10 |  | The amount of Spiritual damage dealt on targets when using Phantasmal Style. |
| `phantasmalSHPMastered` | 0.01 |  | The multiplier of Spiritual damage dealt on targets when using Phantasmal Style with mastery. |
| `fallStrikeRange` | 8 |  | The max range in block of Fallen Strike. |
| `fallStrikeSHP` | 500 |  | The amount of Spiritual Damage to deal on targets when using Fallen Strike. |
| `fallStrikeCooldown` | 10 |  | The cooldown in second of the Fallen Strike mode. |

## `[Sniper]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `magiculeCostWeapon` | 100 |  | Magicule Cost to activate Create Weapon. |
| `meleeDodge` | 10 |  | Melee Dodge Chance when toggled. |
| `projectileDodge` | 10 |  | Projectile Dodge Chance when toggled. |
| `dodgeNegation` | 50 |  | Dodge Negation Chance when toggled. |
| `presenceSense` | 2 |  | The level of Presence Sense when toggled. |
| `manipulationBoost` | 2 |  | The Spatial Damage Boost when activated Manipulation. |
| `warpShot` | 0.5 |  | The warp shot level when activated Spatial Manipulation's Warp Shot. |
| `energyCostPistol` | 100 |  | Magicule/Aura Cost to use the created pistol. |
| `physicalDamage` | 30 |  | The damage output of the Physical bullet. |
| `physicalCooldown` | 10 |  | The cooldown in tick of the Physical bullet. |
| `magicDamage` | 100 |  | The damage output of the Magic bullet. |
| `magicDamageMastered` | 200 |  | The damage output of the Magic bullet when mastered. |
| `magicCooldown` | 60 |  | The cooldown in tick of the Magic bullet. |
| `grenadeExplosion` | 4 |  | The explosion radius of the Grenade. |
| `grenadeCooldown` | 3 |  | The cooldown in second of the Grenade. |
| `grenadeCooldownMastered` | 1 |  | The cooldown in second of the Grenade when mastered. |

## `[Spearhead]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 60,000 |  | Magicule Acquirement Cost. |
| `allyRadius` | 20 |  | The radius in block to apply skill effect on Allies. |
| `allyAttack` | 10 |  | The bonus attack damage allies gain when activated (doubled with Mastery). |
| `allyArmor` | 5 |  | The bonus armor allies gain when activated (doubled with Mastery). |
| `allySpeed` | 0.02 |  | The bonus speed allies gain when activated (doubled with Mastery). |
| `allySwim` | 1 |  | The bonus swimming speed allies gain when activated (doubled with Mastery). |
| `fallenRange` | 20 |  | The range in block that the owner needs to be within fallen subordinates to gain their power. |

## `[Starved]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `magiculeCostCorrosion` | 200 |  | Magicule Cost to activate Corrosion. |
| `corrosionDuration` | 200 |  | The duration in tick of the Corrosion effect when attacking targets. |
| `corrosionLevel` | 2 |  | The level of the Corrosion effect when attacking targets. |
| `corrosionSpeedMultiplier` | 0.5 |  | Activation Speed Multiplier when activating the Corrosion Mode. |
| `corrosionRadius` | 5 |  | The radius in block of the Corrosion Mode. |
| `corrosionDamage` | 5 |  | The amount of damage dealt onto targets every 10 tick using the Corrosion Mode. |
| `corrosionEPSteal` | 0.2 |  | The EP multiplier of targets killed by the Corrosion Mode to be added to the user's Each of Aura and Magicule. |
| `dominationRadius` | 15 |  | The radius of the Spiritual Domination mode. |
| `waterCapacity` | 3,000 |  | The bonus water capacity when the skill is acquired. |
| `lavaCapacity` | 3,000 |  | The bonus lava capacity when the skill is acquired. |

## `[Suppressor]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 30,000 |  | Magicule Acquirement Cost. |
| `magiculeCostSwap` | 100 |  | Magicule Cost to activate Swap. |
| `magiculeCostBlockade` | 300 |  | Magicule Cost to activate Spatial Blockade. |
| `magiculeCostMotion` | 10 |  | Magicule Cost per block to use Spatial Motion. |
| `magiculeCostPortal` | 50 |  | Magicule Cost per block to use Spatial Motion per block using Portal. |
| `chantSpeed` | 2 |  | The chant speed multiplier when toggled. |
| `blockadeDuration` | 1,200 |  | The duration in tick of the Spatial Blockade when activated. |
| `swapRange` | 30 |  | The max range in block of the Swap mode. |
| `motionRange` | 30 |  | The max range in block of the Spatial Motion mode. |
| `motionRangeMastered` | 50 |  | The max range in block of the Spatial Motion mode when mastered. |
| `warpChargeTick` | 0 |  | The charge tick of the Teleport mode before warping any entity. |
| `motionCooldown` | 5 |  | The cooldown in second of the Spatial Motion mode. |
| `motionCooldownMastered` | 2 |  | The cooldown in second of the Spatial Motion mode when mastered. |

## `[Survivor]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 40,000 |  | Magicule Acquirement Cost. |

## `[Thrower]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 30,000 |  | Magicule Acquirement Cost. |
| `magiculeCost` | 50 |  | Magicule Cost to activate. |
| `entityThrow` | 3 |  | The base entity throw power. |
| `entityThrowManipulation` | 1 |  | The bonus entity throw power from Gravity Manipulation. |
| `entityThrowDomination` | 2 |  | The bonus entity throw power from Gravity Domination. |
| `airThrowDamage` | 30 |  | The base damage of thrown air. |
| `airThrowDamageMastered` | 50 |  | The base damage of thrown air when mastered. |
| `itemThrowDamage` | 50 |  | The base damage of thrown items. |
| `itemThrowDamageMastered` | 100 |  | The base damage of thrown items when mastered. |
| `itemThrowManipulation` | 2 |  | The bonus damage multiplier from Gravity Manipulation. |
| `itemThrowDomination` | 3 |  | The bonus damage multiplier from Gravity Domination. |
| `maxBreakableBlocks` | 10 |  | The maximum number of blocks that can be broken by throwing Mining Tools. |

## `[Traveler]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `magiculeCostMotion` | 5 |  | Magicule Cost per block to use Instant Motion. |
| `magiculeCostTeleport` | 5 |  | Magicule Cost per block to use Teleport per block. |
| `magiculeCostPortal` | 25 |  | Magicule Cost per block to use Teleport per block using Portal. |
| `magiculeCostArrow` | 150 |  | Magicule Cost to activate Stardust Arrow. |
| `auraCostArrow` | 150 |  | Aura Cost to activate Stardust Arrow. |
| `magiculeCostRain` | 5,000 |  | Magicule Cost to activate Stardust Rain. |
| `auraCostRain` | 5,000 |  | Aura Cost to activate Stardust Rain. |
| `manipulationBoost` | 2 |  | The Spatial Damage Boost when activated Manipulation. |
| `warpShot` | 0.5 |  | The warp shot level when activated Spatial Manipulation's Warp Shot. |
| `motionRange` | 200 |  | The max range in block of the Instant Motion mode. |
| `motionCooldown` | 5 |  | The cooldown in second of the Instant Motion mode. |
| `motionCooldownMastered` | 2 |  | The cooldown in second of the Instant Motion mode when mastered. |
| `warpChargeTick` | 0 |  | The charge tick of the Teleport mode before warping any entity. |
| `teleportCooldown` | 10 |  | The cooldown in second of the Teleport mode. |
| `teleportCooldownMastered` | 5 |  | The cooldown in second of the Teleport mode when mastered. |
| `arrowDamage` | 30 |  | The damage of an arrow when using Stardust Arrow. |
| `rainRange` | 20 |  | The max range in block of Stardust Rain. |
| `rainNumber` | 12 |  | The number of arrows in Stardust Rain. |
| `rainDamage` | 30 |  | The damage of an arrow when using Stardust Rain. |
| `rainCooldown` | 5 |  | The cooldown for Stardust Rain. |
| `rainCooldownMastered` | 4 |  | The cooldown for Stardust Rain when mastered. |

## `[Tuner]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `hpMultiplier` | 0.25 |  | The multiplier of HP that the user needs to below to activate Unexpected Result. |
| `bonusAttack` | 30 |  | The bonus attack damage when activated Unexpected Result with mastery (doubled with Mastery). |
| `bonusAttackSpeed` | 0.2 |  | The bonus attack speed when activated Unexpected Result with mastery (doubled with Mastery). |
| `bonusSpeed` | 0.04 |  | The bonus speed when activated Unexpected Result with mastery (doubled with Mastery). |
| `bonusSwim` | 1 |  | The bonus swim speed when activated Unexpected Result with mastery (doubled with Mastery). |
| `bonusMeleeDodge` | 15 |  | The bonus melee dodge chance when activated Unexpected Result with mastery (doubled with Mastery). |
| `bonusProjectileDodge` | 15 |  | The bonus projectile dodge chance when activated Unexpected Result with mastery (doubled with Mastery). |
| `hpRevive` | 1 |  | The multiplier of HP that the user gets when revived by the skill. |
| `shpRevive` | 1 |  | The multiplier of SHP that the user gets when revived by the skill. |
| `epRevive` | 0.5 |  | The multiplier of Aura/Magicule that the user gets when revived by the skill. |
| `epReviveMastered` | 0.75 |  | The multiplier of Aura/Magicule that the user gets when revived by the skill with mastery. |
| `deathReset` | 1,200 |  | The timer in tick till the next death count reset. |

## `[Unyielding]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 60,000 |  | Magicule Acquirement Cost. |
| `magiculeBackupCost` | 0.25 |  | Magicule Cost multiplier of the user's maximum Magicule required to spawn a backup. |
| `unyieldingRadius` | 30 |  | The radius in block that subordinates need to stay within the user to increase Unyielding point. |
| `unyieldingPointGain` | 1 |  | The number of Unyielding points that a subordinate gains every 5 seconds while in required radius. |
| `unyieldingPointGainMastered` | 2 |  | The number of Unyielding points that a subordinate gains every 5 seconds while in required radius when mastered. |
| `unyieldingPointEP` | 120 |  | The number of Unyielding points needed to gain each 10% of the EP of a fallen subordinate. |
| `unyieldingPointSkill` | 120 |  | The number of Unyielding points needed to gain skills from a fallen subordinate. |
| `unyieldingPointSkillUnique` | 600 |  | The number of Unyielding points needed to gain Unique skills from a fallen subordinate. |
| `backupCooldown` | 5 |  | The cooldown in second to spawn/swap a backup. |
| `backupCooldownMastered` | 3 |  | The cooldown in second to spawn/swap a backup when mastered. |

## `[Usurper]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 50,000 |  | Magicule Acquirement Cost. |
| `magiculeCostRob` | 1,000 |  | Magicule Cost to activate Rob. |
| `magiculeCostCopy` | 1,000 |  | Magicule Cost to activate Copy. |
| `magiculeCostTakeover` | 5,000 |  | Magicule Cost to activate Force Takeover. |
| `epDrain` | 0.01 |  | The multiplier of the target's EP to drain when attacked by the user. |
| `robSuccess` | 25 |  | The percentage chance to rob successfully. |
| `robSuccessMastered` | 50 |  | The percentage chance to rob successfully when mastered. |
| `robMastery` | 0.5 |  | The multiplier of max mastery that the robbed skill gains. |
| `robCooldown` | 10 |  | The cooldown in second of the Rob mode. |
| `copySuccess` | 25 |  | The percentage chance to copy successfully. |
| `copySuccessMastered` | 50 |  | The percentage chance to copy successfully when mastered. |
| `copyMastery` | 0.5 |  | The multiplier of max mastery that the copied skill gains. |
| `copyCooldown` | 10 |  | The cooldown in second of the Copy mode. |
| `takeoverEP` | 0.75 |  | The multiplier of the user's EP that the targeted spirit's owner needs to be higher to not be affected by Takeover. |
| `takeoverDuration` | 6,000 |  | The duration in tick of the Takeover effect on the controlled spirit (-1 = permanent). |
| `takeoverDurationMastered` | 12,000 |  | The duration in tick of the Takeover effect on the controlled spirit when mastered (-1 = permanent). |
| `takeoverCooldown` | 10 |  | The cooldown in second of the Force Takeover mode. |

## `[Villain]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 60,000 |  | Magicule Acquirement Cost. |
| `magiculeCostHaki` | 25 |  | Magicule Cost to activate Hero Haki. |
| `magiculeCostCharisma` | 200 |  | Magicule Cost to activate Hero's Charisma. |
| `intimidationRadius` | 15 |  | The radius in block of the Villain's Intimidation's effect on allies. |
| `controlRadius` | 10 |  | The radius in block of the Villain's Charisma's effect. |
| `controlDuration` | 2,400 |  | The duration in tick of the Mind Control effect when activating Villain's Charisma (-1 = permanent). |
| `controlResistedDuration` | 1,200 |  | The duration in tick of the Mind Control effect when activating Villain's Charisma while the target has Spiritual Attack Resistance (-1 = permanent). |
| `majinPercentage` | 100 |  | The percentage to become Majin when dying of Magicule Poison while having this skill. |
| `auraPercentage` | 1.5 |  | The bonus Aura percentage the user gains when toggled on. |
| `magiculePercentage` | 1.5 |  | The bonus Magicule percentage the user gains when toggled on. |
| `dodgeNegateChance` | 0.25 |  | The bonus Dodge negate chance the user gains when toggled on. |

## `[Wrath]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 100,000 |  | Magicule Acquirement Cost. |
| `magiculeCostEnrage` | 100 |  | Magicule Cost to activate Enrage. |
| `breederMultiplier` | 0.02 |  | The multiplier of the user's maximum magicule to gain every 100 ticks. |
| `breederUnderChance` | 3 |  | The chance to gain an Rampage level when the user is under maximum Magicule (doubled with mastery). |
| `breederAboveChance` | 6 |  | The chance to gain an Rampage level when the user is above maximum Magicule (doubled with mastery). |
| `maxRampage` | 10 |  | The maximum level of Rampage the user can get from using Magicule Breader. |
| `maxRampageMastered` | 20 |  | The maximum level of Rampage the user can get from using Magicule Breader when mastered. |
| `breederDuration` | 600 |  | The duration in tick of the Rampage effect when using Magicule Breader. |
| `rampageArmor` | 5 |  | The bonus armor points each level of Rampage on the user when using Magicule Breader. |
| `rampageAttack` | 30 |  | The bonus attack points each level of Rampage on the user when using Magicule Breader. |
| `rampageAttackSpeed` | 0.02 |  | The bonus attack speed each level of Rampage on the user when using Magicule Breader. |
| `rampageSpeed` | 0.01 |  | The bonus speed points each level of Rampage on the user when using Magicule Breader. |
| `rampageKnockbackResistance` | 0.1 |  | The bonus knockback resistance each level of Rampage on the user when using Magicule Breader. |
| `enrageRadius` | 7 |  | The radius in block of the Enrage mode. |
| `enrageDuration` | 400 |  | The base duration of the Rampage effect when using the Enrage mode. |
| `enrageIncreaseTick` | 200 |  | The amount of tick activated needed to increase 1 level of Rampage when using the Enrage. |
