# Vortex Punch

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `trnightmare:vortex_punch` |
| **Cooldowns (s)** | 8 |
| **Activation** | Press |

</div>

> Drag your target in, then shatter them with a wind-boosted impact. Requires empty hands.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 10,000 or 400 |

## How it works

- Activated by pressing the skill key

## Stats (config defaults)

Set in [`config/nightmare/ability/battlewill/nightmare_battlewill.toml`](../../configs/config-nightmare-ability-battlewill-nightmare-battlewill.md).

| Option | Default | Description |
|---|---|---|
| `VortexPunch.epAcquirement` | 400,000 | EP required to learn Vortex Punch. (unused) |
| `VortexPunch.learningAuraCost` | 10,000 | Aura point cost used while learning Vortex Punch. |
| `VortexPunch.auraCost` | 400 | Aura cost per use. |
| `VortexPunch.cooldownSeconds` | 8 | Cooldown in seconds after use. |
| `VortexPunch.baseDamageMultiplier` | 2.5 | Base damage multiplier. |
| `VortexPunch.masteredDamageMultiplier` | 5 | Mastered damage multiplier. |
| `VortexPunch.range` | 12 | Reach for target selection. |
