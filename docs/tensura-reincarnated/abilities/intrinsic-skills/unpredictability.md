# Unpredictability

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Unpredictability](../../../assets/icons/tensura/skill/unpredictability.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:unpredictability` |
| **Activation** | Toggle |

</div>

> In the hands of a True Hero, unpredictability reigns supreme. The Hero sees all, becoming able to ignore dodge and even read the movements of their opponent to disable their critical attacks or their dodge avoidance.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| dodgeNegate | 100 | add |

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `Unpredictability.negateDodge` | 100 | The bonus chance to negate dodging when activated. |

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
