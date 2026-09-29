# Corroder

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Corroder](../../../assets/icons/mysticism/skill/corroder.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:corroder` |
| **Modes** | 2 |
| **Cooldowns (s)** | 15 mastered, 20 otherwise |
| **Activation** | Press, Hold |

</div>

> Apply powerful Corrosion to your physical attacks. Turn into Corrosion and sear your enemies. Deal massive armor-ignoring damage with a Corrosion slash.

## Modes

| # | Mode |
|---|---|
| 1 | Dissolve |
| 2 | Cross Corrosion |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Dissolve | 100 |  |
| Cross Corrosion | 1,000 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when you damage a target
- Triggers on melee contact
- Triggers when an effect is applied to you

## Related

- **Effects:** [Corrosion](../../../tensura-reincarnated/effects/corrosion.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Corroder.mpAcquirement` | 25,000 | Magicule Acquirement Cost. |
| `Corroder.meleeCorrosionLevel` | 2 | The level of Corrosion you apply when performing a melee attack when the skill is in slot. |
| `Corroder.meleeCorrosionLevelMastered` | 3 | The level of Corrosion you apply when performing a melee attack when the skill is mastered and in slot. |
| `Corroder.meleeCorrosionDuration` | 200 | The amount of time in ticks of the the Corrosion effect when performing a melee attack when the skill is in slot. (Take seconds times 20.) |
| `Corroder.meleeCorrosionDurationMastered` | 300 | The amount of time in ticks of the Corrosion effect when performing a melee attack when the skill is mastered and in slot. (Take seconds times 20.) |
| `Corroder.dissolveCost` | 100 | The magicule cost of the Dissolve mode, taken every 10 ticks. |
| `Corroder.dissolveRadius` | 10 | The radius of your corrosion damage from the Dissolve mode. |
| `Corroder.dissolveRadiusMastered` | 15 | The radius of your corrosion damage from the Dissolve mode when the skill is mastered. |
| `Corroder.dissolveDamage` | 10 | The damage of your corrosion from the Dissolve mode. |
| `Corroder.dissolveDamageMastered` | 15 | The damage of your corrosion from the Dissolve mode when the skill is mastered. |
| `Corroder.dissolveCorrosionLevel` | 1 | The level of Corrosion you apply from the Dissolve mode. |
| `Corroder.dissolveCorrosionLevelMastered` | 2 | The level of Corrosion you apply from the Dissolve mode. |
| `Corroder.dissolveCorrosionDuration` | 200 | The amount of time in ticks of the Corrosion effect from the Dissolve mode. (Take seconds times 20.) |
| `Corroder.dissolveCorrosionDurationMastered` | 300 | The amount of time in ticks of the Corrosion effect from the Dissolve mode when the skill is mastered. (Take seconds times 20.) |
| `Corroder.crossCorrosionCost` | 1,000 | The magicule cost of the Cross Corrosion mode. |
| `Corroder.crossCorrosionMultiplier` | 2 | The damage multiplier of your next attack when Cross Corrosion is used. |
| `Corroder.crossCorrosionCooldown` | 20 | The cooldown of Cross Corrosion in seconds. |
| `Corroder.crossCorrosionCooldownMastered` | 15 | The cooldown of Cross Corrosion in seconds when the skill is mastered. |

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
