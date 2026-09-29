# Darkness Cannon

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Darkness Cannon](../../../assets/icons/tensura/skill/darkness_cannon.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:darkness_cannon` |
| **Element** | Darkness |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Press, Hold |

</div>

> Shoot a long beam which deals massive damage, destroys armor and debilitates enemies.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 35,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Removed and re-rolled when you change race

## Related

- **Referenced by:** [Designer](../../../tr-nightmares/abilities/unique-skills/designer.md), [Hand of Destruction](../../../tr-nightmares/abilities/extra-skills/hand-of-destruction.md), [｢ Astarte, Lord of Heaven ｣](../../../tr-nightmares/abilities/ultimate-skills/astarte.md), [Witch of Envy, Satella](../../../tensura-more-skills/abilities/ultimate-skills/witch-of-envy-satella.md), [Satella](../../../tensura-more-skills/abilities/unique-skills/satella.md), [Darkness Domination](../../../tensura-mysticism/abilities/extra-skills/darkness-domination.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `DarknessCannon.castTime` | 80 | Cast time in tick. |
| `DarknessCannon.castTimeMastered` | 40 | Cast time in tick when mastered. |
| `DarknessCannon.magiculeCost` | 35,000 | Magicule Cost to cast. |
| `DarknessCannon.range` | 20 | The range in block of the magic. |
| `DarknessCannon.damage` | 250 | The damage of the magic. |
| `DarknessCannon.witherLevel` | 2 | The level of Wither effect when attacked by the magic. |
| `DarknessCannon.witherDuration` | 600 | The duration in tick of Wither effect when attacked by the magic. |
| `DarknessCannon.hungerLevel` | 2 | The level of Hunger effect when attacked by the magic. |
| `DarknessCannon.hungerDuration` | 600 | The duration in tick of Hunger effect when attacked by the magic. |
| `DarknessCannon.insanityDuration` | 200 | The duration in tick of Insanity effect when attacked by the magic. |
| `DarknessCannon.durabilityBreak` | 1,000 | The additional amount of durability break for the targets' armors. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryMedium` | 500 | The max amount of mastery point for Medium Spiritual Magic. |
| `SpiritualMagic.masteryGreater` | 1,000 | The max amount of mastery point for Greater Spiritual Magic. |
| `SpiritualMagic.masteryLord` | 10,000 | The max amount of mastery point for Lord Spiritual Magic. |

## Tags

`tensura:skills/reset_with_race`, `tensura:skills/spiritual_magic`
