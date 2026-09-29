# Frostcoil Sea Serpent

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:frostcoil_sea_serpent` |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 200,000 - 200,000 |
| **Magicule** | 150,000 - 150,000 |
| **Health bonus** | 340 |
| **Spiritual health bonus** | 1,360 |
| **Attack damage bonus** | 7 |
| **Movement speed bonus** | 0.03 |
| **EP to evolve into** | 200,000 |

</div>

> A sea dragon race that lives in the coldest depths of the Ocean's tundra's, using its enhanced ears to find its prey, and its speed to catch them.

## Evolution

- **Evolves from:** [Greater Glacier Wyrm](greater-glacier-wyrm.md), [Attuned Wyrm](attuned-wyrm.md), [Lesser Glacier Wyrm](lesser-glacier-wyrm.md), [Lesser Pyre Wyrm](lesser-pyre-wyrm.md), [Greater Pyre Wyrm](greater-pyre-wyrm.md)
- **Evolves into:** [Frostwrought Leviathan](frostwrought-leviathan.md)
- **Default evolution:** [Frostwrought Leviathan](frostwrought-leviathan.md)
- **On awakening (True Demon Lord / True Hero):** [Frostwrought Leviathan](frostwrought-leviathan.md)

### Requirements to evolve into Frostcoil Sea Serpent

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 200,000 | 33.4% |
| Master [Water Manipulation](../../tensura-reincarnated/abilities/extra-skills/water-manipulation.md) | 33.3% |
| Master [Cryogenic Cessation](../abilities/extra-skills/cryogenic-cessation.md) | 33.3% |

### Evolution tree

```mermaid
flowchart LR
  r0["Attuned Wyrm"]
  r1["Frostcoil Sea Serpent"]
  r2["Frostwrought Leviathan"]
  r3["Greater Glacier Wyrm"]
  r4["Greater Pyre Wyrm"]
  r5["Lesser Glacier Wyrm"]
  r6["Lesser Pyre Wyrm"]
  r7["Rimeblight Hydra"]
  r8["Rimefang Drake"]
  r9["Scorchtail Salamander"]
  r10["Scorchtalon Wyvern"]
  r11["Sundeity Loong"]
  r12["Sunfire Lindwurm"]
  r0 --> r1
  r0 --> r5
  r0 --> r6
  r1 --> r2
  r3 --> r1
  r3 --> r8
  r4 --> r1
  r4 --> r9
  r4 --> r12
  r5 --> r1
  r5 --> r3
  r6 --> r1
  r6 --> r4
  r8 --> r7
  r9 --> r10
  r12 --> r11
```

## Traits

- Spiritual lifeform

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 1 | add |
| Max Health | 340 | add |
| Max Spiritual Health | 1,360 | add |
| Attack Damage | 7 | add |
| Attack Speed | 1 | add |
| Knockback Resistance | 0.06 | add |
| Movement Speed | 0.03 | add |
| Swim Speed Multiplier | 0.03 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/wyrm_config.toml`](../configs/config-mysticism-race-wyrm-config.md).

