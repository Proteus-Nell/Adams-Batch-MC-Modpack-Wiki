# Heat Wave

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Heat Wave](../../../assets/icons/tensura/skill/heat_wave.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:heat_wave` |
| **Modes** | 2 |
| **Cooldowns (s)** | 1 mastered, 3 otherwise |
| **Activation** | Press, Hold |

</div>

> Shoot a fiery projectile or summon a short-ranged fire storm which will damage all nearby entities.

## Modes

| # | Mode |
|---|---|
| 1 | Heat Sphere |
| 2 | Heat Storm |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 20 or 40 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Innate to mobs: [Shizu](../../mobs/shizu.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/sculk_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Referenced by:** [Flame Manipulation](flame-manipulation.md), [｢ Amaterasu, Lord of Shimmering Flames ｣](../../../tr-nightmares/abilities/ultimate-skills/amaterasu.md), [Phainon, The Deliverer](../../../tensura-more-skills/abilities/ultimate-skills/phainon.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `HeatWave.magiculeCostSphere` | 40 | Magicule Cost to activate Heat Sphere. |
| `HeatWave.magiculeCostStorm` | 20 | Magicule Cost to activate Heat Storm. |
| `HeatWave.sphereDamage` | 30 | The Damage of the Heat Sphere. |
| `HeatWave.sphereBurnTick` | 20 | The duration in tick of the burning when a target got inflicted by the Heat Sphere. |
| `HeatWave.stormRadius` | 5 | The Radius of the Heat Storm. |
| `HeatWave.stormDamage` | 5 | The Damage of the Heat Storm. |
| `HeatWave.stormBurnTick` | 200 | The duration in tick of the burning when a target got inflicted by the Heat Storm. |
| `HeatWave.sphereCooldown` | 3 | The cooldown for Heat Sphere. |
| `HeatWave.sphereCooldownMastered` | 1 | The cooldown for Heat Sphere when mastered. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/extra_skills`
