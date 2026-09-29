# Demon Prince

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:demon_prince` |
| **Difficulty** | Intermediate |
| **Alignment** | Majin |
| **Aura** | 350,000 - 700,000 |
| **Magicule** | 450,000 - 850,000 |
| **Health bonus** | 1,200 |
| **Spiritual health bonus** | 6,650 |
| **Attack damage bonus** | 1.65 |
| **Movement speed bonus** | 0.03 |
| **EP to evolve into** | 600,000 |

</div>

## Evolution

- **Evolves from:** [Royal Demon](royal-demon.md)

### Requirements to evolve into Demon Prince

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 600,000 | 50% |
| Consume 150 of [Soul Essence](../items/materials/soul-essence.md) | 50% |

### Evolution tree

```mermaid
flowchart LR
  r0["Demon Knight"]
  r1["Demon Prince"]
  r2["Hell Rizer"]
  r3["High-Class Demon"]
  r4["Knight of Black"]
  r5["Lower-Class Demon"]
  r6["Middle-Class Demon"]
  r7["Royal Demon"]
  r8["Ten Commandment"]
  r0 --> r4
  r3 --> r0
  r3 --> r2
  r3 --> r7
  r3 --> r8
  r5 --> r3
  r5 --> r6
  r6 --> r3
  r7 --> r1
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/electricity_nullification.png) [Electricity Nullification](../../tensura-reincarnated/abilities/resistance-skills/electricity-nullification.md)
- ![](../../assets/icons/tensura/skill/spiritual_attack_nullification.png) [Spiritual Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/spiritual-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/gravity_attack_nullification.png) [Gravity Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/gravity-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/magic_nullification.png) [Magic Nullification](../../tensura-reincarnated/abilities/resistance-skills/magic-nullification.md)
- ![](../../assets/icons/tensura/skill/magic_darkness_transform.png) [Magic Darkness Transform](../../tensura-reincarnated/abilities/extra-skills/magic-darkness-transform.md)
- ![](../../assets/icons/trnightmare/skill/dark_magic_release.png) [Dark Magic Release](../abilities/intrinsic-skills/dark-magic-release.md)

## Traits

