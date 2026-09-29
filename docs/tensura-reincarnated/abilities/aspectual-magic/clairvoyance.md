# Clairvoyance

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Clairvoyance](../../../assets/icons/tensura/skill/clairvoyance.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:clairvoyance` |
| **Element** | Misc |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Increase the caster's eye sight.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10 |  |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active

## Obtaining

- Sold by dwarf traders (low rare tome)
- Can appear in uncommon tomes in burnt wizard towers

## Related

- **Referenced by:** [Farsight](../common-skills/farsight.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Clairvoyance.castTime` | 20 | Cast time in tick. |
| `Clairvoyance.magiculeCost` | 10 | Magicule Cost per second to cast. |
| `Clairvoyance.maxZoom` | 25 | The Max Zoom Multiplier. |
| `Clairvoyance.maxZoomMastered` | 50 | The Max Zoom Multiplier when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/low_rare_tome_dwarf_trade`, `tensura:skills/uncommon_tome_burnt_wizard_tower`
