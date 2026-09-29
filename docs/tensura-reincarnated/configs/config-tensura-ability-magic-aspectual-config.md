# `config/tensura/ability/magic/aspectual_config.toml`

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Configs](index.md)</small>

## `[MagicWall]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 120 |  | Cast time in tick. |
| `castTimeMastered` | 100 |  | Cast time in tick when mastered. |
| `magiculeCost` | 400 |  | Magicule Cost to cast. |
| `distance` | 4 |  | The distance in block from the caster to create the magic wall. |
| `width` | 4 |  | The width radius of the magic wall. |
| `speedMultiplier` | 0.5 |  | The speed multiplier of the targets going through the magic wall. |
| `magicProjectileReduction` | 30 |  | The damage reduction of the magic projectiles going through the magic wall. |
| `magicProjectileReductionMastered` | 50 |  | The damage reduction of the magic projectiles going through the magic wall when mastered. |
| `wallDuration` | 200 |  | The duration in tick of the Magic Wall. |
| `wallDurationMastered` | 500 |  | The duration in tick of the Magic Wall when mastered. |

## `[MagicBarrier]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 160 |  | Cast time in tick. |
| `magiculeMultiplierCost` | 0.05 |  | The multiplier of the caster's Max Magicule to be calculated for the Magicule Cost to cast. |
| `minCost` | 2,000 |  | Minimum Magicule Cost to cast. |
| `barrierThreshold` | 0.1667 |  | The multiplier of the caster's HP to be the magic damage threshold for the Barrier effect. |
| `belowReduction` | 0.1667 |  | The multiplier of the caster's HP to be reduced from the magic damage taken when the damage is below the threshold. |
| `aboveReduction` | 0.0833 |  | The multiplier of the caster's HP to be reduced from the magic damage taken when the damage is above the threshold. |
| `barrierThresholdMastered` | 0.2 |  | The multiplier of the caster's HP to be the magic damage threshold for the Barrier effect when mastered. |
| `belowReductionMastered` | 0.2 |  | The multiplier of the caster's HP to be reduced from the magic damage taken when the damage is below the threshold when mastered. |
| `aboveReductionMastered` | 0.1 |  | The multiplier of the caster's HP to be reduced from the magic damage taken when the damage is above the threshold when mastered. |
| `barrierDuration` | 200 |  | The duration in tick of the Barrier effect. |
| `barrierDurationMastered` | 400 |  | The duration in tick of the Barrier effect when mastered. |

## `[Barrier]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 160 |  | Cast time in tick. |
| `magiculeMultiplierCost` | 0.05 |  | The multiplier of the caster's Max Magicule to be calculated for the Magicule Cost to cast. |
| `minCost` | 2,000 |  | Minimum Magicule Cost to cast. |
| `barrierThreshold` | 0.1667 |  | The multiplier of the caster's HP to be the physical damage threshold for the Barrier effect. |
| `belowReduction` | 0.1667 |  | The multiplier of the caster's HP to be reduced from the physical damage taken when the damage is below the threshold. |
| `aboveReduction` | 0.0833 |  | The multiplier of the caster's HP to be reduced from the physical damage taken when the damage is above the threshold. |
| `barrierThresholdMastered` | 0.2 |  | The multiplier of the caster's HP to be the physical damage threshold for the Barrier effect when mastered. |
| `belowReductionMastered` | 0.2 |  | The multiplier of the caster's HP to be reduced from the physical damage taken when the damage is below the threshold when mastered. |
| `aboveReductionMastered` | 0.1 |  | The multiplier of the caster's HP to be reduced from the physical damage taken when the damage is above the threshold when mastered. |
| `barrierDuration` | 200 |  | The duration in tick of the Barrier effect. |
| `barrierDurationMastered` | 400 |  | The duration in tick of the Barrier effect when mastered. |

## `[ReinforcedBarrier]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 160 |  | Cast time in tick. |
| `magiculeMultiplierCost` | 0.05 |  | The multiplier of the caster's Max Magicule to be calculated for the Magicule Cost to cast. |
| `minCost` | 5,000 |  | Minimum Magicule Cost to cast. |
| `barrierThreshold` | 0.2 |  | The multiplier of the caster's HP to be the damage threshold for the Barrier effect. |
| `belowReduction` | 0.2 |  | The multiplier of the caster's HP to be reduced from the damage taken when the damage is below the threshold. |
| `aboveReduction` | 0.1 |  | The multiplier of the caster's HP to be reduced from the damage taken when the damage is above the threshold. |
| `barrierDuration` | 600 |  | The duration in tick of the Barrier effect. |
| `barrierThresholdMagic` | 0.25 |  | The multiplier of the caster's HP to be the magic damage threshold for the Barrier effect of the Magic Defense mode. |
| `belowReductionMagic` | 0.25 |  | The multiplier of the caster's HP to be reduced from the magic damage taken when the damage is below the threshold with the Magic Defense mode. |
| `aboveReductionMagic` | 0.125 |  | The multiplier of the caster's HP to be reduced from the magic damage taken when the damage is above the threshold with the Magic Defense mode. |
| `barrierDurationMagic` | 300 |  | The duration in tick of the Barrier effect of the Magic Defense mode. |
| `cooldownMagic` | 45 |  | The cooldown in second of the Magic Defense mode. |
| `barrierThresholdPhysical` | 0.25 |  | The multiplier of the caster's HP to be the physical damage threshold for the Barrier effect of the Physical Defense mode. |
| `belowReductionPhysical` | 0.25 |  | The multiplier of the caster's HP to be reduced from the physical damage taken when the damage is below the threshold with the Physical Defense mode. |
| `aboveReductionPhysical` | 0.125 |  | The multiplier of the caster's HP to be reduced from the physical damage taken when the damage is above the threshold with the Physical Defense mode. |
| `barrierDurationPhysical` | 300 |  | The duration in tick of the Barrier effect of the Physical Defense mode. |
| `cooldownPhysical` | 45 |  | The cooldown in second of the Physical Defense mode. |

## `[AntiShockArea]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 220 |  | Cast time in tick. |
| `magiculeCost` | 15,000 |  | Magicule Cost to cast. |
| `radius` | 7.5 |  | The radius in block of the barrier. |
| `radiusMastered` | 15 |  | The radius in block of the barrier when mastered. |
| `duration` | 2,400 |  | The duration in tick of the barrier. |
| `durationMastered` | 3,600 |  | The duration in tick of the barrier when mastered. |
| `antiShockDamage` | 1 |  | The amount of physical damage that attacks reduce to when applied inside the barrier. |
| `cooldown` | 5 |  | The cooldown in second to create a barrier. |
| `cooldownMastered` | 3 |  | The cooldown in second to create a barrier when mastered. |

