# Empty

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:empty` |
| **Difficulty** | Intermediate |
| **Alignment** | Majin |
| **Aura** | 200,000 - 200,000 |
| **Magicule** | 200,000 - 200,000 |
| **Health bonus** | 160 |
| **Spiritual health bonus** | 2,240 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0.01 |
| **EP to evolve into** | 200,000 |

</div>

> A Remnant that chose the hard way out. Instead of accepting their forgotten past, they chose to fight it, to no avail. A greater, emptier husk awaits.

## Evolution

- **Evolves from:** [Remnant](remnant.md)
- **Evolves into:** [Revenant](revenant.md)
- **Default evolution:** [Revenant](revenant.md)
- **On awakening (True Demon Lord / True Hero):** [Revenant](revenant.md)

### Requirements to evolve into Empty

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 200,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Ascended"]
  r1["Divine Excelsius"]
  r2["Divine Inferius"]
  r3["Empty"]
  r4["Forgotten"]
  r5["Remnant"]
  r6["Revenant"]
  r7["Whole"]
  r0 --> r1
  r3 --> r6
  r4 --> r5
  r4 --> r6
  r5 --> r3
  r5 --> r6
  r5 --> r7
  r6 --> r2
  r7 --> r0
```

## Traits

- Spawns as a spiritual lifeform
- Spiritual lifeform

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 160 | add |
| Max Spiritual Health | 2,240 | add |
| Attack Damage | 0 | add |
| Attack Speed | 0.1 | add |
| Knockback Resistance | 1 | add |
| Movement Speed | 0.01 | add |
| Swim Speed Multiplier | 0.01 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/forgotten_config.toml`](../configs/config-mysticism-race-forgotten-config.md).

| Option | Default | Description |
|---|---|---|
| `Empty.epRequirement` | 200,000 | EP requirement to evolve into an Empty. |
| `Empty.minAura` | 200,000 | Minimal aura. |
| `Empty.maxAura` | 200,000 | Maximum aura. |
| `Empty.minMagicule` | 200,000 | Minimal magicule. |
| `Empty.maxMagicule` | 200,000 | Maximum magicule. |
| `Empty.size` | 0 | Bonus Size. |
| `Empty.maxHealth` | 160 | Bonus Max Health. |
| `Empty.maxSpiritualHealth` | 2,240 | Bonus Max Spiritual Health. |
| `Empty.attack` | 0 | Bonus Attack Damage. |
| `Empty.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `Empty.knockbackResistance` | 1 | Bonus Knockback Resistance. |
| `Empty.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `Empty.swimSpeed` | 0.01 | Bonus Swimming Speed Multiplier. |
| `Empty.intrinsicSkills` | "tensura:spiritual_attack_resistance", "tensura:possession", "mysticism:relapse" | The list of intrinsic skills that the race gets. |
| `Remnant.epRequirement` | 100,000 | EP requirement to evolve into a Remnant. |
| `Remnant.minAura` | 50,000 | Minimal aura. |
| `Remnant.maxAura` | 50,000 | Maximum aura. |
| `Remnant.minMagicule` | 60,000 | Minimal magicule. |
| `Remnant.maxMagicule` | 60,000 | Maximum magicule. |
| `Remnant.size` | 0 | Bonus Size. |
| `Remnant.maxHealth` | 60 | Bonus Max Health. |
| `Remnant.maxSpiritualHealth` | 1,040 | Bonus Max Spiritual Health. |
| `Remnant.attack` | -0.5 | Bonus Attack Damage. |
| `Remnant.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `Remnant.knockbackResistance` | 1 | Bonus Knockback Resistance. |
| `Remnant.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `Remnant.swimSpeed` | 0.01 | Bonus Swimming Speed Multiplier. |
| `Remnant.intrinsicSkills` | "tensura:spiritual_attack_resistance", "tensura:possession", "mysticism:relapse" | The list of intrinsic skills that the race gets. |
| `Forgotten.minAura` | 100 | Minimal aura. |
| `Forgotten.maxAura` | 600 | Maximum aura. |
| `Forgotten.minMagicule` | 425 | Minimal magicule. |
| `Forgotten.maxMagicule` | 700 | Maximum magicule. |
| `Forgotten.size` | 0 | Bonus Size. |
| `Forgotten.maxHealth` | 0 | Bonus Max Health. |
| `Forgotten.maxSpiritualHealth` | 0 | Bonus Max Spiritual Health. |
| `Forgotten.attack` | -1 | Bonus Attack Damage. |
| `Forgotten.attackSpeed` | 0 | Bonus Attack Speed. |
| `Forgotten.knockbackResistance` | 1 | Bonus Knockback Resistance. |
| `Forgotten.movementSpeed` | 0 | Bonus Movement Speed. |
| `Forgotten.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `Forgotten.intrinsicSkills` | "tensura:spiritual_attack_resistance", "tensura:possession", "mysticism:relapse" | The list of intrinsic skills that the race gets. |

## Tags

`tensura:races/spawn_as_spiritual`, `tensura:races/spiritual`
