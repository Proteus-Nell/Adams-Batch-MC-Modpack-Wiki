# Icicle Spear

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Icicle Spear](../../../assets/icons/tensura/skill/icicle_spear.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:icicle_spear` |
| **Element** | Ice |
| **Max mastery** | 700 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Press, Hold |

</div>

> Strike targets with a giant icicle spike from the ground.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 40,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (high upgraded tome)
- Can appear in uncommon tomes in frozen wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill registry IDs automatically granted with Albis Vina.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `IcicleSpear.castTime` | 120 | Cast time in tick. |
| `IcicleSpear.magiculeCost` | 40,000 | Magicule Cost to cast. |
| `IcicleSpear.range` | 20 | The range in block of the magic. |
| `IcicleSpear.magicDamage` | 200 | The magic damage of the icicle. |
| `IcicleSpear.icicleRadius` | 3 | The radius in block of the icicle. |
| `IcicleSpear.icicleRadiusMastered` | 4 | The radius in block of the icicle when mastered. |
| `IcicleSpear.cooldown` | 5 | The cooldown in second of the magic. |
| `IcicleSpear.cooldownMastered` | 3 | The cooldown in second of the magic when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/high_upgraded_tome_dwarf_trade`, `tensura:skills/uncommon_tome_frozen_wizard_tower`
