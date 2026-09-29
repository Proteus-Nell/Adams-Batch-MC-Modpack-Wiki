# Falsifier

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Falsifier](../../../assets/icons/tensura/skill/falsifier.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:falsifier` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 15,000 |
| **Cooldowns (s)** | cooldown + 120, 5 mastered, 10 otherwise |
| **Activation** | Press, Hold |

</div>

> See through falsehoods and invisibility, conceal your presence from prying eyes and create illusions.

## Modes

| # | Mode |
|---|---|
| 1 | Presence Concealment |
| 2 | Illusion |
| 3 | Fake Death |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 200 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you take damage

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.4 | multiply total |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Effects:** [Falsifier](../../effects/falsifier.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Falsifier.mpAcquirement` | 15,000 | Magicule Acquirement Cost. |
| `Falsifier.magiculeCost` | 200 | Magicule Cost to activate Concealment. |
| `Falsifier.concealmentDuration` | 2,400 | The duration in tick of the Concealment effect when activated. |
| `Falsifier.concealmentCooldown` | 20 | The cooldown in second of the Concealment Mode. |
| `Falsifier.concealmentCooldownMastered` | 0 | The cooldown in second of the Concealment Mode when mastered. |
| `Falsifier.fakeSpeedMultiplier` | 0.6 | Activation Speed Multiplier when activating Fake Death. |
| `Falsifier.fakeSpeedMultiplierMastered` | 0.8 | Activation Speed Multiplier when activating Fake Death with mastery. |
| `Falsifier.fakeMaxTime` | 600 | The maximum time in tick that the user can hold down Fake Death. |
| `Falsifier.fakeInputMultiplier` | 0.5 | The input damage multiplier that the user takes when Fake Death is triggered. |
| `Falsifier.fakeConcealmentDuration` | 60 | The duration in tick of the Concealment effect after Fake Death is triggered. |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- Clear Slot
- Empty

</details>

## Tags

`tensura:skills/endearing`, `tensura:skills/unique_skills`
