# Chimera Lord

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:chimera_lord` |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 150,000 - 300,000 |
| **Magicule** | 200,000 - 400,000 |
| **Health bonus** | 300 |
| **Spiritual health bonus** | 2,000 |
| **Attack damage bonus** | 2.5 |
| **Movement speed bonus** | 0.03 |
| **EP to evolve into** | 120,000 |

</div>

## Evolution

- **Evolves from:** [Golden Chimera](golden-chimera.md)
- **Evolves into:** [Divine Chimera](divine-chimera.md)
- **Default evolution:** [Divine Chimera](divine-chimera.md)
- **On awakening (True Demon Lord / True Hero):** [Golden Chimera](golden-chimera.md)
- **During the Harvest Festival:** [Divine Chimera](divine-chimera.md)

### Requirements to evolve into Chimera Lord

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 2,000,000 | 20% |
| Kill 5 bosses | 20% |
| Consume 10 of ENCHANTED_GOLDEN_APPLE | 15% |
| Consume 15 of [Royal Blood](../../tensura-reincarnated/items/miscellaneous/royal-blood.md) | 15% |
| Consume 15 of [Elemental Essence](../../tensura-reincarnated/items/materials/elemental-essence.md) | 15% |
| Consume 15 of [Dragon Essence](../../tensura-reincarnated/items/materials/dragon-essence.md) | 15% |

### Evolution tree

```mermaid
flowchart LR
  r0["Chimera Lord"]
  r1["Divine Chimera"]
  r2["Golden Chimera"]
  r3["Greater Chimera"]
  r4["Lesser Chimera"]
  r0 --> r1
  r0 --> r2
  r1 --> r2
  r2 --> r0
  r3 --> r2
  r4 --> r2
  r4 --> r3
```

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 300 | add |
| Max Spiritual Health | 2,000 | add |
| Attack Damage | 2.5 | add |
| Attack Speed | 0.4 | add |
| Knockback Resistance | 0.5 | add |
| Movement Speed | 0.03 | add |
| Swim Speed Multiplier | 0.2 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/chimera_config.toml`](../configs/config-nightmare-race-chimera-config.md).

