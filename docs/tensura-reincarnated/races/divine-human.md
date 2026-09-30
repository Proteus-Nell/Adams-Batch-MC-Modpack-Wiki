# Divine Human

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:divine_human` |
| **Stage** | <span class="stage stage-final">Final</span> |
| **Difficulty** | Easy |
| **Alignment** | Holy |
| **Aura** | 1,000,000 - 1,000,000 |
| **Magicule** | 1,000,000 - 1,000,000 |
| **Health bonus** | 980 |
| **Spiritual health bonus** | 6,000 |
| **Attack damage bonus** | 3 |
| **Movement speed bonus** | 0.1 |
| **EP to evolve into** | 2,000,000 |

</div>

> Human that achieved divinity, possessing an immortal physical body that will never age.

## Evolution

- **Evolves from:** [Human Saint](human-saint.md)

### Requirements to evolve into Divine Human

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

## Traits

- Divine

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 980 | add |
| Max Spiritual Health | 6,000 | add |
| Attack Damage | 3 | add |
| Attack Speed | 0.7 | add |
| Knockback Resistance | 0.3 | add |
| Movement Speed | 0.1 | add |
| Swim Speed Multiplier | 1 | add |

## Stats (config defaults)

Set in [`config/tensura/race/human_config.toml`](../configs/config-tensura-race-human-config.md).

| Option | Default | Description |
|---|---|---|
| `DivineHuman.epRequirement` | 2,000,000 | EP requirement to evolve into Divine Human. |
| `DivineHuman.minAura` | 1,000,000 | Minimal aura. |
| `DivineHuman.maxAura` | 1,000,000 | Maximum aura. |
| `DivineHuman.minMagicule` | 1,000,000 | Minimal magicule. |
| `DivineHuman.maxMagicule` | 1,000,000 | Maximum magicule. |
| `DivineHuman.size` | 0 | Bonus Size. |
| `DivineHuman.maxHealth` | 980 | Bonus Max Health. |
| `DivineHuman.maxSpiritualHealth` | 6,000 | Bonus Max Spiritual Health. |
| `DivineHuman.attack` | 3 | Bonus Attack Damage. |
| `DivineHuman.attackSpeed` | 0.7 | Bonus Attack Speed. |
| `DivineHuman.knockbackResistance` | 0.3 | Bonus Knockback Resistance. |
| `DivineHuman.movementSpeed` | 0.1 | Bonus Movement Speed. |
| `DivineHuman.swimSpeed` | 1 | Bonus Swimming Speed Multiplier. |
| `HumanSaint.epRequirement` | 400,000 | EP requirement to evolve into Human Saint. |
| `HumanSaint.bossRequirement` | 4 | The number of Bosses defeated to evolve into Human Saint. |
| `HumanSaint.minAura` | 400,000 | Minimal aura. |
| `HumanSaint.maxAura` | 400,000 | Maximum aura. |
| `HumanSaint.minMagicule` | 400,000 | Minimal magicule. |
| `HumanSaint.maxMagicule` | 400,000 | Maximum magicule. |
| `HumanSaint.size` | 0 | Bonus Size. |
| `HumanSaint.maxHealth` | 480 | Bonus Max Health. |
| `HumanSaint.maxSpiritualHealth` | 3,000 | Bonus Max Spiritual Health. |
| `HumanSaint.attack` | 2 | Bonus Attack Damage. |
| `HumanSaint.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `HumanSaint.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `HumanSaint.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `HumanSaint.swimSpeed` | 0.5 | Bonus Swimming Speed Multiplier. |
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

## Tags

`tensura:races/divine`
