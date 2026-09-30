# Disintegration

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Other Magic](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Other Magic |
| **ID** | `trnightmare:disintegration` |
| **Max mastery** | 700 |
| **Activation** | Hold |

</div>

> Gather Purifying energy into an array, and unleash it upon an imprisoned foe.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 350,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Can appear in epic tomes from wizard towers
- Can be found in skill tomes
- Sold by dwarf traders (great upgraded tome)

## Related

- **Effects:** [Movement Interference](../../../tensura-reincarnated/effects/movement-interference.md)
- **Summons / entities:** Disintegration

## Stats (config defaults)

Set in [`config/nightmare/ability/magic/holy.toml`](../../configs/config-nightmare-ability-magic-holy.md).

| Option | Default | Description |
|---|---|---|
| `Disintegration.castTime` | 8 | Cast time in seconds. |
| `Disintegration.magiculeCost` | 350,000 | Magicule Cost to cast. |
| `Disintegration.spiritronCost` | 110 | Spiritron Cost to cast. |
| `Disintegration.holyDamage` | 350 | The holy damage of the spell per damage tick. |

Set in [`config/tensura/ability/magic_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/epic_tome_wizard_tower`, `tensura:skills/found_in_tome`, `tensura:skills/great_upgraded_tome_dwarf_trade`, `tensura:skills/magic`
