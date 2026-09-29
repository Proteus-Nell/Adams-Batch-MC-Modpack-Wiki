# ｢ Metatron, Lord of Purity ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:metatron` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 950,000 |
| **Max mastery** | 25,000 |
| **Cooldowns (s)** | 1 |
| **Activation** | Press, Hold |

</div>

> The Domination of Pure Energy, Separation of Concepts, and the Prevention of Interference.

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

- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.
- Acquisition checks: [Saint](../unique-skills/saint.md), [｢ Metatron, Lord of Purity ｣](metatron.md)
- In-game message: *In the heat of battle, when prayers must be answered, evil must be cleaned, order must be maintained through the separation of powers, you find yourself glowing in Holy Light. [ Ultimate Skill: Metatron, Lord of Purity ] has been obtained.*

## Related

- **Related skills:** [Saint](../unique-skills/saint.md)
- **Effects:** [Holy Damage](../../../tensura-reincarnated/effects/holy-damage.md), [Magic Interference](../../../tensura-reincarnated/effects/magic-interference.md), [Anti-Magic](../../../tensura-reincarnated/effects/anti-magic.md), [Movement Interference](../../../tensura-reincarnated/effects/movement-interference.md)
- **Summons / entities:** Disintegration
- **Referenced by:** [｢ Surya, King of Brillance ｣](surya.md), [Nun Manas](nun-manas.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Metatron.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Metatron.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Metatron.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Metatron.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Metatron.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Metatron.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Metatron.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Metatron.mpAcquirement` | 950,000 | Magicule Acquirement Cost. |
| `Metatron.spiritronReqPercent` | 80 | Percentage of magicules required to generate Spiritron Points. |
| `Metatron.reducedMagiculeCost` | 80 | Percentage of magicules paid if reduced. |
| `Metatron.spReduceRequirement` | 150 | Spiritron Points required to reduce magicule costs. |
| `Metatron.spGenerationDefault` | 5 | Number of Spiritrons generated (Unmastered). |
| `Metatron.spGenerationMastered` | 10 | Number of Spiritrons generated (Mastered). |
| `Metatron.spPurifyRequirement` | 80 | Spiritron Points required to purify physical attacks. |
| `Metatron.spPurifyRequirementMagic` | 200 | Spiritron Points required to purify magic attacks. |
| `Metatron.purifyDamage` | 40 | Amount of Holy Damage dealt by physical attacks (1.5x on mastery). |
| `Metatron.purifyDamageMagic` | 40 | Amount of Holy Damage dealt by spells attacks. |
| `Metatron.miracleBuff` | 90 | Amount Holy damage is buffed by Holy Miracle. |
| `Metatron.miracleBuffMastered` | 90 | Amount Holy damage is buffed by Holy Miracle when mastered. |
| `Metatron.miracleDebuff` | 25 | Amount of damage dealt to user by Holy Miracle. |
| `Metatron.miracleDebuffMastered` | 15 | Amount of damage dealt to user by Holy Miracle when mastered. |
| `Metatron.spDisintegrationRequirement` | 75 | Spiritron Points required to cast Disintegration. |
| `Metatron.mpDisintegrationRequirement` | 25,000 | Magicules required to cast Disintegration. |
| `Metatron.disintegrationDamage` | 150 | Amount of damage dealt by disintegration. |
| `Metatron.disintegrationDamageMastered` | 200 | Amount of damage dealt by disintegration Mastered. |
| `Metatron.disintegrationArea` | 70 | Amount of damage dealt nearby disintegration. |
| `Metatron.disintegrationAreaMastered` | 50 | Amount of damage dealt nearby disintegration. |
| `Metatron.meltDamage` | 90 | Amount of Holy damage dealt by Melt Cut. |
| `Metatron.meltCooldown` | 1 | Cooldown of Melt Cut. |
| `Metatron.spMax` | 200 | Max Spiritron points on Acquirement of Metatron. |
| `Metatron.spMaxMastered` | 500 | Max Spiritron points on mastery of Metatron. |
| `Metatron.metaSpells` | 5 | Holy Spells required for Metatron. |
| `Metatron.metaRaids` | 7 | Raids required for Metatron. |
| `Metatron.enableUltimateEvolution` | true | Whether Metatron evolution is allowed. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

## Tags

`tensura:skills/nun`, `tensura:skills/ultimate_skills`
