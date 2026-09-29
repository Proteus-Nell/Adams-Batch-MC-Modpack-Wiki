# ｢ Astaroth, King of Fallen ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:astaroth` |
| **Modes** | 9 |
| **Acquisition cost (MP)** | 3,900,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 5, 15 |
| **Activation** | Press, Hold |

</div>

> A King-class ultimate skill associated with fallen authority and corrupt dominion.

## Modes

| # | Mode |
|---|---|
| 1 | Fallen Edge |
| 2 | Fallen Catastrophe |
| 3 | Fallen Strike |
| 4 | Phantasmal Style |
| 5 | Fallen Thanatos |
| 6 | Fallen Sleep |
| 7 | Skill Domination |
| 8 | Sacrilegious Creation |
| 9 | Destruction |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 |  |
| Always | 50,000 or 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| inst | amount | add |

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Acquisition checks: [｢ Astaroth, King of Fallen ｣](astaroth.md), [｢ Astarte, Lord of Heaven ｣](astarte.md), [｢ Belphegor, Lord of Sloth ｣](belphegor.md)
- In-game message: *Heaven and Sloth merge. Astaroth, King of Fallen, awakens.*

## Related

- **Related skills:** [Hand of Creation](../extra-skills/hand-of-creation.md), [Hand of Destruction](../extra-skills/hand-of-destruction.md), [｢ Astarte, Lord of Heaven ｣](astarte.md), [｢ Belphegor, Lord of Sloth ｣](belphegor.md), [Spiritual Attack Nullification](../../../tensura-reincarnated/abilities/resistance-skills/spiritual-attack-nullification.md), [Spiritual Attack Resistance](../../../tensura-reincarnated/abilities/resistance-skills/spiritual-attack-resistance.md)
- **Effects:** [Shadow Step](../../../tensura-reincarnated/effects/shadow-step.md), [Drowsiness](../../../tensura-reincarnated/effects/drowsiness.md)
- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Astaroth.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Astaroth.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Astaroth.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Astaroth.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Astaroth.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Astaroth.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Astaroth.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Astaroth.enableUltimateEvolution` | true |  |
| `Astaroth.mpAcquirement` | 3,900,000 |  |
| `Astaroth.epRequirement` | 15,000,000 |  |
| `Astaroth.belphegorStoredMpRequired` | 100,000 |  |
| `Astaroth.heavenlyDesignUsesRequired` | 10 |  |
| `Astaroth.recycleUsesRequired` | 10 |  |
| `Astaroth.holyDamageReduction` | 0.15 |  |
| `Astaroth.dualityLearningBonus` | 15 |  |
| `Astaroth.dualityMasteryBonus` | 15 |  |
| `Astaroth.phantasmalPercent` | 0.025 |  |
| `Astaroth.phantasmalPercentMastered` | 0.05 |  |
| `Astaroth.phantasmalDrowsinessChance` | 0.15 |  |
| `Astaroth.phantasmalDrowsinessChanceMastered` | 0.3 |  |
| `Astaroth.phantasmalDrowsinessDuration` | 200 |  |
| `Astaroth.fallenCatastropheRange` | 12 |  |
| `Astaroth.magiculeCostFallenCatastrophe` | 50,000 |  |
| `Astaroth.fallenCatastropheCooldown` | 15 |  |
| `Astaroth.fallenCatastropheDrowsinessDuration` | 200 |  |
| `Astaroth.fallenStrikePercent` | 0.025 |  |
| `Astaroth.fallenStrikePercentMastered` | 0.05 |  |
| `Astaroth.fallenThanatosRadius` | 20 |  |
| `Astaroth.magiculeCostThanatosPerTick` | 50 |  |
| `Astaroth.fallenThanatosDrowsinessDuration` | 200 |  |
| `Astaroth.fallenSleepHealHP` | 100 |  |
| `Astaroth.fallenSleepHealSHP` | 100 |  |
| `Astaroth.fallenSleepHealMasteryBonus` | 0.25 |  |
| `Astaroth.fallenSleepMpRegenMultiplier` | 15 |  |
| `Astaroth.fallenSleepStoredMpPerSecond` | 1,500 |  |
| `Astaroth.fallenSleepStoredMpPerSecondMastered` | 3,000 |  |
| `Astaroth.fallenSleepAllyStoredMpThreshold` | 500,000 |  |
| `Astaroth.fallenSleepAllyMpPerSecond` | 5,000 |  |
| `Astaroth.fallenSleepAllyRadius` | 15 |  |
| `Astaroth.fallenSleepCooldown` | 5 |  |
| `Astaroth.magiculeCostFallenSleepPerTick` | 10 |  |
| `Astaroth.skillCreateMpMultiplier` | 8 |  |
| `Astaroth.uniqueTempMasteryCost` | 1,000 |  |
| `Astaroth.uniquePermMasteryCost` | 5,000 |  |
| `Astaroth.ultimateTempMasteryCost` | 10,000 |  |
| `Astaroth.fallenOneStoredMpPerMinute` | 30,000 |  |
| `Astaroth.fallenOneMpPerMinute` | 25,000 |  |
| `Astaroth.fallenWorldRadius` | 32 |  |
| `Astaroth.fallenWorldDurationTicks` | 1,200 |  |
| `Astaroth.recycleBonusChance` | 0.3 |  |
| `Astaroth.recycleBonusChanceMastered` | 0.6 |  |
| `Astaroth.recycleBonusMpFraction` | 0.4 |  |
| `Astaroth.recycleBonusMpFractionMastered` | 0.8 |  |
| `Astaroth.fallenOneMinuteTier1` | 1 |  |
| `Astaroth.fallenOneMinuteTier2` | 3 |  |
| `Astaroth.fallenOneMinuteTier3` | 5 |  |
| `Astaroth.fallenOneMinuteTier4` | 8 |  |
| `Astaroth.fallenOneMinuteTier5` | 10 |  |
| `Astaroth.fallenOneMinuteTier6` | 15 |  |
| `Astaroth.fallenOneAttackTier1` | 35 |  |
| `Astaroth.fallenOneAttackTier2` | 70 |  |
| `Astaroth.fallenOneAttackTier3` | 105 |  |
| `Astaroth.fallenOneAttackTier4` | 140 |  |
| `Astaroth.fallenOneAttackTier5` | 175 |  |
| `Astaroth.fallenOneAttackTier6` | 205 |  |
| `Astaroth.fallenOneArmorTier1` | 30 |  |
| `Astaroth.fallenOneArmorTier2` | 60 |  |
| `Astaroth.fallenOneArmorTier3` | 90 |  |
| `Astaroth.fallenOneArmorTier4` | 120 |  |
| `Astaroth.fallenOneArmorTier5` | 150 |  |
| `Astaroth.fallenOneArmorTier6` | 170 |  |
| `Astaroth.fallenOneDamageReductionTier1` | 0.1 |  |
| `Astaroth.fallenOneDamageReductionTier2` | 0.2 |  |
| `Astaroth.fallenOneDamageReductionTier3` | 0.3 |  |
| `Astaroth.fallenOneDamageReductionTier4` | 0.4 |  |
| `Astaroth.fallenOneDamageReductionTier5` | 0.5 |  |
| `Astaroth.fallenOneDamageReductionTier6` | 0.6 |  |
| `Astaroth.fallenLordHolyReduction` | 0.15 |  |
| `Astaroth.fallenLordSpiritualReduction` | 0.15 |  |
| `Astaroth.ruinationHolySpiritualDmgReduction` | 0.5 |  |
| `Astaroth.ruinationHolySpiritualDmgBonus` | 50 |  |
| `Astaroth.creationMpRegenPercent` | 0.15 |  |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## In-game messages

<details markdown><summary>Show 6 messages</summary>

- Fallen Slumber  ▶  Stored Magicules: %s
- Use Skill Domination to store skills first.
- No skills available to destroy.
- Ultimate skills cannot be created permanently.
- Stored %s skill(s) for Sacrilegious Creation (not learned).
- Fallen World released.

</details>

## Tags

`tensura:skills/ultimate_skills`
