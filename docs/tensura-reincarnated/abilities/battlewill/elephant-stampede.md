# Elephant Stampede

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Elephant Stampede](../../../assets/icons/tensura/skill/elephant_stampede.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:elephant_stampede` |
| **Kind** | Projectile |
| **Activation** | Hold |

</div>

> Throw a ring of aura spheres around you.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 100 |

## How it works

- Charged or channelled by holding the skill key

## Obtaining

- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `ElephantStampede.auraCost` | 100 | Base Aura Cost to activate. |
| `ElephantStampede.holdTime` | 20 | The Time the user need to hold down to do each time of attack. |
| `ElephantStampede.baseDamage` | 25 | The Damage of each aura bullet (doubled with Mastery). |
| `ElephantStampede.bulletNumber` | 8 | The Number of aura bullets each time activated. |

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
