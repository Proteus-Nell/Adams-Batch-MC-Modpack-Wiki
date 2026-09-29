# Aerial Blade

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Aerial Blade](../../../assets/icons/tensura/skill/aerial_blade.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:aerial_blade` |
| **Element** | Wind |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Cooldowns (s)** | 5 mastered, 10 otherwise |
| **Activation** | Hold |

</div>

> Pull in any nearby entities before dealing massive damage by unleashing the power of your spirit.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 35,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Hinata Sakaguchi](../../mobs/hinata-sakaguchi.md), [Sylphide](../../mobs/sylphide.md)
- Removed and re-rolled when you change race

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `AerialBlade.castTime` | 100 | Cast time in tick. |
| `AerialBlade.castTimeMastered` | 100 | Cast time in tick when mastered. |
| `AerialBlade.magiculeCost` | 35,000 | Magicule Cost to cast. |
| `AerialBlade.range` | 3 | The range in block of the magic. |
| `AerialBlade.rangeMastered` | 4 | The range in block of the magic when mastered. |
| `AerialBlade.damage` | 200 | The damage of the magic. |
| `AerialBlade.cooldown` | 10 | The cooldown in second of the magic. |
| `AerialBlade.cooldownMastered` | 5 | The cooldown in second of the magic when mastered. |

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
