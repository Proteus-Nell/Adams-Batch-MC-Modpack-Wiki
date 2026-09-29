# Kitty Slippers

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Feet](index.md)</small>

<div class="infobox" markdown>

![Kitty Slippers](../../../assets/icons/artifacts/item/kitty_slippers.png)

| | |
|---|---|
| **ID** | `artifacts:kitty_slippers` |
| **Category** | Feet |
| **Curio slot** | Feet |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Kitty Slippers into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **15**, first level costs **100** XP, +100 XP per level.

> Grants the relic bearer feline traits, including soft paws and countless lives.

Found in loot chests of kind: chests in jungle/tropical biomes, village and pillager chests.

#### Cat's Gaze

*Passive. Ability max level 10.*

Scares away all Creepers and Phantoms near the player.

#### Soft Paws

*Passive. Ability max level 10.*

Increases safe falling height by **2-4 (up to 10-20)** blocks.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Modifier | 2-4 | +40% of base per level | 10-20 |

#### Nine Lives

*Unlocks at relic level 5, passive. Ability max level 10.*

Has a **5-10 (up to 17.5-35)**% chance to save the player from fatal damage, leaving them with 1 health point.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Chance | 5-10 | +25% of base per level | 17.5-35 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/kitty_slippers` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `kitty_slippers.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `kitty_slippers.modifyHurtSounds` | true | Whether the Kitty Slippers change the player's hurt sounds |
| `kitty_slippers.repelCreepers` | true | Whether the Kitty Slippers scare nearby creepers |
| `kitty_slippers.repelPhantoms` | true | Whether the Kitty Slippers hiss at nearby phantoms |

## Tags

`artifacts:artifacts`, `artifacts:slot/feet`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
