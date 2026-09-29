# Invisible

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Invisible](../../../assets/icons/tensura/skill/invisible.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:invisible` |
| **Element** | Illusion |
| **Max mastery** | 300 |
| **Activation** | Hold |

</div>

> Turn the caster invisible to hide from targets.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 2,000 |  |

## How it works

- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Obtaining

- Sold by dwarf traders (medium rare tome)
- Can appear in rare tomes in rotted wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Effects:** [Presence Concealment](../../effects/presence-concealment.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Invisible.castTime` | 60 | Cast time in tick. |
| `Invisible.magiculeCost` | 2,000 | Magicule Cost to cast. |
| `Invisible.invisibleLevel` | 1 | The level of the Invisibility effect. |
| `Invisible.invisibleDuration` | 2,400 | The duration in tick of the Invisibility effect. |
| `Invisible.concealmentLevel` | 1 | The level of the Presence Concealment effect when mastered. |
| `Invisible.concealmentDuration` | 6,000 | The duration in tick of the Invisibility effect when mastered. |

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
