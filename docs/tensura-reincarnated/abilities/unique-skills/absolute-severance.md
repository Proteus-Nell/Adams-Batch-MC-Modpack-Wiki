# Absolute Severance

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Absolute Severance](../../../assets/icons/tensura/skill/absolute_severance.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:absolute_severance` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 60,000 |
| **Cooldowns (s)** | 3 |
| **Activation** | Press |

</div>

> Wield the power to cut through any who stand in your path, whether by coating your strikes or launching slashing projectiles that sever all in their path.

## Modes

| # | Mode |
|---|---|
| 1 | Severance Coat |
| 2 | Severance Cutter |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Severance Coat | 1,000 |  |
| Severance Cutter | 20,000 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Effects:** [Severance Blade](../../effects/severance-blade.md)
- **Referenced by:** [Time Traveler](../../../tr-nightmares/abilities/unique-skills/time-traveler.md), [｢ Yog-Sothoth, Lord of Space-Time ｣](../../../tr-nightmares/abilities/ultimate-skills/yog-sothoth.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `AbsoluteSeverance.mpAcquirement` | 60,000 | Magicule Acquirement Cost. |
| `AbsoluteSeverance.magiculeCostCoating` | 1,000 | Magicule Cost to activate Coating. |
| `AbsoluteSeverance.magiculeCostProjectile` | 20,000 | Magicule Cost to activate Severance Projectile. |
| `AbsoluteSeverance.coatingDuration` | 12,000 | The duration in tick of the Severance Blade effect (Coating). |
| `AbsoluteSeverance.coatingLevel` | 5 | The level of the Severance Blade effect (+ 10 Damage Boost each level). |
| `AbsoluteSeverance.coatingLevelMastered` | 20 | The level of the Severance Blade effect when mastered. |
| `AbsoluteSeverance.projectileDamage` | 50 | The damage of the Severance Projectile. |
| `AbsoluteSeverance.projectileDamageMastered` | 300 | The damage of the Severance Projectile when mastered. |
| `AbsoluteSeverance.projectileSize` | 5 | The size of the Severance Projectile. |
| `AbsoluteSeverance.projectileSizeMastered` | 8 | The size of the Severance Projectile when mastered. |
| `AbsoluteSeverance.projectileDuration` | 20 | The duration in tick of the Severance Projectile. |
| `AbsoluteSeverance.projectileDurationMastered` | 40 | The duration in tick of the Severance Projectile when mastered. |
| `AbsoluteSeverance.projectileCooldown` | 3 | The cooldown in second of the Severance Projectile. |

## Tags

`tensura:skills/unique_skills`
