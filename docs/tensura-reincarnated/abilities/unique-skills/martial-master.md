# Martial Master

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Martial Master](../../../assets/icons/tensura/skill/martial_master.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:martial_master` |
| **Acquisition cost (MP)** | 40,000 |
| **Activation** | Toggle, Press |

</div>

> Empower your physical attacks, accelerate your thought process to react and dodge better while beating your enemies to submission.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 100 |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Triggers when you damage a target
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| dodge | 0.25 | add |
| invulnerability | 2 | add |
| melee | 25 | add |
| projectile | 100 | add |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Related skills:** [Heavenly Eye](../extra-skills/heavenly-eye.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `MartialMaster.mpAcquirement` | 40,000 | Magicule Acquirement Cost. |
| `MartialMaster.auraCost` | 100 | Aura Cost to activate Ultra Acceleration. |
| `MartialMaster.damageMultiplier` | 1.5 | The melee/battlewill damage multiplier when using Secret. |
| `MartialMaster.ultraDistance` | 15 | The Ultra Acceleration distance when activated. |
| `MartialMaster.ultraDistanceMastered` | 20 | The Ultra Acceleration distance when activated with mastery. |
| `MartialMaster.ultraDamage` | 15 | The bonus attack when using Ultra Acceleration on a target. |
| `MartialMaster.ultraDamageMastered` | 75 | The bonus attack when using Ultra Acceleration on a target when mastered. |
| `MartialMaster.chantSpeed` | 2 | The chant speed multiplier when toggled. |
| `MartialMaster.meleeDodge` | 25 | Melee Dodge Chance when toggled. |
| `MartialMaster.projectileDodge` | 100 | Projectile Dodge Chance when toggled. |
| `MartialMaster.dodgeStrength` | 0.25 | The bonus dodge strength when toggled. |
| `MartialMaster.dodgeInvulnerability` | 2 | The bonus dodge invulnerability when toggled. |
| `MartialMaster.learningPoint` | 4 | The bonus number of bonus art-learning point to gain when toggled. |
| `MartialMaster.masteryPoint` | 4 | The bonus number of bonus art-mastery point to gain when toggled. |

## Tags

`tensura:skills/unique_skills`
