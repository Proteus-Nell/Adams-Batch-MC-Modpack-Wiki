# Raphael, Lord of Wisdom

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Raphael, Lord of Wisdom](../../../assets/icons/elitetensura/skill/raphealskill.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `elitetensura:raphealskill` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 0 |
| **Cooldowns (s)** | 10, 5 |
| **Activation** | Toggle, Press |

</div>

> The Voice of the World given form — a battlefield-computation entity. Analysis unlocks everything: prediction, barriers, reverse-engineering, and Raphael's own counsel.

## Modes

| # | Mode |
|---|---|
| 1 | Analyze |
| 2 | Reverse-Engineer |
| 3 | Prediction |
| 4 | Multilayer Barrier |
| 5 | Sage's Workshop |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Analyze | 500 |  |
| Reverse-Engineer | 5,000 |  |
| Prediction | 2,000 |  |
| Multilayer Barrier | 500 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| var3 | 16 | add |
| var4 | 16 | add |

## Obtaining

- Acquisition checks: [Great Sage](../../../tensura-reincarnated/abilities/unique-skills/great-sage.md), [Godly Craftsman](../../../tensura-reincarnated/abilities/unique-skills/godly-craftsman.md)

## Related

- **Related skills:** [Great Sage](../../../tensura-reincarnated/abilities/unique-skills/great-sage.md), [Godly Craftsman](../../../tensura-reincarnated/abilities/unique-skills/godly-craftsman.md)
- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UltimateSkillConfig.toml`](../../configs/config-tensura-elitetensura-ultimateskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `RaphealSkill.IsEnabled` | true | Is this Skill Enabled? |
| `RaphealSkill.chantSpeed` | 4 | The chant speed multiplier when toggled. |
| `RaphealSkill.learningPoint` | 16 | The bonus number of learning point to gain when toggled. |
| `RaphealSkill.masteryPoint` | 16 | The bonus number of mastery point to gain when toggled. |
| `RaphealSkill.analysisLevel` | 18 | The Analysis Level when activated. |
| `RaphealSkill.analysisLevelMastered` | 32 | The Analysis Level when activated with Mastery. |
| `RaphealSkill.analysisRadius` | 25 | The Analysis Radius when activated. |
| `RaphealSkill.analysisRadiusMastered` | 64 | The Analysis Radius when activated with Mastery. |
| `RaphealSkill.copyRange` | 20 | The range in block of Analyze / Reverse-Engineer targeting on mobs. |
| `RaphealSkill.copyRangeMagic` | 32 | The range in block of Reverse-Engineer on magic projectiles. |
| `RaphealSkill.copyCooldownSuccess` | 10 | The cooldown in second when the user successfully copied a skill from targets. |
| `RaphealSkill.copyCooldownFail` | 5 | The cooldown in second when the user failed to copy a skill from targets. |
| `RaphealSkill.analysisDurationSeconds` | 300 | How long (seconds) a target stays analyzed after Analyze marks it. |
| `RaphealSkill.maxAnalyzedTargets` | 16 | Maximum number of simultaneously analyzed targets. |
| `RaphealSkill.analyzeMagiculeCost` | 500 | Magicule cost of Analyze (mode 0). |
| `RaphealSkill.reverseEngineerChannelSeconds` | 5 | Observation channel length (seconds) for Reverse-Engineer. |
| `RaphealSkill.reverseEngineerMagiculeCost` | 5,000 | Magicule cost to start a Reverse-Engineer channel (mode 1). |
| `RaphealSkill.predictionNegateCooldownSeconds` | 30 | Seconds between Prediction hit-negations against analyzed attackers. |
| `RaphealSkill.predictionNegateMagiculeCost` | 2,000 | Magicule cost per Prediction hit-negation. |
| `RaphealSkill.predictionCritMultiplier` | 1.5 | Damage multiplier of Prediction's computed strike against analyzed targets. |
| `RaphealSkill.predictionCritCooldownSeconds` | 10 | Seconds between Prediction computed strikes. |
| `RaphealSkill.barrierDamageReduction` | 0.25 | Multilayer Barrier damage reduction (0-1) against unanalyzed attackers. |
| `RaphealSkill.barrierDamageReductionAnalyzed` | 0.5 | Multilayer Barrier damage reduction (0-1) against analyzed attackers. |
| `RaphealSkill.barrierUpkeepMagiculePerSecond` | 100 | Magicule upkeep per second while Multilayer Barrier is active (charged as 5× this once per 5 s skill tick). |
| `RaphealSkill.counselEnabled` | true | Enable Independent Counsel proposals. |
| `RaphealSkill.counselProposalExpirySeconds` | 10 | Seconds a Counsel proposal stays pending before it expires. |
| `RaphealSkill.counselTriggerCooldownSeconds` | 60 | Per-trigger cooldown (seconds) between Counsel proposals. |
| `RaphealSkill.counselLowHealthPercent` | 0.35 | Health fraction (0-1) below which Counsel proposes the barrier. |
| `RaphealSkill.emergencyDefenseEnabled` | true | Enable autonomous Emergency Defense against lethal hits. |
| `RaphealSkill.emergencyDefenseCooldownSeconds` | 300 | Cooldown (seconds) between Emergency Defense activations. |
| `RaphealSkill.emergencyDefenseMagiculeCost` | 20,000 | Magicule cost of an Emergency Defense activation. |
| `RaphealSkill.arsMagnaRequiresAnalysis` | true | If true, Ars Magna benefits (instant cast, chant annulment, half MP) require a computed situation (live analysis / Prediction / Barrier). If false, plain toggle is enough. |
| `RaphealSkill.maxBonusLevel` | 4 | How many levels that Rapheal can go above the maximum level of an enchantment. |
| `RaphealSkill.enchantmentBlacklist` | "tensura:dead_end_rainbow", "tensura:tsukumogami" | Lists of enchantments that Godly Craftsman cannot learn or add. |
| `RaphealSkill.maxBonusBlacklist` | - | Lists of enchantments that Godly Craftsman cannot learn or add above the enchantment's maximum level. |
| `RaphealSkill.curseChance` | - | The percentage chance to obtain a Curse Engraving per Engraving on the item. |
| `RaphealSkill.storageSlots` | 54 | Spatial storage slots (Tensura: Great Sage 20, Researcher 45, Predator 63). Shrinking on a live world silently drops items in the removed slots. |
| `RaphealSkill.storageStackSize` | 256 | Max stack size per spatial storage slot (Tensura: 128). |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## In-game messages

<details markdown><summary>Show 31 messages</summary>

- «Raphael»
- Notice. Vital signs critical. Proposal: deploy Multilayer Barrier.
- Notice. Analyzed hostile within engagement range. Proposal: engage Prediction.
- Press the skill key to approve.
- Understood. Executing.
- No valid subject in view.
- Analysis complete: %1$s
- Vitals: %1$s / %2$s HP — Existence Points: %3$s
- Magicule: %1$s — Aura: %2$s
- Known abilities (%1$s):
- Subject %1$s registered. Analysis retained for %2$s seconds.
- Appraisal deactivated.
- Observing %1$s. Reconstruction in %2$s seconds.
- Reconstruction complete. Acquired: %1$s.
- Observation interrupted. Insufficient data.
- Observation cancelled.
- Subject %1$s not yet analyzed. Analysis required before reconstruction.
- Prediction engaged. Computing hostile trajectories.
- Prediction suspended.
- Attack trajectory computed. Negated.
- Opening identified. Strike optimized.
- Multilayer Barrier deployed. Adjusting to threat analysis.
- Multilayer Barrier released.
- Report. Lethal damage predicted — emergency defense executed autonomously.
- Workshop facility: %1$s
- Spatial Storage
- Research &amp; Enchanting
- Refining
- Repeat Crafting
- Degenerate Crafting
- Synthesis &amp; Separation

</details>

## Tags

`tensura:skills/no_plundering`, `tensura:skills/ultimate_skills`
