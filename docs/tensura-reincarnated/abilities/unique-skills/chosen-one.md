# Chosen One

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Chosen One](../../../assets/icons/tensura/skill/chosen_one.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:chosen_one` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 90,000 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Toggle, Press, Hold |

</div>

> Radiate authority and charisma to force fear into the hearts of your enemies and to make them follow you instead, while empowering yourself and your allies.

## Modes

| # | Mode |
|---|---|
| 1 | Hero's Haki |
| 2 | Hero's Charisma |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Hero's Haki | 25 |  |
| Hero's Charisma | 200 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Does something when first learned
- Triggers when one of your subordinates dies

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.95 | multiply total |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.

## Related

- **Related skills:** [Spiritual Attack Resistance](../resistance-skills/spiritual-attack-resistance.md), [Spiritual Attack Nullification](../resistance-skills/spiritual-attack-nullification.md)
- **Effects:** [Ally Boost](../../effects/ally-boost.md), [Mind Control](../../effects/mind-control.md), [Rampage](../../effects/rampage.md)
- **Referenced by:** [｢ True Hero, King of Champions ｣](../../../tr-nightmares/abilities/ultimate-skills/true-hero.md), [｢ Yog-Sothoth, Lord of Space-Time ｣](../../../tr-nightmares/abilities/ultimate-skills/yog-sothoth.md), [Phainon, The Deliverer](../../../tensura-more-skills/abilities/ultimate-skills/phainon.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `ChosenOne.mpAcquirement` | 90,000 | Magicule Acquirement Cost. |
| `ChosenOne.magiculeCostHaki` | 25 | Magicule Cost to activate Hero Haki. |
| `ChosenOne.magiculeCostCharisma` | 200 | Magicule Cost to activate Hero's Charisma. |
| `ChosenOne.heroLevel` | 5 | The level of the Hero of the Village effect. |
| `ChosenOne.luckLevel` | 5 | The level of the Luck effect. |
| `ChosenOne.allyCritChance` | 50 | The amount of Critical Chance of the Ally Boost each level.<br>Chosen One has Ally Boost II, Villain has Ally Boost I |
| `ChosenOne.meleeDodge` | 10 | Melee Dodge Chance for the user and allies when activated. |
| `ChosenOne.projectileDodge` | 10 | Projectile Dodge Chance for the user and allies when activated. |
| `ChosenOne.blessingRadius` | 15 | The radius in block of the Hero's Blessing's effect on allies. |
| `ChosenOne.controlRadius` | 10 | The radius in block of the Hero's Charisma's effect. |
| `ChosenOne.controlDuration` | 2,400 | The duration in tick of the Mind Control effect when activating Hero's Charisma (-1 = permanent). |
| `ChosenOne.controlResistedDuration` | 1,200 | The duration in tick of the Mind Control effect when activating Hero's Charisma while the target has Spiritual Attack Resistance (-1 = permanent). |
| `ChosenOne.hpMultiplier` | 0.5 | The multiplier of Max Health when an entity is revived as Ally with Hero's Charisma. |
| `ChosenOne.shpMultiplier` | 0.5 | The multiplier of Max Spiritual Health when an entity is revived as Ally with Hero's Charisma. |

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `Haki.speedMultiplier` | 0.05 | Activation Speed Multiplier when activated. |
| `Haki.epAcquirement` | 100,000 | EP Requirement for Learning. |
| `Haki.magiculeCost` | 25 | Magicule Cost to activate. |
| `Haki.speedMultiplier` | 0.05 | Activation Speed Multiplier when activated. |
| `Haki.speedMultiplierMastered` | 0.1 | Activation Speed Multiplier when activated with mastery. |
| `Haki.hakiRadius` | 15 | The attack radius of the haki in blocks. |
| `Haki.epDifferenceMultiplier` | 0.25 | The EP difference multiplier for each Fear Level. |
| `Haki.fearDuration` | 200 | The duration in tick of the Fear effect when applied. |
| `Haki.cooldown` | 5 | The cooldown in second of the haki. |
| `Haki.cooldownMastered` | 3 | The cooldown in second of the haki when mastered. |

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