- Divine

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 1,200 | add |
| Max Spiritual Health | 6,650 | add |
| Attack Damage | 1.65 | add |
| Attack Speed | 0.18 | add |
| Knockback Resistance | 0.36 | add |
| Movement Speed | 0.03 | add |
| Swim Speed Multiplier | 0.07 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/demon_clan_config.toml`](../configs/config-nightmare-race-demon-clan-config.md).

| Option | Default | Description |
|---|---|---|
| `DemonPrince.epRequirement` | 600,000 | EP required to evolve into Demon Prince (EvolutionRequirement.EPRequirement). |
| `DemonPrince.essenceRequirement` | 150 | Soul Essence required to evolve into Demon Prince (EvolutionRequirement.ItemConsumeRequirement). |
| `DemonPrince.minAura` | 350,000 | Minimal aura. |
| `DemonPrince.maxAura` | 700,000 | Maximum aura. |
| `DemonPrince.minMagicule` | 450,000 | Minimal magicule. |
| `DemonPrince.maxMagicule` | 850,000 | Maximum magicule. |
| `DemonPrince.size` | 0 | Bonus Size. |
| `DemonPrince.maxHealth` | 1,200 | Bonus Max Health. |
| `DemonPrince.maxSpiritualHealth` | 6,650 | Bonus Max Spiritual Health. |
| `DemonPrince.attack` | 1.65 | Bonus Attack Damage. |
| `DemonPrince.attackSpeed` | 0.18 | Bonus Attack Speed. |
| `DemonPrince.knockbackResistance` | 0.36 | Bonus Knockback Resistance. |
| `DemonPrince.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `DemonPrince.swimSpeed` | 0.07 | Bonus Swimming Speed Multiplier. |
| `DemonPrince.intrinsicPool` | [] (empty) | Intrinsic pool (if used). |
| `DemonPrince.intrinsicCount` | 0 | Intrinsic count (if used). |
| `RoyalDemon.epRequirement` | 400,000 | EP required to evolve into Royal Demon (EvolutionRequirement.EPRequirement). |
| `RoyalDemon.essenceRequirement` | 90 | Soul Essence required to evolve into Royal Demon (EvolutionRequirement.ItemConsumeRequirement). |
| `RoyalDemon.minAura` | 200,000 | Minimal aura. |
| `RoyalDemon.maxAura` | 450,000 | Maximum aura. |
| `RoyalDemon.minMagicule` | 280,000 | Minimal magicule. |
| `RoyalDemon.maxMagicule` | 520,000 | Maximum magicule. |
| `RoyalDemon.size` | 0 | Bonus Size. |
| `RoyalDemon.maxHealth` | 850 | Bonus Max Health. |
| `RoyalDemon.maxSpiritualHealth` | 4,520 | Bonus Max Spiritual Health. |
| `RoyalDemon.attack` | 1.4 | Bonus Attack Damage. |
| `RoyalDemon.attackSpeed` | 0.15 | Bonus Attack Speed. |
| `RoyalDemon.knockbackResistance` | 0.32 | Bonus Knockback Resistance. |
| `RoyalDemon.movementSpeed` | 0.025 | Bonus Movement Speed. |
| `RoyalDemon.swimSpeed` | 0.06 | Bonus Swimming Speed Multiplier. |
| `RoyalDemon.intrinsicPool` | [] (empty) | Intrinsic pool (if used). |
| `RoyalDemon.intrinsicCount` | 0 | Intrinsic count (if used). |
| `HighClassDemon.epRequirement` | 80,000 | EP required to evolve from Mid Class Demon into High Class Demon (EvolutionRequirement.EPRequirement). |
| `HighClassDemon.essenceRequirement` | 15 | Soul Essence required to evolve from Mid Class Demon into High Class Demon (EvolutionRequirement.ItemConsumeRequirement). |
| `HighClassDemon.minAura` | 18,000 | Minimal aura. |
| `HighClassDemon.maxAura` | 40,000 | Maximum aura. |
| `HighClassDemon.minMagicule` | 28,000 | Minimal magicule. |
| `HighClassDemon.maxMagicule` | 55,000 | Maximum magicule. |
| `HighClassDemon.size` | 0.05 | Bonus Size. |
| `HighClassDemon.maxHealth` | 45 | Bonus Max Health. |
| `HighClassDemon.maxSpiritualHealth` | 200 | Bonus Max Spiritual Health. |
| `HighClassDemon.attack` | 0.65 | Bonus Attack Damage. |
| `HighClassDemon.attackSpeed` | 0 | Bonus Attack Speed. |
| `HighClassDemon.knockbackResistance` | 0.15 | Bonus Knockback Resistance. |
| `HighClassDemon.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `HighClassDemon.swimSpeed` | 0.02 | Bonus Swimming Speed Multiplier. |
| `HighClassDemon.intrinsicPool` | "tensura:infinite_regeneration", "tensura:black_flame", "tensura:universal_perception" | Intrinsic pool (if used). |
| `HighClassDemon.intrinsicCount` | 0 | Intrinsic count (if used). |
| `MidClassDemon.epRequirement` | 45,000 | EP required to evolve from Lower Class Demon into Mid Class Demon (EvolutionRequirement.EPRequirement). |
| `MidClassDemon.essenceRequirement` | 10 | Soul Essence required to evolve from Lower Class Demon into Mid Class Demon (EvolutionRequirement.ItemConsumeRequirement). |
| `MidClassDemon.minAura` | 6,000 | Minimal aura. |
| `MidClassDemon.maxAura` | 14,000 | Maximum aura. |
| `MidClassDemon.minMagicule` | 10,000 | Minimal magicule. |
| `MidClassDemon.maxMagicule` | 22,000 | Maximum magicule. |
| `MidClassDemon.size` | 0.08 | Bonus Size. |
| `MidClassDemon.maxHealth` | 28 | Bonus Max Health. |
| `MidClassDemon.maxSpiritualHealth` | 130 | Bonus Max Spiritual Health. |
| `MidClassDemon.attack` | 0.45 | Bonus Attack Damage. |
| `MidClassDemon.attackSpeed` | -0.1 | Bonus Attack Speed. |
| `MidClassDemon.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `MidClassDemon.movementSpeed` | 0 | Bonus Movement Speed. |
| `MidClassDemon.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `MidClassDemon.intrinsicPool` | "tensura:ultraspeed_regeneration" | Intrinsic pool (if used). |
| `MidClassDemon.intrinsicCount` | 0 | Intrinsic count (if used). |
| `LowerClassDemon.minAura` | 2,000 | Minimal aura. |
| `LowerClassDemon.maxAura` | 6,000 | Maximum aura. |
| `LowerClassDemon.minMagicule` | 4,000 | Minimal magicule. |
| `LowerClassDemon.maxMagicule` | 9,000 | Maximum magicule. |
| `LowerClassDemon.size` | 0.1 | Bonus Size. |
| `LowerClassDemon.maxHealth` | 12 | Bonus Max Health. |
| `LowerClassDemon.maxSpiritualHealth` | 70 | Bonus Max Spiritual Health. |
| `LowerClassDemon.attack` | 0.25 | Bonus Attack Damage. |
| `LowerClassDemon.attackSpeed` | -0.2 | Bonus Attack Speed. |
| `LowerClassDemon.knockbackResistance` | 0.05 | Bonus Knockback Resistance. |
| `LowerClassDemon.movementSpeed` | 0 | Bonus Movement Speed. |
| `LowerClassDemon.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `LowerClassDemon.intrinsicPool` | "tensura:self_regeneration", "tensura:magic_sense", "tensura:flame_manipulation" | List of intrinsic skills Lower Class Demon can randomly receive. |
| `LowerClassDemon.intrinsicCount` | 0 | How many intrinsic skills are rolled from the pool (if used). |

## Tags

`tensura:races/divine`
