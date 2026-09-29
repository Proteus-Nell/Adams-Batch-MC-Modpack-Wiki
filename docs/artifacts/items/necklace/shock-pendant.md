# Shock Pendant

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Necklace](index.md)</small>

<div class="infobox" markdown>

![Shock Pendant](../../../assets/icons/artifacts/item/shock_pendant.png)

| | |
|---|---|
| **ID** | `artifacts:shock_pendant` |
| **Category** | Necklace |
| **Curio slot** | Necklace |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Shock Pendant into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Strikes with lightning anyone who dares to attack the relic bearer.

Found in loot chests of kind: chests in mountain biomes.

#### Electric Resistance

*Passive. Ability max level 10.*

Grants complete resistance to lightning damage.

#### Lightning Defense

*Passive. Ability max level 10.*

Has a **10-20 (up to 20-40)**% chance to strike the target attacking the player with lightning, dealing **1-3 (up to 3-9)** damage.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Damage | 1-3 | +20% of base per level | 3-9 |
| Chance | 10-20 | +10% of base per level | 20-40 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/shock_pendant` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `shock_pendant.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `shock_pendant.strikeChance` | 0.25 | The probability that the Shock Pendant strikes an attacking entity with lightning |
| `shock_pendant.cancelLightningDamage` | true | Whether the Shock Pendant cancels damage from lightning |
| `shock_pendant.cooldown` | 0 | The amount of time in seconds the Shock Pendant goes on cooldown for after striking an attacker with lightning |

## Tags

`artifacts:artifacts`, `artifacts:slot/necklace`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
