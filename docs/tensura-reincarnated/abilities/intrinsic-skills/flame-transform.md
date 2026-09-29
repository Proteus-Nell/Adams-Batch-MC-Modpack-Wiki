# Flame Transform

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Flame Transform](../../../assets/icons/tensura/skill/flame_transform.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:flame_transform` |
| **Activation** | Passive |

</div>

> Channel the powers of fire to burn all nearby foes.

## How it works

- Triggers when you damage a target

## Obtaining

- Innate to mobs: [Ifrit](../../mobs/ifrit.md), [Salamander](../../mobs/salamander.md), [Shizu](../../mobs/shizu.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/wyrm_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/ant_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Referenced by:** [Black Flame](../extra-skills/black-flame.md), [Magic Flame Transform](../extra-skills/magic-flame-transform.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `ElementalTransform.damage` | 2 | The elemental damage amount per second on targets when activated. |

## Tags

`tensura:skills/flame_skills`, `tensura:skills/intrinsic_skills`
