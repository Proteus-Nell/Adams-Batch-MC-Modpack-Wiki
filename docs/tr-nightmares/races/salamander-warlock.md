# Salamander Warlock

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:salamander_warlock` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Hard |
| **Alignment** | Majin |
| **Aura** | 500 - 1,500 |
| **Magicule** | 1,500 - 5,500 |
| **Health bonus** | 90 |
| **Spiritual health bonus** | 640 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0.02 |
| **EP to evolve into** | 50,000 |

</div>

## Evolution

- **Evolves from:** [Salamander](salamander.md)
- **Evolves into:** [Salamander Fire Spirit](salamander-fire-spirit.md)
- **Default evolution:** [Salamander Fire Spirit](salamander-fire-spirit.md)
- **On awakening (True Demon Lord / True Hero):** [Salamander Fire Spirit](salamander-fire-spirit.md)
- **During the Harvest Festival:** [Salamander Fire Spirit](salamander-fire-spirit.md)

### Requirements to evolve into Salamander Warlock

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 50,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Salamander"]
  r1["Salamander Assassin"]
  r2["Salamander Fire Spirit Dragon"]
  r3["Salamander Fire Spirit"]
  r4["Salamander Poison Spirit Dragon"]
  r5["Salamander Poison Spirit"]
  r6["Salamander Warlock"]
  r0 --> r1
  r0 --> r6
  r1 --> r5
  r3 --> r2
  r5 --> r4
  r6 --> r3
```

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | -1.1 | add |
| Max Health | 90 | add |
| Max Spiritual Health | 640 | add |
| Attack Damage | 0 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0.5 | add |
| Movement Speed | 0.02 | add |
| Swim Speed Multiplier | 0.5 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/axolotl/salamander_config.toml`](../configs/config-nightmare-race-axolotl-salamander-config.md).

| Option | Default | Description |
|---|---|---|
| `SalamanderWarlock.epRequirement` | 50,000 | EP requirement to evolve. |
| `SalamanderWarlock.minAura` | 500 | Minimal aura. |
| `SalamanderWarlock.maxAura` | 1,500 | Maximum aura. |
| `SalamanderWarlock.minMagicule` | 1,500 | Minimal magicule. |
| `SalamanderWarlock.maxMagicule` | 5,500 | Maximum magicule. |
| `SalamanderWarlock.size` | -1.1 | Bonus Size. |
| `SalamanderWarlock.maxHealth` | 90 | Bonus Max Health. |
| `SalamanderWarlock.maxSpiritualHealth` | 640 | Bonus Max Spiritual Health. |
| `SalamanderWarlock.attack` | 0 | Bonus Attack Damage. |
| `SalamanderWarlock.attackSpeed` | 0 | Bonus Attack Speed. |
| `SalamanderWarlock.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `SalamanderWarlock.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `SalamanderWarlock.swimSpeed` | 0.5 | Bonus Swimming Speed Multiplier. |
| `SalamanderWarlock.intrinsicSkills` | "tensura:thermal_fluctuation_resistance", "tensura:dragon_ear" | List of skills obtained by this race. |
| `Salamander.minAura` | 500 | Minimal aura. |
| `Salamander.maxAura` | 1,500 | Maximum aura. |
| `Salamander.minMagicule` | 1,500 | Minimal magicule. |
| `Salamander.maxMagicule` | 5,500 | Maximum magicule. |
| `Salamander.size` | -1.1 | Bonus Size. |
| `Salamander.maxHealth` | -15 | Bonus Max Health. |
| `Salamander.maxSpiritualHealth` | -10 | Bonus Max Spiritual Health. |
| `Salamander.attack` | 0 | Bonus Attack Damage. |
| `Salamander.attackSpeed` | 0 | Bonus Attack Speed. |
| `Salamander.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `Salamander.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `Salamander.swimSpeed` | 0.3 | Bonus Swimming Speed Multiplier. |
| `Salamander.intrinsicSkills` | "tensura:self_regeneration", "tensura:absorb_and_dissolve", "tensura:fire_breath", "tensura:poison", "tensura:poison_resistance" | List of skills obtained by this race. |
