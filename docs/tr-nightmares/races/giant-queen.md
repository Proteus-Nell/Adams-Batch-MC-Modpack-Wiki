# Giant Queen

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:giant_queen` |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 1,250,000 - 2,500,000 |
| **Magicule** | 750,000 - 1,500,000 |
| **Health bonus** | 930 |
| **Spiritual health bonus** | 5,640 |
| **Attack damage bonus** | 2.5 |
| **Movement speed bonus** | 0.13 |
| **EP to evolve into** | 2,500,000 |

</div>

## Evolution

- **Evolves from:** [Earthshaker pDancer](earthshaker-dancer.md)

### Requirements to evolve into Giant Queen

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 2,500,000 | 100% |

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

- ![](../../assets/icons/tensura/skill/gravity_attack_nullification.png) [Gravity Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/gravity-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/physical_attack_nullification.png) [Physical Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/physical-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/pain_nullification.png) [Pain Nullification](../../tensura-reincarnated/abilities/resistance-skills/pain-nullification.md)
- ![](../../assets/icons/tensura/skill/pierce_nullification.png) [Pierce Nullification](../../tensura-reincarnated/abilities/resistance-skills/pierce-nullification.md)
- ![](../../assets/icons/tensura/skill/earth_attack_nullification.png) [Earth Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/earth-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/magic_resistance.png) [Magic Resistance](../../tensura-reincarnated/abilities/resistance-skills/magic-resistance.md)
-  [Size Condense](../abilities/intrinsic-skills/size-condense.md)

## Traits

- Divine

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 1 | add |
| Max Health | 930 | add |
| Max Spiritual Health | 5,640 | add |
| Attack Damage | 2.5 | add |
| Attack Speed | 2.5 | add |
| Knockback Resistance | 0.3 | add |
| Movement Speed | 0.13 | add |
| Swim Speed Multiplier | 0.13 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/giant_clan_config.toml`](../configs/config-nightmare-race-giant-clan-config.md).

| Option | Default | Description |
|---|---|---|
| `GiantQueen.epRequirement` | 2,500,000 | Existence points required to evolve into Gian tQueen. |
| `GiantQueen.minAura` | 1,250,000 | Minimal aura. |
| `GiantQueen.maxAura` | 2,500,000 | Maximum aura. |
| `GiantQueen.minMagicule` | 750,000 | Minimal magicule. |
| `GiantQueen.maxMagicule` | 1,500,000 | Maximum magicule. |
| `GiantQueen.size` | 1 | Bonus Size. |
| `GiantQueen.maxHealth` | 930 | Bonus Max Health. |
| `GiantQueen.maxSpiritualHealth` | 5,640 | Bonus Max Spiritual Health. |
| `GiantQueen.attack` | 2.5 | Bonus Attack Damage. |
| `GiantQueen.attackSpeed` | 2.5 | Bonus Attack Speed. |
| `GiantQueen.knockbackResistance` | 0.3 | Bonus Knockback Resistance. |
| `GiantQueen.movementSpeed` | 0.13 | Bonus Movement Speed. |
| `GiantQueen.swimSpeed` | 0.13 | Bonus Swimming Speed Multiplier. |
| `EarthshakerDancer.epRequirement` | 420,000 | Existence points required to evolve into Earthshaker Dancer. |
| `EarthshakerDancer.minAura` | 210,000 | Minimal aura. |
| `EarthshakerDancer.maxAura` | 420,000 | Maximum aura. |
| `EarthshakerDancer.minMagicule` | 126,000 | Minimal magicule. |
| `EarthshakerDancer.maxMagicule` | 252,000 | Maximum magicule. |
| `EarthshakerDancer.size` | 0.5 | Bonus Size. |
| `EarthshakerDancer.maxHealth` | 420 | Bonus Max Health. |
| `EarthshakerDancer.maxSpiritualHealth` | 1,600 | Bonus Max Spiritual Health. |
| `EarthshakerDancer.attack` | 2.3 | Bonus Attack Damage. |
| `EarthshakerDancer.attackSpeed` | 1.5 | Bonus Attack Speed. |
| `EarthshakerDancer.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `EarthshakerDancer.movementSpeed` | 0.11 | Bonus Movement Speed. |
| `EarthshakerDancer.swimSpeed` | 0.11 | Bonus Swimming Speed Multiplier. |
| `BigCutie.epRequirement` | 120,000 | Existence points required to evolve into Big Cutie. |
| `BigCutie.minAura` | 60,000 | Minimal aura. |
| `BigCutie.maxAura` | 120,000 | Maximum aura. |
| `BigCutie.minMagicule` | 40,000 | Minimal magicule. |
| `BigCutie.maxMagicule` | 80,000 | Maximum magicule. |
| `BigCutie.size` | 0.5 | Bonus Size. |
| `BigCutie.maxHealth` | 360 | Bonus Max Health. |
| `BigCutie.maxSpiritualHealth` | 840 | Bonus Max Spiritual Health. |
| `BigCutie.attack` | 2 | Bonus Attack Damage. |
| `BigCutie.attackSpeed` | 1.2 | Bonus Attack Speed. |
| `BigCutie.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `BigCutie.movementSpeed` | 0.09 | Bonus Movement Speed. |
| `BigCutie.swimSpeed` | 0.09 | Bonus Swimming Speed Multiplier. |
| `GiantDancer.epRequirement` | 40,000 | Existence points required to evolve into Giant Dancer. |
| `GiantDancer.minAura` | 25,000 | Minimal aura. |
| `GiantDancer.maxAura` | 50,000 | Maximum aura. |
| `GiantDancer.minMagicule` | 15,000 | Minimal magicule. |
| `GiantDancer.maxMagicule` | 30,000 | Maximum magicule. |
| `GiantDancer.size` | 0.5 | Bonus Size. |
| `GiantDancer.maxHealth` | 300 | Bonus Max Health. |
| `GiantDancer.maxSpiritualHealth` | 840 | Bonus Max Spiritual Health. |
| `GiantDancer.attack` | 2 | Bonus Attack Damage. |
| `GiantDancer.attackSpeed` | 1 | Bonus Attack Speed. |
| `GiantDancer.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `GiantDancer.movementSpeed` | 0.07 | Bonus Movement Speed. |
| `GiantDancer.swimSpeed` | 0.07 | Bonus Swimming Speed Multiplier. |
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
