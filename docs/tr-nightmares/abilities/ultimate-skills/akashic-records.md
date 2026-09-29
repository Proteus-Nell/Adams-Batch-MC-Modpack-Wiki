# ｢ Akashic Records, God of Origin ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:akashic_records` |
| **Modes** | 8 |
| **Acquisition cost (MP)** | 20,000,000 |
| **Max mastery** | 50,000 |
| **Cooldowns (s)** | 3,600 |
| **Activation** | Press, Hold |

</div>

> A God-class ultimate skill tied to the origin of knowledge and universal records.

## Modes

| # | Mode |
|---|---|
| 1 | Skill Creation |
| 2 | Informational Understanding |
| 3 | Star King Creation |
| 4 | Godly Body |
| 5 | Residual Breeder Reactor |
| 6 | Star Order |
| 7 | Information Re-Creation |
| 8 | Material Creation |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when an effect is applied to you
- Does something when first learned

## Obtaining

- Listed in the `ultimateEnchantmentBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Ultimate skills blacklisted from Ultimate Enchantment.
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Acquisition checks: [｢ Akashic Records, God of Origin ｣](akashic-records.md), [｢ Astral Light, Lord of Creation ｣](astral-light.md)
- In-game message: *Astral Light ascends into Akashic Records.*

## Related

- **Related skills:** [｢ Astral Light, Lord of Creation ｣](astral-light.md)
- **Effects:** [Magicule Poison](../../../tensura-reincarnated/effects/magicule-poison.md), [Insanity](../../../tensura-reincarnated/effects/insanity.md), [Anti-Skill](../../../tensura-reincarnated/effects/anti-skill.md)
- **Referenced by:** [｢ Mammon, Lord of Greed ｣](mammon.md)

## Stats (config defaults)

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

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `AkashicRecords.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `AkashicRecords.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `AkashicRecords.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `AkashicRecords.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `AkashicRecords.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `AkashicRecords.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `AkashicRecords.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `AkashicRecords.mpAcquireRequirement` | 20,000,000 | Acquirement / evolution max MP requirement. |
| `AkashicRecords.epAcquireRequirement` | 60,000,000 | Current EP required to evolve or run checkevoconditions. |
| `AkashicRecords.zaganBedrockRequired` | 10 | Placeholder Zagan requirement: bedrock blocks mined (MC stats). |
| `AkashicRecords.knowItAllMasteryBonus` | 35 | Know It All: flat Ability Mastery Gain while skill toggled on. |
| `AkashicRecords.knowItAllLearningBonus` | 35 | Know It All: flat Ability Learning Gain while skill toggled on. |
| `AkashicRecords.knowItAllMeleeDodge` | 0.75 | Know It All: melee dodge chance (0-1). |
| `AkashicRecords.knowItAllProjectileDodge` | 0.75 | Know It All: projectile dodge chance (0-1). |
| `AkashicRecords.knowItAllCritDamageBonus` | 1 | Know It All: critical damage multiplier bonus (1.0 = +100% crit damage). |
| `AkashicRecords.maxActiveCreatedSkills` | 3 | Max concurrently active created skills (FIFO removes oldest). |
| `AkashicRecords.skillCreationCooldownSeconds` | 5 | Skill Creation menu cooldown (seconds) after creating a skill. |
| `AkashicRecords.extraUniqueSkills` | [] (empty) | Extra unique skill IDs in Skill Creation (after Creator + Astral extras). |
| `AkashicRecords.extraUltimateSkills` | [] (empty) | Extra ultimate skill IDs in Skill Creation when Akashic Records is mastered. |
| `AkashicRecords.godlyBodyMpCost` | 1,500,000 | Godly Body MP cost. |
| `AkashicRecords.starKingVesselHp` | 15,000 | Star King Vessel (clone) max HP. |
| `AkashicRecords.starKingVesselShp` | 35,000 | Star King Vessel max spiritual HP. |
| `AkashicRecords.starKingVesselAttack` | 15 | Star King Vessel attack damage. |
| `AkashicRecords.starKingVesselArmor` | 100 | Star King Vessel armor. |
| `AkashicRecords.starKingManasVesselHp` | 1,500 | Star King Vessel stats when summoning from bound Manas in inner world. |
| `AkashicRecords.starKingManasVesselAttack` | 40 | Star King Manas vessel attack damage. |
| `AkashicRecords.starKingManasVesselArmor` | 100 | Star King Manas vessel armor. |
| `AkashicRecords.starKingBonusCreatedSkills` | 2 | Random extra created skills granted to a full Star King vessel (0 disables). |
| `AkashicRecords.reactorIntervalTicks` | 115 | Residual Breeder Reactor: ticks between MP pulses. |
| `AkashicRecords.reactorMpFraction` | 0.05 | Residual Breeder Reactor: fraction of max MP gained per pulse. |
| `AkashicRecords.reactorMpFractionMastered` | 0.1 | Residual Breeder Reactor: fraction when mastered. |
| `AkashicRecords.reactorMaxMpMultiplier` | 5.25 | Residual Breeder Reactor: max MP multiplier cap (5.25 = 525%). |
| `AkashicRecords.starOrderCooldownSeconds` | 600 | Star Order cooldown after imprint (Tensura seconds). |
| `AkashicRecords.starKingCooldownSeconds` | 3,600 | Star King Creation cooldown (seconds) after summoning a vessel. |
| `AkashicRecords.materialCreationSoftThreshold` | 16,000 | Material Creation soft MP threshold (current MP below this, else max MP). |
| `AkashicRecords.enableUltimateEvolution` | true | Whether Astral Light can evolve into Akashic Records. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- &lt;wave&gt;&lt;neon p=8 r=2 a=0.14&gt;&lt;grad from=#A7F3FF to=#D7C7FF hue f=0.6 sp=14&gt;&lt;rainb f=1.1 w=0.35&gt;｢ Akashic Records, God of Origin ｣&lt;/rainb&gt;&lt;/grad&gt;&lt;/neon&gt;&lt;/wave&gt;

</details>

## Tags

`tensura:skills/amnesiac`, `tensura:skills/ultimate_skills`
