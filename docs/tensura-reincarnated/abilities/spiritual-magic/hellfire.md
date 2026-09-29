# Hellfire

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Hellfire](../../../assets/icons/tensura/skill/hellfire.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:hellfire` |
| **Element** | Fire |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Hold |

</div>

> Summon a sphere of hellfire to deal massive damage in a small area.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 45,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Hinata Sakaguchi](../../mobs/hinata-sakaguchi.md), [Ifrit](../../mobs/ifrit.md), [Shizu](../../mobs/shizu.md)
- Removed and re-rolled when you change race

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `Hellfire.castTime` | 100 | Cast time in tick. |
| `Hellfire.castTimeMastered` | 100 | Cast time in tick when mastered. |
| `Hellfire.magiculeCost` | 45,000 | Magicule Cost to cast. |
| `Hellfire.range` | 15 | The range in block of the magic. |
| `Hellfire.rangeMastered` | 20 | The range in block of the magic when mastered. |
| `Hellfire.sphereDamage` | 200 | The damage of the Hellfire. |
| `Hellfire.sphereDamageMastered` | 300 | The damage of the Hellfire. |
| `Hellfire.sphereRadius` | 2.5 | The radius of the Hellfire. |
| `Hellfire.sphereRadiusMastered` | 5 | The radius of the Hellfire when mastered. |
| `Hellfire.cooldown` | 5 | The cooldown in second of the magic. |
| `Hellfire.cooldownMastered` | 3 | The cooldown in second of the magic when mastered. |

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
