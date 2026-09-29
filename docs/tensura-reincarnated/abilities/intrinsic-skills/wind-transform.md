# Wind Transform

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Wind Transform](../../../assets/icons/tensura/skill/wind_transform.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:wind_transform` |
| **Activation** | Passive |

</div>

> Channel the powers of wind to paralyze and damage all nearby entities.

## How it works

- Triggers when you damage a target

## Obtaining

- Intrinsic skill of: [qHigher Fairy](../../../tr-nightmares/races/higher-fairy.md)
- Innate to mobs: [Feathered Serpent](../../mobs/feathered-serpent.md), [Sylphide](../../mobs/sylphide.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/wasp_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Effects:** [Paralysis](../../effects/paralysis.md)
- **Referenced by:** [Magic Wind Transform](../extra-skills/magic-wind-transform.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `ElementalTransform.effectDuration` | 160 | The duration in tick of the status effects on targets when activated. |
| `ElementalTransform.damage` | 2 | The elemental damage amount per second on targets when activated. |

## Tags

`tensura:skills/intrinsic_skills`, `tensura:skills/wind_skills`
