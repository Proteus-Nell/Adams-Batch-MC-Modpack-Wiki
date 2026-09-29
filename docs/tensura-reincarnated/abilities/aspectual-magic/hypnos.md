# Hypnos

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Hypnos](../../../assets/icons/tensura/skill/hypnos.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:hypnos` |
| **Element** | Mental |
| **Max mastery** | 1,500 |
| **Cooldowns (s)** | 1 mastered, 3 otherwise |
| **Activation** | Hold |

</div>

> Put even the strongest entities into sleep.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Can appear in epic tomes from wizard towers

## Related

- **Related skills:** [Spiritual Attack Nullification](../resistance-skills/spiritual-attack-nullification.md)
- **Effects:** [Sleep](../../effects/sleep.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Hypnos.castTime` | 180 | Cast time in tick. |
| `Hypnos.castTimeMastered` | 120 | Cast time in tick when mastered. |
| `Hypnos.magiculeMultiplierCost` | 0.025 | The multiplier of the target's EP to be calculated for the Magicule Cost to cast. |
| `Hypnos.minCost` | 50,000 | Minimum Magicule Cost to cast. |
| `Hypnos.range` | 6 | The range in block of the magic. |
| `Hypnos.sleepLevel` | 1 | The level of the Sleep effect. |
| `Hypnos.sleepLevelMastered` | 3 | The level of the Sleep effect when mastered. |
| `Hypnos.sleepDuration` | 1,200 | The duration in tick of the Sleep effect. |
| `Hypnos.sleepDurationResisted` | 600 | The duration in tick of the Sleep effect if the target has Spiritual Attack Nullification. |
| `Hypnos.sleepDurationMastered` | 2,400 | The duration in tick of the Sleep effect when mastered. |
| `Hypnos.sleepDurationMasteredResisted` | 1,200 | The duration in tick of the Sleep effect if the target has Spiritual Attack Nullification when mastered. |
| `Hypnos.cooldown` | 3 | The cooldown in second of the magic in the default mode. |
| `Hypnos.cooldownMastered` | 1 | The cooldown in second of the magic in the default mode when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/epic_tome_wizard_tower`
