# Sacred Haki

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Sacred Haki](../../../assets/icons/tensura/skill/sacred_haki.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:sacred_haki` |
| **Modes** | 2 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Press, Hold |

</div>

> Strike fear into the hearts of evil and give strength to your allies.

## Modes

| # | Mode |
|---|---|
| 1 | Magicule Release |
| 2 | Magicule Coat |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Magicule Release | 50 |  |
| Magicule Coat | 100 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.95 | multiply total |

## Obtaining

- Can be learned by: [Archangel](../../../ascension/races/archangel.md), [Seraphim](../../../ascension/races/seraphim.md), [Divine Angel](../../../ascension/races/divine-angel.md), [Fallen Angel](../../../ascension/races/fallen-angel.md), [Cosmic Deity](../../../ascension/races/cosmic-deity.md), [Chaotic Deity](../../../ascension/races/chaotic-deity.md), [6 Tailed Fox](../../../ascension/races/six-tail-fox.md), [9 Tailed Fox](../../../ascension/races/nine-tail-fox.md), [Divine Kitsune](../../../ascension/races/divine-kitsune.md), [Royal Djinn](../../../ascension/races/royal-djinn.md), [Wishbound Djinn](../../../ascension/races/wishbound-djinn.md), [Primordial Djinn](../../../ascension/races/primordial-djinn.md), [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md), [Monkey King](../../../ascension/races/monkey-king.md), [Divine King](../../../ascension/races/divine-king.md), [Sun Wukong](../../../ascension/races/sun-wukong.md)
- Acquisition checks: [Hero Haki](hero-haki.md)

## Related

- **Related skills:** [Hero Haki](hero-haki.md)
- **Effects:** [Haki Coat](../../effects/haki-coat.md)
- **Referenced by:** [Hero Haki](hero-haki.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `SacredHaki.epAcquirement` | 200,000 | EP Requirement for Learning. |
| `SacredHaki.magiculeCost` | 50 | Magicule Cost to activate Magicule Release. |
| `SacredHaki.magiculeCostCoat` | 100 | Magicule Cost to activate Haki Coat. |
| `SacredHaki.coatDuration` | 2,400 | The duration in tick of the Haki Coat when activated. |
| `SacredHaki.epDifferenceMultiplier` | 0.5 | The EP difference multiplier for each Fear Level. |
| `SacredHaki.healHP` | 60 | The amount of HP to heal allies every 5 seconds. |
| `Haki.speedMultiplier` | 0.05 | Activation Speed Multiplier when activated. |
| `Haki.epAcquirement` | 100,000 | EP Requirement for Learning. |
| `Haki.magiculeCost` | 25 | Magicule Cost to activate. |
| `Haki.speedMultiplier` | 0.05 | Activation Speed Multiplier when activated. |
| `Haki.speedMultiplierMastered` | 0.1 | Activation Speed Multiplier when activated with mastery. |
| `Haki.hakiRadius` | 15 | The attack radius of the haki in blocks. |
| `Haki.epDifferenceMultiplier` | 0.25 | The EP difference multiplier for each Fear Level. |
| `Haki.fearDuration` | 200 | The duration in tick of the Fear effect when applied. |
| `Haki.cooldown` | 5 | The cooldown in second of the haki. |
| `Haki.cooldownMastered` | 3 | The cooldown in second of the haki when mastered. |

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
