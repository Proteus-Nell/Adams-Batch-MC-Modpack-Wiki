# Tengu Saint

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:tengu_saint` |
| **Difficulty** | Easy |
| **Alignment** | Holy |
| **Aura** | 800,000 - 900,000 |
| **Magicule** | 800,000 - 900,000 |
| **Health bonus** | 650 |
| **Spiritual health bonus** | 3,800 |
| **Attack damage bonus** | 4 |
| **Movement speed bonus** | 0.04 |
| **EP to evolve into** | 400,000 |

</div>

> The result of a Tengu becoming once more a spiritual being.

## Evolution

- **Evolves from:** [Tengu](tengu.md)
- **Evolves into:** [Divine Tengu](divine-tengu.md)
- **Default evolution:** [Divine Tengu](divine-tengu.md)
- **On awakening (True Demon Lord / True Hero):** [Divine Tengu](divine-tengu.md)

### Requirements to evolve into Tengu Saint

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Kill 4 bosses | 50% |
| Reach Existence Points of 400,000 | 50% |

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
| Max Health | 650 | add |
| Max Spiritual Health | 3,800 | add |
| Attack Damage | 4 | add |
| Attack Speed | 0.8 | add |
| Knockback Resistance | 0.8 | add |
| Movement Speed | 0.04 | add |
| Swim Speed Multiplier | 0.4 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/angel_config.toml`](../configs/config-mysticism-race-angel-config.md).

| Option | Default | Description |
|---|---|---|
| `TenguSaint.epRequirement` | 400,000 | EP requirement to evolve into a Tengu Saint. |
| `TenguSaint.minAura` | 800,000 | Minimal aura. |
| `TenguSaint.maxAura` | 900,000 | Maximum aura. |
| `TenguSaint.minMagicule` | 800,000 | Minimal magicule. |
| `TenguSaint.maxMagicule` | 900,000 | Maximum magicule. |
| `TenguSaint.size` | 0 | Bonus Size. |
| `TenguSaint.maxHealth` | 650 | Bonus Max Health. |
| `TenguSaint.maxSpiritualHealth` | 3,800 | Bonus Max Spiritual Health. |
| `TenguSaint.attack` | 4 | Bonus Attack Damage. |
| `TenguSaint.attackSpeed` | 0.8 | Bonus Attack Speed. |
| `TenguSaint.knockbackResistance` | 0.8 | Bonus Knockback Resistance. |
| `TenguSaint.movementSpeed` | 0.04 | Bonus Movement Speed. |
| `TenguSaint.swimSpeed` | 0.4 | Bonus Swimming Speed Multiplier. |
| `TenguSaint.intrinsicSkills` | "tensura:magic_resistance", "tensura:possession", "mysticism:light_manipulation", "tensura:beast_transformation", "tensura:self_regeneration", "tensura:godwolf_sense", "tensura:holy_attack_resistance" | The list of intrinsic skills that the race gets. |
| `Tengu.minAura` | 100,000 | Minimal aura. |
| `Tengu.maxAura` | 150,000 | Maximum aura. |
| `Tengu.minMagicule` | 100,000 | Minimal magicule. |
| `Tengu.maxMagicule` | 150,000 | Maximum magicule. |
| `Tengu.size` | 0 | Bonus Size. |
| `Tengu.maxHealth` | 130 | Bonus Max Health. |
| `Tengu.maxSpiritualHealth` | 600 | Bonus Max Spiritual Health. |
| `Tengu.attack` | 2.5 | Bonus Attack Damage. |
| `Tengu.attackSpeed` | 0.4 | Bonus Attack Speed. |
| `Tengu.knockbackResistance` | 0.6 | Bonus Knockback Resistance. |
| `Tengu.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `Tengu.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
| `Tengu.intrinsicSkills` | "tensura:magic_resistance", "tensura:possession", "mysticism:light_manipulation", "tensura:beast_transformation", "tensura:self_regeneration", "tensura:godwolf_sense" | The list of intrinsic skills that the race gets. |
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
