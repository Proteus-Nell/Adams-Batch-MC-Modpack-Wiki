# Engineer

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Engineer](../../../assets/icons/mysticism/skill/engineer.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:engineer` |
| **Modes** | 2 |
| **Cooldowns (s)** | 15 mastered, 30 otherwise, 15 mastered, 25 otherwise |
| **Activation** | Press, Hold |

</div>

> Tinkering and tinkering. No one understood the machines as much as you did. In fact, no one understood you either. Perhaps it was always meant to be.

## Modes

| # | Mode |
|---|---|
| 1 | Build |
| 2 | Bubble Shield |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |
| Always | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Adjusted by scrolling while active

## Related

- **Summons / entities:** [Sentry](../../mobs/sentry.md), [Dispenser](../../mobs/dispenser.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Engineer.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Engineer.buildSentryCost` | 500 | The magicule cost of the Build mode when placing a Sentry. |
| `Engineer.buildSentryCostMastered` | 500 | The magicule cost of the Build mode when placing a Sentry, when the skill is mastered. |
| `Engineer.sentryLevel1FireRate` | 10 | The fire rate of a Level 1 Sentry. |
| `Engineer.sentryLevel2LevelUpTime` | 2,400 | The time taken (in ticks) for a Level 1 Sentry to evolve to Level 2. |
| `Engineer.sentryLevel2FireRate` | 5 | The fire rate of a Level 2 Sentry. |
| `Engineer.sentryLevel3LevelUpTime` | 6,000 | The time taken (in ticks) for a Level 2 Sentry to evolve to Level 3. |
| `Engineer.sentryLevel3FireRate` | 10 | The fire rate of a Level 3 Sentry. |
| `Engineer.buildDispenserCost` | 500 | The magicule cost of the Build mode when placing a Dispenser. |
| `Engineer.buildDispenserCostMastered` | 500 | The magicule cost of the Build mode when placing a Dispenser, when the skill is mastered. |
| `Engineer.buildCooldown` | 30 | The cooldown of the Build mode in seconds. |
| `Engineer.buildCooldownMastered` | 15 | The cooldown of the Build mode in seconds, when the skill is mastered. |
| `Engineer.bubbleShieldCost` | 1,000 | The magicule cost of the Bubble Shield mode. |
| `Engineer.bubbleShieldCostMastered` | 1,000 | The magicule cost of the Bubble Shield mode when the skill is mastered. |
| `Engineer.bubbleShieldShouldHurt` | false | Should the Bubble Shield be able to be destroyed from within? ("true" = yes/"false" = no) |
| `Engineer.bubbleShieldSize` | 7 | The size of the Bubble Shield in radius. Decimal values will crash your game. |
| `Engineer.bubbleShieldCooldown` | 25 | The cooldown in seconds of the Bubble Shield mode. |
| `Engineer.bubbleShieldCooldownMastered` | 15 | The cooldown in seconds of the Bubble Shield mode when the skill is mastered. |
| `Engineer.bubbleShieldLifespan` | 300 | The lifespan of the Bubble Shield, in ticks (seconds x 20. 600 = 30 seconds). |
| `Engineer.bubbleShieldLifespanMastered` | 600 | The lifespan of the Bubble Shield when the skill is mastered, in ticks (seconds x 20. 600 = 30 seconds). |
| `Engineer.percentageDispenserEPRegenLevel1` | 0.5 | The percentage of EP regenerated to a Dipsenser's allies when it's activated when it is level one. |
| `Engineer.percentageDispenserEPRegenLevel2` | 1 | The percentage of EP regenerated to a Dipsenser's allies when it's activated when it is level two. |
| `Engineer.percentageDispenserEPRegenLevel3` | 3 | The percentage of EP regenerated to a Dipsenser's allies when it's activated when it is level three. |
| `Engineer.healthDispenserRegenLevel2` | 10 | The amount of HP regenerated to a Dipsenser's allies when it's activated when it is level two. |
| `Engineer.healthDispenserRegenLevel3` | 5 | The percentage of HP regenerated to a Dipsenser's allies when it's activated when it is level three. |
| `Engineer.foodDispenserRegenLevel1` | 1 | The amount of food regenerated to a Dipsenser's allies when it's activated when it is level one. |
| `Engineer.foodDispenserRegenLevel2` | 2 | The amount of food regenerated to a Dipsenser's allies when it's activated when it is level two. |
| `Engineer.foodDispenserRegenLevel3` | 3 | The amount of food regenerated to a Dipsenser's allies when it's activated when it is level three. |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- Your dispenser has reached Level %s!
- Your turret has reached Level %s!

</details>
