# Godly Craftsman

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Godly Craftsman](../../../assets/icons/tensura/skill/godly_craftsman.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:godly_craftsman` |
| **Acquisition cost (MP)** | 60,000 |
| **Activation** | Press |

</div>

> Utilize your years of experience to create masterpieces with ease and engrave your weapons for terrifying efficiency.

## How it works

- Activated by pressing the skill key

## Obtaining

- Acquisition checks: [Researcher](researcher.md)

## Related

- **Related skills:** [Researcher](researcher.md)
- **Referenced by:** [Researcher](researcher.md), [｢ Amatsumara, Lord of Crafts ｣](../../../tr-nightmares/abilities/ultimate-skills/amatsumara.md), [Raphael, Lord of Wisdom](../../../elite-tensura/abilities/ultimate-skills/raphealskill.md), [Hephaestus, Lord of Creation](../../../elite-tensura/abilities/ultimate-skills/hephaestus.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `GodlyCraftsman.mpAcquirement` | 60,000 | Magicule Acquirement Cost. |
| `GodlyCraftsman.maxBonusLevel` | 2 | How many levels that GodlyCraftsman can go above the maximum level of an enchantment. |
| `GodlyCraftsman.enchantmentBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:enervation", "tensura:lethargy", "tensura:sealing", "tensura:stagnation", "tensura:ruination", "tensura:vitality", "tensura:vigor", "tensura:transcendence", "tensura:growth", "tensura:restoration" | Lists of enchantments that Godly Craftsman cannot learn or add. |
| `GodlyCraftsman.maxBonusBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:barrier_piercing", "tensura:breathing_support", "tensura:crushing", "tensura:energy_steal", "tensura:elemental_boost", "tensura:elemental_resistance", "tensura:energy_protection", "tensura:holy_weapon", "tensura:intangibility", "tensura:magic_weapon", "tensura:magicule_absorption", "tensura:magic_capacity", "tensura:magic_protection", "tensura:severance", "tensura:slotting", "tensura:soul_eater" ... (34 total) | Lists of enchantments that Godly Craftsman cannot learn or add above the enchantment's maximum level. |
| `GodlyCraftsman.curseChance` | 0.03 | The percentage chance to obtain a Curse Engraving per Engraving on the item. |

## Tags

`tensura:skills/unique_skills`
