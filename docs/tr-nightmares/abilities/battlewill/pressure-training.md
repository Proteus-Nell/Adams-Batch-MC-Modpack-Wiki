# Pressure Training

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `trnightmare:pressure_training` |
| **Modes** | 7 |
| **Cooldowns (s)** | 8 |
| **Activation** | Press, Hold |

</div>

> Cycle damage types while sneaking, then endure that damage to train your resistances.

## Modes

| # | Mode |
|---|---|
| 1 | Pressure Type: Physical |
| 2 | Pressure Type: Fire |
| 3 | Pressure Type: Water |
| 4 | Pressure Type: Earth |
| 5 | Pressure Type: Lightning |
| 6 | Pressure Type: Wind |
| 7 | Pressure Type: Spiritual |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 10,000 or 1,000 |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Stats (config defaults)

Set in [`config/nightmare/ability/battlewill/nightmare_battlewill.toml`](../../configs/config-nightmare-ability-battlewill-nightmare-battlewill.md).

| Option | Default | Description |
|---|---|---|
| `PressureTraining.epAcquirement` | 750,000 | EP required to learn Pressure Training. (unused) |
| `PressureTraining.learningAuraCost` | 10,000 | Aura point cost used while learning Pressure Training. |
| `PressureTraining.auraCostPerSecond` | 1,000 | Aura cost per second. |
| `PressureTraining.selfDamagePerSecond` | 50 | Self-damage per second. |
| `PressureTraining.cooldownSeconds` | 8 | Cooldown in seconds after release. |
