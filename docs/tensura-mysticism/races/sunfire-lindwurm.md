# Sunfire Lindwurm

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:sunfire_lindwurm` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 180,000 - 180,000 |
| **Magicule** | 140,000 - 140,000 |
| **Health bonus** | 440 |
| **Spiritual health bonus** | 1,760 |
| **Attack damage bonus** | 6 |
| **Movement speed bonus** | 0.03 |
| **EP to evolve into** | 180,000 |

</div>

> A wingless spiritual dragon race that crawls across the ground, it helps those that it can, while also hunting for its own prey, it shows mercy, making sure to end the lives of prey quick and swiftly using rays of light.

## Evolution

- **Evolves from:** [Greater Pyre Wyrm](greater-pyre-wyrm.md)
- **Evolves into:** [Sundeity Loong](sundeity-loong.md)
- **Default evolution:** [Sundeity Loong](sundeity-loong.md)
- **On awakening (True Demon Lord / True Hero):** [Sundeity Loong](sundeity-loong.md)

### Requirements to evolve into Sunfire Lindwurm

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 180,000 | 33.4% |
| Master [Light Manipulation](../abilities/extra-skills/light-manipulation.md) | 33.3% |
| Master [Profaned Prominence](../abilities/extra-skills/profaned-prominence.md) | 33.3% |

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
| Max Health | 440 | add |
| Max Spiritual Health | 1,760 | add |
| Attack Damage | 6 | add |
| Attack Speed | 5 | add |
| Knockback Resistance | 0.09 | add |
| Movement Speed | 0.03 | add |
| Swim Speed Multiplier | 0.03 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/wyrm_config.toml`](../configs/config-mysticism-race-wyrm-config.md).

| Option | Default | Description |
|---|---|---|
| `SunfireLindwurm.minAura` | 180,000 | Minimal aura. |
| `SunfireLindwurm.maxAura` | 180,000 | Maximum aura. |
| `SunfireLindwurm.minMagicule` | 140,000 | Minimal magicule. |
| `SunfireLindwurm.maxMagicule` | 140,000 | Maximum magicule. |
| `SunfireLindwurm.size` | 1 | Bonus Size. |
| `SunfireLindwurm.maxHealth` | 440 | Bonus Max Health. |
| `SunfireLindwurm.maxSpiritualHealth` | 1,760 | Bonus Max Spiritual Health. |
| `SunfireLindwurm.attack` | 6 | Bonus Attack Damage. |
| `SunfireLindwurm.attackSpeed` | 5 | Bonus Attack Speed. |
| `SunfireLindwurm.knockbackResistance` | 0.09 | Bonus Knockback Resistance. |
| `SunfireLindwurm.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `SunfireLindwurm.swimSpeed` | 0.03 | Bonus Swimming Speed Multiplier. |
| `SunfireLindwurm.epRequirement` | 180,000 | EP requirement to evolve into Sunfire Lindwurm. |
| `SunfireLindwurm.abilityRequirement` | "mysticism:light_manipulation" | The first ability needed to evolve into Sunfire Lindwurm. |
| `SunfireLindwurm.abilityMasteryRequirement` | true | Does the ffirst ability need to be mastered? (true/false) |
| `SunfireLindwurm.ability2Requirement` | "mysticism:profaned_prominence" | The second ability needed to evolve into Sunfire Lindwurm. |
| `SunfireLindwurm.ability2MasteryRequirement` | true | Does the second ability need to be mastered? (true/false) |
| `SunfireLindwurm.intrinsicSkills` | "tensura:flame_attack_resistance", "mysticism:profaned_prominence", "tensura:dragon_ear", "tensura:dragon_skin", "tensura:flame_transform" | The list of intrinsic skills that the race gets. |
| `GreaterPyreWyrm.minAura` | 5,000 | Minimal aura. |
| `GreaterPyreWyrm.maxAura` | 8,000 | Maximum aura. |
| `GreaterPyreWyrm.minMagicule` | 5,000 | Minimal magicule. |
| `GreaterPyreWyrm.maxMagicule` | 10,000 | Maximum magicule. |
| `GreaterPyreWyrm.size` | 0.8 | Bonus Size. |
| `GreaterPyreWyrm.maxHealth` | 180 | Bonus Max Health. |
| `GreaterPyreWyrm.maxSpiritualHealth` | 720 | Bonus Max Spiritual Health. |
| `GreaterPyreWyrm.attack` | 1.8 | Bonus Attack Damage. |
| `GreaterPyreWyrm.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `GreaterPyreWyrm.knockbackResistance` | 0.08 | Bonus Knockback Resistance. |
| `GreaterPyreWyrm.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `GreaterPyreWyrm.swimSpeed` | 0.03 | Bonus Swimming Speed Multiplier. |
| `GreaterPyreWyrm.flameEssenceAmount` | 10 | Amount of Flame Essence needed eaten to evolve into a Greater Pyre Wyrm. |
| `GreaterPyreWyrm.epRequirement` | 30,000 | EP requirement to evolve into Greater Pyre Wyrm. |
| `GreaterPyreWyrm.intrinsicSkills` | "tensura:flame_attack_resistance", "mysticism:profaned_prominence" | The list of intrinsic skills that the race gets. |
| `LesserPyreWyrm.minAura` | 1,500 | Minimal aura. |
| `LesserPyreWyrm.maxAura` | 2,000 | Maximum aura. |
| `LesserPyreWyrm.minMagicule` | 2,000 | Minimal magicule. |
| `LesserPyreWyrm.maxMagicule` | 2,500 | Maximum magicule. |
| `LesserPyreWyrm.size` | 0.5 | Bonus Size. |
| `LesserPyreWyrm.maxHealth` | 30 | Bonus Max Health. |
| `LesserPyreWyrm.maxSpiritualHealth` | 120 | Bonus Max Spiritual Health. |
| `LesserPyreWyrm.attack` | 1.5 | Bonus Attack Damage. |
| `LesserPyreWyrm.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `LesserPyreWyrm.knockbackResistance` | 0.04 | Bonus Knockback Resistance. |
| `LesserPyreWyrm.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `LesserPyreWyrm.swimSpeed` | 0.03 | Bonus Swimming Speed Multiplier. |
| `LesserPyreWyrm.flameEssenceAmount` | 1 | Amount of Flame Essence needed eaten to evolve into a Lesser Pyre Wyrm. |
| `LesserPyreWyrm.intrinsicSkills` | "tensura:flame_attack_resistance" | The list of intrinsic skills that the race gets. |
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
