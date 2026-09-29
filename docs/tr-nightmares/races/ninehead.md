# Ninehead

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:ninehead` |
| **Difficulty** | Intermediate |
| **Alignment** | Default |
| **Aura** | 1,000 - 2,000 |
| **Magicule** | 2,000 - 4,000 |
| **Health bonus** | 15 |
| **Spiritual health bonus** | 60 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0 |
| **EP to evolve into** | 0 |

</div>

> A powerful fox evolution approaching legendary status.

## Evolution

- **Evolves from:** [Greater Mystic Fox](greater-mystic-fox.md)
- **Evolves into:** [Ninetail](ninetail.md)
- **Default evolution:** [Ninetail](ninetail.md)

### Requirements to evolve into Ninehead

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of ep requirement | 100% |

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
| Scale | size | add |
| Max Health | max HP | add |
| Max Spiritual Health | max spiritual HP | add |
| Attack Damage | attack | add |
| Attack Speed | attack speed | add |
| Knockback Resistance | knockback resistance | add |
| Movement Speed | movement speed | add |
| Swim Speed Multiplier | swim speed | add |

## Stats (config defaults)

Set in [`config/nightmare/race/mystic_fox_config.toml`](../configs/config-nightmare-race-mystic-fox-config.md).

| Option | Default | Description |
|---|---|---|
| `Ninehead.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `Ninehead.minAura` | 1,000 | Minimal aura. |
| `Ninehead.maxAura` | 2,000 | Maximum aura. |
| `Ninehead.minMagicule` | 2,000 | Minimal magicule. |
| `Ninehead.maxMagicule` | 4,000 | Maximum magicule. |
| `Ninehead.size` | 0 | Bonus Size. |
| `Ninehead.maxHealth` | 15 | Bonus Max Health. |
| `Ninehead.maxSpiritualHealth` | 60 | Bonus Max Spiritual Health. |
| `Ninehead.attack` | 0 | Bonus Attack Damage. |
| `Ninehead.attackSpeed` | 0 | Bonus Attack Speed. |
| `Ninehead.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Ninehead.movementSpeed` | 0 | Bonus Movement Speed. |
| `Ninehead.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
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
