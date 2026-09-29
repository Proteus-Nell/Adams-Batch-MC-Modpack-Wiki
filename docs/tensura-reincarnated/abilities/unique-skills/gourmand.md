# Gourmand

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Gourmand](../../../assets/icons/tensura/skill/gourmand.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:gourmand` |
| **Acquisition cost (MP)** | 70,000 |
| **Activation** | Toggle, Press |

</div>

> Feast on the energy of your opponents. Steal magicule with your attacks and become more powerful when killing others.

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Triggers on melee contact

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| aura | bonus aura | add |
| magicule | bonus magicule | add |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Effects:** [Fear](../../effects/fear.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Gourmand.mpAcquirement` | 70,000 | Magicule Acquirement Cost. |
| `Gourmand.auraPercentage` | 3 | The bonus Aura percentage the user gains when toggled on. |
| `Gourmand.auraPercentageMastered` | 7.5 | The bonus Aura percentage the user gains when toggled on with Mastery. |
| `Gourmand.magiculePercentage` | 3 | The bonus Magicule percentage the user gains when toggled on. |
| `Gourmand.magiculePercentageMastered` | 7.5 | The bonus Magicule percentage the user gains when toggled on with Mastery. |
| `Gourmand.epStealChance` | 50 | The chance to steal MP from targets when the user attack them with Gourmand. |
| `Gourmand.epStealChanceMastered` | 75 | The chance to steal MP from targets when the user attack them with Gourmand when mastered. |
| `Gourmand.epStealPercentage` | 0.01 | The multiplier of MP to steal from targets when the user attack them with Gourmand. |
| `Gourmand.fearHeartEat` | 5 | The optional level of Fear that the target needs to have to be affected by Heart Eat. |
| `Gourmand.epHeartEat` | 0.1 | The optional multiplier of the user's EP that the target needs to have below to be affected by Heart Eat. |
| `Gourmand.heartEatEpMultiplier` | 1 | The multiplier of the target's EP that the user will recover with once activated Heart Eat (Split bewteen MP and AP). |

## Tags

`tensura:skills/unique_skills`
