# Wight

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:wight` |
| **Difficulty** | Hard |
| **Alignment** | Majin |
| **Aura** | 100 - 500 |
| **Magicule** | 2,000 - 3,000 |
| **Health bonus** | 0 |
| **Spiritual health bonus** | 0 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0 |

</div>

> A Demi-Spiritual skeletal Undead Monster, highly weakened by sunlight.

## Evolution

- **Evolves into:** [Human](human.md), [Wight King](wight-king.md)
- **Default evolution:** [Wight King](wight-king.md)
- **On awakening (True Demon Lord / True Hero):** [Spirit Skeleton](spirit-skeleton.md)
- **During the Harvest Festival:** [Wight King](wight-king.md)

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

- ![](../../assets/icons/tensura/skill/physical_attack_resistance.png) [Physical Attack Resistance](../abilities/resistance-skills/physical-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/pain_nullification.png) [Pain Nullification](../abilities/resistance-skills/pain-nullification.md)

## Traits

- Necromancer
- Undead

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 0 | add |
| Max Spiritual Health | 0 | add |
| Attack Damage | 0 | add |
| Attack Speed | -0.2 | add |
| Knockback Resistance | 0 | add |
| Movement Speed | 0 | add |
| Swim Speed Multiplier | 0 | add |

## Stats (config defaults)

Set in [`config/tensura/race/wight_config.toml`](../configs/config-tensura-race-wight-config.md).

| Option | Default | Description |
|---|---|---|
| `Wight.minAura` | 100 | Minimal aura. |
| `Wight.maxAura` | 500 | Maximum aura. |
| `Wight.minMagicule` | 2,000 | Minimal magicule. |
| `Wight.maxMagicule` | 3,000 | Maximum magicule. |
| `Wight.size` | 0 | Bonus Size. |
| `Wight.maxHealth` | 0 | Bonus Max Health. |
| `Wight.maxSpiritualHealth` | 0 | Bonus Max Spiritual Health. |
| `Wight.attack` | 0 | Bonus Attack Damage. |
| `Wight.attackSpeed` | -0.2 | Bonus Attack Speed. |
| `Wight.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Wight.movementSpeed` | 0 | Bonus Movement Speed. |
| `Wight.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |

## Tags

`tensura:races/necromancer`, `tensura:races/undead`
