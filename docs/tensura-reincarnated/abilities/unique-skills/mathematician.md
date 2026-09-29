# Mathematician

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Mathematician](../../../assets/icons/tensura/skill/mathematician.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:mathematician` |
| **Acquisition cost (MP)** | 40,000 |
| **Activation** | Toggle, Press |

</div>

> Use mathematics to improve your combat abilities, become able to use analytical appraisal to assess all.

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you die
- Triggers when you respawn

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| degrade | 1 | add |
| melee | 10 | add |
| projectile | 10 | add |
| dodgeNegate | 50 | add |
| critical | 75 | add |
| learning | 2 | add |
| mastery | 2 | add |

## Obtaining

- Innate to mobs: [Hinata Sakaguchi](../../mobs/hinata-sakaguchi.md)
- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Summons / entities:** Tensura
- **Referenced by:** [Alteration](../../../tr-nightmares/abilities/extra-skills/alteration.md), [Pride Manas](../../../tr-nightmares/abilities/ultimate-skills/pride-manas.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Mathematician.mpAcquirement` | 40,000 | Magicule Acquirement Cost. |
| `Mathematician.analysisLevel` | 8 | The Analysis Level when activated. |
| `Mathematician.analysisLevelMastered` | 12 | The Analysis Level when activated with Mastery. |
| `Mathematician.analysisRadius` | 5 | The Analysis Radius when activated. |
| `Mathematician.analysisRadiusMastered` | 15 | The Analysis Radius when activated with Mastery. |
| `Mathematician.chantSpeed` | 2 | The chant speed multiplier when toggled. |
| `Mathematician.meleeDodge` | 10 | Melee Dodge Chance when toggled. |
| `Mathematician.projectileDodge` | 10 | Projectile Dodge Chance when toggled. |
| `Mathematician.dodgeNegation` | 50 | Dodge Negation Chance when toggled. |
| `Mathematician.critChance` | 75 | Critical Attack Chance when toggled. |
| `Mathematician.learningPoint` | 2 | The bonus number of learning point to gain when toggled. |
| `Mathematician.masteryPoint` | 2 | The bonus number of mastery point to gain when toggled. |

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
