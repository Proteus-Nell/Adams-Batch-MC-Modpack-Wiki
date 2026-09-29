# Enlightened Ogre

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:enlightened_ogre` |
| **Difficulty** | Easy |
| **Alignment** | Default |
| **Aura** | 100,000 - 100,000 |
| **Magicule** | 100,000 - 100,000 |
| **Health bonus** | 100 |
| **Spiritual health bonus** | 340 |
| **Attack damage bonus** | 4 |
| **Movement speed bonus** | 0.02 |
| **EP to evolve into** | 100,000 |

</div>

> Ogre that has "evolved the correct way" and became a Demi-Spiritual Lifeform.

## Evolution

- **Evolves from:** [Ogre](ogre.md)
- **Evolves into:** [Mystic Oni](mystic-oni.md), [Wicked Oni](wicked-oni.md)
- **Default evolution:** [Mystic Oni](mystic-oni.md)
- **On awakening (True Demon Lord / True Hero):** [Spirit Oni](spirit-oni.md)
- **During the Harvest Festival:** [Mystic Oni](mystic-oni.md)

### Requirements to evolve into Enlightened Ogre

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 100,000 | 100% |

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

- ![](../../assets/icons/tensura/skill/steel_strength.png) [Steel Strength](../abilities/extra-skills/steel-strength.md)
- ![](../../assets/icons/tensura/skill/strength.png) [Strength](../abilities/common-skills/strength.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 100 | add |
| Max Spiritual Health | 340 | add |
| Attack Damage | 4 | add |
| Attack Speed | 0.3 | add |
| Knockback Resistance | 0.2 | add |
| Movement Speed | 0.02 | add |
| Swim Speed Multiplier | 0.2 | add |

## Stats (config defaults)

Set in [`config/tensura/race/ogre_config.toml`](../configs/config-tensura-race-ogre-config.md).

| Option | Default | Description |
|---|---|---|
| `EnlightenedOgre.epRequirement` | 100,000 | EP requirement to evolve into Enlightened Ogre. |
| `EnlightenedOgre.minAura` | 100,000 | Minimal aura. |
| `EnlightenedOgre.maxAura` | 100,000 | Maximum aura. |
| `EnlightenedOgre.minMagicule` | 100,000 | Minimal magicule. |
| `EnlightenedOgre.maxMagicule` | 100,000 | Maximum magicule. |
| `EnlightenedOgre.size` | 0 | Bonus Size. |
| `EnlightenedOgre.maxHealth` | 100 | Bonus Max Health. |
| `EnlightenedOgre.maxSpiritualHealth` | 340 | Bonus Max Spiritual Health. |
| `EnlightenedOgre.attack` | 4 | Bonus Attack Damage. |
| `EnlightenedOgre.attackSpeed` | 0.3 | Bonus Attack Speed. |
| `EnlightenedOgre.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `EnlightenedOgre.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `EnlightenedOgre.swimSpeed` | 0.2 | Bonus Swimming Speed Multiplier. |
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
