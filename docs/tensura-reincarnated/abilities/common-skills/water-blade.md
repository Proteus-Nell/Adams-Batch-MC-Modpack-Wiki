# Water Blade

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

![Water Blade](../../../assets/icons/tensura/skill/water_blade.png)

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `tensura:water_blade` |
| **Activation** | Press |

</div>

> Shoot out a blade of water which flies in a straight line.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Listed in the `allowedSkills` config option (config/nightmare/ability/skill/nightmare_unique.toml): List of skills Handler is allowed to upgrade. (is every skill it can by default)
- Acquisition checks: [Hydraulic Propulsion](hydraulic-propulsion.md)

## Related

- **Related skills:** [Hydraulic Propulsion](hydraulic-propulsion.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/common_config.toml`](../../configs/config-tensura-ability-skill-common-config.md).

| Option | Default | Description |
|---|---|---|
| `WaterBlade.epAcquirement` | 10,000 | EP Requirement for Learning. |
| `WaterBlade.magiculeCost` | 10 | Base Magicule Cost to activate. |
| `WaterBlade.damage` | 40 | The damage of the Water Blade. |
| `WaterBlade.speedMultiplier` | 5 | The speed multiplier of the Water Blade. |

## Tags

`tensura:skills/common_skills`, `tensura:skills/water_skills`
