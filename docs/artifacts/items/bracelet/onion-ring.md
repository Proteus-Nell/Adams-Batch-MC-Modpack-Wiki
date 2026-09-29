# Onion Ring

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Bracelet](index.md)</small>

<div class="infobox" markdown>

![Onion Ring](../../../assets/icons/artifacts/item/onion_ring.png)

| | |
|---|---|
| **ID** | `artifacts:onion_ring` |
| **Category** | Bracelet |
| **Curio slot** | Bracelet |

</div>

## What it does

Food.

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Onion Ring into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **15**, first level costs **100** XP, +100 XP per level.

> Enhances the relic bearer's block mining efficiency when sufficiently satiated.

Found in loot chests of kind: chests in cave biomes, mineshaft chests.

#### Miner's Hunger

*Passive. Ability max level 10.*

Increases block mining speed by **1-1.5 (up to 3-4.5)**% per unit of the player's saturation.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Amount | 1-1.5 | +20% of base per level | 3-4.5 |

#### Raw Appetite

*Unlocks at relic level 5, passive. Ability max level 10.*

When mining blocks, there is a **5-15 (up to 10-30)**% chance to restore 1 hunger point and 0.5 saturation to the player.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Chance | 5-15 | +10% of base per level | 10-30 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/onion_ring` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `onion_ring.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `onion_ring.hasteDurationPerFoodPoint` | 6 | The duration of haste that is applied per food point eaten while wearing the Onion Ring |
| `onion_ring.hasteLevel` | 2 | The level of the haste effect that is applied by the Onion Ring |

## Tags

`artifacts:artifacts`, `curios:bracelet`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
