# Create Lesser Undead

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Create Lesser Undead](../../../assets/icons/tensura/skill/create_lesser_undead.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:create_lesser_undead` |
| **Element** | Necromancy |
| **Modes** | 3 |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Press, Hold |

</div>

> Call forth weak undead from the ground to aid the caster.

## Modes

| # | Mode |
|---|---|
| 1 | Zombie |
| 2 | Skeleton |
| 3 | Random Undead |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 800 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Does something when mastered

## Obtaining

- Intrinsic skill of: [Wight King](../../races/wight-king.md), [Spirit Skeleton](../../races/spirit-skeleton.md), [Divine Skeleton](../../races/divine-skeleton.md)
- Can be learned by: [Death Knight](../../../ascension/races/death-knight.md), [Dullahan](../../../ascension/races/dullahan.md), [Dark Lord Dullahan](../../../ascension/races/dark-lord-dullahan.md), [Elder Lich](../../../ascension/races/elder-lich.md), [Lich](../../../ascension/races/lich.md), [Lich King](../../../ascension/races/lich-king.md)
- Can appear in common tomes in rotted wizard towers

## Related

- **Related skills:** [Create Greater Undead](create-greater-undead.md)
- **Summons / entities:** [Zombie](../../mobs/zombie.md), [Skeleton](../../mobs/skeleton.md)
- **Referenced by:** [Create Greater Undead](create-greater-undead.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `CreateLesserUndead.castTime` | 80 | Cast time in tick. |
| `CreateLesserUndead.magiculeCost` | 800 | Magicule Cost to create each undead. |
| `CreateLesserUndead.undeadDuration` | 300 | How long in second will the summoned undead will stay. |
| `CreateLesserUndead.undeadNumber` | 1 | The number of undead getting summoned by the magic. |
| `CreateLesserUndead.undeadNumberMastered` | 3 | The number of undead getting summoned by the magic when sneaking with mastery. |
| `CreateLesserUndead.undeadHP` | 20 | The HP that each undead created has. |
| `CreateLesserUndead.undeadAttack` | 5 | The attack damage that each undead created has. |
| `CreateLesserUndead.cooldown` | 10 | The cooldown in second of the magic. |
| `CreateLesserUndead.cooldownMastered` | 5 | The cooldown in second of the magic when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryMedium` | 500 | The max amount of mastery point for Medium Spiritual Magic. |
| `SpiritualMagic.masteryGreater` | 1,000 | The max amount of mastery point for Greater Spiritual Magic. |
| `SpiritualMagic.masteryLord` | 10,000 | The max amount of mastery point for Lord Spiritual Magic. |

## Tags

`tensura:skills/common_tome_rotted_wizard_tower`, `tensura:skills/necromancy_magic`, `tensura:skills/spiritual_magic`
