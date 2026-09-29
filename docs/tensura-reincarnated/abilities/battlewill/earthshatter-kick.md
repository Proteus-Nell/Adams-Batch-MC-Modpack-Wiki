# Earthshatter Kick

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Earthshatter Kick](../../../assets/icons/tensura/skill/earthshatter_kick.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:earthshatter_kick` |
| **Kind** | Melee |
| **Activation** | Press |

</div>

> Stomp your foot down upheaving the land around you.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 150 |

## How it works

- Activated by pressing the skill key

## Obtaining

- Intrinsic skill of: [Earthshaker pDancer](../../../tr-nightmares/races/earthshaker-dancer.md)
- Sold by dwarf traders (medium manual)
- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `EarthshatterKick.auraCost` | 150 | Aura Cost to activate. |
| `EarthshatterKick.radius` | 5 | The radius of the earthquake. |
| `EarthshatterKick.baseDamage` | 10 | The Damage the affected targets get take when activated (doubled when mastered). |

## Tags

`tensura:skills/battlewill`, `tensura:skills/medium_manual_dwarf_trade`
