# `config/nightmare/ability/battlewill/nightmare_battlewill.toml`

<small>[TR: Nightmares](../index.md) &rsaquo; [Configs](index.md)</small>

## `[VortexPunch]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 400,000 |  | EP required to learn Vortex Punch. (unused) |
| `learningAuraCost` | 10,000 |  | Aura point cost used while learning Vortex Punch. |
| `auraCost` | 400 |  | Aura cost per use. |
| `cooldownSeconds` | 8 |  | Cooldown in seconds after use. |
| `baseDamageMultiplier` | 2.5 |  | Base damage multiplier. |
| `masteredDamageMultiplier` | 5 |  | Mastered damage multiplier. |
| `range` | 12 |  | Reach for target selection. |

## `[BarrageStrike]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 400,000 |  | EP required to learn Barrage Strike. (unused) |
| `learningAuraCost` | 10,000 |  | Aura point cost used while learning Barrage Strike. |
| `auraCost` | 0 |  | Aura cost per use. |
| `cooldownSeconds` | 10 |  | Cooldown in seconds after use. |
| `hits` | 4 |  | Number of hits while unmastered. |
| `hitsMastered` | 8 |  | Number of hits while mastered. |
| `baseDamageMultiplier` | 1 |  | Base damage multiplier. |
| `masteredDamageMultiplier` | 2 |  | Mastered damage multiplier. |
| `range` | 12 |  | Targeting range. |

## `[OniPyre]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 1,500,000 |  | EP required to learn Oni Pyre. |
| `learningAuraCost` | 15,000 |  | Aura point cost used while learning Oni Pyre. |
| `auraCostPerPillar` | 300 |  | Aura cost per pillar. |
| `chargeTimeTicks` | 100 |  | Charge time in ticks. |
| `pillarDamage` | 150 |  | Pillar damage per second. |
| `pillarRadius` | 2 |  | Pillar radius. |
| `durationTicks` | 100 |  | Duration in ticks while unmastered. |
| `durationMasteredTicks` | 200 |  | Duration in ticks while mastered. |
| `range` | 15 |  | Target search range. |
| `cooldownSeconds` | 30 |  | Cooldown in seconds after release. |

## `[AuraArmor]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 500,000 |  | EP required to learn Aura Armor. (unused) |
| `learningAuraCost` | 10,000 |  | Aura point cost used while learning Aura Armor. |
| `auraStep` | 50,000 |  | Aura step size used for scaling. |
| `maxAuraCounted` | 500,000 |  | Maximum aura value counted for scaling. |
| `attackBonusPerStep` | 1 |  | Attack damage gained per step. |
| `armorBonusPerStep` | 4 |  | Armor gained per step. |
| `cooldownSeconds` | 5 |  | Cooldown in seconds after toggling. |

## `[PressureTraining]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 750,000 |  | EP required to learn Pressure Training. (unused) |
| `learningAuraCost` | 10,000 |  | Aura point cost used while learning Pressure Training. |
| `auraCostPerSecond` | 1,000 |  | Aura cost per second. |
| `selfDamagePerSecond` | 50 |  | Self-damage per second. |
| `cooldownSeconds` | 8 |  | Cooldown in seconds after release. |

## `[SpiralPenetrator]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 750,000 |  | EP required to learn Spiral Penetrator. (unused) |
| `learningAuraCost` | 25,000 |  | Aura point cost used while learning Spiral Penetrator. |
| `auraCostPerPowerScale` | 25,000 |  | Aura cost per power scale. |
| `chargeStepTicks` | 10 |  | Ticks needed to gain one power scale. |
| `maxPowerScale` | 10 |  | Maximum power scale. |
| `damageMultiplierPerPowerScale` | 15 |  | Damage multiplier per power scale. |
| `cooldownSeconds` | 300 |  | Cooldown in seconds after firing. |

## `[BattleMode]`

| Option | Default | Range | Description |
|---|---|---|---|
| `epAcquirement` | 750,000 |  | EP required to learn Battle Mode. (unused) |
| `learningAuraCost` | 10,000 |  | Aura point cost used while learning Battle Mode. |
| `auraCostPerSecond` | 500 |  | Aura cost per second while locked on. |
| `lockRange` | 128 |  | Maximum lock range in blocks. |
| `cooldownSeconds` | 3 |  | Cooldown in seconds after locking or unlocking. |

## `[AirPalm]`

| Option | Default | Range | Description |
|---|---|---|---|
| `learningAuraCost` | 10,000 |  | Aura point cost used while learning Air Palm. |
| `auraCost` | 2,500 |  | Aura cost per use. |
| `cooldownSeconds` | 8 |  | Cooldown in seconds after use. |
| `damageMultiplier` | 3 |  | Damage multiplier applied to attack damage (split evenly between wind and gravity). |
| `range` | 16 |  | Range of the shockwave in blocks. |
| `width` | 2 |  | Half-width of the shockwave hitbox in blocks. |

## `[MaximumWill]`

| Option | Default | Range | Description |
|---|---|---|---|
| `learningAuraCost` | 15,000 |  | Aura point cost used while learning Maximum Will. |
| `auraCostPerSecond` | 12,000 |  | Aura cost per second while holding. |
| `damageMultiplier` | 5 |  | Damage multiplier on counter-attack release. |
| `masteredDamageMultiplier` | 10 |  | Mastered damage multiplier on counter-attack release. |
| `masteredMpCostPerSecond` | 5,000 |  | MP cost per second while holding and mastered. |
| `cooldownSeconds` | 10 |  | Cooldown in seconds after releasing Maximum Will. |

## `[GravityHammer]`

| Option | Default | Range | Description |
|---|---|---|---|
| `learningAuraCost` | 10,000 |  | Aura used while learning. |
| `auraCost` | 2,550 |  | Aura cost per use. |
| `cooldownSeconds` | 10 |  | Cooldown in seconds. |
| `baseDamage` | 100 |  | Base gravity damage dealt. |
| `masteredDamage` | 250 |  | Mastered gravity damage dealt. |
| `radius` | 10 |  | Radius in blocks to affect. |
| `knockupStrength` | 1.5 |  | Upward knockup velocity. |

## `[NightStrike]`

| Option | Default | Range | Description |
|---|---|---|---|
| `learningAuraCost` | 10,000 |  | Aura used while learning. |
| `auraCost` | 12,500 |  | Aura cost per activation (each stage). |
| `cooldownSeconds` | 15 |  | Cooldown in seconds after detonation. |
| `strikeMultiplier` | 2 |  | First strike damage multiplier. |
| `detonationMultiplier` | 10 |  | Blood Mist detonation damage multiplier. |
| `range` | 16 |  | Targeting range in blocks. |
