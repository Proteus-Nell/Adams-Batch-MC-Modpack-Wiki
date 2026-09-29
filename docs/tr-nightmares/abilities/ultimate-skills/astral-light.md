# ｢ Astral Light, Lord of Creation ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:astral_light` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 750,000 |
| **Max mastery** | 15,000 |
| **Cooldowns (s)** | 30 |
| **Activation** | Press, Hold |

</div>

> An ultimate skill of creation-based light and celestial manifestation.

> [!NOTE]
> **Pack note:** this pack changes the defaults below.
> - `AstralLight.astralExtraUniqueSkills` is **"trnightmare:infinity", "trnightmare:ending", "trnightmare:coffin_of_darkness", "trnightmare:cadence", "trnightmare:endorse", "trnightmare:tempter", "trnightmare:breaker", "trnightmare:deadly_poison", "trnightmare:saint", "trnightmare:investigator"** (mod default: "trnightmare:infinity", "trnightmare:ending", "trnightmare:coffin_of_darkness", "trnightmare:tempter", "trnightmare:breaker", "trnightmare:deadly_poison", "trnightmare:investigator")
> - `AstralLight.astralMasteredCreationUltimates` is **"trnightmare:susanoo", "trnightmare:tsukiyomi", "trnightmare:amaterasu", "trnightmare:sandalaphon_judgment", "trnightmare:hastur", "trnightmare:agni", "trnightmare:belial", "trnightmare:azazel", "trnightmare:samael", "trnightmare:metatron", "trnightmare:faust"** (mod default: "trnightmare:susanoo", "trnightmare:tsukiyomi", "trnightmare:amaterasu", "trnightmare:sandalaphon_judgment", "trnightmare:hastur", "trnightmare:agni", "trnightmare:belial", "trnightmare:azazel", "trnightmare:samael", "trnightmare:faust")

## Modes

| # | Mode |
|---|---|
| 1 | Skill Creation |
| 2 | Tachyon |
| 3 | Bodily Recreation |
| 4 | Material Creation |
| 5 | Memory Restoration |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| learning | l | add |
| mastery | m | add |

## Obtaining

- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Acquisition checks: [Creator](../../../tensura-reincarnated/abilities/unique-skills/creator.md), [｢ Astral Light, Lord of Creation ｣](astral-light.md)
- In-game message: *The Unique Skill Creator resonates with Astral Light: you have obtained the Ultimate Skill %s.*
- In-game message: *&lt;wave&gt;&lt;neon p=8 r=2 a=0.14&gt;&lt;grad from=#7FFFD4 to=#C8A2FF hue f=0.6 sp=14&gt;&lt;rainb f=1.1 w=0.35&gt;｢ Astral Light, Lord of Creation ｣&lt;/rainb&gt;&lt;/grad&gt;&lt;/neon&gt;&lt;/wave&gt;*

## Related