| Option | Default | Description |
|---|---|---|
| `ChimeraLord.minAura` | 150,000 | Minimal aura. |
| `ChimeraLord.maxAura` | 300,000 | Maximum aura. |
| `ChimeraLord.minMagicule` | 200,000 | Minimal magicule. |
| `ChimeraLord.maxMagicule` | 400,000 | Maximum magicule. |
| `ChimeraLord.size` | 0 | Bonus Size. |
| `ChimeraLord.maxHealth` | 300 | Bonus Max Health. |
| `ChimeraLord.maxSpiritualHealth` | 2,000 | Bonus Max Spiritual Health. |
| `ChimeraLord.attack` | 2.5 | Bonus Attack Damage. |
| `ChimeraLord.attackSpeed` | 0.4 | Bonus Attack Speed. |
| `ChimeraLord.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `ChimeraLord.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `ChimeraLord.swimSpeed` | 0.2 | Bonus Swimming Speed Multiplier. |
| `ChimeraLord.intrinsicPool` | "tensura:absorb_and_dissolve", "tensura:beast_transformation", "tensura:dragon_ear", "tensura:dragon_eye", "tensura:dragon_mode", "tensura:dragon_skin", "tensura:giantification", "tensura:water_breathing", "tensura:corrosion", "tensura:self_regeneration", "tensura:voice_cannon", "tensura:snake_eye", "tensura:ultra_instinct", "tensura:shadow_motion", "tensura:sticky_steel_thread", "tensura:abnormal_condition_resistance", "tensura:magic_resistance", "tensura:pain_resistance", "tensura:poison_resistance", "tensura:black_lightning" ... (22 total) | List of intrinsic skills Chimera Lord can randomly receive. |
| `ChimeraLord.intrinsicCount` | 5 | How many intrinsic skills a Chimera Lord receives. |
| `GoldenChimera.epRequirement` | 120,000 | EP requirement to evolve into Arch Chimera. |
| `GoldenChimera.minAura` | 30,000 | Minimal aura. |
| `GoldenChimera.maxAura` | 60,000 | Maximum aura. |
| `GoldenChimera.minMagicule` | 60,000 | Minimal magicule. |
| `GoldenChimera.maxMagicule` | 120,000 | Maximum magicule. |
| `GoldenChimera.size` | 0 | Bonus Size. |
| `GoldenChimera.maxHealth` | 120 | Bonus Max Health. |
| `GoldenChimera.maxSpiritualHealth` | 500 | Bonus Max Spiritual Health. |
| `GoldenChimera.attack` | 1.5 | Bonus Attack Damage. |
| `GoldenChimera.attackSpeed` | 0.2 | Bonus Attack Speed. |
| `GoldenChimera.knockbackResistance` | 0.3 | Bonus Knockback Resistance. |
| `GoldenChimera.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `GoldenChimera.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
| `GoldenChimera.intrinsicPool` | "tensura:absorb_and_dissolve", "tensura:beast_transformation", "tensura:dragon_ear", "tensura:dragon_eye", "tensura:dragon_mode", "tensura:dragon_skin", "tensura:giantification", "tensura:water_breathing", "tensura:corrosion", "tensura:self_regeneration", "tensura:voice_cannon", "tensura:snake_eye", "tensura:ultra_instinct", "tensura:shadow_motion", "tensura:sticky_steel_thread", "tensura:abnormal_condition_resistance", "tensura:magic_resistance", "tensura:pain_resistance", "tensura:poison_resistance" | List of intrinsic skills Golden Chimera can randomly receive. |
| `GoldenChimera.intrinsicCount` | 4 | How many intrinsic skills a Golden Chimera receives. |
| `GreaterChimera.epRequirement` | 20,000 | EP requirement to evolve into Greater Chimera. |
| `GreaterChimera.minAura` | 8,000 | Minimal aura. |
| `GreaterChimera.maxAura` | 15,000 | Maximum aura. |
| `GreaterChimera.minMagicule` | 12,000 | Minimal magicule. |
| `GreaterChimera.maxMagicule` | 25,000 | Maximum magicule. |
| `GreaterChimera.size` | 0.2 | Bonus Size. |
| `GreaterChimera.maxHealth` | 50 | Bonus Max Health. |
| `GreaterChimera.maxSpiritualHealth` | 180 | Bonus Max Spiritual Health. |
| `GreaterChimera.attack` | 0.8 | Bonus Attack Damage. |
| `GreaterChimera.attackSpeed` | 0 | Bonus Attack Speed. |
| `GreaterChimera.knockbackResistance` | 0.15 | Bonus Knockback Resistance. |
| `GreaterChimera.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `GreaterChimera.swimSpeed` | 0.05 | Bonus Swimming Speed Multiplier. |
| `GreaterChimera.intrinsicPool` | "tensura:absorb_and_dissolve", "tensura:beast_transformation", "tensura:dragon_ear", "tensura:dragon_eye", "tensura:dragon_mode", "tensura:dragon_skin", "tensura:giantification", "tensura:water_breathing", "tensura:corrosion", "tensura:self_regeneration", "tensura:voice_cannon", "tensura:snake_eye", "tensura:ultra_instinct" | List of intrinsic skills Greater Chimera can randomly receive. |
| `GreaterChimera.intrinsicCount` | 3 | How many intrinsic skills a Greater Chimera receives. |
| `LesserChimera.minAura` | 1,500 | Minimal aura. |
| `LesserChimera.maxAura` | 2,500 | Maximum aura. |
| `LesserChimera.minMagicule` | 3,000 | Minimal magicule. |
| `LesserChimera.maxMagicule` | 4,500 | Maximum magicule. |
| `LesserChimera.size` | 0.4 | Bonus Size. |
| `LesserChimera.maxHealth` | 18 | Bonus Max Health. |
| `LesserChimera.maxSpiritualHealth` | 80 | Bonus Max Spiritual Health. |
| `LesserChimera.attack` | 0.3 | Bonus Attack Damage. |
| `LesserChimera.attackSpeed` | -0.3 | Bonus Attack Speed. |
| `LesserChimera.knockbackResistance` | 0.05 | Bonus Knockback Resistance. |
| `LesserChimera.movementSpeed` | 0 | Bonus Movement Speed. |
| `LesserChimera.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `LesserChimera.intrinsicPool` | "tensura:absorb_and_dissolve", "tensura:beast_transformation", "tensura:dragon_ear", "tensura:dragon_eye", "tensura:dragon_mode", "tensura:dragon_skin", "tensura:giantification", "tensura:water_breathing" | List of intrinsic skills Lesser Chimera can randomly receive. |
| `LesserChimera.intrinsicCount` | 2 | How many intrinsic skills a Lesser Chimera receives from the pool. |
