# Earth Transform

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Earth Transform](../../../assets/icons/tensura/skill/earth_transform.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:earth_transform` |
| **Activation** | Passive |

</div>

> Channel the powers of the earth to deal increased damage and increase local gravity around you.

## How it works

- Triggers when you damage a target

## Obtaining

- Innate to mobs: [Beast Gnome](../../mobs/beast-gnome.md), [War Gnome](../../mobs/war-gnome.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/ant_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Burden](../aspectual-magic/burden.md)
- **Referenced by:** [Magic Earth Transform](../extra-skills/magic-earth-transform.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `ElementalTransform.effectDuration` | 160 | The duration in tick of the status effects on targets when activated. |
| `ElementalTransform.damage` | 2 | The elemental damage amount per second on targets when activated. |

## Tags

`tensura:skills/earth_skills`, `tensura:skills/intrinsic_skills`
