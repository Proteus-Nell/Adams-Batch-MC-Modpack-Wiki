# Wind Blade

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Wind Blade](../../../assets/icons/tensura/skill/wind_blade.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:wind_blade` |
| **Element** | Wind |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Cooldowns (s)** | 2 |
| **Activation** | Hold |

</div>

> Fires a concentrated blade of wind which has heavy knockback.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Sylphide](../../mobs/sylphide.md)
- Removed and re-rolled when you change race

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `WindBlade.castTime` | 40 | Cast time in tick. |
| `WindBlade.castTimeMastered` | 20 | Cast time in tick when mastered. |
| `WindBlade.magiculeCost` | 500 | Magicule Cost to cast. |
| `WindBlade.damage` | 20 | The damage of the wind blade. |
| `WindBlade.cooldown` | 2 | The cooldown in second of the magic. |

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
