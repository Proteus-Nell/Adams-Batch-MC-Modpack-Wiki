# Charm of Sinking

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Necklace](index.md)</small>

<div class="infobox" markdown>

![Charm of Sinking](../../../assets/icons/artifacts/item/charm_of_sinking.png)

| | |
|---|---|
| **ID** | `artifacts:charm_of_sinking` |
| **Category** | Necklace |
| **Curio slot** | Necklace |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Charm of Sinking into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Grants the relic bearer's legs the ability to absorb air from the ground.

Found in loot chests of kind: chests in ocean/river biomes.

#### Anchor

*Passive. Ability max level 10.*

Doubles the player's sinking speed.

#### Diver

*Passive. Ability max level 10.*

While the player stands on the underwater floor, it blocks air consumption and slowly restores its supply by **0.2-0.4 (up to 0.6-1.2)** seconds every second.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Air | 0.2-0.4 | +20% of base per level | 0.6-1.2 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/charm_of_sinking` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `charm_of_sinking.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `charm_of_sinking.enabled` | true | Whether the Charm of Sinking removes the wearer's collision with water |
| `charm_of_sinking.underwaterFallDamage` | false | Whether it is possible to take fall damage underwater when wearing the Charm of Sinking |
| `charm_of_sinking.oxygenBonus` | 1.5 | How much longer players wearing the Charm of Sinking can stay underwater |

## Tags

`artifacts:artifacts`, `artifacts:slot/necklace`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
