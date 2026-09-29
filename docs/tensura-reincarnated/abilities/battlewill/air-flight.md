# Air Flight

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Air Flight](../../../assets/icons/tensura/skill/air_flight.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:air_flight` |
| **Kind** | Utility |
| **Activation** | Press, Hold |

</div>

> Use your aura to propel you forward, and hover in air.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 15 | 15 |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active

## Obtaining

- Sold by dwarf traders (high manual)
- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Related

- **Effects:** [Magic Interference](../../effects/magic-interference.md)

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `AirFlight.auraCost` | 15 | Aura Cost to activate. |
| `AirFlight.magiculeCost` | 15 | Magicule Cost to activate. |
| `AirFlight.forwardBoost` | 0.2 | The boost power of the user's forward movement when activated. |
| `AirFlight.forwardBoostMastered` | 0.4 | The boost power of the user's forward movement when activated with Mastery. |

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

`tensura:skills/battlewill`, `tensura:skills/high_manual_dwarf_trade`
