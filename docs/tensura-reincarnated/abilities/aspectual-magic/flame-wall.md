# Flame Wall

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Flame Wall](../../../assets/icons/tensura/skill/flame_wall.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:flame_wall` |
| **Element** | Illusion |
| **Max mastery** | 300 |
| **Activation** | Hold |

</div>

> Create a wall of illusional fire to keep targets away.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (medium rare tome)
- Can appear in rare tomes in rotted wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Summons / entities:** Tensura, Fire Pillar

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `FlameWall.castTime` | 60 | Cast time in tick. |
| `FlameWall.magiculeCost` | 1,000 | Magicule Cost to cast. |
| `FlameWall.range` | 10 | The range in block of the magic. |
| `FlameWall.width` | 4 | The width radius of the Flame Wall. |
| `FlameWall.height` | 8 | The height of the Flame Wall. |
| `FlameWall.magicDamage` | 1 | The magic damage of the Flame Wall. |
| `FlameWall.damageInterval` | 10 | The damaging interval in ticks of the Flame Wall. |
| `FlameWall.damageIntervalMastered` | 5 | The damaging interval in ticks of the Flame Wall when mastered. |
| `FlameWall.knockback` | 0.1 | The knockback multiplier of the Flame Wall. |
| `FlameWall.wallDuration` | 200 | The duration in tick of the Flame Wall. |
| `FlameWall.wallDurationMastered` | 300 | The duration in tick of the Flame Wall when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/medium_rare_tome_dwarf_trade`, `tensura:skills/rare_tome_rotted_wizard_tower`
