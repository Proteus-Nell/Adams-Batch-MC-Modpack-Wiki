# Lesser Zombie Dragon

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:lesser_zombie_dragon` |
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

> A cursed lesser dragon reanimated by deathly force.

## Evolution

- **Evolves from:** [Lesser Dragon](lesser-dragon.md)
- **Evolves into:** [Medium Zombie Dragon](medium-zombie-dragon.md)
- **Default evolution:** [Medium Zombie Dragon](medium-zombie-dragon.md)

### Requirements to evolve into Lesser Zombie Dragon

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of min base aura + min base magicule | 100% |

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
| `LesserZombieDragon.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `LesserZombieDragon.minAura` | 1,000 | Minimal aura. |
| `LesserZombieDragon.maxAura` | 2,000 | Maximum aura. |
| `LesserZombieDragon.minMagicule` | 3,000 | Minimal magicule. |
| `LesserZombieDragon.maxMagicule` | 6,000 | Maximum magicule. |
| `LesserZombieDragon.size` | 0 | Bonus Size. |
| `LesserZombieDragon.maxHealth` | 20 | Bonus Max Health. |
| `LesserZombieDragon.maxSpiritualHealth` | 80 | Bonus Max Spiritual Health. |
| `LesserZombieDragon.attack` | 0 | Bonus Attack Damage. |
| `LesserZombieDragon.attackSpeed` | 0 | Bonus Attack Speed. |
| `LesserZombieDragon.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `LesserZombieDragon.movementSpeed` | 0 | Bonus Movement Speed. |
| `LesserZombieDragon.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `LesserZombieDragon.minAura` | 6,000 |  |
| `LesserZombieDragon.maxAura` | 12,000 |  |
| `LesserZombieDragon.minMagicule` | 8,000 |  |
| `LesserZombieDragon.maxMagicule` | 16,000 |  |
| `LesserZombieDragon.size` | 0.2 |  |
| `LesserZombieDragon.maxHealth` | 45 |  |
| `LesserZombieDragon.maxSpiritualHealth` | 80 |  |
| `LesserZombieDragon.attack` | 1 |  |
| `LesserZombieDragon.attackSpeed` | -0.25 |  |
| `LesserZombieDragon.knockbackResistance` | 0.2 |  |
| `LesserZombieDragon.movementSpeed` | -0.005 |  |
| `LesserZombieDragon.swimSpeed` | -0.05 |  |

## Tags

`tensura:races/has_creative_flight`
