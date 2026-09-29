# Wise Manas

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Wise Manas](../../../assets/icons/trnightmare/skill/raphael_knowledge.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:wise_manas` |
| **Acquisition cost (MP)** | 250,000 |
| **Activation** | Toggle, Press |

</div>

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you die
- Triggers when you respawn
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| learning | learning point | add |
| mastery | mastery point | add |
| dodgeNegate | negate dodge | add |

## Related

- **Related skills:** [｢ Raphael, Lord of Wisdom ｣](raphael-wisdom.md), [Degenerate](../../../tensura-reincarnated/abilities/unique-skills/degenerate.md), [｢ Raphael, Lord of Knowledge ｣](raphael-knowledge.md)

## Stats (config defaults)

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

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
