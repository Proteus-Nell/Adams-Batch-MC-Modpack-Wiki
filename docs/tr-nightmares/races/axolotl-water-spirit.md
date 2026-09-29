# Axolotl Water Spirit

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:axolotl_water_spirit` |
| **Difficulty** | Hard |
| **Alignment** | Holy |
| **Aura** | 500 - 500 |
| **Magicule** | 1,500 - 5,500 |
| **Health bonus** | 180 |
| **Spiritual health bonus** | 3,600 |
| **Attack damage bonus** | 1 |
| **Movement speed bonus** | 0.02 |
| **EP to evolve into** | 200,000 |

</div>

## Evolution

- **Evolves from:** [Axolotl Wizard](axolotl-wizard.md)
- **Evolves into:** [Axolotl Water Spirit Dragon](axolotl-water-dragon.md)
- **Default evolution:** [Axolotl Water Spirit Dragon](axolotl-water-dragon.md)
- **On awakening (True Demon Lord / True Hero):** [Axolotl Water Spirit Dragon](axolotl-water-dragon.md)
- **During the Harvest Festival:** [Axolotl Water Spirit Dragon](axolotl-water-dragon.md)

### Requirements to evolve into Axolotl Water Spirit

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 200,000 | 34% |
| Master name | 33% |
| Consume 60 of COD | 33% |

### Evolution tree

```mermaid
flowchart LR
  r0["Axolotl"]
  r1["Axolotl Knight"]
  r2["Axolotl Steel Spirit Dragon"]
  r3["Axolotl Steel Spirit"]
  r4["Axolotl Water Spirit Dragon"]
  r5["Axolotl Water Spirit"]
  r6["Axolotl Wizard"]
  r0 --> r1
  r0 --> r6
  r1 --> r3
  r3 --> r2
  r5 --> r4
  r6 --> r5
```

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | -1.1 | add |
| Max Health | 180 | add |
| Max Spiritual Health | 3,600 | add |
| Attack Damage | 1 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 5 | add |
| Movement Speed | 0.02 | add |
| Swim Speed Multiplier | 0.5 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/axolotl/axolotl_config.toml`](../configs/config-nightmare-race-axolotl-axolotl-config.md).

| Option | Default | Description |
|---|---|---|
| `WaterSpirit.epRequirement` | 200,000 | EP requirement to evolve. |
| `WaterSpirit.codRequirement` | 60 | Raw cod requirement to evolve |
| `WaterSpirit.minAura` | 500 | Minimal aura. |
| `WaterSpirit.maxAura` | 500 | Maximum aura. |
| `WaterSpirit.minMagicule` | 1,500 | Minimal magicule. |
| `WaterSpirit.maxMagicule` | 5,500 | Maximum magicule. |
| `WaterSpirit.size` | -1.1 | Bonus Size. |
| `WaterSpirit.maxHealth` | 180 | Bonus Max Health. |
| `WaterSpirit.maxSpiritualHealth` | 3,600 | Bonus Max Spiritual Health. |
| `WaterSpirit.attack` | 1 | Bonus Attack Damage. |
| `WaterSpirit.attackSpeed` | 0 | Bonus Attack Speed. |
| `WaterSpirit.knockbackResistance` | 5 | Bonus Knockback Resistance. |
| `WaterSpirit.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `WaterSpirit.swimSpeed` | 0.5 | Bonus Swimming Speed Multiplier. |
| `WaterSpirit.intrinsicSkills` | "trnightmare:water_ki_release" | List of skills obtained by this race. |
| `AxolotlWizard.epRequirement` | 50,000 | EP requirement to evolve. |
| `AxolotlWizard.minAura` | 500 | Minimal aura. |
| `AxolotlWizard.maxAura` | 1,500 | Maximum aura. |
| `AxolotlWizard.minMagicule` | 1,500 | Minimal magicule. |
| `AxolotlWizard.maxMagicule` | 5,500 | Maximum magicule. |
| `AxolotlWizard.size` | -1.1 | Bonus Size. |
| `AxolotlWizard.maxHealth` | 0 | Bonus Max Health. |
| `AxolotlWizard.maxSpiritualHealth` | 40 | Bonus Max Spiritual Health. |
| `AxolotlWizard.attack` | 0 | Bonus Attack Damage. |
| `AxolotlWizard.attackSpeed` | 0 | Bonus Attack Speed. |
| `AxolotlWizard.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `AxolotlWizard.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `AxolotlWizard.swimSpeed` | 0.5 | Bonus Swimming Speed Multiplier. |
| `AxolotlWizard.intrinsicSkills` | "tensura:self_regeneration", "tensura:absorb_and_dissolve", "tensura:water_breathing", "tensura:wind_attack_resistance" | List of skills obtained by this race. |
| `Axolotl.epRequirement` | 50,000 | EP requirement to evolve. |
| `Axolotl.minAura` | 500 | Minimal aura. |
| `Axolotl.maxAura` | 1,500 | Maximum aura. |
| `Axolotl.minMagicule` | 1,500 | Minimal magicule. |
| `Axolotl.maxMagicule` | 5,500 | Maximum magicule. |
| `Axolotl.size` | -1.1 | Bonus Size. |
| `Axolotl.maxHealth` | -15 | Bonus Max Health. |
| `Axolotl.maxSpiritualHealth` | -10 | Bonus Max Spiritual Health. |
| `Axolotl.attack` | 0 | Bonus Attack Damage. |
| `Axolotl.attackSpeed` | 0 | Bonus Attack Speed. |
| `Axolotl.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `Axolotl.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `Axolotl.swimSpeed` | 0.5 | Bonus Swimming Speed Multiplier. |
| `Axolotl.intrinsicSkills` | "tensura:self_regeneration", "tensura:absorb_and_dissolve", "tensura:water_breathing", "tensura:wind_attack_resistance" | List of skills obtained by this race. |
