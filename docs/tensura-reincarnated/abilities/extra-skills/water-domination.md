# Water Domination

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Water Domination](../../../assets/icons/tensura/skill/water_domination.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:water_domination` |
| **Activation** | Toggle, Press, Hold |

</div>

> Boosts Water abilities by a large amount.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 or 10 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill IDs granted by Elfaria. Includes Albis so old Ars Weiss clones stay compatible, magic basics, transforms, senses, chant annulment,...
- Acquisition checks: [Water Manipulation](water-manipulation.md)

## Related

- **Related skills:** [Water Manipulation](water-manipulation.md)
- **Summons / entities:** Tensura, Water Ball
- **Referenced by:** [Water Manipulation](water-manipulation.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `WaterManipulation.dominationEpAcquirement` | 400,000 | EP Requirement for to learn Domination. |
| `WaterManipulation.waterSkillAcquirement` | 3 | The number of mastered water skills needed to learn Water Manipulation. |
| `WaterManipulation.dominationEpAcquirement` | 400,000 | EP Requirement for to learn Domination. |
| `WaterManipulation.resistDegradationAcquirement` | 800,000 | EP Requirement for to use Resist Degradation when mastered. |
| `WaterManipulation.manipulationBoost` | 1.5 | The Water Damage Boost when activated Manipulation. |
| `WaterManipulation.dominationBoost` | 3 | The Water Damage Boost when activated Domination. |
| `WaterManipulation.magiculeCostBreath` | 10 | Magicule Cost to activate Water Breath. |
| `WaterManipulation.magiculeCostBall` | 100 | Magicule Cost to activate Water Ball. |
| `WaterManipulation.breathDamage` | 8 | The damage of the Water Breath when activated. |
| `WaterManipulation.breathDamageMastered` | 4 | The damage of the Water Breath when activated with Mastery. |
| `WaterManipulation.ballDamage` | 12 | The damage of the Water Ball when activated. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/elemental_domination`, `tensura:skills/extra_skills`, `tensura:skills/water_skills`
