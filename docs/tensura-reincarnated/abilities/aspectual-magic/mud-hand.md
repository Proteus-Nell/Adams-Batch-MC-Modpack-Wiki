# Mud Hand

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Mud Hand](../../../assets/icons/tensura/skill/mud_hand.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:mud_hand` |
| **Element** | Earth |
| **Max mastery** | 300 |
| **Activation** | Press, Hold |

</div>

> Bind targets with several hands of mud.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Can appear in common tomes in buried wizard towers
- Sold by dwarf traders (medium basic tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Effects:** [Movement Interference](../../effects/movement-interference.md)
- **Referenced by:** [Mud Spears](mud-spears.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `MudHand.castTime` | 80 | Cast time in tick. |
| `MudHand.magiculeCost` | 5,000 | Magicule Cost to cast. |
| `MudHand.range` | 20 | The range in block of the magic. |
| `MudHand.bindLevel` | 10 | The level of Movement Interference to apply on target when casted (-10% speed each level). |
| `MudHand.slowLevel` | 2 | The level of the Slowness effect to apply on target when the spell stops while mastered. |
| `MudHand.slowDuration` | 100 | The duration in tick of the Slowness effect to apply on target when the spell stops while mastered. |
| `MudHand.maxHold` | 100 | The max number of ticks that the caster can hold magic down. |
| `MudHand.maxHoldMastered` | 200 | The max number of ticks that the caster can hold magic down when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/common_tome_buried_wizard_tower`, `tensura:skills/medium_basic_tome_dwarf_trade`
