# Snake Eye

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Snake Eye](../../../assets/icons/tensura/skill/snake_eye.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:snake_eye` |
| **Modes** | 5 |
| **Activation** | Hold |

</div>

> Apply various debuff on targets on sight.

## Modes

| # | Mode |
|---|---|
| 1 | Corrosion |
| 2 | Poison |
| 3 | Paralysis |
| 4 | Petrification |
| 5 | Insanity |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 80 |  |

## How it works

- Charged or channelled by holding the skill key

## Obtaining

- Can be learned by: [3 Tailed Fox](../../../ascension/races/three-tail-fox.md), [6 Tailed Fox](../../../ascension/races/six-tail-fox.md), [9 Tailed Fox](../../../ascension/races/nine-tail-fox.md), [Divine Kitsune](../../../ascension/races/divine-kitsune.md), [Blood Noble](../../../ascension/races/blood-noble.md), [Elder Bloodfiend](../../../ascension/races/elder-bloodfiend.md), [Progenitor Bloodfiend](../../../ascension/races/progenitor-bloodfiend.md), [Phantom Djinn](../../../ascension/races/phantom-djinn.md), [Royal Djinn](../../../ascension/races/royal-djinn.md), [Wishbound Djinn](../../../ascension/races/wishbound-djinn.md), [Primordial Djinn](../../../ascension/races/primordial-djinn.md), [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Greater Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Golden Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Chimera Lord can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.

## Related

- **Effects:** [Corrosion](../../effects/corrosion.md), [Fatal Poison](../../effects/fatal-poison.md), [Paralysis](../../effects/paralysis.md), [Petrification](../../effects/petrification.md), [Insanity](../../effects/insanity.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `SnakeEye.magiculeCost` | 80 | Magicule Cost to activate. |
| `SnakeEye.maxRange` | 20 | The maximum range in block of Snake Eye. |
| `SnakeEye.increaseTick` | 300 | The amount of tick activated needed to increase 1 level of a effect. |

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

`tensura:skills/extra_skills`
