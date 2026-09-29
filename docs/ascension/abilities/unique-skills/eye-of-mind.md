# Eye of Mind

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Eye of Mind](../../../assets/icons/ascension/skill/eye_of_mind.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `ascension:eye_of_mind` |
| **Modes** | 4 |
| **Cooldowns (s)** | 5, 60 |
| **Activation** | Toggle, Press, Hold |

</div>

> Toggle: 10x learning/mastery rate. Modes: Analytical Appraisal (read the battlefield), Analysis (steal a skill from an enemy), Detrimental Gaze (inflict crippling status), Ray of Death (black beam draining a fraction of target HP per second).

## Modes

| # | Mode |
|---|---|
| 1 | Analytical Appraisal |
| 2 | Analysis |
| 3 | Detrimental Gaze |
| 4 | Ray of Death |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Listed in the `additionalUniqueSkills` config option (config/tensura/ascension-common.toml): Unique skills added to the reincarnation pool. Remove an entry to exclude that skill from random reincarnation rolls.

## Related

- **Summons / entities:** Ray Of Death

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `eye_of_mind.enabled` | true | Enable Eye of Mind. |
| `eye_of_mind.passiveBonus` | 9 (0 to 100) | Learning/mastery attribute bonus while toggled (+9 = 10x faster total). |
| `eye_of_mind.rayMagiculePerSec` | 0.02 (0 to 1) | Fraction of max magicule drained per second while Ray of Death is held. |

## Tags

`tensura:skills/unique_skills`
