# Enlightened Hobgoblin

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:enlightened_hobgoblin` |
| **Difficulty** | Easy |
| **Alignment** | Default |
| **Aura** | 100,000 - 100,000 |
| **Magicule** | 100,000 - 100,000 |
| **Health bonus** | 90 |
| **Spiritual health bonus** | 300 |
| **Attack damage bonus** | 1 |
| **Movement speed bonus** | 0.01 |
| **EP to evolve into** | 100,000 |

</div>

> Hobgoblin that has "evolved the correct way" and became a Demi-Spiritual Lifeform.

## Evolution

- **Evolves from:** [Hobgoblin](hobgoblin.md)
- **Evolves into:** [Hobgoblin Saint](hobgoblin-saint.md)
- **Default evolution:** [Hobgoblin Saint](hobgoblin-saint.md)
- **On awakening (True Demon Lord / True Hero):** [Hobgoblin Saint](hobgoblin-saint.md)

### Requirements to evolve into Enlightened Hobgoblin

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

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 90 | add |
| Max Spiritual Health | 300 | add |
| Attack Damage | 1 | add |
| Attack Speed | 0.3 | add |
| Knockback Resistance | 0.05 | add |
| Movement Speed | 0.01 | add |
| Swim Speed Multiplier | 0.1 | add |

## Stats (config defaults)

Set in [`config/tensura/race/goblin_config.toml`](../configs/config-tensura-race-goblin-config.md).

| Option | Default | Description |
|---|---|---|
| `EnlightenedHobgoblin.epRequirement` | 100,000 | EP requirement to evolve into Enlightened Hobgoblin. |
| `EnlightenedHobgoblin.minAura` | 100,000 | Minimal aura. |
| `EnlightenedHobgoblin.maxAura` | 100,000 | Maximum aura. |
| `EnlightenedHobgoblin.minMagicule` | 100,000 | Minimal magicule. |
| `EnlightenedHobgoblin.maxMagicule` | 100,000 | Maximum magicule. |
| `EnlightenedHobgoblin.size` | 0 | Bonus Size. |
| `EnlightenedHobgoblin.maxHealth` | 90 | Bonus Max Health. |
| `EnlightenedHobgoblin.maxSpiritualHealth` | 300 | Bonus Max Spiritual Health. |
| `EnlightenedHobgoblin.attack` | 1 | Bonus Attack Damage. |
| `EnlightenedHobgoblin.attackSpeed` | 0.3 | Bonus Attack Speed. |
| `EnlightenedHobgoblin.knockbackResistance` | 0.05 | Bonus Knockback Resistance. |
| `EnlightenedHobgoblin.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `EnlightenedHobgoblin.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
| `Hobgoblin.epRequirement` | 2,000 | EP requirement to evolve into Hobgoblin. |
| `Hobgoblin.minAura` | 1,400 | Minimal aura. |
| `Hobgoblin.maxAura` | 1,400 | Maximum aura. |
| `Hobgoblin.minMagicule` | 1,400 | Minimal magicule. |
| `Hobgoblin.maxMagicule` | 1,400 | Maximum magicule. |
| `Hobgoblin.size` | 0 | Bonus Size. |
| `Hobgoblin.maxHealth` | 4 | Bonus Max Health. |
| `Hobgoblin.maxSpiritualHealth` | 10 | Bonus Max Spiritual Health. |
| `Hobgoblin.attack` | 0 | Bonus Attack Damage. |
| `Hobgoblin.attackSpeed` | 0 | Bonus Attack Speed. |
| `Hobgoblin.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Hobgoblin.movementSpeed` | 0 | Bonus Movement Speed. |
| `Hobgoblin.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
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
