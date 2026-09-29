# Shadow Motion

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Shadow Motion](../../../assets/icons/tensura/skill/shadow_motion.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:shadow_motion` |
| **Modes** | 3 |
| **Activation** | Press, Hold |

</div>

> Melt into the shadows and move unseen by all but the most keen observers.

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Shadow Step |
| 3 | Shadow Storage |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Mode 1 | 10 |  |
| Shadow Step | 200 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Intrinsic skill of: [Vampire](../../races/vampire.md), [Vampire Overcomer](../../races/vampire-overcomer.md), [Vampire Lord](../../races/vampire-lord.md), [Divine Vampire](../../races/divine-vampire.md), [Corrupted Dragonkin](../../../ascension/races/corrupted-dragonkin.md), [Corrupted Dragon](../../../ascension/races/corrupted-dragon.md), [Cursed Dragon](../../../ascension/races/cursed-dragon.md), [Demonic Dragon](../../../ascension/races/demonic-dragon.md), [Demon Dragon God](../../../ascension/races/demon-dragon-god.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Golden Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Chimera Lord can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.
- Listed in the `intrinsicSkills` config option (config/nightmare/race/scholar_config.toml): List of skills obtained by this race.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/direwolf_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/special_direwolf_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Effects:** [Rest](../../effects/rest.md), [Shadow Step](../../effects/shadow-step.md)
- **Items:** [Shadow Storage](../../items/miscellaneous/shadow-storage.md)
- **Referenced by:** [Night Cloak](../../../tr-nightmares/abilities/aspectual-magic/night-cloak.md), [Satella](../../../tensura-more-skills/abilities/unique-skills/satella.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `ShadowMotion.magiculeCost` | 10 | Magicule Cost to activate Default Mode. |
| `ShadowMotion.magiculeCostStep` | 200 | Magicule Cost to activate Shadow Step. |
| `ShadowMotion.stepRange` | 20 | The maximum range in block of Shadow Step. |

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

`tensura:skills/extra_skills`, `tensura:skills/space_skills`
