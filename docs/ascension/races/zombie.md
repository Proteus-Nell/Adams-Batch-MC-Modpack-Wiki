# Zombie

<small>[Ascension](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `ascension:zombie` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 100 - 500 |
| **Magicule** | 2,000 - 3,000 |
| **Health bonus** | 0 |
| **Spiritual health bonus** | 0 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0 |

</div>

> A risen corpse — entry to the Undead chain, branching off the Wight race. Pain Resistance and Majin alignment, but burns and weakens in sunlight.

## Evolution

- **Evolves from:** [Wight](../../tensura-reincarnated/races/wight.md)
- **Evolves into:** [Skeleton](undead-skeleton.md)
- **Default evolution:** [Skeleton](undead-skeleton.md)
- **On awakening (True Demon Lord / True Hero):** [Skeleton](undead-skeleton.md)
- **During the Harvest Festival:** [Skeleton](undead-skeleton.md)

### Requirements to evolve into Zombie

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of undead_skeleton (evolution ep) | 100% |

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

## Learnable skills

This race can learn these skills through training.

- ![](../../assets/icons/tensura/skill/pain_resistance.png) [Pain Resistance](../../tensura-reincarnated/abilities/resistance-skills/pain-resistance.md)

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

Set in [`config/tensura/race/wight_config.toml`](../../tensura-reincarnated/configs/config-tensura-race-wight-config.md).

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
