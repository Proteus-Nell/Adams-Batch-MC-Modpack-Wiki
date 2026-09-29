# Usurper

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Usurper](../../../assets/icons/tensura/skill/usurper.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:usurper` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 50,000 |
| **Cooldowns (s)** | 10 |
| **Activation** | Press |

</div>

> Seize your enemies' power or their summons. Steal their abilities and take control of their skills, draining their strength for your own.

## Modes

| # | Mode |
|---|---|
| 1 | Rob |
| 2 | Copy |
| 3 | Force Takeover |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Rob | 1,000 |  |
| Copy | 1,000 |  |
| Force Takeover | 5,000 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Triggers on melee contact

## Obtaining

- Innate to mobs: [Hinata Sakaguchi](../../mobs/hinata-sakaguchi.md)
- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Effects:** [Mind Control](../../effects/mind-control.md), [Anti-Skill](../../effects/anti-skill.md)
- **Referenced by:** [Time Traveler](../../../tr-nightmares/abilities/unique-skills/time-traveler.md), [｢ Yog-Sothoth, Lord of Space-Time ｣](../../../tr-nightmares/abilities/ultimate-skills/yog-sothoth.md), [Pride Manas](../../../tr-nightmares/abilities/ultimate-skills/pride-manas.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Usurper.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Usurper.magiculeCostRob` | 1,000 | Magicule Cost to activate Rob. |
| `Usurper.magiculeCostCopy` | 1,000 | Magicule Cost to activate Copy. |
| `Usurper.magiculeCostTakeover` | 5,000 | Magicule Cost to activate Force Takeover. |
| `Usurper.epDrain` | 0.01 | The multiplier of the target's EP to drain when attacked by the user. |
| `Usurper.robSuccess` | 25 | The percentage chance to rob successfully. |
| `Usurper.robSuccessMastered` | 50 | The percentage chance to rob successfully when mastered. |
| `Usurper.robMastery` | 0.5 | The multiplier of max mastery that the robbed skill gains. |
| `Usurper.robCooldown` | 10 | The cooldown in second of the Rob mode. |
| `Usurper.copySuccess` | 25 | The percentage chance to copy successfully. |
| `Usurper.copySuccessMastered` | 50 | The percentage chance to copy successfully when mastered. |
| `Usurper.copyMastery` | 0.5 | The multiplier of max mastery that the copied skill gains. |
| `Usurper.copyCooldown` | 10 | The cooldown in second of the Copy mode. |
| `Usurper.takeoverEP` | 0.75 | The multiplier of the user's EP that the targeted spirit's owner needs to be higher to not be affected by Takeover. |
| `Usurper.takeoverDuration` | 6,000 | The duration in tick of the Takeover effect on the controlled spirit (-1 = permanent). |
| `Usurper.takeoverDurationMastered` | 12,000 | The duration in tick of the Takeover effect on the controlled spirit when mastered (-1 = permanent). |
| `Usurper.takeoverCooldown` | 10 | The cooldown in second of the Force Takeover mode. |

## Tags

`tensura:skills/greed`, `tensura:skills/unique_skills`
