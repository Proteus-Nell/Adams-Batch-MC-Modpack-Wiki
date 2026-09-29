# Cook

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Cook](../../../assets/icons/tensura/skill/cook.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:cook` |
| **Modes** | 1 |
| **Acquisition cost (MP)** | 60,000 |
| **Cooldowns (s)** | 1 |
| **Activation** | Toggle, Press |

</div>

> Bend reality to ensure your enemies meet their demise by ignoring their dodge and barriers.

## Modes

| # | Mode |
|---|---|
| 1 | Chaotic Fate |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Triggers when you damage a target
- Triggers on melee contact

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| degrade | 1 | add |
| critical | 100 | add |
| dodgeNegate | 100 | add |
| learning | 4 | add |
| mastery | 4 | add |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.
- Listed in the `allowedSkills` config option (config/nightmare/ability/skill/nightmare_unique.toml): List of skills Handler is allowed to upgrade. (is every skill it can by default)

## Related

- **Referenced by:** [Alteration](../../../tr-nightmares/abilities/extra-skills/alteration.md), [｢ Sariel, Lord of Hope ｣](../../../tr-nightmares/abilities/ultimate-skills/sariel.md), [｢ Susanoo, Lord of Tyranny ｣](../../../tr-nightmares/abilities/ultimate-skills/susanoo.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Cook.mpAcquirement` | 60,000 | Magicule Acquirement Cost. |
| `Cook.critChance` | 100 | Critical Attack Chance when toggled. |
| `Cook.dodgeNegation` | 100 | Dodge Negation Chance when toggled. |
| `Cook.learningPoint` | 4 | The bonus number of learning point to gain when toggled. |
| `Cook.masteryPoint` | 4 | The bonus number of mastery point to gain when toggled. |
| `Cook.barrierEP` | 2 | The multiplier of the user's EP that the target to have above to ignore Barrier shattering when attacked by the user. |
| `Cook.hpReducedMultiplier` | 1 | The multiplier of the user's damage dealt that the target's Max Health get reduced by. |

## Tags

`tensura:skills/unique_skills`
