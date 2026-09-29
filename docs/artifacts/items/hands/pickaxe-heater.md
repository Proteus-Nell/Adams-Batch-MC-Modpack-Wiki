# Pickaxe Heater

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Hands](index.md)</small>

<div class="infobox" markdown>

![Pickaxe Heater](../../../assets/icons/artifacts/item/pickaxe_heater.png)

| | |
|---|---|
| **ID** | `artifacts:pickaxe_heater` |
| **Category** | Hands |
| **Curio slot** | Hands |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Pickaxe Heater into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Concentrates surrounding heat precisely onto the relic bearer's tools.

Found in loot chests of kind: chests in cave biomes, mineshaft chests.

#### Heat Concentration

*Active (toggleable). Ability max level 10.*

Smelts any mined block if possible, consuming one charge from a buffer with a capacity of **20-25 (up to 70-75)** units. The buffer regenerates 1 charge every **7-6 (up to 1.2-1)** seconds.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Capacity | 20-25 | +5 per level | 70-75 |
| Duration | 7-6 | -8.3% of base per level | 1.2-1 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/pickaxe_heater` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `pickaxe_heater.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `pickaxe_heater.enabled` | true | Whether the Pickaxe Heater smelts mined ores |

## Tags

`artifacts:artifacts`, `artifacts:slot/hands`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
