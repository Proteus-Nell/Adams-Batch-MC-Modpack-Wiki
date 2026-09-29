# Power Glove

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Hands](index.md)</small>

<div class="infobox" markdown>

![Power Glove](../../../assets/icons/artifacts/item/power_glove.png)

| | |
|---|---|
| **ID** | `artifacts:power_glove` |
| **Category** | Hands |
| **Curio slot** | Hands |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Power Glove into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Allows the relic bearer to perform empowered attacks.

Found in loot chests of kind: village and pillager chests.

#### Power Strike

*Passive. Ability max level 10.*

Increases the player's damage dealt by **80-100 (up to 400-500)**% but enters a 5-second cooldown after each attack.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Amount | 80-100 | +40% of base per level | 400-500 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/power_glove` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `power_glove.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `power_glove.attackDamageBonus` | 4 | The amount of extra damage that is dealt by melee attacks from players wearing the Power Glove |

## Tags

`artifacts:artifacts`, `artifacts:slot/hands`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
