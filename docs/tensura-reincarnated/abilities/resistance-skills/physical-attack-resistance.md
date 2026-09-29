# Physical Attack Resistance

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Resistance Skills](index.md)</small>

<div class="infobox" markdown>

![Physical Attack Resistance](../../../assets/icons/tensura/skill/physical_attack_resistance.png)

| | |
|---|---|
| **Type** | Resistance Skill |
| **ID** | `tensura:physical_attack_resistance` |
| **Acquisition cost (MP)** | 1,000 or 100 |
| **Activation** | Toggle |

</div>

> Ignore weaker physical attacks or reduce the damage from stronger blows.

## How it works

- Can be toggled on and off
- Triggers when you are attacked
- Triggers when you take damage
- Triggers when an effect is applied to you

## Obtaining

- Intrinsic skill of: [Metal Slime](../../races/metal-slime.md), [Wight](../../races/wight.md), [Wight King](../../races/wight-king.md), [Spirit Skeleton](../../races/spirit-skeleton.md), [Divine Skeleton](../../races/divine-skeleton.md), [Middle-Class Demon](../../../tr-nightmares/races/mid-class-demon.md), [Lesser Giant](../../../tr-nightmares/races/lesser-giant.md), [Giant Warrior](../../../tr-nightmares/races/giant-warrior.md), [Giant Dancer](../../../tr-nightmares/races/giant-dancer.md), [Medium hGoddess](../../../tr-nightmares/races/medium-class-goddess.md), [Nameless Goddess](../../../tr-nightmares/races/nameless-goddess.md), [Brother Of Chaos](../../../tr-nightmares/races/brother-of-chaos.md), [Perfect Doppelganger](../../../tr-nightmares/races/perfect-doppelganger.md), [Eidolon](../../../tr-nightmares/races/eidolon.md), [Elemental Lord](../../../tensura-mysticism/races/elemental-lord.md), [Majin Elemental Lord](../../../tensura-mysticism/races/majin-lord.md), [Divine Majin Elemental](../../../tensura-mysticism/races/divine-majin-elemental.md), [Divine Elemental](../../../tensura-mysticism/races/divine-elemental.md), [Cursed Mariner](../../../ascension/races/cursed-mariner.md), [Cursed Dreadnaught](../../../ascension/races/cursed-dreadnaught.md), [Phantom Corsair](../../../ascension/races/phantom-corsair.md), [Davy Jones](../../../ascension/races/davy-jones.md)
- Can be learned by: [Giant Frog](../../../ascension/races/giant-frog.md), [Poison Toad](../../../ascension/races/poison-toad.md), [Swamp Sovereign](../../../ascension/races/swamp-sovereign.md), [Bog Ancient](../../../ascension/races/bog-ancient.md), [Venom Lord](../../../ascension/races/venom-lord.md), [Frog Monarch](../../../ascension/races/frog-monarch.md), [Elder Bloodfiend](../../../ascension/races/elder-bloodfiend.md), [Progenitor Bloodfiend](../../../ascension/races/progenitor-bloodfiend.md), [Chaos Dragon](../../../ascension/races/chaos-dragon.md), [Monkey](../../../ascension/races/monkey.md), [Monkey Warrior](../../../ascension/races/monkey-warrior.md), [Monkey Martial Artist](../../../ascension/races/monkey-martial-artist.md), [Monkey King](../../../ascension/races/monkey-king.md), [Divine King](../../../ascension/races/divine-king.md), [Sun Wukong](../../../ascension/races/sun-wukong.md)
- Innate to mobs: [Charybdis](../../mobs/charybdis.md), [Gazel Dwargo](../../mobs/gazel-dwargo.md), [Hinata Sakaguchi](../../mobs/hinata-sakaguchi.md), [Metal Slime](../../mobs/metal-slime.md), [Shizu](../../mobs/shizu.md)
- Listed in the `learnableResistances` config option (config/tensura/reincarnation_config.toml): List of Resistances that can be available for learning when a player or an entity joins the world.
- Listed in the `hardResistances` config option (config/tensura/ability/skill/resistance_config.toml): The List of Resistance that are considered to be hard to acquire
- Listed in the `intrinsicSkills` config option (config/nightmare/race/axolotl/axolotl_config.toml): List of skills obtained by this race.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/phantom_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/angel_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/beetle_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/mantis_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/wasp_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Physical Attack Nullification](physical-attack-nullification.md)
- **Referenced by:** [Stripes](../../../tr-nightmares/abilities/unique-skills/stripes.md), [Naberius](../../../tensura-more-skills/abilities/ultimate-skills/naberius.md)

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
