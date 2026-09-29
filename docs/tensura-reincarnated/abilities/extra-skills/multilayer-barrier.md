# Multilayer Barrier

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Multilayer Barrier](../../../assets/icons/tensura/skill/multilayer_barrier.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:multilayer_barrier` |
| **Cooldowns (s)** | 10 |
| **Activation** | Press |

</div>

> Protect yourself with a multitude of powerful defensive barriers.

## How it works

- Activated by pressing the skill key

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| attributeInstance | barrier points | add |

## Obtaining

- Can be learned by: [Cosmic Deity](../../../ascension/races/cosmic-deity.md), [Chaotic Deity](../../../ascension/races/chaotic-deity.md), [Wishbound Djinn](../../../ascension/races/wishbound-djinn.md), [Primordial Djinn](../../../ascension/races/primordial-djinn.md), [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md), [Divine King](../../../ascension/races/divine-king.md), [Sun Wukong](../../../ascension/races/sun-wukong.md), [Dark Lord Dullahan](../../../ascension/races/dark-lord-dullahan.md)
- Listed in the `conditionPurgeIds` config option (config/nightmare/ability/skill/nightmare_ult.toml): Effect IDs purged by Remove barrier break and Dispel (namespace:path).

## Related

- **Referenced by:** [Ranged Barrier](../common-skills/ranged-barrier.md), [Elegy](../../../tr-nightmares/abilities/unique-skills/elegy.md), [｢ Hastur, Lord of Starwind ｣](../../../tr-nightmares/abilities/ultimate-skills/hastur.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `MultilayerBarrier.magiculeCost` | 5 | Base Magicule Cost to block damage per damage point. |
| `MultilayerBarrier.pointMultiplier` | 1.5 | The barrier point multiplier compared to the user's maximum health. |
| `MultilayerBarrier.allyPointMultiplier` | 0.75 | The barrier point multiplier compared to the target's maximum health when used on an ally. |
| `MultilayerBarrier.cooldown` | 10 | The cooldown in seconds of this skill when activated. |

## Tags

`tensura:skills/extra_skills`
