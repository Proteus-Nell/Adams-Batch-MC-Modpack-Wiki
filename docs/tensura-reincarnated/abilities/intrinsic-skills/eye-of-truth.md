# Eye of Truth

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Eye of Truth](../../../assets/icons/tensura/skill/eye_of_truth.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:eye_of_truth` |
| **Activation** | Toggle |

</div>

> By obtaining the mythical Hero Egg, the veil of deception is torn apart. No illusion or concealment can deceive your sight, and your vision becomes perfect.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Triggers when an effect is applied to you

## Obtaining

- Intrinsic skill of: [Divine Angel](../../../ascension/races/divine-angel.md), [Cosmic Deity](../../../ascension/races/cosmic-deity.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `EyeOfTruth.senseLevel` | 4 | The level Presence Sense when activated. |

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

`tensura:skills/intrinsic_skills`, `tensura:skills/restricted_learnable`
