# Snowshoes

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Feet](index.md)</small>

<div class="infobox" markdown>

![Snowshoes](../../../assets/icons/artifacts/item/snowshoes.png)

| | |
|---|---|
| **ID** | `artifacts:snowshoes` |
| **Category** | Feet |
| **Curio slot** | Feet |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Snowshoes into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Improves the relic bearer's mobility in harsh snowy conditions.

Found in loot chests of kind: chests in snowy biomes, chests in taiga biomes, chests in mountain biomes.

#### Light Step

*Passive. Ability max level 10.*

Allows walking on powder snow without sinking.

#### Snow Walker

*Passive. Ability max level 10.*

Increases movement speed on snow by **20-40 (up to 40-80)**%.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Amount | 20-40 | +10% of base per level | 40-80 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/snowshoes` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `snowshoes.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `snowshoes.allowWalkingOnPowderedSnow` | true | Whether the Snowshoes allow the wearer to walk on powdered snow |
| `snowshoes.movementSpeedOnSnowBonus` | 0.3 | How much the Snowshoes increase the wearer's movement speed on snow blocks |

## Tags

`artifacts:artifacts`, `artifacts:slot/feet`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
