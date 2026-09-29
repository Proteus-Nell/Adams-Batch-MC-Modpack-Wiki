# Giant Elder

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:giant_elder` |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 24,000 - 48,000 |
| **Magicule** | 40,000 - 80,000 |
| **Health bonus** | 330 |
| **Spiritual health bonus** | 1,140 |
| **Attack damage bonus** | 3 |
| **Movement speed bonus** | 0.05 |
| **EP to evolve into** | 80,000 |

</div>

## Evolution

- **Evolves from:** [Giant Dancer](giant-dancer.md), [Giant Warrior](giant-warrior.md)
- **Evolves into:** [Fang of Earth](fang-of-earth.md)
- **Default evolution:** [Fang of Earth](fang-of-earth.md)
- **On awakening (True Demon Lord / True Hero):** [Fang of Earth](fang-of-earth.md)
- **During the Harvest Festival:** [Fang of Earth](fang-of-earth.md)

### Requirements to evolve into Giant Elder

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of ep requirement | 100% |

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

- ![](../../assets/icons/tensura/skill/flame_attack_resistance.png) [Flame Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/flame-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/poison_resistance.png) [Poison Resistance](../../tensura-reincarnated/abilities/resistance-skills/poison-resistance.md)
- ![](../../assets/icons/tensura/skill/earth_domination.png) [Earth Domination](../../tensura-reincarnated/abilities/extra-skills/earth-domination.md)
- ![](../../assets/icons/tensura/skill/body_armor.png) [Body Armor](../../tensura-reincarnated/abilities/intrinsic-skills/body-armor.md)
-  [Size Condense](../abilities/intrinsic-skills/size-condense.md)

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

Set in [`config/nightmare/race/giant_clan_config.toml`](../configs/config-nightmare-race-giant-clan-config.md).

| Option | Default | Description |
|---|---|---|
| `GiantElder.epRequirement` | 80,000 | Existence points required to evolve into Giant Elder. |
| `GiantElder.minAura` | 24,000 | Minimal aura. |
| `GiantElder.maxAura` | 48,000 | Maximum aura. |
| `GiantElder.minMagicule` | 40,000 | Minimal magicule. |
| `GiantElder.maxMagicule` | 80,000 | Maximum magicule. |
| `GiantElder.size` | 1 | Bonus Size. |
| `GiantElder.maxHealth` | 330 | Bonus Max Health. |
| `GiantElder.maxSpiritualHealth` | 1,140 | Bonus Max Spiritual Health. |
| `GiantElder.attack` | 3 | Bonus Attack Damage. |
| `GiantElder.attackSpeed` | 1 | Bonus Attack Speed. |
| `GiantElder.knockbackResistance` | 0.7 | Bonus Knockback Resistance. |
| `GiantElder.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `GiantElder.swimSpeed` | 0.05 | Bonus Swimming Speed Multiplier. |
| `GiantWarrior.epRequirement` | 40,000 | Existence points required to evolve into Giant Warrior. |
| `GiantWarrior.minAura` | 25,000 | Minimal aura. |
| `GiantWarrior.maxAura` | 50,000 | Maximum aura. |
| `GiantWarrior.minMagicule` | 15,000 | Minimal magicule. |
| `GiantWarrior.maxMagicule` | 30,000 | Maximum magicule. |
| `GiantWarrior.size` | 0.5 | Bonus Size. |
| `GiantWarrior.maxHealth` | 330 | Bonus Max Health. |
| `GiantWarrior.maxSpiritualHealth` | 940 | Bonus Max Spiritual Health. |
| `GiantWarrior.attack` | 3.5 | Bonus Attack Damage. |
| `GiantWarrior.attackSpeed` | 0 | Bonus Attack Speed. |
| `GiantWarrior.knockbackResistance` | 0.8 | Bonus Knockback Resistance. |
| `GiantWarrior.movementSpeed` | 0.04 | Bonus Movement Speed. |
| `GiantWarrior.swimSpeed` | 0.04 | Bonus Swimming Speed Multiplier. |
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
