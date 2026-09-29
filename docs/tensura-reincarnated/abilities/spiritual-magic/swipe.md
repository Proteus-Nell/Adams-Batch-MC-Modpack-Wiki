# Swipe

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Swipe](../../../assets/icons/tensura/skill/swipe.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:swipe` |
| **Element** | Space |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Hold |

</div>

> Slashing through space in a straight line, displacing entities or teleporting the caster.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Hinata Sakaguchi](../../mobs/hinata-sakaguchi.md)
- Removed and re-rolled when you change race

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `Swipe.castTime` | 60 | Cast time in tick. |
| `Swipe.castTimeMastered` | 60 | Cast time in tick when mastered. |
| `Swipe.magiculeCost` | 50,000 | Magicule Cost to cast. |
| `Swipe.range` | 15 | The range in block of the magic. |
| `Swipe.rangeMastered` | 20 | The range in block of the magic when mastered. |
| `Swipe.damage` | 200 | The damage of the magic. |
| `Swipe.damageMastered` | 300 | The damage of the magic when mastered. |
| `Swipe.cooldown` | 5 | The cooldown in second of the magic. |
| `Swipe.cooldownMastered` | 3 | The cooldown in second of the magic when mastered. |

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
