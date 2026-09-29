# Summon Pegasus

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Summoning Magic](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Summoning Magic |
| **ID** | `trnightmare:summon_pegasus` |
| **Max mastery** | 200 |
| **Activation** | Press, Hold |

</div>

> Summon a loyal pegasus to serve as a flying companion and mount.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when one of your subordinates dies

## Related

- **Summons / entities:** [Pegasus](../../../tensura-reincarnated/mobs/pegasus.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/magic/summoning.toml`](../../configs/config-nightmare-ability-magic-summoning.md).

| Option | Default | Description |
|---|---|---|
| `Pegasus.castTime` | 100 | Cast time in tick. |
| `Pegasus.castTimeMastered` | 60 | Cast time in tick when mastered. |
| `Pegasus.magiculeCost` | 50 | Magicule Cost to cast. |
| `Pegasus.magiculeCostSecond` | 10 | Magicule Cost each second to keep the Pegasus alive. |
| `Pegasus.summonDuration` | 600 | How long in second the summoned Pegasus will stay. |
| `Pegasus.cooldown` | 600 | The cooldown in second of the magic. |
| `Pegasus.cooldownMastered` | 300 | The cooldown in second of the magic when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |
