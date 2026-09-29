# Hydraulic Propulsion

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

![Hydraulic Propulsion](../../../assets/icons/tensura/skill/hydraulic_propulsion.png)

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `tensura:hydraulic_propulsion` |
| **Activation** | Press |

</div>

> Propel yourself at high speeds underwater.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 2 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Intrinsic skill of: [Merfolk](../../races/merfolk.md), [Enlightened Merfolk](../../races/enlightened-merfolk.md), [Merfolk Saint](../../races/merfolk-saint.md), [Divine Fish](../../races/divine-fish.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/wyrm_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Referenced by:** [Water Blade](water-blade.md), [Water Current Control](water-current-control.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/common_config.toml`](../../configs/config-tensura-ability-skill-common-config.md).

| Option | Default | Description |
|---|---|---|
| `HydraulicPropulsion.epAcquirement` | 10,000 | EP Requirement for Learning. |
| `HydraulicPropulsion.magiculeCost` | 2 | Magicule Cost to activate. |
| `HydraulicPropulsion.riptideLevel` | 3 | The level of the riptide boost when activated. |
| `HydraulicPropulsion.riptideDuration` | 10 | The duration in tick of the riptide boost when activated. |
| `HydraulicPropulsion.riptideMultiplier` | 1 | The damage multiplier compared to the user's attack when hit target during Riptide boost. |

## Tags

`tensura:skills/common_skills`, `tensura:skills/water_skills`
