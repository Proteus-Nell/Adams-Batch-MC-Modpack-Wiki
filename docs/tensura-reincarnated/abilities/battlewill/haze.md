# Haze

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Haze](../../../assets/icons/tensura/skill/haze.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:haze` |
| **Kind** | Utility |
| **Activation** | Toggle, Press, Hold |

</div>

> Wrap yourself in a cloak of aura concealing yourself from even the most heightened of senses.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 20 |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Acquisition checks: [Formhide](formhide.md)

## Related

- **Related skills:** [Formhide](formhide.md)
- **Effects:** [Presence Concealment](../../effects/presence-concealment.md)
- **Referenced by:** [Formhide](formhide.md), [｢ Amaterasu, Lord of Shimmering Flames ｣](../../../tr-nightmares/abilities/ultimate-skills/amaterasu.md)

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `Haze.auraCost` | 20 | Aura Cost to activate. |
| `Haze.concealment` | 2 | The Presence Concealment level when activated. |

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

`tensura:skills/battlewill`
