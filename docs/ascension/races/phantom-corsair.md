# Phantom Corsair

<small>[Ascension](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `ascension:phantom_corsair` |
| **Difficulty** | Hard |
| **Alignment** | Majin |
| **Aura** | 100 - 500 |
| **Magicule** | 2,000 - 3,000 |
| **Health bonus** | 0 |
| **Spiritual health bonus** | 0 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0 |

</div>

> A dread pirate dissolved into spectral darkness — slips through walls and commands the deep.

## Evolution

- **Evolves from:** [Cursed Dreadnaught](cursed-dreadnaught.md)
- **Evolves into:** [Davy Jones](davy-jones.md)
- **Default evolution:** [Davy Jones](davy-jones.md)
- **On awakening (True Demon Lord / True Hero):** [Davy Jones](davy-jones.md)
- **During the Harvest Festival:** [Davy Jones](davy-jones.md)

### Requirements to evolve into Phantom Corsair

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of phantom_corsair (evolution ep) | 50% |
| True Demon Lord | 50% |

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

- ![](../../assets/icons/tensura/skill/body_armor.png) [Body Armor](../../tensura-reincarnated/abilities/intrinsic-skills/body-armor.md)
- ![](../../assets/icons/tensura/skill/water_breathing.png) [Water Breathing](../../tensura-reincarnated/abilities/intrinsic-skills/water-breathing.md)
- ![](../../assets/icons/tensura/skill/drain.png) [Drain](../../tensura-reincarnated/abilities/intrinsic-skills/drain.md)
- ![](../../assets/icons/tensura/skill/physical_attack_resistance.png) [Physical Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/physical-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/pain_nullification.png) [Pain Nullification](../../tensura-reincarnated/abilities/resistance-skills/pain-nullification.md)

## Learnable skills

This race can learn these skills through training.

- ![](../../assets/icons/tensura/skill/water_manipulation.png) [Water Manipulation](../../tensura-reincarnated/abilities/extra-skills/water-manipulation.md)
- ![](../../assets/icons/tensura/skill/spatial_motion.png) [Spatial Motion](../../tensura-reincarnated/abilities/extra-skills/spatial-motion.md)
- ![](../../assets/icons/tensura/skill/magic_darkness_transform.png) [Magic Darkness Transform](../../tensura-reincarnated/abilities/extra-skills/magic-darkness-transform.md)
- ![](../../assets/icons/tensura/skill/darkness_attack_resistance.png) [Darkness Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/darkness-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/water_attack_nullification.png) [Water Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/water-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/body_double.png) [Body Double](../../tensura-reincarnated/abilities/extra-skills/body-double.md)
- ![](../../assets/icons/tensura/skill/weather_domination.png) [Weather Domination](../../tensura-reincarnated/abilities/extra-skills/weather-domination.md)
- ![](../../assets/icons/tensura/skill/spiritual_attack_resistance.png) [Spiritual Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/spiritual-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/water_current_control.png) [Water Current Control](../../tensura-reincarnated/abilities/common-skills/water-current-control.md)
- ![](../../assets/icons/tensura/skill/mortal_fear.png) [Mortal Fear](../../tensura-reincarnated/abilities/extra-skills/mortal-fear.md)
- ![](../../assets/icons/tensura/skill/steel_strength.png) [Steel Strength](../../tensura-reincarnated/abilities/extra-skills/steel-strength.md)
- ![](../../assets/icons/tensura/skill/water_attack_resistance.png) [Water Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/water-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/cold_resistance.png) [Cold Resistance](../../tensura-reincarnated/abilities/resistance-skills/cold-resistance.md)

## Traits

- Damage handling for fire

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0.27 | add |
| Scale | 0.13 | add |
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
