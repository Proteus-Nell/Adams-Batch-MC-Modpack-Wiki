# Analyst

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Analyst](../../../assets/icons/tensura/skill/analyst.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:analyst` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 30,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> Enhance cognitive processing, analyze targets and phenomena, accelerate magic casting and deepen understanding of the laws of the world to optimize all actions.

## Modes

| # | Mode |
|---|---|
| 1 | Analytical Appraisal |
| 2 | Analyze |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you die
- Triggers when you respawn
- Does something when mastered

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| learning | 2 | add |
| mastery | 2 | add |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.
- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.

## Related

- **Related skills:** [Law Manipulation](../extra-skills/law-manipulation.md)
- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Analyst.mpAcquirement` | 30,000 | Magicule Acquirement Cost. |
| `Analyst.analysisLevel` | 18 | The Analysis Level when activated. |
| `Analyst.analysisLevelMastered` | 28 | The Analysis Level when activated with Mastery. |
| `Analyst.analysisRadius` | 20 | The Analysis Radius when activated. |
| `Analyst.analysisRadiusMastered` | 25 | The Analysis Radius when activated with Mastery. |
| `Analyst.analyzeRange` | 30 | The range in block of Analyze. |
| `Analyst.analyzeTime` | 100 | The hold time in tick of Analyze to copy a Magic. |
| `Analyst.analyzeTimeMastered` | 60 | The hold time in tick of Analyze to copy a Magic. |
| `Analyst.learningPoint` | 2 | The bonus number of learning point to gain when toggled. |
| `Analyst.masteryPoint` | 2 | The bonus number of mastery point to gain when toggled. |
| `Analyst.chantSpeed` | 2 | The chant speed multiplier when toggled. |

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
