# Feral Claws

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Hands](index.md)</small>

<div class="infobox" markdown>

![Feral Claws](../../../assets/icons/artifacts/item/feral_claws.png)

| | |
|---|---|
| **ID** | `artifacts:feral_claws` |
| **Category** | Hands |
| **Curio slot** | Hands |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Feral Claws into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Awakens a bloodthirsty instinct in the relic bearer, making them fight faster with each consecutive attack.

Found in loot chests of kind: any Overworld chest.

#### Beast's Fury

*Passive. Ability max level 10.*

Increases the player's attack speed by **5-15 (up to 11-33)**% for each consecutive attack performed within 3 seconds of the last. Otherwise, loses 1 charge per second. Attacking with an unfilled attack speed bar resets the accumulated charges.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Modifier | 5-15 | +12% of base per level | 11-33 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/feral_claws` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `feral_claws.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `feral_claws.attackSpeedBonus` | 0.3 | How much the Feral Claws increase the wearer's attack speed |

## Tags

`artifacts:artifacts`, `artifacts:slot/hands`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
