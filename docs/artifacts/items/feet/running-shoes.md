# Running Shoes

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Feet](index.md)</small>

<div class="infobox" markdown>

![Running Shoes](../../../assets/icons/artifacts/item/running_shoes.png)

| | |
|---|---|
| **ID** | `artifacts:running_shoes` |
| **Category** | Feet |
| **Curio slot** | Feet |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Running Shoes into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Strengthens the relic bearer's legs, allowing them to move faster.

Found in loot chests of kind: village and pillager chests, chests in plains biomes.

#### Wide Stride

*Passive. Ability max level 10.*

Increases the player's running speed by **50-80 (up to 150-240)**%.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Speed | 50-80 | +20% of base per level | 150-240 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/running_shoes` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `running_shoes.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `running_shoes.sprintingSpeedBonus` | 0.4 | How much the Running Shoes increase the wearer's sprinting speed |
| `running_shoes.sprintingStepHeightBonus` | 0.5 | How much the Running Shoes increase the wearer's step height while sprinting |

## Tags

`artifacts:artifacts`, `artifacts:slot/feet`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
