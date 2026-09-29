# Hephaestus, Lord of Creation

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Hephaestus, Lord of Creation](../../../assets/icons/elitetensura/skill/hephaestus.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `elitetensura:hephaestus` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 0 |
| **Max mastery** | 10,000 |
| **Cooldowns (s)** | 120, 90, 600, 4, 30 |
| **Activation** | Press |

</div>

> The forge answers its lord. Repair and reforge what exists, engrave it, conjure arms from nothing, sense the ore beneath stone, and turn a smith's mastery into a weapon.

## Modes

| # | Mode |
|---|---|
| 1 | Reforge |
| 2 | Engrave |
| 3 | Conjure Arms |
| 4 | Hammer of Creation |
| 5 | Chains of Hephaestus |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Engrave | 6,000 |  |
| Conjure Arms | 25,000 |  |
| Hammer of Creation | 4,000 |  |
| Chains of Hephaestus | 10,000 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Acquisition checks: [Godly Craftsman](../../../tensura-reincarnated/abilities/unique-skills/godly-craftsman.md), [Creator](../../../tensura-reincarnated/abilities/unique-skills/creator.md)

## Related

- **Related skills:** [Godly Craftsman](../../../tensura-reincarnated/abilities/unique-skills/godly-craftsman.md), [Creator](../../../tensura-reincarnated/abilities/unique-skills/creator.md)
- **Effects:** [Bound](../../effects/bound.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UltimateSkillConfig.toml`](../../configs/config-tensura-elitetensura-ultimateskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `HephaestusSkill.IsEnabled` | true | Is this Skill Enabled? |
| `HephaestusSkill.reforgeCost` | 8,000 | Magicule cost to reforge, flat portion. |
| `HephaestusSkill.reforgeCostPerDamage` | 4 | Extra magicule per point of durability missing. |
| `HephaestusSkill.reforgeCooldown` | 120 | Reforge cooldown in SECONDS. |
| `HephaestusSkill.reforgeScoreMin` | 35 | Lowest score a reforge can roll (0-100). Reforge does NOT inherit the item's old score. |
| `HephaestusSkill.reforgeScoreMax` | 95 | Highest score a reforge can roll (0-100). |
| `HephaestusSkill.engraveCostPerLevel` | 6,000 | Magicule cost per level of the chosen engraving. |
| `HephaestusSkill.engraveCooldown` | 90 | Engrave cooldown in SECONDS. |
| `HephaestusSkill.conjureRecipeId` | "forged_high_magisteel_sword" | Forge recipe id used as the conjured weapon template. |
| `HephaestusSkill.conjureCost` | 25,000 | Magicule cost to conjure. |
| `HephaestusSkill.conjureCooldown` | 600 | Conjure cooldown in SECONDS. |
| `HephaestusSkill.conjureDurationTicks` | 6,000 | How long a conjured weapon lasts, in ticks (20 ticks = 1 second). |
| `HephaestusSkill.conjureMasteryPerRank` | 8 | Forge mastery levels required per quality rank above POOR for the conjured weapon. |
| `HephaestusSkill.hammerBaseDamage` | 12 | Base damage of the hammer strike. |
| `HephaestusSkill.hammerDamagePerMastery` | 0.8 | Bonus damage per forge mastery level (mastery caps at 50). |
| `HephaestusSkill.hammerDamagePerQualityRank` | 6 | Bonus damage per quality rank of the best item ever crafted (0-6). |
| `HephaestusSkill.hammerRange` | 5 | Hammer reach in blocks. |
| `HephaestusSkill.hammerAngle` | 60 | Hammer cone half-angle in degrees. |
| `HephaestusSkill.hammerCost` | 4,000 | Magicule cost per hammer swing. |
| `HephaestusSkill.hammerCooldown` | 4 | Hammer cooldown in SECONDS. |
| `HephaestusSkill.chainsRange` | 12 | Chains range in blocks. |
| `HephaestusSkill.chainsDurationTicks` | 120 | Bound effect duration in ticks. |
| `HephaestusSkill.chainsAmplifier` | 1 | Bound effect amplifier (0 = level I). |
| `HephaestusSkill.chainsCost` | 10,000 | Magicule cost to cast Chains. |
| `HephaestusSkill.chainsCooldown` | 30 | Chains cooldown in SECONDS. |
| `HephaestusSkill.oreSenseRadius` | 24 | Ore Sense scan radius in blocks. |
| `HephaestusSkill.oreSenseScanIntervalTicks` | 40 | Ticks between Ore Sense rescans. Lower = more responsive, more CPU. |
| `HephaestusSkill.oreSenseDrainPerTick` | 150 | Magicule drained per skill tick callback while Ore Sense is toggled on. |
| `HephaestusSkill.divineHandEnabled` | true | Enable the once-per-day free minigame stage. |
| `HephaestusSkill.nationBoonQualityFlat` | 3 | Flat forge quality points granted to every member of the holder's nation. |
| `HephaestusSkill.friendlyFire` | false | If true, Hammer of Creation and Chains of Hephaestus also hit players in the user's own nation or hunt party. |

Set in [`config/tensura/ability/skill_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryUltimate` | 10,000 | The max amount of mastery point for Ultimate Skills. |
| `Mastery.masteryIntrinsic` | 100 | The max amount of mastery point for Intrinsic Skills. |
| `Mastery.masteryExtra` | 500 | The max amount of mastery point for Extra Skills. |
| `Mastery.masteryUnique` | 1,000 | The max amount of mastery point for Unique Skills. |
| `Mastery.masteryUniqueSin` | 1,500 | The max amount of mastery point for Unique Skills of Sins. |
| `Mastery.masteryUltimate` | 10,000 | The max amount of mastery point for Ultimate Skills. |

## Tags

`tensura:skills/no_plundering`, `tensura:skills/ultimate_skills`
