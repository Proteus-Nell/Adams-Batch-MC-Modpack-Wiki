# Solar Wave

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Solar Wave](../../../assets/icons/tensura/skill/solar_wave.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:solar_wave` |
| **Element** | Light |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Hold |

</div>

> Shoot a wave of light energy that blinds and slows hit enemies.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Removed and re-rolled when you change race

## Related

- **Summons / entities:** Solar Grenade

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `SolarWave.castTime` | 60 | Cast time in tick. |
| `SolarWave.castTimeMastered` | 60 | Cast time in tick when mastered. |
| `SolarWave.magiculeCost` | 1,000 | Magicule Cost to cast. |
| `SolarWave.waveDamage` | 30 | The damage of the projectile. |
| `SolarWave.waveRadius` | 4 | The radius in block of the wave. |
| `SolarWave.blindnessDuration` | 300 | The duration in tick of the Blindness effect when affected by the wave. |
| `SolarWave.blindnessLevel` | 1 | The level of the Blindness effect when affected by the wave. |
| `SolarWave.blindnessLevelMastered` | 2 | The level of the Blindness effect when affected by the wave with mastery. |

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
