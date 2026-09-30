# Ice Wall

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Ice Wall](../../../assets/icons/tensura/skill/ice_wall.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:ice_wall` |
| **Element** | Ice |
| **Max mastery** | 300 |
| **Activation** | Hold |

</div>

> Call forth walls of ice upon targets.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 8,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (medium upgraded tome)
- Can appear in uncommon tomes in frozen wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill registry IDs automatically granted with Albis Vina.

## Related

- **Effects:** [Chill](../../effects/chill.md), [Frost](../../effects/frost.md)
- **Summons / entities:** Ice Pillar

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `IceWall.castTime` | 60 | Cast time in tick. |
| `IceWall.magiculeCost` | 8,000 | Magicule Cost to cast. |
| `IceWall.range` | 20 | The range in block of the magic. |
| `IceWall.contactDamage` | 30 | The contact damage in magic of the ice walls. |
| `IceWall.contactDamageMastered` | 65 | The contact damage in magic of the ice walls when mastered. |
| `IceWall.contactChillLevel` | 1 | The level of the Chill effect when contacting ice walls. |
| `IceWall.contactChillLevelMastered` | 2 | The level of the Chill effect when contacting ice walls when mastered. |
| `IceWall.contactChillDuration` | 200 | The duration in tick of the Chill effect when contacting ice walls. |
| `IceWall.contactChillDurationMastered` | 300 | The duration in tick of the Chill effect when contacting ice walls when mastered. |
| `IceWall.aoeRadius` | 5 | The aoe effect radius in block of the ice walls. |
| `IceWall.aoeDamage` | 50 | The aoe effect damage in magic of the ice walls. |
| `IceWall.breakFrostLevel` | 1 | The level of the contacting Frost effect when the ice walls break while mastered. |
| `IceWall.breakFrostDuration` | 200 | The duration in tick of the contacting Frost effect when the ice walls break while mastered. |
| `IceWall.wallDuration` | 400 | The duration in tick of the Earth Wall. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/medium_upgraded_tome_dwarf_trade`, `tensura:skills/uncommon_tome_frozen_wizard_tower`
