# Gardener

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Gardener](../../../assets/icons/mysticism/skill/gardener.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:gardener` |
| **Modes** | 3 |
| **Cooldowns (s)** | 1 mastered, 3 otherwise, 300 |
| **Activation** | Press |

</div>

> The crops, the wild, everything was there for you. You sow the seeds and wish only for a bountiful harvest. And in turn, the crops bless you.

## Modes

| # | Mode |
|---|---|
| 1 | Blessing |
| 2 | Overgrow |
| 3 | Entwine |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Gardener.mpAcquirement` | 40,000 | Magicule Acquirement Cost. |
| `Gardener.cropMasteryCost` | 100 | The magicules taken every 5 seconds for the Crop Mastery passive. |
| `Gardener.cropMasteryChance` | 50 | The chance for a crop to grow to the next stage every 5 seconds when Crop Mastery is triggered. |
| `Gardener.cropMasteryChanceHipokute` | 10 | The chance for a Hipokute plant to grow to the next stage every 5 seconds when Crop Mastery is triggered. |
| `Gardener.cropMasteryChanceMastered` | 75 | The chance for a crop to grow to the next stage every 5 seconds when Crop Mastery is triggered. |
| `Gardener.cropMasteryChanceHipokuteMastered` | 20 | The chance for a Hipokute plant to grow to the next stage every 5 seconds when Crop Mastery is triggered. |
| `Gardener.overgrowCropRequirement` | 25 | The amount of crops you need to grow to gain a charge for Overgrow. |
| `Gardener.blessingCost` | 250 | The magicule cost of the Blessing mode, for each item in the stack (blessingCost \* stack amount = MP cost). |
| `Gardener.blessingCostMastered` | 500 | The magicule cost of the Blessing mode when the skill is mastered, for each item in the stack (blessingCostMastered \* stack amount = MP cost). |
| `Gardener.blessingCooldown` | 3 | The cooldown of the Blessing mode in seconds. |
| `Gardener.blessingCooldownMastered` | 1 | The cooldown of the Blessing mode in seconds when the skill is mastered. |
| `Gardener.dawnBlessingEffect` | "tensura:strengthen" | The effect granted to the food stack when Blessing is used at dawn. |
| `Gardener.dawnEffectLevel` | 3 | The effect level granted to the consumer of the food stack when Blessing is used at dawn. |
| `Gardener.dawnDuration` | 3,600 | The duration of the effect granted to the consumer of the food stack when Blessing is used at dawn. |
| `Gardener.dawnEffectLevelMastered` | 5 | The effect level granted to the consumer of the food stack when Blessing is used at dawn when Gardener is mastered. |
| `Gardener.dawnDurationMastered` | 6,000 | The duration of the effect granted to the consumer of the food stack when Blessing is used at dawn when Gardener is mastered. |
| `Gardener.noonBlessingEffect` | "minecraft:resistance" | The effect granted to the food stack when Blessing is used at noon. |
| `Gardener.noonEffectLevel` | 1 | The effect level granted to the consumer of the food stack when Blessing is used at noon. |
| `Gardener.noonDuration` | 3,600 | The duration of the effect granted to the consumer of the food stack when Blessing is used at noon. |
| `Gardener.noonEffectLevelMastered` | 2 | The effect level granted to the consumer of the food stack when Blessing is used at noon when Gardener is mastered. |
| `Gardener.noonDurationMastered` | 3,600 | The duration of the effect granted to the consumer of the food stack when Blessing is used at noon when Gardener is mastered. |
| `Gardener.nightBlessingEffect` | "minecraft:speed" | The effect granted to the food stack when Blessing is used at night. |
| `Gardener.nightEffectLevel` | 3 | The effect level granted to the consumer of the food stack when Blessing is used at night. |
| `Gardener.nightDuration` | 3,600 | The duration of the effect granted to the consumer of the food stack when Blessing is used at night. |
| `Gardener.nightEffectLevelMastered` | 5 | The effect level granted to the consumer of the food stack when Blessing is used at night when Gardener is mastered. |
| `Gardener.nightDurationMastered` | 6,000 | The duration of the effect granted to the consumer of the food stack when Blessing is used at night when Gardener is mastered. |
| `Gardener.overgrowCooldown` | 300 | The cooldown of the Overgrow mode in seconds. |
| `Gardener.overgrowDuration` | 500 | The duration that Overgrow lasts for, in ticks (seconds x 20). |

## Tags

`tensura:skills/unique_skills`
