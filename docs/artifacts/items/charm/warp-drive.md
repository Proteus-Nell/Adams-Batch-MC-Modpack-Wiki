# Warp Drive

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Charm](index.md)</small>

<div class="infobox" markdown>

![Warp Drive](../../../assets/icons/artifacts/item/warp_drive.png)

| | |
|---|---|
| **ID** | `artifacts:warp_drive` |
| **Category** | Charm |
| **Curio slot** | Charm |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Warp Drive into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Allows the relic bearer to teleport their body over short distances.

Found in loot chests of kind: End and stronghold chests, any End chest.

#### Translocation

*Active (instantaneous). Ability max level 10.*

Teleports the player to a position along their line of sight within **5-15 (up to 33-100)** blocks, then goes on a cooldown for **5-4 (up to 1.2-1)** seconds.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Distance | 5-15 | +56.5% of base per level | 33-100 |
| Cooldown | 5-4 | -7.5% of base per level | 1.2-1 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/warp_drive` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `warp_drive.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `warp_drive.enabled` | true | Whether the Warp Drive causes ender pearls to not be consumed |
| `warp_drive.hungerCost` | 2 | How many hunger points it costs to throw an Ender Pearl using the Warp Drive |
| `warp_drive.nullifyEnderPearlDamage` | true | Whether the Warp Drive causes Ender Pearls not to deal any damage |
| `warp_drive.cooldown` | 0 | The duration Ender Pearls go on cooldown for after being thrown using the Warp Drive |

## Tags

`artifacts:artifacts`, `artifacts:slot/charm`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
