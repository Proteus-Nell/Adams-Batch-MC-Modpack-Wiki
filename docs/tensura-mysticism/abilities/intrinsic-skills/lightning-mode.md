# Lightning Mode

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Lightning Mode](../../../assets/icons/mysticism/skill/lightning_mode.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `mysticism:lightning_mode` |
| **Cooldowns (s)** | 1,200 |
| **Activation** | Press |

</div>

> Burst forth with an incredible speed boost, gaining doubled EP temporarily on top of higher damage. Beware of the terrible drawbacks.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/beetle_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Effects:** [Lightning Mode](../../effects/lightning-mode.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/intrinsic_config.toml`](../../configs/config-mysticism-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `LightningMode.magiculeCost` | 0 | Magicule Cost to activate. |
| `LightningMode.transformationDuration` | 3,600 | The duration in tick of the Transformation. |
| `LightningMode.transformationDurationMastered` | 7,200 | The duration in tick of the Transformation. |
| `LightningMode.cooldown` | 1,200 | The Cooldown in second after activation. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

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
