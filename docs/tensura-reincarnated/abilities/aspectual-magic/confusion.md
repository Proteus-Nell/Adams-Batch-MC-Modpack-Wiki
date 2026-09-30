# Confusion

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Confusion](../../../assets/icons/tensura/skill/confusion.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:confusion` |
| **Element** | Illusion |
| **Max mastery** | 300 |
| **Activation** | Hold |

</div>

> Apply vision confusion to surrounding targets.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 2,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (medium rare tome)
- Can appear in rare tomes in rotted wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Summons / entities:** Tensura
- **Referenced by:** [Lunatic](../../../tr-nightmares/abilities/unique-skills/lunatic.md), [Dragon Factor Haki](../../../tr-nightmares/abilities/intrinsic-skills/dragon-factor-haki.md), [Witch of Vainglory](../../../tensura-more-skills/abilities/ultimate-skills/witch-of-vainglory.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Confusion.castTime` | 100 | Cast time in tick. |
| `Confusion.magiculeCost` | 2,000 | Magicule Cost to cast. |
| `Confusion.radius` | 10 | The radius in block of the magic. |
| `Confusion.confusionLevel` | 1 | The level of the Confusion effect per 25% EP difference between the target and the caster. |
| `Confusion.confusionMaxLevel` | 3 | The maximum level of the Confusion effect. |
| `Confusion.confusionMaxLevelMastered` | 4 | The maximum level of the Confusion effect when mastered. |
| `Confusion.confusionDuration` | 300 | The duration of the Confusion effect when casted. |
| `Confusion.confusionDurationMastered` | 400 | The duration of the Confusion effect when casted with mastery. |
| `Confusion.bypassEP` | 1.5 | The multiplier of the caster's EP that the target needs to have above to be not applied by Confusion. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/medium_rare_tome_dwarf_trade`, `tensura:skills/rare_tome_rotted_wizard_tower`
