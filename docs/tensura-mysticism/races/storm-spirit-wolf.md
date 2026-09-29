# Storm Spirit Wolf

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:storm_spirit_wolf` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 425,000 - 425,000 |
| **Magicule** | 425,000 - 425,000 |
| **Health bonus** | 680 |
| **Spiritual health bonus** | 4,360 |
| **Attack damage bonus** | 4 |
| **Movement speed bonus** | 0.04 |
| **EP to evolve into** | 800,000 |

</div>

> A truly scary being. This is a Direwolf that has "evolved the correct way" and become a Spiritual Lifeform. One is rarely born once in a millennium, and all normal Direwolves and Star Wolves bow to this creature.

## Evolution

- **Evolves from:** [Tempest Star Wolf](tempest-star-wolf.md), [Scorch Wolf](scorch-wolf.md), [Blazing Scorch Wolf](blazing-scorch-wolf.md), [Star Wolf](star-wolf.md)
- **Evolves into:** [Divine Wolf](divine-wolf.md)
- **Default evolution:** [Divine Wolf](divine-wolf.md)
- **On awakening (True Demon Lord / True Hero):** [Divine Wolf](divine-wolf.md)
- **During the Harvest Festival:** [Tempest Star Wolf](tempest-star-wolf.md)

### Requirements to evolve into Storm Spirit Wolf

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 800,000 | 50% |
| Master name | 50% |

### Evolution tree

```mermaid
flowchart LR
  r0["Amped Guitar Wolf"]
  r1["Antumbra Spirit Wolf"]
  r2["Black Fang"]
  r3["Blazing Scorch Wolf"]
  r4["Blue Fang"]
  r5["Brown Fang"]
  r6["Darkness Fang"]
  r7["Direwolf"]
  r8["Divine Wolf"]
  r9["Frost Wolf"]
  r10["Magic Spirit Wolf"]
  r11["Glacier Spirit Wolf"]
  r12["Green Fang"]
  r13["Guitar Wolf"]
  r14["Light Fang"]
  r15["Magic Spirit Wolf"]
  r16["Molten Spirit Wolf"]
  r17["Mountain Spirit Wolf"]
  r18["Mystical Black Fang"]
  r19["Mystical Black Fang"]
  r20["Mystical Brown Fang"]
  r21["Mystical Darkness Fang"]
  r22["Mystical Green Fang"]
  r23["Mystical Light Fang"]
  r24["Mystical Purple Fang"]
  r25["Mystical Red Fang"]
  r26["Nivalis Frost Wolf"]
  r27["Magic Spirit Wolf"]
  r28["Penumbra Spirit Wolf"]
  r29["Planet Spirit Wolf"]
  r30["Purple Fang"]
  r31["Red Fang"]
  r32["Scorch Wolf"]
  r33["Star Wolf"]
  r34["Storm Spirit Wolf"]
  r35["String Spirit Wolf"]
  r36["Tempest Star Wolf"]
  r37["Volcanic Spirit Wolf"]
  r0 --> r35
  r1 --> r8
  r1 --> r23
  r2 --> r15
  r2 --> r18
  r3 --> r16
  r3 --> r34
  r4 --> r19
  r4 --> r27
  r5 --> r17
  r5 --> r20
  r6 --> r21
  r6 --> r28
  r7 --> r2
  r7 --> r4
  r7 --> r5
  r7 --> r6
  r7 --> r9
  r7 --> r12
  r7 --> r13
  r7 --> r14
  r7 --> r15
  r7 --> r30
  r7 --> r31
  r7 --> r32
  r7 --> r33
  r8 --> r2
  r9 --> r11
  r9 --> r26
  r10 --> r8
  r10 --> r22
  r11 --> r8
  r11 --> r26
  r12 --> r10
  r12 --> r22
  r13 --> r0
  r13 --> r35
  r14 --> r1
  r14 --> r23
  r15 --> r2
  r15 --> r8
  r16 --> r3
  r16 --> r8
  r17 --> r8
  r17 --> r20
  r18 --> r15
  r19 --> r27
  r20 --> r17
  r21 --> r28
  r22 --> r10
  r23 --> r1
  r24 --> r29
  r25 --> r37
  r26 --> r11
  r27 --> r8
  r27 --> r19
  r28 --> r8
  r28 --> r21
  r29 --> r8
  r29 --> r24
  r30 --> r24
  r30 --> r29
  r31 --> r25
  r31 --> r37
  r32 --> r3
  r32 --> r34
  r33 --> r34
  r33 --> r36
  r34 --> r8
  r34 --> r36
  r35 --> r0
  r35 --> r8
  r36 --> r34
  r37 --> r8
  r37 --> r25
