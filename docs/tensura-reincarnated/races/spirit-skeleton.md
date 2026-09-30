# Spirit Skeleton

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:spirit_skeleton` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 300,000 - 300,000 |
| **Magicule** | 500,000 - 500,000 |
| **Health bonus** | 520 |
| **Spiritual health bonus** | 3,200 |
| **Attack damage bonus** | 3 |
| **Movement speed bonus** | 0.03 |
| **EP to evolve into** | 800,000 |

</div>

> Wight that has "evolved the correct way" and became a Spiritual Lifeform.

## Evolution

- **Evolves from:** [Wight King](wight-king.md), [Wight](wight.md)
- **Evolves into:** [Divine Skeleton](divine-skeleton.md)
- **Default evolution:** [Divine Skeleton](divine-skeleton.md)
- **On awakening (True Demon Lord / True Hero):** [Divine Skeleton](divine-skeleton.md)
- **During the Harvest Festival:** [Wight King](wight-king.md)

### Requirements to evolve into Spirit Skeleton

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 800,000 | 100% |

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

- ![](../../assets/icons/tensura/skill/curse.png) [Curse](../abilities/spiritual-magic/curse.md)
- ![](../../assets/icons/tensura/skill/create_lesser_undead.png) [Create Lesser Undead](../abilities/spiritual-magic/create-lesser-undead.md)
- ![](../../assets/icons/tensura/skill/physical_attack_resistance.png) [Physical Attack Resistance](../abilities/resistance-skills/physical-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/pain_nullification.png) [Pain Nullification](../abilities/resistance-skills/pain-nullification.md)

## Traits

- Necromancer
- Spiritual lifeform
- Undead

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 520 | add |
| Max Spiritual Health | 3,200 | add |
| Attack Damage | 3 | add |
| Attack Speed | 0.3 | add |
| Knockback Resistance | 0.1 | add |
| Movement Speed | 0.03 | add |
| Swim Speed Multiplier | 0.3 | add |

## Stats (config defaults)

Set in [`config/tensura/race/wight_config.toml`](../configs/config-tensura-race-wight-config.md).

| Option | Default | Description |
|---|---|---|
| `SpiritSkeleton.epRequirement` | 800,000 | EP requirement to evolve into Spirit Skeleton. |
| `SpiritSkeleton.minAura` | 300,000 | Minimal aura. |
| `SpiritSkeleton.maxAura` | 300,000 | Maximum aura. |
| `SpiritSkeleton.minMagicule` | 500,000 | Minimal magicule. |
| `SpiritSkeleton.maxMagicule` | 500,000 | Maximum magicule. |
| `SpiritSkeleton.size` | 0 | Bonus Size. |
| `SpiritSkeleton.maxHealth` | 520 | Bonus Max Health. |
| `SpiritSkeleton.maxSpiritualHealth` | 3,200 | Bonus Max Spiritual Health. |
| `SpiritSkeleton.attack` | 3 | Bonus Attack Damage. |
| `SpiritSkeleton.attackSpeed` | 0.3 | Bonus Attack Speed. |
| `SpiritSkeleton.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `SpiritSkeleton.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `SpiritSkeleton.swimSpeed` | 0.3 | Bonus Swimming Speed Multiplier. |
| `WightKing.epRequirement` | 200,000 | EP requirement to evolve into Wight King. |
| `WightKing.minAura` | 100,000 | Minimal aura. |
| `WightKing.maxAura` | 100,000 | Maximum aura. |
| `WightKing.minMagicule` | 300,000 | Minimal magicule. |
| `WightKing.maxMagicule` | 300,000 | Maximum magicule. |
| `WightKing.size` | 0 | Bonus Size. |
| `WightKing.maxHealth` | 100 | Bonus Max Health. |
| `WightKing.maxSpiritualHealth` | 515 | Bonus Max Spiritual Health. |
| `WightKing.attack` | 1 | Bonus Attack Damage. |
| `WightKing.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `WightKing.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `WightKing.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `WightKing.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
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

`tensura:races/necromancer`, `tensura:races/spiritual`, `tensura:races/undead`
