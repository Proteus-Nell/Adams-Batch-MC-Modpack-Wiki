# Giant Dancer

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:giant_dancer` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 25,000 - 50,000 |
| **Magicule** | 15,000 - 30,000 |
| **Health bonus** | 300 |
| **Spiritual health bonus** | 840 |
| **Attack damage bonus** | 2 |
| **Movement speed bonus** | 0.07 |
| **EP to evolve into** | 40,000 |

</div>

## Evolution

- **Evolves from:** [Lesser Giant](lesser-giant.md)
- **Evolves into:** [Big Cutie](big-cutie.md), [Giant Elder](giant-elder.md)
- **Default evolution:** [Giant Elder](giant-elder.md)
- **On awakening (True Demon Lord / True Hero):** [Giant Elder](giant-elder.md)
- **During the Harvest Festival:** [Giant Elder](giant-elder.md)

### Requirements to evolve into Giant Dancer

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 40,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Big Cutie"]
  r1["Earthshaker pDancer"]
  r2["Fang of Earth"]
  r3["Giant Dancer"]
  r4["Giant Elder"]
  r5["Giant King"]
  r6["Giant Queen"]
  r7["Giant Warrior"]
  r8["God Of Earth"]
  r9["Lesser Giant"]
  r10["Mutant Giant"]
  r11["One Eyed God"]
  r0 --> r1
  r1 --> r6
  r2 --> r5
  r3 --> r0
  r3 --> r4
  r4 --> r2
  r7 --> r4
  r7 --> r10
  r9 --> r3
  r9 --> r7
  r10 --> r11
  r11 --> r8
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/earth_attack_resistance.png) [Earth Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/earth-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/physical_attack_resistance.png) [Physical Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/physical-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/earth_manipulation.png) [Earth Manipulation](../../tensura-reincarnated/abilities/extra-skills/earth-manipulation.md)
-  [Size Condense](../abilities/intrinsic-skills/size-condense.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0.5 | add |
| Max Health | 300 | add |
| Max Spiritual Health | 840 | add |
| Attack Damage | 2 | add |
| Attack Speed | 1 | add |
| Knockback Resistance | 0.5 | add |
| Movement Speed | 0.07 | add |
| Swim Speed Multiplier | 0.07 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/giant_clan_config.toml`](../configs/config-nightmare-race-giant-clan-config.md).

| Option | Default | Description |
|---|---|---|
| `GiantDancer.epRequirement` | 40,000 | Existence points required to evolve into Giant Dancer. |
| `GiantDancer.minAura` | 25,000 | Minimal aura. |
| `GiantDancer.maxAura` | 50,000 | Maximum aura. |
| `GiantDancer.minMagicule` | 15,000 | Minimal magicule. |
| `GiantDancer.maxMagicule` | 30,000 | Maximum magicule. |
| `GiantDancer.size` | 0.5 | Bonus Size. |
| `GiantDancer.maxHealth` | 300 | Bonus Max Health. |
| `GiantDancer.maxSpiritualHealth` | 840 | Bonus Max Spiritual Health. |
| `GiantDancer.attack` | 2 | Bonus Attack Damage. |
| `GiantDancer.attackSpeed` | 1 | Bonus Attack Speed. |
| `GiantDancer.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `GiantDancer.movementSpeed` | 0.07 | Bonus Movement Speed. |
| `GiantDancer.swimSpeed` | 0.07 | Bonus Swimming Speed Multiplier. |
| `LesserGiant.minAura` | 500 | Minimal aura. |
| `LesserGiant.maxAura` | 500 | Maximum aura. |
| `LesserGiant.minMagicule` | 1,500 | Minimal magicule. |
| `LesserGiant.maxMagicule` | 5,500 | Maximum magicule. |
| `LesserGiant.size` | 0.5 | Bonus Size. |
| `LesserGiant.maxHealth` | 80 | Bonus Max Health. |
| `LesserGiant.maxSpiritualHealth` | 240 | Bonus Max Spiritual Health. |
| `LesserGiant.attack` | 2 | Bonus Attack Damage. |
| `LesserGiant.attackSpeed` | 0 | Bonus Attack Speed. |
| `LesserGiant.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `LesserGiant.movementSpeed` | 0.04 | Bonus Movement Speed. |
| `LesserGiant.swimSpeed` | 0.04 | Bonus Swimming Speed Multiplier. |
