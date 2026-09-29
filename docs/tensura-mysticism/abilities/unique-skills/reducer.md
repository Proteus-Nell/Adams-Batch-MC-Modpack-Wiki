# Reducer

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Reducer](../../../assets/icons/mysticism/skill/reducer.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:reducer` |
| **Modes** | 2 |
| **Activation** | Toggle, Press |

</div>

> Manipulate and wield the power of energy itself, being able to channel the power of the holy element into super strong attacks.

## Modes

| # | Mode |
|---|---|
| 1 | Emancipation |
| 2 | Purity Edge |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Emancipation | 2,000 |  |
| Purity Edge | 10,000 |  |
| other modes | 2,000 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Triggers when you respawn
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| mpRegen | 9 | add |
| apRegen | 9 | add |

## Related

- **Effects:** [Emancipation](../../effects/reducer-holy-coat.md), [Purity Edge](../../effects/reducer-purity-edge.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Reducer.mpAcquisition` | 90,000 | Magicule Acquirement Cost. |
| `Reducer.purificationReduction` | 0.5 | The percentage of energy cost reduction you receive when Reducer is toggled on. |
| `Reducer.purificationReductionMastered` | 0.33 | The percentage of energy cost reduction you receive when Reducer is toggled on, when the skill is mastered. |
| `Reducer.magiculeRegenerationMultiplierBuff` | 9 | The ADDITIONAL multiplier (base 1) of magicule regeneration you receive when Reducer is in slot. |
| `Reducer.auraRegenerationMultiplierBuff` | 9 | The ADDITIONAL multiplier (base 1) of aura regeneration you receive when Reducer is in slot. |
| `Reducer.emancipationCost` | 2,000 | The magicule cost to toggle on the Emancipation mode. |
| `Reducer.emancipationMaintainCost` | 300 | The magicule cost to maintain the Emancipation mode. |
| `Reducer.emancipationMultiplier` | 1.75 | The multiplier of Holy Damage the user will deal when Emancipation is toggled on. |
| `Reducer.purityEdgeCost` | 10,000 | The magicule cost of the Purity Edge mode. |
| `Reducer.purityEdgeDamagePercentage` | 0.25 | The percentage of health that will be drained from the target on connecting with Purity Edge. |
| `Reducer.purityEdgeDamagePercentageMastered` | 0.5 | The percentage of health that will be drained from the target on connecting with Purity Edge when the skill is mastered. |
| `Reducer.purityEdgeRecoilTime` | 60 | The time you have to connect a hit before suffering the recoil damage in ticks. |
| `Reducer.purityEdgeRecoilTimeMastered` | 100 | The time you have to connect a hit before suffering the recoil damage in ticks when the skill is mastered. |
| `Reducer.purityEdgeCooldown` | 120 | The cooldown of the Purity Edge mode in seconds. |
| `Reducer.purityEdgeCooldownMastered` | 60 | The cooldown of the Purity Edge mode in seconds when the skill is mastered. |
| `Reducer.purityEdgeRecoil` | 0.75 | The recoil of the Purity Edge mode if you do not land a hit in time. |
| `Reducer.purityEdgeRecoilMastered` | 0.25 | The recoil of the Purity Edge mode if you do not land a hit in time when the skill is mastered. |

## Tags

`tensura:skills/unique_skills`, `tensura:skills/virtue_skills`
