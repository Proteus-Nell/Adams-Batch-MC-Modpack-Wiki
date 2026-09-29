# Victorious Harbinger

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Victorious Harbinger](../../../assets/icons/mysticism/skill/victorious_harbinger.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:victorious_harbinger` |
| **Modes** | 2 |
| **Cooldowns (s)** | 60, 40 |
| **Activation** | Toggle, Press, Hold |

</div>

> You are the forerunner of victory, your presence declares near fated victory, shatter the morale of your enemies and have no doubt in your abilities.

## Modes

| # | Mode |
|---|---|
| 1 | Might |
| 2 | Tenacious Resolve |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Might | 2,000 |  |
| Tenacious Resolve | 500 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when an effect is applied to you

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| relentlessBarrage | 0.1 | add x base |

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `VictoriousHarbinger.mpAcquirement` | 80,000 | Magicule Acquirement Cost. |
| `VictoriousHarbinger.mightCost` | 2,000 | The magicule cost of the Might mode, taken every 10 ticks. |
| `VictoriousHarbinger.mightCooldown` | 40 | The Cooldown of the Might mode |
| `VictoriousHarbinger.tenaciousResolveCost` | 500 | The Magicule cost of the Tenacious Resolve mode |
| `VictoriousHarbinger.effectLevel` | 1 | The Level of effect to reduce by |
| `VictoriousHarbinger.immunityList` | "new ArrayList&lt;&gt;()" | List of effects the holder of this skill is immune to |

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
