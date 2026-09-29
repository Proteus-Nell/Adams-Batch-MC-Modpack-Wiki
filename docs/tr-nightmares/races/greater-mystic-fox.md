# Greater Mystic Fox

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:greater_mystic_fox` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Easy |
| **Alignment** | Default |
| **Aura** | 18,000 - 34,000 |
| **Magicule** | 36,000 - 72,000 |
| **Health bonus** | 155 |
| **Spiritual health bonus** | 230 |
| **Attack damage bonus** | 1.1 |
| **Movement speed bonus** | 0.04 |
| **EP to evolve into** | 45,000 |

</div>

> A developed mystic fox with sharpened perception and spiritual power.

## Evolution

- **Evolves from:** [Lesser Mystic Fox](lesser-mystic-fox.md)
- **Evolves into:** [Ninehead](ninehead.md)
- **Default evolution:** [Ninehead](ninehead.md)
- **During the Harvest Festival:** [Ninehead](ninehead.md)

### Requirements to evolve into Greater Mystic Fox

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 45,000 | 100% |

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

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | -0.5 | add |
| Max Health | 155 | add |
| Max Spiritual Health | 230 | add |
| Attack Damage | 1.1 | add |
| Attack Speed | 0.2 | add |
| Knockback Resistance | 0.2 | add |
| Movement Speed | 0.04 | add |
| Swim Speed Multiplier | 0.05 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/mystic_fox_config.toml`](../configs/config-nightmare-race-mystic-fox-config.md).

| Option | Default | Description |
|---|---|---|
| `GreaterMysticFox.epRequirement` | 45,000 |  |
| `GreaterMysticFox.minAura` | 18,000 |  |
| `GreaterMysticFox.maxAura` | 34,000 |  |
| `GreaterMysticFox.minMagicule` | 36,000 |  |
| `GreaterMysticFox.maxMagicule` | 72,000 |  |
| `GreaterMysticFox.size` | -0.5 |  |
| `GreaterMysticFox.maxHealth` | 155 |  |
| `GreaterMysticFox.maxSpiritualHealth` | 230 |  |
| `GreaterMysticFox.attack` | 1.1 |  |
| `GreaterMysticFox.attackSpeed` | 0.2 |  |
| `GreaterMysticFox.knockbackResistance` | 0.2 |  |
| `GreaterMysticFox.movementSpeed` | 0.04 |  |
| `GreaterMysticFox.swimSpeed` | 0.05 |  |
