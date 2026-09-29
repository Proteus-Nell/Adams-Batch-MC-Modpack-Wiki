# Magic Wall

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Magic Wall](../../../assets/icons/tensura/skill/magic_wall.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:magic_wall` |
| **Element** | Barrier |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Generate a magic wall to protect the caster.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 400 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (low rare tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `MagicWall.castTime` | 120 | Cast time in tick. |
| `MagicWall.castTimeMastered` | 100 | Cast time in tick when mastered. |
| `MagicWall.magiculeCost` | 400 | Magicule Cost to cast. |
| `MagicWall.distance` | 4 | The distance in block from the caster to create the magic wall. |
| `MagicWall.width` | 4 | The width radius of the magic wall. |
| `MagicWall.speedMultiplier` | 0.5 | The speed multiplier of the targets going through the magic wall. |
| `MagicWall.magicProjectileReduction` | 30 | The damage reduction of the magic projectiles going through the magic wall. |
| `MagicWall.magicProjectileReductionMastered` | 50 | The damage reduction of the magic projectiles going through the magic wall when mastered. |
| `MagicWall.wallDuration` | 200 | The duration in tick of the Magic Wall. |
| `MagicWall.wallDurationMastered` | 500 | The duration in tick of the Magic Wall when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/low_rare_tome_dwarf_trade`
