# 9 Tailed Fox

<small>[Ascension](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `ascension:nine_tail_fox` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Extreme |
| **Alignment** | Default |
| **Aura** | 1,500 - 2,500 |
| **Magicule** | 300 - 600 |
| **Health bonus** | 2 |
| **Spiritual health bonus** | 10 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0.05 |

</div>

> The legendary nine-tailed fox — a true hero of fox-kind.

## Evolution

- **Evolves from:** [6 Tailed Fox](six-tail-fox.md)
- **Evolves into:** [Divine Kitsune](divine-kitsune.md)
- **Default evolution:** [Divine Kitsune](divine-kitsune.md)
- **On awakening (True Demon Lord / True Hero):** [Divine Kitsune](divine-kitsune.md)
- **During the Harvest Festival:** [Divine Kitsune](divine-kitsune.md)

### Requirements to evolve into 9 Tailed Fox

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 900,000 | 50% |
| Consume 5 of [Elemental Essence](../../tensura-reincarnated/items/materials/elemental-essence.md) | 50% |

### Evolution tree

```mermaid
flowchart LR
  r0["Divine Kitsune"]
  r1["Kitsune"]
  r2["9 Tailed Fox"]
  r3["6 Tailed Fox"]
  r4["3 Tailed Fox"]
  r1 --> r4
  r2 --> r0
  r3 --> r2
  r4 --> r3
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/light_transform.png) [Light Transform](../../tensura-reincarnated/abilities/intrinsic-skills/light-transform.md)
- ![](../../assets/icons/tensura/skill/divine_ki_release.png) [Divine Ki Release](../../tensura-reincarnated/abilities/intrinsic-skills/divine-ki-release.md)
- ![](../../assets/icons/tensura/skill/charm.png) [Charm](../../tensura-reincarnated/abilities/intrinsic-skills/charm.md)
- ![](../../assets/icons/ascension/skill/sharpened_claws.png) [Sharpened Claws](../abilities/intrinsic-skills/sharpened-claws.md)

## Learnable skills

This race can learn these skills through training.

- ![](../../assets/icons/tensura/skill/infinite_regeneration.png) [Infinite Regeneration](../../tensura-reincarnated/abilities/extra-skills/infinite-regeneration.md)
- ![](../../assets/icons/tensura/skill/majesty.png) [Majesty](../../tensura-reincarnated/abilities/extra-skills/majesty.md)
- ![](../../assets/icons/tensura/skill/magic_nullification.png) [Magic Nullification](../../tensura-reincarnated/abilities/resistance-skills/magic-nullification.md)
- ![](../../assets/icons/tensura/skill/holy_attack_nullification.png) [Holy Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/holy-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/ultraspeed_regeneration.png) [Ultraspeed Regeneration](../../tensura-reincarnated/abilities/extra-skills/ultraspeed-regeneration.md)
- ![](../../assets/icons/tensura/skill/spatial_motion.png) [Spatial Motion](../../tensura-reincarnated/abilities/extra-skills/spatial-motion.md)
- ![](../../assets/icons/tensura/skill/thought_acceleration.png) [Thought Acceleration](../../tensura-reincarnated/abilities/extra-skills/thought-acceleration.md)
- ![](../../assets/icons/tensura/skill/sacred_haki.png) [Sacred Haki](../../tensura-reincarnated/abilities/extra-skills/sacred-haki.md)
- ![](../../assets/icons/tensura/skill/flame_attack_nullification.png) [Flame Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/flame-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/holy_attack_resistance.png) [Holy Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/holy-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/mana_manipulation.png) [Mana Manipulation](../../tensura-reincarnated/abilities/extra-skills/mana-manipulation.md)
- ![](../../assets/icons/tensura/skill/snake_eye.png) [Snake Eye](../../tensura-reincarnated/abilities/extra-skills/snake-eye.md)
- ![](../../assets/icons/tensura/skill/magic_resistance.png) [Magic Resistance](../../tensura-reincarnated/abilities/resistance-skills/magic-resistance.md)
- ![](../../assets/icons/tensura/skill/magic_sense.png) [Magic Sense](../../tensura-reincarnated/abilities/extra-skills/magic-sense.md)
- ![](../../assets/icons/tensura/skill/danger_sense.png) [Danger Sense](../../tensura-reincarnated/abilities/extra-skills/danger-sense.md)
- ![](../../assets/icons/tensura/skill/farsight.png) [Farsight](../../tensura-reincarnated/abilities/common-skills/farsight.md)
- ![](../../assets/icons/tensura/skill/flame_attack_resistance.png) [Flame Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/flame-attack-resistance.md)

## Traits

- Divine

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0.2 | add |
| Scale | 0.1 | add |
| Scale | 0 | add |
| Scale | -0.1 | add |
| Scale | size | add |
| Max Health | max HP | add |
| Max Spiritual Health | max spiritual HP | add |
| Attack Damage | attack | add |
| Attack Speed | attack speed | add |
| Knockback Resistance | knockback resistance | add |
| Movement Speed | movement speed | add |
| Swim Speed Multiplier | swim speed | add |

## Stats (config defaults)

Set in [`config/tensura/race/beastfolk_config.toml`](../../tensura-reincarnated/configs/config-tensura-race-beastfolk-config.md).

| Option | Default | Description |
|---|---|---|
| `Beastfolk.minAura` | 1,500 | Minimal aura. |
| `Beastfolk.maxAura` | 2,500 | Maximum aura. |
| `Beastfolk.minMagicule` | 300 | Minimal magicule. |
| `Beastfolk.maxMagicule` | 600 | Maximum magicule. |
| `Beastfolk.size` | 0 | Bonus Size. |
| `Beastfolk.maxHealth` | 2 | Bonus Max Health. |
| `Beastfolk.maxSpiritualHealth` | 10 | Bonus Max Spiritual Health. |
| `Beastfolk.attack` | 0 | Bonus Attack Damage. |
| `Beastfolk.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `Beastfolk.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Beastfolk.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `Beastfolk.swimSpeed` | 0.5 | Bonus Swimming Speed Multiplier. |

## Tags

`tensura:races/divine`
