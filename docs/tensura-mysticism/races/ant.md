# Ant

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:ant` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 1,000 - 2,000 |
| **Magicule** | 2,000 - 3,000 |
| **Health bonus** | 15 |
| **Spiritual health bonus** | 85 |
| **Attack damage bonus** | -0.8 |
| **Movement speed bonus** | -0.03 |

</div>

> Ants are fearless critters that have absurdly tanky exoskeletons, known for being bulky and hard to take down. Prepare for a long, drawn out battle if you encounter one!

## Evolution

- **Evolves from:** [Insect](insect.md)
- **Evolves into:** [Fire Ant](fire-ant.md), [Hardshell Ant](hardshell-ant.md)
- **Default evolution:** [Hardshell Ant](hardshell-ant.md)
- **On awakening (True Demon Lord / True Hero):** [Earth Soul Insect](earth-soul-insect.md)
- **During the Harvest Festival:** [Hardshell Ant](hardshell-ant.md)

### Requirements to evolve into Ant

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 3,000 | 100% |

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Armor | 5 | add |
| Scale | -0.75 | add |
| Max Health | 15 | add |
| Max Spiritual Health | 85 | add |
| Attack Damage | -0.8 | add |
| Attack Speed | -0.5 | add |
| Knockback Resistance | 0.3 | add |
| Movement Speed | -0.03 | add |
| Swim Speed Multiplier | 0 | add |

## Stats (config defaults)

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
