# Helium Flamingo

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Belt](index.md)</small>

<div class="infobox" markdown>

![Helium Flamingo](../../../assets/icons/artifacts/item/helium_flamingo.png)

| | |
|---|---|
| **ID** | `artifacts:helium_flamingo` |
| **Category** | Belt |
| **Curio slot** | Belt |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Helium Flamingo into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Temporarily allows the relic bearer to glide through air as they would water.

Found in loot chests of kind: chests in ocean/river biomes, any End chest, End and stronghold chests.

#### Air Swimmer

*Passive. Ability max level 10.*

When performing a double jump, allows the player to float in the air for up to **3-5 (up to 9-15)** seconds. Movement speed in the air is proportional to the player's swimming speed with an additional bonus of **20-30 (up to 60-90)**%.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Time | 3-5 | +20% of base per level | 9-15 |
| Speed | 20-30 | +20% of base per level | 60-90 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/helium_flamingo` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `helium_flamingo.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `helium_flamingo.flightDuration` | 8 | The amount of time in seconds a player can fly with the Helium Flamingo before needing to recharge |
| `helium_flamingo.rechargeDuration` | 15 | The amount of time in seconds it takes for the Helium Flamingo to recharge |
| `helium_flamingo.cooldown` | 3 | The duration in seconds the Helium Flamingo goes on cooldown for when stopping flight |

## Tags

`artifacts:artifacts`, `artifacts:slot/belt`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
