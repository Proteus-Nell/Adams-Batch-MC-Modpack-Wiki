# Lesser Zombie Dragon

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:lesser_zombie_dragon` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Intermediate |
| **Alignment** | Default |
| **Aura** | 6,000 - 12,000 |
| **Magicule** | 8,000 - 16,000 |
| **Health bonus** | 45 |
| **Spiritual health bonus** | 80 |
| **Attack damage bonus** | 1 |
| **Movement speed bonus** | -0.005 |
| **EP to evolve into** | 0 |

</div>

> A cursed lesser dragon reanimated by deathly force.

## Evolution

- **Evolves from:** [Lesser Dragon](lesser-dragon.md)
- **Evolves into:** [Medium Zombie Dragon](medium-zombie-dragon.md)
- **Default evolution:** [Medium Zombie Dragon](medium-zombie-dragon.md)
- **During the Harvest Festival:** [Medium Zombie Dragon](medium-zombie-dragon.md)

### Requirements to evolve into Lesser Zombie Dragon

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 14,000 | 100% |

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
  r9["Divine Vampiric Dragon Lord"]
  r10["Divine Void Dragon"]
  r11["Dragon Lord"]
  r12["Element Dragon"]
  r13["Ender Dragon Prince"]
  r14["Gehenna Dragon"]
  r15["Greater Thrall Dragon"]
  r16["Heavenly Dragon"]
  r17["Lesser Daemonic Dragon"]
  r18["Lesser Dragon"]
  r19["Lesser Ender Dragon"]
  r20["Lesser Holy Dragon"]
  r21["Lesser Nether Dragon"]
  r22["Lesser Thrall Dragon"]
  r23["Lesser Zombie Dragon"]
  r24["Medium Daemonic Dragon"]
  r25["Medium Dragon"]
  r26["Medium Ender Dragon"]
  r27["Medium Holy Dragon"]
  r28["Medium Nether Dragon"]
  r29["Medium Zombie Dragon"]
  r30["Netherite Dragon"]
  r31["Saint Dragon"]
  r32["Scrap Dragon"]
  r33["Vampiric Dragon"]
  r34["Vampiric Dragon Lord"]
  r35["Void Dragon"]
  r0 --> r2
  r1 --> r3
  r1 --> r11
  r1 --> r12
  r2 --> r4
  r3 --> r14
  r5 --> r6
  r11 --> r5
  r11 --> r14
  r12 --> r3
  r12 --> r11
  r13 --> r35
  r14 --> r6
  r15 --> r33
  r16 --> r7
  r17 --> r24
  r18 --> r17
  r18 --> r19
  r18 --> r20
  r18 --> r21
  r18 --> r22
  r18 --> r23
  r18 --> r25
  r19 --> r26
  r20 --> r27
  r21 --> r28
  r22 --> r15
  r23 --> r29
  r24 --> r0
  r25 --> r1
  r25 --> r29
  r26 --> r13
  r27 --> r31
  r28 --> r32
  r29 --> r3
  r30 --> r8
  r31 --> r16
  r32 --> r30
  r33 --> r34
  r34 --> r9
  r35 --> r10
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
| Scale | 0.2 | add |
| Max Health | 45 | add |
| Max Spiritual Health | 80 | add |
| Attack Damage | 1 | add |
| Attack Speed | -0.25 | add |
| Knockback Resistance | 0.2 | add |
| Movement Speed | -0.005 | add |
| Swim Speed Multiplier | -0.05 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/dragon_config.toml`](../configs/config-nightmare-race-dragon-config.md).

| Option | Default | Description |
|---|---|---|
| `LesserZombieDragon.epRequirement` | 0 | EP requirement to evolve into this tier. |
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
