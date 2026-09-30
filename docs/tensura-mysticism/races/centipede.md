# Centipede

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:centipede` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 1,000 - 2,000 |
| **Magicule** | 2,000 - 3,000 |
| **Health bonus** | 4 |
| **Spiritual health bonus** | 35 |
| **Attack damage bonus** | 0.5 |
| **Movement speed bonus** | 0.3 |

</div>

> Centipedes are fast, speed-oriented insects that can escape virtually any fight. Their many legs makes up for their lack of power.

## Evolution

- **Evolves from:** [Insect](insect.md)
- **Evolves into:** [Yellow Centipede](yellow-centipede.md), [Blue Centipede](blue-centipede.md), [Purple Centipede](purple-centipede.md)
- **Default evolution:** [Yellow Centipede](yellow-centipede.md)
- **On awakening (True Demon Lord / True Hero):** [Paralysis Soul Insect](paralysis-soul-insect.md)
- **During the Harvest Festival:** [Yellow Centipede](yellow-centipede.md)

### Requirements to evolve into Centipede

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 3,000 | 100% |

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | -0.75 | add |
| Max Health | 4 | add |
| Max Spiritual Health | 35 | add |
| Attack Damage | 0.5 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0 | add |
| Movement Speed | 0.3 | add |
| Swim Speed Multiplier | -0.5 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/insect/centipede_config.toml`](../configs/config-mysticism-race-insect-centipede-config.md).

| Option | Default | Description |
|---|---|---|
| `Centipede.minAura` | 1,000 | Minimal aura. |
| `Centipede.maxAura` | 2,000 | Maximum aura. |
| `Centipede.minMagicule` | 2,000 | Minimal magicule. |
| `Centipede.maxMagicule` | 3,000 | Maximum magicule. |
| `Centipede.size` | -0.75 | Bonus Size. |
| `Centipede.maxHealth` | 4 | Bonus Max Health. |
| `Centipede.maxSpiritualHealth` | 35 | Bonus Max Spiritual Health. |
| `Centipede.attack` | 0.5 | Bonus Attack Damage. |
| `Centipede.attackSpeed` | 0 | Bonus Attack Speed. |
| `Centipede.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Centipede.movementSpeed` | 0.3 | Bonus Movement Speed. |
| `Centipede.swimSpeed` | -0.5 | Bonus Swimming Speed Multiplier. |
| `Centipede.intrinsicSkills` | "mysticism:exoskeleton", "tensura:analytical_appraisal", "tensura:paralysis" | The list of intrinsic skills that the race gets. |

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
