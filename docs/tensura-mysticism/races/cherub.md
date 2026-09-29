# Cherub

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:cherub` |
| **Difficulty** | Easy |
| **Alignment** | Holy |
| **Aura** | 205,000 - 215,000 |
| **Magicule** | 175,000 - 180,000 |
| **Health bonus** | 620 |
| **Spiritual health bonus** | 3,702 |
| **Attack damage bonus** | 3 |
| **Movement speed bonus** | 0.04 |
| **EP to evolve into** | 140,000 |

</div>

> The second most powerful type of pure Angel known.

## Evolution

- **Evolves from:** [Arch Angel](arch-angel.md), [Lesser Angel](lesser-angel.md), [Greater Angel](greater-angel.md)
- **Evolves into:** [Seraph](seraph.md)
- **Default evolution:** [Seraph](seraph.md)
- **On awakening (True Demon Lord / True Hero):** [Seraph](seraph.md)

### Requirements to evolve into Cherub

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Awaken [True Demon Lord./True Hero.] | 50% |
| Be named | 50% |
| Have a physical body | 50% |

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
- Spiritual lifeform

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 620 | add |
| Max Spiritual Health | 3,702 | add |
| Attack Damage | 3 | add |
| Attack Speed | 0.5 | add |
| Knockback Resistance | 0.6 | add |
| Movement Speed | 0.04 | add |
| Swim Speed Multiplier | 0.4 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/angel_config.toml`](../configs/config-mysticism-race-angel-config.md).

| Option | Default | Description |
|---|---|---|
| `Cherub.minAura` | 205,000 | Minimal aura. |
| `Cherub.maxAura` | 215,000 | Maximum aura. |
| `Cherub.minMagicule` | 175,000 | Minimal magicule. |
| `Cherub.maxMagicule` | 180,000 | Maximum magicule. |
| `Cherub.size` | 0 | Bonus Size. |
| `Cherub.maxHealth` | 620 | Bonus Max Health. |
| `Cherub.maxSpiritualHealth` | 3,702 | Bonus Max Spiritual Health. |
| `Cherub.attack` | 3 | Bonus Attack Damage. |
| `Cherub.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `Cherub.knockbackResistance` | 0.6 | Bonus Knockback Resistance. |
| `Cherub.movementSpeed` | 0.04 | Bonus Movement Speed. |
| `Cherub.swimSpeed` | 0.4 | Bonus Swimming Speed Multiplier. |
| `Cherub.intrinsicSkills` | "tensura:magic_resistance", "tensura:possession", "mysticism:light_manipulation", "tensura:physical_attack_resistance", "tensura:holy_attack_resistance" | The list of intrinsic skills that the race gets. |
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

`tensura:races/has_creative_flight`, `tensura:races/spiritual`
