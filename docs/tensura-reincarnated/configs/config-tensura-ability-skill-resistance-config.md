# `config/tensura/ability/skill/resistance_config.toml`

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Configs](index.md)</small>

## Top level

| Option | Default | Range | Description |
|---|---|---|---|
| `hpDamageBypassResistance` | 0.5 |  | How many times of current HP that incoming damage value needs to be higher to deal damage to the user with Resistances<br>-1 = always applied regardless of HP |
| `resistanceDamageMultiplier` | 0.5 |  | The multiplier that will be applied on incoming damage when the damage went through Resistances |
| `hpDamageBypassNullification` | -1 |  | How many times of current HP that incoming damage value needs to be higher to deal damage to the user with Nullifications<br>-1 = always applied regardless of HP |
| `nullificationDamageMultiplier` | 0 |  | The multiplier that will be applied on incoming damage when the damage went through Nullifications |
| `damagePointMultiplier` | 10 |  | The multiplier of learning point requirement for damage points that the skill to reach for 1 learning point |

## `[EasyResistance]`

| Option | Default | Range | Description |
|---|---|---|---|
| `easyResistances` | "tensura:corrosion_resistance", "tensura:poison_resistance", "tensura:paralysis_resistance" |  | The List of Resistance that are considered to be easy to acquire |
| `easyResistanceDamageRequirement` | 5 |  | The amount of damage that a player need to take at once to acquire 1 learning point for an easy Resistance |
| `easyResistancePointRequirement` | 350 |  | The amount of learning points that a player need to have to acquire an easy Resistance |

## `[MediumResistance]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mediumResistances` | "tensura:cold_resistance", "tensura:heat_resistance", "tensura:darkness_attack_resistance", "tensura:earth_attack_resistance", "tensura:flame_attack_resistance", "tensura:light_attack_resistance", "tensura:spatial_attack_resistance", "tensura:water_attack_resistance", "tensura:wind_attack_resistance", "tensura:gravity_attack_resistance", "tensura:holy_attack_resistance", "tensura:electricity_resistance", "tensura:pain_resistance", "tensura:thermal_fluctuation_resistance" |  | The List of Resistance that are considered to be medium to acquire |
| `mediumResistanceDamageRequirement` | 15 |  | The amount of damage that a player need to take at once to acquire 1 learning point for a medium Resistance |
| `mediumResistancePointRequirement` | 500 |  | The amount of learning points that a player need to have to acquire a medium Resistance |

## `[HardResistance]`

| Option | Default | Range | Description |
|---|---|---|---|
| `hardResistances` | "tensura:physical_attack_resistance", "tensura:spiritual_attack_resistance", "tensura:abnormal_condition_resistance", "tensura:magic_resistance" |  | The List of Resistance that are considered to be hard to acquire |
| `hardResistanceDamageRequirement` | 20 |  | The amount of damage that a player need to take at once to acquire 1 learning point for a hard Resistance |
| `hardResistancePointRequirement` | 700 |  | The amount of learning points that a player need to have to acquire a hard Resistance |
