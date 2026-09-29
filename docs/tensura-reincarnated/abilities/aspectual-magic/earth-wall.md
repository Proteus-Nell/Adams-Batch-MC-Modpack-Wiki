# Earth Wall

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Earth Wall](../../../assets/icons/tensura/skill/earth_wall.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:earth_wall` |
| **Element** | Earth |
| **Modes** | 4 |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Call forth giant earth walls from the ground.

## Modes

| # | Mode |
|---|---|
| 1 | 5x5x1 Wall |
| 2 | 5x5x2 Wall |
| 3 | 5x5x3 Wall |
| 4 | 10x10x1 Wall |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Can appear in common tomes in buried wizard towers
- Sold by dwarf traders (low basic tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Referenced by:** [Gaia, Lord of Earth](../../../elite-tensura/abilities/ultimate-skills/gaia.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `EarthWall.castTime` | 40 | Cast time in tick. |
| `EarthWall.castTimeMastered` | 20 | Cast time in tick when mastered. |
| `EarthWall.magiculeCost` | 1,000 | Magicule Cost to cast. |
| `EarthWall.range` | 20 | The range in block of the magic. |
| `EarthWall.wallDuration` | 1,200 | The duration in tick of the Earth Wall. |

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
