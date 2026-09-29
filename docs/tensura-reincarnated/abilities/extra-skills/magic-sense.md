# Magic Sense

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Magic Sense](../../../assets/icons/tensura/skill/magic_sense.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:magic_sense` |
| **Activation** | Toggle, Press |

</div>

> Using magicule to sense entities around.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Does something when first learned
- Does something when mastered

## Obtaining

- Intrinsic skill of: [Lower-Class Demon](../../../tr-nightmares/races/lower-class-demon.md), [Eidolon](../../../tr-nightmares/races/eidolon.md), [Shadow Mimic](../../../tr-nightmares/races/shadow-mimic.md), [Lesser Mimic](../../../tr-nightmares/races/lesser-mimic.md)
- Can be learned by: [Kitsune](../../../ascension/races/kitsune.md), [3 Tailed Fox](../../../ascension/races/three-tail-fox.md), [6 Tailed Fox](../../../ascension/races/six-tail-fox.md), [9 Tailed Fox](../../../ascension/races/nine-tail-fox.md), [Divine Kitsune](../../../ascension/races/divine-kitsune.md), [Fledgling Bloodfiend](../../../ascension/races/fledgling-bloodfiend.md), [Kindred Bloodfiend](../../../ascension/races/kindred-bloodfiend.md), [Blood Noble](../../../ascension/races/blood-noble.md), [Elder Bloodfiend](../../../ascension/races/elder-bloodfiend.md), [Progenitor Bloodfiend](../../../ascension/races/progenitor-bloodfiend.md), [Whisper Djinn](../../../ascension/races/whisper-djinn.md), [Trickster Djinn](../../../ascension/races/trickster-djinn.md), [Phantom Djinn](../../../ascension/races/phantom-djinn.md), [Royal Djinn](../../../ascension/races/royal-djinn.md), [Wishbound Djinn](../../../ascension/races/wishbound-djinn.md), [Primordial Djinn](../../../ascension/races/primordial-djinn.md), [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md), [Gazer](../../../ascension/races/gazer.md), [Spectator](../../../ascension/races/spectator-gazer.md), [Mindwitness](../../../ascension/races/mindwitness.md), [Gauth](../../../ascension/races/gauth.md), [Beholder](../../../ascension/races/beholder.md), [Death Tyrant](../../../ascension/races/death-tyrant.md), [Monkey King](../../../ascension/races/monkey-king.md), [Divine King](../../../ascension/races/divine-king.md), [Sun Wukong](../../../ascension/races/sun-wukong.md), [Mage Skeleton](../../../ascension/races/mage-skeleton.md), [Elder Lich](../../../ascension/races/elder-lich.md), [Lich](../../../ascension/races/lich.md), [Lich King](../../../ascension/races/lich-king.md)
- Innate to mobs: [Arch Daemon](../../mobs/arch-daemon.md), [Beast Gnome](../../mobs/beast-gnome.md), [Charybdis](../../mobs/charybdis.md), [Gazel Dwargo](../../mobs/gazel-dwargo.md), [Greater Daemon](../../mobs/greater-daemon.md), [Hinata Sakaguchi](../../mobs/hinata-sakaguchi.md), [Lesser Daemon](../../mobs/lesser-daemon.md), [Mai Furuki](../../mobs/mai-furuki.md), [Shizu](../../mobs/shizu.md), [Memoires](../../../tensura-mysticism/mobs/memoires.md)
- Listed in the `charybdisCoreFusingSkills` config option (config/tensura/block_config.toml): List of Skills that can be obtained from fusing with Inert Charybdis Core using Degenerate and similar abilities.
- Listed in the `charybdisCoreFusingSkillsActive` config option (config/tensura/block_config.toml): List of Skills that can be obtained from fusing with Active Charybdis Core using Degenerate and similar abilities.
- Listed in the `intrinsicPool` config option (config/nightmare/race/demon_clan_config.toml): List of intrinsic skills Lower Class Demon can randomly receive.
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill IDs granted by Elfaria. Includes Albis so old Ars Weiss clones stay compatible, magic basics, transforms, senses, chant annulment,...
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/direwolf_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Danger Sense](danger-sense.md), [Sense Soundwave](sense-soundwave.md), [Sense Heat Source](sense-heat-source.md), [Universal Perception](universal-perception.md)
- **Referenced by:** [Danger Sense](danger-sense.md), [Sense Heat Source](sense-heat-source.md), [Sense Soundwave](sense-soundwave.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `MagicSense.presenceSensePress` | 0.5 | The level of Presence Sense when activated. |
| `MagicSense.presenceSenseMastered` | 1 | The level of Presence Sense when activated with mastery. |
| `MagicSense.magiculeCost` | 5 | Magicule Cost to activate. |

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
