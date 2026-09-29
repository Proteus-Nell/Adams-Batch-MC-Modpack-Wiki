# Pride

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Pride](../../../assets/icons/tensura/skill/pride.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:pride` |
| **Modes** | 1 |
| **Acquisition cost (MP)** | 100,000 |
| **Max mastery** | 1,500 |
| **Cooldowns (s)** | max((45 × mastery), 1), max((4.5 × mastery), 1) |
| **Activation** | Press, Hold |

</div>

> Turn the strength of your opponents into your own and turn the tides of battle. Copy abilities when you are struck by them, provided you meet the necessary conditions.

## Modes

| # | Mode |
|---|---|
| 1 | Copy |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Triggers when you damage a target
- Triggers on melee contact
- Triggers when you are attacked
- Triggers when you take damage
- Triggers when an effect is applied to you
- Triggers when a projectile hits you
- Triggers when you die
- Triggers when you respawn

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `DemonicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Demonic skills registry names that can be created via Demon Essence consumption. Format: modid:skill_name

## Related

- **Referenced by:** [｢ Lucifer, Lord of Pride ｣](../../../tr-nightmares/abilities/ultimate-skills/lucifer.md), [｢ Michael, Lord of Justice ｣](../../../tr-nightmares/abilities/ultimate-skills/michael.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Pride.mpAcquirement` | 100,000 | Magicule Acquirement Cost. |
| `Pride.copyChance` | 20 | The skill copy chance when attacked. |
| `Pride.copyChanceMastered` | 100 | The skill copy chance when attacked with mastery. |
| `Pride.copyMastery` | 0.0004 | The amount of mastery that Pride gains per Magicule Cost of the successfully copied ability. |
| `Pride.copyMasteryFail` | 0 | The multiplier of mastery that Pride gains per Magicule Cost of the failed ability. |
| `Pride.copyCooldown` | 45 | The cooldown in second that Pride gets per Mastery gained from successfully copying an ability. |
| `Pride.copyCooldownFail` | 4.5 | The cooldown in second that Pride gets per Mastery gained from failing to copy an ability. |

Set in [`config/tensura/ability/skill_config.toml`](../../configs/config-tensura-ability-skill-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryUniqueSin` | 1,500 | The max amount of mastery point for Unique Skills of Sins. |
| `Mastery.masteryIntrinsic` | 100 | The max amount of mastery point for Intrinsic Skills. |
| `Mastery.masteryExtra` | 500 | The max amount of mastery point for Extra Skills. |
| `Mastery.masteryUnique` | 1,000 | The max amount of mastery point for Unique Skills. |
| `Mastery.masteryUniqueSin` | 1,500 | The max amount of mastery point for Unique Skills of Sins. |
| `Mastery.masteryUltimate` | 10,000 | The max amount of mastery point for Ultimate Skills. |

## Tags

`tensura:skills/pride`, `tensura:skills/sin_skills`, `tensura:skills/unique_skills`
