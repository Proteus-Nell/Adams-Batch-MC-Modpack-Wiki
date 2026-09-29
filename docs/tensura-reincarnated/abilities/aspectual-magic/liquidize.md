# Liquidize

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Liquidize](../../../assets/icons/tensura/skill/liquidize.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:liquidize` |
| **Element** | Earth |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Liquidize the earth where the caster desires to turn into deadly traps.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 250 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Can appear in common tomes in buried wizard towers
- Sold by dwarf traders (low basic tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `learnableMagics` config option (config/tensura/EliteTensura/Races.toml)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Liquidize.castTime` | 80 | Cast time in tick. |
| `Liquidize.castTimeMastered` | 60 | Cast time in tick when mastered. |
| `Liquidize.magiculeCost` | 250 | Magicule Cost to cast. |
| `Liquidize.range` | 10 | The range in block of the magic. |
| `Liquidize.radius` | 2 | The radius in block of where the caster targeted to be turned into loose soil. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/common_tome_buried_wizard_tower`, `tensura:skills/low_basic_tome_dwarf_trade`
