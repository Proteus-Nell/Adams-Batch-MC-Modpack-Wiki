# Universal Perception

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Universal Perception](../../../assets/icons/tensura/skill/universal_perception.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:universal_perception` |
| **Activation** | Toggle, Press |

</div>

> Combine all magic, sound and heat sense to detect entities around.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 25 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Intrinsic skill of: [Demon Slime](../../races/demon-slime.md), [God Slime](../../races/god-slime.md), [High-Class Demon](../../../tr-nightmares/races/high-class-demon.md), [Slayer Fairy](../../../tr-nightmares/races/slayer-fairy.md), [Sacred qTree sChild](../../../tr-nightmares/races/sacred-tree-child.md), [Mutant Giant](../../../tr-nightmares/races/mutant-giant.md), [Earthshaker pDancer](../../../tr-nightmares/races/earthshaker-dancer.md), [Higher hGoddess](../../../tr-nightmares/races/higher-class-goddess.md), [Goddess Princess](../../../tr-nightmares/races/princess-of-goddess.md), [Daughter pOf Light](../../../tr-nightmares/races/daughter-of-light.md), [sAccursed gGoddess](../../../tr-nightmares/races/accursed-goddess.md), [Lance hCorporal](../../../tr-nightmares/races/lance-corporal.md), [Divine hSoldier](../../../tr-nightmares/races/divine-soldier.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/demon_clan_config.toml): Intrinsic pool (if used).
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill IDs granted by Elfaria. Includes Albis so old Ars Weiss clones stay compatible, magic basics, transforms, senses, chant annulment,...

## Related

- **Summons / entities:** Tensura
- **Referenced by:** [Magic Sense](magic-sense.md), [Sense Heat Source](sense-heat-source.md), [Sense Soundwave](sense-soundwave.md), [｢ Hastur, Lord of Starwind ｣](../../../tr-nightmares/abilities/ultimate-skills/hastur.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `UniversalPerception.presenceSense` | 3 | The level of Presence Sense when activated. |
| `UniversalPerception.presenceRadius` | 20 | The bonus Presence Sense Radius when activated. |
| `UniversalPerception.heatRadius` | 30 | The radius in block that mobs and blocks around the user will be detected by heat sense. |
| `UniversalPerception.magiculeCost` | 25 | Magicule Cost to activate. |

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
