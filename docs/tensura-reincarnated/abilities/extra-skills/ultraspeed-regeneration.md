# Ultraspeed Regeneration

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Ultraspeed Regeneration](../../../assets/icons/tensura/skill/ultraspeed_regeneration.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:ultraspeed_regeneration` |
| **Activation** | Toggle |

</div>

> Boost your bodies healing to nearly impossible levels

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

## Obtaining

- Intrinsic skill of: [Wicked Oni](../../races/wicked-oni.md), [Death Oni](../../races/death-oni.md), [Divine Fighter](../../races/divine-fighter.md), [Divine Giant](../../races/divine-giant.md), [Vampire Lord](../../races/vampire-lord.md), [Divine Vampire](../../races/divine-vampire.md), [Netherite Dragon](../../../tr-nightmares/races/netherite-dragon.md), [Divine Netherite Dragon](../../../tr-nightmares/races/divine-netherite-dragon.md), [Middle-Class Demon](../../../tr-nightmares/races/mid-class-demon.md), [Slayer Fairy](../../../tr-nightmares/races/slayer-fairy.md), [qFairy pPrince](../../../tr-nightmares/races/fairy-prince.md), [One Eyed God](../../../tr-nightmares/races/one-eyed-god.md), [Higher hGoddess](../../../tr-nightmares/races/higher-class-goddess.md), [Nameless Goddess](../../../tr-nightmares/races/nameless-goddess.md), [Brother Of Chaos](../../../tr-nightmares/races/brother-of-chaos.md), [Goddess Princess](../../../tr-nightmares/races/princess-of-goddess.md), [Daughter pOf Light](../../../tr-nightmares/races/daughter-of-light.md), [sAccursed gGoddess](../../../tr-nightmares/races/accursed-goddess.md), [Lance hCorporal](../../../tr-nightmares/races/lance-corporal.md), [Divine hSoldier](../../../tr-nightmares/races/divine-soldier.md)
- Can be learned by: [Seraphim](../../../ascension/races/seraphim.md), [Divine Angel](../../../ascension/races/divine-angel.md), [Fallen Angel](../../../ascension/races/fallen-angel.md), [Cosmic Deity](../../../ascension/races/cosmic-deity.md), [Chaotic Deity](../../../ascension/races/chaotic-deity.md), [Bog Ancient](../../../ascension/races/bog-ancient.md), [Venom Lord](../../../ascension/races/venom-lord.md), [Frog Monarch](../../../ascension/races/frog-monarch.md), [6 Tailed Fox](../../../ascension/races/six-tail-fox.md), [9 Tailed Fox](../../../ascension/races/nine-tail-fox.md), [Divine Kitsune](../../../ascension/races/divine-kitsune.md), [Blood Noble](../../../ascension/races/blood-noble.md), [Elder Bloodfiend](../../../ascension/races/elder-bloodfiend.md), [Progenitor Bloodfiend](../../../ascension/races/progenitor-bloodfiend.md), [Wishbound Djinn](../../../ascension/races/wishbound-djinn.md), [Primordial Djinn](../../../ascension/races/primordial-djinn.md), [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md), [Beholder](../../../ascension/races/beholder.md), [Death Tyrant](../../../ascension/races/death-tyrant.md), [Divine King](../../../ascension/races/divine-king.md), [Sun Wukong](../../../ascension/races/sun-wukong.md)
- Innate to mobs: [Charybdis](../../mobs/charybdis.md), [Supermassive Slime](../../mobs/supermassive-slime.md)
- Listed in the `charybdisCoreFusingSkills` config option (config/tensura/block_config.toml): List of Skills that can be obtained from fusing with Inert Charybdis Core using Degenerate and similar abilities.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Chimera Lord can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/demon_clan_config.toml): Intrinsic pool (if used).

## Related

- **Effects:** [Self-Regeneration](../../effects/self-regeneration.md), [Instant Regeneration](../../effects/instant-regeneration.md)
- **Referenced by:** [Infinite Regeneration](infinite-regeneration.md), [Imaginator](../../../tr-nightmares/abilities/unique-skills/imaginator.md), [Arelkos](../../../tr-nightmares/abilities/unique-skills/arelkos.md), [Tenacity](../../../tensura-mysticism/abilities/intrinsic-skills/tenacity.md), [Butcher](../../../tensura-mysticism/abilities/unique-skills/butcher.md), [Timeless Mage](../../../ascension/abilities/ultimate-skills/timeless-mage.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `UltraspeedRegeneration.epAcquirement` | 300,000 | EP Requirement for Learning. |

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
