# Creator

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Creator](../../../assets/icons/tensura/skill/creator.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:creator` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 75,000 |
| **Activation** | Press |

</div>

> Create any Unique Skill and use it for a limited amount of time.

## Modes

| # | Mode |
|---|---|
| 1 | Analytical Appraisal |
| 2 | Skill Creation |

## How it works

- Activated by pressing the skill key
- Triggers when you die
- Triggers when you respawn

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.

## Related

- **Effects:** [Anti-Skill](../../effects/anti-skill.md)
- **Referenced by:** [｢ Astral Light, Lord of Creation ｣](../../../tr-nightmares/abilities/ultimate-skills/astral-light.md), [Hephaestus, Lord of Creation](../../../elite-tensura/abilities/ultimate-skills/hephaestus.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Creator.mpAcquirement` | 75,000 | Magicule Acquirement Cost. |
| `Creator.analysisLevel` | 2 | The Analysis Level when activated. |
| `Creator.analysisLevelMastered` | 6 | The Analysis Level when activated with Mastery. |
| `Creator.analysisRadius` | 0 | The Analysis Radius when activated. |
| `Creator.analysisRadiusMastered` | 5 | The Analysis Radius when activated with Mastery. |
| `Creator.creationCooldown` | 1,200 | The cooldown in second after creating a Skill. |
| `Creator.creationVanishTimer` | 1,200 | The cooldown in second before the created skill vanishes. |
| `Creator.masteryGainMultiplier` | 5 | The multiplier for mastery point gaining when created a Skill. |
| `Creator.uniqueSkills` | "tensura:anti_skill", "tensura:analyst", "tensura:absolute_severance", "tensura:berserk", "tensura:berserker", "tensura:bewilder", "tensura:chef", "tensura:commander", "tensura:cook", "tensura:falsifier", "tensura:fighter", "tensura:fusionist", "tensura:gourmand", "tensura:guardian", "tensura:healer", "tensura:martial_master", "tensura:mathematician", "tensura:murderer", "tensura:musician", "tensura:observer" ... (39 total) | List of Unique skills that can be created by Creator. |

## Tags

`tensura:skills/unique_skills`
