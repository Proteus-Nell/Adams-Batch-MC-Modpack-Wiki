# Cross Necklace

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Necklace](index.md)</small>

<div class="infobox" markdown>

![Cross Necklace](../../../assets/icons/artifacts/item/cross_necklace.png)

| | |
|---|---|
| **ID** | `artifacts:cross_necklace` |
| **Category** | Necklace |
| **Curio slot** | Necklace |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Cross Necklace into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Envelops the relic bearer in a protective aura, granting temporary invulnerability after each hit taken.

Found in loot chests of kind: chests in desert biomes.

#### Invincibility

*Passive. Ability max level 10.*

Increases the duration of invulnerability after taking damage by **0.3-0.5 (up to 0.9-1.5)** seconds.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Modifier | 0.3-0.5 | +20% of base per level | 0.9-1.5 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/cross_necklace` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `cross_necklace.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `cross_necklace.bonusInvincibilityTicks` | 20 | The amount of extra ticks the player stays invincible for after taking damage while wearing the Cross Necklace |
| `cross_necklace.cooldown` | 0 | The duration in seconds the Cross Necklace goes on cooldown for after activating |

## Tags

`artifacts:artifacts`, `artifacts:slot/necklace`, `minecraft:piglin_loved`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
