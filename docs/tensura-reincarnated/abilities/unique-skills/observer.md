# Observer

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Observer](../../../assets/icons/tensura/skill/observer.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:observer` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 30,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> See all, evade all. Instinctively avoid attacks, detect concealed dangers, and identify hidden entities. Nothing escapes your watchful gaze.

## Modes

| # | Mode |
|---|---|
| 1 | Danger Detection |
| 2 | Presence Detection |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when a mob targets you

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Presence Sense | 1 | add |
| Presence Sense Radius | 20 | add |
| melee | 20 | add |
| projectile | 100 | add |

## Obtaining

- Innate to mobs: [Shin Ryusei](../../mobs/shin-ryusei.md)
- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Summons / entities:** Tensura
- **Referenced by:** [Pride Manas](../../../tr-nightmares/abilities/ultimate-skills/pride-manas.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Observer.mpAcquirement` | 30,000 | Magicule Acquirement Cost. |
| `Observer.bonusSenseLevel` | 1 | The Bonus Presence Sense Level when activated. |
| `Observer.bonusSenseRadius` | 20 | The Bonus Presence Sense Radius when activated. |
| `Observer.meleeDodge` | 20 | Melee Dodge Chance when toggled. |
| `Observer.projectileDodge` | 100 | Projectile Dodge Chance when toggled. |

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
