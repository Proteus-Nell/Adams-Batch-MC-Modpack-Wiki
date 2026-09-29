# Justice Manas

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Justice Manas](../../../assets/icons/trnightmare/skill/michael.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:justice_manas` |
| **Modes** | 6 |
| **Acquisition cost (MP)** | 900,000 |
| **Max mastery** | 5,000 |
| **Activation** | Press, Hold |

</div>

## Modes

| # | Mode |
|---|---|
| 1 | Castle Guard |
| 2 | Armageddon |
| 3 | Regalia Dominion |
| 4 | Ultimate Dominion |
| 5 | Alternative |
| 6 | Ultimate Enchantment |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you are attacked
- Triggers when you take damage
- Does something when first learned

## Obtaining

- Acquisition checks: [｢ Michael, Lord of Justice ｣](michael.md)
- In-game message: *Evolution complete: Michael has awakened.*

## Related

- **Related skills:** [｢ Michael, Lord of Justice ｣](michael.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Michael.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Michael.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Michael.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Michael.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Michael.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Michael.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Michael.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Michael.mpAcquirement` | 900,000 | Magicule obtainment cost. |
| `Michael.castleGuardRequiredSubordinates` | 3 | Castle Guard minimum subordinate count required. |
| `Michael.castleGuardDurationTicks` | 3,600 | Castle Guard active duration (ticks). |
| `Michael.castleGuardMpDrain` | 10,000 | Castle Guard MP drain per second when not mastered. |
| `Michael.castleGuardMpDrainMastered` | 5,000 | Castle Guard MP drain per second when mastered. |
| `Michael.armageddonHoldTicks` | 400 | Armageddon hold duration (ticks). |
| `Michael.armageddonHoldTicksMastered` | 100 | Armageddon hold duration when mastered (ticks). |
| `Michael.armageddonCooldownSeconds` | 300 | Armageddon cooldown (Tensura seconds). |
| `Michael.armageddonSummonCount` | 3 | Armageddon angel knight summon count when not mastered. |
| `Michael.armageddonSummonCountMastered` | 6 | Armageddon angel knight summon count when mastered. |
| `Michael.armageddonSummonHp` | 500 | Armageddon angel knight HP when not mastered. |
| `Michael.armageddonSummonHpMastered` | 1,000 | Armageddon angel knight HP when mastered. |
| `Michael.regaliaHoldTicks` | 1,200 | Regalia hold duration (ticks). |
| `Michael.regaliaHoldTicksMastered` | 600 | Regalia hold duration when mastered (ticks). |
| `Michael.regaliaTargetRange` | 8 | Regalia targeting range (blocks). |
| `Michael.regaliaDominanceStrength` | 1.2 | Regalia domination strength multiplier. |
| `Michael.regaliaDominationTicks` | 60 | Regalia domination duration. |
| `Michael.regaliaCooldownSeconds` | 180 | Regalia cooldown. |
| `Michael.ultimateDominionTargetRange` | 12 | Ultimate Dominion targeting range (blocks). |
| `Michael.ultimateDominionCooldownSeconds` | 120 | Ultimate Dominion cooldown. |
| `Michael.subordinateBondThreshold` | 1,500 | Sariel bond points required for subordinate dominion (no Virtue Skill needed). |
| `Michael.alternativeGrantLimit` | 8 | Alternative grant variants Michael can bestow before the set is exhausted. |
| `Michael.ultimateEnchantmentCooldownSeconds` | 2,400 | Ultimate Enchantment cooldown in seconds. |
| `Michael.ultimateEnchantmentBlacklist` | "trnightmare:akashic_records", "trnightmare:azathoth", "trnightmare:nodens", "trnightmare:yog-sothort", "trnightmare:michael" | Ultimate skills blacklisted from Ultimate Enchantment. |
| `Michael.evolutionRaidWins` | 25 | Raid wins required to evolve Dominator into Michael. |
| `Michael.evolutionMobKills` | 5,000 | Mob kills required to evolve Dominator into Michael. |
| `Michael.virtueDominionSkills` | "trnightmare:gabriel", "trnightmare:michael", "trnightmare:raguel", "trnightmare:sariel", "trnightmare:sandalphon_judgement", "trnightmare:sandalphon_punishment", "trnightmare:haniel", "trnightmare:metatron", "trnightmare:uriel_lord_of_oath", "trnightmare:uriel_lord_of_vow", "trnightmare:raphael_knowledge", "trnightmare:raphael_wisdom", "trnightmare:astarte", "trnightmare:stasis", "trnightmare:cadence", "trnightmare:glorius", "trnightmare:designer", "trnightmare:saint", "trnightmare:endorse", "tensura:infinity_prison" ... (23 total) | Virtue skills that Ultimate Dominion can copy from targets. |
| `Michael.enableUltimateEvolution` | true | Whether Michael evolution is allowed. |
