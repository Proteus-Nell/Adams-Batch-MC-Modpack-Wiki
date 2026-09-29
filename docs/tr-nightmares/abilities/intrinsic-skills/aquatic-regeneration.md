# Aquatic Regeneration

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:aquatic_regeneration` |
| **Activation** | Toggle |

</div>

> An intrinsic skill that rapidly restores health while in or near water.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50 or 100 |  |

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

## Related

- **Effects:** [Self-Regeneration](../../../tensura-reincarnated/effects/self-regeneration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `AquaticRegeneration.magiculeCost` | 100 | Base Magicule Cost to activate. |
| `AquaticRegeneration.regenLevel` | 3 | The level of the self-regeneration effect. |
| `AquaticRegeneration.regenLevelMastered` | 4 | The level of the self-regeneration effect when mastered. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
