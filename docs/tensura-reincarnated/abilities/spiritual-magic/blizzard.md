# Blizzard

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Blizzard](../../../assets/icons/tensura/skill/blizzard.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:blizzard` |
| **Element** | Water |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Cooldowns (s)** | 10 |
| **Activation** | Press, Hold |

</div>

> Creates a powerful storm of ice to slow your enemies and turn the tides of battle.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Hinata Sakaguchi](../../mobs/hinata-sakaguchi.md)
- Removed and re-rolled when you change race
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill registry IDs automatically granted with Albis Vina.

## Related

- **Effects:** [Chill](../../effects/chill.md)
- **Referenced by:** [Ice Blizzard](../aspectual-magic/ice-blizzard.md), [Kyurem](../../../tensura-mysticism/abilities/unique-skills/kyurem.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `Blizzard.castTime` | 160 | Cast time in tick. |
| `Blizzard.castTimeMastered` | 160 | Cast time in tick when mastered. |
| `Blizzard.magiculeCost` | 50,000 | Magicule Cost to cast. |
| `Blizzard.blizzardDamage` | 30 | The damage per second of the blizzard. |
| `Blizzard.blizzardRadius` | 15 | The radius in block of the blizzard. |
| `Blizzard.chillDuration` | 120 | The duration of the Chill effect every 5 seconds. |
| `Blizzard.blizzardDuration` | 2,000 | The duration in tick of the blizzard. |
| `Blizzard.blizzardDurationMastered` | 3,200 | The duration in tick of the blizzard when mastered. |
| `Blizzard.icicleDamage` | 250 | The damage of the icicle. |
| `Blizzard.icicleSize` | 2 | The size of the icicle. |
| `Blizzard.icicleCooldown` | 10 | The cooldown in second of the icicle. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryMedium` | 500 | The max amount of mastery point for Medium Spiritual Magic. |
| `SpiritualMagic.masteryGreater` | 1,000 | The max amount of mastery point for Greater Spiritual Magic. |
| `SpiritualMagic.masteryLord` | 10,000 | The max amount of mastery point for Lord Spiritual Magic. |

## Tags

`tensura:skills/ice_skills`, `tensura:skills/reset_with_race`, `tensura:skills/spiritual_magic`
