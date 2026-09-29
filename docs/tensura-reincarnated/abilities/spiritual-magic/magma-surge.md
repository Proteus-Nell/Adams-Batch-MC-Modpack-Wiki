# Magma Surge

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Magma Surge](../../../assets/icons/tensura/skill/magma_surge.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:magma_surge` |
| **Element** | Earth |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Cooldowns (s)** | 5 mastered, 10 otherwise |
| **Activation** | Hold |

</div>

> Fire a spread of lava that burns and melts anything for a limited time.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 40,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Removed and re-rolled when you change race

## Related

- **Related skills:** [Burden](../aspectual-magic/burden.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `MagmaSurge.castTime` | 80 | Cast time in tick. |
| `MagmaSurge.castTimeMastered` | 80 | Cast time in tick when mastered. |
| `MagmaSurge.magiculeCost` | 40,000 | Magicule Cost to cast. |
| `MagmaSurge.magmaDamage` | 200 | The damage of each magma projectile. |
| `MagmaSurge.magmaDamageMastered` | 300 | The damage of each magma projectile when mastered. |
| `MagmaSurge.burdenLevel` | 2 | The level of the Burden effect when mastered. |
| `MagmaSurge.burdenDuration` | 200 | The duration in tick of the Burden effect when mastered. |
| `MagmaSurge.cooldown` | 10 | The cooldown in second of the magic. |
| `MagmaSurge.cooldownMastered` | 5 | The cooldown in second of the magic when mastered. |

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
