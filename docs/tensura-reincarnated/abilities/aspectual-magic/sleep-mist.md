# Sleep Mist

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Sleep Mist](../../../assets/icons/tensura/skill/sleep_mist.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:sleep_mist` |
| **Element** | Water |
| **Max mastery** | 300 |
| **Activation** | Hold |

</div>

> Release a wide area of sleeping mist to paralyze targets.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Greater Daemon](../../mobs/greater-daemon.md)
- Can appear in common tomes in frozen wizard towers
- Sold by dwarf traders (medium basic tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill registry IDs automatically granted with Albis Vina.

## Related

- **Effects:** [Paralysis](../../effects/paralysis.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `SleepMist.castTime` | 100 | Cast time in tick. |
| `SleepMist.magiculeCost` | 5,000 | Magicule Cost to cast. |
| `SleepMist.mistRadius` | 5 | The radius in block of the sleep mist. |
| `SleepMist.mistLevel` | 2 | The level of the paralyzing effect. |
| `SleepMist.mistDuration` | 300 | The duration in tick of the sleep mist and the paralyzing effect. |
| `SleepMist.mistDurationMastered` | 500 | The duration in tick of the sleep mist and the paralyzing effect when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/common_tome_frozen_wizard_tower`, `tensura:skills/medium_basic_tome_dwarf_trade`
