# Bullet Punch

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Bullet Punch](../../../assets/icons/mysticism/skill/bullet_punch.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `mysticism:bullet_punch` |
| **Cooldowns (s)** | 15 |
| **Activation** | Passive |

</div>

> You can only be fast, and go even faster. On the next attack, you speed up and deliver four quick attacks.

## How it works

- Triggers when you damage a target

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/mantis_config.toml): The list of intrinsic skills that the race gets.

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/intrinsic_config.toml`](../../configs/config-mysticism-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `BulletPunch.cooldown` | 15 | The cooldown in seconds. |
| `BulletPunch.cooldownMastered` | 15 | The cooldown in seconds when the skill is mastered. |
| `BulletPunch.amount` | 4 | The amount of punches. |

## Tags

`tensura:skills/intrinsic_skills`
