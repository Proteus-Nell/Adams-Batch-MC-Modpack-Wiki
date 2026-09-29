# Fighter

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Fighter](../../../assets/icons/tensura/skill/fighter.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:fighter` |
| **Acquisition cost (MP)** | 50,000 |
| **Cooldowns (s)** | 3 |
| **Activation** | Toggle |

</div>

> Achieve mastery through discipline. Learn combat and magic abilities instantly, gain more mastery points, and hit much harder.

## How it works

- Can be toggled on and off
- Adjusted by scrolling while active
- Triggers when you damage a target

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| mastery | 2 | add |
| dodge | 0.25 | add |
| invulnerability | 2 | add |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Fighter.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Fighter.attackBoost` | 75 | The physical attack damage boost when in Slot. |
| `Fighter.attackBoostMastered` | 150 | The physical attack damage boost when in Slot with mastery. |
| `Fighter.masteryPoint` | 2 | The bonus number of mastery point to gain when toggled. |
| `Fighter.dodgeStrength` | 0.25 | The bonus dodge strength when toggled. |
| `Fighter.dodgeInvulnerability` | 2 | The bonus dodge invulnerability when toggled. |

## Tags

`tensura:skills/unique_skills`
