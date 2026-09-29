# Salamander

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:salamander` |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 500 - 1,500 |
| **Magicule** | 1,500 - 5,500 |
| **Health bonus** | -15 |
| **Spiritual health bonus** | -10 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0.02 |

</div>

> A fierce reptilian race born from volcanic flame, driven by heat, ambition, and relentless will.

## Evolution

- **Evolves into:** [Salamander Assassin](salamander-assassin.md), [Salamander Warlock](salamander-warlock.md)
- **Default evolution:** [Salamander Assassin](salamander-assassin.md)
- **On awakening (True Demon Lord / True Hero):** [Salamander Assassin](salamander-assassin.md)
- **During the Harvest Festival:** [Salamander Assassin](salamander-assassin.md)

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
| Max Health | -15 | add |
| Max Spiritual Health | -10 | add |
| Attack Damage | 0 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0.5 | add |
| Movement Speed | 0.02 | add |
| Swim Speed Multiplier | 0.3 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/axolotl/salamander_config.toml`](../configs/config-nightmare-race-axolotl-salamander-config.md).

| Option | Default | Description |
|---|---|---|
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
