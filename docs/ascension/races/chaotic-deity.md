# Chaotic Deity

<small>[Ascension](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `ascension:chaotic_deity` |
| **Difficulty** | Extreme |
| **Alignment** | Majin |
| **Aura** | 300 - 600 |
| **Magicule** | 1,500 - 2,500 |
| **Health bonus** | 10 |
| **Spiritual health bonus** | 5 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0 |

</div>

> A Fallen Angel ascended into a force of primordial chaos.

## Evolution

- **Evolves from:** [Fallen Angel](fallen-angel.md)

### Requirements to evolve into Chaotic Deity

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of chaotic_deity (evolution ep) | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Angel"]
  r1["Archangel"]
  r2["Chaotic Deity"]
  r3["Cosmic Deity"]
  r4["Divine Angel"]
  r5["Fallen Angel"]
  r6["Seraphim"]
  r7["Divine Bird"]
  r8["Harpy"]
  r9["Harpy Queen"]
  r10["Spirit Bird"]
  r0 --> r1
  r0 --> r9
  r0 --> r10
  r1 --> r6
  r1 --> r9
  r1 --> r10
  r4 --> r3
  r5 --> r2
  r6 --> r4
  r6 --> r5
  r8 --> r9
  r8 --> r10
  r9 --> r10
  r10 --> r7
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/titanification.png) [Titanification](../../tensura-reincarnated/abilities/intrinsic-skills/titanification.md)
- ![](../../assets/icons/tensura/skill/possession.png) [Possession](../../tensura-reincarnated/abilities/intrinsic-skills/possession.md)
- ![](../../assets/icons/tensura/skill/body_armor.png) [Body Armor](../../tensura-reincarnated/abilities/intrinsic-skills/body-armor.md)
- ![](../../assets/icons/tensura/skill/divine_ki_release.png) [Divine Ki Release](../../tensura-reincarnated/abilities/intrinsic-skills/divine-ki-release.md)
- ![](../../assets/icons/tensura/skill/light_transform.png) [Light Transform](../../tensura-reincarnated/abilities/intrinsic-skills/light-transform.md)

## Learnable skills

This race can learn these skills through training.

- ![](../../assets/icons/tensura/skill/thought_acceleration.png) [Thought Acceleration](../../tensura-reincarnated/abilities/extra-skills/thought-acceleration.md)
- ![](../../assets/icons/tensura/skill/multilayer_barrier.png) [Multilayer Barrier](../../tensura-reincarnated/abilities/extra-skills/multilayer-barrier.md)
- ![](../../assets/icons/tensura/skill/demon_lord_haki.png) [Demon Lord Haki](../../tensura-reincarnated/abilities/extra-skills/demon-lord-haki.md)
- ![](../../assets/icons/tensura/skill/magic_nullification.png) [Magic Nullification](../../tensura-reincarnated/abilities/resistance-skills/magic-nullification.md)
- ![](../../assets/icons/tensura/skill/physical_attack_nullification.png) [Physical Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/physical-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/darkness_attack_nullification.png) [Darkness Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/darkness-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/infinite_regeneration.png) [Infinite Regeneration](../../tensura-reincarnated/abilities/extra-skills/infinite-regeneration.md)
- ![](../../assets/icons/tensura/skill/darkness_attack_resistance.png) [Darkness Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/darkness-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/holy_attack_nullification.png) [Holy Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/holy-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/ultraspeed_regeneration.png) [Ultraspeed Regeneration](../../tensura-reincarnated/abilities/extra-skills/ultraspeed-regeneration.md)
- ![](../../assets/icons/tensura/skill/majesty.png) [Majesty](../../tensura-reincarnated/abilities/extra-skills/majesty.md)
- ![](../../assets/icons/tensura/skill/sacred_haki.png) [Sacred Haki](../../tensura-reincarnated/abilities/extra-skills/sacred-haki.md)
- ![](../../assets/icons/tensura/skill/magic_light_transform.png) [Magic Light Transform](../../tensura-reincarnated/abilities/extra-skills/magic-light-transform.md)
- ![](../../assets/icons/tensura/skill/light_attack_nullification.png) [Light Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/light-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/holy_attack_resistance.png) [Holy Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/holy-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/gravity_flight.png) [Gravity Flight](../../tensura-reincarnated/abilities/common-skills/gravity-flight.md)

## Traits

- Divine

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Safe Fall Distance | 3 | add |
| Scale | 0 | add |
| Max Health | 10 | add |
| Max Spiritual Health | 5 | add |
| Attack Damage | 0 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0 | add |
| Movement Speed | 0 | add |
| Swim Speed Multiplier | 0 | add |

## Stats (config defaults)

Set in [`config/tensura/race/harpy_config.toml`](../../tensura-reincarnated/configs/config-tensura-race-harpy-config.md).

| Option | Default | Description |
|---|---|---|
| `Harpy.safeFalling` | 3 | Bonus Safe Falling distance. |
| `Harpy.minAura` | 300 | Minimal aura. |
| `Harpy.maxAura` | 600 | Maximum aura. |
| `Harpy.minMagicule` | 1,500 | Minimal magicule. |
| `Harpy.maxMagicule` | 2,500 | Maximum magicule. |
| `Harpy.size` | 0 | Bonus Size. |
| `Harpy.maxHealth` | 10 | Bonus Max Health. |
| `Harpy.maxSpiritualHealth` | 5 | Bonus Max Spiritual Health. |
| `Harpy.attack` | 0 | Bonus Attack Damage. |
| `Harpy.attackSpeed` | 0 | Bonus Attack Speed. |
| `Harpy.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Harpy.movementSpeed` | 0 | Bonus Movement Speed. |
| `Harpy.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `Harpy.safeFalling` | 3 | Bonus Safe Falling distance. |
| `Harpy.flightBoost` | 0.75 | Flight Upward Boost Power. |
| `Harpy.flightCooldown` | 3 | Flight Boost Cooldown. |

## Tags

`tensura:races/divine`
