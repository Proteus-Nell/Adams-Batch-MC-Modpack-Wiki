# Flame Manipulation

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Flame Manipulation](../../../assets/icons/tensura/skill/flame_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:flame_manipulation` |
| **Activation** | Toggle, Press, Hold |

</div>

> Boosts the power of fire abilities by a decent amount.

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers on melee contact
- Does something when mastered

## Obtaining

- Intrinsic skill of: [Lower-Class Demon](../../../tr-nightmares/races/lower-class-demon.md)
- Can be learned by: [Mage Skeleton](../../../ascension/races/mage-skeleton.md), [Elder Lich](../../../ascension/races/elder-lich.md), [Lich](../../../ascension/races/lich.md), [Lich King](../../../ascension/races/lich-king.md)
- Innate to mobs: [Ifrit](../../mobs/ifrit.md), [Salamander](../../mobs/salamander.md), [Shizu](../../mobs/shizu.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/demon_clan_config.toml): List of intrinsic skills Lower Class Demon can randomly receive.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/direwolf_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/special_direwolf_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/ant_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Heat Wave](heat-wave.md), [Flame Domination](flame-domination.md)
- **Effects:** [Black Burn](../../effects/black-burn.md)
- **Summons / entities:** Tensura, [Flame Breath](../intrinsic-skills/flame-breath.md), Black Flame Breath
- **Referenced by:** [Black Flame](black-flame.md), [Flame Domination](flame-domination.md), [Fire Blessing](../../../tr-nightmares/abilities/extra-skills/fire-blessing.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `FlameManipulation.fireSkillAcquirement` | 3 | The number of mastered fire skills needed to learn Flame Manipulation. |
| `FlameManipulation.dominationEpAcquirement` | 400,000 | EP Requirement for to learn Domination. |
| `FlameManipulation.resistDegradationAcquirement` | 800,000 | EP Requirement for to use Resist Degradation when mastered. |
| `FlameManipulation.manipulationBoost` | 1.5 | The Flame Damage Boost when activated Manipulation. |
| `FlameManipulation.dominationBoost` | 3 | The Flame Damage Boost when activated Domination. |
| `FlameManipulation.manipulationBurnTick` | 100 | How long in tick that the target will be set on fire when attacked with Manipulation's Coating (doubled with Mastery). |
| `FlameManipulation.dominationBurnTick` | 200 | How long in tick that the target will be set on fire when attacked with Domination's Coating (doubled with Mastery). |
| `FlameManipulation.breathDamage` | 8 | The damage of the Fire Breath when activated. |
| `FlameManipulation.breathDamageMastered` | 20 | The damage of the Fire Breath when activated with Mastery. |

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

`tensura:skills/elemental_manipulation`, `tensura:skills/extra_skills`, `tensura:skills/flame_skills`
