# Mental Crush

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Mental Crush](../../../assets/icons/tensura/skill/mental_crush.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:mental_crush` |
| **Element** | Mental |
| **Max mastery** | 700 |
| **Cooldowns (s)** | 3 |
| **Activation** | Hold |

</div>

> Crush the mind of targets.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 30,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Can appear in rare tomes in buried wizard towers
- Can appear in rare tomes in burnt wizard towers
- Can appear in rare tomes in frozen wizard towers
- Can appear in rare tomes in rotted wizard towers
- Can appear in rare tomes in ruined wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Related skills:** [Spiritual Attack Nullification](../resistance-skills/spiritual-attack-nullification.md), [Spiritual Attack Resistance](../resistance-skills/spiritual-attack-resistance.md)
- **Effects:** [Fragility](../../effects/fragility.md), [Flashed Blindness](../../effects/flashed-blindness.md), [Insanity](../../effects/insanity.md)
- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `MentalCrush.castTime` | 100 | Cast time in tick. |
| `MentalCrush.magiculeCost` | 30,000 | Magicule Cost to cast. |
| `MentalCrush.range` | 6 | The range in block of the magic. |
| `MentalCrush.minSHP` | 100 | The minimal SHP damage that a target takes from the magic. |
| `MentalCrush.minSHPResisted` | 50 | The minimal SHP damage that a target takes from the magic if Spiritual Attack Resistance is toggled. |
| `MentalCrush.shpMultiplier` | 0.1 | The multiplier of max SHP that a target takes from the magic. |
| `MentalCrush.shpMultiplierResist` | 0.05 | The multiplier of max SHP that a target takes from the magic if Spiritual Attack Resistance is toggled. |
| `MentalCrush.shpMultiplierWeakened` | 0.2 | The multiplier of max SHP that a Weakened target takes from the magic with Mastery. |
| `MentalCrush.shpMultiplierWeakenedResist` | 0.1 | The multiplier of max SHP that a Weakened target takes from the magic with Mastery if Spiritual Attack Resistance is toggled. |
| `MentalCrush.fragilityLevel` | 2 | The level of Fragility that the magic applies on targets. |
| `MentalCrush.fragilityDuration` | 300 | The duration in second of Fragility that the magic applies on targets. |
| `MentalCrush.insanityChance` | 0.25 | The chance for targets to get Insanity from the magic. |
| `MentalCrush.insanityChanceWeakened` | 0.5 | The chance for Weakened targets to get Insanity from the magic. |
| `MentalCrush.insanityLevel` | 3 | The max level of Insanity that the magic can apply on targets. |
| `MentalCrush.insanityDuration` | 600 | The duration in second of Insanity that the magic applies on targets. |
| `MentalCrush.weakenedMultiplier` | 0.5 | The multiplier of max SHP that the target needs to be below to be considered Weakened. |
| `MentalCrush.cooldown` | 3 | The cooldown in second of the magic. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/rare_tome_buried_wizard_tower`, `tensura:skills/rare_tome_burnt_wizard_tower`, `tensura:skills/rare_tome_frozen_wizard_tower`, `tensura:skills/rare_tome_rotted_wizard_tower`, `tensura:skills/rare_tome_ruined_wizard_tower`
