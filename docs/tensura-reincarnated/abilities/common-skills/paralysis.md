# Paralysis

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

![Paralysis](../../../assets/icons/tensura/skill/paralysis.png)

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `tensura:paralysis` |
| **Activation** | Passive |

</div>

> Empower your attacks with the effect of Paralysis, toggleable when mastered.

## How it works

- Triggers on melee contact

## Obtaining

- Innate to mobs: [Hell Moth](../../mobs/hell-moth.md)
- Listed in the `effectToRemove` config option (config/tensura/ability/battlewill_config.toml): The List of harmful effects that get removed upon activation.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/centipede_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Effects:** [Paralysis](../../effects/paralysis.md)
- **Summons / entities:** [Evil Centipede](../../mobs/evil-centipede.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/common_config.toml`](../../configs/config-tensura-ability-skill-common-config.md).

| Option | Default | Description |
|---|---|---|
| `Paralysis.centipedeAcquirement` | 500 | Evil Centipede beaten Requirement for Learning. |
| `Paralysis.paralysisDuration` | 200 | The duration in tick of the Paralysis effect. |
| `Paralysis.paralysisLevel` | 1 | The level of the Paralysis effect. |
| `Paralysis.paralysisLevelMastered` | 2 | The level of the Paralysis effect when Mastered. |

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
