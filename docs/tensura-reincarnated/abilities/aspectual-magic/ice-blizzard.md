# Ice Blizzard

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Ice Blizzard](../../../assets/icons/tensura/skill/ice_blizzard.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:ice_blizzard` |
| **Element** | Ice |
| **Max mastery** | 700 |
| **Cooldowns (s)** | 60 |
| **Activation** | Press, Hold |

</div>

> Create a powerful storm of snow to freeze your enemies.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 30,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (high upgraded tome)
- Can appear in uncommon tomes in frozen wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill registry IDs automatically granted with Albis Vina.

## Related

- **Related skills:** [Blizzard](../spiritual-magic/blizzard.md)
- **Effects:** [Chill](../../effects/chill.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `IceBlizzard.castTime` | 160 | Cast time in tick. |
| `IceBlizzard.castTimeHold` | 100 | Cast time in tick to do the hold effect after the initial cast. |
| `IceBlizzard.magiculeCost` | 30,000 | Magicule Cost to cast. |
| `IceBlizzard.magiculeCostHold` | 5,000 | Magicule Cost to hold each 100 ticks. |
| `IceBlizzard.blizzardDamage` | 200 | The magic damage of the blizzard. |
| `IceBlizzard.blizzardRadius` | 17.5 | The radius in block of the blizzard. |
| `IceBlizzard.chillLevel` | 2 | The level of the Chill effect. |
| `IceBlizzard.chillDuration` | 600 | The duration in tick of the Chill effect. |
| `IceBlizzard.blizzardDamageHold` | 80 | The magic damage of the blizzard when held down each 100 ticks after the initial cast. |
| `IceBlizzard.chillLevelHold` | 1 | The additional level of the Chill effect when held down each 100 ticks after the initial cast. |
| `IceBlizzard.chillDurationHold` | 300 | The additional duration in tick of the Chill effect when held down each 100 ticks after the initial cast. |
| `IceBlizzard.maxHold` | 3 | The max number of times that the caster can activate the hold attack after the initial cast. |
| `IceBlizzard.maxHoldMastered` | 5 | The max number of times that the caster can activate the hold attack after the initial cast when mastered. |

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