```

## Traits

- Spiritual lifeform

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Step Height | 0.5 | add |
| Scale | 0 | add |
| Max Health | 680 | add |
| Max Spiritual Health | 4,360 | add |
| Attack Damage | 4 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0.2 | add |
| Movement Speed | 0.04 | add |
| Swim Speed Multiplier | 0.4 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/direwolf/special_direwolf_config.toml`](../configs/config-mysticism-race-direwolf-special-direwolf-config.md).

| Option | Default | Description |
|---|---|---|
| `StormSpiritWolf.epRequirement` | 800,000 | EP requirement to evolve into Storm Spirit Wolf. |
| `StormSpiritWolf.abilityRequirement` | "tensura:black_lightning" | The ability needed to evolve into Storm Spirit Wolf. |
| `StormSpiritWolf.abilityMasteryRequirement` | true | Does the ability need to be mastered? (true/false) |
| `StormSpiritWolf.minAura` | 425,000 | Minimal aura. |
| `StormSpiritWolf.maxAura` | 425,000 | Maximum aura. |
| `StormSpiritWolf.minMagicule` | 425,000 | Minimal magicule. |
| `StormSpiritWolf.maxMagicule` | 425,000 | Maximum magicule. |
| `StormSpiritWolf.size` | 0 | Bonus Size. |
| `StormSpiritWolf.maxHealth` | 680 | Bonus Max Health. |
| `StormSpiritWolf.maxSpiritualHealth` | 4,360 | Bonus Max Spiritual Health. |
| `StormSpiritWolf.attack` | 4 | Bonus Attack Damage. |
| `StormSpiritWolf.attackSpeed` | 0 | Bonus Attack Speed. |
| `StormSpiritWolf.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `StormSpiritWolf.movementSpeed` | 0.04 | Bonus Movement Speed. |
| `StormSpiritWolf.swimSpeed` | 0.4 | Bonus Swimming Speed Multiplier. |
| `StormSpiritWolf.stepHeight` | 0.5 | Bonus Step Height. |
| `StormSpiritWolf.intrinsicSkills` | "tensura:thought_communication", "tensura:shadow_motion", "tensura:coercion", "tensura:water_manipulation", "tensura:wind_manipulation", "tensura:spatial_manipulation", "tensura:godwolf_sense", "tensura:ultra_instinct", "tensura:black_lightning", "tensura:lightning_manipulation" | The list of intrinsic skills that the race gets. |
| `TempestStarWolf.epRequirement` | 200,000 | EP requirement to evolve into Tempest Star Wolf. |
| `TempestStarWolf.abilityRequirement1` | "tensura:water_manipulation" | The first ability that needs to be mastered to evolve into Tempest Star Wolf. |
| `TempestStarWolf.abilityMasteryRequirement1` | true | Does the first ability need to be mastered? (true/false) |
| `TempestStarWolf.abilityRequirement2` | "tensura:wind_manipulation" | The second ability that needs to be mastered to evolve into Tempest Star Wolf. |
| `TempestStarWolf.abilityMasteryRequirement2` | true | Does the second ability need to be mastered? (true/false) |
| `TempestStarWolf.abilityRequirement3` | "tensura:spatial_manipulation" | The third ability that needs to be mastered to evolve into Tempest Star Wolf. |
| `TempestStarWolf.abilityMasteryRequirement3` | true | Does the third ability need to be mastered? (true/false) |
| `TempestStarWolf.minAura` | 125,000 | Minimal aura. |
| `TempestStarWolf.maxAura` | 125,000 | Maximum aura. |
| `TempestStarWolf.minMagicule` | 125,000 | Minimal magicule. |
| `TempestStarWolf.maxMagicule` | 125,000 | Maximum magicule. |
| `TempestStarWolf.size` | 0 | Bonus Size. |
| `TempestStarWolf.maxHealth` | 380 | Bonus Max Health. |
| `TempestStarWolf.maxSpiritualHealth` | 2,320 | Bonus Max Spiritual Health. |
| `TempestStarWolf.attack` | 3 | Bonus Attack Damage. |
| `TempestStarWolf.attackSpeed` | 0 | Bonus Attack Speed. |
| `TempestStarWolf.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `TempestStarWolf.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `TempestStarWolf.swimSpeed` | 0.3 | Bonus Swimming Speed Multiplier. |
| `TempestStarWolf.stepHeight` | 0.5 | Bonus Step Height. |
| `TempestStarWolf.intrinsicSkills` | "tensura:thought_communication", "tensura:shadow_motion", "tensura:coercion", "tensura:water_manipulation", "tensura:wind_manipulation", "tensura:spatial_manipulation", "tensura:godwolf_sense", "tensura:ultra_instinct", "tensura:black_lightning", "tensura:lightning_manipulation" | The list of intrinsic skills that the race gets. |
| `StarWolf.epRequirement` | 10,000 | EP requirement to evolve into Star Wolf. |
| `StarWolf.abilityRequirement1` | "tensura:water_manipulation" | The first ability that needs to be mastered to evolve into Star Wolf. |
| `StarWolf.abilityMasteryRequirement1` | false | Does the first ability need to be mastered? (true/false) |
| `StarWolf.abilityRequirement2` | "tensura:wind_manipulation" | The second ability that needs to be mastered to evolve into Star Wolf. |
| `StarWolf.abilityMasteryRequirement2` | false | Does the second ability need to be mastered? (true/false) |
| `StarWolf.abilityRequirement3` | "tensura:spatial_manipulation" | The third ability that needs to be mastered to evolve into Star Wolf. |
| `StarWolf.abilityMasteryRequirement3` | false | Does the third ability need to be mastered? (true/false) |
| `StarWolf.heightRequirement` | 120 | The height requirement to evolve into Star Wolf. |
| `StarWolf.minAura` | 5,250 | Minimal aura. |
| `StarWolf.maxAura` | 5,250 | Maximum aura. |
| `StarWolf.minMagicule` | 5,250 | Minimal magicule. |
| `StarWolf.maxMagicule` | 5,250 | Maximum magicule. |
| `StarWolf.size` | 0 | Bonus Size. |
| `StarWolf.maxHealth` | 25 | Bonus Max Health. |
| `StarWolf.maxSpiritualHealth` | 265 | Bonus Max Spiritual Health. |
| `StarWolf.attack` | 3 | Bonus Attack Damage. |
| `StarWolf.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `StarWolf.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `StarWolf.movementSpeed` | 0.0275 | Bonus Movement Speed. |
| `StarWolf.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
| `StarWolf.stepHeight` | 0.5 | Bonus Step Height. |
| `StarWolf.intrinsicSkills` | "tensura:thought_communication", "tensura:shadow_motion", "tensura:coercion", "tensura:water_manipulation", "tensura:wind_manipulation", "tensura:spatial_manipulation" | The list of intrinsic skills that the race gets. |

