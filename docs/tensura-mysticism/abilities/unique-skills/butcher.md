# Butcher

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Butcher](../../../assets/icons/mysticism/skill/butcher.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:butcher` |
| **Modes** | 3 |
| **Activation** | Press |

</div>

> Slice, dice, and feel your hunger. Your thirst for the hunt is unquenching, so grab a plate and have a taste.

## Modes

| # | Mode |
|---|---|
| 1 | Heighten |
| 2 | Rupture |
| 3 | 血淋林的爱 |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Heighten | 1,500 |  |
| Rupture | 2,500 |  |
| 血淋林的爱 | 3,000 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Triggers when you damage a target

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| movementSpeed | 1 | multiply total |
| attackSpeed | 1 | multiply total |
| stepHeight | 0.5 | add |

## Related

- **Related skills:** [Infinite Regeneration](../../../tensura-reincarnated/abilities/extra-skills/infinite-regeneration.md), [Ultraspeed Regeneration](../../../tensura-reincarnated/abilities/extra-skills/ultraspeed-regeneration.md), [Survivor](../../../tensura-reincarnated/abilities/unique-skills/survivor.md)
- **Effects:** [Rupturing](../../effects/rupturing.md), [Self-Regeneration](../../../tensura-reincarnated/effects/self-regeneration.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Butcher.mpAcquirement` | 80,000 | Magicule Acquirement Cost. |
| `Butcher.heightenCost` | 1,500 | The magicule cost of the Heighten mode. |
| `Butcher.ruptureCost` | 2,500 | The magicule cost of the Rupture mode. |
| `Butcher.ruptureMarkRequirement` | 15 | The number of marks required on an entity to trigger the Rupture mode. |
| `Butcher.ruptureCooldown` | 30 | The cooldown of the Rupture mode in seconds. |
| `Butcher.ruptureCooldownMode` | true | Should the cooldown be per target or flat? TRUE for "per target", FALSE for flat cooldown. |
| `Butcher.血淋林的爱Cost` | 3,000 | The magicule cost of 血淋林的爱. |
| `Butcher.血淋林的爱Cooldown` | 120 | The cooldown of the 血淋林的爱 Art in seconds. |
| `Butcher.血淋林的爱MarkRequirement` | 20 | The number of marks required to gain a charge of the 血淋林的爱 Art. |
| `Butcher.chargesGained` | 1 | The amount of charges you gain when killing an enemy that meets the above threshold defined. |

## In-game messages

<details markdown><summary>Show 7 messages</summary>

- Arm
- Butcher
- Head
- Leg
- No body parts selected. Select one and try again.
- Too many body parts selected. Maximum of three.
- Torso

</details>

## Tags

`tensura:skills/unique_skills`
