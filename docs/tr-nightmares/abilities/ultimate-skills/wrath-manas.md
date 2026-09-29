# Wrath Manas

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Wrath Manas](../../../assets/icons/trnightmare/skill/satanael.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:wrath_manas` |
| **Modes** | 2 |
| **Activation** | Hold |

</div>

## Modes

| # | Mode |
|---|---|
| 1 | Output Control |
| 2 | Reactor |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |

## How it works

- Charged or channelled by holding the skill key
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when an effect is applied to you
- Triggers when you respawn
- Does something when first learned

## Obtaining

- Acquisition checks: [｢ Satanael, Lord of Wrath ｣](satanael.md)
- In-game message: *Evolution complete: Satanael has awakened.*

## Related

- **Related skills:** [｢ Satanael, Lord of Wrath ｣](satanael.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Satanael.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Satanael.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Satanael.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Satanael.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Satanael.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Satanael.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Satanael.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Satanael.mpAcquirement` | 1,500,000 | Magicule cost required to acquire Satanael |
| `Satanael.stampedeMinLevel` | 15 | Stampede: minimum Rampage level required to prevent death |
| `Satanael.stampedeCost` | 15 | Stampede: Rampage levels consumed when death is prevented |
| `Satanael.stampedeTakeoverChance` | 0.25 | Stampede: chance of losing control and entering Berserk Takeover |
| `Satanael.stampedeTakeoverDuration` | 600 | Stampede: duration of Berserk Takeover in ticks |
| `Satanael.stampedeFriendlyFire` | true | Stampede: whether Berserk Takeover allows friendly fire |
| `Satanael.angerPointChance` | 0.15 | Anger Point: chance to gain Rampage when taking damage |
| `Satanael.angerPointMaxRampage` | 10 | Anger Point: maximum Rampage level this passive can grant |
| `Satanael.reactorMpGainBase` | 0.04 | Reactor: MP gain per activation (base) |
| `Satanael.reactorMpGainMastery` | 0.06 | Reactor: MP gain per activation (mastery) |
| `Satanael.reactorRampageChance` | 0.05 | Reactor: chance to add Rampage per activation |
| `Satanael.reactorOverflowChance` | 0.1 | Reactor: chance to add Rampage when MP exceeds natural maximum |
| `Satanael.reactorDurationBase` | 1,200 | Reactor: Rampage duration added per activation (base) |
| `Satanael.reactorDurationMastery` | 2,400 | Reactor: Rampage duration added per activation (mastery) |
| `Satanael.outputStepPercent` | 10 | Output Control: percent changed per scroll step |
| `Satanael.outputThreshold` | 90 | Output Control: threshold below which Rampage is replaced with Reactor effect |
| `Satanael.reactorArmor` | 3 | Reactor Effect: armor bonus per Rampage level |
| `Satanael.reactorAttack` | 15 | Reactor Effect: attack damage bonus per Rampage level |
| `Satanael.reactorAttackSpeed` | 0.01 | Reactor Effect: attack speed bonus per Rampage level |
| `Satanael.reactorSpeed` | 0.005 | Reactor Effect: movement speed bonus per Rampage level |
| `Satanael.reactorSwimSpeed` | 0.005 | Reactor Effect: swim speed bonus per Rampage level |
| `Satanael.reactorKnockbackResist` | 0.05 | Reactor Effect: knockback resistance per Rampage level |
| `Satanael.maxRampage` | 20 | Maximum Rampage level Satanael can reach without mastery |
| `Satanael.maxRampageMastery` | 30 | Maximum Rampage level Satanael can reach with mastery |
| `Satanael.angerPointDuration` | 200 | Duration (in ticks) of Rampage when first applied by Anger Point. |
| `Satanael.stampedeCooldown` | 300 | Cooldown (in seconds) before Stampede can trigger again. |
| `Satanael.enableUltimateEvolution` | true | Whether Satanael evolution is allowed. If false, Wrath cannot evolve into Satanael. |
| `Satanael.SatanaelHeroCount` | 20 | Wrath → Satanael: required Rampage level |
| `Satanael.satanaelHP` | 40 | Wrath → Satanael: HP percent threshold (e.g., 40 = below 40%) |
| `Satanael.satanaelMobKills` | 500 | Wrath → Satanael: required mob kills |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