Set in [`config/mysticism/race/direwolf/direwolf_config.toml`](../configs/config-mysticism-race-direwolf-direwolf-config.md).

| Option | Default | Description |
|---|---|---|
| `Direwolf.minAura` | 1,834 | Minimal aura. |
| `Direwolf.maxAura` | 2,166 | Maximum aura. |
| `Direwolf.minMagicule` | 1,833 | Minimal magicule. |
| `Direwolf.maxMagicule` | 2,167 | Maximum magicule. |
| `Direwolf.size` | -0.25 | Bonus Size. |
| `Direwolf.maxHealth` | 6 | Bonus Max Health. |
| `Direwolf.maxSpiritualHealth` | 35 | Bonus Max Spiritual Health. |
| `Direwolf.attack` | 3 | Bonus Attack Damage. |
| `Direwolf.attackSpeed` | 0 | Bonus Attack Speed. |
| `Direwolf.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Direwolf.movementSpeed` | 0.025 | Bonus Movement Speed. |
| `Direwolf.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
| `Direwolf.stepHeight` | 0.5 | Bonus Step Height. |
| `Direwolf.intrinsicSkills` | "tensura:thought_communication", "tensura:shadow_motion", "tensura:coercion" | The list of intrinsic skills that the race gets. |

## Tags

`tensura:races/spiritual`
