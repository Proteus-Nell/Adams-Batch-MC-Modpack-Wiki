# Gravity Flight

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

![Gravity Flight](../../../assets/icons/tensura/skill/gravity_flight.png)

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `tensura:gravity_flight` |
| **Activation** | Hold |

</div>

> Manipulate gravity to allow flight, your momentum from before will be continued.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5 |  |

## How it works

- Charged or channelled by holding the skill key

## Obtaining

- Can be learned by: [Angel](../../../ascension/races/angel.md), [Archangel](../../../ascension/races/archangel.md), [Seraphim](../../../ascension/races/seraphim.md), [Divine Angel](../../../ascension/races/divine-angel.md), [Fallen Angel](../../../ascension/races/fallen-angel.md), [Cosmic Deity](../../../ascension/races/cosmic-deity.md), [Chaotic Deity](../../../ascension/races/chaotic-deity.md)
- Innate to mobs: [Charybdis](../../mobs/charybdis.md)

## Related

- **Effects:** [Magic Interference](../../effects/magic-interference.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/common_config.toml`](../../configs/config-tensura-ability-skill-common-config.md).

| Option | Default | Description |
|---|---|---|
| `GravityFlight.epAcquirement` | 10,000 | EP Requirement for Learning. |
| `GravityFlight.magiculeCost` | 5 | Magicule Cost to activate. |
| `GravityFlight.upMultiplier` | 1 | The multiplier of the going-up speed when hold down. |

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

`tensura:skills/common_skills`, `tensura:skills/gravity_skills`
