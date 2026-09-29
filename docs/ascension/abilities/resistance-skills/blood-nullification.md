# Blood Nullification

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Resistance Skills](index.md)</small>

<div class="infobox" markdown>

![Blood Nullification](../../../assets/icons/ascension/skill/blood_nullification.png)

| | |
|---|---|
| **Type** | Resistance Skill |
| **ID** | `ascension:blood_nullification` |
| **Acquisition cost (MP)** | 1,000 or 100 |
| **Activation** | Toggle |

</div>

> Negates all blood-attribute damage.

## How it works

- Can be toggled on and off
- Triggers when you are attacked
- Triggers when you take damage
- Triggers when an effect is applied to you

## Related

- **Referenced by:** [Blood Resistance](blood-resistance.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-config.md).

| Option | Default | Description |
|---|---|---|
| `mpAcquirementNullification` | 1,000 | The base Magicule Acquirement Cost for Nullification Skills. |
| `mpAcquirementResistance` | 100 | The base Magicule Acquirement Cost for Resistance Skills. |

Set in [`config/tensura/ability/skill/resistance_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-resistance-config.md).

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
