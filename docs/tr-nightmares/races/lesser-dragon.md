# Lesser Dragon

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:lesser_dragon` |
| **Difficulty** | Intermediate |
| **Alignment** | Default |
| **Aura** | 1,000 - 2,000 |
| **Magicule** | 3,000 - 6,000 |
| **Health bonus** | 20 |
| **Spiritual health bonus** | 80 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0 |
| **EP to evolve into** | 0 |

</div>

> A young dragon with fierce instincts and rising magical potential.

## Evolution

- **Evolves into:** [Lesser Holy Dragon](lesser-holy-dragon.md), [Lesser Daemonic Dragon](lesser-daemonic-dragon.md), [Lesser Ender Dragon](lesser-ender-dragon.md), [Lesser Nether Dragon](lesser-nether-dragon.md)
- **Default evolution:** [Lesser Zombie Dragon](lesser-zombie-dragon.md), [Medium Dragon](medium-dragon.md)

### Evolution tree

```mermaid
flowchart LR
  r0["Arch Daemonic Dragon"]
  r1["Arch Dragon"]
  r2["Daemonic Dragon Lord"]
  r3["Death Dragon"]
  r4["Devil Dragon Lord"]
  r5["Divine Dragon Lord"]
  r6["Divine Gehenna Dragon"]
  r7["Divine Heavenly Dragon"]
  r8["Divine Netherite Dragon"]
  r9["Divine Void Dragon"]
  r10["Dragon Lord"]
  r11["Element Dragon"]
  r12["Ender Dragon Prince"]
  r13["Gehenna Dragon"]
  r14["Heavenly Dragon"]
  r15["Lesser Daemonic Dragon"]
  r16["Lesser Dragon"]
  r17["Lesser Ender Dragon"]
  r18["Lesser Holy Dragon"]
  r19["Lesser Nether Dragon"]
  r20["Lesser Zombie Dragon"]
  r21["Medium Daemonic Dragon"]
  r22["Medium Dragon"]
  r23["Medium Ender Dragon"]
  r24["Medium Holy Dragon"]
  r25["Medium Nether Dragon"]
  r26["Medium Zombie Dragon"]
  r27["Netherite Dragon"]
  r28["Saint Dragon"]
  r29["Scrap Dragon"]
  r30["Void Dragon"]
  r0 --> r2
  r1 --> r3
  r1 --> r10
  r1 --> r11
  r2 --> r4
  r3 --> r13
  r5 --> r6
  r10 --> r5
  r10 --> r13
  r11 --> r3
  r11 --> r10
  r12 --> r30
  r13 --> r6
  r14 --> r7
  r15 --> r21
  r16 --> r15
  r16 --> r17
  r16 --> r18
  r16 --> r19
  r16 --> r20
  r16 --> r22
  r17 --> r23
  r18 --> r24
  r19 --> r25
  r20 --> r26
  r21 --> r0
  r22 --> r1
  r22 --> r26
  r23 --> r12
  r24 --> r28
  r25 --> r29
  r26 --> r3
  r27 --> r8
  r28 --> r14
  r29 --> r27
  r30 --> r9
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/dragon_ear.png) [Dragon Ear](../../tensura-reincarnated/abilities/intrinsic-skills/dragon-ear.md)
- ![](../../assets/icons/tensura/skill/dragon_eye.png) [Dragon Eye](../../tensura-reincarnated/abilities/intrinsic-skills/dragon-eye.md)
- ![](../../assets/icons/tensura/skill/dragon_skin.png) [Dragon Skin](../../tensura-reincarnated/abilities/intrinsic-skills/dragon-skin.md)
-  [Size Condense](../abilities/intrinsic-skills/size-condense.md)

## Traits

- Has creative-style flight

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

Set in [`config/nightmare/race/dragon_config.toml`](../configs/config-nightmare-race-dragon-config.md).

| Option | Default | Description |
|---|---|---|
| `LesserDragon.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `LesserDragon.minAura` | 1,000 | Minimal aura. |
| `LesserDragon.maxAura` | 2,000 | Maximum aura. |
| `LesserDragon.minMagicule` | 3,000 | Minimal magicule. |
| `LesserDragon.maxMagicule` | 6,000 | Maximum magicule. |
| `LesserDragon.size` | 0 | Bonus Size. |
| `LesserDragon.maxHealth` | 20 | Bonus Max Health. |
| `LesserDragon.maxSpiritualHealth` | 80 | Bonus Max Spiritual Health. |
| `LesserDragon.attack` | 0 | Bonus Attack Damage. |
| `LesserDragon.attackSpeed` | 0 | Bonus Attack Speed. |
| `LesserDragon.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `LesserDragon.movementSpeed` | 0 | Bonus Movement Speed. |
| `LesserDragon.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `LesserDragon.minAura` | 5,000 |  |
| `LesserDragon.maxAura` | 14,000 |  |
| `LesserDragon.minMagicule` | 12,000 |  |
| `LesserDragon.maxMagicule` | 32,000 |  |
| `LesserDragon.size` | 0.2 |  |
| `LesserDragon.maxHealth` | 45 |  |
| `LesserDragon.maxSpiritualHealth` | 130 |  |
| `LesserDragon.attack` | 1.8 |  |
| `LesserDragon.attackSpeed` | 0.1 |  |
| `LesserDragon.knockbackResistance` | 0.15 |  |
| `LesserDragon.movementSpeed` | 0.01 |  |
| `LesserDragon.swimSpeed` | 0.05 |  |

## Tags

`tensura:races/has_creative_flight`
