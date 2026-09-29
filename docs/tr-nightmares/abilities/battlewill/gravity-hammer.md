# Gravity Hammer

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `trnightmare:gravity_hammer` |
| **Cooldowns (s)** | 10 |
| **Activation** | Press |

</div>

> Crush the ground with gravity force, damaging and launching nearby grounded enemies upward.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 10,000 or 2,550 |

## How it works

- Activated by pressing the skill key
- Does something when mastered

## Related

- **Related skills:** [Gravity Manipulation](../../../tensura-reincarnated/abilities/extra-skills/gravity-manipulation.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/battlewill/nightmare_battlewill.toml`](../../configs/config-nightmare-ability-battlewill-nightmare-battlewill.md).

| Option | Default | Description |
|---|---|---|
| `GravityHammer.learningAuraCost` | 10,000 | Aura used while learning. |
| `GravityHammer.auraCost` | 2,550 | Aura cost per use. |
| `GravityHammer.cooldownSeconds` | 10 | Cooldown in seconds. |
| `GravityHammer.baseDamage` | 100 | Base gravity damage dealt. |
| `GravityHammer.masteredDamage` | 250 | Mastered gravity damage dealt. |
| `GravityHammer.radius` | 10 | Radius in blocks to affect. |
| `GravityHammer.knockupStrength` | 1.5 | Upward knockup velocity. |
