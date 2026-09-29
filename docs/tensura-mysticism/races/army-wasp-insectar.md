# Army Wasp Insectar

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:army_wasp_insectar` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 100,000 - 100,000 |
| **Magicule** | 100,000 - 100,000 |
| **Health bonus** | 300 |
| **Spiritual health bonus** | 2,320 |
| **Attack damage bonus** | 1.5 |
| **Movement speed bonus** | 0 |
| **EP to evolve into** | 100,000 |

</div>

> WIP

## Evolution

- **Evolves from:** [Army Wasp](army-wasp.md)
- **Evolves into:** [Army Wasp Savant](army-wasp-savant.md), [Wind Soul Insect](wind-soul-insect.md)
- **Default evolution:** [Army Wasp Savant](army-wasp-savant.md)
- **On awakening (True Demon Lord / True Hero):** [Star Soul Insect](star-soul-insect.md)

### Requirements to evolve into Army Wasp Insectar

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 100,000 | 100% |

## Traits

- Has creative-style flight

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Flying Speed | 0.01 | add |
| Flying Speed | 0 | add |
| Scale | 0.5 | add |
| Max Health | 300 | add |
| Max Spiritual Health | 2,320 | add |
| Attack Damage | 1.5 | add |
| Attack Speed | 0.25 | add |
| Knockback Resistance | 0.2 | add |
| Movement Speed | 0 | add |
| Swim Speed Multiplier | -0.3 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/insect/wasp_config.toml`](../configs/config-mysticism-race-insect-wasp-config.md).

| Option | Default | Description |
|---|---|---|
| `ArmyWaspInsectar.epRequirement` | 100,000 | EP requirement to evolve into Army Wasp Insectar. |
| `ArmyWaspInsectar.minAura` | 100,000 | Minimal aura. |
| `ArmyWaspInsectar.maxAura` | 100,000 | Maximum aura. |
| `ArmyWaspInsectar.minMagicule` | 100,000 | Minimal magicule. |
| `ArmyWaspInsectar.maxMagicule` | 100,000 | Maximum magicule. |
| `ArmyWaspInsectar.size` | 0.5 | Bonus Size. |
| `ArmyWaspInsectar.maxHealth` | 300 | Bonus Max Health. |
| `ArmyWaspInsectar.maxSpiritualHealth` | 2,320 | Bonus Max Spiritual Health. |
| `ArmyWaspInsectar.attack` | 1.5 | Bonus Attack Damage. |
| `ArmyWaspInsectar.attackSpeed` | 0.25 | Bonus Attack Speed. |
| `ArmyWaspInsectar.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `ArmyWaspInsectar.movementSpeed` | 0 | Bonus Movement Speed. |
| `ArmyWaspInsectar.swimSpeed` | -0.3 | Bonus Swimming Speed Multiplier. |
| `ArmyWaspInsectar.flightSpeed` | 0.01 | Bonus Flight Speed Multiplier. |
| `ArmyWaspInsectar.intrinsicSkills` | "mysticism:exoskeleton", "tensura:analytical_appraisal" | The list of intrinsic skills that the race gets. |
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
