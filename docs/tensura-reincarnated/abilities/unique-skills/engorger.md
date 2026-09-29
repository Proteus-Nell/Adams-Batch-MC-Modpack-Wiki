# Engorger

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Engorger](../../../assets/icons/tensura/skill/engorger.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:engorger` |
| **Acquisition cost (MP)** | 30,000 |
| **Activation** | Toggle, Press |

</div>

> Increase your size and boost your physical stats.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 300 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.

## Related

- **Effects:** [Engorgement](../../effects/engorgement.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Engorger.mpAcquirement` | 30,000 | Magicule Acquirement Cost. |
| `Engorger.magiculeCost` | 300 | Magicule Cost to activate. |
| `Engorger.armor` | 10 | The amount of armor point from Engorgement. |
| `Engorger.attack` | 10 | The amount of attack point from Engorgement. |
| `Engorger.attackKnock` | 1 | The amount of attack knockback from Engorgement. |
| `Engorger.knockResistance` | 0.4 | The amount of knockback resistance from Engorgement. |
| `Engorger.speed` | 0.1 | The amount of speed from Engorgement. |
| `Engorger.jumpBoost` | 0.1 | The amount of jump boost from Engorgement. |
| `Engorger.range` | 2.5 | The amount of range from Engorgement. |
| `Engorger.size` | 1.5 | The amount of size from Engorgement. |
| `Engorger.heal` | 1 | The amount of HP the user regenerates from Engorgement each second. |
| `Engorger.dashLevel` | 3 | The level of the dash boost when activated (similar to Riptide). |
| `Engorger.dashDuration` | 15 | The duration in tick of the dash boost when activated. |
| `Engorger.dashAttackMultiplier` | 1 | The damage multiplier compared to the user's attack damage when hit target during Dash boost. |
| `Engorger.dashAttackBonus` | 50 | The Bonus attack damage of the dash boost on top of the user's attack damage. |
| `Engorger.dashAttackBonusMastered` | 100 | The Bonus attack damage of the dash boost on top of the user's attack damage when mastered. |

## Tags

`tensura:skills/unique_skills`
