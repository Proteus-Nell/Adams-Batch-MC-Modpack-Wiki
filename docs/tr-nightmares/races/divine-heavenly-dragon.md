# Divine Heavenly Dragon

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:divine_heavenly_dragon` |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 1,000 - 2,000 |
| **Magicule** | 3,000 - 6,000 |
| **Health bonus** | 20 |
| **Spiritual health bonus** | 80 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0 |
| **EP to evolve into** | 0 |

</div>

## Evolution

- **Evolves from:** [Heavenly Dragon](heavenly-dragon.md)

### Requirements to evolve into Divine Heavenly Dragon

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of ep requirement | 50% |
| Consume holy essence requirement of [Holy Essence](../items/materials/holy-essence.md) | 50% |

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
- ![](../../assets/icons/tensura/skill/magic_resistance.png) [Magic Resistance](../../tensura-reincarnated/abilities/resistance-skills/magic-resistance.md)
- ![](../../assets/icons/tensura/skill/light_attack_resistance.png) [Light Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/light-attack-resistance.md)
-  [Holy Lightning](../abilities/other-magic/holy-lightning.md)
-  [Size Condense](../abilities/intrinsic-skills/size-condense.md)

## Traits

- Divine
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
| `DivineHeavenlyDragon.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `DivineHeavenlyDragon.minAura` | 1,000 | Minimal aura. |
| `DivineHeavenlyDragon.maxAura` | 2,000 | Maximum aura. |
| `DivineHeavenlyDragon.minMagicule` | 3,000 | Minimal magicule. |
| `DivineHeavenlyDragon.maxMagicule` | 6,000 | Maximum magicule. |
| `DivineHeavenlyDragon.size` | 0 | Bonus Size. |
| `DivineHeavenlyDragon.maxHealth` | 20 | Bonus Max Health. |
| `DivineHeavenlyDragon.maxSpiritualHealth` | 80 | Bonus Max Spiritual Health. |
| `DivineHeavenlyDragon.attack` | 0 | Bonus Attack Damage. |
| `DivineHeavenlyDragon.attackSpeed` | 0 | Bonus Attack Speed. |
| `DivineHeavenlyDragon.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `DivineHeavenlyDragon.movementSpeed` | 0 | Bonus Movement Speed. |
| `DivineHeavenlyDragon.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `DivineHeavenlyDragon.essenceRequirement` | 1 | Holy Essence required to evolve into this tier. |
| `DivineHeavenlyDragon.epRequirement` | 3,000,000 |  |
| `DivineHeavenlyDragon.minAura` | 900,000 |  |
| `DivineHeavenlyDragon.maxAura` | 1,700,000 |  |
| `DivineHeavenlyDragon.minMagicule` | 1,500,000 |  |
| `DivineHeavenlyDragon.maxMagicule` | 3,000,000 |  |
| `DivineHeavenlyDragon.size` | 1.08 |  |
| `DivineHeavenlyDragon.maxHealth` | 1,000 |  |
| `DivineHeavenlyDragon.maxSpiritualHealth` | 8,500 |  |
| `DivineHeavenlyDragon.attack` | 4.1 |  |
| `DivineHeavenlyDragon.attackSpeed` | 0.22 |  |
| `DivineHeavenlyDragon.knockbackResistance` | 0.88 |  |
| `DivineHeavenlyDragon.movementSpeed` | 0.03 |  |
| `DivineHeavenlyDragon.swimSpeed` | 0.2 |  |
| `DivineHeavenlyDragon.essenceRequirement` | 16 | Holy Essence required to evolve into this tier. |
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
| `MediumDragon.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `MediumDragon.minAura` | 1,000 | Minimal aura. |
| `MediumDragon.maxAura` | 2,000 | Maximum aura. |
| `MediumDragon.minMagicule` | 3,000 | Minimal magicule. |
| `MediumDragon.maxMagicule` | 6,000 | Maximum magicule. |
| `MediumDragon.size` | 0 | Bonus Size. |
| `MediumDragon.maxHealth` | 20 | Bonus Max Health. |
| `MediumDragon.maxSpiritualHealth` | 80 | Bonus Max Spiritual Health. |
| `MediumDragon.attack` | 0 | Bonus Attack Damage. |
| `MediumDragon.attackSpeed` | 0 | Bonus Attack Speed. |
| `MediumDragon.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `MediumDragon.movementSpeed` | 0 | Bonus Movement Speed. |
| `MediumDragon.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `MediumDragon.epRequirement` | 160,000 |  |
| `MediumDragon.minAura` | 40,000 |  |
| `MediumDragon.maxAura` | 80,000 |  |
| `MediumDragon.minMagicule` | 120,000 |  |
| `MediumDragon.maxMagicule` | 160,000 |  |
| `MediumDragon.size` | 0.35 |  |
| `MediumDragon.maxHealth` | 170 |  |
| `MediumDragon.maxSpiritualHealth` | 360 |  |
| `MediumDragon.attack` | 1.2 |  |
| `MediumDragon.attackSpeed` | 0 |  |
| `MediumDragon.knockbackResistance` | 0.25 |  |
| `MediumDragon.movementSpeed` | 0.015 |  |
| `MediumDragon.swimSpeed` | 0.08 |  |
| `MediumZombieDragon.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `MediumZombieDragon.minAura` | 1,000 | Minimal aura. |
| `MediumZombieDragon.maxAura` | 2,000 | Maximum aura. |
| `MediumZombieDragon.minMagicule` | 3,000 | Minimal magicule. |
| `MediumZombieDragon.maxMagicule` | 6,000 | Maximum magicule. |
| `MediumZombieDragon.size` | 0 | Bonus Size. |
| `MediumZombieDragon.maxHealth` | 20 | Bonus Max Health. |
| `MediumZombieDragon.maxSpiritualHealth` | 80 | Bonus Max Spiritual Health. |
| `MediumZombieDragon.attack` | 0 | Bonus Attack Damage. |
| `MediumZombieDragon.attackSpeed` | 0 | Bonus Attack Speed. |
| `MediumZombieDragon.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `MediumZombieDragon.movementSpeed` | 0 | Bonus Movement Speed. |
| `MediumZombieDragon.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `MediumZombieDragon.epRequirement` | 100,000 |  |
| `MediumZombieDragon.minAura` | 24,000 |  |
| `MediumZombieDragon.maxAura` | 45,000 |  |
| `MediumZombieDragon.minMagicule` | 35,000 |  |
| `MediumZombieDragon.maxMagicule` | 70,000 |  |
| `MediumZombieDragon.size` | 0.35 |  |
| `MediumZombieDragon.maxHealth` | 90 |  |
| `MediumZombieDragon.maxSpiritualHealth` | 340 |  |
| `MediumZombieDragon.attack` | 1.6 |  |
| `MediumZombieDragon.attackSpeed` | -0.1 |  |
| `MediumZombieDragon.knockbackResistance` | 0.35 |  |
| `MediumZombieDragon.movementSpeed` | 0 |  |
| `MediumZombieDragon.swimSpeed` | -0.02 |  |
| `ArchDragon.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `ArchDragon.minAura` | 1,000 | Minimal aura. |
| `ArchDragon.maxAura` | 2,000 | Maximum aura. |
| `ArchDragon.minMagicule` | 3,000 | Minimal magicule. |
| `ArchDragon.maxMagicule` | 6,000 | Maximum magicule. |
| `ArchDragon.size` | 0 | Bonus Size. |
| `ArchDragon.maxHealth` | 20 | Bonus Max Health. |
| `ArchDragon.maxSpiritualHealth` | 80 | Bonus Max Spiritual Health. |
| `ArchDragon.attack` | 0 | Bonus Attack Damage. |
| `ArchDragon.attackSpeed` | 0 | Bonus Attack Speed. |
| `ArchDragon.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `ArchDragon.movementSpeed` | 0 | Bonus Movement Speed. |
| `ArchDragon.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `ArchDragon.epRequirement` | 400,000 |  |
| `ArchDragon.minAura` | 80,000 |  |
| `ArchDragon.maxAura` | 150,000 |  |
| `ArchDragon.minMagicule` | 250,000 |  |
| `ArchDragon.maxMagicule` | 300,000 |  |
| `ArchDragon.size` | 0.5 |  |
| `ArchDragon.maxHealth` | 444 |  |
| `ArchDragon.maxSpiritualHealth` | 888 |  |
| `ArchDragon.attack` | 1.8 |  |
| `ArchDragon.attackSpeed` | 0.1 |  |
| `ArchDragon.knockbackResistance` | 0.35 |  |
| `ArchDragon.movementSpeed` | 0.02 |  |
| `ArchDragon.swimSpeed` | 0.12 |  |
| `ElementDragon.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `ElementDragon.minAura` | 1,000 | Minimal aura. |
| `ElementDragon.maxAura` | 2,000 | Maximum aura. |
| `ElementDragon.minMagicule` | 3,000 | Minimal magicule. |
| `ElementDragon.maxMagicule` | 6,000 | Maximum magicule. |
| `ElementDragon.size` | 0 | Bonus Size. |
| `ElementDragon.maxHealth` | 20 | Bonus Max Health. |
| `ElementDragon.maxSpiritualHealth` | 80 | Bonus Max Spiritual Health. |
| `ElementDragon.attack` | 0 | Bonus Attack Damage. |
| `ElementDragon.attackSpeed` | 0 | Bonus Attack Speed. |
| `ElementDragon.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `ElementDragon.movementSpeed` | 0 | Bonus Movement Speed. |
| `ElementDragon.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `ElementDragon.epRequirement` | 800,000 |  |
| `ElementDragon.essenceRequirement` | 25 | Elemental Essence required to evolve into Element Dragon. |
| `ElementDragon.minAura` | 180,000 |  |
| `ElementDragon.maxAura` | 300,000 |  |
| `ElementDragon.minMagicule` | 350,000 |  |
| `ElementDragon.maxMagicule` | 600,000 |  |
| `ElementDragon.size` | 0.65 |  |
| `ElementDragon.maxHealth` | 777 |  |
| `ElementDragon.maxSpiritualHealth` | 1,000 |  |
| `ElementDragon.attack` | 2.3 |  |
| `ElementDragon.attackSpeed` | 0.2 |  |
| `ElementDragon.knockbackResistance` | 0.45 |  |
| `ElementDragon.movementSpeed` | 0.025 |  |
| `ElementDragon.swimSpeed` | 0.15 |  |
| `DeathDragon.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `DeathDragon.minAura` | 1,000 | Minimal aura. |
| `DeathDragon.maxAura` | 2,000 | Maximum aura. |
| `DeathDragon.minMagicule` | 3,000 | Minimal magicule. |
| `DeathDragon.maxMagicule` | 6,000 | Maximum magicule. |
| `DeathDragon.size` | 0 | Bonus Size. |
| `DeathDragon.maxHealth` | 20 | Bonus Max Health. |
| `DeathDragon.maxSpiritualHealth` | 80 | Bonus Max Spiritual Health. |
| `DeathDragon.attack` | 0 | Bonus Attack Damage. |
| `DeathDragon.attackSpeed` | 0 | Bonus Attack Speed. |
| `DeathDragon.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `DeathDragon.movementSpeed` | 0 | Bonus Movement Speed. |
| `DeathDragon.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `DeathDragon.epRequirement` | 400,000 |  |
| `DeathDragon.minAura` | 90,000 |  |
| `DeathDragon.maxAura` | 180,000 |  |
| `DeathDragon.minMagicule` | 160,000 |  |
| `DeathDragon.maxMagicule` | 320,000 |  |
| `DeathDragon.size` | 0.55 |  |
| `DeathDragon.maxHealth` | 370 |  |
| `DeathDragon.maxSpiritualHealth` | 560 |  |
| `DeathDragon.attack` | 2.2 |  |
| `DeathDragon.attackSpeed` | 0 |  |
| `DeathDragon.knockbackResistance` | 0.5 |  |
| `DeathDragon.movementSpeed` | 0.01 |  |
| `DeathDragon.swimSpeed` | 0 |  |
| `DragonLord.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `DragonLord.minAura` | 1,000 | Minimal aura. |
| `DragonLord.maxAura` | 2,000 | Maximum aura. |
| `DragonLord.minMagicule` | 3,000 | Minimal magicule. |
| `DragonLord.maxMagicule` | 6,000 | Maximum magicule. |
| `DragonLord.size` | 0 | Bonus Size. |
| `DragonLord.maxHealth` | 20 | Bonus Max Health. |
| `DragonLord.maxSpiritualHealth` | 80 | Bonus Max Spiritual Health. |
| `DragonLord.attack` | 0 | Bonus Attack Damage. |
| `DragonLord.attackSpeed` | 0 | Bonus Attack Speed. |
| `DragonLord.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `DragonLord.movementSpeed` | 0 | Bonus Movement Speed. |
| `DragonLord.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `DragonLord.epRequirement` | 800,000 |  |
| `DragonLord.minAura` | 350,000 |  |
| `DragonLord.maxAura` | 600,000 |  |
| `DragonLord.minMagicule` | 700,000 |  |
| `DragonLord.maxMagicule` | 1,200,000 |  |
| `DragonLord.size` | 0.8 |  |
| `DragonLord.maxHealth` | 800 |  |
| `DragonLord.maxSpiritualHealth` | 1,150 |  |
| `DragonLord.attack` | 2.8 |  |
| `DragonLord.attackSpeed` | 0.25 |  |
| `DragonLord.knockbackResistance` | 0.6 |  |
| `DragonLord.movementSpeed` | 0.03 |  |
| `DragonLord.swimSpeed` | 0.2 |  |
| `GehennaDragon.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `GehennaDragon.minAura` | 1,000 | Minimal aura. |
| `GehennaDragon.maxAura` | 2,000 | Maximum aura. |
| `GehennaDragon.minMagicule` | 3,000 | Minimal magicule. |
| `GehennaDragon.maxMagicule` | 6,000 | Maximum magicule. |
| `GehennaDragon.size` | 0 | Bonus Size. |
| `GehennaDragon.maxHealth` | 20 | Bonus Max Health. |
| `GehennaDragon.maxSpiritualHealth` | 80 | Bonus Max Spiritual Health. |
| `GehennaDragon.attack` | 0 | Bonus Attack Damage. |
| `GehennaDragon.attackSpeed` | 0 | Bonus Attack Speed. |
| `GehennaDragon.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `GehennaDragon.movementSpeed` | 0 | Bonus Movement Speed. |
| `GehennaDragon.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `GehennaDragon.epRequirement` | 800,000 |  |
| `GehennaDragon.minAura` | 380,000 |  |
| `GehennaDragon.maxAura` | 680,000 |  |
| `GehennaDragon.minMagicule` | 700,000 |  |
| `GehennaDragon.maxMagicule` | 1,300,000 |  |
| `GehennaDragon.size` | 0.85 |  |
| `GehennaDragon.maxHealth` | 740 |  |
| `GehennaDragon.maxSpiritualHealth` | 2,520 |  |
| `GehennaDragon.attack` | 3 |  |
| `GehennaDragon.attackSpeed` | 0.1 |  |
| `GehennaDragon.knockbackResistance` | 0.7 |  |
| `GehennaDragon.movementSpeed` | 0.02 |  |
| `GehennaDragon.swimSpeed` | 0.05 |  |
| `DivineDragonLord.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `DivineDragonLord.minAura` | 1,000 | Minimal aura. |
| `DivineDragonLord.maxAura` | 2,000 | Maximum aura. |
| `DivineDragonLord.minMagicule` | 3,000 | Minimal magicule. |
| `DivineDragonLord.maxMagicule` | 6,000 | Maximum magicule. |
| `DivineDragonLord.size` | 0 | Bonus Size. |
| `DivineDragonLord.maxHealth` | 20 | Bonus Max Health. |
| `DivineDragonLord.maxSpiritualHealth` | 80 | Bonus Max Spiritual Health. |
| `DivineDragonLord.attack` | 0 | Bonus Attack Damage. |
| `DivineDragonLord.attackSpeed` | 0 | Bonus Attack Speed. |
| `DivineDragonLord.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `DivineDragonLord.movementSpeed` | 0 | Bonus Movement Speed. |
| `DivineDragonLord.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `DivineDragonLord.epRequirement` | 2,000,000 |  |
| `DivineDragonLord.minAura` | 800,000 |  |
| `DivineDragonLord.maxAura` | 1,500,000 |  |
| `DivineDragonLord.minMagicule` | 1,500,000 |  |
| `DivineDragonLord.maxMagicule` | 3,000,000 |  |
| `DivineDragonLord.size` | 1 |  |
| `DivineDragonLord.maxHealth` | 990 |  |
| `DivineDragonLord.maxSpiritualHealth` | 8,100 |  |
| `DivineDragonLord.attack` | 3.5 |  |
| `DivineDragonLord.attackSpeed` | 0.35 |  |
| `DivineDragonLord.knockbackResistance` | 0.8 |  |
| `DivineDragonLord.movementSpeed` | 0.035 |  |
| `DivineDragonLord.swimSpeed` | 0.25 |  |
| `DivineGehennaDragon.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `DivineGehennaDragon.minAura` | 1,000 | Minimal aura. |
| `DivineGehennaDragon.maxAura` | 2,000 | Maximum aura. |
| `DivineGehennaDragon.minMagicule` | 3,000 | Minimal magicule. |
| `DivineGehennaDragon.maxMagicule` | 6,000 | Maximum magicule. |
| `DivineGehennaDragon.size` | 0 | Bonus Size. |
| `DivineGehennaDragon.maxHealth` | 20 | Bonus Max Health. |
| `DivineGehennaDragon.maxSpiritualHealth` | 80 | Bonus Max Spiritual Health. |
| `DivineGehennaDragon.attack` | 0 | Bonus Attack Damage. |
| `DivineGehennaDragon.attackSpeed` | 0 | Bonus Attack Speed. |
| `DivineGehennaDragon.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `DivineGehennaDragon.movementSpeed` | 0 | Bonus Movement Speed. |
| `DivineGehennaDragon.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `DivineGehennaDragon.epRequirement` | 2,100,000 |  |
| `DivineGehennaDragon.minAura` | 900,000 |  |
| `DivineGehennaDragon.maxAura` | 1,700,000 |  |
| `DivineGehennaDragon.minMagicule` | 1,700,000 |  |
| `DivineGehennaDragon.maxMagicule` | 3,200,000 |  |
| `DivineGehennaDragon.size` | 1.05 |  |
| `DivineGehennaDragon.maxHealth` | 900 |  |
| `DivineGehennaDragon.maxSpiritualHealth` | 7,850 |  |
| `DivineGehennaDragon.attack` | 3.8 |  |
| `DivineGehennaDragon.attackSpeed` | 0.2 |  |
| `DivineGehennaDragon.knockbackResistance` | 0.9 |  |
| `DivineGehennaDragon.movementSpeed` | 0.03 |  |
| `DivineGehennaDragon.swimSpeed` | 0.1 |  |

## Tags

`tensura:races/divine`, `tensura:races/has_creative_flight`
