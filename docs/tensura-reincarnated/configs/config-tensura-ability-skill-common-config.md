# `config/tensura/ability/skill/common_config.toml`

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Coercion]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 5,000 |  | EP Requirement for Learning. |
| `magiculeCost` | 50 |  | Magicule Cost to activate. |
| `roarRange` | 14 |  | The attack range of the roar in blocks. |
| `epDifferenceMultiplier` | 0.25 |  | The EP difference multiplier for each Fear Level. |
| `fearDuration` | 200 |  | The duration in tick of the Fear effect. |
| `cooldown` | 2 |  | The Cooldown in second after activation (halved when mastered). |

## `[Corrosion]`

| Option | Default | Range | Description |
|---|---|---|---|
| `rottenFleshAcquirement` | 100 |  | Rotten flesh eaten Optional Requirement for Learning. |
| `serpentAcquirement` | 100 |  | Tempest Serpent beaten Optional Requirement for Learning. |
| `orcAcquirement` | 1 |  | Orc Lord/Disaster beaten Optional Requirement for Learning. |
| `corrosionDuration` | 200 |  | The duration in tick of the Corrosion/Wither effect. |
| `corrosionLevel` | 1 |  | The level of the Corrosion/Wither effect. |

## `[FarSight]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 5,000 |  | EP Requirement for Learning. |
| `maxZoom` | 50 |  | The Max Zoom Multiplier. |
| `maxSenseRadius` | 60 |  | The Max Bonus Presence Sense Radius when mastered. |

## `[GravityField]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 20,000 |  | EP Requirement for Learning. |
| `magiculeCost` | 50 |  | Magicule Cost to activate. |
| `cooldown` | 5 |  | The Cooldown in second after activation. |
| `fieldDuration` | 1,200 |  | The duration in tick of the Gravity Field. |
| `fieldRadius` | 6 |  | The radius of the Gravity Field. |
| `fieldRadiusMastered` | 10 |  | The radius of the Gravity Field when mastered. |
| `speedLevel` | 2 |  | The level of the speed/slowness effect when applied. |
| `slowFallLevel` | 1 |  | The level of the slow-fall/burden effect when applied. |

## `[GravityFlight]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 10,000 |  | EP Requirement for Learning. |
| `magiculeCost` | 5 |  | Magicule Cost to activate. |
| `upMultiplier` | 1 |  | The multiplier of the going-up speed when hold down. |

## `[HydraulicPropulsion]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 10,000 |  | EP Requirement for Learning. |
| `magiculeCost` | 2 |  | Magicule Cost to activate. |
| `riptideLevel` | 3 |  | The level of the riptide boost when activated. |
| `riptideDuration` | 10 |  | The duration in tick of the riptide boost when activated. |
| `riptideMultiplier` | 1 |  | The damage multiplier compared to the user's attack when hit target during Riptide boost. |

## `[Paralysis]`

| Option | Default | Range | Description |
|---|---|---|---|
| `centipedeAcquirement` | 500 |  | Evil Centipede beaten Requirement for Learning. |
| `paralysisDuration` | 200 |  | The duration in tick of the Paralysis effect. |
| `paralysisLevel` | 1 |  | The level of the Paralysis effect. |
| `paralysisLevelMastered` | 2 |  | The level of the Paralysis effect when Mastered. |

## `[Poison]`

| Option | Default | Range | Description |
|---|---|---|---|
| `spiderEyeAcquirement` | 100 |  | Spider Eye eaten Optional Requirement for Learning. |
| `spiderAcquirement` | 100 |  | Black Spider beaten Optional Requirement for Learning. |
| `poisonDuration` | 200 |  | The duration in tick of the Poison effect. |
| `poisonLevel` | 1 |  | The level of the Poison effect. |

## `[RangedBarrier]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 80,000 |  | EP Requirement for Learning. |
| `ifritAcquirement` | 1 |  | Ifrit beaten Requirement for Learning. |
| `magiculeCost` | 5 |  | Base Magicule Cost to activate. |
| `barrierRange` | 30 |  | The max activation range for the barriers in blocks. |
| `barrierDuration` | 1,200 |  | The duration of the barrier when activated (doubled when mastered). |
| `barrierRadius` | 2 |  | The radius of the barrier in the first mode. |
| `barrierRadiusSecond` | 5 |  | The radius of the barrier in the second mode. |
| `barrierRadiusThird` | 10 |  | The radius of the barrier in the third mode. |

## `[SelfRegeneration]`

| Option | Default | Range | Description |
|---|---|---|---|
| `slimeAcquirement` | 500 |  | Slime beaten Requirement for Learning. |
| `magiculeCost` | 100 |  | Base Magicule Cost to activate. |
| `regenLevel` | 1 |  | The level of the self-regeneration effect. |
| `regenLevelMastered` | 2 |  | The level of the self-regeneration effect when mastered. |
| `regenHP` | 2 |  | How much HP to regenerate each second per level. |
| `regenSHP` | 4 |  | How much SHP to regenerate each second per level when mastered. |

## `[Strength]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 3,000 |  | EP Requirement for Learning. |
| `magiculeCost` | 30 |  | Base Magicule Cost to activate. |
| `strengthenDuration` | 1,200 |  | The duration of the Strengthen effect when activated. |
| `strengthenDurationMastered` | 2,400 |  | The duration of the Strengthen effect when activated with mastery. |
| `strengthenLevel` | 1 |  | The level of the Strengthen effect when activated (+3 Attack Damage per level). |
| `strengthenLevelMastered` | 2 |  | The level of the Strengthen effect when activated with Mastered. |
| `cooldown` | 3 |  | The Cooldown in second of the skill. |

## `[Telepathy]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 2,000 |  | EP Requirement for Learning. |
| `telepathyRadius` | 30 |  | The radius of the Telepathy activation. |

## `[ThoughtCommunication]`

| Option | Default | Range | Description |
|---|---|---|---|
| `telepathyRadius` | 30 |  | The radius of the Telepathy activation. |

## `[VoiceCannon]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 10,000 |  | EP Requirement for Learning when Coercion mastered. |
| `magiculeCost` | 500 |  | Magicule Cost to activate . |
| `cannonDamage` | 20 |  | The damage of the Voice Cannon when hit a target. |
| `cannonDamageMastered` | 30 |  | The damage of the Voice Cannon when hit a target with mastery. |
| `cannonRange` | 15 |  | The range in block of the Voice Cannon. |
| `cannonRangeMastered` | 20 |  | The range in block of the Voice Cannon when mastered. |
| `cannonCooldown` | 3 |  | The cooldown in second after activating Voice Cannon. |

## `[WaterBlade]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 10,000 |  | EP Requirement for Learning. |
| `magiculeCost` | 10 |  | Base Magicule Cost to activate. |
| `damage` | 40 |  | The damage of the Water Blade. |
| `speedMultiplier` | 5 |  | The speed multiplier of the Water Blade. |

## `[WaterCurrentControl]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 6,000 |  | EP Requirement for Learning. |
| `swimBoost` | 4 |  | The Swim Speed Multiplier when activated. |