## `[AntiMagicArea]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 220 |  | Cast time in tick. |
| `magiculeCost` | 20,000 |  | Magicule Cost to cast. |
| `radius` | 10 |  | The radius in block of the barrier. |
| `radiusMastered` | 25 |  | The radius in block of the barrier when mastered. |
| `duration` | 1,200 |  | The duration in tick of the barrier. |
| `cooldown` | 5 |  | The cooldown in second to create a barrier. |
| `cooldownMastered` | 3 |  | The cooldown in second to create a barrier when mastered. |

## `[EarthLock]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 40 |  | Cast time in tick. |
| `magiculeCost` | 100 |  | Magicule Cost to cast. |
| `range` | 10 |  | The range in block of the magic. |
| `radius` | 2 |  | The radius in block of where the caster targeted to be turned into solid version. |
| `knockbackResistance` | 0.2 |  | The amount of knockback resistance that the caster gains when using the Self-Lock mode when mastered. |
| `knockbackResistanceDuration` | 240 |  | The duration in tick of knockback resistance that the caster gains when using the Self-Lock mode when mastered. |

## `[Liquidize]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 80 |  | Cast time in tick. |
| `castTimeMastered` | 60 |  | Cast time in tick when mastered. |
| `magiculeCost` | 250 |  | Magicule Cost to cast. |
| `range` | 10 |  | The range in block of the magic. |
| `radius` | 2 |  | The radius in block of where the caster targeted to be turned into loose soil. |

## `[EarthWall]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 40 |  | Cast time in tick. |
| `castTimeMastered` | 20 |  | Cast time in tick when mastered. |
| `magiculeCost` | 1,000 |  | Magicule Cost to cast. |
| `range` | 20 |  | The range in block of the magic. |
| `wallDuration` | 1,200 |  | The duration in tick of the Earth Wall. |

## `[MudHand]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 80 |  | Cast time in tick. |
| `magiculeCost` | 5,000 |  | Magicule Cost to cast. |
| `range` | 20 |  | The range in block of the magic. |
| `bindLevel` | 10 |  | The level of Movement Interference to apply on target when casted (-10% speed each level). |
| `slowLevel` | 2 |  | The level of the Slowness effect to apply on target when the spell stops while mastered. |
| `slowDuration` | 100 |  | The duration in tick of the Slowness effect to apply on target when the spell stops while mastered. |
| `maxHold` | 100 |  | The max number of ticks that the caster can hold magic down. |
| `maxHoldMastered` | 200 |  | The max number of ticks that the caster can hold magic down when mastered. |

## `[StoneShot]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 80 |  | Cast time in tick. |
| `magiculeCost` | 45,000 |  | Magicule Cost to cast. |
| `stoneNumber` | 3 |  | The number of stones to shoot each usage. |
| `magicDamage` | 150 |  | The magic damage of each stone shot. |
| `earthDamage` | 50 |  | The earth damage of each stone shot. |
| `cooldown` | 3 |  | The cooldown in second of the magic in the default mode. |
| `cooldownMastered` | 1 |  | The cooldown in second of the magic in the default mode when mastered. |

## `[MudSpears]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 80 |  | Cast time in tick. |
| `castTimeMudHand` | 40 |  | Cast time in tick when Mud Hand is already casted. |
| `magiculeCost` | 70,000 |  | Magicule Cost to cast. |
| `range` | 20 |  | The range in block of the magic. |
| `magicDamage` | 250 |  | The magic damage of each mud spike. |
| `magicDamageBonus` | 50 |  | The bonus magic damage of each mud spike if Mud Hand is already casted. |
| `earthDamage` | 50 |  | The earth damage of each mud spike. |
| `spreadDamage` | 20 |  | The earth damage of each mud spike casted from Spread Mode. |
| `spreadDuration` | 600 |  | The duration in tick of each mud spike casted from Spread Mode. |
| `spreadRadius` | 5 |  | The radius in block of the Spread Mode. |
| `cooldown` | 3 |  | The cooldown in second of the magic in the default mode. |
| `cooldownMastered` | 1 |  | The cooldown in second of the magic in the default mode when mastered. |

## `[Reinforcement]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `magiculeCost` | 4,000 |  | Magicule Cost to cast. |
| `range` | 10 |  | The range in block of the magic. |
| `reinforcementLevel` | 3 |  | The level of the Reinforcement effect. |
| `reinforcementDuration` | 2,400 |  | The duration in tick of the Strength effect. |
| `reinforcementDurationMastered` | 12,000 |  | The duration in tick of the Strength effect when mastered. |

## `[Strength]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `magiculeCost` | 4,000 |  | Magicule Cost to cast. |
| `range` | 10 |  | The range in block of the magic. |
| `strengthLevel` | 3 |  | The level of the Strength effect. |
| `strengthDuration` | 2,400 |  | The duration in tick of the Strength effect. |
| `strengthDurationMastered` | 12,000 |  | The duration in tick of the Strength effect when mastered. |

## `[Agility]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `magiculeCost` | 3,000 |  | Magicule Cost to cast. |
| `range` | 10 |  | The range in block of the magic. |
| `speedLevel` | 3 |  | The level of the Speed effect. |
| `speedDuration` | 2,400 |  | The duration in tick of the Speed effect. |
| `speedDurationMastered` | 12,000 |  | The duration in tick of the Speed effect when mastered. |
| `hasteLevel` | 3 |  | The level of the Haste effect. |
| `hasteDuration` | 2,400 |  | The duration in tick of the Haste Boost effect. |
| `hasteDurationMastered` | 12,000 |  | The duration in tick of the Haste Boost effect when mastered. |

## `[Protection]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `magiculeCost` | 4,000 |  | Magicule Cost to cast. |
| `range` | 10 |  | The range in block of the magic. |
| `protectionArmor` | 20 |  | The armor boost of the Protection effect per level. |
| `protectionLevel` | 1 |  | The level of the Protection effect. |
| `protectionDuration` | 2,400 |  | The duration in tick of the Protection effect. |
| `protectionDurationMastered` | 12,000 |  | The duration in tick of the Protection effect when mastered. |

## `[Explosion]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTimeLevel` | 50 |  | Cast time in tick per level. |
| `magiculeCost` | 10,000 |  | Magicule Cost multiplier to add up each level (level 1 = 10,000 and level 2 equals 20,000 for a total cost of 30,000. Level 3 total cost would be 60,000, etc.) |
| `range` | 64 |  | The range in block of the explosion mode. |
| `rangeTrap` | 20 |  | The range in block of the Trap mode. |
| `blastRadius` | 5 |  | The radius in block of the explosion each level. |
| `magicDamage` | 100 |  | The magic damage of the explosion each level. |
| `minLevel` | 3 |  | The min level the explosion mode has to reach to be casted. |
| `maxLevel` | 5 |  | The max level the explosion mode can reach. |
| `maxLevelMastered` | 10 |  | The max level the explosion mode can reach when mastered. |
| `maxLevelTrap` | 3 |  | The max level the Trap mode can reach. |

