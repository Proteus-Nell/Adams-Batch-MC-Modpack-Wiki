# Analyze

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Analyze](../../../assets/icons/tensura/skill/analyze.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:analyze` |
| **Element** | Misc |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Analyze targets' status and power.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50 |  |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (low rare tome)
- Can appear in uncommon tomes in burnt wizard towers

## Related

- **Referenced by:** [Analytical Appraisal](../extra-skills/analytical-appraisal.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Analyze.castTime` | 40 | Cast time in tick. |
| `Analyze.magiculeCost` | 50 | Magicule Cost per second to cast. |
| `Analyze.bonusAnalysis` | 1 | The Bonus Analysis Level when held. |
| `Analyze.bonusAnalysisMastered` | 2 | The Bonus Analysis Level when held while mastered. |
| `Analyze.bonusAnalysisRadius` | 5 | The Bonus Analysis Distance when held. |
| `Analyze.bonusAnalysisRadiusMastered` | 10 | The Bonus Analysis Distance when held with Mastery. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/low_rare_tome_dwarf_trade`, `tensura:skills/uncommon_tome_burnt_wizard_tower`
