# Heavenly Eye

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Heavenly Eye](../../../assets/icons/tensura/skill/heavenly_eye.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:heavenly_eye` |
| **Activation** | Toggle |

</div>

> Project your otherworldly gaze to see all nearby entities and partially ignore dodging abilities.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| dodgeNegate | 50 | add |

## Obtaining

- Intrinsic skill of: [Lesser hGoddess](../../../tr-nightmares/races/lesser-goddess.md)

## Related

- **Summons / entities:** Tensura
- **Referenced by:** [Martial Master](../unique-skills/martial-master.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `HeavenlyEye.presenceSense` | 4 | The level of Presence Sense when activated. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/extra_skills`
