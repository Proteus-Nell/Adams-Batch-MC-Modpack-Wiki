# Phantom

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:phantom` |
| **Difficulty** | Hard |
| **Alignment** | Majin |
| **Aura** | 2,500 - 3,500 |
| **Magicule** | 5,500 - 6,500 |
| **Health bonus** | 15 |
| **Spiritual health bonus** | 70 |
| **Attack damage bonus** | 0.3 |
| **Movement speed bonus** | 0.01 |

</div>

> A demi-spiritual creature born in the Underworld by the magicules of the World Destroying Dragon.

## Evolution

- **Evolves into:** [Field Officer](field-officer.md)
- **Default evolution:** [Field Officer](field-officer.md)
- **On awakening (True Demon Lord / True Hero):** [Staff Officer](staff-officer.md)
- **During the Harvest Festival:** [Field Officer](field-officer.md)

### Evolution tree

```mermaid
flowchart LR
  r0["Field Officer"]
  r1["General"]
  r2["Mystic Angel"]
  r3["Phantom"]
  r4["Staff Officer"]
  r0 --> r1
  r0 --> r4
  r1 --> r4
  r3 --> r0
  r3 --> r4
  r4 --> r2
```

## Traits

- Spawns as a spiritual lifeform

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 15 | add |
| Max Spiritual Health | 70 | add |
| Attack Damage | 0.3 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0.1 | add |
| Movement Speed | 0.01 | add |
| Swim Speed Multiplier | 0 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/phantom_config.toml`](../configs/config-mysticism-race-phantom-config.md).

| Option | Default | Description |
|---|---|---|
| `Phantom.essenceRequired` | 1 | Quantity of cryptid essence required to become a phantom as a lesser angel. |
| `Phantom.minAura` | 2,500 | Minimal aura. |
| `Phantom.maxAura` | 3,500 | Maximum aura. |
| `Phantom.minMagicule` | 5,500 | Minimal magicule. |
| `Phantom.maxMagicule` | 6,500 | Maximum magicule. |
| `Phantom.size` | 0 | Bonus Size. |
| `Phantom.maxHealth` | 15 | Bonus Max Health. |
| `Phantom.maxSpiritualHealth` | 70 | Bonus Max Spiritual Health. |
| `Phantom.attack` | 0.3 | Bonus Attack Damage. |
| `Phantom.attackSpeed` | 0 | Bonus Attack Speed. |
| `Phantom.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `Phantom.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `Phantom.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `Phantom.intrinsicSkills` | "tensura:magic_resistance", "tensura:possession" | The list of intrinsic skills that the race gets. |

## Tags

`tensura:races/spawn_as_spiritual`
