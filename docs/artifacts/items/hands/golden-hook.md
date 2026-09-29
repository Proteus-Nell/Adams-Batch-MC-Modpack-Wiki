# Golden Hook

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Hands](index.md)</small>

<div class="infobox" markdown>

![Golden Hook](../../../assets/icons/artifacts/item/golden_hook.png)

| | |
|---|---|
| **ID** | `artifacts:golden_hook` |
| **Category** | Hands |
| **Curio slot** | Hands |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Golden Hook into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

**How it earns experience:**

Allows the relic bearer to perform more precise attacks, retaining more experience from killed mobs.

Found in loot chests of kind: bastion chests.

#### Thirst for Knowledge

*Passive. Ability max level 10.*

Increases experience gained from killing mobs by **20-40 (up to 50-100)**%.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Amount | 20-40 | +15% of base per level | 50-100 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/golden_hook` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `golden_hook.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `golden_hook.entityExperienceBonus` | 0.5 | The amount of extra experience dropped by entities that are killed by players wearing the Golden Hook |

## Tags

`artifacts:artifacts`, `artifacts:slot/hands`, `minecraft:piglin_loved`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
