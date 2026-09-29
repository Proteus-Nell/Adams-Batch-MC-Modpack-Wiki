# Army Wasp

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:army_wasp` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 5,250 - 5,250 |
| **Magicule** | 5,250 - 5,250 |
| **Health bonus** | 50 |
| **Spiritual health bonus** | 350 |
| **Attack damage bonus** | 0.5 |
| **Movement speed bonus** | 0 |
| **EP to evolve into** | 10,000 |

</div>

> An evolved scorpion, with the capability of manipulating gravity itself. It floats around aimlessly and randomly stings things it finds interesting. It has never been hunted excessively due to its nature, so its defenses are extremely weak.

## Evolution

- **Evolves from:** [Wasp](wasp.md)
- **Evolves into:** [Army Wasp Insectar](army-wasp-insectar.md)
- **Default evolution:** [Army Wasp Insectar](army-wasp-insectar.md)
- **On awakening (True Demon Lord / True Hero):** [Star Soul Insect](star-soul-insect.md)
- **During the Harvest Festival:** [Army Wasp Insectar](army-wasp-insectar.md)

### Requirements to evolve into Army Wasp

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 10,000 | 100% |

## Traits

- Has creative-style flight

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Flying Speed | 0 | add |
| Scale | 0.25 | add |
| Max Health | 50 | add |
| Max Spiritual Health | 350 | add |
| Attack Damage | 0.5 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0.1 | add |
| Movement Speed | 0 | add |
| Swim Speed Multiplier | -0.3 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/insect/wasp_config.toml`](../configs/config-mysticism-race-insect-wasp-config.md).

| Option | Default | Description |
|---|---|---|
| `ArmyWasp.epRequirement` | 10,000 | EP requirement to evolve into Army Wasp. |
| `ArmyWasp.minAura` | 5,250 | Minimal aura. |
| `ArmyWasp.maxAura` | 5,250 | Maximum aura. |
| `ArmyWasp.minMagicule` | 5,250 | Minimal magicule. |
| `ArmyWasp.maxMagicule` | 5,250 | Maximum magicule. |
| `ArmyWasp.size` | 0.25 | Bonus Size. |
| `ArmyWasp.maxHealth` | 50 | Bonus Max Health. |
| `ArmyWasp.maxSpiritualHealth` | 350 | Bonus Max Spiritual Health. |
| `ArmyWasp.attack` | 0.5 | Bonus Attack Damage. |
| `ArmyWasp.attackSpeed` | 0 | Bonus Attack Speed. |
| `ArmyWasp.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `ArmyWasp.movementSpeed` | 0 | Bonus Movement Speed. |
| `ArmyWasp.swimSpeed` | -0.3 | Bonus Swimming Speed Multiplier. |
| `ArmyWasp.flightSpeed` | 0 | Bonus Flight Speed Multiplier. |
| `ArmyWasp.intrinsicSkills` | "mysticism:exoskeleton", "tensura:analytical_appraisal" | The list of intrinsic skills that the race gets. |
| `Wasp.minAura` | 1,000 | Minimal aura. |
| `Wasp.maxAura` | 2,000 | Maximum aura. |
| `Wasp.minMagicule` | 2,000 | Minimal magicule. |
| `Wasp.maxMagicule` | 3,000 | Maximum magicule. |
| `Wasp.size` | -0.75 | Bonus Size. |
| `Wasp.maxHealth` | 4 | Bonus Max Health. |
| `Wasp.maxSpiritualHealth` | 35 | Bonus Max Spiritual Health. |
| `Wasp.attack` | -0.5 | Bonus Attack Damage. |
| `Wasp.attackSpeed` | 0 | Bonus Attack Speed. |
| `Wasp.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Wasp.movementSpeed` | 0 | Bonus Movement Speed. |
| `Wasp.swimSpeed` | -0.3 | Bonus Swimming Speed Multiplier. |
| `Wasp.flightSpeed` | -0.02 | Bonus Flight Speed Multiplier. |
| `Wasp.intrinsicSkills` | "mysticism:exoskeleton", "tensura:analytical_appraisal" | The list of intrinsic skills that the race gets. |

Set in [`config/mysticism/general.toml`](../configs/config-mysticism-general.md).

| Option | Default | Description |
|---|---|---|
| `General.refresh` | true | Should the Tensura configurations add Mysticism's skills and races on next launch? |
| `General.flightSpeed` | 0.05 | The default flying speed of all Mysticism races. |
| `General.seCostMultiplier` | 4 | SE cost multiplier when acquiring a Unique Skill. Default: 4, which means the skill's magicule cost \* 4 |

Set in [`config/mysticism/race/insect/ant_config.toml`](../configs/config-mysticism-race-insect-ant-config.md).

| Option | Default | Description |
|---|---|---|
| `Ant.minAura` | 1,000 | Minimal aura. |
| `Ant.maxAura` | 2,000 | Maximum aura. |
| `Ant.minMagicule` | 2,000 | Minimal magicule. |
| `Ant.maxMagicule` | 3,000 | Maximum magicule. |
| `Ant.size` | -0.75 | Bonus Size. |
| `Ant.maxHealth` | 15 | Bonus Max Health. |
| `Ant.maxSpiritualHealth` | 85 | Bonus Max Spiritual Health. |
| `Ant.attack` | -0.8 | Bonus Attack Damage. |
| `Ant.attackSpeed` | -0.5 | Bonus Attack Speed. |
| `Ant.knockbackResistance` | 0.3 | Bonus Knockback Resistance. |
| `Ant.movementSpeed` | -0.03 | Bonus Movement Speed. |
| `Ant.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `Ant.armor` | 5 | Bonus Armor |
| `Ant.intrinsicSkills` | "mysticism:exoskeleton", "tensura:analytical_appraisal" | The list of intrinsic skills that the race gets. |

## Tags

`tensura:races/has_creative_flight`
