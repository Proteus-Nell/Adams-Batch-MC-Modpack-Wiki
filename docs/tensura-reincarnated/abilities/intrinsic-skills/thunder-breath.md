# Thunder Breath

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Thunder Breath](../../../assets/icons/tensura/skill/thunder_breath.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:thunder_breath` |
| **Activation** | Press, Hold |

</div>

> Release thunder from your mouth to damage foes in front of you.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Related

- **Summons / entities:** [Thunder Breath](thunder-breath.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `ThunderBreath.magiculeCost` | 50 | Base Magicule Cost to activate (halved when mastered). |
| `ThunderBreath.damage` | 10 | The damage each second of the Poison Breath. |
| `ThunderBreath.damageMastered` | 20 | The damage each second of the Poison Breath when mastered. |

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

`tensura:skills/intrinsic_skills`, `tensura:skills/lightning_skills`
