# Salamander Poison Spirit Dragon

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:salamander_poison_dragon` |
| **Stage** | <span class="stage stage-final">Final</span> |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 500 - 500 |
| **Magicule** | 1,500 - 5,500 |
| **Health bonus** | 880 |
| **Spiritual health bonus** | 5,500 |
| **Attack damage bonus** | 3 |
| **Movement speed bonus** | 0.1 |
| **EP to evolve into** | 1,800,000 |

</div>

## Evolution

- **Evolves from:** [Salamander Poison Spirit](salamander-poison-spirit.md)

### Requirements to evolve into Salamander Poison Spirit Dragon

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 1,800,000 | 50% |
| Kill 4 bosses | 50% |

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

## Traits

- Divine

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | -1.1 | add |
| Max Health | 880 | add |
| Max Spiritual Health | 5,500 | add |
| Attack Damage | 3 | add |
| Attack Speed | -3 | add |
| Knockback Resistance | 1 | add |
| Movement Speed | 0.1 | add |
| Swim Speed Multiplier | 1 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/axolotl/salamander_config.toml`](../configs/config-nightmare-race-axolotl-salamander-config.md).

| Option | Default | Description |
|---|---|---|
| `PoisonDragon.epRequirement` | 1,800,000 | EP requirement to evolve. |
| `PoisonDragon.bossRequirement` | 4 | Bosses required to evolve. |
| `PoisonDragon.minAura` | 500 | Minimal aura. |
| `PoisonDragon.maxAura` | 500 | Maximum aura. |
| `PoisonDragon.minMagicule` | 1,500 | Minimal magicule. |
| `PoisonDragon.maxMagicule` | 5,500 | Maximum magicule. |
| `PoisonDragon.size` | -1.1 | Bonus Size. |
| `PoisonDragon.maxHealth` | 880 | Bonus Max Health. |
| `PoisonDragon.maxSpiritualHealth` | 5,500 | Bonus Max Spiritual Health. |
| `PoisonDragon.attack` | 3 | Bonus Attack Damage. |
| `PoisonDragon.attackSpeed` | -3 | Bonus Attack Speed. |
| `PoisonDragon.knockbackResistance` | 1 | Bonus Knockback Resistance. |
| `PoisonDragon.movementSpeed` | 0.1 | Bonus Movement Speed. |
| `PoisonDragon.swimSpeed` | 1 | Bonus Swimming Speed Multiplier. |
| `PoisonDragon.intrinsicSkills` | "trnightmare:poison_ki_release", "trnightmare:poison_dragon_armor", "tensura:poison_nullification", "trnightmare:axolotl_haki" | List of skills obtained by this race. |
| `PoisonSpirit.epRequirement` | 250,000 | EP requirement to evolve. |
| `PoisonSpirit.spiderEyeRequirement` | 100 | Spider Eyes requirement to evolve. |
| `PoisonSpirit.minAura` | 500 | Minimal aura. |
| `PoisonSpirit.maxAura` | 500 | Maximum aura. |
| `PoisonSpirit.minMagicule` | 1,500 | Minimal magicule. |
| `PoisonSpirit.maxMagicule` | 5,500 | Maximum magicule. |
| `PoisonSpirit.size` | -1.1 | Bonus Size. |
| `PoisonSpirit.maxHealth` | 200 | Bonus Max Health. |
| `PoisonSpirit.maxSpiritualHealth` | 3,600 | Bonus Max Spiritual Health. |
| `PoisonSpirit.attack` | 2 | Bonus Attack Damage. |
| `PoisonSpirit.attackSpeed` | -2 | Bonus Attack Speed. |
| `PoisonSpirit.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `PoisonSpirit.movementSpeed` | 0.08 | Bonus Movement Speed. |
| `PoisonSpirit.swimSpeed` | 0.8 | Bonus Swimming Speed Multiplier. |
| `PoisonSpirit.intrinsicSkills` | "trnightmare:poison_ki_release", "tensura:darkness_attack_resistance" | List of skills obtained by this race. |
| `SalamanderAssassin.epRequirement` | 50,000 | EP requirement to evolve. |
| `SalamanderAssassin.minAura` | 500 | Minimal aura. |
| `SalamanderAssassin.maxAura` | 500 | Maximum aura. |
| `SalamanderAssassin.minMagicule` | 1,500 | Minimal magicule. |
| `SalamanderAssassin.maxMagicule` | 5,500 | Maximum magicule. |
| `SalamanderAssassin.size` | -1.1 | Bonus Size. |
| `SalamanderAssassin.maxHealth` | 10 | Bonus Max Health. |
| `SalamanderAssassin.maxSpiritualHealth` | 15 | Bonus Max Spiritual Health. |
| `SalamanderAssassin.attack` | 2 | Bonus Attack Damage. |
| `SalamanderAssassin.attackSpeed` | -1 | Bonus Attack Speed. |
| `SalamanderAssassin.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `SalamanderAssassin.movementSpeed` | 0.04 | Bonus Movement Speed. |
| `SalamanderAssassin.swimSpeed` | 0.6 | Bonus Swimming Speed Multiplier. |
| `SalamanderAssassin.intrinsicSkills` | "tensura:dragon_eye", "tensura:poisonous_breath" | List of skills obtained by this race. |
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

## Tags

`tensura:races/divine`
