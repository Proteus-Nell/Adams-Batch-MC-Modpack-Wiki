# Soul Beast

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:soul_beast` |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 360,000 - 650,000 |
| **Magicule** | 700,000 - 1,250,000 |
| **Health bonus** | 600 |
| **Spiritual health bonus** | 4,200 |
| **Attack damage bonus** | 2.9 |
| **Movement speed bonus** | 0.055 |
| **EP to evolve into** | 900,000 |

</div>

> A transcendent fox spirit fused with vast spiritual essence.

## Evolution

- **Evolves from:** [Ninetail](ninetail.md)
- **Evolves into:** [Divine Fox](divine-fox.md)
- **Default evolution:** [Divine Fox](divine-fox.md)

### Requirements to evolve into Soul Beast

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 900,000 | 100% |

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
| Max Health | 600 | add |
| Max Spiritual Health | 4,200 | add |
| Attack Damage | 2.9 | add |
| Attack Speed | 0.35 | add |
| Knockback Resistance | 0.7 | add |
| Movement Speed | 0.055 | add |
| Swim Speed Multiplier | 0.12 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/mystic_fox_config.toml`](../configs/config-nightmare-race-mystic-fox-config.md).

| Option | Default | Description |
|---|---|---|
| `SoulBeast.epRequirement` | 900,000 |  |
| `SoulBeast.minAura` | 360,000 |  |
| `SoulBeast.maxAura` | 650,000 |  |
| `SoulBeast.minMagicule` | 700,000 |  |
| `SoulBeast.maxMagicule` | 1,250,000 |  |
| `SoulBeast.size` | 0 |  |
| `SoulBeast.maxHealth` | 600 |  |
| `SoulBeast.maxSpiritualHealth` | 4,200 |  |
| `SoulBeast.attack` | 2.9 |  |
| `SoulBeast.attackSpeed` | 0.35 |  |
| `SoulBeast.knockbackResistance` | 0.7 |  |
| `SoulBeast.movementSpeed` | 0.055 |  |
| `SoulBeast.swimSpeed` | 0.12 |  |
