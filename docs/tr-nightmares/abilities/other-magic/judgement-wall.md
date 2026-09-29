# Judgement Wall

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Other Magic](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Other Magic |
| **ID** | `trnightmare:judgement_wall` |
| **Max mastery** | 300 |
| **Activation** | Hold |

</div>

> A wall passing judgement upon that which is not holy. Majin that touch the wall shall face damage, while the rest will merely be repelled.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Can appear in common tomes in buried wizard towers
- Can appear in common tomes in burnt wizard towers
- Can appear in common tomes in frozen wizard towers
- Can appear in common tomes in rotted wizard towers
- Can appear in common tomes in ruined wizard towers
- Can be found in skill tomes
- Sold by dwarf traders (low basic tome)
- Sold by dwarf traders (low upgraded tome)

## Related

- **Summons / entities:** Judgement Pillar

## Stats (config defaults)

Set in [`config/nightmare/ability/magic/holy.toml`](../../configs/config-nightmare-ability-magic-holy.md).

| Option | Default | Description |
|---|---|---|
| `JudgementWall.castTime` | 60 | Cast time in tick. |
| `JudgementWall.magiculeCost` | 5,000 | Magicule Cost to cast. |
| `JudgementWall.spiritronCost` | 5 | Spiritron Cost to cast. |
| `JudgementWall.range` | 10 | The range in block of the magic. |
| `JudgementWall.width` | 4 | The width radius of Judgement Wall. |
| `JudgementWall.height` | 8 | The height of Judgement Wall. |
| `JudgementWall.damage` | 40 | The damage of Judgement Wall. |
| `JudgementWall.damageInterval` | 10 | The damaging interval in ticks of Judgement Wall. |
| `JudgementWall.damageIntervalMastered` | 5 | The damaging interval in ticks of Judgement Wall when mastered. |
| `JudgementWall.knockback` | 0.5 | The knockback multiplier. |
| `JudgementWall.knockResistNegate` | 0.6 | The knockback resistance negation. |
| `JudgementWall.wallDuration` | 10 | The duration in seconds. |
| `JudgementWall.wallDurationMastered` | 15 | The duration in seconds when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/common_tome_buried_wizard_tower`, `tensura:skills/common_tome_burnt_wizard_tower`, `tensura:skills/common_tome_frozen_wizard_tower`, `tensura:skills/common_tome_rotted_wizard_tower`, `tensura:skills/common_tome_ruined_wizard_tower`, `tensura:skills/found_in_tome`, `tensura:skills/low_basic_tome_dwarf_trade`, `tensura:skills/low_upgraded_tome_dwarf_trade`, `tensura:skills/magic`
