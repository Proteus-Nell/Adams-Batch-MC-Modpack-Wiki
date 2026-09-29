# Earth Domination

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Earth Domination](../../../assets/icons/tensura/skill/earth_domination.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:earth_domination` |
| **Modes** | 3 |
| **Activation** | Toggle, Press |

</div>

> Boosts the power of  Earth abilities by a large amount.

## Modes

| # | Mode |
|---|---|
| 1 | Earth Wall |
| 2 | Blocks Break |
| 3 | Earth Pit |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Blocks Break | 10 |  |
| Earth Pit | 20 |  |
| other modes | 5 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key

## Obtaining

- Intrinsic skill of: [Big Cutie](../../../tr-nightmares/races/big-cutie.md), [Giant Elder](../../../tr-nightmares/races/giant-elder.md)
- Innate to mobs: [Gazel Dwargo](../../mobs/gazel-dwargo.md)
- Acquisition checks: [Earth Manipulation](earth-manipulation.md)

## Related

- **Related skills:** [Earth Manipulation](earth-manipulation.md)
- **Referenced by:** [Earth Manipulation](earth-manipulation.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `EarthManipulation.dominationEpAcquirement` | 400,000 | EP Requirement for to learn Domination. |
| `EarthManipulation.earthSkillAcquirement` | 3 | The number of mastered earth skills needed to learn Earth Manipulation. |
| `EarthManipulation.dominationEpAcquirement` | 400,000 | EP Requirement for to learn Domination. |
| `EarthManipulation.resistDegradationAcquirement` | 800,000 | EP Requirement for to use Resist Degradation when mastered. |
| `EarthManipulation.magiculeCostWall` | 5 | Magicule Cost to activate Wall. |
| `EarthManipulation.magiculeCostBreak` | 10 | Magicule Cost to activate Break. |
| `EarthManipulation.magiculeCostPit` | 20 | Magicule Cost to activate Pit. |
| `EarthManipulation.manipulationBoost` | 1.5 | The Earth Damage Boost when activated Manipulation. |
| `EarthManipulation.dominationBoost` | 3 | The Earth Damage Boost when activated Domination. |
| `EarthManipulation.wallDamage` | 5 | The damage of the Earth Wall. |
| `EarthManipulation.wallRadius` | 2 | The radius of the Earth Wall. |
| `EarthManipulation.wallHeight` | 4 | The height of the Earth Wall. |
| `EarthManipulation.wallDuration` | 1,200 | The duration in tick of the Earth Wall. |
| `EarthManipulation.breakRadius` | 1 | The extending radius of the Earth Break. |
| `EarthManipulation.pitRadius` | 2 | The radius of the Earth Pit. |

## Tags

`tensura:skills/earth_skills`, `tensura:skills/elemental_domination`, `tensura:skills/extra_skills`
