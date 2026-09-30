# Severer

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Severer](../../../assets/icons/tensura/skill/severer.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:severer` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 30,000 |
| **Cooldowns (s)** | 1 mastered, 3 otherwise |
| **Activation** | Press |

</div>

> Slice through reality and manifest spatial blades which cut through armor and unleash devastating blade storms.

## Modes

| # | Mode |
|---|---|
| 1 | Dummy Sword |
| 2 | Blade Storm |
| 3 | Severance |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Blade Storm | 2,000 |  |
| Severance | 200 |  |
| other modes | 100 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Innate to mobs: [Kyoya Tachibana](../../mobs/kyoya-tachibana.md)
- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Effects:** [Severance Blade](../../effects/severance-blade.md)
- **Items:** [Spatial Blade](../../items/weapons/spatial-blade.md)
- **Summons / entities:** [Severance](../../enchantments/severance.md), Severer Blade
- **Referenced by:** [Pride Manas](../../../tr-nightmares/abilities/ultimate-skills/pride-manas.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Severer.mpAcquirement` | 30,000 | Magicule Acquirement Cost. |
| `Severer.magiculeCostDummy` | 100 | Magicule Cost to activate Dummy Sword. |
| `Severer.magiculeCostStorm` | 2,000 | Magicule Cost to activate Blade Storm. |
| `Severer.magiculeCostSeverance` | 200 | Magicule Cost to activate Severance. |
| `Severer.engravingLevel` | 5 | The level of the Severance engraving of the Dummy Sword. |
| `Severer.engravingLevelMastered` | 10 | The level of the Severance engraving of the Dummy Sword when mastered. |
| `Severer.stormNumber` | 5 | The number of blades of the Blade Storm. |
| `Severer.stormNumberMastered` | 10 | The number of blades of the Blade Storm when mastered. |
| `Severer.stormCooldown` | 3 | The cooldown in second of the Blade Storm. |
| `Severer.stormCooldownMastered` | 1 | The cooldown in second of the Blade Storm when mastered. |
| `Severer.severanceLevel` | 1 | The level of the Severance effect when activating the Severance mode. |
| `Severer.severanceLevelMastered` | 2 | The level of the Severance effect when activating the Severance mode with mastery. |
| `Severer.severanceDuration` | 2,400 | The duration in tick of the Severance effect when activating the Severance mode. |

## Tags

`tensura:skills/unique_skills`
