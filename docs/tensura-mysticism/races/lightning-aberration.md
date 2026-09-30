# Lightning Aberration

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:lightning_aberration` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Extreme |
| **Alignment** | Majin |
| **Aura** | 400,000 - 400,000 |
| **Magicule** | 400,000 - 400,000 |
| **Health bonus** | 730 |
| **Spiritual health bonus** | 600 |
| **Attack damage bonus** | 3.5 |
| **Movement speed bonus** | 0.0425 |
| **EP to evolve into** | 400,000 |

</div>

> Pray that its power is not truly unleashed. Know the fear and drive behind an aberration of pure electricity. It is a demi-spiritual lifeform.

## Evolution

- **Evolves from:** [Overloading Worm](overloading-worm.md), [Charged Perforator](charged-perforator.md)
- **Evolves into:** [Dissonance Deity](dissonance-deity.md)
- **Default evolution:** [Dissonance Deity](dissonance-deity.md)
- **On awakening (True Demon Lord / True Hero):** [Dissonance Deity](dissonance-deity.md)

### Requirements to evolve into Lightning Aberration

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 400,000 | 50% |
| Consume 30 of [Lightning Essence](../items/food/lightning-essence.md) | 50% |

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

## Traits

- Spiritual lifeform

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0.25 | add |
| Max Health | 730 | add |
| Max Spiritual Health | 600 | add |
| Attack Damage | 3.5 | add |
| Attack Speed | 0.4 | add |
| Knockback Resistance | 0.5 | add |
| Movement Speed | 0.0425 | add |
| Swim Speed Multiplier | 0.3 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/sculk_config.toml`](../configs/config-mysticism-race-sculk-config.md).

| Option | Default | Description |
|---|---|---|
| `LightningAberration.essenceRequired` | 30 | Quantity of Lightning Essence required to become a Lightning Aberration as a Overloading Worm. |
| `LightningAberration.epRequirement` | 400,000 | EP requirement to evolve into a Lightning Aberration. |
| `LightningAberration.minAura` | 400,000 | Minimal aura. |
| `LightningAberration.maxAura` | 400,000 | Maximum aura. |
| `LightningAberration.minMagicule` | 400,000 | Minimal magicule. |
| `LightningAberration.maxMagicule` | 400,000 | Maximum magicule. |
| `LightningAberration.size` | 0.25 | Bonus Size. |
| `LightningAberration.maxHealth` | 730 | Bonus Max Health. |
| `LightningAberration.maxSpiritualHealth` | 600 | Bonus Max Spiritual Health. |
| `LightningAberration.attack` | 3.5 | Bonus Attack Damage. |
| `LightningAberration.attackSpeed` | 0.4 | Bonus Attack Speed. |
| `LightningAberration.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `LightningAberration.movementSpeed` | 0.0425 | Bonus Movement Speed. |
| `LightningAberration.swimSpeed` | 0.3 | Bonus Swimming Speed Multiplier. |
| `LightningAberration.intrinsicSkills` | "tensura:sense_soundwave", "tensura:lightning_manipulation", "tensura:electricity_resistance", "tensura:heat_resistance", "mysticism:discharge", "tensura:lightning_domination" | The list of intrinsic skills that the race gets. |
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

## Tags

`tensura:races/spiritual`
