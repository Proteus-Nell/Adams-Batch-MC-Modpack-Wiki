# Revenant

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:revenant` |
| **Difficulty** | Intermediate |
| **Alignment** | Majin |
| **Aura** | 500,000 - 500,000 |
| **Magicule** | 500,000 - 500,000 |
| **Health bonus** | 580 |
| **Spiritual health bonus** | 5,740 |
| **Attack damage bonus** | 4 |
| **Movement speed bonus** | 0.0475 |
| **EP to evolve into** | 800,000 |

</div>

> A husk of what could have been. Revenants carve their way out of the hell they have created for themselves, one soul at a time.

## Evolution

- **Evolves from:** [Empty](empty.md), [Forgotten](forgotten.md), [Remnant](remnant.md)
- **Evolves into:** [Divine Inferius](divine-inferius.md)
- **Default evolution:** [Divine Inferius](divine-inferius.md)

### Requirements to evolve into Revenant

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 800,000 | 60% |
| Slay 1 of f o l g e n. | 5% |
| Slay 1 of k i r a r a  m i z u t a n i. | 5% |
| Slay 1 of k y o y a  t a c h i b a n a. | 5% |
| Slay 1 of m a i  f u r u k i. | 5% |
| Slay 1 of m a r k  l a u r e n. | 5% |
| Slay 1 of s h i n j i  t a n i m u r a. | 5% |
| Slay 1 of s h i n  r y u s e i. | 5% |
| Slay 1 of s h o g o  t a g u c h i. | 5% |

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
| Max Health | 580 | add |
| Max Spiritual Health | 5,740 | add |
| Attack Damage | 4 | add |
| Attack Speed | 0.35 | add |
| Knockback Resistance | 1 | add |
| Movement Speed | 0.0475 | add |
| Swim Speed Multiplier | 0.04 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/forgotten_config.toml`](../configs/config-mysticism-race-forgotten-config.md).

| Option | Default | Description |
|---|---|---|
| `Revenant.epRequirement` | 800,000 | EP requirement to evolve into a Revenant. |
| `Revenant.minAura` | 500,000 | Minimal aura. |
| `Revenant.maxAura` | 500,000 | Maximum aura. |
| `Revenant.minMagicule` | 500,000 | Minimal magicule. |
| `Revenant.maxMagicule` | 500,000 | Maximum magicule. |
| `Revenant.size` | 0 | Bonus Size. |
| `Revenant.maxHealth` | 580 | Bonus Max Health. |
| `Revenant.maxSpiritualHealth` | 5,740 | Bonus Max Spiritual Health. |
| `Revenant.attack` | 4 | Bonus Attack Damage. |
| `Revenant.attackSpeed` | 0.35 | Bonus Attack Speed. |
| `Revenant.knockbackResistance` | 1 | Bonus Knockback Resistance. |
| `Revenant.movementSpeed` | 0.0475 | Bonus Movement Speed. |
| `Revenant.swimSpeed` | 0.04 | Bonus Swimming Speed Multiplier. |
| `Revenant.intrinsicSkills` | "tensura:spiritual_attack_resistance", "tensura:possession", "mysticism:relapse" | The list of intrinsic skills that the race gets. |
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
