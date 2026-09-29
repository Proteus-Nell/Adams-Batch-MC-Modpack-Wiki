# Summon Hound Dog

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Summoning Magic](index.md)</small>

<div class="infobox" markdown>

![Summon Hound Dog](../../../assets/icons/tensura/skill/summon_hound_dog.png)

| | |
|---|---|
| **Type** | Summoning Magic |
| **ID** | `tensura:summon_hound_dog` |
| **Max mastery** | 200 |
| **Activation** | Press, Hold |

</div>

> Summon a Hound Dog to temporarily fight for you.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when one of your subordinates dies

## Stats (config defaults)

Set in [`config/tensura/ability/magic/summoning_config.toml`](../../configs/config-tensura-ability-magic-summoning-config.md).

| Option | Default | Description |
|---|---|---|
| `SummonHoundDog.castTime` | 100 | Cast time in tick. |
| `SummonHoundDog.castTimeMastered` | 60 | Cast time in tick when mastered. |
| `SummonHoundDog.magiculeCost` | 50 | Magicule Cost to cast. |
| `SummonHoundDog.magiculeCostSecond` | 10 | Magicule Cost each second to keep the Hound Dog alive. |
| `SummonHoundDog.summonDuration` | 600 | How long in second will the summoned Hound Dog will stay. |
| `SummonHoundDog.cooldown` | 600 | The cooldown in second of the magic. |
| `SummonHoundDog.cooldownMastered` | 300 | The cooldown in second of the magic when mastered. |

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

`tensura:skills/summoning_magic`
