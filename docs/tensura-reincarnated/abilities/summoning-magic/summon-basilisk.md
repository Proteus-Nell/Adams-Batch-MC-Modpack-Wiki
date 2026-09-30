# Summon Basilisk

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Summoning Magic](index.md)</small>

<div class="infobox" markdown>

![Summon Basilisk](../../../assets/icons/tensura/skill/summon_basilisk.png)

| | |
|---|---|
| **Type** | Summoning Magic |
| **ID** | `tensura:summon_basilisk` |
| **Max mastery** | 200 |
| **Activation** | Press, Hold |

</div>

> Summon a Basilisk to temporarily fight for you.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when one of your subordinates dies

## Related

- **Summons / entities:** [Basilisk](../../mobs/basilisk.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/summoning_config.toml`](../../configs/config-tensura-ability-magic-summoning-config.md).

| Option | Default | Description |
|---|---|---|
| `SummonBasilisk.castTime` | 100 | Cast time in tick. |
| `SummonBasilisk.castTimeMastered` | 60 | Cast time in tick when mastered. |
| `SummonBasilisk.magiculeCost` | 500 | Magicule Cost to cast. |
| `SummonBasilisk.magiculeCostSecond` | 100 | Magicule Cost each second to keep the Basilisk alive. |
| `SummonBasilisk.summonDuration` | 600 | How long in second will the summoned Basilisk will stay. |
| `SummonBasilisk.cooldown` | 600 | The cooldown in second of the magic. |
| `SummonBasilisk.cooldownMastered` | 300 | The cooldown in second of the magic when mastered. |

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
