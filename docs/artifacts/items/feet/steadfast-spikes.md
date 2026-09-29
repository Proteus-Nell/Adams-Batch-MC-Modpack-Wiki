# Steadfast Spikes

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Feet](index.md)</small>

<div class="infobox" markdown>

![Steadfast Spikes](../../../assets/icons/artifacts/item/steadfast_spikes.png)

| | |
|---|---|
| **ID** | `artifacts:steadfast_spikes` |
| **Category** | Feet |
| **Curio slot** | Feet |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Steadfast Spikes into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Firmly anchors the relic bearer's feet to any surface.

Found in loot chests of kind: chests in cave biomes, mineshaft chests, chests in mountain biomes.

#### Clinging Claws

*Passive. Ability max level 10.*

Allows slow wall sliding, negating fall damage.

#### Grip

*Passive. Ability max level 10.*

Increases resistance to knockback and slippery blocks by **20-30 (up to 50-75)**%.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Modifier | 20-30 | +15% of base per level | 50-75 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/steadfast_spikes` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `steadfast_spikes.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `steadfast_spikes.knockbackResistance` | 1 | How much knockback resistance is granted by the Steadfast Spikes |
| `steadfast_spikes.slipperinessReduction` | 1 | How much the Steadfast Spikes reduce the slipperiness of ice |

## Tags

`artifacts:artifacts`, `artifacts:slot/feet`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
