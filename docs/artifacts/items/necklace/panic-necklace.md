# Panic Necklace

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Necklace](index.md)</small>

<div class="infobox" markdown>

![Panic Necklace](../../../assets/icons/artifacts/item/panic_necklace.png)

| | |
|---|---|
| **ID** | `artifacts:panic_necklace` |
| **Category** | Necklace |
| **Curio slot** | Necklace |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Panic Necklace into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Quickens the relic bearer's heartbeat, warning of impending danger.

Found in loot chests of kind: chests in cave biomes, mineshaft chests.

#### Panic

*Passive. Ability max level 10.*

Increases the player's movement speed by **1-2 (up to 2-4)**% for each mob within a **6-8 (up to 12-16)** blocks radius targeting the player for attack.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Movement | 1-2 | +10% of base per level | 2-4 |
| Radius | 6-8 | +10% of base per level | 12-16 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/panic_necklace` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `panic_necklace.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `panic_necklace.speedLevel` | 1 | The level of the speed effect that is applied by the Panic Necklace |
| `panic_necklace.speedDuration` | 8 | The duration in seconds of the speed effect that is applied when taking damage while wearing the Panic Necklace |
| `panic_necklace.cooldown` | 0 | The duration in seconds the Panic Necklace goes on cooldown for after taking damage |

## Tags

`artifacts:artifacts`, `artifacts:slot/necklace`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
