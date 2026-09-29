# Night Vision Goggles

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Face](index.md)</small>

<div class="infobox" markdown>

![Night Vision Goggles](../../../assets/icons/artifacts/item/night_vision_goggles.png)

| | |
|---|---|
| **ID** | `artifacts:night_vision_goggles` |
| **Category** | Face |
| **Curio slot** | Face |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Night Vision Goggles into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Allows the relic bearer to see more clearly in the dark.

Found in loot chests of kind: chests in cave biomes, mineshaft chests, chests in the deep dark.

#### Gamma Vision

*Active (toggleable). Ability max level 10.*

Enhances the brightness of poorly lit areas and reduces the effectiveness of blindness and darkness by **10-15 (up to 60-90)**%.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Amount | 10-15 | +50% of base per level | 60-90 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/night_vision_goggles` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `night_vision_goggles.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `night_vision_goggles.strength` | 0.15 | The strength of the night vision effect applied by the Night Vision Goggles |

## Tags

`artifacts:artifacts`, `artifacts:slot/face`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
