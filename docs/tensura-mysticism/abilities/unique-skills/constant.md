# Constant

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Constant](../../../assets/icons/mysticism/skill/constant.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:constant` |
| **Modes** | 4 |
| **Cooldowns (s)** | 10, 120, 15, 20 |
| **Activation** | Press, Hold |

</div>

> Use magicules to force differing stats to remain the same. Become nigh invincible for a short period of time while

## Modes

| # | Mode |
|---|---|
| 1 | Constant: Health |
| 2 | Constant: Physical |
| 3 | Constant: Destruction |
| 4 | Constant: Energy |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Constant: Health | 1,000 |  |
| Constant: Physical | 0 |  |
| Constant: Destruction | 3,000 |  |
| Constant: Energy | 1,000 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you damage a target
- Triggers when you are attacked
- Does something when first learned

## Related

- **Effects:** [Constant: Health](../../effects/constant-health.md), [Constant: Destruction](../../effects/constant-destruction.md), [Constant: Energy](../../effects/constant-energy.md), [Constant: Energy Debuff](../../effects/constant-energy-debuff.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Constant.mpAcquirement` | 40,000 | Magicule Acquirement Cost. |
| `Constant.constantHealthCost` | 1,000 | Magicule cost of the Constant: Health mode. |
| `Constant.constantHealthTickCost` | 1,000 | Magicule cost of the Constant: Health mode that drains every second (20 ticks). |
| `Constant.constantHealthHeldTicks` | 300 | The maximum amount of time in ticks (multiply seconds by 20) that you can hold down Constant: Health for. |
| `Constant.constantHealthHeldTicksMastered` | 300 | The maximum amount of time in ticks (multiply seconds by 20) that you can hold down Constant: Health for when the skill is mastered. |
| `Constant.constantHealthCooldown` | 15 | The cooldown of the Constant: Health mode. |
| `Constant.constantHealthCooldownMastered` | 15 | The cooldown of the Constant: Health mode when the skill is mastered. |
| `Constant.constantPhysicalCost` | 0 | Magicule cost of the Constant: Physical mode. |
| `Constant.constantPhysicalTimer` | 100 | How long should the timer for Constant: Physical run for in ticks. |
| `Constant.constantPhysicalCooldown` | 10 | The cooldown of the Constant: Physical mode. |
| `Constant.constantPhysicalCooldownMastered` | 10 | The cooldown of the Constant: Physical mode. |
| `Constant.constantDestructionCost` | 3,000 | Magicule cost of the Constant: Destruction mode. |
| `Constant.constantDestructionHeldTicks` | 200 | The maximum amount of time in ticks (multiply seconds by 20) that you can hold down Constant: Destruction for. |
| `Constant.constantDestructionHeldTicksMastered` | 200 | The maximum amount of time in ticks (multiply seconds by 20) that you can hold down Constant: Destruction for when the skill is mastered. |
| `Constant.constantDestructionMaxDamage` | 5,000 | The maximum damage that Constant: Destruction can have. (Default: 5000) |
| `Constant.constantDestructionCooldown` | 20 | The cooldown of the Constant: Destruction mode. |
| `Constant.constantDestructionCooldownMastered` | 20 | The cooldown of the Constant: Destruction mode when the skill is mastered. |
| `Constant.constantEnergyCost` | 1,000 | Magicule cost of the Constant: Energy mode. |
| `Constant.constantEnergyDuration` | 10 | The duration, in seconds, of the Constant: Energy effect. |
| `Constant.constantEnergyDebuffDuration` | 180 | The duration, in seconds, of the debuff of the Constant: Energy effect. |
| `Constant.constantEnergyCooldown` | 120 | The cooldown of the Constant: Energy mode. |

## Tags

`tensura:skills/unique_skills`