## `[ChainExplosion]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 140 |  | Cast time in tick. |
| `magiculeCost` | 80,000 |  | Magicule Cost to cast. |
| `range` | 32 |  | The range in block of the magic. |
| `explosionNumber` | 3 |  | The number of explosions of the magic. |
| `magicDamage` | 200 |  | The magic damage of each explosion. |
| `magicDamageMastered` | 300 |  | The magic damage of each explosion when mastered. |
| `explosionRadius` | 10 |  | The radius in block of each explosion. |
| `explosionRadiusMastered` | 15 |  | The radius in block of each explosion when mastered. |
| `explosionDelay` | 30 |  | The tick delay between each explosion. |

## `[Fire]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 40 |  | Cast time in tick. |
| `castTimeMastered` | 20 |  | Cast time in tick when mastered. |
| `magiculeCost` | 150 |  | Magicule Cost to cast. |
| `magicDamage` | 20 |  | The magic damage of the fire. |
| `fireDamage` | 10 |  | The fire damage of the fire. |

## `[FireLance]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 50 |  | Cast time in tick. |
| `castTimeRepeat` | 10 |  | Cast time in tick between each lance in Repeat Mode. |
| `magiculeCost` | 1,000 |  | Magicule Cost to cast. |
| `magicDamage` | 50 |  | The magic damage of the fire. |
| `fireDamage` | 20 |  | The fire damage of the fire. |

## `[FireBall]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 60 |  | Cast time in tick. |
| `castTimeMastered` | 20 |  | Cast time in tick when mastered. |
| `magiculeCost` | 30,000 |  | Magicule Cost to cast. |
| `magiculeCostCharged` | 50,000 |  | Magicule Cost to cast when charged. |
| `magicDamage` | 100 |  | The magic damage of the fireball. |
| `fireDamage` | 30 |  | The fire damage of the fireball. |
| `explosionRadius` | 3 |  | The explosion radius in block of the fireball. |
| `magicDamageCharged` | 250 |  | The magic damage of the fireball when charged. |
| `fireDamageCharged` | 60 |  | The fire damage of the fireball when charged. |
| `explosionRadiusCharged` | 6 |  | The explosion radius in block of the fireball when charged. |
| `cooldown` | 3 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 1 |  | The cooldown in second of the magic when mastered. |

## `[FireWall]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 60 |  | Cast time in tick. |
| `magiculeCost` | 5,000 |  | Magicule Cost to cast. |
| `range` | 10 |  | The range in block of the magic. |
| `width` | 4 |  | The width radius of the Fire Wall. |
| `height` | 8 |  | The height of the Fire Wall. |
| `magicDamage` | 30 |  | The magic damage of the Fire Wall. |
| `fireDamage` | 10 |  | The fire damage of the Fire Wall. |
| `damageInterval` | 10 |  | The damaging interval in ticks of the Fire Wall. |
| `damageIntervalMastered` | 5 |  | The damaging interval in ticks of the Fire Wall when mastered. |
| `knockback` | 0.5 |  | The knockback multiplier of the Fire Wall. |
| `knockResistNegate` | 0.6 |  | The knockback resistance negation of the Fire Wall when mastered. |
| `wallDuration` | 200 |  | The duration in tick of the Fire Wall. |
| `wallDurationMastered` | 300 |  | The duration in tick of the Fire Wall when mastered. |

## `[FireStorm]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `magiculeCost` | 10,000 |  | Magicule Cost to cast. |
| `range` | 20 |  | The range in block of the Condensed mode. |
| `width` | 15 |  | The width radius of the Fire Storm in Spread mode. |
| `height` | 10 |  | The surge height of the Fire  Storm in Spread mode. |
| `magicDamage` | 20 |  | The magic damage of the Fire Storm in Spread mode. |
| `fireDamage` | 30 |  | The fire damage of the Fire Storm in Spread mode. |
| `magicSurgeDamage` | 200 |  | The magic Surge damage of the Fire Storm in Spread mode. |
| `fireSurgeDamage` | 50 |  | The fire Surge damage of the Fire Storm in Spread mode. |
| `damageInterval` | 10 |  | The damaging interval in ticks of the Fire Storm in Spread mode. |
| `surgeInterval` | 30 |  | The surge interval in ticks of the Fire Storm in Spread mode. |
| `stormDuration` | 150 |  | The duration in ticks of the Fire Storm in Spread mode. |
| `condensedSize` | 5 |  | The size of the Fire Storm in Condensed mode. |
| `condensedInterval` | 20 |  | The damaging interval in ticks of the Fire Storm in Condensed mode. |
| `magicCondensedDamage` | 300 |  | The magic damage of the Fire Storm in Condensed mode. |
| `fireCondensedDamage` | 100 |  | The fire damage of the Fire Storm in Condensed mode. |
| `condensedDuration` | 40 |  | The duration in ticks of the Fire Storm in Condensed mode. |
| `cooldown` | 7 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 5 |  | The cooldown in second of the magic when mastered. |

## `[Float]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 40 |  | Cast time in tick. |
| `magiculeCost` | 100 |  | Magicule Cost to cast. |
| `levitationDuration` | 200 |  | The duration in tick of the Levitation effect to apply on the caster. |
| `levitationLevel` | 1 |  | The level of the Levitation effect to apply on the caster. |
| `projectileDamage` | 25 |  | The magic damage of the projectile. |
| `projectileDuration` | 200 |  | The duration in tick of the Levitation effect of the projectile. |
| `projectileLevel` | 1 |  | The level of the Levitation effect of the projectile. |

## `[Lighten]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 60 |  | Cast time in tick. |
| `magiculeCost` | 250 |  | Magicule Cost to cast. |
| `range` | 10 |  | The range in block of the magic. |
| `speedLevel` | 2 |  | The level of the Speed effect. |
| `speedDuration` | 400 |  | The duration in tick of the Speed effect. |
| `speedDurationMastered` | 1,200 |  | The duration in tick of the Speed effect when mastered. |
| `jumpLevel` | 2 |  | The level of the Jump Boost effect. |
| `jumpDuration` | 400 |  | The duration in tick of the Jump Boost effect. |
| `jumpDurationMastered` | 1,200 |  | The duration in tick of the Jump Boost effect when mastered. |

