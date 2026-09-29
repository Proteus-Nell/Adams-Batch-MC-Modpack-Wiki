# Flame Pendant

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Necklace](index.md)</small>

<div class="infobox" markdown>

![Flame Pendant](../../../assets/icons/artifacts/item/flame_pendant.png)

| | |
|---|---|
| **ID** | `artifacts:flame_pendant` |
| **Category** | Necklace |
| **Curio slot** | Necklace |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Flame Pendant into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Burns anyone who dares to attack the relic bearer.

Found in loot chests of kind: fire/Nether-themed chests (and ruined portals), any Nether chest.

#### Fiery Defense

*Passive. Ability max level 10.*

Has a **20-30 (up to 40-60)**% chance to ignite the target attacking the player for **2-3 (up to 8-12)** seconds.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Time | 2-3 | +30% of base per level | 8-12 |
| Chance | 20-30 | +10% of base per level | 40-60 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/flame_pendant` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `flame_pendant.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `flame_pendant.strikeChance` | 0.4 | The probability that the Flame Pendant lights an attacker on fire |
| `flame_pendant.fireDuration` | 10 | How long an attacking entity is set on fire for when the Flame Pendant activates |
| `flame_pendant.grantFireResistance` | true | Whether the Flame Pendant grants Fire Resistance after igniting an entity |
| `flame_pendant.cooldown` | 0 | The duration in seconds the Flame Pendant goes on cooldown for after setting an entity on fire |

## Tags

`artifacts:artifacts`, `artifacts:slot/necklace`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
