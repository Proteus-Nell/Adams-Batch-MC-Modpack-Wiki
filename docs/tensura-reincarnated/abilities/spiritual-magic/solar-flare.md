# Solar Flare

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Solar Flare](../../../assets/icons/tensura/skill/solar_flare.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:solar_flare` |
| **Element** | Light |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Cooldowns (s)** | 10 mastered, 20 otherwise |
| **Activation** | Hold |

</div>

> Shoot a shockwave of light energy to give nausea, blindness and slowness to all targets in a wide AOE.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 35,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Removed and re-rolled when you change race

## Related

- **Related skills:** [Abnormal Condition Nullification](../resistance-skills/abnormal-condition-nullification.md)
- **Effects:** [Flashed Blindness](../../effects/flashed-blindness.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `SolarFlare.castTime` | 120 | Cast time in tick. |
| `SolarFlare.castTimeMastered` | 120 | Cast time in tick when mastered. |
| `SolarFlare.magiculeCost` | 35,000 | Magicule Cost to cast. |
| `SolarFlare.radius` | 15 | The radius in block of the magic. |
| `SolarFlare.flareDamage` | 200 | The damage of the flare. |
| `SolarFlare.flareBlindness` | 2 | The level of the Flashed Blindness effect when applied by the magic. |
| `SolarFlare.flareNausea` | 1 | The level of the Nausea effect when applied by the magic. |
| `SolarFlare.flareSlowness` | 1 | The level of the Slowness effect when applied by the magic. |
| `SolarFlare.flareDuration` | 300 | The duration in tick of each effect when applied by the magic. |
| `SolarFlare.flareDurationMastered` | 600 | The duration in tick of each effect when applied by the magic when mastered. |
| `SolarFlare.cooldown` | 20 | The cooldown in second of the magic. |
| `SolarFlare.cooldownMastered` | 10 | The cooldown in second of the magic when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryMedium` | 500 | The max amount of mastery point for Medium Spiritual Magic. |
| `SpiritualMagic.masteryGreater` | 1,000 | The max amount of mastery point for Greater Spiritual Magic. |
| `SpiritualMagic.masteryLord` | 10,000 | The max amount of mastery point for Lord Spiritual Magic. |

## Tags

`tensura:skills/reset_with_race`, `tensura:skills/spiritual_magic`
