# Ninehead

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:ninehead` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Intermediate |
| **Alignment** | Default |
| **Aura** | 70,000 - 130,000 |
| **Magicule** | 140,000 - 260,000 |
| **Health bonus** | 295 |
| **Spiritual health bonus** | 430 |
| **Attack damage bonus** | 1.7 |
| **Movement speed bonus** | 0.045 |
| **EP to evolve into** | 160,000 |

</div>

> A powerful fox evolution approaching legendary status.

## Evolution

- **Evolves from:** [Greater Mystic Fox](greater-mystic-fox.md)
- **Evolves into:** [Ninetail](ninetail.md)
- **Default evolution:** [Ninetail](ninetail.md)
- **During the Harvest Festival:** [Ninetail](ninetail.md)

### Requirements to evolve into Ninehead

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 160,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Divine Fox"]
  r1["Greater Mystic Fox"]
  r2["Lesser Mystic Fox"]
  r3["Ninehead"]
  r4["Ninetail"]
  r5["Soul Beast"]
  r1 --> r3
  r2 --> r1
  r3 --> r4
  r4 --> r5
  r5 --> r0
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/abnormal_condition_nullification.png) [Abnormal Condition Nullification](../../tensura-reincarnated/abilities/resistance-skills/abnormal-condition-nullification.md)
-  [Beast Unification](../abilities/intrinsic-skills/beast-unification.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 295 | add |
| Max Spiritual Health | 430 | add |
| Attack Damage | 1.7 | add |
| Attack Speed | 0.25 | add |
| Knockback Resistance | 0.35 | add |
| Movement Speed | 0.045 | add |
| Swim Speed Multiplier | 0.08 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/mystic_fox_config.toml`](../configs/config-nightmare-race-mystic-fox-config.md).

| Option | Default | Description |
|---|---|---|
| `Ninehead.epRequirement` | 160,000 |  |
| `Ninehead.minAura` | 70,000 |  |
| `Ninehead.maxAura` | 130,000 |  |
| `Ninehead.minMagicule` | 140,000 |  |
| `Ninehead.maxMagicule` | 260,000 |  |
| `Ninehead.size` | 0 |  |
| `Ninehead.maxHealth` | 295 |  |
| `Ninehead.maxSpiritualHealth` | 430 |  |
| `Ninehead.attack` | 1.7 |  |
| `Ninehead.attackSpeed` | 0.25 |  |
| `Ninehead.knockbackResistance` | 0.35 |  |
| `Ninehead.movementSpeed` | 0.045 |  |
| `Ninehead.swimSpeed` | 0.08 |  |
