# Formhide

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Formhide](../../../assets/icons/tensura/skill/formhide.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:formhide` |
| **Kind** | Utility |
| **Activation** | Hold |

</div>

> Match your aura to the surroundings, which makes you imperceptible.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 15 |

## How it works

- Charged or channelled by holding the skill key
- Does something when mastered

## Obtaining

- Sold by dwarf traders (medium manual)
- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Related

- **Related skills:** [Haze](haze.md)
- **Effects:** [Presence Concealment](../../effects/presence-concealment.md)
- **Referenced by:** [Haze](haze.md)

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `Formhide.auraCost` | 15 | Aura Cost to activate. |
| `Formhide.concealment` | 1 | The Presence Concealment level when activated. |

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

`tensura:skills/battlewill`, `tensura:skills/medium_manual_dwarf_trade`
