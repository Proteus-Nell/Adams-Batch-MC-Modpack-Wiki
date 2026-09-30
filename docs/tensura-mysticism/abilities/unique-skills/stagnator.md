# Stagnator

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Stagnator](../../../assets/icons/mysticism/skill/stagnator.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:stagnator` |
| **Modes** | 4 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise, 10 |
| **Activation** | Press, Hold |

</div>

> Cease all change. The times call for it. Prevent targets from moving or regenerating, and stop all things from harming you.

## Modes

| # | Mode |
|---|---|
| 1 | Stagnate Aura |
| 2 | Inaction |
| 3 | Stasis Coat |
| 4 | Stasis Shot |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Stagnate Aura | 250 |  |
| Inaction | 50 |  |
| other modes | 0 |  |
| Stasis Shot | 1,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you take damage

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -1 | multiply total |
| Flying Speed | -1 | multiply total |
| Attack Damage | -1 | multiply total |
| Attack Speed | -1 | multiply total |
| Jump Strength | -1 | multiply total |
| Block Interaction Range | -1 | multiply total |
| Follow Range | -1 | multiply total |
| Swim Speed Multiplier | -1 | multiply total |

## Related

- **Effects:** [Stagnate](../../effects/stagnate.md), [Silence](../../../tensura-reincarnated/effects/silence.md), [Severance Blade](../../../tensura-reincarnated/effects/severance-blade.md)
- **Summons / entities:** Stasis Shot

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Stagnator.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Stagnator.stagnateAuraCost` | 250 | The magicule cost of the Stagnate Aura mode, taken every 10 ticks. |
| `Stagnator.stagnateAuraRadius` | 25 | The radius in blocks of the Stagnate Aura mode. |
| `Stagnator.stagnateAuraCooldown` | 5 | The cooldown of the Stagnate Aura mode in seconds. |
| `Stagnator.stagnateAuraCooldownMastered` | 3 | The cooldown of the Stagnate Aura mode in seconds, when the skill is mastered. |
| `Stagnator.inactionCost` | 50 | The Magicule cost of the Inaction mode, taken every 10 ticks. |
| `Stagnator.inactionCooldown` | 5 | The cooldown of the Inaction mode in seconds. |
| `Stagnator.inactionCooldownMastered` | 3 | The cooldown of the Inaction mode in seconds, when the skill is mastered. |
| `Stagnator.stasisShotCost` | 1,000 | The Magicule Cost of the Stasis Shot mode. |
| `Stagnator.stasisShotDamage` | 50 | The Damage of Stasis Shot projectile. |
| `Stagnator.stasisShotMasteredDamage` | 100 | The Damage of Stasis Shot Projectile when Mastered |
| `Stagnator.stasisShotCooldown` | 10 | The cooldown of Stasis Shot Mode in seconds. |
| `Stagnator.stasisShotCooldownMastered` | 5 | The cooldown of Stasis Shot Mode in seconds, when the skill is mastered. |

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
