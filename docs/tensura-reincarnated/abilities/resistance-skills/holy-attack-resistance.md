# Holy Attack Resistance

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Resistance Skills](index.md)</small>

<div class="infobox" markdown>

![Holy Attack Resistance](../../../assets/icons/tensura/skill/holy_attack_resistance.png)

| | |
|---|---|
| **Type** | Resistance Skill |
| **ID** | `tensura:holy_attack_resistance` |
| **Acquisition cost (MP)** | 1,000 or 100 |
| **Activation** | Toggle |

</div>

> Ignore weaker holy attacks or reduce the damage from stronger divine powers.

## How it works

- Can be toggled on and off
- Triggers when you are attacked
- Triggers when you take damage
- Triggers when an effect is applied to you

## Obtaining

- Intrinsic skill of: [Fairy Princess](../../../tr-nightmares/races/fairy-princess.md), [Lesser hGoddess](../../../tr-nightmares/races/lesser-goddess.md)
- Can be learned by: [Angel](../../../ascension/races/angel.md), [Archangel](../../../ascension/races/archangel.md), [Seraphim](../../../ascension/races/seraphim.md), [Divine Angel](../../../ascension/races/divine-angel.md), [Fallen Angel](../../../ascension/races/fallen-angel.md), [Cosmic Deity](../../../ascension/races/cosmic-deity.md), [Chaotic Deity](../../../ascension/races/chaotic-deity.md), [6 Tailed Fox](../../../ascension/races/six-tail-fox.md), [9 Tailed Fox](../../../ascension/races/nine-tail-fox.md), [Divine Kitsune](../../../ascension/races/divine-kitsune.md), [Royal Djinn](../../../ascension/races/royal-djinn.md), [Wishbound Djinn](../../../ascension/races/wishbound-djinn.md), [Primordial Djinn](../../../ascension/races/primordial-djinn.md), [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md), [Chaos Dragon](../../../ascension/races/chaos-dragon.md)
- Innate to mobs: [Gazel Dwargo](../../mobs/gazel-dwargo.md), [Hinata Sakaguchi](../../mobs/hinata-sakaguchi.md)
- Listed in the `learnableResistances` config option (config/tensura/reincarnation_config.toml): List of Resistances that can be available for learning when a player or an entity joins the world.
- Listed in the `mediumResistances` config option (config/tensura/ability/skill/resistance_config.toml): The List of Resistance that are considered to be medium to acquire
- Listed in the `intrinsicSkills` config option (config/mysticism/race/phantom_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/angel_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Referenced by:** [Kronairos, Lord of the Endless](../../../tensura-more-skills/abilities/ultimate-skills/kronairos-lord-of-the-endless.md), [Divine General Mahoraga](../../../tensura-more-skills/abilities/ultimate-skills/divine-general-mahoraga.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill_config.toml`](../../configs/config-tensura-ability-skill-config.md).

| Option | Default | Description |
|---|---|---|
| `mpAcquirementNullification` | 1,000 | The base Magicule Acquirement Cost for Nullification Skills. |
| `mpAcquirementResistance` | 100 | The base Magicule Acquirement Cost for Resistance Skills. |

Set in [`config/tensura/ability/skill/resistance_config.toml`](../../configs/config-tensura-ability-skill-resistance-config.md).

| Option | Default | Description |
|---|---|---|
| `EasyResistance.easyResistances` | "tensura:corrosion_resistance", "tensura:poison_resistance", "tensura:paralysis_resistance" | The List of Resistance that are considered to be easy to acquire |
| `EasyResistance.easyResistances` | "tensura:corrosion_resistance", "tensura:poison_resistance", "tensura:paralysis_resistance" | The List of Resistance that are considered to be easy to acquire |
| `EasyResistance.easyResistanceDamageRequirement` | 5 | The amount of damage that a player need to take at once to acquire 1 learning point for an easy Resistance |
| `EasyResistance.easyResistancePointRequirement` | 350 | The amount of learning points that a player need to have to acquire an easy Resistance |
| `MediumResistance.mediumResistances` | "tensura:cold_resistance", "tensura:heat_resistance", "tensura:darkness_attack_resistance", "tensura:earth_attack_resistance", "tensura:flame_attack_resistance", "tensura:light_attack_resistance", "tensura:spatial_attack_resistance", "tensura:water_attack_resistance", "tensura:wind_attack_resistance", "tensura:gravity_attack_resistance", "tensura:holy_attack_resistance", "tensura:electricity_resistance", "tensura:pain_resistance", "tensura:thermal_fluctuation_resistance" | The List of Resistance that are considered to be medium to acquire |
| `MediumResistance.mediumResistances` | "tensura:cold_resistance", "tensura:heat_resistance", "tensura:darkness_attack_resistance", "tensura:earth_attack_resistance", "tensura:flame_attack_resistance", "tensura:light_attack_resistance", "tensura:spatial_attack_resistance", "tensura:water_attack_resistance", "tensura:wind_attack_resistance", "tensura:gravity_attack_resistance", "tensura:holy_attack_resistance", "tensura:electricity_resistance", "tensura:pain_resistance", "tensura:thermal_fluctuation_resistance" | The List of Resistance that are considered to be medium to acquire |
| `MediumResistance.mediumResistanceDamageRequirement` | 15 | The amount of damage that a player need to take at once to acquire 1 learning point for a medium Resistance |
| `MediumResistance.mediumResistancePointRequirement` | 500 | The amount of learning points that a player need to have to acquire a medium Resistance |
| `HardResistance.hardResistances` | "tensura:physical_attack_resistance", "tensura:spiritual_attack_resistance", "tensura:abnormal_condition_resistance", "tensura:magic_resistance" | The List of Resistance that are considered to be hard to acquire |
| `HardResistance.hardResistances` | "tensura:physical_attack_resistance", "tensura:spiritual_attack_resistance", "tensura:abnormal_condition_resistance", "tensura:magic_resistance" | The List of Resistance that are considered to be hard to acquire |
| `HardResistance.hardResistanceDamageRequirement` | 20 | The amount of damage that a player need to take at once to acquire 1 learning point for a hard Resistance |
| `HardResistance.hardResistancePointRequirement` | 700 | The amount of learning points that a player need to have to acquire a hard Resistance |
| `hpDamageBypassNullification` | -1 | How many times of current HP that incoming damage value needs to be higher to deal damage to the user with Nullifications<br>-1 = always applied regardless of HP |
| `hpDamageBypassResistance` | 0.5 | How many times of current HP that incoming damage value needs to be higher to deal damage to the user with Resistances<br>-1 = always applied regardless of HP |
| `nullificationDamageMultiplier` | 0 | The multiplier that will be applied on incoming damage when the damage went through Nullifications |
| `resistanceDamageMultiplier` | 0.5 | The multiplier that will be applied on incoming damage when the damage went through Resistances |
| `damagePointMultiplier` | 10 | The multiplier of learning point requirement for damage points that the skill to reach for 1 learning point |

## Tags

`tensura:skills/resistance_skills`
