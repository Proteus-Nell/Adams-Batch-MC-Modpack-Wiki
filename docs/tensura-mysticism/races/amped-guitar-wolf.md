# Amped Guitar Wolf

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:amped_guitar_wolf` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 125,000 - 125,000 |
| **Magicule** | 125,000 - 125,000 |
| **Health bonus** | 380 |
| **Spiritual health bonus** | 2,320 |
| **Attack damage bonus** | 3 |
| **Movement speed bonus** | 0.03 |
| **EP to evolve into** | 200,000 |

</div>

> An evolved Guitar Wolf that has a deep connection to sound. It can disrupt the magic of nearby enemies, typically being a highly-feared and regarded monster.

## Evolution

- **Evolves from:** [Guitar Wolf](guitar-wolf.md), [String Spirit Wolf](string-spirit-wolf.md)
- **Evolves into:** [String Spirit Wolf](string-spirit-wolf.md)
- **Default evolution:** [String Spirit Wolf](string-spirit-wolf.md)
- **On awakening (True Demon Lord / True Hero):** [String Spirit Wolf](string-spirit-wolf.md)

### Requirements to evolve into Amped Guitar Wolf

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 200,000 | 50% |
| Master [Sound Manipulation](../../tensura-reincarnated/abilities/extra-skills/sound-manipulation.md) | 50% |

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
| Max Health | 380 | add |
| Max Spiritual Health | 2,320 | add |
| Attack Damage | 3 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0.1 | add |
| Movement Speed | 0.03 | add |
| Swim Speed Multiplier | 0.3 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/direwolf/special_direwolf_config.toml`](../configs/config-mysticism-race-direwolf-special-direwolf-config.md).

| Option | Default | Description |
|---|---|---|
| `AmpedGuitarWolf.epRequirement` | 200,000 | EP requirement to evolve into Amped Guitar Wolf. |
| `AmpedGuitarWolf.abilityRequirement` | "tensura:sound_manipulation" | The ability needed to evolve into Amped Guitar Wolf. |
| `AmpedGuitarWolf.abilityMasteryRequirement` | true | Does the ability need to be mastered? (true/false) |
| `AmpedGuitarWolf.minAura` | 125,000 | Minimal aura. |
| `AmpedGuitarWolf.maxAura` | 125,000 | Maximum aura. |
| `AmpedGuitarWolf.minMagicule` | 125,000 | Minimal magicule. |
| `AmpedGuitarWolf.maxMagicule` | 125,000 | Maximum magicule. |
| `AmpedGuitarWolf.size` | 0 | Bonus Size. |
| `AmpedGuitarWolf.maxHealth` | 380 | Bonus Max Health. |
| `AmpedGuitarWolf.maxSpiritualHealth` | 2,320 | Bonus Max Spiritual Health. |
| `AmpedGuitarWolf.attack` | 3 | Bonus Attack Damage. |
| `AmpedGuitarWolf.attackSpeed` | 0 | Bonus Attack Speed. |
| `AmpedGuitarWolf.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `AmpedGuitarWolf.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `AmpedGuitarWolf.swimSpeed` | 0.3 | Bonus Swimming Speed Multiplier. |
| `AmpedGuitarWolf.stepHeight` | 0.5 | Bonus Step Height. |
| `AmpedGuitarWolf.intrinsicSkills` | "tensura:thought_communication", "tensura:shadow_motion", "tensura:coercion", "tensura:sticky_steel_thread", "tensura:godwolf_sense" | The list of intrinsic skills that the race gets. |
| `GuitarWolf.epRequirement` | 10,000 | EP requirement to evolve into Guitar Wolf. |
| `GuitarWolf.abilityRequirement` | "tensura:sound_manipulation" | The ability needed to evolve into Guitar Wolf. |
| `GuitarWolf.abilityMasteryRequirement` | false | Does the ability need to be mastered? (true/false) |
| `GuitarWolf.minAura` | 5,250 | Minimal aura. |
| `GuitarWolf.maxAura` | 5,250 | Maximum aura. |
| `GuitarWolf.minMagicule` | 5,250 | Minimal magicule. |
| `GuitarWolf.maxMagicule` | 5,250 | Maximum magicule. |
| `GuitarWolf.size` | 0 | Bonus Size. |
| `GuitarWolf.maxHealth` | 25 | Bonus Max Health. |
| `GuitarWolf.maxSpiritualHealth` | 265 | Bonus Max Spiritual Health. |
| `GuitarWolf.attack` | 3 | Bonus Attack Damage. |
| `GuitarWolf.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `GuitarWolf.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `GuitarWolf.movementSpeed` | 0.0275 | Bonus Movement Speed. |
| `GuitarWolf.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
| `GuitarWolf.stepHeight` | 0.5 | Bonus Step Height. |
| `GuitarWolf.intrinsicSkills` | "tensura:thought_communication", "tensura:shadow_motion", "tensura:coercion", "tensura:sticky_steel_thread" | The list of intrinsic skills that the race gets. |

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
