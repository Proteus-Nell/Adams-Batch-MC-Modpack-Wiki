# Researcher

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Researcher](../../../assets/icons/tensura/skill/researcher.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:researcher` |
| **Acquisition cost (MP)** | 30,000 |
| **Activation** | Press |

</div>

> Study ancient magic tomes, reverse engineer them, and create wonders beyond imagination.

## How it works

- Activated by pressing the skill key
- Does something when mastered

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Related skills:** [Godly Craftsman](godly-craftsman.md)
- **Referenced by:** [Godly Craftsman](godly-craftsman.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Researcher.mpAcquirement` | 30,000 | Magicule Acquirement Cost. |
| `Researcher.maxBonusLevel` | 1 | How many levels that Researcher can go above the maximum level of an enchantment. |
| `Researcher.enchantmentBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:barrier_piercing", "tensura:breathing_support", "tensura:crushing", "tensura:energy_steal", "tensura:elemental_boost", "tensura:elemental_resistance", "tensura:energy_protection", "tensura:holy_weapon", "tensura:intangibility", "tensura:magic_weapon", "tensura:magicule_absorption", "tensura:magic_capacity", "tensura:magic_protection", "tensura:severance", "tensura:slotting", "tensura:soul_eater" ... (34 total) | Lists of enchantments that Researcher cannot learn or add. |
| `Researcher.maxBonusBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:barrier_piercing", "tensura:breathing_support", "tensura:crushing", "tensura:energy_steal", "tensura:elemental_boost", "tensura:elemental_resistance", "tensura:energy_protection", "tensura:holy_weapon", "tensura:intangibility", "tensura:magic_weapon", "tensura:magicule_absorption", "tensura:magic_capacity", "tensura:magic_protection", "tensura:severance", "tensura:slotting", "tensura:soul_eater" ... (34 total) | Lists of enchantments that Researcher cannot learn or add above the enchantment's maximum level. |
| `Researcher.curseChance` | 0.03 | The percentage chance to obtain a Curse Engraving per Engraving on the item. |

## Tags

`tensura:skills/unique_skills`
