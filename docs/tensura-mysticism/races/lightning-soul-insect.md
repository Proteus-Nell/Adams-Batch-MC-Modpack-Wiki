# Lightning Soul Insect

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:lightning_soul_insect` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 400,000 - 400,000 |
| **Magicule** | 400,000 - 400,000 |
| **Health bonus** | 380 |
| **Spiritual health bonus** | 6,265 |
| **Attack damage bonus** | 2 |
| **Movement speed bonus** | 0.15 |
| **EP to evolve into** | 400,000 |

</div>

> A Drone Beetle that has evolved "the right way" and became a spiritual life-form. It embodies the element of Lightning perfectly, rupturing the battlefield and being nigh untouchable.

> [!NOTE]
> **Pack note:** this pack changes the defaults below.
> - `General.refresh` is **false** (mod default: true)

## Evolution

- **Evolves from:** [Drone Beetle Insectar](drone-beetle-insectar.md), [Beetle](beetle.md)
- **Evolves into:** [Divine Drone Beetle](divine-drone-beetle.md)
- **Default evolution:** [Divine Drone Beetle](divine-drone-beetle.md)
- **On awakening (True Demon Lord / True Hero):** [Divine Drone Beetle](divine-drone-beetle.md)

### Requirements to evolve into Lightning Soul Insect

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 400,000 | 50% |
| Acquire [Lightning Manipulation](../../tensura-reincarnated/abilities/extra-skills/lightning-manipulation.md) | 50% |

## Traits

- Has creative-style flight
- Spiritual lifeform

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Flying Speed | 0.02 | add |
| Flying Speed | 0 | add |
| Scale | -0.25 | add |
| Max Health | 380 | add |
| Max Spiritual Health | 6,265 | add |
| Attack Damage | 2 | add |
| Attack Speed | 1.5 | add |
| Knockback Resistance | 0.3 | add |
| Movement Speed | 0.15 | add |
| Swim Speed Multiplier | 0.15 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/insect/beetle_config.toml`](../configs/config-mysticism-race-insect-beetle-config.md).

| Option | Default | Description |
|---|---|---|
| `LightningSoulInsect.epRequirement` | 400,000 | EP requirement to evolve into Lightning Soul Insect. |
| `LightningSoulInsect.abilityRequirement` | "tensura:lightning_manipulation" | The ability needed to evolve into Lightning Soul Insect. |
| `LightningSoulInsect.minAura` | 400,000 | Minimal aura. |
| `LightningSoulInsect.maxAura` | 400,000 | Maximum aura. |
| `LightningSoulInsect.minMagicule` | 400,000 | Minimal magicule. |
| `LightningSoulInsect.maxMagicule` | 400,000 | Maximum magicule. |
| `LightningSoulInsect.size` | -0.25 | Bonus Size. |
| `LightningSoulInsect.maxHealth` | 380 | Bonus Max Health. |
| `LightningSoulInsect.maxSpiritualHealth` | 6,265 | Bonus Max Spiritual Health. |
| `LightningSoulInsect.attack` | 2 | Bonus Attack Damage. |
| `LightningSoulInsect.attackSpeed` | 1.5 | Bonus Attack Speed. |
| `LightningSoulInsect.knockbackResistance` | 0.3 | Bonus Knockback Resistance. |
| `LightningSoulInsect.movementSpeed` | 0.15 | Bonus Movement Speed. |
| `LightningSoulInsect.swimSpeed` | 0.15 | Bonus Swimming Speed Multiplier. |
| `LightningSoulInsect.flightSpeed` | 0.02 | Bonus Flight Speed Multiplier. |
| `LightningSoulInsect.intrinsicSkills` | "mysticism:exoskeleton", "tensura:analytical_appraisal", "tensura:strength", "tensura:lightning_manipulation", "tensura:electricity_resistance", "mysticism:lightning_mode" | The list of intrinsic skills that the race gets. |
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

`tensura:races/has_creative_flight`, `tensura:races/spiritual`
