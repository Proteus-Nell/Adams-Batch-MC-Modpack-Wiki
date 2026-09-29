# ｢ Yog-Sothoth, Lord of Space-Time ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:yog_sothoth` |
| **Modes** | 8 |
| **Acquisition cost (MP)** | 1,101,000 |
| **Max mastery** | 25,000 |
| **Cooldowns (s)** | 10, 3, 20, 180, 120 |
| **Activation** | Toggle, Press |

</div>

> Ultimate spacetime lord — coating, usurpation, prison, and time itself.

## Modes

| # | Mode |
|---|---|
| 1 | Rob |
| 2 | Copy |
| 3 | Takeover |
| 4 | Absolute End |
| 5 | Infinity Prison |
| 6 | Time Leap |
| 7 | Reverse Fate |
| 8 | Time Stop |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers on melee contact
- Triggers when you die
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| atk | bonus | add |

## Obtaining

- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.
- Acquisition checks: [Time Traveler](../unique-skills/time-traveler.md), [｢ Yog-Sothoth, Lord of Space-Time ｣](yog-sothoth.md), [Usurper](../../../tensura-reincarnated/abilities/unique-skills/usurper.md), [Infinity Prison](../../../tensura-reincarnated/abilities/unique-skills/infinity-prison.md), [Absolute Severance](../../../tensura-reincarnated/abilities/unique-skills/absolute-severance.md)
- In-game message: *The Unique Skill Time Traveler has evolved into the Ultimate Skill Yog-Sothoth, Lord of Spacetime.*

## Related

