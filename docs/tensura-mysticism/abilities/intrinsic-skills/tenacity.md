# Tenacity

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `mysticism:tenacity` |
| **Max mastery** | 500 |
| **Activation** | Toggle |

</div>

> Become tenacious and repair your body. Since magic and mana itself has rejected you, utilise your pure aura alone.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/restricted_human_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Ultraspeed Regeneration](../../../tensura-reincarnated/abilities/extra-skills/ultraspeed-regeneration.md), [Infinite Regeneration](../../../tensura-reincarnated/abilities/extra-skills/infinite-regeneration.md)
- **Effects:** [Aura Healing](../../effects/aura-healing.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/intrinsic_config.toml`](../../configs/config-mysticism-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `Tenacity.auraCost` | 100 | Aura Cost per HP regenerated. |
| `Tenacity.auraCostMastered` | 60 | Aura Cost per HP regenerated when mastered. |
| `Tenacity.shouldRegenSHPOnMastery` | true | Should Tenacity heal the spiritual body when the skill is mastered? |
| `Tenacity.shpAuraCost` | 120 | Aura Cost per SHP regenerated. |
| `Tenacity.shpAuraCostMastered` | 80 | Aura Cost per SHP regenerated when mastered. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

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
