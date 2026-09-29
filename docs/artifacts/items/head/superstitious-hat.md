# Superstitious Hat

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Head](index.md)</small>

<div class="infobox" markdown>

![Superstitious Hat](../../../assets/icons/artifacts/item/superstitious_hat.png)

| | |
|---|---|
| **ID** | `artifacts:superstitious_hat` |
| **Category** | Head |
| **Curio slot** | Head |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Superstitious Hat into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Increases loot drops from defeated mobs.

Found in loot chests of kind: chests in cave biomes, mineshaft chests.

#### Big Loot

*Passive. Ability max level 10.*

Has a **10-20 (up to 35-70)**% chance to apply an additional level of Looting to defeated mobs. If successful, the ability repeats, adding another Looting level. This continues until the chance fails, summing all levels.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Chance | 10-20 | +25% of base per level | 35-70 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/superstitious_hat` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `superstitious_hat.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `superstitious_hat.lootingLevelBonus` | 1 | The amount of extra levels of Looting that are granted by the Superstitious Hat |

## Tags

`artifacts:artifacts`, `artifacts:slot/head`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
