# Electro Blast

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Electro Blast](../../../assets/icons/tensura/skill/electro_blast.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:electro_blast` |
| **Element** | Wind |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Press, Hold |

</div>

> Fire a beam attack that pierces through enemies and deals devastating damage while paralyzing your enemies.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 25,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Innate to mobs: [Sylphide](../../mobs/sylphide.md)
- Removed and re-rolled when you change race

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `ElectroBlast.castTime` | 140 | Cast time in tick. |
| `ElectroBlast.castTimeMastered` | 100 | Cast time in tick when mastered. |
| `ElectroBlast.magiculeCost` | 25,000 | Magicule Cost to cast. |
| `ElectroBlast.range` | 20 | The range in block of the magic. |
| `ElectroBlast.damage` | 125 | The damage of the magic. |
| `ElectroBlast.explosion` | 2 | The explosion level of the magic. |
| `ElectroBlast.paralysisLevel` | 2 | The level of Paralysis when applied by the magic. |
| `ElectroBlast.paralysisDuration` | 600 | The duration in tick of Paralysis when applied by the magic. |

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
