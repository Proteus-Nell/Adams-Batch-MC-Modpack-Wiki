# Magma Worm

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:magma_worm` |
| **Difficulty** | Extreme |
| **Alignment** | Majin |
| **Aura** | 75,000 - 75,000 |
| **Magicule** | 75,000 - 75,000 |
| **Health bonus** | 100 |
| **Spiritual health bonus** | 300 |
| **Attack damage bonus** | 2 |
| **Movement speed bonus** | 0.02 |
| **EP to evolve into** | 100,000 |

</div>

> "And his brother loved worms..." A powerful evolved variant of the sculk worm, gaining a long, worm-like appendage.

## Evolution

- **Evolves from:** [Molten Perforator](molten-perforator.md)
- **Evolves into:** [Enflamed Aberration](enflamed-aberration.md)
- **Default evolution:** [Enflamed Aberration](enflamed-aberration.md)
- **On awakening (True Demon Lord / True Hero):** [Enflamed Aberration](enflamed-aberration.md)

### Requirements to evolve into Magma Worm

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 100,000 | 50% |
| Consume 10 of [Flame Essence](../items/materials/flame-essence.md) | 50% |

### Evolution tree

```mermaid
flowchart LR
  r0["Charged Perforator"]
  r1["Dissonance Deity"]
  r2["Enflamed Aberration"]
  r3["Lightning Aberration"]
  r4["Magma Worm"]
  r5["Molten Perforator"]
  r6["Overloading Worm"]
  r7["Reaper Aberration"]
  r8["Sculk Worm"]
  r9["Soul Aberration"]
  r10["Soul Shrieker"]
  r11["Violence Deity"]
  r12["Warden"]
  r0 --> r3
  r0 --> r6
  r2 --> r11
  r3 --> r1
  r4 --> r2
  r5 --> r2
  r5 --> r4
  r6 --> r3
  r8 --> r0
  r8 --> r5
  r8 --> r9
  r8 --> r10
  r9 --> r7
  r9 --> r12
  r10 --> r9
  r10 --> r12
  r12 --> r9
```

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0.5 | add |
| Max Health | 100 | add |
| Max Spiritual Health | 300 | add |
| Attack Damage | 2 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0.4 | add |
| Movement Speed | 0.02 | add |
| Swim Speed Multiplier | 0.2 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/sculk_config.toml`](../configs/config-mysticism-race-sculk-config.md).

| Option | Default | Description |
|---|---|---|
| `MagmaWorm.essenceRequired` | 10 | Quantity of Flame Essence required to become a Magma Worm as a Molten Perforator. |
| `MagmaWorm.epRequirement` | 100,000 | EP requirement to evolve into Magma Worm. |
| `MagmaWorm.minAura` | 75,000 | Minimal aura. |
| `MagmaWorm.maxAura` | 75,000 | Maximum aura. |
| `MagmaWorm.minMagicule` | 75,000 | Minimal magicule. |
| `MagmaWorm.maxMagicule` | 75,000 | Maximum magicule. |
| `MagmaWorm.size` | 0.5 | Bonus Size. |
| `MagmaWorm.maxHealth` | 100 | Bonus Max Health. |
| `MagmaWorm.maxSpiritualHealth` | 300 | Bonus Max Spiritual Health. |
| `MagmaWorm.attack` | 2 | Bonus Attack Damage. |
| `MagmaWorm.attackSpeed` | 0 | Bonus Attack Speed. |
| `MagmaWorm.knockbackResistance` | 0.4 | Bonus Knockback Resistance. |
| `MagmaWorm.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `MagmaWorm.swimSpeed` | 0.2 | Bonus Swimming Speed Multiplier. |
| `MagmaWorm.intrinsicSkills` | "tensura:sense_soundwave", "tensura:heat_resistance", "tensura:flame_breath" | The list of intrinsic skills that the race gets. |
| `MoltenPerforator.essenceRequired` | 3 | Quantity of Flame Essence required to become a Molten Perforator as a Sculk Worm. |
| `MoltenPerforator.epRequirement` | 4,000 | EP requirement to evolve into Magma Worm. |
| `MoltenPerforator.minAura` | 4,500 | Minimal aura. |
| `MoltenPerforator.maxAura` | 5,500 | Maximum aura. |
| `MoltenPerforator.minMagicule` | 5,500 | Minimal magicule. |
| `MoltenPerforator.maxMagicule` | 7,500 | Maximum magicule. |
| `MoltenPerforator.size` | 0 | Bonus Size. |
| `MoltenPerforator.maxHealth` | 30 | Bonus Max Health. |
| `MoltenPerforator.maxSpiritualHealth` | 90 | Bonus Max Spiritual Health. |
| `MoltenPerforator.attack` | 0.4 | Bonus Attack Damage. |
| `MoltenPerforator.attackSpeed` | 0 | Bonus Attack Speed. |
| `MoltenPerforator.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `MoltenPerforator.movementSpeed` | 0.005 | Bonus Movement Speed. |
| `MoltenPerforator.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `MoltenPerforator.intrinsicSkills` | "tensura:sense_soundwave", "tensura:heat_resistance", "tensura:flame_breath" | The list of intrinsic skills that the race gets. |
| `SculkWorm.minAura` | 100 | Minimal aura. |
| `SculkWorm.maxAura` | 250 | Maximum aura. |
| `SculkWorm.minMagicule` | 800 | Minimal magicule. |
| `SculkWorm.maxMagicule` | 1,200 | Maximum magicule. |
| `SculkWorm.size` | -0.5 | Bonus Size. |
| `SculkWorm.maxHealth` | -12 | Bonus Max Health. |
| `SculkWorm.maxSpiritualHealth` | -4 | Bonus Max Spiritual Health. |
| `SculkWorm.attack` | -0.5 | Bonus Attack Damage. |
| `SculkWorm.attackSpeed` | 3.5 | Bonus Attack Speed. |
| `SculkWorm.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `SculkWorm.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `SculkWorm.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `SculkWorm.intrinsicSkills` | "tensura:sense_soundwave" | The list of intrinsic skills that the race gets. |
