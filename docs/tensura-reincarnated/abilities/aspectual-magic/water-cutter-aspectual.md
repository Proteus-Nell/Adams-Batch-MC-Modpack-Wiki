# Water Cutter

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Water Cutter](../../../assets/icons/tensura/skill/water_cutter_aspectual.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:water_cutter_aspectual` |
| **Element** | Water |
| **Modes** | 2 |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Fire concentrated blades of water toward targets.

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Mode 2 |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 or 1,000 |  |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Lesser Daemon](../../mobs/lesser-daemon.md)
- Can appear in common tomes in frozen wizard towers
- Sold by dwarf traders (low basic tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill registry IDs automatically granted with Albis Vina.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `WaterCutter.castTime` | 30 | Cast time in tick. |
| `WaterCutter.castTimeRepeat` | 15 | Repeat cast time in tick when mastered. |
| `WaterCutter.magiculeCost` | 1,000 | Magicule Cost to cast. |
| `WaterCutter.magiculeCostRepeat` | 500 | Magicule Cost to repeat cast when mastered. |
| `WaterCutter.magicDamage` | 40 | The magic damage of the water cutter. |

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