| Option | Default | Description |
|---|---|---|
| `FrostcoilSeaSerpent.minAura` | 200,000 | Minimal aura. |
| `FrostcoilSeaSerpent.maxAura` | 200,000 | Maximum aura. |
| `FrostcoilSeaSerpent.minMagicule` | 150,000 | Minimal magicule. |
| `FrostcoilSeaSerpent.maxMagicule` | 150,000 | Maximum magicule. |
| `FrostcoilSeaSerpent.size` | 1 | Bonus Size. |
| `FrostcoilSeaSerpent.maxHealth` | 340 | Bonus Max Health. |
| `FrostcoilSeaSerpent.maxSpiritualHealth` | 1,360 | Bonus Max Spiritual Health. |
| `FrostcoilSeaSerpent.attack` | 7 | Bonus Attack Damage. |
| `FrostcoilSeaSerpent.attackSpeed` | 1 | Bonus Attack Speed. |
| `FrostcoilSeaSerpent.knockbackResistance` | 0.06 | Bonus Knockback Resistance. |
| `FrostcoilSeaSerpent.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `FrostcoilSeaSerpent.swimSpeed` | 0.03 | Bonus Swimming Speed Multiplier. |
| `FrostcoilSeaSerpent.epRequirement` | 200,000 | EP requirement to evolve into Frostcoil Sea Serpent. |
| `FrostcoilSeaSerpent.abilityRequirement` | "tensura:water_manipulation" | The first ability needed to evolve into Frostcoil Sea Serpent. |
| `FrostcoilSeaSerpent.abilityMasteryRequirement` | true | Does the ffirst ability need to be mastered? (true/false) |
| `FrostcoilSeaSerpent.ability2Requirement` | "mysticism:cryogenic_cessation" | The second ability needed to evolve into Frostcoil Sea Serpent. |
| `FrostcoilSeaSerpent.ability2MasteryRequirement` | true | Does the second ability need to be mastered? (true/false) |
| `FrostcoilSeaSerpent.intrinsicSkills` | "tensura:cold_resistance", "mysticism:cryogenic_cessation", "tensura:dragon_ear", "tensura:dragon_skin", "tensura:ultrasonic_waves", "tensura:hydraulic_propulsion" | The list of intrinsic skills that the race gets. |
| `GreaterGlacierWyrm.minAura` | 8,000 | Minimal aura. |
| `GreaterGlacierWyrm.maxAura` | 8,000 | Maximum aura. |
| `GreaterGlacierWyrm.minMagicule` | 10,000 | Minimal magicule. |
| `GreaterGlacierWyrm.maxMagicule` | 10,000 | Maximum magicule. |
| `GreaterGlacierWyrm.size` | 0.8 | Bonus Size. |
| `GreaterGlacierWyrm.maxHealth` | 180 | Bonus Max Health. |
| `GreaterGlacierWyrm.maxSpiritualHealth` | 660 | Bonus Max Spiritual Health. |
| `GreaterGlacierWyrm.attack` | 3 | Bonus Attack Damage. |
| `GreaterGlacierWyrm.attackSpeed` | 2 | Bonus Attack Speed. |
| `GreaterGlacierWyrm.knockbackResistance` | 0.05 | Bonus Knockback Resistance. |
| `GreaterGlacierWyrm.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `GreaterGlacierWyrm.swimSpeed` | 0.02 | Bonus Swimming Speed Multiplier. |
| `GreaterGlacierWyrm.iceEssenceAmount` | 10 | Amount of Ice Essence needed eaten to evolve into a Greater Glacier Wyrm. |
| `GreaterGlacierWyrm.epRequirement` | 30,000 | EP requirement to evolve into Greater Glacier Wyrm. |
| `GreaterGlacierWyrm.intrinsicSkills` | "tensura:cold_resistance", "mysticism:cryogenic_cessation" | The list of intrinsic skills that the race gets. |
| `LesserGlacierWyrm.minAura` | 1,000 | Minimal aura. |
| `LesserGlacierWyrm.maxAura` | 1,500 | Maximum aura. |
| `LesserGlacierWyrm.minMagicule` | 2,000 | Minimal magicule. |
| `LesserGlacierWyrm.maxMagicule` | 2,500 | Maximum magicule. |
| `LesserGlacierWyrm.size` | 0.5 | Bonus Size. |
| `LesserGlacierWyrm.maxHealth` | 40 | Bonus Max Health. |
| `LesserGlacierWyrm.maxSpiritualHealth` | 160 | Bonus Max Spiritual Health. |
| `LesserGlacierWyrm.attack` | 1 | Bonus Attack Damage. |
| `LesserGlacierWyrm.attackSpeed` | 1 | Bonus Attack Speed. |
| `LesserGlacierWyrm.knockbackResistance` | 0.04 | Bonus Knockback Resistance. |
| `LesserGlacierWyrm.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `LesserGlacierWyrm.swimSpeed` | 0.03 | Bonus Swimming Speed Multiplier. |
| `LesserGlacierWyrm.iceEssenceAmount` | 1 | Amount of Ice Essence needed eaten to evolve into a Lesser Glacier Wyrm. |
| `LesserGlacierWyrm.intrinsicSkills` | "tensura:cold_resistance" | The list of intrinsic skills that the race gets. |
| `AttunedWyrm.minAura` | 500 | Minimal aura. |
| `AttunedWyrm.maxAura` | 1,000 | Maximum aura. |
| `AttunedWyrm.minMagicule` | 1,500 | Minimal magicule. |
| `AttunedWyrm.maxMagicule` | 2,000 | Maximum magicule. |
| `AttunedWyrm.size` | 0.3 | Bonus Size. |
| `AttunedWyrm.maxHealth` | 0 | Bonus Max Health. |
| `AttunedWyrm.maxSpiritualHealth` | 0 | Bonus Max Spiritual Health. |
| `AttunedWyrm.attack` | 1 | Bonus Attack Damage. |
| `AttunedWyrm.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `AttunedWyrm.knockbackResistance` | 1 | Bonus Knockback Resistance. |
| `AttunedWyrm.movementSpeed` | 0 | Bonus Movement Speed. |
| `AttunedWyrm.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `AttunedWyrm.intrinsicSkills` | [] (empty) | The list of intrinsic skills that the race gets. |

## Tags

`tensura:races/spiritual`
