# Water Manipulation

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Water Manipulation](../../../assets/icons/tensura/skill/water_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:water_manipulation` |
| **Activation** | Toggle, Press, Hold |

</div>

> Boosts Water abilities by a decent amount.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 or 10 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Does something when mastered

## Obtaining

- Can be learned by: [Swamp Sovereign](../../../ascension/races/swamp-sovereign.md), [Bog Ancient](../../../ascension/races/bog-ancient.md), [Venom Lord](../../../ascension/races/venom-lord.md), [Frog Monarch](../../../ascension/races/frog-monarch.md), [Phantom Corsair](../../../ascension/races/phantom-corsair.md), [Davy Jones](../../../ascension/races/davy-jones.md), [Mage Skeleton](../../../ascension/races/mage-skeleton.md), [Elder Lich](../../../ascension/races/elder-lich.md), [Lich](../../../ascension/races/lich.md), [Lich King](../../../ascension/races/lich-king.md)
- Innate to mobs: [Aqua Frog](../../mobs/aqua-frog.md), [Undine](../../mobs/undine.md)
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill IDs granted by Elfaria. Includes Albis so old Ars Weiss clones stay compatible, magic basics, transforms, senses, chant annulment,...
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/direwolf_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/special_direwolf_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/centipede_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Water Domination](water-domination.md)
- **Referenced by:** [Water Domination](water-domination.md), [Weather Manipulation](weather-manipulation.md), [Water Blessing](../../../tr-nightmares/abilities/extra-skills/water-blessing.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
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

`tensura:skills/elemental_manipulation`, `tensura:skills/extra_skills`, `tensura:skills/water_skills`
