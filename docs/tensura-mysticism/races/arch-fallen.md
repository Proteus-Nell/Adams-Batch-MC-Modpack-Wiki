# Arch Fallen

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:arch_fallen` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 70,000 - 75,000 |
| **Magicule** | 120,000 - 145,000 |
| **Health bonus** | 110 |
| **Spiritual health bonus** | 600 |
| **Attack damage bonus** | 2.3 |
| **Movement speed bonus** | 0.01 |
| **EP to evolve into** | 140,000 |

</div>

> An arch angel that got corrupted by magicules, then chose to abandon the light for the darkness.

## Evolution

- **Evolves from:** [Greater Fallen](greater-fallen.md)
- **Evolves into:** [Fallen Lord](fallen-lord.md)
- **Default evolution:** [Fallen Lord](fallen-lord.md)
- **On awakening (True Demon Lord / True Hero):** [Fallen Lord](fallen-lord.md)

### Requirements to evolve into Arch Fallen

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 140,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Arch Fallen"]
  r1["Fallen"]
  r2["Fallen Lord"]
  r3["Greater Fallen"]
  r4["Lesser Fallen"]
  r0 --> r2
  r2 --> r1
  r3 --> r0
  r3 --> r2
  r4 --> r2
  r4 --> r3
```

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 110 | add |
| Max Spiritual Health | 600 | add |
| Attack Damage | 2.3 | add |
| Attack Speed | 0.4 | add |
| Knockback Resistance | 0.4 | add |
| Movement Speed | 0.01 | add |
| Swim Speed Multiplier | 0.1 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/angel_config.toml`](../configs/config-mysticism-race-angel-config.md).

| Option | Default | Description |
|---|---|---|
| `ArchFallen.epRequirement` | 140,000 | EP requirement to evolve into a Fallen Arch Angel. |
| `ArchFallen.minAura` | 70,000 | Minimal aura. |
| `ArchFallen.maxAura` | 75,000 | Maximum aura. |
| `ArchFallen.minMagicule` | 120,000 | Minimal magicule. |
| `ArchFallen.maxMagicule` | 145,000 | Maximum magicule. |
| `ArchFallen.size` | 0 | Bonus Size. |
| `ArchFallen.maxHealth` | 110 | Bonus Max Health. |
| `ArchFallen.maxSpiritualHealth` | 600 | Bonus Max Spiritual Health. |
| `ArchFallen.attack` | 2.3 | Bonus Attack Damage. |
| `ArchFallen.attackSpeed` | 0.4 | Bonus Attack Speed. |
| `ArchFallen.knockbackResistance` | 0.4 | Bonus Knockback Resistance. |
| `ArchFallen.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `ArchFallen.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
| `ArchFallen.intrinsicSkills` | "tensura:magic_resistance", "mysticism:darkness_manipulation", "tensura:physical_attack_resistance" | The list of intrinsic skills that the race gets. |
| `GreaterFallen.epRequirement` | 20,000 | EP requirement to evolve into Fallen Greater Angel. |
| `GreaterFallen.minAura` | 25,000 | Minimal aura. |
| `GreaterFallen.maxAura` | 30,000 | Maximum aura. |
| `GreaterFallen.minMagicule` | 40,000 | Minimal magicule. |
| `GreaterFallen.maxMagicule` | 55,000 | Maximum magicule. |
| `GreaterFallen.size` | 0 | Bonus Size. |
| `GreaterFallen.maxHealth` | 80 | Bonus Max Health. |
| `GreaterFallen.maxSpiritualHealth` | 220 | Bonus Max Spiritual Health. |
| `GreaterFallen.attack` | 1.2 | Bonus Attack Damage. |
| `GreaterFallen.attackSpeed` | 0.2 | Bonus Attack Speed. |
| `GreaterFallen.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `GreaterFallen.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `GreaterFallen.swimSpeed` | 0.2 | Bonus Swimming Speed Multiplier. |
| `GreaterFallen.intrinsicSkills` | "tensura:magic_resistance", "mysticism:darkness_manipulation" | The list of intrinsic skills that the race gets. |
| `LesserFallen.minAura` | 4,500 | Minimal aura. |
| `LesserFallen.maxAura` | 5,500 | Maximum aura. |
| `LesserFallen.minMagicule` | 7,500 | Minimal magicule. |
| `LesserFallen.maxMagicule` | 9,500 | Maximum magicule. |
| `LesserFallen.size` | 0 | Bonus Size. |
| `LesserFallen.maxHealth` | 30 | Bonus Max Health. |
| `LesserFallen.maxSpiritualHealth` | 100 | Bonus Max Spiritual Health. |
| `LesserFallen.attack` | 0.5 | Bonus Attack Damage. |
| `LesserFallen.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `LesserFallen.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `LesserFallen.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `LesserFallen.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `LesserFallen.intrinsicSkills` | "tensura:magic_resistance", "mysticism:darkness_manipulation" | The list of intrinsic skills that the race gets. |
