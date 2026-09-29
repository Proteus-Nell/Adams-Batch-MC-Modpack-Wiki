# Gauth

<small>[Ascension](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `ascension:gauth` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Extreme |
| **Alignment** | Majin |
| **Aura** | 300 - 300 |
| **Magicule** | 700 - 700 |
| **Health bonus** | -8 |
| **Spiritual health bonus** | -16 |
| **Attack damage bonus** | -0.5 |
| **Movement speed bonus** | -0.02 |

</div>

> A lesser beholder of armored body and unraveling eyestalks.

## Evolution

- **Evolves from:** [Mindwitness](mindwitness.md)
- **Evolves into:** [Beholder](beholder.md)
- **Default evolution:** [Beholder](beholder.md)
- **On awakening (True Demon Lord / True Hero):** [Beholder](beholder.md)
- **During the Harvest Festival:** [Beholder](beholder.md)

### Requirements to evolve into Gauth

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 800,000 | 50% |
| True Demon Lord | 50% |

### Evolution tree

```mermaid
flowchart LR
  r0["Beholder"]
  r1["Death Tyrant"]
  r2["Gauth"]
  r3["Gazer"]
  r4["Mindwitness"]
  r5["Spectator"]
  r0 --> r1
  r2 --> r0
  r3 --> r5
  r4 --> r2
  r5 --> r4
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/body_armor.png) [Body Armor](../../tensura-reincarnated/abilities/intrinsic-skills/body-armor.md)
- ![](../../assets/icons/tensura/skill/possession.png) [Possession](../../tensura-reincarnated/abilities/intrinsic-skills/possession.md)
- ![](../../assets/icons/tensura/skill/charm.png) [Charm](../../tensura-reincarnated/abilities/intrinsic-skills/charm.md)
- ![](../../assets/icons/tensura/skill/drain.png) [Drain](../../tensura-reincarnated/abilities/intrinsic-skills/drain.md)

## Learnable skills

This race can learn these skills through training.

- ![](../../assets/icons/tensura/skill/magic_nullification.png) [Magic Nullification](../../tensura-reincarnated/abilities/resistance-skills/magic-nullification.md)
- ![](../../assets/icons/tensura/skill/spiritual_attack_nullification.png) [Spiritual Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/spiritual-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/mortal_fear.png) [Mortal Fear](../../tensura-reincarnated/abilities/extra-skills/mortal-fear.md)
- ![](../../assets/icons/tensura/skill/magic_jamming.png) [Magic Jamming](../../tensura-reincarnated/abilities/extra-skills/magic-jamming.md)
- ![](../../assets/icons/tensura/skill/thought_acceleration.png) [Thought Acceleration](../../tensura-reincarnated/abilities/extra-skills/thought-acceleration.md)
- ![](../../assets/icons/tensura/skill/analytical_appraisal.png) [Analytical Appraisal](../../tensura-reincarnated/abilities/extra-skills/analytical-appraisal.md)
- ![](../../assets/icons/tensura/skill/abnormal_condition_resistance.png) [Abnormal Condition Resistance](../../tensura-reincarnated/abilities/resistance-skills/abnormal-condition-resistance.md)
- ![](../../assets/icons/tensura/skill/magic_sense.png) [Magic Sense](../../tensura-reincarnated/abilities/extra-skills/magic-sense.md)
- ![](../../assets/icons/tensura/skill/danger_sense.png) [Danger Sense](../../tensura-reincarnated/abilities/extra-skills/danger-sense.md)
- ![](../../assets/icons/tensura/skill/spiritual_attack_resistance.png) [Spiritual Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/spiritual-attack-resistance.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0.4 | add |
| Scale | 0.25 | add |
| Scale | 0.05 | add |
| Scale | -0.15 | add |
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
