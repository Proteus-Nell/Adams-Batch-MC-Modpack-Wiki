# Icicle Lance

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Icicle Lance](../../../assets/icons/tensura/skill/icicle_lance.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:icicle_lance` |
| **Element** | Ice |
| **Modes** | 2 |
| **Max mastery** | 100 |
| **Activation** | Press, Hold |

</div>

> Shoot frozen icicles toward targets.

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Mode 2 |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 850 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Greater Daemon](../../mobs/greater-daemon.md)
- Can appear in common tomes in frozen wizard towers
- Sold by dwarf traders (low upgraded tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill registry IDs automatically granted with Albis Vina.

## Related

- **Summons / entities:** Ice Lance
- **Referenced by:** [Icicle Rain](icicle-rain.md), [Ice Breaker](ice-breaker.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `IcicleLance.castTime` | 50 | Cast time in tick. |
| `IcicleLance.castTimeShot` | 20 | Cast time in tick of the Icicle Shot mode. |
| `IcicleLance.magiculeCost` | 850 | Magicule Cost to cast per icicle. |
| `IcicleLance.magicDamage` | 40 | The magic damage of the icicle. |
| `IcicleLance.icicleShotNumber` | 4 | The number of icicles spawn each time using Icicle Shot. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/common_tome_frozen_wizard_tower`, `tensura:skills/low_upgraded_tome_dwarf_trade`
