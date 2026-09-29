# Infinite Regeneration

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Infinite Regeneration](../../../assets/icons/tensura/skill/infinite_regeneration.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:infinite_regeneration` |
| **Activation** | Toggle |

</div>

> Use your massive amount of magicule to instantly regenerate from all but the most grievous of injuries.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

## Obtaining

- Intrinsic skill of: [Demon Slime](../../races/demon-slime.md), [God Slime](../../races/god-slime.md), [Divine Vampire](../../races/divine-vampire.md), [High-Class Demon](../../../tr-nightmares/races/high-class-demon.md)
- Can be learned by: [Divine Angel](../../../ascension/races/divine-angel.md), [Fallen Angel](../../../ascension/races/fallen-angel.md), [Cosmic Deity](../../../ascension/races/cosmic-deity.md), [Chaotic Deity](../../../ascension/races/chaotic-deity.md), [Frog Monarch](../../../ascension/races/frog-monarch.md), [9 Tailed Fox](../../../ascension/races/nine-tail-fox.md), [Divine Kitsune](../../../ascension/races/divine-kitsune.md), [Progenitor Bloodfiend](../../../ascension/races/progenitor-bloodfiend.md), [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md), [Chaos Dragon](../../../ascension/races/chaos-dragon.md), [Death Tyrant](../../../ascension/races/death-tyrant.md), [Sun Wukong](../../../ascension/races/sun-wukong.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/demon_clan_config.toml): Intrinsic pool (if used).
- Listed in the `intrinsicSkills` config option (config/mysticism/race/wyrm_config.toml): The list of intrinsic skills that the race gets.
- Acquisition checks: [Ultraspeed Regeneration](ultraspeed-regeneration.md)

## Related

- **Related skills:** [Ultraspeed Regeneration](ultraspeed-regeneration.md)
- **Effects:** [Instant Regeneration](../../effects/instant-regeneration.md)
- **Referenced by:** [Imaginator](../../../tr-nightmares/abilities/unique-skills/imaginator.md), [Arelkos](../../../tr-nightmares/abilities/unique-skills/arelkos.md), [Dragon Factor Haki](../../../tr-nightmares/abilities/intrinsic-skills/dragon-factor-haki.md), [Tenacity](../../../tensura-mysticism/abilities/intrinsic-skills/tenacity.md), [Butcher](../../../tensura-mysticism/abilities/unique-skills/butcher.md), [Timeless Mage](../../../ascension/abilities/ultimate-skills/timeless-mage.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `InfiniteRegeneration.epAcquirement` | 2,000,000 | EP Requirement for Learning. |
| `InfiniteRegeneration.magiculeCost` | 100 | Magicule Cost per HP regenerated. |
| `InfiniteRegeneration.magiculeCostMastered` | 60 | Magicule Cost per HP regenerated when mastered. |
| `InfiniteRegeneration.shpMagiculeCost` | 120 | Magicule Cost per SHP regenerated. |
| `InfiniteRegeneration.shpMagiculeCostMastered` | 80 | Magicule Cost per SHP regenerated when mastered. |

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
