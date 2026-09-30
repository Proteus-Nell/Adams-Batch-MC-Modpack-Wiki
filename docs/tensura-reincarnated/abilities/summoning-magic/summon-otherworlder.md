# Summon Otherworlder

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Summoning Magic](index.md)</small>

<div class="infobox" markdown>

![Summon Otherworlder](../../../assets/icons/tensura/skill/summon_otherworlder.png)

| | |
|---|---|
| **Type** | Summoning Magic |
| **ID** | `tensura:summon_otherworlder` |
| **Max mastery** | 200 |
| **Activation** | Press, Hold |

</div>

> Summon a human from a different world.

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when one of your subordinates dies

## Obtaining

- Can appear in epic tomes from wizard towers

## Related

- **Summons / entities:** Magic Circle

## Stats (config defaults)

Set in [`config/tensura/ability/magic/summoning_config.toml`](../../configs/config-tensura-ability-magic-summoning-config.md).

| Option | Default | Description |
|---|---|---|
| `SummonOtherworlder.castInterval` | 60 | Cast time in tick each time the magic circle can be provided with Magicule. |
| `SummonOtherworlder.castRange` | 8 | Cast range in block of the magic. |
| `SummonOtherworlder.magiculeCostTotal` | 3,000,000 | Magicule Cost total to summon an otherworlder. |
| `SummonOtherworlder.magiculeCostInterval` | 50,000 | Magicule Cost the magic circle takes each cast interval. |
| `SummonOtherworlder.magiculeCostIntervalMastered` | 100,000 | Magicule Cost the magic circle takes each cast interval when mastered. |
| `SummonOtherworlder.failChance` | 0.5 | The chance to fail summon an otherworlder. |
| `SummonOtherworlder.failChanceMastered` | 0.3 | The chance to fail summon an otherworlder when mastered. |
| `SummonOtherworlder.circleDuration` | 600 | How long in second will the magic circle stay each time it is provided with Magicule. |
| `SummonOtherworlder.cooldown` | 1,200 | The cooldown in second of the magic. |

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

`tensura:skills/epic_tome_wizard_tower`, `tensura:skills/summoning_magic`, `tensura:skills/unlearnt_cast_excluded`
