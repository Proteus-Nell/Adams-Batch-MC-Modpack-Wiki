# Solar Rain

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Solar Rain](../../../assets/icons/tensura/skill/solar_rain.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:solar_rain` |
| **Element** | Light |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Hold |

</div>

> Shoot many light projectiles that deal massive damage to undead creatures.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 8,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Removed and re-rolled when you change race

## Related

- **Summons / entities:** Light Arrow

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `SolarRain.castTime` | 80 | Cast time in tick. |
| `SolarRain.castTimeMastered` | 80 | Cast time in tick when mastered. |
| `SolarRain.magiculeCost` | 8,000 | Magicule Cost to cast. |
| `SolarRain.range` | 20 | The range in block of the magic. |
| `SolarRain.rangeMastered` | 30 | The range in block of the magic when mastered. |
| `SolarRain.arrowNumber` | 10 | The number of arrows when casted. |
| `SolarRain.arrowNumberMastered` | 20 | The number of arrows when casted with mastery. |
| `SolarRain.arrowDamage` | 30 | The damage of each arrow when casted. |
| `SolarRain.cooldown` | 5 | The cooldown in second of the magic. |
| `SolarRain.cooldownMastered` | 3 | The cooldown in second of the magic when mastered. |

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
