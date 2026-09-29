# Gate

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Gate](../../../assets/icons/tensura/skill/gate.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:gate` |
| **Element** | Space |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Hold |

</div>

> Tear space asunder connecting two points in space.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50 |  |

## How it works

- Triggers when the held key is released
- Does something when first learned
- Does something when mastered

## Obtaining

- Removed and re-rolled when you change race
- Listed in the `formulaSuccessionBlacklist` config option (config/tensuramoreskills-grand.toml): Spell registry IDs that Formula Succession is not allowed to mirror.

## Related

- **Related skills:** [Spatial Motion](../extra-skills/spatial-motion.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `Gate.castTime` | 300 | Cast time in tick. |
| `Gate.castTimeMastered` | 300 | Cast time in tick when mastered. |
| `Gate.magiculeCost` | 50 | Magicule Cost per block to warp. |
| `Gate.warpChargeTick` | 100 | The charge tick of the portal before warping any entity. |
| `Gate.cooldown` | 20 | The cooldown in second of the magic. |
| `Gate.cooldownMastered` | 10 | The cooldown in second of the magic when mastered. |

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