- **Related skills:** [Creator](../../../tensura-reincarnated/abilities/unique-skills/creator.md)
- **Effects:** [Anti-Skill](../../../tensura-reincarnated/effects/anti-skill.md)
- **Referenced by:** [｢ Mammon, Lord of Greed ｣](mammon.md), [｢ Akashic Records, God of Origin ｣](akashic-records.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | This pack | Description |
|---|---|---|---|
| `AstralLight.masterySinUlt` | 15,000 | | The max amount of mastery points for Sin Ultimate Skills. |
| `AstralLight.masteryVirtueUlt` | 25,000 | | The max amount of mastery points for Virtue Ultimate Skills. |
| `AstralLight.masteryAngelicUlt` | 5,000 | | The max amount of mastery points for Angelic Ultimate Skills. |
| `AstralLight.masteryDemonicUlt` | 5,000 | | The max amount of mastery points for Demonic Ultimate Skills. |
| `AstralLight.masteryGodUlt` | 50,000 | | The max amount of mastery points for God Ultimate Skills. |
| `AstralLight.masteryKingUlt` | 35,000 | | The max amount of mastery points for King Ultimate Skills. |
| `AstralLight.masteryGenericUlt` | 5,000 | | The max amount of mastery points for Generic Ultimate Skills. |
| `AstralLight.mpAcquirement` | 750,000 | | Acquirement MP cost display baseline (evolution uses evolutionMinMagiculeCap). |
| `AstralLight.evolutionMinMagiculeCap` | 750,000 | | Minimum max magicules required to evolve (750k default). |
| `AstralLight.antiSkillCreatesFloor` | 10 | | Anti-Skill creations via Creator must exceed this integer (default: need &gt;10 i.e. count 11+). |
| `AstralLight.tachyonMasteryBonus` | 25 | | Tachyon Processing: flat Ability Mastery Gain while In-Slot on that mode. |
| `AstralLight.tachyonLearningBonus` | 25 | | Tachyon Processing: flat Ability Learning Gain while In-Slot on that mode. |
| `AstralLight.bodilyHoldSeconds` | 60 | | Bodily Recreation: seconds of hold required (skill tick = 1/s; hold uses 20 MC ticks per slice). |
| `AstralLight.bodilyMpPerTickSecond` | 5,000 | | Bodily Recreation: MP drained each second while held. |
| `AstralLight.bodilyCooldownSeconds` | 3,600 | | Bodily Recreation: cooldown after success (Tensura seconds). |
| `AstralLight.directiveImprintCooldownSeconds` | 600 | | Directive Imprint: cooldown after a successful imprint (Tensura seconds). |
| `AstralLight.materialCreationSoftThreshold` | 8,192 | | Material Creation mode: EMC at or below this spends current magicules only; above applies daemon-bound tag and max magicule cost. |
| `AstralLight.astralExtraUniqueSkills` | "trnightmare:infinity", "trnightmare:ending", "trnightmare:coffin_of_darkness", "trnightmare:tempter", "trnightmare:breaker", "trnightmare:deadly_poison", "trnightmare:investigator" | "trnightmare:infinity", "trnightmare:ending", "trnightmare:coffin_of_darkness", "trnightmare:cadence", "trnightmare:endorse", "trnightmare:tempter", "trnightmare:breaker", "trnightmare:deadly_poison", "trnightmare:saint", "trnightmare:investigator" | Extra unique skill IDs merged into Astral Light Skill Creation (after Tensura Creator). |
| `AstralLight.astralMasteredCreationUltimates` | "trnightmare:susanoo", "trnightmare:tsukiyomi", "trnightmare:amaterasu", "trnightmare:sandalaphon_judgment", "trnightmare:hastur", "trnightmare:agni", "trnightmare:belial", "trnightmare:azazel", "trnightmare:samael", "trnightmare:faust" | "trnightmare:susanoo", "trnightmare:tsukiyomi", "trnightmare:amaterasu", "trnightmare:sandalaphon_judgment", "trnightmare:hastur", "trnightmare:agni", "trnightmare:belial", "trnightmare:azazel", "trnightmare:samael", "trnightmare:metatron", "trnightmare:faust" | Ultimate skill IDs only offered from Astral Light Skill Creation when Astral Light is mastered. |
| `AstralLight.enableUltimateEvolution` | true | | Whether Creator can evolve into Astral Light. |

Set in [`config/tensura/ability/skill/unique_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Creator.mpAcquirement` | 75,000 | Magicule Acquirement Cost. |
| `Creator.analysisLevel` | 2 | The Analysis Level when activated. |
| `Creator.analysisLevelMastered` | 6 | The Analysis Level when activated with Mastery. |
| `Creator.analysisRadius` | 0 | The Analysis Radius when activated. |
| `Creator.analysisRadiusMastered` | 5 | The Analysis Radius when activated with Mastery. |
| `Creator.creationCooldown` | 1,200 | The cooldown in second after creating a Skill. |
| `Creator.creationVanishTimer` | 1,200 | The cooldown in second before the created skill vanishes. |
| `Creator.masteryGainMultiplier` | 5 | The multiplier for mastery point gaining when created a Skill. |
| `Creator.uniqueSkills` | "tensura:anti_skill", "tensura:analyst", "tensura:absolute_severance", "tensura:berserk", "tensura:berserker", "tensura:bewilder", "tensura:chef", "tensura:commander", "tensura:cook", "tensura:falsifier", "tensura:fighter", "tensura:fusionist", "tensura:gourmand", "tensura:guardian", "tensura:healer", "tensura:martial_master", "tensura:mathematician", "tensura:murderer", "tensura:musician", "tensura:observer" ... (39 total) | List of Unique skills that can be created by Creator. |

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `MaterialCreation.epAcquirement` | 10,000 | EP obtainment cost (intrinsic skill parity). |
| `MaterialCreation.researchHitsToLearn` | 100 | Total research points needed on one item/block identity before it is learned (Understanding mode). |
| `MaterialCreation.destroyChance` | 0.15 | Chance to destroy the researched stack or block each pulse. |
| `MaterialCreation.understandingCooldownTicks` | 600 | Cooldown in Minecraft ticks after each Understanding pulse (skill UI uses seconds → stored value / 20). |
| `MaterialCreation.reachDistance` | 6 | Ray trace reach when main hand is empty. |
| `MaterialCreation.refundFraction` | 0.5 | Refund fraction when inserting daemon-bound stacks into the bench refund slot. |
| `MaterialCreation.softMagiculeThreshold` | 4,096 | EMC at or below this value spends current magicules only and is not daemon-bound. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- &lt;wave&gt;&lt;neon p=8 r=2 a=0.14&gt;&lt;grad from=#7FFFD4 to=#C8A2FF hue f=0.6 sp=14&gt;&lt;rainb f=1.1 w=0.35&gt;｢ Astral Light, Lord of Creation ｣&lt;/rainb&gt;&lt;/grad&gt;&lt;/neon&gt;&lt;/wave&gt;

</details>

## Tags

`tensura:skills/amnesiac`
