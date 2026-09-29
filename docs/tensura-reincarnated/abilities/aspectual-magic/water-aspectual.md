# Water

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Water](../../../assets/icons/tensura/skill/water_aspectual.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:water_aspectual` |
| **Element** | Water |
| **Modes** | 4 |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Call forth small amounts of water.

## Modes

| # | Mode |
|---|---|
| 1 | 1x1 Water |
| 2 | 3x3 Water |
| 3 | 5x5 Water |
| 4 | 10x10 Water |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Lesser Daemon](../../mobs/lesser-daemon.md)
- Can appear in common tomes in frozen wizard towers
- Sold by dwarf traders (low basic tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `learnableMagics` config option (config/tensura/EliteTensura/Races.toml)
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill registry IDs automatically granted with Albis Vina.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Water.castTime` | 20 | Cast time in tick. |
| `Water.magiculeCost` | 100 | Magicule Cost to cast per water block. |
| `Water.range` | 6 | The range in block of the magic. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/common_tome_frozen_wizard_tower`, `tensura:skills/low_basic_tome_dwarf_trade`
