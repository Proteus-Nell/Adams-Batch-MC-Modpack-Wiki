# Divine Berserker

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Divine Berserker](../../../assets/icons/tensura/skill/divine_berserker.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:divine_berserker` |
| **Acquisition cost (MP)** | 30,000 |
| **Cooldowns (s)** | 600, duration ÷ 20 + 600 |
| **Activation** | Press |

</div>

> Empower your body by a massive amount but beware the aftereffects.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10,000 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target

## Obtaining

- Intrinsic skill of: [Divine Fighter](../../races/divine-fighter.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.

## Related

- **Effects:** [Ogre Berserker](../../effects/ogre-berserker.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `DivineBerserker.mpAcquirement` | 30,000 | Magicule Acquirement Cost. |
| `DivineBerserker.magiculeCost` | 10,000 | Magicule Cost to activate. |
| `DivineBerserker.battlewillMultiplier` | 1.5 | The Battlewill damage multiplier that the user does when activated. |
| `DivineBerserker.battlewillMultiplierMastered` | 2 | The Battlewill damage multiplier that the user does when activated with mastery. |
| `DivineBerserker.transformationDuration` | 3,600 | The duration in tick of the Transformation. |
| `DivineBerserker.transformationDurationMastered` | 7,200 | The duration in tick of the Transformation. |
| `DivineBerserker.cooldown` | 600 | The Cooldown in second after activation. |

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

`tensura:skills/unique_skills`
