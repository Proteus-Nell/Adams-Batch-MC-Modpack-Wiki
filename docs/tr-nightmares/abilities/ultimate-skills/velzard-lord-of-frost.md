# ｢ Velzard, Lord of Frost ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:velzard_lord_of_frost` |
| **Acquisition cost (MP)** | 1,000,000 |
| **Max mastery** | 35,000 |
| **Activation** | Press, Hold |

</div>

> True Dragon of Frost. Frost-type magic while in slot. Hold to summon Velzard's human form.

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `TrueDragon.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `TrueDragon.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `TrueDragon.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `TrueDragon.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `TrueDragon.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `TrueDragon.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `TrueDragon.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `TrueDragon.mpAcquirement` | 1,000,000 | Magicule cost to acquire a True Dragon ultimate (unused — granted via Inner World bond). |
| `TrueDragon.baseSummonHoldSeconds` | 60 | Base seconds to hold summon before human-form clone appears. |
| `TrueDragon.summonHoldReductionPer100Mastery` | 10 | Seconds removed from summon hold per 100 skill mastery. |
| `TrueDragon.ultimateLearnChance` | 0.05 | Chance at 500+ rapport to learn the Lord ultimate while holding the intrinsic. |
| `TrueDragon.stormDamageMultiplier` | 1.5 | Storm Lord in-slot damage multiplier (1.5 = +50%). |
| `TrueDragon.scorchDamageMultiplier` | 1.5 | Scorch Lord in-slot damage multiplier (1.5 = +50%). |
| `TrueDragon.frostDamageMultiplier` | 2.5 | Frost Lord in-slot cold damage multiplier (2.5 = +150%). |
| `TrueDragon.earthDamageMultiplier` | 1.75 | Earth Lord in-slot earth damage multiplier (1.75 = +75%). |
| `TrueDragon.gravityDamageMultiplier` | 1.75 | Earth Lord in-slot gravity damage multiplier (1.75 = +75%). |
| `TrueDragon.antiMasteryPerRelation` | 1 | Anti-Skill mastery gained per rapport point above the rapport when Anti was first learned. |
| `TrueDragon.dragonBodyHp` | 1,400 | Dragon body form max HP (replaces base max health while active). |
| `TrueDragon.dragonBodyShp` | 8,560 | Dragon body form max spiritual HP (replaces base while active). |
| `TrueDragon.dragonBodyAttack` | 21 | Dragon body form attack damage (replaces base while active). |
| `TrueDragon.dragonBodyArmor` | 75 | Dragon body form armor (replaces base while active). |
| `TrueDragon.enableUltimateEvolution` | true | Whether True Dragon can be obtained naturally |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

## Tags

`tensura:skills/ultimate_skills`
