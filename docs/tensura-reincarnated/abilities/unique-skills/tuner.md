# Tuner

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Tuner](../../../assets/icons/tensura/skill/tuner.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:tuner` |
| **Acquisition cost (MP)** | 50,000 |
| **Cooldowns (s)** | 1,200 |
| **Activation** | Passive |

</div>

> Change your fate survive fatal blows, regenerate instantly and manipulate probability.

## How it works

- Has a continuous (per-tick) effect
- Triggers when you die

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Effects:** [Fate Change](../../effects/fate-change.md)
- **Referenced by:** [｢ Mood Maker, Lord of Psychology ｣](../../../tr-nightmares/abilities/ultimate-skills/mood-maker.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Tuner.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Tuner.hpMultiplier` | 0.25 | The multiplier of HP that the user needs to below to activate Unexpected Result. |
| `Tuner.bonusAttack` | 30 | The bonus attack damage when activated Unexpected Result with mastery (doubled with Mastery). |
| `Tuner.bonusAttackSpeed` | 0.2 | The bonus attack speed when activated Unexpected Result with mastery (doubled with Mastery). |
| `Tuner.bonusSpeed` | 0.04 | The bonus speed when activated Unexpected Result with mastery (doubled with Mastery). |
| `Tuner.bonusSwim` | 1 | The bonus swim speed when activated Unexpected Result with mastery (doubled with Mastery). |
| `Tuner.bonusMeleeDodge` | 15 | The bonus melee dodge chance when activated Unexpected Result with mastery (doubled with Mastery). |
| `Tuner.bonusProjectileDodge` | 15 | The bonus projectile dodge chance when activated Unexpected Result with mastery (doubled with Mastery). |
| `Tuner.hpRevive` | 1 | The multiplier of HP that the user gets when revived by the skill. |
| `Tuner.shpRevive` | 1 | The multiplier of SHP that the user gets when revived by the skill. |
| `Tuner.epRevive` | 0.5 | The multiplier of Aura/Magicule that the user gets when revived by the skill. |
| `Tuner.epReviveMastered` | 0.75 | The multiplier of Aura/Magicule that the user gets when revived by the skill with mastery. |
| `Tuner.deathReset` | 1,200 | The timer in tick till the next death count reset. |

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
