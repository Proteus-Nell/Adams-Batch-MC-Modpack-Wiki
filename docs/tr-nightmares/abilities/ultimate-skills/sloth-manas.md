# Sloth Manas

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:sloth_manas` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 1,000,000 |
| **Activation** | Toggle, Press, Hold |

</div>

## Modes

| # | Mode |
|---|---|
| 1 | Fallen Catastrophe |
| 2 | Fallen Thanatos |
| 3 | Fallen Strike |
| 4 | True Sleep |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage
- Does something when first learned

## Obtaining

- Acquisition checks: [｢ Belphegor, Lord of Sloth ｣](belphegor.md)
- In-game message: *Sloth surrenders to sleep. Belphegor, Lord of Sloth, awakens.*

## Related

- **Related skills:** [｢ Belphegor, Lord of Sloth ｣](belphegor.md)
- **Effects:** [Rest](../../../tensura-reincarnated/effects/rest.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Belphegor.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Belphegor.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Belphegor.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Belphegor.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Belphegor.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Belphegor.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Belphegor.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Belphegor.enableUltimateEvolution` | true | whether Belphegor can be obtained naturally |
| `Belphegor.mpAcquirement` | 1,000,000 | The Cost for the Ultimate Skill: Belphegor. |
| `Belphegor.evolutionSleepCount` | 50 | Sleep count required for evolution (10 min cooldown between counts). |
| `Belphegor.evolutionSlothStoredMp` | 25,000 | Stored MP on Sloth skill tag required for evolution. |
| `Belphegor.evolutionBedStillMinutes` | 10 | Minutes spent standing still on a bed required for evolution. |
| `Belphegor.evolutionMobKills` | 1,000 | Mob kills required for evolution. |
| `Belphegor.phantasmalPercent` | 0.025 | Percent of target's spiritual HP dealt by Phantasmal Style (unmastered). |
| `Belphegor.phantasmalPercentMastered` | 0.05 | Percent of target's spiritual HP dealt by Phantasmal Style (mastered). |
| `Belphegor.phantasmalDrowsinessChance` | 0.15 | Chance to apply one level of Drowsiness on hit (unmastered). 0.15 = 15% |
| `Belphegor.phantasmalDrowsinessChanceMastered` | 0.3 | Chance to apply one level of Drowsiness on hit (mastered). 0.30 = 30% |
| `Belphegor.phantasmalDrowsinessDuration` | 200 | Duration (ticks) of Drowsiness applied by Phantasmal Style. |
| `Belphegor.fallenCatastropheRange` | 12 | Range to target for Fallen Catastrophe. |
| `Belphegor.magiculeCostFallenCatastrophe` | 50,000 | Magicule cost for Fallen Catastrophe. |
| `Belphegor.fallenCatastropheCooldown` | 10 | Cooldown (skill seconds, 1 per second) for Fallen Catastrophe. |
| `Belphegor.fallenCatastropheDrowsinessDuration` | 200 | Drowsiness duration (ticks) applied by Fallen Catastrophe when conditions partially met. |
| `Belphegor.fallenThanatosRange` | 20 | Range to target for Fallen Thanatos. |
| `Belphegor.magiculeCostThanatosPerTick` | 125 | Magicule cost per tick while holding Fallen Thanatos. |
| `Belphegor.fallenThanatosDrowsinessDuration` | 200 | Drowsiness duration (ticks) applied per application by Fallen Thanatos. |
| `Belphegor.fallenStrikePercent` | 0.05 | Percent of target's spiritual HP dealt by Fallen Strike (unmastered). |
| `Belphegor.fallenStrikePercentMastered` | 0.07 | Percent of target's spiritual HP dealt by Fallen Strike (mastered). |
| `Belphegor.magiculeCostFallenStrike` | 10,000 | Magicule cost for Fallen Strike activation (in-slot). |
| `Belphegor.magiculeCostTrueSleepPerTick` | 10 | Magicule cost per tick while holding True Sleep. |
| `Belphegor.trueSleepHealHP` | 100 | HP healed per second while True Sleep is held (unmastered). |
| `Belphegor.trueSleepHealSHP` | 20 | Spiritual HP healed per second while True Sleep is held (unmastered). |
| `Belphegor.trueSleepHealHPMasteryPercent` | 0.1 | Additional HP percent healed per second when mastered (fraction of target's max HP). |
| `Belphegor.trueSleepHealSHPMasteryPercent` | 0.1 | Additional SHP percent healed per second when mastered (fraction of max SHP). |
| `Belphegor.trueSleepMPPerSecond` | 200 | Temporary MP gained per second while True Sleep is held. |
| `Belphegor.trueSleepAllyRadius` | 15 | Radius to affect allies when consuming stored MP. |
| `Belphegor.trueSleepAllyCostPerAlly` | 1,000 | Cost (temp MP) per ally when restoring allies. |
| `Belphegor.trueSleepAllyHealHP` | 2,000 | HP restored to each ally when consuming stored MP. |
| `Belphegor.trueSleepAllyHealSHP` | 20 | Spiritual HP restored to each ally when consuming stored MP. |
| `Belphegor.trueSleepAllyGainAP` | 2,000 | AP restored to each ally when consuming stored MP. |
| `Belphegor.trueSleepAllyGainMP` | 2,000 | MP restored to each ally when consuming stored MP. |
| `Belphegor.trueSleepCooldown` | 5 | Cooldown (skill seconds, 1 per second) applied to True Sleep on release. |
| `Belphegor.enableBelphegorEvolution` | true | Whether Belphegor evolution is allowed. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
