# Great Mage

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Great Mage](../../../assets/icons/ascension/skill/great_mage.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `ascension:great_mage` |
| **Modes** | 3 |
| **Cooldowns (s)** | 1 |
| **Activation** | Toggle, Press |

</div>

> Toggle: +19% learning/mastery rate for all skills, plus Chant Annulment for mastered magic. Modes: Magic Chant (learn new magic for XP), Study (steal a skill from a target's mind), Create Tome (turn a learned magic into a tome book).

## Modes

| # | Mode |
|---|---|
| 1 | Magic Chant |
| 2 | Study |
| 3 | Create Tome |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key

## Obtaining

- Listed in the `additionalUniqueSkills` config option (config/tensura/ascension-common.toml): Unique skills added to the reincarnation pool. Remove an entry to exclude that skill from random reincarnation rolls.

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `great_mage.enabled` | true | Enable Great Mage. |
| `great_mage.passiveBonus` | 0.19 (0 to 100) | Learning/mastery attribute bonus while toggled. |
| `great_mage.tomeCooldownSeconds` | 1 (0 to 3,600) | Create Tome cooldown (seconds). Short anti-spam gate — the real cost is the XP charged inside the tome GUI. |
| `great_mage.chantCooldownSecondsMastered` | 300 (0 to 3,600) | Magic Chant cooldown, mastered (seconds). |
| `great_mage.chantCooldownSeconds` | 600 (0 to 3,600) | Magic Chant cooldown, unmastered (seconds). |
| `great_mage.cooldownSecondsMastered` | 60 (0 to 3,600) | Study cooldown, mastered (seconds). |
| `great_mage.cooldownSeconds` | 120 (0 to 3,600) | Study cooldown, unmastered (seconds). |
| `great_mage.chantXpCost` | 10 (0 to 1,000) | Vanilla XP levels consumed per Magic Chant cast. |

## Tags

`tensura:skills/unique_skills`
