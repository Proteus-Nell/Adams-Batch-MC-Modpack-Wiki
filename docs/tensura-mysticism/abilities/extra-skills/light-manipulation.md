# Light Manipulation

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Light Manipulation](../../../assets/icons/mysticism/skill/light_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `mysticism:light_manipulation` |
| **Activation** | Toggle, Press, Hold |

</div>

> Boosts the power of light abilities by a decent amount.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 200 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Does something when mastered

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/angel_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/special_direwolf_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Light Domination](light-domination.md), [Solar Beam](../../../tensura-reincarnated/abilities/spiritual-magic/solar-beam.md)
- **Summons / entities:** Tensura
- **Referenced by:** [Light Domination](light-domination.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/extra_config.toml`](../../configs/config-mysticism-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `LightManipulation.lightSkillAcquirement` | 3 | The number of mastered light skills needed to learn Light Manipulation. |
| `LightManipulation.dominationEpAcquirement` | 2,000,000 | EP Requirement for to learn Domination. |
| `LightManipulation.resistDegradationAcquirement` | 2,000,000 | EP Requirement for to use Resist Degradation when mastered. |
| `LightManipulation.manipulationBoost` | 1.5 | The Light Damage Boost when activated Manipulation. |
| `LightManipulation.dominationBoost` | 3 | The Light Damage Boost when activated Domination. |
| `LightManipulation.magiculeCost` | 200 | Magicule Cost to use. |
| `LightManipulation.range` | 30 | The range in block of the magic. |
| `LightManipulation.damage` | 20 | The damage of the magic. |
| `LightManipulation.arrowNumber` | 10 | The number of arrows. |
| `LightManipulation.arrowNumberMastered` | 15 | The number of arrows when the skill is mastered. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/elemental_manipulation`, `tensura:skills/extra_skills`, `tensura:skills/light_skills`
