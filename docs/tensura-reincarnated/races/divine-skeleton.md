# Divine Skeleton

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:divine_skeleton` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 1,000,000 - 1,000,000 |
| **Magicule** | 1,000,000 - 1,000,000 |
| **Health bonus** | 1,140 |
| **Spiritual health bonus** | 6,500 |
| **Attack damage bonus** | 4 |
| **Movement speed bonus** | 0.05 |
| **EP to evolve into** | 2,000,000 |

</div>

> Wight that achieved divinity, possessing an immortal physical body that will never age.

## Evolution

- **Evolves from:** [Spirit Skeleton](spirit-skeleton.md)
- **During the Harvest Festival:** [Wight King](wight-king.md)

### Requirements to evolve into Divine Skeleton

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 2,000,000 | 100% |

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

- ![](../../assets/icons/tensura/skill/divine_ki_release.png) [Divine Ki Release](../abilities/intrinsic-skills/divine-ki-release.md)
- ![](../../assets/icons/tensura/skill/curse.png) [Curse](../abilities/spiritual-magic/curse.md)
- ![](../../assets/icons/tensura/skill/create_lesser_undead.png) [Create Lesser Undead](../abilities/spiritual-magic/create-lesser-undead.md)
- ![](../../assets/icons/tensura/skill/physical_attack_resistance.png) [Physical Attack Resistance](../abilities/resistance-skills/physical-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/pain_nullification.png) [Pain Nullification](../abilities/resistance-skills/pain-nullification.md)

## Traits

- Divine
- Necromancer
- Undead

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 1,140 | add |
| Max Spiritual Health | 6,500 | add |
| Attack Damage | 4 | add |
| Attack Speed | 0.5 | add |
| Knockback Resistance | 0.3 | add |
| Movement Speed | 0.05 | add |
| Swim Speed Multiplier | 0.5 | add |

## Stats (config defaults)

Set in [`config/tensura/race/wight_config.toml`](../configs/config-tensura-race-wight-config.md).

| Option | Default | Description |
|---|---|---|
| `DivineSkeleton.epRequirement` | 2,000,000 | EP requirement to evolve into Divine Skeleton. |
| `DivineSkeleton.minAura` | 1,000,000 | Minimal aura. |
| `DivineSkeleton.maxAura` | 1,000,000 | Maximum aura. |
| `DivineSkeleton.minMagicule` | 1,000,000 | Minimal magicule. |
| `DivineSkeleton.maxMagicule` | 1,000,000 | Maximum magicule. |
| `DivineSkeleton.size` | 0 | Bonus Size. |
| `DivineSkeleton.maxHealth` | 1,140 | Bonus Max Health. |
| `DivineSkeleton.maxSpiritualHealth` | 6,500 | Bonus Max Spiritual Health. |
| `DivineSkeleton.attack` | 4 | Bonus Attack Damage. |
| `DivineSkeleton.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `DivineSkeleton.knockbackResistance` | 0.3 | Bonus Knockback Resistance. |
| `DivineSkeleton.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `DivineSkeleton.swimSpeed` | 0.5 | Bonus Swimming Speed Multiplier. |
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

`tensura:races/divine`, `tensura:races/necromancer`, `tensura:races/undead`
