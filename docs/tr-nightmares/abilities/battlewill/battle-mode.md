# Battle Mode

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `trnightmare:battle_mode` |
| **Cooldowns (s)** | 3 |
| **Activation** | Press |

</div>

> Lock onto the target in your sights. The lock breaks if they move too far, out-conceal your Presence Sense, or you release it.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 10,000 or 500 |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Related

- **Effects:** [Presence Sense](../../../tensura-reincarnated/effects/presence-sense.md), [Presence Concealment](../../../tensura-reincarnated/effects/presence-concealment.md), [Complete Concealment](../../effects/complete-concealment.md)
- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/nightmare/ability/battlewill/nightmare_battlewill.toml`](../../configs/config-nightmare-ability-battlewill-nightmare-battlewill.md).

| Option | Default | Description |
|---|---|---|
| `BattleMode.epAcquirement` | 750,000 | EP required to learn Battle Mode. (unused) |
| `BattleMode.learningAuraCost` | 10,000 | Aura point cost used while learning Battle Mode. |
| `BattleMode.auraCostPerSecond` | 500 | Aura cost per second while locked on. |
| `BattleMode.lockRange` | 128 | Maximum lock range in blocks. |
| `BattleMode.cooldownSeconds` | 3 | Cooldown in seconds after locking or unlocking. |

## In-game messages

<details markdown><summary>Show 3 messages</summary>

- Lock On — %1$s
- Locked onto %1$s
- Lock released

</details>
