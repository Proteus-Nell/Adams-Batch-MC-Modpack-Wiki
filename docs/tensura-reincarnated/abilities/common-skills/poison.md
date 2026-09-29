# Poison

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

![Poison](../../../assets/icons/tensura/skill/poison.png)

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `tensura:poison` |
| **Activation** | Passive |

</div>

> Empower your attacks with the effect of Poison, toggleable when mastered.

## How it works

- Triggers on melee contact

## Obtaining

- Innate to mobs: [Aqua Frog](../../mobs/aqua-frog.md), [Army Wasp](../../mobs/army-wasp.md), [Phantaspore](../../mobs/phantaspore.md)
- Listed in the `intrinsicSkills` config option (config/nightmare/race/axolotl/salamander_config.toml): List of skills obtained by this race.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/scorpion_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Effects:** [Fatal Poison](../../effects/fatal-poison.md)
- **Referenced by:** [Lethal Poison](../../../tensura-mysticism/abilities/intrinsic-skills/lethal-poison.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/common_config.toml`](../../configs/config-tensura-ability-skill-common-config.md).

| Option | Default | Description |
|---|---|---|
| `Poison.spiderEyeAcquirement` | 100 | Spider Eye eaten Optional Requirement for Learning. |
| `Poison.spiderAcquirement` | 100 | Black Spider beaten Optional Requirement for Learning. |
| `Poison.poisonDuration` | 200 | The duration in tick of the Poison effect. |
| `Poison.poisonLevel` | 1 | The level of the Poison effect. |

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

`tensura:skills/common_skills`
