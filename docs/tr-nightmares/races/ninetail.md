# Ninetail

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:ninetail` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 170,000 - 300,000 |
| **Magicule** | 320,000 - 580,000 |
| **Health bonus** | 450 |
| **Spiritual health bonus** | 720 |
| **Attack damage bonus** | 2.2 |
| **Movement speed bonus** | 0.05 |
| **EP to evolve into** | 420,000 |

</div>

> A mythical fox form that has awakened deeper soul-force and aura.

## Evolution

- **Evolves from:** [Ninehead](ninehead.md)
- **Evolves into:** [Soul Beast](soul-beast.md)
- **Default evolution:** [Soul Beast](soul-beast.md)
- **During the Harvest Festival:** [Soul Beast](soul-beast.md)

### Requirements to evolve into Ninetail

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 420,000 | 100% |

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
-  [Beast Domination](../abilities/intrinsic-skills/beast-domination.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 450 | add |
| Max Spiritual Health | 720 | add |
| Attack Damage | 2.2 | add |
| Attack Speed | 0.3 | add |
| Knockback Resistance | 0.5 | add |
| Movement Speed | 0.05 | add |
| Swim Speed Multiplier | 0.1 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/mystic_fox_config.toml`](../configs/config-nightmare-race-mystic-fox-config.md).

| Option | Default | Description |
|---|---|---|
| `Ninetail.epRequirement` | 420,000 |  |
| `Ninetail.minAura` | 170,000 |  |
| `Ninetail.maxAura` | 300,000 |  |
| `Ninetail.minMagicule` | 320,000 |  |
| `Ninetail.maxMagicule` | 580,000 |  |
| `Ninetail.size` | 0 |  |
| `Ninetail.maxHealth` | 450 |  |
| `Ninetail.maxSpiritualHealth` | 720 |  |
| `Ninetail.attack` | 2.2 |  |
| `Ninetail.attackSpeed` | 0.3 |  |
| `Ninetail.knockbackResistance` | 0.5 |  |
| `Ninetail.movementSpeed` | 0.05 |  |
| `Ninetail.swimSpeed` | 0.1 |  |
