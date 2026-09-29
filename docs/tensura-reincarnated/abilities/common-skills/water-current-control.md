# Water Current Control

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

![Water Current Control](../../../assets/icons/tensura/skill/water_current_control.png)

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `tensura:water_current_control` |
| **Activation** | Toggle |

</div>

> Manipulate water around you to propel yourself in any direction.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Does something when mastered

## Obtaining

- Can be learned by: [Frog](../../../ascension/races/frog.md), [Giant Frog](../../../ascension/races/giant-frog.md), [Poison Toad](../../../ascension/races/poison-toad.md), [Swamp Sovereign](../../../ascension/races/swamp-sovereign.md), [Bog Ancient](../../../ascension/races/bog-ancient.md), [Venom Lord](../../../ascension/races/venom-lord.md), [Frog Monarch](../../../ascension/races/frog-monarch.md), [Cursed Mariner](../../../ascension/races/cursed-mariner.md), [Cursed Dreadnaught](../../../ascension/races/cursed-dreadnaught.md), [Phantom Corsair](../../../ascension/races/phantom-corsair.md), [Davy Jones](../../../ascension/races/davy-jones.md)

## Related

- **Related skills:** [Hydraulic Propulsion](hydraulic-propulsion.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/common_config.toml`](../../configs/config-tensura-ability-skill-common-config.md).

| Option | Default | Description |
|---|---|---|
| `WaterCurrentControl.epAcquirement` | 6,000 | EP Requirement for Learning. |
| `WaterCurrentControl.swimBoost` | 4 | The Swim Speed Multiplier when activated. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/common_skills`, `tensura:skills/water_skills`
