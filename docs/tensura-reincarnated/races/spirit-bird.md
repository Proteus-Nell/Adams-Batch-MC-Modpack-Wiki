# Spirit Bird

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:spirit_bird` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 400,000 - 400,000 |
| **Magicule** | 400,000 - 400,000 |
| **Health bonus** | 580 |
| **Spiritual health bonus** | 4,540 |
| **Attack damage bonus** | 2 |
| **Movement speed bonus** | 0.05 |
| **EP to evolve into** | 800,000 |

</div>

> Harpy that has "evolved the correct way" and became a Spiritual Lifeform.

## Evolution

- **Evolves from:** [Harpy Queen](harpy-queen.md), [Harpy](harpy.md), [Angel](../../ascension/races/angel.md), [Archangel](../../ascension/races/archangel.md)
- **Evolves into:** [Divine Bird](divine-bird.md)
- **Default evolution:** [Divine Bird](divine-bird.md)
- **On awakening (True Demon Lord / True Hero):** [Divine Bird](divine-bird.md)

### Requirements to evolve into Spirit Bird

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 800,000 | 100% |

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

- ![](../../assets/icons/tensura/skill/magic_jamming.png) [Magic Jamming](../abilities/extra-skills/magic-jamming.md)

## Traits

- Can glide
- Spiritual lifeform

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Safe Fall Distance | 7 | add |
| Safe Fall Distance | 5 | add |
| Safe Fall Distance | 3 | add |
| Scale | 0 | add |
| Max Health | 580 | add |
| Max Spiritual Health | 4,540 | add |
| Attack Damage | 2 | add |
| Attack Speed | 0.5 | add |
| Knockback Resistance | 0.2 | add |
| Movement Speed | 0.05 | add |
| Swim Speed Multiplier | 0.5 | add |

## Stats (config defaults)

Set in [`config/tensura/race/harpy_config.toml`](../configs/config-tensura-race-harpy-config.md).

| Option | Default | Description |
|---|---|---|
| `SpiritBird.safeFalling` | 7 | Bonus Safe Falling distance. |
| `SpiritBird.epRequirement` | 800,000 | EP requirement to evolve into Spirit Bird. |
| `SpiritBird.minAura` | 400,000 | Minimal aura. |
| `SpiritBird.maxAura` | 400,000 | Maximum aura. |
| `SpiritBird.minMagicule` | 400,000 | Minimal magicule. |
| `SpiritBird.maxMagicule` | 400,000 | Maximum magicule. |
| `SpiritBird.size` | 0 | Bonus Size. |
| `SpiritBird.maxHealth` | 580 | Bonus Max Health. |
| `SpiritBird.maxSpiritualHealth` | 4,540 | Bonus Max Spiritual Health. |
| `SpiritBird.attack` | 2 | Bonus Attack Damage. |
| `SpiritBird.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `SpiritBird.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `SpiritBird.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `SpiritBird.swimSpeed` | 0.5 | Bonus Swimming Speed Multiplier. |
| `SpiritBird.safeFalling` | 7 | Bonus Safe Falling distance. |
| `SpiritBird.flightBoost` | 0.95 | Flight Upward Boost Power. |
| `SpiritBird.flightCooldown` | 3 | Flight Boost Cooldown. |
| `HarpyQueen.safeFalling` | 5 | Bonus Safe Falling distance. |
| `HarpyQueen.epRequirement` | 200,000 | EP requirement to evolve into Harpy Queen. |
| `HarpyQueen.minAura` | 150,000 | Minimal aura. |
| `HarpyQueen.maxAura` | 150,000 | Maximum aura. |
| `HarpyQueen.minMagicule` | 150,000 | Minimal magicule. |
| `HarpyQueen.maxMagicule` | 150,000 | Maximum magicule. |
| `HarpyQueen.size` | 0 | Bonus Size. |
| `HarpyQueen.maxHealth` | 120 | Bonus Max Health. |
| `HarpyQueen.maxSpiritualHealth` | 290 | Bonus Max Spiritual Health. |
| `HarpyQueen.attack` | 1 | Bonus Attack Damage. |
| `HarpyQueen.attackSpeed` | 0.2 | Bonus Attack Speed. |
| `HarpyQueen.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `HarpyQueen.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `HarpyQueen.swimSpeed` | 0.3 | Bonus Swimming Speed Multiplier. |
| `HarpyQueen.safeFalling` | 5 | Bonus Safe Falling distance. |
| `HarpyQueen.flightBoost` | 0.85 | Flight Upward Boost Power. |
| `HarpyQueen.flightCooldown` | 3 | Flight Boost Cooldown. |
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

`tensura:races/can_glide`, `tensura:races/spiritual`