## `[Burden]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 80 |  | Cast time in tick. |
| `magiculeCost` | 50 |  | Magicule Cost to cast. |
| `burdenLevel` | 3 |  | The level of the Burden effect of the projectile. |
| `burdenDuration` | 600 |  | The duration in tick of the Burden effect of the projectile. |
| `slownessLevel` | 2 |  | The level of the Slowness effect of the projectile when mastered. |
| `slownessDuration` | 600 |  | The duration in tick of the Slowness effect of the projectile when mastered. |

## `[Freeze]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 10 |  | Cast time in tick. |
| `magiculeCost` | 100 |  | Magicule Cost to cast. |
| `range` | 6 |  | The range in block of the magic. |
| `frostWalkMode` | 5 |  | The radius in block of Frost Walk mode. |

## `[IcicleLance]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 50 |  | Cast time in tick. |
| `castTimeShot` | 20 |  | Cast time in tick of the Icicle Shot mode. |
| `magiculeCost` | 850 |  | Magicule Cost to cast per icicle. |
| `magicDamage` | 40 |  | The magic damage of the icicle. |
| `icicleShotNumber` | 4 |  | The number of icicles spawn each time using Icicle Shot. |

## `[IcicleSpear]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 120 |  | Cast time in tick. |
| `magiculeCost` | 40,000 |  | Magicule Cost to cast. |
| `range` | 20 |  | The range in block of the magic. |
| `magicDamage` | 200 |  | The magic damage of the icicle. |
| `icicleRadius` | 3 |  | The radius in block of the icicle. |
| `icicleRadiusMastered` | 4 |  | The radius in block of the icicle when mastered. |
| `cooldown` | 5 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 3 |  | The cooldown in second of the magic when mastered. |

## `[IcicleRain]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 120 |  | Cast time in tick. |
| `castTimeRepeat` | 100 |  | Repeat cast time in tick when mastered. |
| `magiculeCost` | 15,000 |  | Magicule Cost to cast. |
| `magiculeCostRepeat` | 10,000 |  | Magicule Cost to repeat cast when mastered. |
| `lanceNumber` | 30 |  | The number of icicle lances to shoot each usage. |
| `magicDamage` | 60 |  | The magic damage of each icicle lance. |
| `radius` | 15 |  | The radius of the attack's area. |
| `maxTimeRepeat` | 3 |  | The maximum number of times that repeat shoots lances after the initial shot. |
| `cooldown` | 3 |  | The cooldown in second of the magic in the default mode. |
| `cooldownMastered` | 1 |  | The cooldown in second of the magic in the default mode when mastered. |

## `[IceWall]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 60 |  | Cast time in tick. |
| `magiculeCost` | 8,000 |  | Magicule Cost to cast. |
| `range` | 20 |  | The range in block of the magic. |
| `contactDamage` | 30 |  | The contact damage in magic of the ice walls. |
| `contactDamageMastered` | 65 |  | The contact damage in magic of the ice walls when mastered. |
| `contactChillLevel` | 1 |  | The level of the Chill effect when contacting ice walls. |
| `contactChillLevelMastered` | 2 |  | The level of the Chill effect when contacting ice walls when mastered. |
| `contactChillDuration` | 200 |  | The duration in tick of the Chill effect when contacting ice walls. |
| `contactChillDurationMastered` | 300 |  | The duration in tick of the Chill effect when contacting ice walls when mastered. |
| `aoeRadius` | 5 |  | The aoe effect radius in block of the ice walls. |
| `aoeDamage` | 50 |  | The aoe effect damage in magic of the ice walls. |
| `breakFrostLevel` | 1 |  | The level of the contacting Frost effect when the ice walls break while mastered. |
| `breakFrostDuration` | 200 |  | The duration in tick of the contacting Frost effect when the ice walls break while mastered. |
| `wallDuration` | 400 |  | The duration in tick of the Earth Wall. |

## `[IceBlizzard]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 160 |  | Cast time in tick. |
| `castTimeHold` | 100 |  | Cast time in tick to do the hold effect after the initial cast. |
| `magiculeCost` | 30,000 |  | Magicule Cost to cast. |
| `magiculeCostHold` | 5,000 |  | Magicule Cost to hold each 100 ticks. |
| `blizzardDamage` | 200 |  | The magic damage of the blizzard. |
| `blizzardRadius` | 17.5 |  | The radius in block of the blizzard. |
| `chillLevel` | 2 |  | The level of the Chill effect. |
| `chillDuration` | 600 |  | The duration in tick of the Chill effect. |
| `blizzardDamageHold` | 80 |  | The magic damage of the blizzard when held down each 100 ticks after the initial cast. |
| `chillLevelHold` | 1 |  | The additional level of the Chill effect when held down each 100 ticks after the initial cast. |
| `chillDurationHold` | 300 |  | The additional duration in tick of the Chill effect when held down each 100 ticks after the initial cast. |
| `maxHold` | 3 |  | The max number of times that the caster can activate the hold attack after the initial cast. |
| `maxHoldMastered` | 5 |  | The max number of times that the caster can activate the hold attack after the initial cast when mastered. |

## `[IceBreaker]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `magiculeCost` | 70,000 |  | Magicule Cost to cast. |
| `magicDamage` | 100 |  | The magic damage of the icicle. |
| `frostDamage` | 100 |  | The extra ice damage of the icicle if the target has Frost. |
| `chillDamage` | 25 |  | The extra ice damage of the icicle for each level of Chill on target. |
| `chillDamageMastered` | 50 |  | The extra ice damage of the icicle for each level of Chill on target when mastered. |
| `impactRadius` | 4 |  | The impact radius of the icicle. |
| `cooldown` | 3 |  | The cooldown in second of the magic in the default mode. |
| `cooldownMastered` | 1 |  | The cooldown in second of the magic in the default mode when mastered. |

## `[FlameWall]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 60 |  | Cast time in tick. |
| `magiculeCost` | 1,000 |  | Magicule Cost to cast. |
| `range` | 10 |  | The range in block of the magic. |
| `width` | 4 |  | The width radius of the Flame Wall. |
| `height` | 8 |  | The height of the Flame Wall. |
| `magicDamage` | 1 |  | The magic damage of the Flame Wall. |
| `damageInterval` | 10 |  | The damaging interval in ticks of the Flame Wall. |
| `damageIntervalMastered` | 5 |  | The damaging interval in ticks of the Flame Wall when mastered. |
| `knockback` | 0.1 |  | The knockback multiplier of the Flame Wall. |
| `wallDuration` | 200 |  | The duration in tick of the Flame Wall. |
| `wallDurationMastered` | 300 |  | The duration in tick of the Flame Wall when mastered. |

