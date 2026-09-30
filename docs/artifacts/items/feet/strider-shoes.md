# Strider Shoes

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Feet](index.md)</small>

<div class="infobox" markdown>

![Strider Shoes](../../../assets/icons/artifacts/item/strider_shoes.png)

| | |
|---|---|
| **ID** | `artifacts:strider_shoes` |
| **Category** | Feet |
| **Curio slot** | Feet |

</div>

## What it does

Feet artifact. While you're **sneaking** you can walk across the surface of lava. They also make you immune to "hot floor" damage from standing on magma blocks and similar blocks.

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/strider_shoes` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `strider_shoes.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `strider_shoes.enabled` | true | Whether the Strider Shoes allow sneaking on lava |
| `strider_shoes.cancelHotFloorDamage` | true | Whether the Strider Shoes make the wearer immune to hot floor damage |

## Tags

`artifacts:artifacts`, `artifacts:slot/feet`
