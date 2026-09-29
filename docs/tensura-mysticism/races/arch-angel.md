# Arch Angel

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:arch_angel` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Easy |
| **Alignment** | Holy |
| **Aura** | 100,000 - 105,000 |
| **Magicule** | 40,000 - 45,000 |
| **Health bonus** | 100 |
| **Spiritual health bonus** | 580 |
| **Attack damage bonus** | 2 |
| **Movement speed bonus** | 0.01 |
| **EP to evolve into** | 140,000 |

</div>

> Only few Angels make it to this point because of their lack of ego.

## Evolution

- **Evolves from:** [Greater Angel](greater-angel.md)
- **Evolves into:** [Cherub](cherub.md), [Tengu](tengu.md)
- **Default evolution:** [Cherub](cherub.md)
- **On awakening (True Demon Lord / True Hero):** [Cherub](cherub.md)
- **During the Harvest Festival:** [Cherub](cherub.md)

### Requirements to evolve into Arch Angel

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 140,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Arch Angel"]
  r1["Cherub"]
  r2["Divine Tengu"]
  r3["Greater Angel"]
  r4["Lesser Angel"]
  r5["Seraph"]
  r6["Tengu"]
  r7["Tengu Saint"]
  r0 --> r1
  r0 --> r6
  r1 --> r2
  r1 --> r5
  r3 --> r0
  r3 --> r1
  r3 --> r6
  r4 --> r1
  r4 --> r3
  r6 --> r7
  r7 --> r2
```

## Traits

- Has creative-style flight
- Spawns as a spiritual lifeform
- Spiritual lifeform

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 100 | add |
| Max Spiritual Health | 580 | add |
| Attack Damage | 2 | add |
| Attack Speed | 0.2 | add |
| Knockback Resistance | 0.4 | add |
| Movement Speed | 0.01 | add |
| Swim Speed Multiplier | 0.1 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/angel_config.toml`](../configs/config-mysticism-race-angel-config.md).

| Option | Default | Description |
|---|---|---|
| `ArchAngel.epRequirement` | 140,000 | EP requirement to evolve into an Arch Angel. |
| `ArchAngel.minAura` | 100,000 | Minimal aura. |
| `ArchAngel.maxAura` | 105,000 | Maximum aura. |
| `ArchAngel.minMagicule` | 40,000 | Minimal magicule. |
| `ArchAngel.maxMagicule` | 45,000 | Maximum magicule. |
| `ArchAngel.size` | 0 | Bonus Size. |
| `ArchAngel.maxHealth` | 100 | Bonus Max Health. |
| `ArchAngel.maxSpiritualHealth` | 580 | Bonus Max Spiritual Health. |
| `ArchAngel.attack` | 2 | Bonus Attack Damage. |
| `ArchAngel.attackSpeed` | 0.2 | Bonus Attack Speed. |
| `ArchAngel.knockbackResistance` | 0.4 | Bonus Knockback Resistance. |
| `ArchAngel.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `ArchAngel.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
| `ArchAngel.intrinsicSkills` | "tensura:magic_resistance", "tensura:possession", "mysticism:light_manipulation", "tensura:physical_attack_resistance" | The list of intrinsic skills that the race gets. |
| `GreaterAngel.epRequirement` | 20,000 | EP requirement to evolve into a Greater Angel. |
| `GreaterAngel.minAura` | 35,000 | Minimal aura. |
| `GreaterAngel.maxAura` | 45,000 | Maximum aura. |
| `GreaterAngel.minMagicule` | 15,000 | Minimal magicule. |
| `GreaterAngel.maxMagicule` | 25,000 | Maximum magicule. |
| `GreaterAngel.size` | 0 | Bonus Size. |
| `GreaterAngel.maxHealth` | 60 | Bonus Max Health. |
| `GreaterAngel.maxSpiritualHealth` | 200 | Bonus Max Spiritual Health. |
| `GreaterAngel.attack` | 1 | Bonus Attack Damage. |
| `GreaterAngel.attackSpeed` | 0 | Bonus Attack Speed. |
| `GreaterAngel.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `GreaterAngel.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `GreaterAngel.swimSpeed` | 0.2 | Bonus Swimming Speed Multiplier. |
| `GreaterAngel.intrinsicSkills` | "tensura:magic_resistance", "tensura:possession", "mysticism:light_manipulation" | The list of intrinsic skills that the race gets. |
| `LesserAngel.minAura` | 5,500 | Minimal aura. |
| `LesserAngel.maxAura` | 6,500 | Maximum aura. |
| `LesserAngel.minMagicule` | 1,500 | Minimal magicule. |
| `LesserAngel.maxMagicule` | 3,500 | Maximum magicule. |
| `LesserAngel.size` | 0 | Bonus Size. |
| `LesserAngel.maxHealth` | 20 | Bonus Max Health. |
| `LesserAngel.maxSpiritualHealth` | 90 | Bonus Max Spiritual Health. |
| `LesserAngel.attack` | 0.4 | Bonus Attack Damage. |
| `LesserAngel.attackSpeed` | 0 | Bonus Attack Speed. |
| `LesserAngel.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `LesserAngel.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `LesserAngel.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `LesserAngel.intrinsicSkills` | "tensura:magic_resistance", "tensura:possession", "mysticism:light_manipulation" | The list of intrinsic skills that the race gets. |

## Tags

`tensura:races/has_creative_flight`, `tensura:races/spawn_as_spiritual`, `tensura:races/spiritual`