## `[Confusion]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `magiculeCost` | 2,000 |  | Magicule Cost to cast. |
| `radius` | 10 |  | The radius in block of the magic. |
| `confusionLevel` | 1 |  | The level of the Confusion effect per 25% EP difference between the target and the caster. |
| `confusionMaxLevel` | 3 |  | The maximum level of the Confusion effect. |
| `confusionMaxLevelMastered` | 4 |  | The maximum level of the Confusion effect when mastered. |
| `confusionDuration` | 300 |  | The duration of the Confusion effect when casted. |
| `confusionDurationMastered` | 400 |  | The duration of the Confusion effect when casted with mastery. |
| `bypassEP` | 1.5 |  | The multiplier of the caster's EP that the target needs to have above to be not applied by Confusion. |

## `[Invisible]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 60 |  | Cast time in tick. |
| `magiculeCost` | 2,000 |  | Magicule Cost to cast. |
| `invisibleLevel` | 1 |  | The level of the Invisibility effect. |
| `invisibleDuration` | 2,400 |  | The duration in tick of the Invisibility effect. |
| `concealmentLevel` | 1 |  | The level of the Presence Concealment effect when mastered. |
| `concealmentDuration` | 6,000 |  | The duration in tick of the Invisibility effect when mastered. |

## `[Mirage]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 60 |  | Cast time in tick. |
| `castTimeMastered` | 120 |  | Cast time in tick to create more clones when mastered while sneaking. |
| `magiculeCost` | 2,000 |  | Magicule Cost to cast. |
| `cloneEP` | 500 |  | The amount of EP that each illusionary clone has. |
| `cloneNumber` | 4 |  | The number of clones can the magic create each cast. |
| `cloneNumberMastered` | 8 |  | The number of clones can the magic create each cast when mastered while sneaking. |
| `cloneDuration` | 300 |  | The duration in ticks of each Clone before disappearing. |
| `cloneDurationMastered` | 600 |  | The duration in ticks of each Clone before disappearing when mastered. |
| `cooldown` | 5 |  | The cooldown in second to spawn a clone. |
| `cooldownMastered` | 3 |  | The cooldown in second to spawn a clone when mastered. |

