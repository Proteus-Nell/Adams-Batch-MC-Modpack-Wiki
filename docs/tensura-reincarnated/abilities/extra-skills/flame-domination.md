# Flame Domination

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Flame Domination](../../../assets/icons/tensura/skill/flame_domination.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:flame_domination` |
| **Activation** | Toggle, Hold |

</div>

> Boosts the power of fire abilities by a large amount.

## How it works

- Can be toggled on and off
- Charged or channelled by holding the skill key
- Triggers on melee contact

## Obtaining

- Acquisition checks: [Flame Manipulation](flame-manipulation.md)

## Related

- **Related skills:** [Flame Manipulation](flame-manipulation.md)
- **Summons / entities:** Tensura
- **Referenced by:** [Black Flame](black-flame.md), [Flame Manipulation](flame-manipulation.md), [Oni Pyre](../../../tr-nightmares/abilities/battlewill/oni-pyre.md), [Phainon, The Deliverer](../../../tensura-more-skills/abilities/ultimate-skills/phainon.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `FlameManipulation.dominationEpAcquirement` | 400,000 | EP Requirement for to learn Domination. |
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

`tensura:skills/elemental_domination`, `tensura:skills/extra_skills`, `tensura:skills/flame_skills`, `tensura:skills/restricted_learnable`
