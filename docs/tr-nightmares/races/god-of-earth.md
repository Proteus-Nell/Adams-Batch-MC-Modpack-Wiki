# God Of Earth

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:god_of_earth` |
| **Difficulty** | Hard |
| **Alignment** | Majin |
| **Aura** | 375,000 - 750,000 |
| **Magicule** | 625,000 - 1,250,000 |
| **Health bonus** | 1,230 |
| **Spiritual health bonus** | 5,740 |
| **Attack damage bonus** | 11 |
| **Movement speed bonus** | 0.07 |
| **EP to evolve into** | 1,250,000 |

</div>

## Evolution

- **Evolves from:** [One Eyed God](one-eyed-god.md)

### Requirements to evolve into God Of Earth

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of ep requirement | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Big Cutie"]
  r1["Earthshaker pDancer"]
  r2["Fang of Earth"]
  r3["Giant Dancer"]
  r4["Giant Elder"]
  r5["Giant King"]
  r6["Giant Queen"]
  r7["Giant Warrior"]
  r8["God Of Earth"]
  r9["Lesser Giant"]
  r10["Mutant Giant"]
  r11["One Eyed God"]
  r0 --> r1
  r1 --> r6
  r2 --> r5
  r3 --> r0
  r3 --> r4
  r4 --> r2
  r7 --> r4
  r7 --> r10
  r9 --> r3
  r9 --> r7
  r10 --> r11
  r11 --> r8
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/spiritual_attack_resistance.png) [Spiritual Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/spiritual-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/thermal_fluctuation_nullification.png) [Thermal Fluctuation Nullification](../../tensura-reincarnated/abilities/resistance-skills/thermal-fluctuation-nullification.md)
- ![](../../assets/icons/tensura/skill/magic_nullification.png) [Magic Nullification](../../tensura-reincarnated/abilities/resistance-skills/magic-nullification.md)
- ![](../../assets/icons/tensura/skill/electricity_nullification.png) [Electricity Nullification](../../tensura-reincarnated/abilities/resistance-skills/electricity-nullification.md)
- ![](../../assets/icons/tensura/skill/darkness_attack_nullification.png) [Darkness Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/darkness-attack-nullification.md)
-  [Size Condense](../abilities/intrinsic-skills/size-condense.md)

## Traits

- Divine

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | size | add |
| Max Health | max HP | add |
| Max Spiritual Health | max spiritual HP | add |
| Attack Damage | attack | add |
| Attack Speed | attack speed | add |
| Knockback Resistance | knockback resistance | add |
| Movement Speed | movement speed | add |
| Swim Speed Multiplier | swim speed | add |

## Stats (config defaults)

Set in [`config/nightmare/race/giant_clan_config.toml`](../configs/config-nightmare-race-giant-clan-config.md).

| Option | Default | Description |
|---|---|---|
| `GodOfEarth.epRequirement` | 1,250,000 | Existence points required to evolve into God Of Earth. |
| `GodOfEarth.minAura` | 375,000 | Minimal aura. |
| `GodOfEarth.maxAura` | 750,000 | Maximum aura. |
| `GodOfEarth.minMagicule` | 625,000 | Minimal magicule. |
| `GodOfEarth.maxMagicule` | 1,250,000 | Maximum magicule. |
| `GodOfEarth.size` | 2.5 | Bonus Size. |
| `GodOfEarth.maxHealth` | 1,230 | Bonus Max Health. |
| `GodOfEarth.maxSpiritualHealth` | 5,740 | Bonus Max Spiritual Health. |
| `GodOfEarth.attack` | 11 | Bonus Attack Damage. |
| `GodOfEarth.attackSpeed` | 0.3 | Bonus Attack Speed. |
| `GodOfEarth.knockbackResistance` | 1.4 | Bonus Knockback Resistance. |
| `GodOfEarth.movementSpeed` | 0.07 | Bonus Movement Speed. |
| `GodOfEarth.swimSpeed` | 0.07 | Bonus Swimming Speed Multiplier. |
| `OneEyedGod.epRequirement` | 450,000 | Existence points required to evolve into One Eyed God. |
| `OneEyedGod.minAura` | 135,000 | Minimal aura. |
| `OneEyedGod.maxAura` | 270,000 | Maximum aura. |
| `OneEyedGod.minMagicule` | 225,000 | Minimal magicule. |
| `OneEyedGod.maxMagicule` | 450,000 | Maximum magicule. |
| `OneEyedGod.size` | 2 | Bonus Size. |
| `OneEyedGod.maxHealth` | 730 | Bonus Max Health. |
| `OneEyedGod.maxSpiritualHealth` | 4,440 | Bonus Max Spiritual Health. |
| `OneEyedGod.attack` | 7.5 | Bonus Attack Damage. |
| `OneEyedGod.attackSpeed` | 0.2 | Bonus Attack Speed. |
| `OneEyedGod.knockbackResistance` | 1.2 | Bonus Knockback Resistance. |
| `OneEyedGod.movementSpeed` | 0.06 | Bonus Movement Speed. |
| `OneEyedGod.swimSpeed` | 0.06 | Bonus Swimming Speed Multiplier. |
| `MutantGiant.epRequirement` | 100,000 | Existence points required to evolve into Mutant Giant. |
| `MutantGiant.minAura` | 30,000 | Minimal aura. |
| `MutantGiant.maxAura` | 60,000 | Maximum aura. |
| `MutantGiant.minMagicule` | 50,000 | Minimal magicule. |
| `MutantGiant.maxMagicule` | 100,000 | Maximum magicule. |
| `MutantGiant.size` | 1.5 | Bonus Size. |
| `MutantGiant.maxHealth` | 400 | Bonus Max Health. |
| `MutantGiant.maxSpiritualHealth` | 940 | Bonus Max Spiritual Health. |
| `MutantGiant.attack` | 4.5 | Bonus Attack Damage. |
| `MutantGiant.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `MutantGiant.knockbackResistance` | 1 | Bonus Knockback Resistance. |
| `MutantGiant.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `MutantGiant.swimSpeed` | 0.05 | Bonus Swimming Speed Multiplier. |
| `GiantWarrior.epRequirement` | 40,000 | Existence points required to evolve into Giant Warrior. |
| `GiantWarrior.minAura` | 25,000 | Minimal aura. |
| `GiantWarrior.maxAura` | 50,000 | Maximum aura. |
| `GiantWarrior.minMagicule` | 15,000 | Minimal magicule. |
| `GiantWarrior.maxMagicule` | 30,000 | Maximum magicule. |
| `GiantWarrior.size` | 0.5 | Bonus Size. |
| `GiantWarrior.maxHealth` | 330 | Bonus Max Health. |
| `GiantWarrior.maxSpiritualHealth` | 940 | Bonus Max Spiritual Health. |
| `GiantWarrior.attack` | 3.5 | Bonus Attack Damage. |
| `GiantWarrior.attackSpeed` | 0 | Bonus Attack Speed. |
| `GiantWarrior.knockbackResistance` | 0.8 | Bonus Knockback Resistance. |
| `GiantWarrior.movementSpeed` | 0.04 | Bonus Movement Speed. |
| `GiantWarrior.swimSpeed` | 0.04 | Bonus Swimming Speed Multiplier. |
| `LesserGiant.minAura` | 500 | Minimal aura. |
| `LesserGiant.maxAura` | 500 | Maximum aura. |
| `LesserGiant.minMagicule` | 1,500 | Minimal magicule. |
| `LesserGiant.maxMagicule` | 5,500 | Maximum magicule. |
| `LesserGiant.size` | 0.5 | Bonus Size. |
| `LesserGiant.maxHealth` | 80 | Bonus Max Health. |
| `LesserGiant.maxSpiritualHealth` | 240 | Bonus Max Spiritual Health. |
| `LesserGiant.attack` | 2 | Bonus Attack Damage. |
| `LesserGiant.attackSpeed` | 0 | Bonus Attack Speed. |
| `LesserGiant.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `LesserGiant.movementSpeed` | 0.04 | Bonus Movement Speed. |
| `LesserGiant.swimSpeed` | 0.04 | Bonus Swimming Speed Multiplier. |

## Tags

`tensura:races/divine`
