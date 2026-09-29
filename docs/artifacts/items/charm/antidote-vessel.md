# Antidote Vessel

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Charm](index.md)</small>

<div class="infobox" markdown>

![Antidote Vessel](../../../assets/icons/artifacts/item/antidote_vessel.png)

| | |
|---|---|
| **ID** | `artifacts:antidote_vessel` |
| **Category** | Charm |
| **Curio slot** | Charm |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Antidote Vessel into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **15**, first level costs **100** XP, +100 XP per level.

> Enhances the relic bearer's resistance to effects.

Found in loot chests of kind: chests in jungle/tropical biomes.

#### Poison Resistance

*Passive. Ability max level 10.*

Reduces the duration of negative effects received by **20-40 (up to 40-80)**%.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Amount | 20-40 | +10% of base per level | 40-80 |

#### Alchemical Touch

*Unlocks at relic level 5, passive. Ability max level 10.*

Each successful attack steals **1-1.5 (up to 5-7.5)** seconds from all positive effects present on the target.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Duration | 1-1.5 | +40% of base per level | 5-7.5 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/antidote_vessel` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `antidote_vessel.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `antidote_vessel.enabled` | true | Whether the Antidote Vessel reduces the duration of negative effects |
| `antidote_vessel.maxEffectDuration` | 5 | The maximum duration in seconds negative mob effects can last when wearing the Antidote Vessel |

## Tags

`artifacts:artifacts`, `artifacts:slot/charm`, `minecraft:piglin_loved`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
