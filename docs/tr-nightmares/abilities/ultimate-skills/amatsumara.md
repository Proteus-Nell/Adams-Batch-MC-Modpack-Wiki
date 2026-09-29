# ｢ Amatsumara, Lord of Crafts ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:amatsumara` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 600,000 |
| **Max mastery** | 5,000 |
| **Activation** | Press |

</div>

> Ultimate craftsmanship. Requires mastered Godly Craftsman, Law Manipulation, and 100 unique item types engraved through Godly Craftsman. In-slot Precision Miner grants Luck V and triple ore drops. Kiln, Refine, Smithing, and Craftsmen modes open portable workshops with 500,000 EP gear bonuses.

## Modes

| # | Mode |
|---|---|
| 1 | Kiln |
| 2 | Refine |
| 3 | Smithing |
| 4 | Craftsmen |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Does something when first learned

## Obtaining

- Acquisition checks: [Godly Craftsman](../../../tensura-reincarnated/abilities/unique-skills/godly-craftsman.md), [｢ Amatsumara, Lord of Crafts ｣](amatsumara.md)
- In-game message: *The forge sings with a thousand perfected forms. Godly Craftsman has evolved into Amatsumara, Lord of Crafts.*

## Related

- **Related skills:** [Godly Craftsman](../../../tensura-reincarnated/abilities/unique-skills/godly-craftsman.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Amatsumara.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Amatsumara.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Amatsumara.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Amatsumara.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Amatsumara.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Amatsumara.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Amatsumara.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Amatsumara.mpAcquirement` | 600,000 | Magicule acquirement cost. |
| `Amatsumara.uniqueEngravedItemRequirement` | 100 | Unique item types engraved through Godly Craftsman required for evolution. |
| `Amatsumara.enableUltimateEvolution` | true | Whether Amatsumara evolution is allowed. |
| `Amatsumara.maxBonusLevel` | 2 | Bonus enchantment levels for Amatsumara craftsmen engrave tab. |
| `Amatsumara.enchantmentBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:enervation", "tensura:lethargy", "tensura:sealing", "tensura:stagnation", "tensura:ruination", "tensura:vitality", "tensura:vigor", "tensura:transcendence", "tensura:growth", "tensura:restoration" | Enchantment blacklist for Amatsumara craftsmen. |
| `Amatsumara.maxBonusBlacklist` | [] (empty) | Enchantments that cannot exceed vanilla max level. |
| `Amatsumara.curseChance` | 0.03 | Curse chance per engraving. |
| `Amatsumara.craftEpBonus` | 500,000 | Default EP applied to gear crafted through Amatsumara modes. |
| `Amatsumara.skillEngraveBlacklist` | "tensura:creator", "trnightmare:astral_light", "trnightmare:akashic_records", "trnightmare:asmodues", "trnightmare:beelzebuth", "trnightmare:leviathan", "trnightmare:lucifer", "trnightmare:mammon", "trnightmare:belphegor", "trnightmare:azazel", "trnightmare:gabriel", "trnightmare:michael", "trnightmare:raguel", "trnightmare:sariel", "trnightmare:haniel", "trnightmare:astarte", "trnightmare:abbadon", "trnightmare:astaroth", "trnightmare:cthugha", "trnightmare:cthulhu" ... (26 total) | Skills that cannot be engraved through Amatsumara skill engrave. |

Set in [`config/tensura/ability/skill/unique_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `GodlyCraftsman.mpAcquirement` | 60,000 | Magicule Acquirement Cost. |
| `GodlyCraftsman.maxBonusLevel` | 2 | How many levels that GodlyCraftsman can go above the maximum level of an enchantment. |
| `GodlyCraftsman.enchantmentBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:enervation", "tensura:lethargy", "tensura:sealing", "tensura:stagnation", "tensura:ruination", "tensura:vitality", "tensura:vigor", "tensura:transcendence", "tensura:growth", "tensura:restoration" | Lists of enchantments that Godly Craftsman cannot learn or add. |
| `GodlyCraftsman.maxBonusBlacklist` | "tensura:dead_end_rainbow", "tensura:holy_coat", "tensura:magic_interference", "tensura:tsukumogami", "tensura:barrier_piercing", "tensura:breathing_support", "tensura:crushing", "tensura:energy_steal", "tensura:elemental_boost", "tensura:elemental_resistance", "tensura:energy_protection", "tensura:holy_weapon", "tensura:intangibility", "tensura:magic_weapon", "tensura:magicule_absorption", "tensura:magic_capacity", "tensura:magic_protection", "tensura:severance", "tensura:slotting", "tensura:soul_eater" ... (34 total) | Lists of enchantments that Godly Craftsman cannot learn or add above the enchantment's maximum level. |
| `GodlyCraftsman.curseChance` | 0.03 | The percentage chance to obtain a Curse Engraving per Engraving on the item. |
