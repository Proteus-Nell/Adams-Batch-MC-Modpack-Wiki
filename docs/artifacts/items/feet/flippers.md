# Flippers

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Feet](index.md)</small>

<div class="infobox" markdown>

![Flippers](../../../assets/icons/artifacts/item/flippers.png)

| | |
|---|---|
| **ID** | `artifacts:flippers` |
| **Category** | Feet |
| **Curio slot** | Feet |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Flippers into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Strengthens the relic bearer's legs, allowing them to swim faster.

Found in loot chests of kind: chests in ocean/river biomes.

#### Fish Tail

*Passive. Ability max level 10.*

Increases the player's swimming speed by **20-40 (up to 70-140)**%.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Modifier | 20-40 | +25% of base per level | 70-140 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/flippers` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `flippers.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `flippers.swimSpeedBonus` | 0.7 | How much the Flippers increase the wearer's swim speed |

## Tags

`artifacts:artifacts`, `artifacts:slot/feet`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
