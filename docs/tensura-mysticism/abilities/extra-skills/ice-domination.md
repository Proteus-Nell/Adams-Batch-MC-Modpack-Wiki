# Ice Domination

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Ice Domination](../../../assets/icons/mysticism/skill/ice_domination.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `mysticism:ice_domination` |
| **Activation** | Toggle, Hold |

</div>

> Boosts the power of ice abilities by a large amount.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 |  |

## How it works

- Can be toggled on and off
- Charged or channelled by holding the skill key

## Obtaining

- Acquisition checks: [Ice Manipulation](ice-manipulation.md)

## Related

- **Related skills:** [Ice Manipulation](ice-manipulation.md)
- **Summons / entities:** Mysticism, [Ice Breath](../../../tensura-reincarnated/abilities/intrinsic-skills/ice-breath.md)
- **Referenced by:** [Ice Manipulation](ice-manipulation.md)

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

`tensura:skills/elemental_domination`, `tensura:skills/extra_skills`, `tensura:skills/ice_skills`
