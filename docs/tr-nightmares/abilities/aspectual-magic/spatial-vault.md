# Spatial Vault

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `trnightmare:spatial_vault` |
| **Max mastery** | 700 |
| **Activation** | Hold |

</div>

> After a four-second chant, open a 24-row spatial storage with 200-stack capacity and draw nearby dropped items into it while the spell is in slot. Mastery raises the stack cap to 400 and removes the cast time.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 |  |

## How it works

- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Does something when mastered

## Obtaining

- Acquisition checks: [Spatial Storage](../../../tensura-reincarnated/abilities/aspectual-magic/spatial-storage.md), [Molecular Manipulation](../../../tensura-reincarnated/abilities/extra-skills/molecular-manipulation.md)

## Related

- **Related skills:** [Spatial Storage](../../../tensura-reincarnated/abilities/aspectual-magic/spatial-storage.md), [Molecular Manipulation](../../../tensura-reincarnated/abilities/extra-skills/molecular-manipulation.md), [Spatial Sorter](spatial-sorter.md)
- **Referenced by:** [Spatial Sorter](spatial-sorter.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `SpatialStorage.castTime` | 40 | Cast time in tick. |
| `SpatialStorage.magiculeCost` | 3,000 | Magicule Cost to cast. |
| `SpatialStorage.spatialSlots` | 54 | The number of slots of the Spatial Storage. |
| `SpatialStorage.spatialStack` | 100 | The maximum stack size of items in the Spatial Storage. |
| `SpatialStorage.spatialStackMastered` | 200 | The maximum stack size of items in the Spatial Storage when mastered. |
