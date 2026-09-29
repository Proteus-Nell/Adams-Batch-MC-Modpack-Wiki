# Lighten

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Lighten](../../../assets/icons/tensura/skill/lighten.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:lighten` |
| **Element** | Gravity |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Lighten the caster's gravity for greater speed and jump power.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 250 |  |

## How it works

- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Obtaining

- Sold by dwarf traders (low upgraded tome)
- Can appear in uncommon tomes in buried wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Lighten.castTime` | 60 | Cast time in tick. |
| `Lighten.magiculeCost` | 250 | Magicule Cost to cast. |
| `Lighten.range` | 10 | The range in block of the magic. |
| `Lighten.speedLevel` | 2 | The level of the Speed effect. |
| `Lighten.speedDuration` | 400 | The duration in tick of the Speed effect. |
| `Lighten.speedDurationMastered` | 1,200 | The duration in tick of the Speed effect when mastered. |
| `Lighten.jumpLevel` | 2 | The level of the Jump Boost effect. |
| `Lighten.jumpDuration` | 400 | The duration in tick of the Jump Boost effect. |
| `Lighten.jumpDurationMastered` | 1,200 | The duration in tick of the Jump Boost effect when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/low_upgraded_tome_dwarf_trade`, `tensura:skills/uncommon_tome_buried_wizard_tower`
