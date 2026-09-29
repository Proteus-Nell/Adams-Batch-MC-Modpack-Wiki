# Chorus Totem

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Charm](index.md)</small>

<div class="infobox" markdown>

![Chorus Totem](../../../assets/icons/artifacts/item/chorus_totem.png)

| | |
|---|---|
| **ID** | `artifacts:chorus_totem` |
| **Category** | Charm |
| **Curio slot** | Charm |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Chorus Totem into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Allows the relic bearer to rewind time when making rash decisions.

Found in loot chests of kind: End and stronghold chests, any End chest.

#### Temporal Loop

*Passive. Ability max level 10.*

Each attack against the relic bearer has a **2-4 (up to 4-7)**% chance per percent of missing health to teleport the attacker to a random location within a **5-7 (up to 10-14)** block radius.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Chance | 2-4 | +10% of base per level | 4-7 |
| Radius | 5-7 | +10% of base per level | 10-14 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/chorus_totem` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `chorus_totem.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `chorus_totem.consumeOnUse` | true | Whether the Chorus Totem is consumed after activating |
| `chorus_totem.teleportationChance` | 1 | The probability that the Chorus Totem activates when a player dies |
| `chorus_totem.healthRestored` | 9 | The amount of health points that are restored after the Chorus Totem activates |
| `chorus_totem.cooldown` | 0 | The duration in seconds the Chorus Totem goes on cooldown for after activating |

## Tags

`artifacts:artifacts`, `artifacts:slot/charm`, `hardcorerevival:passthrough_death_when_held`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
