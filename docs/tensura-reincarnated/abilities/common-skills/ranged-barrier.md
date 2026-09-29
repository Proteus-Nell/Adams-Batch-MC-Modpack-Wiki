# Ranged Barrier

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

![Ranged Barrier](../../../assets/icons/tensura/skill/ranged_barrier.png)

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `tensura:ranged_barrier` |
| **Modes** | 3 |
| **Activation** | Press |

</div>

> Place down differently sized barriers which block enemies in or out. Strong attacks can still destroy them.

## Modes

| # | Mode |
|---|---|
| 1 | 5x5x5 Barrier |
| 2 | 10x10x10 Barrier |
| 3 | 20x20x20 Barrier |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5 × radius mode |  |

## How it works

- Activated by pressing the skill key
- Does something when mastered

## Obtaining

- Innate to mobs: [Ifrit](../../mobs/ifrit.md), [Shizu](../../mobs/shizu.md)
- Listed in the `intrinsicSkills` config option (config/nightmare/race/scholar_config.toml): List of skills obtained by this race.

## Related

- **Related skills:** [Multilayer Barrier](../extra-skills/multilayer-barrier.md)
- **Summons / entities:** Boss Killed, [Ifrit](../../mobs/ifrit.md), [Ranged Barrier](ranged-barrier.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/common_config.toml`](../../configs/config-tensura-ability-skill-common-config.md).

| Option | Default | Description |
|---|---|---|
| `RangedBarrier.epAcquirement` | 80,000 | EP Requirement for Learning. |
| `RangedBarrier.ifritAcquirement` | 1 | Ifrit beaten Requirement for Learning. |
| `RangedBarrier.magiculeCost` | 5 | Base Magicule Cost to activate. |
| `RangedBarrier.barrierRange` | 30 | The max activation range for the barriers in blocks. |
| `RangedBarrier.barrierDuration` | 1,200 | The duration of the barrier when activated (doubled when mastered). |
| `RangedBarrier.barrierRadius` | 2 | The radius of the barrier in the first mode. |
| `RangedBarrier.barrierRadiusSecond` | 5 | The radius of the barrier in the second mode. |
| `RangedBarrier.barrierRadiusThird` | 10 | The radius of the barrier in the third mode. |

## Tags

`tensura:skills/common_skills`
