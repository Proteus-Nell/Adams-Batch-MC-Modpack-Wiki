# Enlightened Human

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:enlightened_human` |
| **Difficulty** | Easy |
| **Alignment** | Default |
| **Aura** | 140,000 - 140,000 |
| **Magicule** | 60,000 - 60,000 |
| **Health bonus** | 80 |
| **Spiritual health bonus** | 300 |
| **Attack damage bonus** | 1 |
| **Movement speed bonus** | 0.01 |
| **EP to evolve into** | 100,000 |

</div>

> Human that has "evolved the correct way" and became a Demi-Spiritual Lifeform.

## Evolution

- **Evolves from:** [Human](human.md)
- **Evolves into:** [Human Saint](human-saint.md)
- **Default evolution:** [Human Saint](human-saint.md)
- **On awakening (True Demon Lord / True Hero):** [Human Saint](human-saint.md)

### Requirements to evolve into Enlightened Human

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 100,000 | 100% |

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

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 80 | add |
| Max Spiritual Health | 300 | add |
| Attack Damage | 1 | add |
| Attack Speed | 0.2 | add |
| Knockback Resistance | 0.1 | add |
| Movement Speed | 0.01 | add |
| Swim Speed Multiplier | 0.1 | add |

## Stats (config defaults)

Set in [`config/tensura/race/human_config.toml`](../configs/config-tensura-race-human-config.md).

| Option | Default | Description |
|---|---|---|
| `EnlightenedHuman.epRequirement` | 100,000 | EP requirement to evolve into Enlightened Human. |
| `EnlightenedHuman.minAura` | 140,000 | Minimal aura. |
| `EnlightenedHuman.maxAura` | 140,000 | Maximum aura. |
| `EnlightenedHuman.minMagicule` | 60,000 | Minimal magicule. |
| `EnlightenedHuman.maxMagicule` | 60,000 | Maximum magicule. |
| `EnlightenedHuman.size` | 0 | Bonus Size. |
| `EnlightenedHuman.maxHealth` | 80 | Bonus Max Health. |
| `EnlightenedHuman.maxSpiritualHealth` | 300 | Bonus Max Spiritual Health. |
| `EnlightenedHuman.attack` | 1 | Bonus Attack Damage. |
| `EnlightenedHuman.attackSpeed` | 0.2 | Bonus Attack Speed. |
| `EnlightenedHuman.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `EnlightenedHuman.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `EnlightenedHuman.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
| `Human.minAura` | 760 | Minimal aura. |
| `Human.maxAura` | 1,140 | Maximum aura. |
| `Human.minMagicule` | 50 | Minimal magicule. |
| `Human.maxMagicule` | 70 | Maximum magicule. |
| `Human.size` | 0 | Bonus Size. |
| `Human.maxHealth` | 0 | Bonus Max Health. |
| `Human.maxSpiritualHealth` | 0 | Bonus Max Spiritual Health. |
| `Human.attack` | 0 | Bonus Attack Damage. |
| `Human.attackSpeed` | 0 | Bonus Attack Speed. |
| `Human.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Human.movementSpeed` | 0 | Bonus Movement Speed. |
| `Human.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
