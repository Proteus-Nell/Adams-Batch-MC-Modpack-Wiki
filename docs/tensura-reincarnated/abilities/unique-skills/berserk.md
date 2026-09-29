# Berserk

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Berserk](../../../assets/icons/tensura/skill/berserk.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:berserk` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 20,000 |
| **Cooldowns (s)** | 1,200, 600 |
| **Activation** | Toggle, Press |

</div>

> Massively empower your body and infuse it with a flame aura. Allows you to go into a risky but overwhelmingly powerful berserker mode.

## Modes

| # | Mode |
|---|---|
| 1 | Rage |
| 2 | Mad Ogre |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 300 or 5,000 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Effects:** [Mad Ogre](../../effects/mad-ogre.md), [Rampage](../../effects/rampage.md), [Strengthen](../../effects/strengthen.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Berserk.mpAcquirement` | 20,000 | Magicule Acquirement Cost. |
| `Berserk.magiculeCostFlameAura` | 200 | Magicule Cost to each attack while toggled Flame Aura. |
| `Berserk.magiculeCostRage` | 300 | Magicule Cost to activate Rage. |
| `Berserk.magiculeCostMadOgre` | 5,000 | Magicule Cost to activate Mad Ogre. |
| `Berserk.masteryGainMultiplier` | 5 | The multiplier for mastery point gaining when activating Mad Ogre. |
| `Berserk.rageDuration` | 6,000 | The duration in tick of the Strengthen effect when activated Rage. |
| `Berserk.rageLevel` | 5 | The level of the Strengthen effect when activated Rage (+3 Attack Damage per level). |
| `Berserk.rageLevelMastered` | 10 | The level of the Strengthen effect when activated Rage with Mastered. |
| `Berserk.madOgreDuration` | 12,000 | The duration in tick of the Mad Ogre effect when activated. |
| `Berserk.madOgreLevel` | 1 | The level of the Mad Ogre effect when activated. |
| `Berserk.madOgreLevelMastered` | 2 | The level of the Mad Ogre effect when activated with Mastered. |
| `Berserk.orbDamage` | 100 | The damage of each flame orb shot by Mad Ogres when mastered. |
| `Berserk.orbBlast` | 4 | The blast radius of each flame orb when triggered when mastered. |
| `Berserk.defenceMultiplier` | 0.5 | The input damage multiplier that the user takes when in defence mode of Mad Ogres. |
| `Berserk.cooldown` | 600 | The Cooldown in second after Mad Ogre runs out. |
| `Berserk.flameAuraBoost` | 2 | The Flame Damage Boost when toggled Flame Aura. |
| `Berserk.flameAuraBurnTick` | 200 | How long in tick that the target will be set on fire when attacked with Flame Aura toggled. |
| `Berserk.flameAuraDamage` | 0.5 | How Flame damage multiplied based on the user's physical/battlewill attack with Flame Aura toggled. |

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
