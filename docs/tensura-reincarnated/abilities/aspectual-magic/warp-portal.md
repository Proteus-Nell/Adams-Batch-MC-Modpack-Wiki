# Warp Portal

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Warp Portal](../../../assets/icons/tensura/skill/warp_portal.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:warp_portal` |
| **Element** | Space |
| **Max mastery** | 300 |
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

- Sold by dwarf traders (medium upgraded tome)
- Can appear in uncommon tomes in ruined wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `formulaSuccessionBlacklist` config option (config/tensuramoreskills-grand.toml): Spell registry IDs that Formula Succession is not allowed to mirror.

## Related

- **Related skills:** [Spatial Motion](../extra-skills/spatial-motion.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `WarpPortal.castTime` | 80 | Cast time in tick. |
| `WarpPortal.magiculeCost` | 50 | Magicule Cost per block to warp. |
| `WarpPortal.warpChargeTick` | 100 | The charge tick of the portal before warping any entity. |
| `WarpPortal.cooldown` | 20 | The cooldown in second of the magic. |
| `WarpPortal.cooldownMastered` | 10 | The cooldown in second of the magic when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/medium_upgraded_tome_dwarf_trade`, `tensura:skills/uncommon_tome_ruined_wizard_tower`
