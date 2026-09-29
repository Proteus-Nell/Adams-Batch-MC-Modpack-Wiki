# Ogre Berserker

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Ogre Berserker](../../../assets/icons/tensura/skill/ogre_berserker.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:ogre_berserker` |
| **Cooldowns (s)** | 600, duration ÷ 20 + 600 |
| **Activation** | Press |

</div>

> Allow rage to consume you to massively improve your physical powers for a time before the aftereffects set in.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5,000 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Related

- **Effects:** [Ogre Berserker](../../effects/ogre-berserker.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `OgreBerserker.magiculeCost` | 5,000 | Magicule Cost to activate. |
| `OgreBerserker.transformationDuration` | 3,600 | The duration in tick of the Transformation. |
| `OgreBerserker.transformationDurationMastered` | 7,200 | The duration in tick of the Transformation. |
| `OgreBerserker.cooldown` | 600 | The Cooldown in second after activation. |

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
