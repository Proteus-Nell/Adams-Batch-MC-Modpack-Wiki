# Demon Knight

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:demon_knight` |
| **Difficulty** | Intermediate |
| **Alignment** | Majin |
| **Aura** | 45,000 - 95,000 |
| **Magicule** | 60,000 - 120,000 |
| **Health bonus** | 700 |
| **Spiritual health bonus** | 4,800 |
| **Attack damage bonus** | 5.9 |
| **Movement speed bonus** | 0.015 |
| **EP to evolve into** | 150,000 |

</div>

## Evolution

- **Evolves from:** [High-Class Demon](high-class-demon.md)
- **Evolves into:** [Knight of Black](knight-black.md)
- **Default evolution:** [Knight of Black](knight-black.md)
- **On awakening (True Demon Lord / True Hero):** [Knight of Black](knight-black.md)
- **During the Harvest Festival:** [Knight of Black](knight-black.md)

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

- ![](../../assets/icons/tensura/skill/darkness_attack_nullification.png) [Darkness Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/darkness-attack-nullification.md)

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

Set in [`config/nightmare/race/demon_clan_config.toml`](../configs/config-nightmare-race-demon-clan-config.md).

| Option | Default | Description |
|---|---|---|
| `DemonKnight.epRequirement` | 150,000 | EP required to evolve from High Class Demon into Demon Knight (EvolutionRequirement.EPRequirement). |
| `DemonKnight.essenceRequirement` | 30 | Soul Essence required to evolve from High Class Demon into Demon Knight (EvolutionRequirement.ItemConsumeRequirement). |
| `DemonKnight.minAura` | 45,000 | Minimal aura. |
| `DemonKnight.maxAura` | 95,000 | Maximum aura. |
| `DemonKnight.minMagicule` | 60,000 | Minimal magicule. |
| `DemonKnight.maxMagicule` | 120,000 | Maximum magicule. |
| `DemonKnight.size` | 0.05 | Bonus Size. |
| `DemonKnight.maxHealth` | 700 | Bonus Max Health. |
| `DemonKnight.maxSpiritualHealth` | 4,800 | Bonus Max Spiritual Health. |
| `DemonKnight.attack` | 5.9 | Bonus Attack Damage. |
| `DemonKnight.attackSpeed` | 0.05 | Bonus Attack Speed. |
| `DemonKnight.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `DemonKnight.movementSpeed` | 0.015 | Bonus Movement Speed. |
| `DemonKnight.swimSpeed` | 0.03 | Bonus Swimming Speed Multiplier. |
| `DemonKnight.intrinsicPool` | [] (empty) | Intrinsic pool (if used). |
| `DemonKnight.intrinsicCount` | 0 | Intrinsic count (if used). |
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
