# Ghoul

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:ghoul` |
| **Difficulty** | Hard |
| **Alignment** | Majin |
| **Aura** | 1,000 - 2,000 |
| **Magicule** | 2,000 - 3,000 |
| **Health bonus** | -6 |
| **Spiritual health bonus** | -20 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | -0.02 |

</div>

> A vampiric thrall brought about by Blood Raise, highly weakened by sunlight.

## Evolution

- **Evolves into:** [Vampire](vampire.md)
- **Default evolution:** [Vampire](vampire.md)
- **On awakening (True Demon Lord / True Hero):** [Vampire Lord](vampire-lord.md)
- **During the Harvest Festival:** [Vampire](vampire.md)

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

- ![](../../assets/icons/tensura/skill/strength.png) [Strength](../abilities/common-skills/strength.md)

## Traits

- Cannot heal by eating
- Undead

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | -6 | add |
| Max Spiritual Health | -20 | add |
| Attack Damage | 0 | add |
| Attack Speed | -0.5 | add |
| Knockback Resistance | 0 | add |
| Movement Speed | -0.02 | add |
| Swim Speed Multiplier | -0.2 | add |

## Stats (config defaults)

Set in [`config/tensura/race/vampire_config.toml`](../configs/config-tensura-race-vampire-config.md).

| Option | Default | Description |
|---|---|---|
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

`tensura:races/unable_to_heal_with_food`, `tensura:races/undead`
