# Dreamer

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Dreamer](../../../assets/icons/mysticism/skill/dreamer.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:dreamer` |
| **Modes** | 3 |
| **Activation** | Press, Hold |

</div>

> Dream a dream so grand it becomes a nightmare... Gain control over the forces of life and death, allowing you to cheat death and restore yourself back to a "save point".

## Modes

| # | Mode |
|---|---|
| 1 | Dream |
| 2 | Hypnosis |
| 3 | Dream Eater |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Dream |  |  |
| Hypnosis | 150 |  |
| Dream Eater | 300 |  |
| other modes | 500 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you die

## Related

- **Effects:** [Drowsiness](../../../tensura-reincarnated/effects/drowsiness.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Dreamer.mpAcquirement` | 60,000 | Magicule Acquirement Cost. |
| `Dreamer.magiculeRecovery` | 0.5 | The percentage of magicules that will be recovered every 5 seconds. |
| `Dreamer.magiculeRecoveryMastered` | 1 | The percentage of magicules that will be recovered every 5 seconds when the skill is mastered. |
| `Dreamer.drainMode` | false | The draining mode of magicules when the Dream mode is used. FALSE for percentage cost. TRUE for flat cost. |
| `Dreamer.dreamSetPercentageCost` | 25 | The percentage of magicules that will be drained from the user to set a dream, IF drainMode above is set to false. |
| `Dreamer.dreamSetFlatCost` | 750 | The flat cost of magicules that will be drained from the user to set a dream, IF drainMode above is set to true. |
| `Dreamer.dreamActivateCost` | 0 | The amount of magicules used when a dream is activated. |
| `Dreamer.hypnosisCost` | 150 | The amount of magicules that the Hypnosis mode drains every second it is active. |
| `Dreamer.dreamEaterCost` | 300 | The amount of magicules that the Dream Eater mode drains when it is used. |
| `Dreamer.dreamCooldown` | 300 | The cooldown of the Dream mode after it has been activated. |
| `Dreamer.dreamCooldownMastered` | 120 | The cooldown of the Dream mode after it has been activated, when the skill is mastered. |
| `Dreamer.hypnosisRadius` | 10 | The radius of the Hypnosis mode in blocks. |
| `Dreamer.hypnosisRadiusMastered` | 15 | The radius of the Hypnosis mode in blocks when the skill is mastered. |
| `Dreamer.hypnosisDuration` | 200 | The duration of the Drowsiness effect in ticks (seconds x 20). |
| `Dreamer.hypnosisDurationMastered` | 300 | The duration of the Drowsiness effect in ticks when the skill is mastered (seconds x 20). |
| `Dreamer.hypnosisLevel` | 1 | The effect level of the Drowsiness effect when applied by Hypnosis. |
| `Dreamer.hypnosisLevelMastered` | 2 | The effect level of the Drowsiness effect when applied by Hypnosis when the skill is mastered. |
| `Dreamer.dreamEaterRange` | 15 | The range of the Dream Eater mode in blocks. |
| `Dreamer.dreamEaterRangeMastered` | 20 | The range of the Dream Eater mode in blocks when the skill is mastered. |
| `Dreamer.dreamEaterDamage` | 30 | The range of the Dream Eater mode in blocks. |
| `Dreamer.dreamEaterDamageMastered` | 50 | The range of the Dream Eater mode in blocks when the skill is mastered. |
| `Dreamer.dreamEaterSpiritualDamage` | 30 | The range of the Dream Eater mode in blocks. |
| `Dreamer.dreamEaterSpiritualDamageMastered` | 50 | The range of the Dream Eater mode in blocks when the skill is mastered. |
| `Dreamer.dreamEaterDreamCooldownReduction` | 15 | The number of seconds that Dream Eater reduces the cooldown of Dream by. |
| `Dreamer.dreamEaterDreamCooldownReductionMastered` | 15 | The number of seconds that Dream Eater reduces the cooldown of Dream by when the skill is mastered. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/unique_skills`
