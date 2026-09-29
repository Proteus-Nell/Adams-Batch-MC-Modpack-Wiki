# Paralysing Breath

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Paralysing Breath](../../../assets/icons/tensura/skill/paralysing_breath.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:paralysing_breath` |
| **Activation** | Press, Hold |

</div>

> Spew a horrifying breath to paralyze your prey.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 25 mastered, 50 otherwise |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Innate to mobs: [Evil Centipede](../../mobs/evil-centipede.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/wyrm_config.toml): The list of intrinsic skills that the race gets.

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `ParalysisBreath.magiculeCost` | 50 | Base Magicule Cost to activate (halved when mastered). |
| `ParalysisBreath.damage` | 2 | The damage each second of the Paralysis Breath. |
| `ParalysisBreath.paralysisLevel` | 3 | The level of the Paralysis effect when applied. |
| `ParalysisBreath.paralysisDuration` | 200 | The duration in tick of the Paralysis effect when applied. |

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

`tensura:skills/intrinsic_skills`
