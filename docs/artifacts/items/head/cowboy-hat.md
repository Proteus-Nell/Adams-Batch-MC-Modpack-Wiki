# Cowboy Hat

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Head](index.md)</small>

<div class="infobox" markdown>

![Cowboy Hat](../../../assets/icons/artifacts/item/cowboy_hat.png)

| | |
|---|---|
| **ID** | `artifacts:cowboy_hat` |
| **Category** | Head |
| **Curio slot** | Head |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Cowboy Hat into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **15**, first level costs **100** XP, +100 XP per level.

> Enhances the agility of the relic bearer’s mounts.

Found in loot chests of kind: village and pillager chests, chests in savanna biomes.

#### Gallop

*Passive. Ability max level 10.*

Increases the movement speed, jump height, and safe fall height of mounts by **20-30 (up to 50-75)**%.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Speed | 20-30 | +15% of base per level | 50-75 |

#### Lasso

*Unlocks at relic level 5, active (instantaneous). Ability max level 10.*

When used, this ability allows you to ride and control any mob for up to **2-5 (up to 5-12.5)** seconds. After the time expires or dismounting, it goes on a 1-minute cooldown.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Time | 2-5 | +15% of base per level | 5-12.5 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/cowboy_hat` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `cowboy_hat.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `cowboy_hat.mountSpeedBonus` | 0.4 | How much the Cowboy Hat increases the speed of ridden mounts |

## Tags

`artifacts:artifacts`, `artifacts:slot/head`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
