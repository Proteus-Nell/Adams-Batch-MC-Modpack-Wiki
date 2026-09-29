# Lucky Scarf

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Necklace](index.md)</small>

<div class="infobox" markdown>

![Lucky Scarf](../../../assets/icons/artifacts/item/lucky_scarf.png)

| | |
|---|---|
| **ID** | `artifacts:lucky_scarf` |
| **Category** | Necklace |
| **Curio slot** | Necklace |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Lucky Scarf into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Increases Luck level when mining blocks.

Found in loot chests of kind: mineshaft chests, chests in cave biomes.

#### Treasure Hunter

*Passive. Ability max level 10.*

Has a **10-20 (up to 35-70)**% chance to apply an additional level of Luck to mined blocks. If successful, the ability repeats, adding another Luck level. This continues until the chance fails, summing all levels.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Chance | 10-20 | +25% of base per level | 35-70 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/lucky_scarf` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `lucky_scarf.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `lucky_scarf.fortuneLevelBonus` | 1 | The amount of extra levels of fortune that are granted by the Lucky Scarf |

## Tags

`artifacts:artifacts`, `artifacts:slot/necklace`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
