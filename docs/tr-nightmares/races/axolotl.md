# Axolotl

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:axolotl` |
| **Stage** | <span class="stage stage-starting">Starting</span> |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 500 - 1,500 |
| **Magicule** | 1,500 - 5,500 |
| **Health bonus** | -15 |
| **Spiritual health bonus** | -10 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0.02 |
| **EP to evolve into** | 50,000 |

</div>

> A calm and curious amphibian race that thrives in tranquil waters and channels magic with patient grace.

## Evolution

- **Evolves into:** [Axolotl Knight](axolotl-knight.md), [Axolotl Wizard](axolotl-wizard.md)

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
| Max Health | -15 | add |
| Max Spiritual Health | -10 | add |
| Attack Damage | 0 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0.5 | add |
| Movement Speed | 0.02 | add |
| Swim Speed Multiplier | 0.5 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/axolotl/axolotl_config.toml`](../configs/config-nightmare-race-axolotl-axolotl-config.md).

| Option | Default | Description |
|---|---|---|
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
