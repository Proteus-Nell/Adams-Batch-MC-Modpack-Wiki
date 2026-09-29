# Vampire Overcomer

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:vampire_overcomer` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 50,000 - 70,000 |
| **Magicule** | 100,000 - 120,000 |
| **Health bonus** | 80 |
| **Spiritual health bonus** | 300 |
| **Attack damage bonus** | 3 |
| **Movement speed bonus** | 0.01 |
| **EP to evolve into** | 150,000 |

</div>

> Vampires that have evolved to overcome their weakness against the sun.

## Evolution

- **Evolves from:** [Vampire](vampire.md)
- **Evolves into:** [Vampire Lord](vampire-lord.md)
- **Default evolution:** [Vampire Lord](vampire-lord.md)
- **On awakening (True Demon Lord / True Hero):** [Vampire Lord](vampire-lord.md)
- **During the Harvest Festival:** [Vampire](vampire.md)

### Requirements to evolve into Vampire Overcomer

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 150,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Cursed Dreadnaught"]
  r1["Cursed Mariner"]
  r2["Dark Lord Dullahan"]
  r3["Davy Jones"]
  r4["Death Knight"]
  r5["Dullahan"]
  r6["Elder Lich"]
  r7["Lich"]
  r8["Lich King"]
  r9["Mage Skeleton"]
  r10["Phantom Corsair"]
  r11["Skeleton Warrior"]
  r12["Skeleton"]
  r13["Zombie"]
  r14["Divine Human"]
  r15["Divine Skeleton"]
  r16["Divine Vampire"]
  r17["Enlightened Human"]
  r18["Ghoul"]
  r19["Human"]
  r20["Human Saint"]
  r21["Spirit Skeleton"]
  r22["Vampire"]
  r23["Vampire Lord"]
  r24["Vampire Overcomer"]
  r25["Wight"]
  r26["Wight King"]
  r0 --> r10
  r1 --> r0
  r4 --> r5
  r5 --> r2
  r6 --> r7
  r7 --> r8
  r9 --> r6
  r10 --> r3
  r11 --> r4
  r12 --> r9
  r12 --> r11
  r13 --> r12
  r15 --> r26
  r16 --> r22
  r17 --> r20
  r18 --> r22
  r18 --> r23
  r19 --> r17
  r19 --> r20
  r19 --> r22
  r20 --> r14
  r21 --> r15
  r21 --> r26
  r22 --> r23
  r22 --> r24
  r23 --> r16
  r23 --> r22
  r24 --> r22
  r24 --> r23
  r25 --> r1
  r25 --> r13
  r25 --> r19
  r25 --> r21
  r25 --> r26
  r26 --> r21
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/blood_mist.png) [Blood Mist](../abilities/intrinsic-skills/blood-mist.md)
- ![](../../assets/icons/tensura/skill/steel_strength.png) [Steel Strength](../abilities/extra-skills/steel-strength.md)
- ![](../../assets/icons/tensura/skill/shadow_motion.png) [Shadow Motion](../abilities/extra-skills/shadow-motion.md)
- ![](../../assets/icons/tensura/skill/coercion.png) [Coercion](../abilities/common-skills/coercion.md)
- ![](../../assets/icons/tensura/skill/strength.png) [Strength](../abilities/common-skills/strength.md)
- ![](../../assets/icons/tensura/skill/charm.png) [Charm](../abilities/intrinsic-skills/charm.md)

## Traits

- Cannot heal by eating

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 80 | add |
| Max Spiritual Health | 300 | add |
| Attack Damage | 3 | add |
| Attack Speed | 0.2 | add |
| Knockback Resistance | 0.3 | add |
| Movement Speed | 0.01 | add |
| Swim Speed Multiplier | 0.1 | add |

## Stats (config defaults)

Set in [`config/tensura/race/vampire_config.toml`](../configs/config-tensura-race-vampire-config.md).

| Option | Default | Description |
|---|---|---|
| `VampireOvercomer.epRequirement` | 150,000 | EP requirement to evolve into Vampire Overcomer. |
| `VampireOvercomer.minAura` | 50,000 | Minimal aura. |
| `VampireOvercomer.maxAura` | 70,000 | Maximum aura. |
| `VampireOvercomer.minMagicule` | 100,000 | Minimal magicule. |
| `VampireOvercomer.maxMagicule` | 120,000 | Maximum magicule. |
| `VampireOvercomer.size` | 0 | Bonus Size. |
| `VampireOvercomer.maxHealth` | 80 | Bonus Max Health. |
| `VampireOvercomer.maxSpiritualHealth` | 300 | Bonus Max Spiritual Health. |
| `VampireOvercomer.attack` | 3 | Bonus Attack Damage. |
| `VampireOvercomer.attackSpeed` | 0.2 | Bonus Attack Speed. |
| `VampireOvercomer.knockbackResistance` | 0.3 | Bonus Knockback Resistance. |
| `VampireOvercomer.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `VampireOvercomer.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
| `Vampire.bloodRequirement` | 1 | The amount of Zane Blood consumed to evolve into Vampire from Ghoul. |
| `Vampire.bloodRequirementHuman` | 5 | The amount of Zane Blood consumed to evolve into Vampire from Human. |
| `Vampire.minAura` | 3,000 | Minimal aura. |
| `Vampire.maxAura` | 5,000 | Maximum aura. |
| `Vampire.minMagicule` | 5,000 | Minimal magicule. |
| `Vampire.maxMagicule` | 7,000 | Maximum magicule. |
| `Vampire.size` | 0 | Bonus Size. |
| `Vampire.maxHealth` | 10 | Bonus Max Health. |
| `Vampire.maxSpiritualHealth` | 0 | Bonus Max Spiritual Health. |
| `Vampire.attack` | 3 | Bonus Attack Damage. |
| `Vampire.attackSpeed` | 0 | Bonus Attack Speed. |
| `Vampire.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `Vampire.movementSpeed` | 0 | Bonus Movement Speed. |
| `Vampire.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `Ghoul.minAura` | 1,000 | Minimal aura. |
| `Ghoul.maxAura` | 2,000 | Maximum aura. |
| `Ghoul.minMagicule` | 2,000 | Minimal magicule. |
| `Ghoul.maxMagicule` | 3,000 | Maximum magicule. |
| `Ghoul.size` | 0 | Bonus Size. |
| `Ghoul.maxHealth` | -6 | Bonus Max Health. |
| `Ghoul.maxSpiritualHealth` | -20 | Bonus Max Spiritual Health. |
| `Ghoul.attack` | 0 | Bonus Attack Damage. |
| `Ghoul.attackSpeed` | -0.5 | Bonus Attack Speed. |
| `Ghoul.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Ghoul.movementSpeed` | -0.02 | Bonus Movement Speed. |
| `Ghoul.swimSpeed` | -0.2 | Bonus Swimming Speed Multiplier. |

## Tags

`tensura:races/unable_to_heal_with_food`
