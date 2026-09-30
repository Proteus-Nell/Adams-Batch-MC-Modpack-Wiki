# Great Sage

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Great Sage](../../../assets/icons/tensura/skill/great_sage.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:great_sage` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 75,000 |
| **Cooldowns (s)** | 10, 5 |
| **Activation** | Toggle, Press |

</div>

> Improve your cognitive skills to learn and cast faster, become able to appraise targets and use analysis to copy skills and process materials to craft or clone items or equipment.

## Modes

| # | Mode |
|---|---|
| 1 | Analytical Appraisal |
| 2 | Analysis |
| 3 | Refining |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you die
- Triggers when you respawn

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| learning | 9 | add |
| mastery | 9 | add |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...
- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.
- Listed in the `AngelicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Angelic skills registry names that can be created via Holy Essence consumption. Format: modid:skill_name
- Listed in the `VirtueSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): Virtue unique skill ids for Michael Ultimate Dominion.

## Related

- **Summons / entities:** Tensura
- **Referenced by:** [｢ Raphael, Lord of Knowledge ｣](../../../tr-nightmares/abilities/ultimate-skills/raphael-knowledge.md), [｢ Raphael, Lord of Wisdom ｣](../../../tr-nightmares/abilities/ultimate-skills/raphael-wisdom.md), [Raphael, Lord of Wisdom](../../../elite-tensura/abilities/ultimate-skills/raphealskill.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `GreatSage.mpAcquirement` | 75,000 | Magicule Acquirement Cost. |
| `GreatSage.chantSpeed` | 2 | The chant speed multiplier when toggled. |
| `GreatSage.learningPoint` | 9 | The bonus number of learning point to gain when toggled. |
| `GreatSage.masteryPoint` | 9 | The bonus number of mastery point to gain when toggled. |
| `GreatSage.analysisLevel` | 8 | The Analysis Level when activated. |
| `GreatSage.analysisLevelMastered` | 18 | The Analysis Level when activated with Mastery. |
| `GreatSage.analysisRadius` | 15 | The Analysis Radius when activated. |
| `GreatSage.analysisRadiusMastered` | 25 | The Analysis Radius when activated with Mastery. |
| `GreatSage.copyRange` | 10 | The range in block of Analysis's Copy on mobs. |
| `GreatSage.copyRangeMagic` | 30 | The range in block of Analysis's Copy on magic circles. |
| `GreatSage.copyChance` | 25 | The chance to success copying skills from targets. |
| `GreatSage.copyChanceMastered` | 50 | The chance to success copying skills from targets when mastered. |
| `GreatSage.copyCooldownSuccess` | 10 | The cooldown in second when the user successfully copied a skill from targets. |
| `GreatSage.copyCooldownFail` | 5 | The cooldown in second when the user failed to copy a skill from targets. |

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

`tensura:skills/unique_skills`, `tensura:skills/virtue_skills`, `tensura:skills/wisdom`
