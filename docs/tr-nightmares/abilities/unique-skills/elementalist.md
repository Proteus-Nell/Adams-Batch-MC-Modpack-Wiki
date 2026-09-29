# Elementalist

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Elementalist](../../../assets/icons/trnightmare/skill/elementalist.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:elementalist` |
| **Modes** | 2 |
| **Activation** | Toggle, Press, Hold |

</div>

> You are one with the elements, harnessing the power of each as you so choose.

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Mode 2 |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers on melee contact
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -1 | multiply total |
| Flying Speed | -1 | multiply total |

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `elementalist.mpAcquirement` | 60,000 | EP / magicule obtainment cost. |
| `elementalist.passiveBoost` | 0.3 | Passive elemental damage boost while toggled (not mastered). |
| `elementalist.passiveBoostMastered` | 0.4 | Passive elemental damage boost while toggled (mastered). |
| `elementalist.connectionBoost` | 20 | Connection boost per stack (not mastered). |
| `elementalist.connectionBoostMastered` | 40 | Connection boost per stack (mastered). |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
