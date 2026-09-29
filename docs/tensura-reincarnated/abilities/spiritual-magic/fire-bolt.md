# Fire Bolt

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Fire Bolt](../../../assets/icons/tensura/skill/fire_bolt.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:fire_bolt` |
| **Element** | Fire |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Hold |

</div>

> Shoots a flaming bolt.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Ifrit](../../mobs/ifrit.md), [Shizu](../../mobs/shizu.md)
- Removed and re-rolled when you change race

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `FireBolt.castTime` | 40 | Cast time in tick. |
| `FireBolt.castTimeMastered` | 20 | Cast time in tick when mastered. |
| `FireBolt.magiculeCost` | 1,000 | Magicule Cost to cast. |
| `FireBolt.damage` | 40 | The damage of the fire bolt. |
| `FireBolt.burnTick` | 60 | The burning duration in tick of targets hit by the fire bolt. |

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
