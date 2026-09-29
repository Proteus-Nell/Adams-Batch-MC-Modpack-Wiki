# Fire Lance

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Fire Lance](../../../assets/icons/tensura/skill/fire_lance.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:fire_lance` |
| **Element** | Fire |
| **Modes** | 2 |
| **Max mastery** | 100 |
| **Activation** | Press, Hold |

</div>

> Shoot fiery lances of magic.

## Modes

| # | Mode |
|---|---|
| 1 | Repeat |
| 2 | Single |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Greater Daemon](../../mobs/greater-daemon.md)
- Can appear in common tomes in burnt wizard towers
- Sold by dwarf traders (medium basic tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `FireLance.castTime` | 50 | Cast time in tick. |
| `FireLance.castTimeRepeat` | 10 | Cast time in tick between each lance in Repeat Mode. |
| `FireLance.magiculeCost` | 1,000 | Magicule Cost to cast. |
| `FireLance.magicDamage` | 50 | The magic damage of the fire. |
| `FireLance.fireDamage` | 20 | The fire damage of the fire. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/common_tome_burnt_wizard_tower`, `tensura:skills/medium_basic_tome_dwarf_trade`
