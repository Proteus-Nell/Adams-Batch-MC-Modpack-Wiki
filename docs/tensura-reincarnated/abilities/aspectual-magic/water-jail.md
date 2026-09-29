# Water Jail

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Water Jail](../../../assets/icons/tensura/skill/water_jail.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:water_jail` |
| **Element** | Water |
| **Max mastery** | 700 |
| **Activation** | Press, Hold |

</div>

> Surround targets with flows of water.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 25,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Innate to mobs: [Arch Daemon](../../mobs/arch-daemon.md)
- Sold by dwarf traders (high basic tome)
- Can appear in uncommon tomes in frozen wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill registry IDs automatically granted with Albis Vina.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `WaterJail.castTime` | 60 | Cast time in tick. |
| `WaterJail.castTimeHold` | 40 | Cast time in tick between damaging when held down. |
| `WaterJail.magiculeCost` | 25,000 | Magicule Cost to cast. |
| `WaterJail.magiculeCostHold` | 1,000 | Magicule Cost to hold down each 40 ticks (castTimeHold). |
| `WaterJail.range` | 20 | The range in block of the magic. |
| `WaterJail.jailSize` | 3 | The size in block of the Water Jail. |
| `WaterJail.magicDamage` | 100 | The magic damage of the Water Jail. |
| `WaterJail.bladeDamage` | 50 | The water blade damage of the Water Jail. |
| `WaterJail.maxHold` | 120 | The max number of ticks that the caster can hold magic down. |
| `WaterJail.maxHoldMastered` | 240 | The max number of ticks that the caster can hold magic down when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/high_basic_tome_dwarf_trade`, `tensura:skills/uncommon_tome_frozen_wizard_tower`
