# Seer

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Seer](../../../assets/icons/tensura/skill/seer.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:seer` |
| **Acquisition cost (MP)** | 20,000 |
| **Cooldowns (s)** | 10, 10 + duration ÷ 20 |
| **Activation** | Toggle, Press |

</div>

> See everything. Foresee your opponent’s moves. Dodge or mitigate their attacks and predict their movement to score critical strikes.

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you take damage

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| melee | melee amount | add |
| projectile | projectile amount | add |
| critical | chance | add |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Effects:** [Future Vision](../../effects/future-vision.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Seer.mpAcquirement` | 20,000 | Magicule Acquirement Cost. |
| `Seer.meleeDodge` | 25 | Melee Dodge Chance when toggled. |
| `Seer.meleeDodgeMastered` | 50 | Melee Dodge Chance when toggled with mastered. |
| `Seer.projectileDodge` | 25 | Projectile Dodge Chance when toggled. |
| `Seer.projectileDodgeMastered` | 50 | Projectile Dodge Chance when toggled with mastered. |
| `Seer.criticalChance` | 33 | Critical Attack Chance when toggled. |
| `Seer.criticalChanceMastered` | 50 | Critical Attack Chance when toggled with mastered. |
| `Seer.inputMultiplier` | 0.7 | The input damage multiplier when toggled. |
| `Seer.inputMultiplierMastered` | 0.5 | The input damage multiplier when toggled with mastery. |
| `Seer.visionDuration` | 200 | The duration in tick of the Future Vision effect. |
| `Seer.visionDurationMastered` | 400 | The duration in tick of the Future Vision effect when mastered. |
| `Seer.visionCooldown` | 10 | The cooldown in second of the Future Vision effect. |

## Tags

`tensura:skills/unique_skills`
