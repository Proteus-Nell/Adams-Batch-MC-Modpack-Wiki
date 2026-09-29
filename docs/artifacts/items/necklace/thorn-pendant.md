# Thorn Pendant

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Necklace](index.md)</small>

<div class="infobox" markdown>

![Thorn Pendant](../../../assets/icons/artifacts/item/thorn_pendant.png)

| | |
|---|---|
| **ID** | `artifacts:thorn_pendant` |
| **Category** | Necklace |
| **Curio slot** | Necklace |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Thorn Pendant into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Poisons anyone who dares to attack the relic bearer.

Found in loot chests of kind: chests in jungle/tropical biomes.

#### Poisonous Defense

*Passive. Ability max level 10.*

Has a **10-20 (up to 25-50)**% chance to reflect **5-15 (up to 10-30)**% damage and apply poison to the target attacking the player for **2-4 (up to 8-16)** seconds.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Multiplier | 5-15 | +10% of base per level | 10-30 |
| Time | 2-4 | +30% of base per level | 8-16 |
| Chance | 10-20 | +15% of base per level | 25-50 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/thorn_pendant` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `thorn_pendant.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `thorn_pendant.strikeChance` | 0.5 | The probability that the Thorn Pendant damages an attacking entity |
| `thorn_pendant.maxDamage` | 6 | The maximum amount of damage that is dealt when the Thorn Pendant activates |
| `thorn_pendant.minDamage` | 2 | The minimum amount of damage that is dealt when the Thorn Pendant activates |
| `thorn_pendant.cooldown` | 0 | The duration in seconds the Thorn Pendant goes on cooldown for after activating |

## Tags

`artifacts:artifacts`, `artifacts:slot/necklace`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
