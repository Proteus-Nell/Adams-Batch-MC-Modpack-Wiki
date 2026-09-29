# Gravitational Void

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Gravitational Void](../../../assets/icons/mysticism/skill/gravitational_void.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `mysticism:gravitational_void` |
| **Element** | Earth |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Cooldowns (s)** | 300 mastered, 420 otherwise, 300, 420 |
| **Activation** | Hold |

</div>

> A black hole sucking everything into a singularity

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500,000 |  |

## How it works

- Triggers when the held key is released

## Related

- **Summons / entities:** Black Hole

## Stats (config defaults)

Set in [`config/mysticism/ability/magic/spiritual_config.toml`](../../configs/config-mysticism-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `GravitationalVoid.castTime` | 400 | Cast time in tick. |
| `GravitationalVoid.castTimeMastered` | 120 | Cast time in tick when mastered. |
| `GravitationalVoid.magiculeCost` | 500,000 | Magicule Cost to cast. |
| `GravitationalVoid.baseGravityDamage` | 50 | The base gravity damage of the black hole. |
| `GravitationalVoid.baseMagicDamage` | 50 | The base magic damage of the black hole. |
| `GravitationalVoid.maxGravityDamage` | 250 | The max gravity damage of the black hole. |
| `GravitationalVoid.maxMagicDamage` | 250 | The max magic damage of the black hole. |
| `GravitationalVoid.maxSize` | 10 | The maximum size of the black hole. |
| `GravitationalVoid.lifespan` | 1,200 | The lifespan of the black hole in ticks. |
| `GravitationalVoid.lifespanMastered` | 3,600 | The lifespan of the black hole in ticks when the magic is mastered. |
| `GravitationalVoid.cooldown` | 420 | The cooldown in second of the magic. |
| `GravitationalVoid.cooldownMastered` | 300 | The cooldown in second of the magic when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryMedium` | 500 | The max amount of mastery point for Medium Spiritual Magic. |
| `SpiritualMagic.masteryGreater` | 1,000 | The max amount of mastery point for Greater Spiritual Magic. |
| `SpiritualMagic.masteryLord` | 10,000 | The max amount of mastery point for Lord Spiritual Magic. |
