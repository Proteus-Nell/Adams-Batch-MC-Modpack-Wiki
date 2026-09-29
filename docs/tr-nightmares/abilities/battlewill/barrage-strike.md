# Barrage Strike

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `trnightmare:barrage_strike` |
| **Cooldowns (s)** | 10 |
| **Activation** | Press |

</div>

> Blink onto your target and unleash a rapid multi-hit combo.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 10,000 or 0 |

## How it works

- Activated by pressing the skill key

## Stats (config defaults)

Set in [`config/nightmare/ability/battlewill/nightmare_battlewill.toml`](../../configs/config-nightmare-ability-battlewill-nightmare-battlewill.md).

| Option | Default | Description |
|---|---|---|
| `BarrageStrike.epAcquirement` | 400,000 | EP required to learn Barrage Strike. (unused) |
| `BarrageStrike.learningAuraCost` | 10,000 | Aura point cost used while learning Barrage Strike. |
| `BarrageStrike.auraCost` | 0 | Aura cost per use. |
| `BarrageStrike.cooldownSeconds` | 10 | Cooldown in seconds after use. |
| `BarrageStrike.hits` | 4 | Number of hits while unmastered. |
| `BarrageStrike.hitsMastered` | 8 | Number of hits while mastered. |
| `BarrageStrike.baseDamageMultiplier` | 1 | Base damage multiplier. |
| `BarrageStrike.masteredDamageMultiplier` | 2 | Mastered damage multiplier. |
| `BarrageStrike.range` | 12 | Targeting range. |
