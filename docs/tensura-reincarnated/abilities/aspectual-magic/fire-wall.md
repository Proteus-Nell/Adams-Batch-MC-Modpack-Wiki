# Fire Wall

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Fire Wall](../../../assets/icons/tensura/skill/fire_wall.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:fire_wall` |
| **Element** | Fire |
| **Max mastery** | 300 |
| **Activation** | Hold |

</div>

> Create a wall of fire to keep targets away.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Can appear in common tomes in burnt wizard towers
- Sold by dwarf traders (low basic tome)
- Can appear in uncommon tomes in burnt wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `FireWall.castTime` | 60 | Cast time in tick. |
| `FireWall.magiculeCost` | 5,000 | Magicule Cost to cast. |
| `FireWall.range` | 10 | The range in block of the magic. |
| `FireWall.width` | 4 | The width radius of the Fire Wall. |
| `FireWall.height` | 8 | The height of the Fire Wall. |
| `FireWall.magicDamage` | 30 | The magic damage of the Fire Wall. |
| `FireWall.fireDamage` | 10 | The fire damage of the Fire Wall. |
| `FireWall.damageInterval` | 10 | The damaging interval in ticks of the Fire Wall. |
| `FireWall.damageIntervalMastered` | 5 | The damaging interval in ticks of the Fire Wall when mastered. |
| `FireWall.knockback` | 0.5 | The knockback multiplier of the Fire Wall. |
| `FireWall.knockResistNegate` | 0.6 | The knockback resistance negation of the Fire Wall when mastered. |
| `FireWall.wallDuration` | 200 | The duration in tick of the Fire Wall. |
| `FireWall.wallDurationMastered` | 300 | The duration in tick of the Fire Wall when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/common_tome_burnt_wizard_tower`, `tensura:skills/low_basic_tome_dwarf_trade`, `tensura:skills/uncommon_tome_burnt_wizard_tower`
