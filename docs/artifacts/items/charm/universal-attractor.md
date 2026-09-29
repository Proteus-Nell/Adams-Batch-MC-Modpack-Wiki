# Universal Attractor

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Charm](index.md)</small>

<div class="infobox" markdown>

![Universal Attractor](../../../assets/icons/artifacts/item/universal_attractor.png)

| | |
|---|---|
| **ID** | `artifacts:universal_attractor` |
| **Category** | Charm |
| **Curio slot** | Charm |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Universal Attractor into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Manipulates a weak magnetic field around the relic bearer, controlling the gravity of nearby items.

Found in loot chests of kind: chests in cave biomes, mineshaft chests.

#### Magnetism

*Active (interruptible). Ability max level 10.*

A toggleable ability with 3 modes: Attraction, Repulsion, and Neutrality. In the red Attraction mode, items within a radius of **3-5 (up to 13-15)** blocks are drawn toward the player. In the blue Repulsion mode, items are pushed away. The purple Neutrality mode disables the relic's effect.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Radius | 3-5 | +1 per level | 13-15 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/universal_attractor` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `universal_attractor.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `universal_attractor.magnetismLevel` | 5 | The level of the magnetism effect that is applied by the Universal Attractor |

## Tags

`artifacts:artifacts`, `artifacts:slot/charm`, `minecraft:piglin_loved`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