## `[Possession]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 200 |  | Cast time in tick. |
| `magiculeCost` | 100,000 |  | Magicule Cost to cast. |
| `range` | 6 |  | The range in block of the magic. |
| `hpMultiplier` | 0.1 |  | The multiplier of the maximum Health that a target needs to be under to be possessed. |
| `shpMultiplier` | 0.1 |  | The multiplier of the maximum Spiritual Health that a target needs to be under to be possessed. |
| `epMultiplier` | 0.25 |  | The multiplier of the user's maximum EP that a target needs to be under to be possessed. |
| `resistanceMultiplier` | 0.5 |  | The multiplier of the possession requirement multipliers when the target has Spiritual Attack Resistance. |
| `maxHealth` | 1,000 |  | The maximum amount of HP the user can get from possessing an entity. |
| `maxAttack` | 100 |  | The maximum amount of Attack Damage the user can get from possessing an entity. |
| `bodyDespawnTick` | 300 |  | The number of seconds that Possession Bodies will despawn. (0 = instant despawn, -1 = doesn't despawn) |

## `[ThunderLance]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 80 |  | Cast time in tick. |
| `magiculeCost` | 5,000 |  | Magicule Cost to cast. |
| `magicDamage` | 50 |  | The magic damage of the lance. |
| `lightningDamage` | 30 |  | The lightning damage of the lance. |
| `rainRadius` | 5 |  | The radius in block of the Rain mode. |
| `rainNumber` | 10 |  | The number of lances to shoot from Rain mode. |
| `magicDamageRain` | 30 |  | The magic damage of each rain lance. |
| `lightningDamageRain` | 30 |  | The lightning damage of each rain lance. |

## `[Thunder]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 20 |  | Cast time in tick. |
| `magiculeCost` | 30,000 |  | Magicule Cost to cast. |
| `range` | 30 |  | The range in block of the magic. |
| `blastRadius` | 3 |  | The radius in block of the thunder strike's blast. |
| `blastRadiusMastered` | 5 |  | The radius in block of the thunder strike's blast when mastered. |
| `magicDamage` | 100 |  | The magic damage of the thunder strike. |
| `magicDamageMastered` | 200 |  | The magic damage of the thunder strike when mastered. |
| `cooldown` | 3 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 1 |  | The cooldown in second of the magic when mastered. |

## `[ThunderOrb]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 120 |  | Cast time in tick. |
| `castTimeMastered` | 80 |  | Cast time in tick when mastered. |
| `magiculeCost` | 20,000 |  | Magicule Cost to cast. |
| `magicDamage` | 80 |  | The magic damage of each lightning strike. |
| `lightningDamage` | 40 |  | The lightning damage of each lightning strike. |
| `strikeInterval` | 10 |  | The interval in tick between each time the sphere strikes enemies. |
| `strikeRadius` | 5 |  | The strike radius in block of the sphere. |
| `strikeRadiusMastered` | 10 |  | The strike radius in block of the sphere when mastered. |
| `cooldown` | 5 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 3 |  | The cooldown in second of the magic when mastered. |

## `[ThunderRain]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 160 |  | Cast time in tick. |
| `castTimeMastered` | 100 |  | Cast time in tick when mastered. |
| `magiculeCost` | 70,000 |  | Magicule Cost to cast. |
| `radius` | 17.5 |  | The radius in block of the rain. |
| `thunderDamage` | 300 |  | The magic damage of each thunder strike. |
| `thunderInterval` | 80 |  | The interval in tick between each times thunders struck. |
| `duration` | 600 |  | The duration in tick of the rain. |
| `coatDamage` | 100 |  | The magic damage of each melee attack from the caster when Coating Mode is casted. |
| `coatNumber` | 5 |  | The number of melee attacks will be coated in thunder when Coating Mode is casted. |
| `cooldown` | 10 |  | The cooldown in second when casted. |

## `[Dominate]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `magiculeCost` | 10,000 |  | Magicule Cost to cast. |
| `range` | 6 |  | The range in block of the magic. |
| `epRequirement` | 10,000 |  | The amount of EP that the target needs to have below to be controlled. |
| `resistedRequirement` | 5,000 |  | The amount of EP that the target needs to have below to be controlled when having Spiritual Attack Resistance toggled. |
| `controlDuration` | 12,000 |  | The duration in tick of the Mind Control effect (-1 = permanent). |
| `controlDurationMastered` | -1 |  | The duration in tick of the Mind Control effect when mastered (-1 = permanent). |

## `[DemonDominate]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `magiculeCost` | 100,000 |  | Magicule Cost to cast. |
| `range` | 10 |  | The range in block of the magic. |
| `epRequirement` | 200,000 |  | The amount of EP that the target needs to have below to be controlled. |
| `resistedRequirement` | 100,000 |  | The amount of EP that the target needs to have below to be controlled when having Spiritual Attack Resistance toggled. |
| `controlDuration` | 12,000 |  | The duration in tick of the Mind Control effect (-1 = permanent). |
| `controlDurationMastered` | -1 |  | The duration in tick of the Mind Control effect when mastered (-1 = permanent). |

## `[DemonMarionette]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 200 |  | Cast time in tick. |
| `magiculeCost` | 200,000 |  | Magicule Cost to cast. |
| `range` | 20 |  | The range in block of the magic. |
| `epRequirement` | 400,000 |  | The amount of EP that the target needs to have below to be controlled. |
| `resistedRequirement` | 200,000 |  | The amount of EP that the target needs to have below to be controlled when having Spiritual Attack Resistance toggled. |
| `epRequirementMastered` | 800,000 |  | The amount of EP that the target needs to have below to be controlled while mastered. |
| `resistedRequirementMastered` | 400,000 |  | The amount of EP that the target needs to have below to be controlled when having Spiritual Attack Resistance toggled while mastered. |
| `slowLevel` | 5 |  | The level of Movement Interference to apply on target when casted (-10% speed each level). |
| `controlDuration` | 12,000 |  | The duration in tick of the Mind Control effect (-1 = permanent). |
| `controlDurationMastered` | -1 |  | The duration in tick of the Mind Control effect when mastered (-1 = permanent). |

## `[MentalCrush]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `magiculeCost` | 30,000 |  | Magicule Cost to cast. |
| `range` | 6 |  | The range in block of the magic. |
| `minSHP` | 100 |  | The minimal SHP damage that a target takes from the magic. |
| `minSHPResisted` | 50 |  | The minimal SHP damage that a target takes from the magic if Spiritual Attack Resistance is toggled. |
| `shpMultiplier` | 0.1 |  | The multiplier of max SHP that a target takes from the magic. |
| `shpMultiplierResist` | 0.05 |  | The multiplier of max SHP that a target takes from the magic if Spiritual Attack Resistance is toggled. |
| `shpMultiplierWeakened` | 0.2 |  | The multiplier of max SHP that a Weakened target takes from the magic with Mastery. |
| `shpMultiplierWeakenedResist` | 0.1 |  | The multiplier of max SHP that a Weakened target takes from the magic with Mastery if Spiritual Attack Resistance is toggled. |
| `fragilityLevel` | 2 |  | The level of Fragility that the magic applies on targets. |
| `fragilityDuration` | 300 |  | The duration in second of Fragility that the magic applies on targets. |
| `insanityChance` | 0.25 |  | The chance for targets to get Insanity from the magic. |
| `insanityChanceWeakened` | 0.5 |  | The chance for Weakened targets to get Insanity from the magic. |
| `insanityLevel` | 3 |  | The max level of Insanity that the magic can apply on targets. |
| `insanityDuration` | 600 |  | The duration in second of Insanity that the magic applies on targets. |
| `weakenedMultiplier` | 0.5 |  | The multiplier of max SHP that the target needs to be below to be considered Weakened. |
| `cooldown` | 3 |  | The cooldown in second of the magic. |

## `[Hypnos]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 180 |  | Cast time in tick. |
| `castTimeMastered` | 120 |  | Cast time in tick when mastered. |
| `magiculeMultiplierCost` | 0.025 |  | The multiplier of the target's EP to be calculated for the Magicule Cost to cast. |
| `minCost` | 50,000 |  | Minimum Magicule Cost to cast. |
| `range` | 6 |  | The range in block of the magic. |
| `sleepLevel` | 1 |  | The level of the Sleep effect. |
| `sleepLevelMastered` | 3 |  | The level of the Sleep effect when mastered. |
| `sleepDuration` | 1,200 |  | The duration in tick of the Sleep effect. |
| `sleepDurationResisted` | 600 |  | The duration in tick of the Sleep effect if the target has Spiritual Attack Nullification. |
| `sleepDurationMastered` | 2,400 |  | The duration in tick of the Sleep effect when mastered. |
| `sleepDurationMasteredResisted` | 1,200 |  | The duration in tick of the Sleep effect if the target has Spiritual Attack Nullification when mastered. |
| `cooldown` | 3 |  | The cooldown in second of the magic in the default mode. |
| `cooldownMastered` | 1 |  | The cooldown in second of the magic in the default mode when mastered. |

## `[Healing]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 60 |  | Cast time in tick. |
| `castTimeMastered` | 30 |  | Cast time in tick when mastered. |
| `minCost` | 1,000 |  | Minimal Magicule Cost to cast. |
| `magiculeCost` | 100 |  | Magicule Cost  to heal each HP. |
| `range` | 6 |  | The range in block of the magic. |
| `hpHeal` | 50 |  | The amount of HP that the magic heals. |
| `hpHealMastered` | 100 |  | The amount of HP that the magic heals when mastered. |
| `hpHealPercentage` | 0.25 |  | The percentage of max HP that the magic heals when mastered (if higher than 100). |
| `cooldown` | 5 |  | The cooldown in second when activated Healing. |
| `cooldownMastered` | 3 |  | The cooldown in second when activated Healing with mastery. |

## `[HealingRain]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `magiculeCost` | 5,000 |  | Magicule Cost to cast. |
| `radius` | 7.5 |  | The radius in block of the rain. |
| `hpHeal` | 10 |  | The amount of HP that the rain heals each second. |
| `hpHealMastered` | 20 |  | The amount of HP that the magic heals each second when mastered. |
| `hpHealPercentage` | 0.05 |  | The percentage of max HP that the magic heals each second when mastered (if higher than 20). |
| `duration` | 100 |  | The duration in tick of the rain. |
| `cooldown` | 5 |  | The cooldown in second when activated Healing. |
| `cooldownMastered` | 3 |  | The cooldown in second when activated Healing with mastery. |

## `[Recovery]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `minCost` | 10,000 |  | Minimal Magicule Cost to cast. |
| `magiculeCost` | 100 |  | Magicule Cost  to heal each HP. |
| `range` | 6 |  | The range in block of the magic. |
| `hpHealPercentage` | 0.5 |  | The percentage of max HP that the magic heals. |
| `foodPoint` | 4 |  | The amount of food point that the magic gives. |
| `foodPointMastered` | 8 |  | The amount of food point that the magic gives when mastered. |
| `saturationPoint` | 10 |  | The amount of saturation point that the magic gives. |
| `saturationPointMastered` | 20 |  | The amount of saturation point that the magic gives when mastered. |
| `cooldown` | 10 |  | The cooldown in second when activated Healing. |
| `cooldownMastered` | 5 |  | The cooldown in second when activated Healing with mastery. |

## `[Antidote]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 120 |  | Cast time in tick. |
| `magiculeCost` | 2,500 |  | Magicule Cost to cast. |
| `range` | 6 |  | The range in block of the magic. |
| `fatalLevel` | 1 |  | The level of Fatal Poison that the magic removes. |
| `fatalDuration` | 10 |  | The duration in second of Fatal Poison that the magic removes. |

## `[FullRecovery]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 120 |  | Cast time in tick. |
| `castTimeMastered` | 80 |  | Cast time in tick when mastered. |
| `minCost` | 30,000 |  | Minimal Magicule Cost to cast. |
| `magiculeCost` | 100 |  | Magicule Cost  to heal each HP. |
| `range` | 6 |  | The range in block of the magic. |
| `hpHealPercentage` | 1 |  | The percentage of max HP that the magic heals. |
| `foodPoint` | 20 |  | The amount of food point that the magic gives. |
| `saturationPoint` | 20 |  | The amount of saturation point that the magic gives. |
| `absorptionLevel` | 4 |  | The level of Absorption that the magic gives. |
| `absorptionDuration` | 2,400 |  | The duration in second of Absorption that the magic gives. |
| `absorptionDurationMastered` | 4,800 |  | The duration in second of Absorption that the magic gives when mastered. |
| `cooldown` | 15 |  | The cooldown in second when activated Healing. |
| `cooldownMastered` | 10 |  | The cooldown in second when activated Healing with mastery. |

## `[Escape]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `magiculeCost` | 800 |  | Magicule Cost to cast. |
| `warpChargeTick` | 100 |  | The charge time in tick before warping the user. |
| `maxRange` | 500 |  | The max range in blocks away from the escape magic circle that the user can teleport to. |
| `maxRangeMastered` | 1,000 |  | The max range in blocks away from the escape magic circle that the user can teleport to when mastered. |
| `autoEscapeHP` | 0.1 |  | The multiplier of max HP that the user needs have below to activate the auto-escape when toggled with mastery. |
| `autoEscapeMP` | 0.01 |  | The multiplier of max MP that the user needs have below to activate the auto-escape when toggled with mastery. |
| `cooldown` | 10 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 5 |  | The cooldown in second of the magic when mastered. |

## `[WarpPortal]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 80 |  | Cast time in tick. |
| `magiculeCost` | 50 |  | Magicule Cost per block to warp. |
| `warpChargeTick` | 100 |  | The charge tick of the portal before warping any entity. |
| `cooldown` | 20 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 10 |  | The cooldown in second of the magic when mastered. |

## `[SpatialStorage]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 40 |  | Cast time in tick. |
| `magiculeCost` | 3,000 |  | Magicule Cost to cast. |
| `spatialSlots` | 54 |  | The number of slots of the Spatial Storage. |
| `spatialStack` | 100 |  | The maximum stack size of items in the Spatial Storage. |
| `spatialStackMastered` | 200 |  | The maximum stack size of items in the Spatial Storage when mastered. |

## `[DimensionCutter]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 120 |  | Cast time in tick. |
| `magiculeCost` | 20,000 |  | Magicule Cost to cast. |
| `spatialDamage` | 50 |  | The spatial damage of the dimension cutter. |
| `spatialDamageMastered` | 100 |  | The spatial damage of the dimension cutter when mastered. |
| `size` | 2 |  | The size multiplier of the dimension cutter. |
| `sizeMastered` | 4 |  | The size multiplier of the dimension cutter when mastered. |
| `cooldown` | 3 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 1 |  | The cooldown in second of the magic when mastered. |

## `[Water]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 20 |  | Cast time in tick. |
| `magiculeCost` | 100 |  | Magicule Cost to cast per water block. |
| `range` | 6 |  | The range in block of the magic. |

## `[Drainage]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 40 |  | Cast time in tick. |
| `magiculeCost` | 20 |  | Magicule Cost per block per 5 ticks to cast this magic. |
| `radius` | 5 |  | The radius in block of the magic. |
| `radiusMastered` | 8 |  | The radius in block of the magic when mastered. |

## `[WaterCutter]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 30 |  | Cast time in tick. |
| `castTimeRepeat` | 15 |  | Repeat cast time in tick when mastered. |
| `magiculeCost` | 1,000 |  | Magicule Cost to cast. |
| `magiculeCostRepeat` | 500 |  | Magicule Cost to repeat cast when mastered. |
| `magicDamage` | 40 |  | The magic damage of the water cutter. |

## `[WaterJail]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 60 |  | Cast time in tick. |
| `castTimeHold` | 40 |  | Cast time in tick between damaging when held down. |
| `magiculeCost` | 25,000 |  | Magicule Cost to cast. |
| `magiculeCostHold` | 1,000 |  | Magicule Cost to hold down each 40 ticks (castTimeHold). |
| `range` | 20 |  | The range in block of the magic. |
| `jailSize` | 3 |  | The size in block of the Water Jail. |
| `magicDamage` | 100 |  | The magic damage of the Water Jail. |
| `bladeDamage` | 50 |  | The water blade damage of the Water Jail. |
| `maxHold` | 120 |  | The max number of ticks that the caster can hold magic down. |
| `maxHoldMastered` | 240 |  | The max number of ticks that the caster can hold magic down when mastered. |

## `[SleepMist]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `magiculeCost` | 5,000 |  | Magicule Cost to cast. |
| `mistRadius` | 5 |  | The radius in block of the sleep mist. |
| `mistLevel` | 2 |  | The level of the paralyzing effect. |
| `mistDuration` | 300 |  | The duration in tick of the sleep mist and the paralyzing effect. |
| `mistDurationMastered` | 500 |  | The duration in tick of the sleep mist and the paralyzing effect when mastered. |

## `[AcidShell]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 80 |  | Cast time in tick. |
| `magiculeCost` | 38,000 |  | Magicule Cost to cast. |
| `magicDamage` | 175 |  | The magic damage of the projectile. |
| `armorHurt` | 300 |  | The durability that the target's armors get reduced when hit by the projectile. |
| `corrosionLevel` | 2 |  | The level of the Corrosion effect of the projectile when mastered. |
| `corrosionDuration` | 400 |  | The duration in tick of the Corrosion effect of the projectile when mastered. |
| `cooldown` | 3 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 1 |  | The cooldown in second of the magic when mastered. |

## `[WindGust]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 20 |  | Cast time in tick. |
| `magiculeCost` | 100 |  | Magicule Cost to cast. |

## `[WindCutter]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 40 |  | Cast time in tick. |
| `castTimeMastered` | 30 |  | Cast time in tick when mastered. |
| `magiculeCost` | 500 |  | Magicule Cost to cast. |
| `magicDamage` | 30 |  | The magic damage of the wind cutter. |
| `windDamage` | 10 |  | The wind damage of the wind cutter. |

## `[TornadoBlade]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 50 |  | Cast time in tick. |
| `magiculeCost` | 40,000 |  | Magicule Cost to cast. |
| `magicDamage` | 150 |  | The magic damage of the wind tornado. |
| `magicDamageMastered` | 300 |  | The magic damage of the wind tornado when mastered. |
| `windDamage` | 25 |  | The wind damage of the wind tornado. |
| `windDamageMastered` | 50 |  | The wind damage of the wind tornado when mastered. |
| `hitRadius` | 3 |  | The damage radius of the wind tornado. |
| `hitRadiusMastered` | 4 |  | The damage radius of the wind tornado when mastered. |
| `burstDelay` | 20 |  | The delay in tick of the wind tornado before exploding. |
| `pullForce` | 0.1 |  | The pull force multiplier of the wind tornado when mastered. |
| `bladeNumber` | 10 |  | The number of wind blades that the wind tornado release on explosion when mastered. |
| `bladeDamage` | 50 |  | The magic damage of each wind blade that the wind tornado release on explosion when mastered. |
| `cooldown` | 3 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 1 |  | The cooldown in second of the magic when mastered. |

## `[WindProtection]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 60 |  | Cast time in tick. |
| `magiculeCost` | 1,000 |  | Magicule Cost to cast. |
| `effectLevel` | 1 |  | The level of the Wind's Protection effect. |
| `effectDuration` | 2,400 |  | The duration in tick of the Wind's Protection effect. |
| `effectLevelMastered` | 3 |  | The level of the Wind's Protection effect when mastered. |
| `effectDurationMastered` | 3,600 |  | The duration in tick of the Wind's Protection effect when mastered. |
| `effectSpeed` | 0.2 |  | The speed boost multiplier of the Wind's Protection effect per level. |
| `effectDodge` | 100 |  | The projectile dodge chance of the Wind's Protection effect per level. |
| `effectKnockback` | 0.1 |  | The knockback resistance of the Wind's Protection effect per level (start from level 2). |
| `effectBurn` | 0.5 |  | The burning time percentage reduction of the Wind's Protection effect per level (start from level 2). |
| `effectFlameBoost` | 0.1 |  | The flame attack boost multiplier of the Wind's Protection effect per level (start from level 2). |

## `[AirflowShut]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `castTimeMastered` | 80 |  | Cast time in tick when mastered. |
| `castTimeHold` | 20 |  | Cast time in tick between effect inflicting when held down. |
| `magiculeCost` | 3,000 |  | Magicule Cost to cast. |
| `magiculeCostHold` | 1,300 |  | Magicule Cost to hold down each 20 ticks (castTimeHold). |
| `range` | 20 |  | The range in block of the magic. |
| `sphereSize` | 5 |  | The size in block of the Air Sphere. |
| `sphereSizeMastered` | 8 |  | The size in block of the Air Sphere from the Expanded Mode. |
| `silenceLevel` | 1 |  | The level of the Silence effect. |
| `silenceDuration` | 100 |  | The duration in tick of the Silence effect. |
| `sphereDuration` | 200 |  | The duration in tick of the Air Sphere after casting. |

## `[Reincarnation]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 200 |  | Cast time in tick. |
| `minimalMagicule` | 10,000 |  | The minimal Magicule cost to cast. |
| `auraCost` | 0.25 |  | The Max Aura multiplier of the caster to be consumed for this magic. |
| `magiculeCost` | 0.25 |  | The Max Magicule multiplier of the caster to be consumed for this magic. |

## `[Analyze]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 40 |  | Cast time in tick. |
| `magiculeCost` | 50 |  | Magicule Cost per second to cast. |
| `bonusAnalysis` | 1 |  | The Bonus Analysis Level when held. |
| `bonusAnalysisMastered` | 2 |  | The Bonus Analysis Level when held while mastered. |
| `bonusAnalysisRadius` | 5 |  | The Bonus Analysis Distance when held. |
| `bonusAnalysisRadiusMastered` | 10 |  | The Bonus Analysis Distance when held with Mastery. |

## `[Clairvoyance]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 20 |  | Cast time in tick. |
| `magiculeCost` | 10 |  | Magicule Cost per second to cast. |
| `maxZoom` | 25 |  | The Max Zoom Multiplier. |
| `maxZoomMastered` | 50 |  | The Max Zoom Multiplier when mastered. |

## `[Doppelganger]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `castTimeMastered` | 80 |  | Cast time in tick when mastered. |
| `magiculeCost` | 0.1 |  | The multiplier of the user's maximum Magicule to be calculated for the magicule cost of the magic. |
| `cloneNumber` | 2 |  | The number of clones can the magic create each cast. |
| `cloneNumberMastered` | 4 |  | The number of clones can the magic create each cast when mastered while sneaking. |
| `cloneHeal` | 2 |  | The amount of HP that a clone heals each second. |
| `cloneHealEnergy` | 20 |  | The amount of Energy that a clone uses each second when healing. |
| `cloneFragility` | 2 |  | The level of Fragility that each clone has. |
| `cooldown` | 5 |  | The cooldown in second to spawn a clone. |
| `cooldownMastered` | 3 |  | The cooldown in second to spawn a clone when mastered. |

## `[Flight]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 60 |  | Cast time in tick. |
| `magiculeCost` | 500 |  | Magicule Cost per second to cast. |
| `pushForce` | 0.05 |  | The push force on the caster when held down. |
| `flightDuration` | 200 |  | The max duration in tick that the magic can be used. |
| `flightDurationMastered` | 300 |  | The max duration in tick that the magic can be used when mastered. |

## `[Healthcare]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `magiculeCost` | 100 |  | Magicule Cost to cast. |
| `healthRegeneration` | 1 |  | The health regeneration boost every 2 seconds. |
| `careDuration` | 10,000 |  | The duration in tick of the Healthcare effect. |
| `careDurationMastered` | 100,000 |  | The duration in tick of the Healthcare effect when mastered. |

## `[SearchEnemy]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 40 |  | Cast time in tick. |
| `magiculeCost` | 100 |  | Magicule Cost to cast. |
| `magiculeCostConstant` | 5 |  | Magicule Cost per second to cast the Constant mode. |
| `searchDuration` | 2,400 |  | The duration in tick of the Enemy Search effect when using default mode. |
