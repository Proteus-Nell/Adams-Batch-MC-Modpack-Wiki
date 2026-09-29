# Giantification

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Giantification](../../../assets/icons/tensura/skill/giantification.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:giantification` |
| **Activation** | Press, Hold |

</div>

> Grow beyond your normal size to gain increased strength and reach.

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| scale | size ÷ 2 | add |
| step | max(size, 0) ÷ 2 | add |
| speed | max(size, 0) × 0.02 | add |
| jump | max(size, 0) × 0.1 | add |
| fall | max(size, 0) | add |
| entityRange | max(size × range, 0) | add |
| blockRange | max(size × range, 0) | add |

## Obtaining

- Intrinsic skill of: [Giant](../../races/giant.md), [Ancient Giant](../../races/ancient-giant.md), [Divine Giant](../../races/divine-giant.md), [Giant Frog](../../../ascension/races/giant-frog.md), [Poison Toad](../../../ascension/races/poison-toad.md), [Swamp Sovereign](../../../ascension/races/swamp-sovereign.md), [Bog Ancient](../../../ascension/races/bog-ancient.md), [Venom Lord](../../../ascension/races/venom-lord.md), [Frog Monarch](../../../ascension/races/frog-monarch.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Lesser Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Greater Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Golden Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Chimera Lord can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `Giantification.damage` | 6 | The attack damage buff the user gains when activated. |
| `Giantification.maxSize` | 3 | The maximum size change in block when activated. |
| `Giantification.minSize` | -1 | The minimum size change in block when activated with Mastery. |
| `Giantification.rangeMultiplier` | 1.5 | The interaction range multiplier to apply with size when activated. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/intrinsic_skills`
