# Healthcare

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Healthcare](../../../assets/icons/tensura/skill/healthcare.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:healthcare` |
| **Element** | Misc |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Boost the caster's health and saturation.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 |  |

## How it works

- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Obtaining

- Sold by dwarf traders (low rare tome)
- Can appear in uncommon tomes in burnt wizard towers

## Related

- **Referenced by:** [Green Thumb](../../../tensura-more-skills/abilities/unique-skills/green-thumb.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Healthcare.castTime` | 100 | Cast time in tick. |
| `Healthcare.magiculeCost` | 100 | Magicule Cost to cast. |
| `Healthcare.healthRegeneration` | 1 | The health regeneration boost every 2 seconds. |
| `Healthcare.careDuration` | 10,000 | The duration in tick of the Healthcare effect. |
| `Healthcare.careDurationMastered` | 100,000 | The duration in tick of the Healthcare effect when mastered. |

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
