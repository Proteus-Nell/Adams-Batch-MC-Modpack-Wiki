# Scale Armor

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Scale Armor](../../../assets/icons/tensura/skill/scale_armor.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:scale_armor` |
| **Activation** | Toggle |

</div>

> Like the lizardmen, move through water and mud with no penalties while receiving a slight defense buff.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| swim | 1 | add |
| armor | 6 | add |

## Obtaining

- Intrinsic skill of: [Lizardman](../../races/lizardman.md), [Dragonewt](../../races/dragonewt.md), [True Dragonewt](../../races/true-dragonewt.md), [Divine Dragon](../../races/divine-dragon.md), [Corrupted Dragonkin](../../../ascension/races/corrupted-dragonkin.md), [Corrupted Dragon](../../../ascension/races/corrupted-dragon.md), [Cursed Dragon](../../../ascension/races/cursed-dragon.md), [Demonic Dragon](../../../ascension/races/demonic-dragon.md), [Demon Dragon God](../../../ascension/races/demon-dragon-god.md), [Ender Dragonewt](../../../ascension/races/ender-dragonewt.md), [Void Dragonewt](../../../ascension/races/void-dragonewt.md), [Abyssal Dragonewt](../../../ascension/races/abyssal-dragonewt.md), [Chaos Dragon](../../../ascension/races/chaos-dragon.md)
- Innate to mobs: [Lizardman](../../mobs/lizardman.md), [Megalodon](../../mobs/megalodon.md), [Orc Disaster](../../mobs/orc-disaster.md), [Orc Lord](../../mobs/orc-lord.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `ScaleArmor.swimMultiplier` | 2 | The swimming speed multiplier that the user gains when toggled. |
| `ScaleArmor.armorPoint` | 6 | The number of armor points that the user gains when toggled. |

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
