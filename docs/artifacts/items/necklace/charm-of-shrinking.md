# Charm of Shrinking

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Necklace](index.md)</small>

<div class="infobox" markdown>

![Charm of Shrinking](../../../assets/icons/artifacts/item/charm_of_shrinking.png)

| | |
|---|---|
| **ID** | `artifacts:charm_of_shrinking` |
| **Category** | Necklace |
| **Curio slot** | Necklace |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Charm of Shrinking into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Allows the relic bearer to shrink their body to access previously unreachable areas.

Found in loot chests of kind: chests in cave biomes, mineshaft chests.

#### Compression

*Passive. Ability max level 10.*

Reduces the player's size by **20-30 (up to 40-60)**%.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Multiplier | 20-30 | +10% of base per level | 40-60 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/charm_of_shrinking` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `charm_of_shrinking.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `charm_of_shrinking.scaleModifier` | -0.5 | How much the Charm of Shrinking decreases or increases the player's Scale<br>Values between -1 and 0 reduce the player's scale<br>Values above 0 increase the player's scale |

## Tags

`artifacts:artifacts`, `artifacts:slot/necklace`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
