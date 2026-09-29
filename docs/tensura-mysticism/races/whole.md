# Whole

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:whole` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Intermediate |
| **Alignment** | Holy |
| **Aura** | 200,000 - 200,000 |
| **Magicule** | 200,000 - 200,000 |
| **Health bonus** | 230 |
| **Spiritual health bonus** | 3,240 |
| **Attack damage bonus** | -0.35 |
| **Movement speed bonus** | 0.01 |
| **EP to evolve into** | 200,000 |

</div>

> Acceptance. The first step to becoming complete. When the remnants of your past collide together, only when you accept your struggles can you become Whole.

## Evolution

- **Evolves from:** [Remnant](remnant.md)
- **Evolves into:** [Ascended](ascended.md)
- **Default evolution:** [Ascended](ascended.md)
- **On awakening (True Demon Lord / True Hero):** [Ascended](ascended.md)

### Requirements to evolve into Whole

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

- Spiritual lifeform

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 230 | add |
| Max Spiritual Health | 3,240 | add |
| Attack Damage | -0.35 | add |
| Attack Speed | 0.1 | add |
| Knockback Resistance | 1 | add |
| Movement Speed | 0.01 | add |
| Swim Speed Multiplier | 0.01 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/forgotten_config.toml`](../configs/config-mysticism-race-forgotten-config.md).

| Option | Default | Description |
|---|---|---|
| `Whole.epRequirement` | 200,000 | EP requirement to evolve into a Whole. |
| `Whole.minAura` | 200,000 | Minimal aura. |
| `Whole.maxAura` | 200,000 | Maximum aura. |
| `Whole.minMagicule` | 200,000 | Minimal magicule. |
| `Whole.maxMagicule` | 200,000 | Maximum magicule. |
| `Whole.size` | 0 | Bonus Size. |
| `Whole.maxHealth` | 230 | Bonus Max Health. |
| `Whole.maxSpiritualHealth` | 3,240 | Bonus Max Spiritual Health. |
| `Whole.attack` | -0.35 | Bonus Attack Damage. |
| `Whole.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `Whole.knockbackResistance` | 1 | Bonus Knockback Resistance. |
| `Whole.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `Whole.swimSpeed` | 0.01 | Bonus Swimming Speed Multiplier. |
| `Whole.intrinsicSkills` | "tensura:spiritual_attack_resistance", "tensura:possession", "mysticism:relapse" | The list of intrinsic skills that the race gets. |
| `Ascended.epRequirement` | 600,000 | EP requirement to evolve into an Ascended. |
| `Ascended.ascendedAwakening` | false | Should Awakening as a Whole instantly set a player to this race? |
| `Ascended.minAura` | 500,000 | Minimal aura. |
| `Ascended.maxAura` | 500,000 | Maximum aura. |
| `Ascended.minMagicule` | 500,000 | Minimal magicule. |
| `Ascended.maxMagicule` | 500,000 | Maximum magicule. |
| `Ascended.size` | 0 | Bonus Size. |
| `Ascended.maxHealth` | 780 | Bonus Max Health. |
| `Ascended.maxSpiritualHealth` | 6,440 | Bonus Max Spiritual Health. |
| `Ascended.attack` | -0.25 | Bonus Attack Damage. |
| `Ascended.attackSpeed` | 0.4 | Bonus Attack Speed. |
| `Ascended.knockbackResistance` | 1 | Bonus Knockback Resistance. |
| `Ascended.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `Ascended.swimSpeed` | 0.03 | Bonus Swimming Speed Multiplier. |
| `Ascended.intrinsicSkills` | "tensura:spiritual_attack_resistance", "tensura:possession", "mysticism:relapse" | The list of intrinsic skills that the race gets. |
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

`tensura:races/spiritual`
