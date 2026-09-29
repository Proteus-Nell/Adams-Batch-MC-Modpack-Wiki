# Lesser Pyre Wyrm

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:lesser_pyre_wyrm` |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 1,500 - 2,000 |
| **Magicule** | 2,000 - 2,500 |
| **Health bonus** | 30 |
| **Spiritual health bonus** | 120 |
| **Attack damage bonus** | 1.5 |
| **Movement speed bonus** | 0.03 |

</div>

> A race of wyrm that live hottest deserts, thriving on the heat and all those that live in it.

## Evolution

- **Evolves from:** [Attuned Wyrm](attuned-wyrm.md)
- **Evolves into:** [Greater Pyre Wyrm](greater-pyre-wyrm.md)
- **Default evolution:** [Greater Pyre Wyrm](greater-pyre-wyrm.md)
- **On awakening (True Demon Lord / True Hero):** [Frostcoil Sea Serpent](frostcoil-sea-serpent.md)
- **During the Harvest Festival:** [Greater Pyre Wyrm](greater-pyre-wyrm.md)

### Requirements to evolve into Lesser Pyre Wyrm

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Consume 1 of [Flame Essence](../items/materials/flame-essence.md) | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Attuned Wyrm"]
  r1["Frostcoil Sea Serpent"]
  r2["Frostwrought Leviathan"]
  r3["Greater Glacier Wyrm"]
  r4["Greater Pyre Wyrm"]
  r5["Lesser Glacier Wyrm"]
  r6["Lesser Pyre Wyrm"]
  r7["Rimeblight Hydra"]
  r8["Rimefang Drake"]
  r9["Scorchtail Salamander"]
  r10["Scorchtalon Wyvern"]
  r11["Sundeity Loong"]
  r12["Sunfire Lindwurm"]
  r0 --> r1
  r0 --> r5
  r0 --> r6
  r1 --> r2
  r3 --> r1
  r3 --> r8
  r4 --> r1
  r4 --> r9
  r4 --> r12
  r5 --> r1
  r5 --> r3
  r6 --> r1
  r6 --> r4
  r8 --> r7
  r9 --> r10
  r12 --> r11
```

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0.5 | add |
| Max Health | 30 | add |
| Max Spiritual Health | 120 | add |
| Attack Damage | 1.5 | add |
| Attack Speed | 0.5 | add |
| Knockback Resistance | 0.04 | add |
| Movement Speed | 0.03 | add |
| Swim Speed Multiplier | 0.03 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/wyrm_config.toml`](../configs/config-mysticism-race-wyrm-config.md).

| Option | Default | Description |
|---|---|---|
| `LesserPyreWyrm.minAura` | 1,500 | Minimal aura. |
| `LesserPyreWyrm.maxAura` | 2,000 | Maximum aura. |
| `LesserPyreWyrm.minMagicule` | 2,000 | Minimal magicule. |
| `LesserPyreWyrm.maxMagicule` | 2,500 | Maximum magicule. |
| `LesserPyreWyrm.size` | 0.5 | Bonus Size. |
| `LesserPyreWyrm.maxHealth` | 30 | Bonus Max Health. |
| `LesserPyreWyrm.maxSpiritualHealth` | 120 | Bonus Max Spiritual Health. |
| `LesserPyreWyrm.attack` | 1.5 | Bonus Attack Damage. |
| `LesserPyreWyrm.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `LesserPyreWyrm.knockbackResistance` | 0.04 | Bonus Knockback Resistance. |
| `LesserPyreWyrm.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `LesserPyreWyrm.swimSpeed` | 0.03 | Bonus Swimming Speed Multiplier. |
| `LesserPyreWyrm.flameEssenceAmount` | 1 | Amount of Flame Essence needed eaten to evolve into a Lesser Pyre Wyrm. |
| `LesserPyreWyrm.intrinsicSkills` | "tensura:flame_attack_resistance" | The list of intrinsic skills that the race gets. |
| `AttunedWyrm.minAura` | 500 | Minimal aura. |
| `AttunedWyrm.maxAura` | 1,000 | Maximum aura. |
| `AttunedWyrm.minMagicule` | 1,500 | Minimal magicule. |
| `AttunedWyrm.maxMagicule` | 2,000 | Maximum magicule. |
| `AttunedWyrm.size` | 0.3 | Bonus Size. |
| `AttunedWyrm.maxHealth` | 0 | Bonus Max Health. |
| `AttunedWyrm.maxSpiritualHealth` | 0 | Bonus Max Spiritual Health. |
| `AttunedWyrm.attack` | 1 | Bonus Attack Damage. |
| `AttunedWyrm.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `AttunedWyrm.knockbackResistance` | 1 | Bonus Knockback Resistance. |
| `AttunedWyrm.movementSpeed` | 0 | Bonus Movement Speed. |
| `AttunedWyrm.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `AttunedWyrm.intrinsicSkills` | [] (empty) | The list of intrinsic skills that the race gets. |
