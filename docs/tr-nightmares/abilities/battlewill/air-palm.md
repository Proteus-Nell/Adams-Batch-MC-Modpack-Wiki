# Air Palm

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `trnightmare:air_palm` |
| **Cooldowns (s)** | 8 |
| **Activation** | Press |

</div>

> Strike the air to launch a wide shockwave, splitting heavy Wind and Gravity damage across targets.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 10,000 or 2,500 |

## How it works

- Activated by pressing the skill key

## Stats (config defaults)

Set in [`config/nightmare/ability/battlewill/nightmare_battlewill.toml`](../../configs/config-nightmare-ability-battlewill-nightmare-battlewill.md).

| Option | Default | Description |
|---|---|---|
| `AirPalm.learningAuraCost` | 10,000 | Aura point cost used while learning Air Palm. |
| `AirPalm.auraCost` | 2,500 | Aura cost per use. |
| `AirPalm.cooldownSeconds` | 8 | Cooldown in seconds after use. |
| `AirPalm.damageMultiplier` | 3 | Damage multiplier applied to attack damage (split evenly between wind and gravity). |
| `AirPalm.range` | 16 | Range of the shockwave in blocks. |
| `AirPalm.width` | 2 | Half-width of the shockwave hitbox in blocks. |
