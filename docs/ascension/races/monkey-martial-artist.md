# Monkey Martial Artist

<small>[Ascension](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `ascension:monkey_martial_artist` |
| **Difficulty** | Intermediate |
| **Alignment** | Default |
| **Aura** | 300 - 300 |
| **Magicule** | 700 - 700 |
| **Health bonus** | -8 |
| **Spiritual health bonus** | -16 |
| **Attack damage bonus** | -0.5 |
| **Movement speed bonus** | -0.02 |

</div>

> A master of unarmed combat, body forged into a weapon.

## Evolution

- **Evolves from:** [Monkey Warrior](monkey-warrior.md)
- **Evolves into:** [Monkey King](monkey-king.md)
- **Default evolution:** [Monkey King](monkey-king.md)
- **On awakening (True Demon Lord / True Hero):** [Monkey King](monkey-king.md)
- **During the Harvest Festival:** [Monkey King](monkey-king.md)

### Requirements to evolve into Monkey Martial Artist

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 100,000 | 100% |

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

- ![](../../assets/icons/tensura/skill/body_armor.png) [Body Armor](../../tensura-reincarnated/abilities/intrinsic-skills/body-armor.md)
- ![](../../assets/icons/tensura/skill/strength.png) [Strength](../../tensura-reincarnated/abilities/common-skills/strength.md)

## Learnable skills

This race can learn these skills through training.

- ![](../../assets/icons/tensura/skill/haki.png) [Haki](../../tensura-reincarnated/abilities/extra-skills/haki.md)
- ![](../../assets/icons/tensura/skill/ultra_instinct.png) [Ultra-Instinct](../../tensura-reincarnated/abilities/extra-skills/ultra-instinct.md)
- ![](../../assets/icons/tensura/skill/steel_strength.png) [Steel Strength](../../tensura-reincarnated/abilities/extra-skills/steel-strength.md)
- ![](../../assets/icons/tensura/skill/strengthen_body.png) [Strengthen Body](../../tensura-reincarnated/abilities/extra-skills/strengthen-body.md)
- ![](../../assets/icons/tensura/skill/physical_attack_resistance.png) [Physical Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/physical-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/danger_sense.png) [Danger Sense](../../tensura-reincarnated/abilities/extra-skills/danger-sense.md)
- ![](../../assets/icons/ascension/skill/intimidating_roar.png) [Intimidating Roar](../abilities/extra-skills/intimidating-roar.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
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
