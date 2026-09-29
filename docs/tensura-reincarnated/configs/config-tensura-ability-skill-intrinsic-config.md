# `config/tensura/ability/skill/intrinsic_config.toml`

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Configs](index.md)</small>

## `[AbsorbDissolve]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeMultiplier` | 1 |  | The multiplier of magicule gained from dissolving items. |
| `healthMultiplier` | 1 |  | The multiplier of health healed from dissolving items. |
| `bonusHP` | 5 |  | The bonus max HP that Slime players can get from each Slime Core used to increase their size. |
| `bonusSize` | 0.1 |  | The bonus max size that Slime players can get from each Slime Core used to increase their size. |
| `maxSize` | 0.75 |  | The max bonus size that Slime players can get from consuming Slime Cores. |

## `[BeastTransformation]`

| Option | Default | Range | Description |
|---|---|---|---|
| `transformationDuration` | 3,600 |  | The duration in tick of the Transformation. |
| `transformationDurationMastered` | 7,200 |  | The duration in tick of the Transformation. |
| `cooldown` | 1,200 |  | The Cooldown in second after activation. |

## `[BloodMist]`

| Option | Default | Range | Description |
|---|---|---|---|
| `rayAcquirement` | 500,000 |  | EP Requirement to use Blood Ray. |
| `magiculeCost` | 500 |  | Magicule Cost to activate the Default Mode. |
| `rayMagiculeCost` | 10,000 |  | Magicule Cost to activate Blood Ray. |
| `mistRange` | 10 |  | The spawn range in block of the blood mist. |
| `mistDamage` | 10 |  | The damage per second of the blood mist. |
| `mistRadius` | 5 |  | The radius of the blood mist. |
| `mistCooldown` | 4 |  | The cooldown of the blood mist (halved with mastery). |
| `rayRange` | 40 |  | The spawn range in block of the blood ray. |
| `rayDamage` | 50 |  | The damage per second of the blood ray. |
| `rayHPCost` | 10 |  | How much HP the user loses every 10 tick of using blood ray. |

## `[BodyArmor]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 50 |  | Magicule Cost to activate. |

## `[Charm]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 80 |  | Base Magicule Cost to activate. |
| `cooldown` | 5 |  | The Cooldown in second after activation. |
| `range` | 5 |  | The range in block for targeting an entity. |
| `fullMultiplier` | 0.25 |  | The multiplier of the user's EP that the target's EP needs to be below for full mind control. |
| `neutralMultiplier` | 0.5 |  | The multiplier of the user's EP that the target's EP needs to be below to become neutral toward the user. |
| `resistedMultiplier` | 0.2 |  | The multiplier of the user's EP that the target's Spiritual Attack Resistance reduces onto the EP requirement. |
| `controlDuration` | 6,000 |  | The duration in tick of the Mind Control effect (-1 = permanent). |
| `controlDurationMastered` | 12,000 |  | The duration in tick of the Mind Control effect when mastered (-1 = permanent). |

## `[DivineKiRelease]`

| Option | Default | Range | Description |
|---|---|---|---|
| `battlewillDamage` | 50 |  | The bonus battlewill damage when toggled. |
| `battlewillDamageMastered` | 100 |  | The bonus battlewill damage when toggled with mastery. |
| `durabilityBreak` | 3 |  | The multiplier of the durability break of the target's equipments when damaged by user's physical/battlewill attack. |
| `durabilityBreakMastered` | 5 |  | The multiplier of the durability break of the target's equipments when damaged by user's physical/battlewill attack when mastered. |

## `[ElementalTransform]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 30 |  | Magicule Cost to activate. |
| `speedMultiplier` | 0.5 |  | The movement speed multiplier of the user when activated. |
| `spiritLevel` | 2 |  | The level of Spiritual Magic the user learns upon obtaining this skill. |
| `radius` | 5 |  | The radius in block of the elemental effect upon targets around the user. |
| `damage` | 2 |  | The elemental damage amount per second on targets when activated. |
| `effectDuration` | 160 |  | The duration in tick of the status effects on targets when activated. |

## `[DragonEar]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 0 |  | Magicule Cost to activate. |
| `bonusRadius` | 30 |  | The bonus Presence Sense Radius when activated. |

## `[DragonEye]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 0 |  | Magicule Cost to activate. |
| `maxZoom` | 50 |  | The Max Zoom Multiplier. |
| `maxSenseRadius` | 100 |  | The Max Bonus Presence Sense Radius when activated. |
| `senseLevel` | 1 |  | The Bonus Presence Sense Level when activated. |
| `senseLevelMastered` | 2 |  | The Bonus Presence Sense Level when activated with Mastery. |

## `[DragonMode]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 0 |  | Magicule Cost to activate. |
| `transformationDuration` | 3,600 |  | The duration in tick of the Transformation. |
| `transformationDurationMastered` | 7,200 |  | The duration in tick of the Transformation. |
| `cooldown` | 1,200 |  | The Cooldown in second after activation. |

## `[DragonSkin]`

| Option | Default | Range | Description |
|---|---|---|---|
| `hihiirokaneEP` | 800,000 |  | The amount of EP needed for Hihi'irokane Armor's stats. |
| `adamantiteEP` | 400,000 |  | The amount of EP needed for Adamantite Armor's stats. |
| `magisteelEP` | 50,000 |  | The amount of EP needed for Pure Magisteel Armor's stats. |

## `[Drain]`

