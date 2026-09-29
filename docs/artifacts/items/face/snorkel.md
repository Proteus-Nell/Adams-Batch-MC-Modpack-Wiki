# Snorkel

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Face](index.md)</small>

<div class="infobox" markdown>

![Snorkel](../../../assets/icons/artifacts/item/snorkel.png)

| | |
|---|---|
| **ID** | `artifacts:snorkel` |
| **Category** | Face |
| **Curio slot** | Face |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Snorkel into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Allows for longer underwater exploration without the risk of drowning.

Found in loot chests of kind: chests in ocean/river biomes.

#### Clear Vision

*Passive. Ability max level 10.*

Removes the fog effect in liquids.

#### Breath Control

*Passive. Ability max level 10.*

Applies a water breathing effect for **5-10 (up to 15-30)** seconds upon full submersion.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Duration | 5-10 | +20% of base per level | 15-30 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/snorkel` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `snorkel.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `snorkel.isInfinite` | false | Whether the Snorkel's water breathing effect depletes when underwater |
| `snorkel.waterBreathingDuration` | 30 | The duration of the water breathing effect that is applied by the Snorkel |

## Tags

`artifacts:artifacts`, `artifacts:slot/face`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
