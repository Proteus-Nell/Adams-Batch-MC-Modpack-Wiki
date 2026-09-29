# Lethal Poison

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Lethal Poison](../../../assets/icons/mysticism/skill/lethal_poison.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `mysticism:lethal_poison` |
| **Activation** | Passive |

</div>

> As the King of Scorpions, your poison is highly dangerous. An upgrade to the Poison skill. Can only be used by King Scorpions and their evolutionary line.

## How it works

- Triggers on melee contact

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/scorpion_config.toml): The list of intrinsic skills that the race gets.
- Acquisition checks: [Poison](../../../tensura-reincarnated/abilities/common-skills/poison.md)

## Related

- **Related skills:** [Poison](../../../tensura-reincarnated/abilities/common-skills/poison.md)
- **Effects:** [Fatal Poison](../../../tensura-reincarnated/effects/fatal-poison.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/intrinsic_config.toml`](../../configs/config-mysticism-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `LethalPoison.duration` | 200 | The duration of the poison effect in ticks. (Multiply seconds by 20.) |
| `LethalPoison.level` | 3 | The level of the poison effect. |
| `LethalPoison.levelMastered` | 6 | The level of the poison effect when the skill is mastered. |

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

`tensura:skills/intrinsic_skills`
