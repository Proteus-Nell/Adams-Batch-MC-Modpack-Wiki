# Drone Beetle Insectar

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:drone_beetle_insectar` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 100,000 - 100,000 |
| **Magicule** | 100,000 - 100,000 |
| **Health bonus** | 130 |
| **Spiritual health bonus** | 825 |
| **Attack damage bonus** | 1.5 |
| **Movement speed bonus** | 0.075 |
| **EP to evolve into** | 100,000 |

</div>

> A Drone Beetle that has gained a humanoid body. Its wings are much stronger and capable of traveling much quicker.

> [!NOTE]
> **Pack note:** this pack changes the defaults below.
> - `General.refresh` is **false** (mod default: true)

## Evolution

- **Evolves from:** [Drone Beetle](drone-beetle.md)
- **Evolves into:** [Drone Beetle Savant](drone-beetle-savant.md), [Lightning Soul Insect](lightning-soul-insect.md)
- **Default evolution:** [Drone Beetle Savant](drone-beetle-savant.md)
- **On awakening (True Demon Lord / True Hero):** [Fantasy Soul Insect](fantasy-soul-insect.md)

### Requirements to evolve into Drone Beetle Insectar

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 100,000 | 100% |

## Traits

- Has creative-style flight

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Flying Speed | 0 | add |
| Scale | 0 | add |
| Max Health | 130 | add |
| Max Spiritual Health | 825 | add |
| Attack Damage | 1.5 | add |
| Attack Speed | 0.5 | add |
| Knockback Resistance | 0.2 | add |
| Movement Speed | 0.075 | add |
| Swim Speed Multiplier | 0 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/insect/beetle_config.toml`](../configs/config-mysticism-race-insect-beetle-config.md).

| Option | Default | Description |
|---|---|---|
| `DroneBeetleInsectar.epRequirement` | 100,000 | EP requirement to evolve into Drone Beetle Insectar. |
| `DroneBeetleInsectar.minAura` | 100,000 | Minimal aura. |
| `DroneBeetleInsectar.maxAura` | 100,000 | Maximum aura. |
| `DroneBeetleInsectar.minMagicule` | 100,000 | Minimal magicule. |
| `DroneBeetleInsectar.maxMagicule` | 100,000 | Maximum magicule. |
| `DroneBeetleInsectar.size` | 0 | Bonus Size. |
| `DroneBeetleInsectar.maxHealth` | 130 | Bonus Max Health. |
| `DroneBeetleInsectar.maxSpiritualHealth` | 825 | Bonus Max Spiritual Health. |
| `DroneBeetleInsectar.attack` | 1.5 | Bonus Attack Damage. |
| `DroneBeetleInsectar.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `DroneBeetleInsectar.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `DroneBeetleInsectar.movementSpeed` | 0.075 | Bonus Movement Speed. |
| `DroneBeetleInsectar.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `DroneBeetleInsectar.flightSpeed` | 0 | Bonus Flight Speed Multiplier. |
| `DroneBeetleInsectar.intrinsicSkills` | "mysticism:exoskeleton", "tensura:analytical_appraisal", "tensura:strength" | The list of intrinsic skills that the race gets. |
| `DroneBeetle.epRequirement` | 10,000 | EP requirement to evolve into Drone Beetle. |
| `DroneBeetle.minAura` | 5,250 | Minimal aura. |
| `DroneBeetle.maxAura` | 5,250 | Maximum aura. |
| `DroneBeetle.minMagicule` | 5,250 | Minimal magicule. |
| `DroneBeetle.maxMagicule` | 5,250 | Maximum magicule. |
| `DroneBeetle.size` | -0.65 | Bonus Size. |
| `DroneBeetle.maxHealth` | 15 | Bonus Max Health. |
| `DroneBeetle.maxSpiritualHealth` | 45 | Bonus Max Spiritual Health. |
| `DroneBeetle.attack` | 1.25 | Bonus Attack Damage. |
| `DroneBeetle.attackSpeed` | 0.2 | Bonus Attack Speed. |
| `DroneBeetle.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `DroneBeetle.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `DroneBeetle.swimSpeed` | -0.1 | Bonus Swimming Speed Multiplier. |
| `DroneBeetle.flightSpeed` | -0.01 | Bonus Flight Speed Multiplier. |
| `DroneBeetle.intrinsicSkills` | "mysticism:exoskeleton", "tensura:analytical_appraisal", "tensura:strength" | The list of intrinsic skills that the race gets. |
| `Beetle.minAura` | 1,000 | Minimal aura. |
| `Beetle.maxAura` | 2,000 | Maximum aura. |
| `Beetle.minMagicule` | 2,000 | Minimal magicule. |
| `Beetle.maxMagicule` | 3,000 | Maximum magicule. |
| `Beetle.size` | -0.6 | Bonus Size. |
| `Beetle.maxHealth` | 2 | Bonus Max Health. |
| `Beetle.maxSpiritualHealth` | 15 | Bonus Max Spiritual Health. |
| `Beetle.attack` | 1 | Bonus Attack Damage. |
| `Beetle.attackSpeed` | 0 | Bonus Attack Speed. |
| `Beetle.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Beetle.movementSpeed` | 0 | Bonus Movement Speed. |
| `Beetle.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `Beetle.intrinsicSkills` | "mysticism:exoskeleton", "tensura:analytical_appraisal", "tensura:strength" | The list of intrinsic skills that the race gets. |

Set in [`config/mysticism/general.toml`](../configs/config-mysticism-general.md).

| Option | Default | This pack | Description |
|---|---|---|---|
| `General.refresh` | true | false | Should the Tensura configurations add Mysticism's skills and races on next launch? |
| `General.flightSpeed` | 0.05 | | The default flying speed of all Mysticism races. |
| `General.seCostMultiplier` | 4 | | SE cost multiplier when acquiring a Unique Skill. Default: 4, which means the skill's magicule cost \* 4 |

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
