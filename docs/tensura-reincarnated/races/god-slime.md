# God Slime

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:god_slime` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 1,000,000 - 1,000,000 |
| **Magicule** | 1,000,000 - 1,000,000 |
| **Health bonus** | 1,000 |
| **Spiritual health bonus** | 6,400 |
| **Attack damage bonus** | 4 |
| **Movement speed bonus** | 0.07 |
| **EP to evolve into** | 2,000,000 |

</div>

> The divine stage of evolution of Slimes.

## Evolution

- **Evolves from:** [Demon Slime](demon-slime.md)

### Requirements to evolve into God Slime

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 2,000,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Demon Slime"]
  r1["God Slime"]
  r2["Metal Slime"]
  r3["Slime"]
  r0 --> r1
  r2 --> r0
  r3 --> r0
  r3 --> r2
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/divine_ki_release.png) [Divine Ki Release](../abilities/intrinsic-skills/divine-ki-release.md)
- ![](../../assets/icons/tensura/skill/possession.png) [Possession](../abilities/intrinsic-skills/possession.md)
- ![](../../assets/icons/tensura/skill/infinite_regeneration.png) [Infinite Regeneration](../abilities/extra-skills/infinite-regeneration.md)
- ![](../../assets/icons/tensura/skill/universal_perception.png) [Universal Perception](../abilities/extra-skills/universal-perception.md)
- ![](../../assets/icons/tensura/skill/physical_attack_nullification.png) [Physical Attack Nullification](../abilities/resistance-skills/physical-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/magic_resistance.png) [Magic Resistance](../abilities/resistance-skills/magic-resistance.md)
- ![](../../assets/icons/tensura/skill/spiritual_attack_resistance.png) [Spiritual Attack Resistance](../abilities/resistance-skills/spiritual-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/cold_resistance.png) [Cold Resistance](../abilities/resistance-skills/cold-resistance.md)
- ![](../../assets/icons/tensura/skill/corrosion_resistance.png) [Corrosion Resistance](../abilities/resistance-skills/corrosion-resistance.md)
- ![](../../assets/icons/tensura/skill/darkness_attack_resistance.png) [Darkness Attack Resistance](../abilities/resistance-skills/darkness-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/earth_attack_resistance.png) [Earth Attack Resistance](../abilities/resistance-skills/earth-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/electricity_resistance.png) [Electricity Resistance](../abilities/resistance-skills/electricity-resistance.md)
- ![](../../assets/icons/tensura/skill/gravity_attack_resistance.png) [Gravity Attack Resistance](../abilities/resistance-skills/gravity-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/heat_resistance.png) [Heat Resistance](../abilities/resistance-skills/heat-resistance.md)
- ![](../../assets/icons/tensura/skill/light_attack_resistance.png) [Light Attack Resistance](../abilities/resistance-skills/light-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/spatial_attack_resistance.png) [Spatial Attack Resistance](../abilities/resistance-skills/spatial-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/water_attack_resistance.png) [Water Attack Resistance](../abilities/resistance-skills/water-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/wind_attack_resistance.png) [Wind Attack Resistance](../abilities/resistance-skills/wind-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/absorb_and_dissolve.png) [Absorb &amp; Dissolve](../abilities/intrinsic-skills/absorb-and-dissolve.md)

## Traits

- Cold-blooded
- Divine
- Slime

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Jump Strength | 0.7 | add |
| Safe Fall Distance | 1.4 | add x base |
| Fall Damage Multiplier | -1 | add |
| Width Multiplier | 3 | add |
| Jump Strength | 0.6 | add |
| Safe Fall Distance | 1.2 | add x base |
| Fall Damage Multiplier | -0.75 | add |
| Jump Strength | 0.4 | add |
| Safe Fall Distance | 0.8 | add x base |
| Fall Damage Multiplier | -0.5 | add |
| Scale | -0.675 | add |
| Max Health | 1,000 | add |
| Max Spiritual Health | 6,400 | add |
| Attack Damage | 4 | add |
| Attack Speed | 0.7 | add |
| Knockback Resistance | 0.7 | add |
| Movement Speed | 0.07 | add |
| Swim Speed Multiplier | 0.7 | add |

## Stats (config defaults)

Set in [`config/tensura/race/slime_config.toml`](../configs/config-tensura-race-slime-config.md).

| Option | Default | Description |
|---|---|---|
| `GodSlime.epRequirement` | 2,000,000 | EP requirement to evolve into God Slime. |
| `GodSlime.minAura` | 1,000,000 | Minimal aura. |
| `GodSlime.maxAura` | 1,000,000 | Maximum aura. |
| `GodSlime.minMagicule` | 1,000,000 | Minimal magicule. |
| `GodSlime.maxMagicule` | 1,000,000 | Maximum magicule. |
| `GodSlime.size` | -0.675 | Bonus Size. |
| `GodSlime.maxHealth` | 1,000 | Bonus Max Health. |
| `GodSlime.maxSpiritualHealth` | 6,400 | Bonus Max Spiritual Health. |
| `GodSlime.attack` | 4 | Bonus Attack Damage. |
| `GodSlime.attackSpeed` | 0.7 | Bonus Attack Speed. |
| `GodSlime.knockbackResistance` | 0.7 | Bonus Knockback Resistance. |
| `GodSlime.movementSpeed` | 0.07 | Bonus Movement Speed. |
| `GodSlime.swimSpeed` | 0.7 | Bonus Swimming Speed Multiplier. |
| `GodSlime.jumpStrength` | 0.7 | Bonus Jump Strength. |
| `GodSlime.fallDamage` | -1 | Fall Damage Multiplier. |
| `GodSlime.maxChargeTick` | 80 | Get Max Jump Charge tick. |
| `GodSlime.width` | 4 | Hitbox width multiplier. |
| `DemonSlime.minAura` | 400,000 | Minimal aura. |
| `DemonSlime.maxAura` | 400,000 | Maximum aura. |
| `DemonSlime.minMagicule` | 400,000 | Minimal magicule. |
| `DemonSlime.maxMagicule` | 400,000 | Maximum magicule. |
| `DemonSlime.size` | -0.675 | Bonus Size. |
| `DemonSlime.maxHealth` | 500 | Bonus Max Health. |
| `DemonSlime.maxSpiritualHealth` | 3,100 | Bonus Max Spiritual Health. |
| `DemonSlime.attack` | 2 | Bonus Attack Damage. |
| `DemonSlime.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `DemonSlime.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `DemonSlime.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `DemonSlime.swimSpeed` | 0.3 | Bonus Swimming Speed Multiplier. |
| `DemonSlime.jumpStrength` | 0.6 | Bonus Jump Strength. |
| `DemonSlime.fallDamage` | -0.75 | Fall Damage Multiplier. |
| `DemonSlime.maxChargeTick` | 60 | Get Max Jump Charge tick. |
| `DemonSlime.width` | 4 | Hitbox width multiplier. |
| `Slime.minAura` | 200 | Minimal aura. |
| `Slime.maxAura` | 500 | Maximum aura. |
| `Slime.minMagicule` | 200 | Minimal magicule. |
| `Slime.maxMagicule` | 500 | Maximum magicule. |
| `Slime.size` | -0.75 | Bonus Size. |
| `Slime.maxHealth` | -10 | Bonus Max Health. |
| `Slime.maxSpiritualHealth` | 15 | Bonus Max Spiritual Health. |
| `Slime.attack` | -0.7 | Bonus Attack Damage. |
| `Slime.attackSpeed` | 0 | Bonus Attack Speed. |
| `Slime.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Slime.movementSpeed` | -0.03 | Bonus Movement Speed. |
| `Slime.swimSpeed` | -0.3 | Bonus Swimming Speed Multiplier. |
| `Slime.jumpStrength` | 0.4 | Bonus Jump Strength. |
| `Slime.fallDamage` | -0.5 | Fall Damage Multiplier. |
| `Slime.maxChargeTick` | 40 | Get Max Jump Charge tick. |
| `Slime.width` | 4 | Hitbox width multiplier. |
| `physicalInput` | 0.5 | The physical damage input multiplier taken by this race. |

## Tags

`tensura:races/cold_blooded`, `tensura:races/divine`, `tensura:races/slime`
