# Spiral Penetrator

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `trnightmare:spiral_penetrator` |
| **Cooldowns (s)** | 300 |
| **Activation** | Press, Hold |

</div>

> Charge up power scales, then lunge through your target with a piercing strike.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 25,000 |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Stats (config defaults)

Set in [`config/nightmare/ability/battlewill/nightmare_battlewill.toml`](../../configs/config-nightmare-ability-battlewill-nightmare-battlewill.md).

| Option | Default | Description |
|---|---|---|
| `SpiralPenetrator.epAcquirement` | 750,000 | EP required to learn Spiral Penetrator. (unused) |
| `SpiralPenetrator.learningAuraCost` | 25,000 | Aura point cost used while learning Spiral Penetrator. |
| `SpiralPenetrator.auraCostPerPowerScale` | 25,000 | Aura cost per power scale. |
| `SpiralPenetrator.chargeStepTicks` | 10 | Ticks needed to gain one power scale. |
| `SpiralPenetrator.maxPowerScale` | 10 | Maximum power scale. |
| `SpiralPenetrator.damageMultiplierPerPowerScale` | 15 | Damage multiplier per power scale. |
| `SpiralPenetrator.cooldownSeconds` | 300 | Cooldown in seconds after firing. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- Spiral Penetrator  ▶  Charge: %1$s / %2$s  (%3$s dmg)

</details>
