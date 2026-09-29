# Alteration

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:alteration` |
| **Max mastery** | 25,000 |
| **Activation** | Press |

</div>

> Synthesize new skills from existing learned skills without requiring Raphael or mastery.

## How it works

- Activated by pressing the skill key

## Obtaining

- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.

## Related

- **Related skills:** [｢ Beelzebuth, Lord of Gluttony ｣](../ultimate-skills/beelzebuth.md), [｢ Raphael, Lord of Wisdom ｣](../ultimate-skills/raphael-wisdom.md), [｢ Uriel, Lord of Oaths ｣](../ultimate-skills/uriel-lord-of-oath.md), [｢ Susanoo, Lord of Tyranny ｣](../ultimate-skills/susanoo.md), [｢ Amaterasu, Lord of Shimmering Flames ｣](../ultimate-skills/amaterasu.md), [Future Attack Prediction](future-attack-prediction.md), [｢ Tsukiyomi, Lord of Moonshadow ｣](../ultimate-skills/tsukiyomi.md), [｢ Azazel, Lord of Temptation ｣](../ultimate-skills/azazel.md), [｢ Belial, Lord of The Dead ｣](../ultimate-skills/belial.md), [｢ Samael, Lord of Deadly Poison ｣](../ultimate-skills/samael.md), [｢ Mood Maker, Lord of Psychology ｣](../ultimate-skills/mood-maker.md), [｢ Beelzebub, Lord of Gourmet ｣](../ultimate-skills/beelzebub.md), [Law Domination](law-domination.md), [｢ Nodens, God of Abyss ｣](../ultimate-skills/nodens.md), [｢ Cthugha, King of Divine Flame ｣](../ultimate-skills/cthugha.md), [Gluttony](../../../tensura-reincarnated/abilities/unique-skills/gluttony.md), [Merciless](../../../tensura-reincarnated/abilities/unique-skills/merciless.md), [Cook](../../../tensura-reincarnated/abilities/unique-skills/cook.md), [Commander](../../../tensura-reincarnated/abilities/unique-skills/commander.md), [Maximum Will](../battlewill/maximum-will.md) and 5 more

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `Alteration.allowedUserIds` | "trnightmare:raphael_knowledge", "trnightmare:raphael_wisdom", "trnightmare:azathoth" | Skill ids that can use Raphael-style alteration by default. |
| `Alteration.allowedSkillIds` | "trnightmare:beelzebub", "trnightmare:beelzebuth", "trnightmare:raphael_wisdom", "trnightmare:susanoo", "trnightmare:uriel_lord_of_oath", "trnightmare:tsukiyomi", "trnightmare:samael", "trnightmare:belial", "trnightmare:azazel", "trnightmare:amaterasu", "trnightmare:law_domination", "trnightmare:mood_maker", "trnightmare:cthugha", "trnightmare:nodens" | Skill ids that can be affected by Raphael-style alteration by default. |

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Raphael.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Raphael.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Raphael.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Raphael.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Raphael.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Raphael.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Raphael.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Raphael.mpAcquirement` | 250,000 | The Magicule cost to acquire the Ultimate Skill: Raphael. |
| `Raphael.chantSpeed` | 4 | Chant speed multiplier while Raphael is toggled on. |
| `Raphael.learningPoint` | 24 | Additional learning point gain while Raphael is toggled on. |
| `Raphael.masteryPoint` | 24 | Additional mastery point gain while Raphael is toggled on. |
| `Raphael.analysisLevel` | 10 | Analysis level granted when not mastered. |
| `Raphael.analysisLevelMastered` | 30 | Analysis level granted when mastered. |
| `Raphael.analysisRadius` | 16 | Analysis radius when not mastered. |
| `Raphael.analysisRadiusMastered` | 32 | Analysis radius when mastered. |
| `Raphael.copyRange` | 15 | Copy range for living entities. |
| `Raphael.copyRangeMagic` | 30 | Copy range for magic circles. |
| `Raphael.copyChance` | 50 | Copy chance (%) when not mastered. |
| `Raphael.copyChanceMastered` | 90 | Copy chance (%) when mastered. |
| `Raphael.copyCooldownSuccess` | 25 | Cooldown on successful copy (seconds). Manas skill cooldowns decrement once per skill tick (not each Minecraft tick). |
| `Raphael.copyCooldownFail` | 10 | Cooldown on failed copy (seconds). Same units as copyCooldownSuccess. |
| `Raphael.negateDodge` | 100 | Raphael Chance to Negate Dodge. |
| `Raphael.integrationRange` | 20 | Maximum distance to target a Body Double for Integration. |
| `Raphael.scanRadius` | 24 | Radius for Raphael's scanning ability. |
| `Raphael.scanGlowDuration` | 60 | Duration of glowing applied during scanning. |
| `Raphael.converseMasteryChance` | 0.25 | Chance (0.0–1.0) to gain mastery when conversing with Raphael. |
| `Raphael.socialityGain` | 1 | Amount of Sociality gained per conversation. |
| `Raphael.socialityNamingThreshold` | 100 | Sociality required before Raphael's Ego can be named. |
| `Raphael.conversePassiveChance` | 0.02 | Chance (0.0–1.0) for Raphael to speak passively every ~10 minutes. |
| `Raphael.alterationCooldownSeconds` | 300 | Cooldown between Alteration evolutionary syntheses (seconds). Skill UI cooldowns use seconds because they decrement on skill ticks, not every Minecraft tick. |
| `Raphael.reconSocialCooldownSeconds` | 600 | Minimum time between social-point gains from Recon talk / Integrate bundle (seconds of in-game time; uses game ticks internally). |
| `Raphael.egoNamingEpRequired` | 5,000,000 | EP required for Body Double naming |
| `Raphael.socialPointsToName` | 50 | Social points needed before Raphael's ego can receive a name. |
| `Raphael.socialGainAlteration` | 5 | Social points gained on successful Alteration evolution. |
| `Raphael.socialGainTalk` | 1 | Social points gained from Raphael conversational lines (shift Recon when off cooldown part). |
| `Raphael.socialGainReconIntegrate` | 3 | Social points gained from Integrate + Recon bundle when cooldown allows. |
| `Raphael.raphaelSkillMastered` | 35 | Skills mastered to obtain Raphael. You also need Sage and Chant Annul |
| `Raphael.raphaelRaidCount` | 10 | Raid Victories to obtain Raphael. |
| `Raphael.raphaelSubordinateCount` | 15 | Subordinates to obtain Raphael. |
| `Raphael.enableUltimateEvolution` | true | Whether Raphael evolution is allowed. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

## Tags

`tensura:skills/no_plundering`
