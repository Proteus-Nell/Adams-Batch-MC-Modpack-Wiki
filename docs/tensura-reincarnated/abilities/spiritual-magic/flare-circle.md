# Flare Circle

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Flare Circle](../../../assets/icons/tensura/skill/flare_circle.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:flare_circle` |
| **Element** | Fire |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Press, Hold |

</div>

> Opens a Gate to Hell from which wicked flames erupt to turn your enemies to ash.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Innate to mobs: [Ifrit](../../mobs/ifrit.md)
- Removed and re-rolled when you change race

## Related

- **Referenced by:** [Ogre Flame](../battlewill/ogre-flame.md), [Sunshine](../../../tr-nightmares/abilities/unique-skills/sunshine.md), [Oni Pyre](../../../tr-nightmares/abilities/battlewill/oni-pyre.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `FlareCircle.castTime` | 60 | Cast time in tick. |
| `FlareCircle.castTimeMastered` | 60 | Cast time in tick when mastered. |
| `FlareCircle.magiculeCost` | 10,000 | Magicule Cost to cast. |
| `FlareCircle.range` | 20 | The range in block of the magic. |
| `FlareCircle.flareDamage` | 80 | The damage of the flare circle. |
| `FlareCircle.flareRadius` | 5 | The radius in block of the flare circle. |
| `FlareCircle.flareHeight` | 7 | The height in block of the flare circle. |
| `FlareCircle.flareDuration` | 100 | The max duration in tick that the magic can be used. |
| `FlareCircle.flareDurationMastered` | 200 | The max duration in tick that the magic can be used with mastery. |

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
