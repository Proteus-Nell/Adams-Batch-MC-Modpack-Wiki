# Earth Manipulation

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Earth Manipulation](../../../assets/icons/tensura/skill/earth_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:earth_manipulation` |
| **Modes** | 3 |
| **Activation** | Toggle, Press |

</div>

> Boosts the power of Earth abilities by a decent amount.

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
- Does something when mastered

## Obtaining

- Intrinsic skill of: [Lesser Giant](../../../tr-nightmares/races/lesser-giant.md), [Giant Warrior](../../../tr-nightmares/races/giant-warrior.md), [Giant Dancer](../../../tr-nightmares/races/giant-dancer.md)
- Can be learned by: [Bog Ancient](../../../ascension/races/bog-ancient.md), [Frog Monarch](../../../ascension/races/frog-monarch.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md), [Mage Skeleton](../../../ascension/races/mage-skeleton.md), [Elder Lich](../../../ascension/races/elder-lich.md), [Lich](../../../ascension/races/lich.md), [Lich King](../../../ascension/races/lich-king.md)
- Innate to mobs: [Beast Gnome](../../mobs/beast-gnome.md), [War Gnome](../../mobs/war-gnome.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/direwolf_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/special_direwolf_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/ant_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Earth Domination](earth-domination.md)
- **Referenced by:** [Earth Domination](earth-domination.md), [Earth Blessing](../../../tr-nightmares/abilities/extra-skills/earth-blessing.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
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

`tensura:skills/earth_skills`, `tensura:skills/elemental_manipulation`, `tensura:skills/extra_skills`
