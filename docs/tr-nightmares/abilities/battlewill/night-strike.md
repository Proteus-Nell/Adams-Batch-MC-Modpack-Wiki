# Night Strike

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `trnightmare:night_strike` |
| **Cooldowns (s)** | 15 |
| **Activation** | Press |

</div>

> Warp behind your target for a devastating opener, apply Blood Mist, then activate again to detonate it.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base aura cost)* | 10,000 or 12,500 |

## How it works

- Activated by pressing the skill key

## Stats (config defaults)

Set in [`config/nightmare/ability/battlewill/nightmare_battlewill.toml`](../../configs/config-nightmare-ability-battlewill-nightmare-battlewill.md).

| Option | Default | Description |
|---|---|---|
| `NightStrike.learningAuraCost` | 10,000 | Aura used while learning. |
| `NightStrike.auraCost` | 12,500 | Aura cost per activation (each stage). |
| `NightStrike.cooldownSeconds` | 15 | Cooldown in seconds after detonation. |
| `NightStrike.strikeMultiplier` | 2 | First strike damage multiplier. |
| `NightStrike.detonationMultiplier` | 10 | Blood Mist detonation damage multiplier. |
| `NightStrike.range` | 16 | Targeting range in blocks. |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- Blood Mist applied — strike again to detonate!
- Blood Mist detonated!

</details>
