# Poison Transform

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Poison Transform](../../../assets/icons/mysticism/skill/poison_transform.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `mysticism:poison_transform` |
| **Activation** | Hold |

</div>

> Channel your inner poison to inject deadly venom's into your target through their every pore.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 30 |  |

## How it works

- Charged or channelled by holding the skill key
- Triggers when you damage a target

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.5 | multiply total |

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/scorpion_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Poisonous Breath](../../../tensura-reincarnated/abilities/intrinsic-skills/poisonous-breath.md)
- **Effects:** [Fatal Poison](../../../tensura-reincarnated/effects/fatal-poison.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `ElementalTransform.magiculeCost` | 30 | Magicule Cost to activate. |
| `ElementalTransform.speedMultiplier` | 0.5 | The movement speed multiplier of the user when activated. |
| `ElementalTransform.spiritLevel` | 2 | The level of Spiritual Magic the user learns upon obtaining this skill. |
| `ElementalTransform.radius` | 5 | The radius in block of the elemental effect upon targets around the user. |
| `ElementalTransform.damage` | 2 | The elemental damage amount per second on targets when activated. |
| `ElementalTransform.effectDuration` | 160 | The duration in tick of the status effects on targets when activated. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/intrinsic_skills`
