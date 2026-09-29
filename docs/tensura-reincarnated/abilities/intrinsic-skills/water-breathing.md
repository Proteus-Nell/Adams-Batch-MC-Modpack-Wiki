# Water Breathing

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Water Breathing](../../../assets/icons/tensura/skill/water_breathing.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:water_breathing` |
| **Activation** | Passive |

</div>

> Remove the requirement of air underwater.

## How it works

- Has a continuous (per-tick) effect

## Obtaining

- Intrinsic skill of: [Merfolk](../../races/merfolk.md), [Enlightened Merfolk](../../races/enlightened-merfolk.md), [Merfolk Saint](../../races/merfolk-saint.md), [Divine Fish](../../races/divine-fish.md), [Frog](../../../ascension/races/frog.md), [Giant Frog](../../../ascension/races/giant-frog.md), [Poison Toad](../../../ascension/races/poison-toad.md), [Swamp Sovereign](../../../ascension/races/swamp-sovereign.md), [Bog Ancient](../../../ascension/races/bog-ancient.md), [Venom Lord](../../../ascension/races/venom-lord.md), [Frog Monarch](../../../ascension/races/frog-monarch.md), [Cursed Mariner](../../../ascension/races/cursed-mariner.md), [Cursed Dreadnaught](../../../ascension/races/cursed-dreadnaught.md), [Phantom Corsair](../../../ascension/races/phantom-corsair.md), [Davy Jones](../../../ascension/races/davy-jones.md)
- Innate to mobs: [Giant Cod](../../mobs/giant-cod.md), [Giant Salmon](../../mobs/giant-salmon.md), [Sissie](../../mobs/sissie.md), [Spear Toro](../../mobs/spear-toro.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Lesser Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Greater Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Golden Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Chimera Lord can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.
- Listed in the `intrinsicSkills` config option (config/nightmare/race/axolotl/axolotl_config.toml): List of skills obtained by this race.

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `WaterBreathing.waterBreathLevel` | 3 | The level of the Water Breathing effect when activated. |

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

`tensura:skills/intrinsic_skills`
