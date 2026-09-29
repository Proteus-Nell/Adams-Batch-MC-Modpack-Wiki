# Kamehameha

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Kamehameha](../../../assets/icons/elitetensura/skill/kamehameha.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `elitetensura:kamehameha` |
| **Max mastery** | 700 |
| **Cooldowns (s)** | 3 mastered, 10 otherwise |
| **Activation** | Hold |

</div>

> Energy magic. Hold to gather magicule into a glowing sphere, then release to fire a sustained blue-white energy wave that tracks your aim, searing everything in its path and exploding against terrain. When mastered, hold past the cast time to charge a wider, far more destructive wave.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 2,500 |  |

## How it works

- Triggers when the held key is released

## Related

- **Related skills:** [Thunder Lance](../../../tensura-reincarnated/abilities/aspectual-magic/thunder-lance.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/MagicConfig.toml`](../../configs/config-tensura-elitetensura-magicconfig.md).

| Option | Default | Description |
|---|---|---|
| `Kamehameha.castTime` | 60 | Cast (charge) time in ticks (20 = 1s). |
| `Kamehameha.castTimeMastered` | 40 | Cast (charge) time in ticks when mastered. |
| `Kamehameha.magiculeCost` | 2,500 | Magicule cost per normal cast. |
| `Kamehameha.magiculeCostCharged` | 5,000 | Magicule cost for the charged (mastered, held-longer) cast. |
| `Kamehameha.cooldown` | 10 | Cooldown in seconds. |
| `Kamehameha.cooldownMastered` | 3 | Cooldown in seconds when mastered. |
| `Kamehameha.damage` | 20 | Damage per beam hit. The beam hits targets repeatedly while they stay inside it, so total damage over the full beam duration is several times this value. |
| `Kamehameha.damageCharged` | 35 | Damage per beam hit for the charged cast. |
| `Kamehameha.beamSize` | 1.5 | Beam thickness (blocks). |
| `Kamehameha.beamSizeCharged` | 2.5 | Beam thickness for the charged cast. |
| `Kamehameha.range` | 40 | Beam reach (blocks). |
| `Kamehameha.beamDuration` | 60 | How long the beam lasts, in ticks (the final 20 ticks fade out). |
| `Kamehameha.beamDurationCharged` | 100 | Beam duration in ticks for the charged cast. |
| `Kamehameha.explosionRadius` | 1.5 | Explosion radius where the beam meets terrain or targets (0 = no explosion). |
| `Kamehameha.explosionRadiusCharged` | 3 | Explosion radius for the charged cast. |

Set in [`config/tensura/ability/magic_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`
