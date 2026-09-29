# Majesty

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Majesty](../../../assets/icons/tensura/skill/majesty.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:majesty` |
| **Activation** | Passive |

</div>

> By boosting your reputation with the villagers, gain a permanent Hero of the Village effect.

## How it works

- Has a continuous (per-tick) effect

## Obtaining

- Intrinsic skill of: [Royal Demon](../../../tr-nightmares/races/royal-demon.md)
- Can be learned by: [Seraphim](../../../ascension/races/seraphim.md), [Divine Angel](../../../ascension/races/divine-angel.md), [Fallen Angel](../../../ascension/races/fallen-angel.md), [Cosmic Deity](../../../ascension/races/cosmic-deity.md), [Chaotic Deity](../../../ascension/races/chaotic-deity.md), [9 Tailed Fox](../../../ascension/races/nine-tail-fox.md), [Divine Kitsune](../../../ascension/races/divine-kitsune.md), [Elder Bloodfiend](../../../ascension/races/elder-bloodfiend.md), [Progenitor Bloodfiend](../../../ascension/races/progenitor-bloodfiend.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md), [Davy Jones](../../../ascension/races/davy-jones.md), [Beholder](../../../ascension/races/beholder.md), [Death Tyrant](../../../ascension/races/death-tyrant.md), [Sun Wukong](../../../ascension/races/sun-wukong.md), [Dark Lord Dullahan](../../../ascension/races/dark-lord-dullahan.md), [Lich King](../../../ascension/races/lich-king.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `Majesty.raidNumber` | 10 | The number of raid needed to be done to gain this skill. |
| `Majesty.heroLevel` | 5 | The level of Hero of the Village effect when applied. |

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
