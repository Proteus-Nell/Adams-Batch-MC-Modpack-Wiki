# Summon Greater Elemental

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Summoning Magic](index.md)</small>

<div class="infobox" markdown>

![Summon Greater Elemental](../../../assets/icons/tensura/skill/summon_greater_elemental.png)

| | |
|---|---|
| **Type** | Summoning Magic |
| **ID** | `tensura:summon_greater_elemental` |
| **Modes** | 5 |
| **Max mastery** | 200 |
| **Activation** | Press, Hold |

</div>

> Summon your contracted greater elemental spirit to have it purge the world of heretics for you.

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Mode 2 |
| 3 | Mode 3 |
| 4 | Mode 4 |
| 5 | Mode 5 |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 3,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when one of your subordinates dies

## Obtaining

- Innate to mobs: [Gazel Dwargo](../../mobs/gazel-dwargo.md), [Hinata Sakaguchi](../../mobs/hinata-sakaguchi.md)
- Removed and re-rolled when you change race

## Stats (config defaults)

Set in [`config/tensura/ability/magic/summoning_config.toml`](../../configs/config-tensura-ability-magic-summoning-config.md).

| Option | Default | Description |
|---|---|---|
| `SummonGreaterElemental.castTime` | 100 | Cast time in tick. |
| `SummonGreaterElemental.castTimeMastered` | 60 | Cast time in tick when mastered. |
| `SummonGreaterElemental.magiculeCost` | 3,000 | Magicule Cost to cast. |
| `SummonGreaterElemental.magiculeCostSecond` | 300 | Magicule Cost each second to keep the Spirit alive. |
| `SummonGreaterElemental.spiritDuration` | 600 | How long in second will the summoned Spirit will stay. |
| `SummonGreaterElemental.attackMultiplier` | 0.5 | The multiplier of Attack damage for the summoned Greater Spirit compared to the wild Boss version. |
| `SummonGreaterElemental.healthMultiplier` | 0.5 | The multiplier of Health for the summoned Greater Spirit compared to the wild Boss version. |
| `SummonGreaterElemental.cooldown` | 600 | The cooldown in second of the magic. |
| `SummonGreaterElemental.cooldownMastered` | 300 | The cooldown in second of the magic when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/reset_with_race`, `tensura:skills/summoning_magic`, `tensura:skills/tome_copy_excluded`, `tensura:skills/unlearnt_cast_excluded`