| Option | Default | Range | Description |
|---|---|---|---|
| `range` | 3 |  | The activation range of the blood drain. |
| `drainAmount` | 6 |  | The amount of HP that the user will drain from the target. |
| `temporaryDuration` | 80 |  | The duration in second that the temporary obtained skill will stay with the user. |

## `[EyeOfTruth]`

| Option | Default | Range | Description |
|---|---|---|---|
| `senseLevel` | 4 |  | The level Presence Sense when activated. |

## `[FlameBreath]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 30 |  | Base Magicule Cost to activate. |
| `damage` | 8 |  | The damage each second of the Flame Breath. |
| `damageMastered` | 16 |  | The damage each second of the Flame Breath when mastered. |

## `[Giantification]`

| Option | Default | Range | Description |
|---|---|---|---|
| `damage` | 6 |  | The attack damage buff the user gains when activated. |
| `maxSize` | 3 |  | The maximum size change in block when activated. |
| `minSize` | -1 |  | The minimum size change in block when activated with Mastery. |
| `rangeMultiplier` | 1.5 |  | The interaction range multiplier to apply with size when activated. |

## `[IceBreath]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 30 |  | Base Magicule Cost to activate. |
| `damage` | 8 |  | The damage each second of the Ice Breath. |
| `damageMastered` | 16 |  | The damage each second of the Ice Breath when mastered. |

## `[OgreBerserker]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 5,000 |  | Magicule Cost to activate. |
| `transformationDuration` | 3,600 |  | The duration in tick of the Transformation. |
| `transformationDurationMastered` | 7,200 |  | The duration in tick of the Transformation. |
| `cooldown` | 600 |  | The Cooldown in second after activation. |

## `[ParalysisBreath]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 50 |  | Base Magicule Cost to activate (halved when mastered). |
| `damage` | 2 |  | The damage each second of the Paralysis Breath. |
| `paralysisLevel` | 3 |  | The level of the Paralysis effect when applied. |
| `paralysisDuration` | 200 |  | The duration in tick of the Paralysis effect when applied. |

## `[PoisonousBreath]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 100 |  | Base Magicule Cost to activate (halved when mastered). |
| `damage` | 15 |  | The damage each second of the Poison Breath. |
| `damageMastered` | 30 |  | The damage each second of the Poison Breath when mastered. |
| `poisonLevel` | 1 |  | The level of the Fatal Poison effect when applied. |
| `poisonDuration` | 200 |  | The duration in tick of the Fatal Poison effect when applied. |

## `[Possession]`

| Option | Default | Range | Description |
|---|---|---|---|
| `range` | 5 |  | The possession range in block. |
| `hpMultiplier` | 0.1 |  | The multiplier of the maximum Health that a target needs to be under to be possessed. |
| `shpMultiplier` | 0.1 |  | The multiplier of the maximum Spiritual Health that a target needs to be under to be possessed. |
| `epMultiplier` | 0.25 |  | The multiplier of the user's maximum EP that a target needs to be under to be possessed. |
| `resistanceMultiplier` | 0.5 |  | The multiplier of the possession requirement multipliers when the target has Spiritual Attack Resistance. |
| `maxHealth` | 1,000 |  | The maximum amount of HP the user can get from possessing an entity. |
| `maxAttack` | 100 |  | The maximum amount of Attack Damage the user can get from possessing an entity. |
| `bodyDespawnTick` | 300 |  | The number of seconds that Possession Bodies will despawn. (0 = instant despawn, -1 = doesn't despawn) |

## `[ScaleArmor]`

| Option | Default | Range | Description |
|---|---|---|---|
| `swimMultiplier` | 2 |  | The swimming speed multiplier that the user gains when toggled. |
| `armorPoint` | 6 |  | The number of armor points that the user gains when toggled. |

## `[ThunderBreath]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 50 |  | Base Magicule Cost to activate (halved when mastered). |
| `damage` | 10 |  | The damage each second of the Poison Breath. |
| `damageMastered` | 20 |  | The damage each second of the Poison Breath when mastered. |

## `[Titanification]`

| Option | Default | Range | Description |
|---|---|---|---|
| `damage` | 60 |  | The attack damage buff the user gains when activated. |
| `armor` | 20 |  | The armor buff the user gains when activated. |
| `maxSize` | 6 |  | The maximum size change in block when activated. |
| `minSize` | 0 |  | The minimum size change in block when activated with Mastery. |
| `rangeMultiplier` | 1.75 |  | The interaction range multiplier to apply with size when activated. |
| `duration` | 120 |  | The duration in second that Titanification effect lasts once activated. |
| `cooldown` | 300 |  | The cooldown in second once the effect runs out or deactivated. |

## `[UltrasonicWaves]`

| Option | Default | Range | Description |
|---|---|---|---|
| `magiculeCost` | 30 |  | Magicule Cost to activate . |
| `auditoryDuration` | 200 |  | The duration in tick of the Auditory Sense effect when activated. |
| `sonicRange` | 8 |  | The range in block of the Sonic Waves mode. |
| `sonicDamage` | 8 |  | The damage of the Sonic Waves when hit a target. |
| `sonicCooldown` | 3 |  | The cooldown in second after activating Sonic Waves (halved with mastery). |

## `[Unpredictability]`

| Option | Default | Range | Description |
|---|---|---|---|
| `negateDodge` | 100 |  | The bonus chance to negate dodging when activated. |

## `[WaterBreathing]`

| Option | Default | Range | Description |
|---|---|---|---|
| `waterBreathLevel` | 3 |  | The level of the Water Breathing effect when activated. |
