# Light Domination

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Light Domination](../../../assets/icons/mysticism/skill/light_domination.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `mysticism:light_domination` |
| **Cooldowns (s)** | 3 |
| **Activation** | Toggle, Press |

</div>

> Boosts the power of Light abilities by a large amount.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 200 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/phantom_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/angel_config.toml): The list of intrinsic skills that the race gets.
- Acquisition checks: [Light Manipulation](light-manipulation.md)

## Related

- **Related skills:** [Light Manipulation](light-manipulation.md)
- **Summons / entities:** Tensura, Light Arrow
- **Referenced by:** [Light Manipulation](light-manipulation.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/extra_config.toml`](../../configs/config-mysticism-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `LightManipulation.lightSkillAcquirement` | 3 | The number of mastered light skills needed to learn Light Manipulation. |
| `LightManipulation.dominationEpAcquirement` | 2,000,000 | EP Requirement for to learn Domination. |
| `LightManipulation.resistDegradationAcquirement` | 2,000,000 | EP Requirement for to use Resist Degradation when mastered. |
| `LightManipulation.manipulationBoost` | 1.5 | The Light Damage Boost when activated Manipulation. |
| `LightManipulation.dominationBoost` | 3 | The Light Damage Boost when activated Domination. |
| `LightManipulation.magiculeCost` | 200 | Magicule Cost to use. |
| `LightManipulation.range` | 30 | The range in block of the magic. |
| `LightManipulation.damage` | 20 | The damage of the magic. |
| `LightManipulation.arrowNumber` | 10 | The number of arrows. |
| `LightManipulation.arrowNumberMastered` | 15 | The number of arrows when the skill is mastered. |

## Tags

`tensura:skills/elemental_domination`, `tensura:skills/extra_skills`, `tensura:skills/light_skills`
