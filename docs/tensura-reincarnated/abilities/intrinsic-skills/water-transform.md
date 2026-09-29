# Water Transform

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Water Transform](../../../assets/icons/tensura/skill/water_transform.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:water_transform` |
| **Activation** | Passive |

</div>

> Channel the powers of water to damage and poison all nearby foes.

## How it works

- Triggers when you damage a target

## Obtaining

- Innate to mobs: [Aqua Frog](../../mobs/aqua-frog.md), [Undine](../../mobs/undine.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/centipede_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Referenced by:** [Magic Water Transform](../extra-skills/magic-water-transform.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `ElementalTransform.effectDuration` | 160 | The duration in tick of the status effects on targets when activated. |
| `ElementalTransform.damage` | 2 | The elemental damage amount per second on targets when activated. |

## Tags

`tensura:skills/intrinsic_skills`, `tensura:skills/water_skills`
