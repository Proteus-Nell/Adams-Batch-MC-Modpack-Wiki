# Reflector

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Reflector](../../../assets/icons/tensura/skill/reflector.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:reflector` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 30,000 |
| **Cooldowns (s)** | 5 |
| **Activation** | Press, Hold |

</div>

> Turn back the tides of battle by reflecting all of the received damage. Unleash a devastating projectile attack or counter an attack directly.

## Modes

| # | Mode |
|---|---|
| 1 | Echo Reflection |
| 2 | Echo Counter |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Adjusted by scrolling while active
- Triggers when you are attacked
- Triggers when you take damage
- Triggers when a projectile hits you
- Triggers when you respawn

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -1 | multiply total |
| Attack Damage | -1 | multiply total |
| Attack Speed | -1 | multiply total |
| Jump Strength | -1 | multiply total |
| Block Interaction Range | -1 | multiply total |
| Dodge Negate Chance | -1 | multiply total |
| Auto Melee Dodge Chance | -1 | multiply total |
| Glide Speed Multiplier | -1 | multiply total |
| Swim Speed Multiplier | -1 | multiply total |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Reflector.mpAcquirement` | 30,000 | Magicule Acquirement Cost. |
| `Reflector.counterSpeedMultiplier` | 0 | The speed multiplier when activating the Echo Counter mode. |
| `Reflector.counterSpeedMultiplierMastered` | 1 | The speed multiplier when activating the Echo Counter mode with mastery. |
| `Reflector.counterDamageMultiplier` | 2.5 | The reflected damage when using Echo Counter. |
| `Reflector.counterProjectileSpeedMultiplier` | 2 | The reflected projectile speed when using Echo Counter. |
| `Reflector.counterCooldown` | 5 | The cooldown in second of the Echo Counter mode. |
| `Reflector.maximumPoint` | 100 | The base maximum echo point to store. |
| `Reflector.bonusPointMultiplier` | 0.001 | The multiplier of user's EP to be calculated for bonus echo point. |
| `Reflector.reflectionDamageMultiplier` | 3 | The projectile damage multiplier when using Echo Reflection. |
| `Reflector.reflectionDamageMultiplierMastered` | 5 | The projectile damage multiplier when using Echo Reflection with mastery. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- Echo Points: %s

</details>

## Tags

`tensura:skills/unique_skills`
