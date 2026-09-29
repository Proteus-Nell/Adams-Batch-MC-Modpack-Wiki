# Ice Manipulation

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Ice Manipulation](../../../assets/icons/mysticism/skill/ice_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `mysticism:ice_manipulation` |
| **Activation** | Toggle, Hold |

</div>

> Boosts the power of ice abilities by a decent amount.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 |  |

## How it works

- Can be toggled on and off
- Charged or channelled by holding the skill key
- Does something when mastered

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/special_direwolf_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Ice Domination](ice-domination.md), [Ice Breath](../../../tensura-reincarnated/abilities/intrinsic-skills/ice-breath.md)
- **Referenced by:** [Ice Domination](ice-domination.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/extra_config.toml`](../../configs/config-mysticism-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `IceManipulation.iceSkillAcquirement` | 1 | The number of mastered ice skills needed to learn Ice Manipulation. |
| `IceManipulation.dominationEpAcquirement` | 2,000,000 | EP Requirement for to learn Domination. |
| `IceManipulation.resistDegradationAcquirement` | 2,000,000 | EP Requirement for to use Resist Degradation when mastered. |
| `IceManipulation.manipulationBoost` | 1.5 | The Ice Damage Boost when activated Manipulation. |
| `IceManipulation.dominationBoost` | 3 | The Ice Damage Boost when activated Domination. |
| `IceManipulation.magiculeCost` | 500 | Magicule cost for Ice Breath. |
| `IceManipulation.damage` | 12 | The damage each second of the Ice Breath. |
| `IceManipulation.damageMastered` | 24 | The damage each second of the Ice Breath when mastered. |

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

`tensura:skills/elemental_manipulation`, `tensura:skills/extra_skills`, `tensura:skills/ice_skills`
