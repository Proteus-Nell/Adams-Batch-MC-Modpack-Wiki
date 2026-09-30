# ｢ Surya, King of Brillance ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:surya` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 1,500,000 |
| **Max mastery** | 35,000 |
| **Cooldowns (s)** | 1 |
| **Activation** | Press, Hold |

</div>

> The absolute authority of Holy magic, Spiritron particles, Separation of Laws, and Dictation of Interference.

## Modes

| # | Mode |
|---|---|
| 1 | Disintegration |
| 2 | Melt Cut |
| 3 | Spiritron Coat |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage
- Triggers when an effect is applied to you
- Does something when first learned
- Does something when mastered

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -1 | multiply total |

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Acquisition checks: [｢ Metatron, Lord of Purity ｣](metatron.md), [｢ Surya, King of Brillance ｣](surya.md)
- In-game message: *Under extreme circumstances, order must be maintained, Purity and Chastity must remain untainted by the Domination of a Moral Justice. Metatron, Lord of Purity has evolved into [ Ultimate Skill: Surya, King of Brilliance ].*

## Related

- **Related skills:** [｢ Metatron, Lord of Purity ｣](metatron.md)
- **Effects:** [Magic Interference](../../../tensura-reincarnated/effects/magic-interference.md), [Anti-Magic](../../../tensura-reincarnated/effects/anti-magic.md), [Movement Interference](../../../tensura-reincarnated/effects/movement-interference.md)
- **Summons / entities:** Disintegration

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Surya.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Surya.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Surya.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Surya.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Surya.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Surya.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Surya.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Surya.mpAcquirement` | 1,500,000 | Magicule Acquirement Cost. |
| `Surya.spiritronReqPercent` | 60 | Percentage of magicules required to generate Spiritron Points. |
| `Surya.reducedMagiculeCost` | 65 | Percentage of magicules paid if reduced. |
| `Surya.spReduceRequirement` | 150 | Spiritron Points required to reduce magicule costs. |
| `Surya.spGenerationDefault` | 10 | Number of Spiritrons generated (Unmastered). |
| `Surya.spGenerationMastered` | 15 | Number of Spiritrons generated (Mastered). |
| `Surya.spPurifyRequirement` | 60 | Spiritron Points required to purify physical attacks. |
| `Surya.spPurifyRequirementMagic` | 150 | Spiritron Points required to purify magic attacks. |
| `Surya.purifyDamage` | 50 | Amount of Holy Damage dealt by physical attacks (1.5x on mastery). |
| `Surya.purifyDamageMagic` | 80 | Amount of Holy Damage dealt by spells attacks. |
| `Surya.miracleBuff` | 110 | Amount Holy damage is buffed by Holy Miracle. |
| `Surya.miracleBuffMastered` | 140 | Amount Holy damage is buffed by Holy Miracle when mastered. |
| `Surya.spDisintegrationRequirement` | 60 | Spiritron Points required to cast Disintegration. |
| `Surya.mpDisintegrationRequirement` | 25,000 | Magicules required to cast Disintegration. |
| `Surya.disintegrationDamage` | 250 | Amount of damage dealt by disintegration. |
| `Surya.disintegrationDamageMastered` | 300 | Amount of damage dealt by disintegration Mastered. |
| `Surya.meltDamage` | 90 | Amount of Holy damage dealt by Melt Cut. |
| `Surya.disCoatDamage` | 50 | True damage dealt by Disintegration Coating. |
| `Surya.meltCooldown` | 1 | Cooldown of Melt Cut. |
| `Surya.disCoatReq` | 400 | Disintegration Coating Spiritron Requirement. |
| `Surya.spMax` | 500 | Max Spiritron points on Acquirement of Surya. |
| `Surya.spMaxMastered` | 800 | Max Spiritron points on mastery of Surya. |
| `Surya.suryaSpells` | 5 | Holy Spells required for Surya. |
| `Surya.suryaRaids` | 15 | Raids required for Surya. |
| `Surya.suryaSpiritrons` | 10,000 | Used spiritrons required for Surya. |
| `Surya.enableUltimateEvolution` | true | Whether Surya evolution is allowed. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

## Tags

`tensura:skills/ultimate_skills`
