# Elfaria, The Hallowed Icemaiden

<small>[TensuraMoreSkills](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Elfaria, The Hallowed Icemaiden](../../../assets/icons/tensuramoreskills/skill/elfaria_the_hallowed_icemaiden.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `tensuramoreskills:elfaria_the_hallowed_icemaiden` |
| **Modes** | 5 |
| **Cooldowns (s)** | max(20, parallel body return cooldown ticks), max(20, parallel body possess cooldown ticks) |
| **Activation** | Toggle, Press, Hold |

</div>

> Finally we meet, Will.

## Modes

| # | Mode |
|---|---|
| 1 | Ars Weiss: Grand Choir |
| 2 | El Ten: Myrdas Fridoliete |
| 3 | El Two: Stellas Natea |
| 4 | El Seven: Fruzel Cardeneia |
| 5 | Glacia Last Albis |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Ars Weiss: Grand Choir | *set by config (ars weiss cost mastered mastered, ars weiss cost otherwise)* |  |
| El Ten: Myrdas Fridoliete | *set by config (riville cost mastered mastered, riville cost otherwise)* |  |
| El Two: Stellas Natea | *set by config (stellas cost mastered mastered, stellas cost otherwise)* |  |
| El Seven: Fruzel Cardeneia | *set by config (fruzel cardeneia cost mastered mastered, fruzel cardeneia cost otherwise)* |  |
| Glacia Last Albis | *set by config (glacia last albis cost mastered mastered, glacia last albis cost otherwise)* |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you die

## Related

- **Effects:** [Frost](../../../tensura-reincarnated/effects/frost.md), [Movement Interference](../../../tensura-reincarnated/effects/movement-interference.md)
- **Summons / entities:** [Ars Weiss Body](../../mobs/ars-weiss-clone.md), Tensura

## Stats (config defaults)

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## In-game messages

<details markdown><summary>Show 16 messages</summary>

- El Ten: Myrdas Fridoliete
- Stellas Natea
- El Seven: Fruzel Cardeneia
- Glacia Last Albis
- Hallowed formula connected.
- Hallowed formula released.
- No Ars Weiss body answered.
- Consciousness transferred to an Ars Weiss body.
- Consciousness returned to the main body.
- The possessed body shattered. You returned to the main body.
- The main body was destroyed. Parallel bodies collapse.
- Myrdas Fridoliete denies death and freezes the field.
- Myrdas Fridoliete cannot deny another death today.
- Hallowed cast: %s/%s
- Drop one item near an Ars Weiss clone. If it is an ore or block sample, the clone searches, mines, gathers drops, and returns them. Otherwise it gathers matching items.
- Ars Weiss bodies released.

</details>
