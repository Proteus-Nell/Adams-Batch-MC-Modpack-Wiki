# Divine King

<small>[Ascension](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `ascension:divine_king` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Hard |
| **Alignment** | Holy |
| **Aura** | 300 - 300 |
| **Magicule** | 700 - 700 |
| **Health bonus** | -8 |
| **Spiritual health bonus** | -16 |
| **Attack damage bonus** | -0.5 |
| **Movement speed bonus** | -0.02 |

</div>

> A Monkey King who crossed into divinity.

## Evolution

- **Evolves from:** [Monkey King](monkey-king.md)
- **Evolves into:** [Sun Wukong](sun-wukong.md)
- **Default evolution:** [Sun Wukong](sun-wukong.md)
- **On awakening (True Demon Lord / True Hero):** [Sun Wukong](sun-wukong.md)
- **During the Harvest Festival:** [Sun Wukong](sun-wukong.md)

### Requirements to evolve into Divine King

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 750,000 | 50% |
| Kill 2 bosses | 50% |

### Evolution tree

```mermaid
flowchart LR
  r0["Divine King"]
  r1["Monkey"]
  r2["Monkey King"]
  r3["Monkey Martial Artist"]
  r4["Monkey Warrior"]
  r5["Sun Wukong"]
  r0 --> r5
  r1 --> r4
  r2 --> r0
  r3 --> r2
  r4 --> r3
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/divine_ki_release.png) [Divine Ki Release](../../tensura-reincarnated/abilities/intrinsic-skills/divine-ki-release.md)
- ![](../../assets/icons/tensura/skill/body_armor.png) [Body Armor](../../tensura-reincarnated/abilities/intrinsic-skills/body-armor.md)
- ![](../../assets/icons/tensura/skill/strength.png) [Strength](../../tensura-reincarnated/abilities/common-skills/strength.md)

## Learnable skills

This race can learn these skills through training.

- ![](../../assets/icons/tensura/skill/hero_haki.png) [Hero Haki](../../tensura-reincarnated/abilities/extra-skills/hero-haki.md)
- ![](../../assets/icons/tensura/skill/multilayer_barrier.png) [Multilayer Barrier](../../tensura-reincarnated/abilities/extra-skills/multilayer-barrier.md)
- ![](../../assets/icons/tensura/skill/ultraspeed_regeneration.png) [Ultraspeed Regeneration](../../tensura-reincarnated/abilities/extra-skills/ultraspeed-regeneration.md)
- ![](../../assets/icons/tensura/skill/sacred_haki.png) [Sacred Haki](../../tensura-reincarnated/abilities/extra-skills/sacred-haki.md)
- ![](../../assets/icons/tensura/skill/thought_acceleration.png) [Thought Acceleration](../../tensura-reincarnated/abilities/extra-skills/thought-acceleration.md)
- ![](../../assets/icons/tensura/skill/magic_sense.png) [Magic Sense](../../tensura-reincarnated/abilities/extra-skills/magic-sense.md)
- ![](../../assets/icons/tensura/skill/haki.png) [Haki](../../tensura-reincarnated/abilities/extra-skills/haki.md)
- ![](../../assets/icons/tensura/skill/ultra_instinct.png) [Ultra-Instinct](../../tensura-reincarnated/abilities/extra-skills/ultra-instinct.md)
- ![](../../assets/icons/tensura/skill/steel_strength.png) [Steel Strength](../../tensura-reincarnated/abilities/extra-skills/steel-strength.md)
- ![](../../assets/icons/tensura/skill/strengthen_body.png) [Strengthen Body](../../tensura-reincarnated/abilities/extra-skills/strengthen-body.md)
- ![](../../assets/icons/tensura/skill/physical_attack_resistance.png) [Physical Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/physical-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/danger_sense.png) [Danger Sense](../../tensura-reincarnated/abilities/extra-skills/danger-sense.md)
- ![](../../assets/icons/ascension/skill/intimidating_roar.png) [Intimidating Roar](../abilities/extra-skills/intimidating-roar.md)

## Traits

- Divine

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0.17 | add |
| Scale | 0.09 | add |
| Scale | 0.01 | add |
| Scale | -0.07 | add |
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

## Tags

`tensura:races/divine`
