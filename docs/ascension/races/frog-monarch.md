# Frog Monarch

<small>[Ascension](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `ascension:frog_monarch` |
| **Difficulty** | Extreme |
| **Alignment** | Default |
| **Aura** | 300 - 300 |
| **Magicule** | 700 - 700 |
| **Health bonus** | -8 |
| **Spiritual health bonus** | -16 |
| **Attack damage bonus** | -0.5 |
| **Movement speed bonus** | -0.02 |

</div>

> The pinnacle of frogkind. Combines the wisdom of the bog with the corruption of venom.

## Evolution

- **Evolves from:** [Bog Ancient](bog-ancient.md), [Venom Lord](venom-lord.md)

### Requirements to evolve into Frog Monarch

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 2,000,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Bog Ancient"]
  r1["Frog"]
  r2["Frog Monarch"]
  r3["Giant Frog"]
  r4["Poison Toad"]
  r5["Swamp Sovereign"]
  r6["Venom Lord"]
  r0 --> r2
  r1 --> r3
  r3 --> r4
  r4 --> r5
  r5 --> r0
  r5 --> r6
  r6 --> r2
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/drain.png) [Drain](../../tensura-reincarnated/abilities/intrinsic-skills/drain.md)
- ![](../../assets/icons/tensura/skill/blood_mist.png) [Blood Mist](../../tensura-reincarnated/abilities/intrinsic-skills/blood-mist.md)
- ![](../../assets/icons/tensura/skill/titanification.png) [Titanification](../../tensura-reincarnated/abilities/intrinsic-skills/titanification.md)
- ![](../../assets/icons/tensura/skill/body_armor.png) [Body Armor](../../tensura-reincarnated/abilities/intrinsic-skills/body-armor.md)
- ![](../../assets/icons/tensura/skill/poisonous_breath.png) [Poisonous Breath](../../tensura-reincarnated/abilities/intrinsic-skills/poisonous-breath.md)
- ![](../../assets/icons/tensura/skill/giantification.png) [Giantification](../../tensura-reincarnated/abilities/intrinsic-skills/giantification.md)
- ![](../../assets/icons/tensura/skill/water_breathing.png) [Water Breathing](../../tensura-reincarnated/abilities/intrinsic-skills/water-breathing.md)

## Learnable skills

This race can learn these skills through training.

- ![](../../assets/icons/tensura/skill/ultraspeed_regeneration.png) [Ultraspeed Regeneration](../../tensura-reincarnated/abilities/extra-skills/ultraspeed-regeneration.md)
- ![](../../assets/icons/tensura/skill/earth_manipulation.png) [Earth Manipulation](../../tensura-reincarnated/abilities/extra-skills/earth-manipulation.md)
- ![](../../assets/icons/tensura/skill/thought_acceleration.png) [Thought Acceleration](../../tensura-reincarnated/abilities/extra-skills/thought-acceleration.md)
- ![](../../assets/icons/tensura/skill/magic_darkness_transform.png) [Magic Darkness Transform](../../tensura-reincarnated/abilities/extra-skills/magic-darkness-transform.md)
- ![](../../assets/icons/tensura/skill/mortal_fear.png) [Mortal Fear](../../tensura-reincarnated/abilities/extra-skills/mortal-fear.md)
- ![](../../assets/icons/tensura/skill/infinite_regeneration.png) [Infinite Regeneration](../../tensura-reincarnated/abilities/extra-skills/infinite-regeneration.md)
- ![](../../assets/icons/tensura/skill/paralysis_nullification.png) [Paralysis Nullification](../../tensura-reincarnated/abilities/resistance-skills/paralysis-nullification.md)
- ![](../../assets/icons/tensura/skill/water_manipulation.png) [Water Manipulation](../../tensura-reincarnated/abilities/extra-skills/water-manipulation.md)
- ![](../../assets/icons/tensura/skill/poison_nullification.png) [Poison Nullification](../../tensura-reincarnated/abilities/resistance-skills/poison-nullification.md)
- ![](../../assets/icons/tensura/skill/physical_attack_resistance.png) [Physical Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/physical-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/poison_resistance.png) [Poison Resistance](../../tensura-reincarnated/abilities/resistance-skills/poison-resistance.md)
- ![](../../assets/icons/tensura/skill/water_current_control.png) [Water Current Control](../../tensura-reincarnated/abilities/common-skills/water-current-control.md)
- ![](../../assets/icons/ascension/skill/toxic_skin.png) [Toxic Skin](../abilities/extra-skills/toxic-skin.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0.05 | add |
| Scale | -0.08 | add |
| Scale | -0.15 | add |
| Scale | -0.2 | add |
| Scale | -0.3 | add |
| Scale | size | add |
| Max Health | max HP | add |
| Max Spiritual Health | max spiritual HP | add |
| Attack Damage | attack | add |
| Attack Speed | attack speed | add |
| Knockback Resistance | knockback resistance | add |
| Movement Speed | movement speed | add |
| Swim Speed Multiplier | swim speed | add |

## Stats (config defaults)

Set in [`config/tensura/race/goblin_config.toml`](../../tensura-reincarnated/configs/config-tensura-race-goblin-config.md).

| Option | Default | Description |
|---|---|---|
| `Goblin.minAura` | 300 | Minimal aura. |
| `Goblin.maxAura` | 300 | Maximum aura. |
| `Goblin.minMagicule` | 700 | Minimal magicule. |
| `Goblin.maxMagicule` | 700 | Maximum magicule. |
| `Goblin.size` | -0.25 | Bonus Size. |
| `Goblin.maxHealth` | -8 | Bonus Max Health. |
| `Goblin.maxSpiritualHealth` | -16 | Bonus Max Spiritual Health. |
| `Goblin.attack` | -0.5 | Bonus Attack Damage. |
| `Goblin.attackSpeed` | -0.5 | Bonus Attack Speed. |
| `Goblin.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Goblin.movementSpeed` | -0.02 | Bonus Movement Speed. |
| `Goblin.swimSpeed` | -0.2 | Bonus Swimming Speed Multiplier. |
