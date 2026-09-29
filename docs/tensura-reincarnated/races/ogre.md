# Ogre

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:ogre` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Easy |
| **Alignment** | Default |
| **Aura** | 1,500 - 2,500 |
| **Magicule** | 300 - 600 |
| **Health bonus** | 6 |
| **Spiritual health bonus** | 15 |
| **Attack damage bonus** | 1 |
| **Movement speed bonus** | 0.01 |

</div>

> A sprite race descended from fire elementals. They possess immense physical capabilities and a strong Japanese lineage.

## Evolution

- **Evolves from:** [Hobgoblin](hobgoblin.md)
- **Evolves into:** [Enlightened Ogre](enlightened-ogre.md), [Kijin](kijin.md)
- **Default evolution:** [Enlightened Ogre](enlightened-ogre.md)
- **On awakening (True Demon Lord / True Hero):** [Spirit Oni](spirit-oni.md)
- **During the Harvest Festival:** [Kijin](kijin.md)

### Requirements to evolve into Ogre

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Battle [Elemental Colossus](../mobs/elemental-colossus.md)(-s) | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Death Oni"]
  r1["Divine Fighter"]
  r2["Divine Oni"]
  r3["Enlightened Hobgoblin"]
  r4["Enlightened Ogre"]
  r5["Goblin"]
  r6["Hobgoblin"]
  r7["Hobgoblin Saint"]
  r8["Kijin"]
  r9["Mystic Oni"]
  r10["Ogre"]
  r11["Spirit Oni"]
  r12["Wicked Oni"]
  r0 --> r1
  r0 --> r2
  r3 --> r7
  r4 --> r9
  r4 --> r11
  r4 --> r12
  r5 --> r6
  r5 --> r7
  r6 --> r3
  r6 --> r7
  r6 --> r10
  r7 --> r2
  r8 --> r9
  r8 --> r11
  r8 --> r12
  r9 --> r11
  r10 --> r4
  r10 --> r8
  r10 --> r11
  r11 --> r2
  r12 --> r0
  r12 --> r11
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/strength.png) [Strength](../abilities/common-skills/strength.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 6 | add |
| Max Spiritual Health | 15 | add |
| Attack Damage | 1 | add |
| Attack Speed | 0.1 | add |
| Knockback Resistance | 0.1 | add |
| Movement Speed | 0.01 | add |
| Swim Speed Multiplier | 0.1 | add |

## Stats (config defaults)

Set in [`config/tensura/race/ogre_config.toml`](../configs/config-tensura-race-ogre-config.md).

| Option | Default | Description |
|---|---|---|
| `Ogre.minAura` | 1,500 | Minimal aura. |
| `Ogre.maxAura` | 2,500 | Maximum aura. |
| `Ogre.minMagicule` | 300 | Minimal magicule. |
| `Ogre.maxMagicule` | 600 | Maximum magicule. |
| `Ogre.size` | 0 | Bonus Size. |
| `Ogre.maxHealth` | 6 | Bonus Max Health. |
| `Ogre.maxSpiritualHealth` | 15 | Bonus Max Spiritual Health. |
| `Ogre.attack` | 1 | Bonus Attack Damage. |
| `Ogre.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `Ogre.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `Ogre.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `Ogre.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
