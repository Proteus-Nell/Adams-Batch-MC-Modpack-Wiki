# Space Transform

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Space Transform](../../../assets/icons/tensura/skill/space_transform.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:space_transform` |
| **Activation** | Passive |

</div>

> Channel the powers of space to weaken and damage all nearby entities.

## How it works

- Triggers when you damage a target

## Obtaining

- Intrinsic skill of: [Ender Dragonewt](../../../ascension/races/ender-dragonewt.md), [Void Dragonewt](../../../ascension/races/void-dragonewt.md), [Abyssal Dragonewt](../../../ascension/races/abyssal-dragonewt.md), [Chaos Dragon](../../../ascension/races/chaos-dragon.md)
- Innate to mobs: [Akash](../../mobs/akash.md), [Winged Cat](../../mobs/winged-cat.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/centipede_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Referenced by:** [Magic Space Transform](../extra-skills/magic-space-transform.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `ElementalTransform.effectDuration` | 160 | The duration in tick of the status effects on targets when activated. |
| `ElementalTransform.damage` | 2 | The elemental damage amount per second on targets when activated. |

## Tags

`tensura:skills/intrinsic_skills`, `tensura:skills/space_skills`
