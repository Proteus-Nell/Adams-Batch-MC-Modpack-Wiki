# Umbrella

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Miscellaneous](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `artifacts:umbrella` |
| **Category** | Miscellaneous |

</div>

## Description

Slows your fall when held

Can be used as a shield

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Umbrella into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **15**, first level costs **100** XP, +100 XP per level.

> Softens the fall, providing safe landing from any height. When skillfully used, it can serve as a reliable shield, keeping enemies at bay.

Found in loot chests of kind: village and pillager chests, chests in mountain biomes.

#### Soft Fall

*Passive. Ability max level 10.*

When held in hand, reduces the player's vertical speed, negating fall damage. Pressing LMB propels the player backward and triggers a cooldown of **2-1.5 (up to 0.6-0.4)** seconds. The push can be used up to **1-3 (up to 11-13)** times in succession before the player touches the ground.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Count | 1-3 | +1 per level | 11-13 |
| Cooldown | 2-1.5 | -7% of base per level | 0.6-0.4 |

#### Air Shield

*Unlocks at relic level 5, passive. Ability max level 10.*

When used, functions as a shield, pushing targets up to **1-3 (up to 2-6)** blocks away.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Knockback | 1-3 | +10% of base per level | 2-6 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/umbrella` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `umbrella.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `umbrella.isShield` | true | Whether the Umbrella can be used as a shield |
| `umbrella.isGlider` | true | Whether the Umbrella slows the player's falling speed when held |

## Tags

`artifacts:artifacts`, `origins:shields`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
