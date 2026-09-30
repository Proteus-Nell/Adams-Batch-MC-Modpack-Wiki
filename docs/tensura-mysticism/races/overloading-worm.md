# Overloading Worm

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:overloading_worm` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Extreme |
| **Alignment** | Majin |
| **Aura** | 100,000 - 100,000 |
| **Magicule** | 100,000 - 100,000 |
| **Health bonus** | 180 |
| **Spiritual health bonus** | 470 |
| **Attack damage bonus** | 1.5 |
| **Movement speed bonus** | 0.02 |
| **EP to evolve into** | 100,000 |

</div>

> "The Reminder." When two brothers played, this one watched.

## Evolution

- **Evolves from:** [Charged Perforator](charged-perforator.md)
- **Evolves into:** [Lightning Aberration](lightning-aberration.md)
- **Default evolution:** [Lightning Aberration](lightning-aberration.md)
- **On awakening (True Demon Lord / True Hero):** [Lightning Aberration](lightning-aberration.md)

### Requirements to evolve into Overloading Worm

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 100,000 | 50% |
| Consume 15 of [Lightning Essence](../items/food/lightning-essence.md) | 50% |

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
| Scale | 0.25 | add |
| Max Health | 180 | add |
| Max Spiritual Health | 470 | add |
| Attack Damage | 1.5 | add |
| Attack Speed | 0.2 | add |
| Knockback Resistance | 0.2 | add |
| Movement Speed | 0.02 | add |
| Swim Speed Multiplier | 0.2 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/sculk_config.toml`](../configs/config-mysticism-race-sculk-config.md).

| Option | Default | Description |
|---|---|---|
| `OverloadingWorm.essenceRequired` | 15 | Quantity of Lightning Essence required to become an Overloading Worm as a Charged Perforator. |
| `OverloadingWorm.epRequirement` | 100,000 | EP requirement to evolve into Overloading Worm. |
| `OverloadingWorm.minAura` | 100,000 | Minimal aura. |
| `OverloadingWorm.maxAura` | 100,000 | Maximum aura. |
| `OverloadingWorm.minMagicule` | 100,000 | Minimal magicule. |
| `OverloadingWorm.maxMagicule` | 100,000 | Maximum magicule. |
| `OverloadingWorm.size` | 0.25 | Bonus Size. |
| `OverloadingWorm.maxHealth` | 180 | Bonus Max Health. |
| `OverloadingWorm.maxSpiritualHealth` | 470 | Bonus Max Spiritual Health. |
| `OverloadingWorm.attack` | 1.5 | Bonus Attack Damage. |
| `OverloadingWorm.attackSpeed` | 0.2 | Bonus Attack Speed. |
| `OverloadingWorm.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `OverloadingWorm.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `OverloadingWorm.swimSpeed` | 0.2 | Bonus Swimming Speed Multiplier. |
| `OverloadingWorm.intrinsicSkills` | "tensura:sense_soundwave", "tensura:lightning_manipulation", "tensura:electricity_resistance", "tensura:heat_resistance", "mysticism:discharge" | The list of intrinsic skills that the race gets. |
| `ChargedPerforator.essenceRequired` | 10 | Quantity of Lightning Essence required to become a Charged Perforator as a Sculk Worm. |
| `ChargedPerforator.epRequirement` | 4,000 | EP requirement to evolve into Charged Perforator. |
| `ChargedPerforator.minAura` | 10,000 | Minimal aura. |
| `ChargedPerforator.maxAura` | 10,000 | Maximum aura. |
| `ChargedPerforator.minMagicule` | 10,000 | Minimal magicule. |
| `ChargedPerforator.maxMagicule` | 10,000 | Maximum magicule. |
| `ChargedPerforator.size` | 0 | Bonus Size. |
| `ChargedPerforator.maxHealth` | 55 | Bonus Max Health. |
| `ChargedPerforator.maxSpiritualHealth` | 270 | Bonus Max Spiritual Health. |
| `ChargedPerforator.attack` | 5 | Bonus Attack Damage. |
| `ChargedPerforator.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `ChargedPerforator.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `ChargedPerforator.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `ChargedPerforator.swimSpeed` | 0.01 | Bonus Swimming Speed Multiplier. |
| `ChargedPerforator.intrinsicSkills` | "tensura:sense_soundwave", "tensura:lightning_manipulation", "tensura:electricity_resistance", "tensura:heat_resistance" | The list of intrinsic skills that the race gets. |
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
