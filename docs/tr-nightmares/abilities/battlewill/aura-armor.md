# Aura Armor

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `trnightmare:aura_armor` |
| **Cooldowns (s)** | 5 |
| **Activation** | Toggle |

</div>

> While active, convert your Max Aura into bonus Attack Damage and Armor.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 10,000 or 0 |

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

## Stats (config defaults)

Set in [`config/nightmare/ability/battlewill/nightmare_battlewill.toml`](../../configs/config-nightmare-ability-battlewill-nightmare-battlewill.md).

| Option | Default | Description |
|---|---|---|
| `AuraArmor.epAcquirement` | 500,000 | EP required to learn Aura Armor. (unused) |
| `AuraArmor.learningAuraCost` | 10,000 | Aura point cost used while learning Aura Armor. |
| `AuraArmor.auraStep` | 50,000 | Aura step size used for scaling. |
| `AuraArmor.maxAuraCounted` | 500,000 | Maximum aura value counted for scaling. |
| `AuraArmor.attackBonusPerStep` | 1 | Attack damage gained per step. |
| `AuraArmor.armorBonusPerStep` | 4 | Armor gained per step. |
| `AuraArmor.cooldownSeconds` | 5 | Cooldown in seconds after toggling. |
