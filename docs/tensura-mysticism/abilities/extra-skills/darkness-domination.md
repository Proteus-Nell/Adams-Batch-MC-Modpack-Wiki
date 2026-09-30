# Darkness Domination

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Darkness Domination](../../../assets/icons/mysticism/skill/darkness_domination.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `mysticism:darkness_domination` |
| **Activation** | Toggle, Press, Hold |

</div>

> Boosts the power of Dark abilities by a large amount.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 800 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/angel_config.toml): The list of intrinsic skills that the race gets.
- Acquisition checks: [Darkness Manipulation](darkness-manipulation.md)

## Related

- **Related skills:** [Darkness Manipulation](darkness-manipulation.md), [Darkness Cannon](../../../tensura-reincarnated/abilities/spiritual-magic/darkness-cannon.md)
- **Summons / entities:** Tensura
- **Referenced by:** [Darkness Manipulation](darkness-manipulation.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/extra_config.toml`](../../configs/config-mysticism-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `DarknessManipulation.darknessSkillAcquirement` | 3 | The number of mastered darkness skills needed to learn Darkness Manipulation. |
| `DarknessManipulation.dominationEpAcquirement` | 2,000,000 | EP Requirement for to learn Domination. |
| `DarknessManipulation.resistDegradationAcquirement` | 2,000,000 | EP Requirement for to use Resist Degradation when mastered. |
| `DarknessManipulation.manipulationBoost` | 1.5 | The Darkness Damage Boost when activated Manipulation. |
| `DarknessManipulation.dominationBoost` | 3 | The Darkness Damage Boost when activated Domination. |
| `DarknessManipulation.magiculeCost` | 800 | Magicule Cost to use. |
| `DarknessManipulation.range` | 15 | The range in block of the magic. |
| `DarknessManipulation.cubeRadius` | 5 | The radius in block of the cube. |
| `DarknessManipulation.cubeDamage` | 10 | The damage each 10 ticks of the cube. |
| `DarknessManipulation.cubeDamageMastered` | 20 | The damage each 10 ticks of the cube when mastered. |
| `DarknessManipulation.cubeSpeed` | 5 | The level of Movement Interference effect (-10% speed each) when applied by the cube. |
| `DarknessManipulation.cubeDuration` | 300 | The duration in tick of the cube when casted. |
| `DarknessManipulation.cooldown` | 4 | The cooldown in tick of the magic. |
| `DarknessManipulation.cooldownMastered` | 2 | The cooldown in tick of the magic when mastered. |
| `DarknessManipulation.damage` | 20 | The damage of the magic. |

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

`tensura:skills/darkness_skills`, `tensura:skills/elemental_domination`, `tensura:skills/extra_skills`
