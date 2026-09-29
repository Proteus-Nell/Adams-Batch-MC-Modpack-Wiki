# Anti-Skill

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Anti-Skill](../../../assets/icons/tensura/skill/anti_skill.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:anti_skill` |
| **Activation** | Passive |

</div>

> Become immune to damage from Magic, Skills and Battlewill, destroy barriers and block skill usage of other entities.

## How it works

- Triggers when you damage a target
- Triggers on melee contact
- Triggers when you are attacked
- Triggers when an effect is applied to you

## Obtaining

- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Effects:** [Anti-Skill](../../effects/anti-skill.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `AntiSkill.antiDuration` | 100 | The duration in tick of the Anti-skill effect to apply on targets when used. |

## Tags

`tensura:skills/no_plundering`, `tensura:skills/unique_skills`
