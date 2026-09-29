# Ice Breath

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Ice Breath](../../../assets/icons/tensura/skill/ice_breath.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:ice_breath` |
| **Activation** | Press, Hold |

</div>

> Spew icy breath to freeze enemies.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 30 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Intrinsic skill of: [Dragonewt](../../races/dragonewt.md), [True Dragonewt](../../races/true-dragonewt.md), [Divine Dragon](../../races/divine-dragon.md), [Corrupted Dragonkin](../../../ascension/races/corrupted-dragonkin.md), [Corrupted Dragon](../../../ascension/races/corrupted-dragon.md), [Cursed Dragon](../../../ascension/races/cursed-dragon.md), [Demonic Dragon](../../../ascension/races/demonic-dragon.md), [Demon Dragon God](../../../ascension/races/demon-dragon-god.md), [Ender Dragonewt](../../../ascension/races/ender-dragonewt.md), [Void Dragonewt](../../../ascension/races/void-dragonewt.md), [Abyssal Dragonewt](../../../ascension/races/abyssal-dragonewt.md), [Chaos Dragon](../../../ascension/races/chaos-dragon.md)

## Related

- **Referenced by:** [Ice Manipulation](../../../tensura-mysticism/abilities/extra-skills/ice-manipulation.md), [Ice Domination](../../../tensura-mysticism/abilities/extra-skills/ice-domination.md), [Cryogenic Cessation](../../../tensura-mysticism/abilities/extra-skills/cryogenic-cessation.md), [Dragon Slayer](../../../ascension/abilities/unique-skills/dragon-slayer.md), [The Slayer of Dragons](../../../ascension/abilities/ultimate-skills/slayer-of-dragons.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `IceBreath.magiculeCost` | 30 | Base Magicule Cost to activate. |
| `IceBreath.damage` | 8 | The damage each second of the Ice Breath. |
| `IceBreath.damageMastered` | 16 | The damage each second of the Ice Breath when mastered. |

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

`tensura:skills/ice_skills`, `tensura:skills/intrinsic_skills`, `tensura:skills/water_skills`
