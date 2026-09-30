# Frost Wolf

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:frost_wolf` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 5,250 - 5,250 |
| **Magicule** | 5,250 - 5,250 |
| **Health bonus** | 25 |
| **Spiritual health bonus** | 265 |
| **Attack damage bonus** | 3 |
| **Movement speed bonus** | 0.0275 |
| **EP to evolve into** | 10,000 |

</div>

> A Direwolf that has a connection to ice. Temperatures drop to lethal freezing points when one exists nearby.

## Evolution

- **Evolves from:** [Direwolf](direwolf.md)
- **Evolves into:** [Nivalis Frost Wolf](nivalis-frost-wolf.md)
- **Default evolution:** [Nivalis Frost Wolf](nivalis-frost-wolf.md)
- **On awakening (True Demon Lord / True Hero):** [Glacier Spirit Wolf](glacier-spirit-wolf.md)
- **During the Harvest Festival:** [Nivalis Frost Wolf](nivalis-frost-wolf.md)

### Requirements to evolve into Frost Wolf

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 10,000 | 20% |
| Acquire [Water Manipulation](../../tensura-reincarnated/abilities/extra-skills/water-manipulation.md) | 20% |
| Acquire [Wind Manipulation](../../tensura-reincarnated/abilities/extra-skills/wind-manipulation.md) | 20% |
| Acquire [Ice Manipulation](../abilities/extra-skills/ice-manipulation.md) | 20% |
| Be in any of the following biomes: list comp | 20% |

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

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Step Height | 0.5 | add |
| Scale | 0 | add |
| Max Health | 25 | add |
| Max Spiritual Health | 265 | add |
| Attack Damage | 3 | add |
| Attack Speed | 0.1 | add |
| Knockback Resistance | 0 | add |
| Movement Speed | 0.0275 | add |
| Swim Speed Multiplier | 0.1 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/direwolf/special_direwolf_config.toml`](../configs/config-mysticism-race-direwolf-special-direwolf-config.md).

| Option | Default | Description |
|---|---|---|
| `FrostWolf.epRequirement` | 10,000 | EP requirement to evolve into Frost Wolf. |
| `FrostWolf.abilityRequirement1` | "tensura:water_manipulation" | The first ability that needs to be mastered to evolve into Scorch Wolf. |
| `FrostWolf.abilityMasteryRequirement1` | false | Does the first ability need to be mastered? (true/false) |
| `FrostWolf.abilityRequirement2` | "tensura:wind_manipulation" | The second ability that needs to be mastered to evolve into Scorch Wolf. |
| `FrostWolf.abilityMasteryRequirement2` | false | Does the second ability need to be mastered? (true/false) |
| `FrostWolf.abilityRequirement3` | "mysticism:ice_manipulation" | The third ability that needs to be mastered to evolve into Scorch Wolf. |
| `FrostWolf.abilityMasteryRequirement3` | false | Does the third ability need to be mastered? (true/false) |
| `FrostWolf.minAura` | 5,250 | Minimal aura. |
| `FrostWolf.maxAura` | 5,250 | Maximum aura. |
| `FrostWolf.minMagicule` | 5,250 | Minimal magicule. |
| `FrostWolf.maxMagicule` | 5,250 | Maximum magicule. |
| `FrostWolf.size` | 0 | Bonus Size. |
| `FrostWolf.maxHealth` | 25 | Bonus Max Health. |
| `FrostWolf.maxSpiritualHealth` | 265 | Bonus Max Spiritual Health. |
| `FrostWolf.attack` | 3 | Bonus Attack Damage. |
| `FrostWolf.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `FrostWolf.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `FrostWolf.movementSpeed` | 0.0275 | Bonus Movement Speed. |
| `FrostWolf.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
| `FrostWolf.stepHeight` | 0.5 | Bonus Step Height. |
| `FrostWolf.intrinsicSkills` | "tensura:thought_communication", "tensura:shadow_motion", "tensura:coercion", "tensura:water_manipulation", "tensura:wind_manipulation", "mysticism:ice_manipulation" | The list of intrinsic skills that the race gets. |

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
