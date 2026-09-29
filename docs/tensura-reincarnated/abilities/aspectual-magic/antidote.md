# Antidote

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Antidote](../../../assets/icons/tensura/skill/antidote.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:antidote` |
| **Element** | Recovery |
| **Max mastery** | 300 |
| **Activation** | Hold |

</div>

> Recover a living being from nausea, poison and weakness.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 2,500 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (medium rare tome)
- Can appear in uncommon tomes in frozen wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Effects:** [Fatal Poison](../../effects/fatal-poison.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Antidote.castTime` | 120 | Cast time in tick. |
| `Antidote.magiculeCost` | 2,500 | Magicule Cost to cast. |
| `Antidote.range` | 6 | The range in block of the magic. |
| `Antidote.fatalLevel` | 1 | The level of Fatal Poison that the magic removes. |
| `Antidote.fatalDuration` | 10 | The duration in second of Fatal Poison that the magic removes. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/medium_rare_tome_dwarf_trade`, `tensura:skills/uncommon_tome_frozen_wizard_tower`
