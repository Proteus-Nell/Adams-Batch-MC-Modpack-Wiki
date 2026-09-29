# Ninetail

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:ninetail` |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 1,000 - 2,000 |
| **Magicule** | 2,000 - 4,000 |
| **Health bonus** | 15 |
| **Spiritual health bonus** | 60 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0 |
| **EP to evolve into** | 0 |

</div>

> A mythical fox form that has awakened deeper soul-force and aura.

## Evolution

- **Evolves from:** [Ninehead](ninehead.md)
- **Evolves into:** [Soul Beast](soul-beast.md)
- **Default evolution:** [Soul Beast](soul-beast.md)

### Requirements to evolve into Ninetail

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
-  [Beast Domination](../abilities/intrinsic-skills/beast-domination.md)

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
| `Ninetail.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `Ninetail.minAura` | 1,000 | Minimal aura. |
| `Ninetail.maxAura` | 2,000 | Maximum aura. |
| `Ninetail.minMagicule` | 2,000 | Minimal magicule. |
| `Ninetail.maxMagicule` | 4,000 | Maximum magicule. |
| `Ninetail.size` | 0 | Bonus Size. |
| `Ninetail.maxHealth` | 15 | Bonus Max Health. |
| `Ninetail.maxSpiritualHealth` | 60 | Bonus Max Spiritual Health. |
| `Ninetail.attack` | 0 | Bonus Attack Damage. |
| `Ninetail.attackSpeed` | 0 | Bonus Attack Speed. |
| `Ninetail.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Ninetail.movementSpeed` | 0 | Bonus Movement Speed. |
| `Ninetail.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
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
