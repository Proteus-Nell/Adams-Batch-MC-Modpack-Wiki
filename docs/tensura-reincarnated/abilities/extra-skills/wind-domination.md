# Wind Domination

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Wind Domination](../../../assets/icons/tensura/skill/wind_domination.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:wind_domination` |
| **Activation** | Toggle, Press, Hold |

</div>

> Boosts Wind abilities by a large amount.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 200 or 20 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Acquisition checks: [Wind Manipulation](wind-manipulation.md)

## Related

- **Related skills:** [Wind Manipulation](wind-manipulation.md)
- **Summons / entities:** Tensura, Wind Sphere, Wind Blow
- **Referenced by:** [Black Lightning](black-lightning.md), [Wind Manipulation](wind-manipulation.md), [｢ Hastur, Lord of Starwind ｣](../../../tr-nightmares/abilities/ultimate-skills/hastur.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `WindManipulation.dominationEpAcquirement` | 400,000 | EP Requirement for to learn Domination. |
| `WindManipulation.windSkillAcquirement` | 3 | The number of mastered wind skills needed to learn Wind Manipulation. |
| `WindManipulation.dominationEpAcquirement` | 400,000 | EP Requirement for to learn Domination. |
| `WindManipulation.resistDegradationAcquirement` | 800,000 | EP Requirement for to use Resist Degradation when mastered. |
| `WindManipulation.manipulationBoost` | 1.5 | The Wind Damage Boost when activated Manipulation. |
| `WindManipulation.dominationBoost` | 3 | The Wind Damage Boost when activated Domination. |
| `WindManipulation.magiculeCostBreath` | 20 | Magicule Cost to activate Water Breath. |
| `WindManipulation.magiculeCostBall` | 200 | Magicule Cost to activate Water Ball. |
| `WindManipulation.breathDamage` | 8 | The damage of the Water Breath when activated. |
| `WindManipulation.breathDamageMastered` | 4 | The damage of the Water Breath when activated with Mastery. |
| `WindManipulation.ballDamage` | 12 | The damage of the Water Ball when activated. |

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

`tensura:skills/elemental_domination`, `tensura:skills/extra_skills`, `tensura:skills/wind_skills`
