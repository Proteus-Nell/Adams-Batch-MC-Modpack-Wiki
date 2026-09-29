# Wasp

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:wasp` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 1,000 - 2,000 |
| **Magicule** | 2,000 - 3,000 |
| **Health bonus** | 4 |
| **Spiritual health bonus** | 35 |
| **Attack damage bonus** | -0.5 |
| **Movement speed bonus** | 0 |

</div>

> Wasps are frail insects that have the innate ability to fly. Though they aren't quick, they have great versatility, and it all exists to protect the Queen.

> [!NOTE]
> **Pack note:** this pack changes the defaults below.
> - `General.refresh` is **false** (mod default: true)

## Evolution

- **Evolves from:** [Insect](insect.md)
- **Evolves into:** [Army Wasp](army-wasp.md), [Queen Wasp](queen-wasp.md)
- **Default evolution:** [Army Wasp](army-wasp.md)
- **On awakening (True Demon Lord / True Hero):** [Wind Soul Insect](wind-soul-insect.md)
- **During the Harvest Festival:** [Army Wasp](army-wasp.md)

### Requirements to evolve into Wasp

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 3,000 | 100% |

## Traits

- Has creative-style flight

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | -0.75 | add |
| Max Health | 4 | add |
| Max Spiritual Health | 35 | add |
| Attack Damage | -0.5 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0 | add |
| Movement Speed | 0 | add |
| Swim Speed Multiplier | -0.3 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/insect/wasp_config.toml`](../configs/config-mysticism-race-insect-wasp-config.md).

| Option | Default | Description |
|---|---|---|
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