- **Related skills:** [Time Traveler](../unique-skills/time-traveler.md), [Usurper](../../../tensura-reincarnated/abilities/unique-skills/usurper.md), [Infinity Prison](../../../tensura-reincarnated/abilities/unique-skills/infinity-prison.md), [Absolute Severance](../../../tensura-reincarnated/abilities/unique-skills/absolute-severance.md), [Chosen One](../../../tensura-reincarnated/abilities/unique-skills/chosen-one.md), [｢ True Hero, King of Champions ｣](true-hero.md), [Hero Haki](../../../tensura-reincarnated/abilities/extra-skills/hero-haki.md), [Dominator](../unique-skills/dominator.md), [｢ Michael, Lord of Justice ｣](michael.md), [Unyielding](../../../tensura-reincarnated/abilities/unique-skills/unyielding.md), [｢ Sariel, Lord of Hope ｣](sariel.md)
- **Effects:** [Mind Control](../../../tensura-reincarnated/effects/mind-control.md), [Infinite Imprisonment](../../../tensura-reincarnated/effects/infinite-imprisonment.md), [Magic Interference](../../../tensura-reincarnated/effects/magic-interference.md), [Anti-Skill](../../../tensura-reincarnated/effects/anti-skill.md), [Severance Blade](../../../tensura-reincarnated/effects/severance-blade.md)
- **Summons / entities:** Severance Cutter
- **Referenced by:** [Witch's Greed](../unique-skills/witches-greed.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Usurper.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Usurper.magiculeCostRob` | 1,000 | Magicule Cost to activate Rob. |
| `Usurper.magiculeCostCopy` | 1,000 | Magicule Cost to activate Copy. |
| `Usurper.magiculeCostTakeover` | 5,000 | Magicule Cost to activate Force Takeover. |
| `Usurper.epDrain` | 0.01 | The multiplier of the target's EP to drain when attacked by the user. |
| `Usurper.robSuccess` | 25 | The percentage chance to rob successfully. |
| `Usurper.robSuccessMastered` | 50 | The percentage chance to rob successfully when mastered. |
| `Usurper.robMastery` | 0.5 | The multiplier of max mastery that the robbed skill gains. |
| `Usurper.robCooldown` | 10 | The cooldown in second of the Rob mode. |
| `Usurper.copySuccess` | 25 | The percentage chance to copy successfully. |
| `Usurper.copySuccessMastered` | 50 | The percentage chance to copy successfully when mastered. |
| `Usurper.copyMastery` | 0.5 | The multiplier of max mastery that the copied skill gains. |
| `Usurper.copyCooldown` | 10 | The cooldown in second of the Copy mode. |
| `Usurper.takeoverEP` | 0.75 | The multiplier of the user's EP that the targeted spirit's owner needs to be higher to not be affected by Takeover. |
| `Usurper.takeoverDuration` | 6,000 | The duration in tick of the Takeover effect on the controlled spirit (-1 = permanent). |
| `Usurper.takeoverDurationMastered` | 12,000 | The duration in tick of the Takeover effect on the controlled spirit when mastered (-1 = permanent). |
| `Usurper.takeoverCooldown` | 10 | The cooldown in second of the Force Takeover mode. |

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `YogSothoth.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `YogSothoth.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `YogSothoth.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `YogSothoth.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `YogSothoth.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `YogSothoth.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `YogSothoth.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `YogSothoth.mpAcquirement` | 1,101,000 | Magicule cost to acquire Yog-Sothoth. |
| `YogSothoth.maxMastery` | 25,000 | Max mastery. |
| `YogSothoth.timeTravelerActivationMin` | 25 | Minimum Time Traveler toggle activations required (&gt; this value). |
| `YogSothoth.enableUltimateEvolution` | true | Whether Yog-Sothoth evolution is allowed. If false, Time Traveler cannot evolve into Yog-Sothoth. |
| `YogSothoth.coatingDamage` | 200 | Absolute Coating attack damage bonus. |
| `YogSothoth.coatingDamageMastered` | 250 | Absolute Coating attack damage bonus when mastered. |
| `YogSothoth.coatingAmplifier` | 1 | Severance Blade amplifier (effect level = value - 1). |
| `YogSothoth.coatingAmplifierMastered` | 1 | Severance Blade amplifier when mastered. |
| `YogSothoth.seizeMpFraction` | 0.015 | Seize: fraction of target max MP stolen per proc (0.015 = 1.5%). Uses percentage drain like Usurper. |
| `YogSothoth.absoluteEndDamage` | 300 | Absolute End damage. |
| `YogSothoth.absoluteEndDamageMastered` | 400 | Absolute End damage when mastered. |
| `YogSothoth.absoluteEndSize` | 8 | Absolute End projectile size. |
| `YogSothoth.absoluteEndSizeMastered` | 12 | Absolute End projectile size when mastered. |
| `YogSothoth.absoluteEndCooldown` | 3 | Absolute End cooldown (seconds). |
| `YogSothoth.imprisonBaseCost` | 150,000 | Infinity Prison base MP cost. |
| `YogSothoth.imprisonTargetEpFraction` | 0.1 | Infinity Prison additional cost as fraction of target EP. |
| `YogSothoth.imprisonRange` | 16 | Infinity Prison range. |
| `YogSothoth.imprisonDuration` | 300 | Infinity Prison duration (seconds). |
| `YogSothoth.imprisonDurationMastered` | 600 | Infinity Prison duration when mastered (seconds). |
| `YogSothoth.imprisonCooldown` | 20 | Infinity Prison cooldown (seconds). |
| `YogSothoth.imprisonMissCooldown` | 20 | Infinity Prison miss cooldown (seconds). |
| `YogSothoth.imprisonMissCooldownMastered` | 10 | Infinity Prison miss cooldown when mastered (seconds). |
| `YogSothoth.imprisonDrainPerPulse` | 100 | MP drained from imprisoned targets per prison tick pulse. |
| `YogSothoth.timeLeapDeathHealHpFraction` | 0.1 | Time Leap death rewind HP fraction healed. |
| `YogSothoth.timeLeapDeathCooldownSeconds` | 500 | Cooldown applied to all modes after Time Leap death rewind (seconds). |
| `YogSothoth.reverseFateLearnPoints` | 500 | Reverse Fate learn points. |
| `YogSothoth.reverseFateRadius` | 60 | Reverse Fate radius. |
| `YogSothoth.reverseFateCooldownSeconds` | 180 | Reverse Fate cooldown after rewind (seconds). |
| `YogSothoth.timeStopLearnPoints` | 100 | Time Stop learn points. |
| `YogSothoth.timeStopDurationTicks` | 200 | Time Stop duration ticks (10s = 200). |
| `YogSothoth.timeStopDurationTicksMastered` | 300 | Time Stop duration ticks when mastered (15s = 300). |
| `YogSothoth.timeStopMagiculeCost` | 950,000 | Time Stop MP cost. |
| `YogSothoth.timeStopCooldownSeconds` | 120 | Time Stop cooldown (seconds). |

## In-game messages

<details markdown><summary>Show 15 messages</summary>

- Rob
- Copy
- Force Takeover
- Absolute End
- Infinity Prison
- Time Leap
- Reverse Fate
- Time Stop
- Time Leap anchor set.
- Time Leap is still on cooldown.
- Time Leap — you return from death.
- Data of %s has been obtained.
- Data of Courage has been obtained.
- Data of Justice has been obtained.
- Data of Hope has been obtained.

</details>

## Tags

`tensura:skills/no_plundering`, `tensura:skills/ultimate_skills`
