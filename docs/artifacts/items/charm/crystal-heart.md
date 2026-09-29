# Crystal Heart

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Charm](index.md)</small>

<div class="infobox" markdown>

![Crystal Heart](../../../assets/icons/artifacts/item/crystal_heart.png)

| | |
|---|---|
| **ID** | `artifacts:crystal_heart` |
| **Category** | Charm |
| **Curio slot** | Charm |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Crystal Heart into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Grants the relic bearer extra strength by increasing their maximum health.

Found in loot chests of kind: chests in cave biomes, mineshaft chests.

#### Will to Live

*Passive. Ability max level 10.*

Increases the player's maximum health by **2-6 (up to 6-18)** points.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Amount | 2-6 | +20% of base per level | 6-18 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/crystal_heart` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `crystal_heart.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `crystal_heart.healthBonus` | 10 | The amount of extra health points that are granted by the Crystal Heart |

## Tags

`artifacts:artifacts`, `artifacts:slot/charm`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
