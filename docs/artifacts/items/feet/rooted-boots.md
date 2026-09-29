# Rooted Boots

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Feet](index.md)</small>

<div class="infobox" markdown>

![Rooted Boots](../../../assets/icons/artifacts/item/rooted_boots.png)

| | |
|---|---|
| **ID** | `artifacts:rooted_boots` |
| **Category** | Feet |
| **Curio slot** | Feet |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Rooted Boots into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Grants the relic bearer the mysterious power of a sheep.

Found in loot chests of kind: any Overworld chest.

#### Herbivory

*Active (toggleable). Ability max level 10.*

Every **7-6 (up to 2-1.7)** seconds transforms the grass block beneath the player into dirt, restoring 1 hunger and saturation point.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Frequency | 7-6 | -7.1% of base per level | 2-1.7 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/rooted_boots` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `rooted_boots.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `rooted_boots.enabled` | true | Whether the Rooted Boots replenish hunger when standing on grass |
| `rooted_boots.hungerReplenishingDuration` | 10 | The amount of time in seconds it takes to replenish a single point of hunger while wearing the Rooted Boots |
| `rooted_boots.growPlantsAfterEating` | true | Whether the Rooted Boots apply a bone meal effect after eating food |

## Tags

`artifacts:artifacts`, `artifacts:slot/feet`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
