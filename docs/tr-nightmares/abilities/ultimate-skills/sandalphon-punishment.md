# ｢ Sandalphon, Lord of Punishment ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:sandalphon_punishment` |
| **Modes** | 7 |
| **Acquisition cost (MP)** | 500,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> Ascended Sandalphon — adds existence concealment and the Sure Hit of Assassination.

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Mode 2 |
| 3 | Mode 3 |
| 4 | Mode 4 |
| 5 | Mode 5 |
| 6 | Existence Concealment |
| 7 | Sure Hit |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target

## Obtaining

- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.
- In-game message: *You have awakened Sandalphon, Lord of Judgment.*

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Sandalphon.learnPointsSureHit` | 500 | Learning points required for Sure Hit of Assassination (mode learning). |
| `Sandalphon.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Sandalphon.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Sandalphon.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Sandalphon.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Sandalphon.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Sandalphon.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Sandalphon.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Sandalphon.mpAcquirement` | 500,000 | Magicule cost to acquire Sandalphon, Lord of Judgment. |
| `Sandalphon.raidWinsRequired` | 15 | Raid wins required for Judgment acquisition. |
| `Sandalphon.masteredSkillsRequired` | 25 | Mastered skills required for Judgment acquisition. |
| `Sandalphon.concealmentLevel` | 5 | Silent Movement toggle: presence concealment amplifier (level = value - 1). |
| `Sandalphon.concealAttackBonus` | 8 | Existence Concealment attack damage bonus while active. |
| `Sandalphon.removeCooldown` | 5 | Remove in-slot cooldown (skill seconds). |
| `Sandalphon.dispelCooldown` | 3 | Dispel in-slot cooldown (skill seconds). |
| `Sandalphon.eraserCooldown` | 2 | Eraser in-slot cooldown (skill seconds). |
| `Sandalphon.necrosisCooldown` | 30 | Necrosis in-slot cooldown (skill seconds). |
| `Sandalphon.necrosisDuration` | 25 | Necrosis duration (skill seconds). |
| `Sandalphon.judgementCooldown` | 1,440 | Judgement combo cooldown (skill seconds). |
| `Sandalphon.judgementNecrosisDuration` | 60 | Judgement Necrosis duration (skill seconds). |
| `Sandalphon.eraserKillEpRatio` | 0.15 | Eraser instant-kill EP ratio vs user (normal). |
| `Sandalphon.eraserMpDrainRatio` | 0.05 | Eraser: fraction of target max magicule drained per hit (non-ultimate targets). |
| `Sandalphon.eraserMpDrainUltRatio` | 0.025 | Eraser: fraction of target max magicule drained vs ultimate holders. |
| `Sandalphon.judgementEraserKillEpRatio` | 0.5 | Judgement Eraser instant-kill EP ratio vs user. |
| `Sandalphon.judgementEraserBonusEpRatio` | 0.35 | Judgement Eraser bonus EP drain fraction of target current EP. |
| `Sandalphon.judgementBarrierDamagePerPoint` | 5 | Judgement bonus damage per barrier point destroyed. |
| `Sandalphon.sureHitDashRange` | 16 | Sure Hit dash range. |
| `Sandalphon.sureHitDamageMultiplier` | 5 | Sure Hit damage multiplier (attack damage). |
| `Sandalphon.sureHitCooldown` | 5 | Sure Hit cooldown (skill seconds). |
| `Sandalphon.learnPointsSureHit` | 500 | Learning points required for Sure Hit of Assassination (mode learning). |
| `Sandalphon.conditionPurgeIds` | "tensura:multilayer_barrier", "tensura:haki_coat", "tensura:strengthen", "minecraft:resistance", "minecraft:absorption" | Effect IDs purged by Remove barrier break and Dispel (namespace:path). |
| `Sandalphon.enableUltimateEvolution` | true | Whether Sandalphon can be obtained naturally |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- Silent Movement

</details>

## Tags

`tensura:skills/ultimate_skills`
