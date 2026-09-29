# Pocket Piston

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Hands](index.md)</small>

<div class="infobox" markdown>

![Pocket Piston](../../../assets/icons/artifacts/item/pocket_piston.png)

| | |
|---|---|
| **ID** | `artifacts:pocket_piston` |
| **Category** | Hands |
| **Curio slot** | Hands |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Pocket Piston into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **15**, first level costs **100** XP, +100 XP per level.

> Grants the relic bearer's hands the strength of mechanisms.

Found in loot chests of kind: village and pillager chests.

#### Concentrated Strike

*Passive. Ability max level 10.*

Increases knockback in melee attacks by **20-40 (up to 50-100)**%.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Interaction | 20-40 | +15% of base per level | 50-100 |

#### Long Reach

*Unlocks at relic level 5, passive. Ability max level 10.*

Increases maximum interaction range with the world by **20-40 (up to 50-100)**%.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Range | 20-40 | +15% of base per level | 50-100 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/pocket_piston` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `pocket_piston.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `pocket_piston.attackKnockbackBonus` | 0.75 | The amount of extra knockback that is granted by the Pocket Piston |

## Tags

`artifacts:artifacts`, `artifacts:slot/hands`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
