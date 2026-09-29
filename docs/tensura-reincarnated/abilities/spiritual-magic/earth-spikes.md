# Earth Spikes

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Earth Spikes](../../../assets/icons/tensura/skill/earth_spikes.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:earth_spikes` |
| **Element** | Earth |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Hold |

</div>

> Raises earth spikes from the ground to pierce through your enemies.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Gazel Dwargo](../../mobs/gazel-dwargo.md), [War Gnome](../../mobs/war-gnome.md)
- Removed and re-rolled when you change race

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `EarthSpikes.castTime` | 40 | Cast time in tick. |
| `EarthSpikes.castTimeMastered` | 40 | Cast time in tick when mastered. |
| `EarthSpikes.magiculeCost` | 500 | Magicule Cost to cast. |
| `EarthSpikes.range` | 20 | The range in block of the magic. |
| `EarthSpikes.spikeDamage` | 30 | The damage of each spike. |
| `EarthSpikes.spikeHeight` | 3 | The height in block of each spike. |

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
