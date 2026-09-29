# Villager Hat

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Head](index.md)</small>

<div class="infobox" markdown>

![Villager Hat](../../../assets/icons/artifacts/item/villager_hat.png)

| | |
|---|---|
| **ID** | `artifacts:villager_hat` |
| **Category** | Head |
| **Curio slot** | Head |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Villager Hat into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Reduces trading prices with villagers, making deals more profitable.

Found in loot chests of kind: village and pillager chests.

#### Innocent Appearance

*Passive. Ability max level 10.*

Prevents Iron Golems from attacking the player.

#### Trade Secret

*Passive. Ability max level 10.*

Increases the discount when trading with villagers by **10-20 (up to 40-80)**%.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Multiplier | 10-20 | +30% of base per level | 40-80 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/villager_hat` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `villager_hat.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `villager_hat.reputationBonus` | 75 | The amount of extra reputation that is granted by the Villager Hat when trading with villagers |

## Tags

`artifacts:artifacts`, `artifacts:slot/head`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
