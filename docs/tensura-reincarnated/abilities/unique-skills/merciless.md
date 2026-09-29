# Merciless

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Merciless](../../../assets/icons/tensura/skill/merciless.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:merciless` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 70,000 |
| **Activation** | Hold |

</div>

> Instantly kill weakened enemies or drain the life force of those who lack the will to fight or of those much weaker than you.

## Modes

| # | Mode |
|---|---|
| 1 | Soul Steal |
| 2 | Soul Consume |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Soul Steal | 100 |  |
| Soul Consume | 100 |  |
| other modes | 0 |  |

## How it works

- Charged or channelled by holding the skill key
- Triggers when you damage a target

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...

## Related

- **Effects:** [Soul Drain](../../effects/soul-drain.md), [Fear](../../effects/fear.md)
- **Referenced by:** [Alteration](../../../tr-nightmares/abilities/extra-skills/alteration.md), [｢ Beelzebuth, Lord of Gluttony ｣](../../../tr-nightmares/abilities/ultimate-skills/beelzebuth.md), [Beelzebuth, Lord of Gluttony](../../../elite-tensura/abilities/ultimate-skills/beelzebuth.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Merciless.mpAcquirement` | 70,000 | Magicule Acquirement Cost. |
| `Merciless.magiculeCostSteal` | 100 | Magicule Cost to activate Soul Steal. |
| `Merciless.magiculeCostConsume` | 100 | Magicule Cost to activate Soul Consume. |
| `Merciless.stealRadius` | 15 | The radius in block of the Soul Steal mode. |
| `Merciless.stealHP` | 0.1 | The multiplier of HP that the target needs to have below to be affected by the Soul Steal mode. |
| `Merciless.stealEP` | 0.1 | The multiplier of user's EP that the target needs to have below to be affected by the Soul Steal mode. |
| `Merciless.stealFear` | 5 | The level of Fear that the target needs to have to be affected by the Soul Steal mode. |
| `Merciless.drainDuration` | 100 | The duration in tick of the Soul Drain effect applied on targets with Soul Consume. |
| `Merciless.drainLevel` | 1 | The level of the Soul Drain effect applied on targets with Soul Consume. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

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
