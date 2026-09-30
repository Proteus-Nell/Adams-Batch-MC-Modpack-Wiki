# Darkness Manipulation

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Darkness Manipulation](../../../assets/icons/mysticism/skill/darkness_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `mysticism:darkness_manipulation` |
| **Cooldowns (s)** | 2 mastered, 4 otherwise |
| **Activation** | Toggle, Press |

</div>

> Boosts the power of Dark abilities by a decent amount.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 800 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Does something when mastered

## Obtaining

- Innate to mobs: [Shadow Imp](../../mobs/shadow-imp.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/angel_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/special_direwolf_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Darkness Domination](darkness-domination.md), [Dark Cube](../../../tensura-reincarnated/abilities/spiritual-magic/dark-cube.md)
- **Summons / entities:** Tensura
- **Referenced by:** [Darkness Domination](darkness-domination.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/extra_config.toml`](../../configs/config-mysticism-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `DarknessManipulation.darknessSkillAcquirement` | 3 | The number of mastered darkness skills needed to learn Darkness Manipulation. |
| `DarknessManipulation.dominationEpAcquirement` | 2,000,000 | EP Requirement for to learn Domination. |
| `DarknessManipulation.resistDegradationAcquirement` | 2,000,000 | EP Requirement for to use Resist Degradation when mastered. |
| `DarknessManipulation.manipulationBoost` | 1.5 | The Darkness Damage Boost when activated Manipulation. |
| `DarknessManipulation.dominationBoost` | 3 | The Darkness Damage Boost when activated Domination. |
| `DarknessManipulation.magiculeCost` | 800 | Magicule Cost to use. |
| `DarknessManipulation.range` | 15 | The range in block of the magic. |
| `DarknessManipulation.cubeRadius` | 5 | The radius in block of the cube. |
| `DarknessManipulation.cubeDamage` | 10 | The damage each 10 ticks of the cube. |
| `DarknessManipulation.cubeDamageMastered` | 20 | The damage each 10 ticks of the cube when mastered. |
| `DarknessManipulation.cubeSpeed` | 5 | The level of Movement Interference effect (-10% speed each) when applied by the cube. |
| `DarknessManipulation.cubeDuration` | 300 | The duration in tick of the cube when casted. |
| `DarknessManipulation.cooldown` | 4 | The cooldown in tick of the magic. |
| `DarknessManipulation.cooldownMastered` | 2 | The cooldown in tick of the magic when mastered. |
| `DarknessManipulation.damage` | 20 | The damage of the magic. |

## Tags

`tensura:skills/darkness_skills`, `tensura:skills/elemental_manipulation`, `tensura:skills/extra_skills`
