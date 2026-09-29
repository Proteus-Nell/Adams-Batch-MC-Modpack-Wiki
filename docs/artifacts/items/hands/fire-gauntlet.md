# Fire Gauntlet

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Hands](index.md)</small>

<div class="infobox" markdown>

![Fire Gauntlet](../../../assets/icons/artifacts/item/fire_gauntlet.png)

| | |
|---|---|
| **ID** | `artifacts:fire_gauntlet` |
| **Category** | Hands |
| **Curio slot** | Hands |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Fire Gauntlet into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Grants the relic bearer’s weapon the powers of the fire element.

Found in loot chests of kind: fire/Nether-themed chests (and ruined portals), any Nether chest.

#### Fire Wave

*Passive. Ability max level 10.*

When attacking, releases several sparks that home in on nearby targets, igniting them for **1.5-2.5 (up to 6-10)** seconds and dealing **5-15 (up to 16-50)**% of the performed attack's damage. The number of sparks is determined through repeated checks of a **20-30 (up to 50-75)**% chance. Each successful check releases one additional spark, but the process stops as soon as the chance fails even once.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Chance | 20-30 | +15% of base per level | 50-75 |
| Damage | 5-15 | +23.5% of base per level | 16-50 |
| Duration | 1.5-2.5 | +30% of base per level | 6-10 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/fire_gauntlet` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `fire_gauntlet.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `fire_gauntlet.fireDuration` | 8 | How long an entity is set on fire for after being attacked by an entity wearing the Fire Gauntlet |

## Tags

`artifacts:artifacts`, `artifacts:slot/hands`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
