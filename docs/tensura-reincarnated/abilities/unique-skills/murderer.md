# Murderer

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Murderer](../../../assets/icons/tensura/skill/murderer.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:murderer` |
| **Acquisition cost (MP)** | 50,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> Disappear into the shadows and deal massive damage, also become undetectable by sound.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Attack Damage | 50 | add |
| attack | damage | add |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.
- Listed in the `AngelicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Angelic skills registry names that can be created via Holy Essence consumption. Format: modid:skill_name
- Listed in the `VirtueSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): Virtue unique skill ids for Michael Ultimate Dominion.

## Related

- **Effects:** [Presence Concealment](../../effects/presence-concealment.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Murderer.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Murderer.magiculeCost` | 50 | Magicule Cost to activate. |
| `Murderer.concealmentLevel` | 3 | The level of the Presence Conceal when hold down the skill. |
| `Murderer.damageBoost` | 50 | The amount of bonus physical damage when hold down the skill. |
| `Murderer.damageBoostMastery` | 150 | The amount of bonus physical damage when hold down the skill with mastery. |

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

`tensura:skills/unique_skills`
