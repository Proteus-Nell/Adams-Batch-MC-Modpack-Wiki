# Curse

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Curse](../../../assets/icons/tensura/skill/curse.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:curse` |
| **Element** | Necromancy |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Hold |

</div>

> Release Miasmic Mist to curse targets.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10,000 |  |

## How it works

- Triggers when the held key is released
- Does something when mastered

## Obtaining

- Intrinsic skill of: [Spirit Skeleton](../../races/spirit-skeleton.md), [Divine Skeleton](../../races/divine-skeleton.md)
- Can appear in uncommon tomes in rotted wizard towers

## Related

- **Related skills:** [Curse Bind](curse-bind.md)
- **Summons / entities:** Miasmic Mist
- **Referenced by:** [Curse Bind](curse-bind.md), [Survivor](../unique-skills/survivor.md), [Abnormal Condition Resistance](../resistance-skills/abnormal-condition-resistance.md), [Abnormal Condition Nullification](../resistance-skills/abnormal-condition-nullification.md), [Soul Shrine](../../../tr-nightmares/abilities/unique-skills/soul-shrine.md), [｢ Mammon, Lord of Greed ｣](../../../tr-nightmares/abilities/ultimate-skills/mammon.md), [Caedros, God of Conquest](../../../tensura-more-skills/abilities/ultimate-skills/caedros-god-of-conquest.md), [Pain, Lord of Six Paths](../../../tensura-more-skills/abilities/ultimate-skills/pain-lord-of-six-paths.md), [Schwi, Lord of True Computation](../../../tensura-more-skills/abilities/ultimate-skills/schwi-ex-machina.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `Curse.castTime` | 120 | Cast time in tick. |
| `Curse.magiculeCost` | 10,000 | Magicule Cost to cast. |
| `Curse.mistRadius` | 5 | The radius in block of the miasmic mist. |
| `Curse.mistInterval` | 40 | The damage interval in tick of the miasmic mist. |
| `Curse.mistDamage` | 40 | The amount of magic damage each interval of the miasmic mist. |
| `Curse.mistDamageMastered` | 60 | The amount of magic damage each interval of the miasmic mist when mastered. |
| `Curse.curseLevel` | 1 | The level of the curse effect. |
| `Curse.curseLevelMastered` | 2 | The level of the curse effect when mastered. |
| `Curse.curseDuration` | 600 | The duration in tick of the curse effect. |
| `Curse.mistDuration` | 400 | The duration in tick of the miasmic mist. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryMedium` | 500 | The max amount of mastery point for Medium Spiritual Magic. |
| `SpiritualMagic.masteryGreater` | 1,000 | The max amount of mastery point for Greater Spiritual Magic. |
| `SpiritualMagic.masteryLord` | 10,000 | The max amount of mastery point for Lord Spiritual Magic. |

## Tags

`tensura:skills/necromancy_magic`, `tensura:skills/spiritual_magic`, `tensura:skills/uncommon_tome_rotted_wizard_tower`
