# Agility

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Agility](../../../assets/icons/tensura/skill/agility.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:agility` |
| **Element** | Enhancement |
| **Max mastery** | 300 |
| **Activation** | Hold |

</div>

> Greatly enhance the caster's movement speed.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 3,000 |  |

## How it works

- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Obtaining

- Can appear in common tomes in rotted wizard towers
- Sold by dwarf traders (medium rare tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Agility.castTime` | 100 | Cast time in tick. |
| `Agility.magiculeCost` | 3,000 | Magicule Cost to cast. |
| `Agility.range` | 10 | The range in block of the magic. |
| `Agility.speedLevel` | 3 | The level of the Speed effect. |
| `Agility.speedDuration` | 2,400 | The duration in tick of the Speed effect. |
| `Agility.speedDurationMastered` | 12,000 | The duration in tick of the Speed effect when mastered. |
| `Agility.hasteLevel` | 3 | The level of the Haste effect. |
| `Agility.hasteDuration` | 2,400 | The duration in tick of the Haste Boost effect. |
| `Agility.hasteDurationMastered` | 12,000 | The duration in tick of the Haste Boost effect when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/common_tome_rotted_wizard_tower`, `tensura:skills/medium_rare_tome_dwarf_trade`
