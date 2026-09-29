# Spatial Storage

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Spatial Storage](../../../assets/icons/tensura/skill/spatial_storage.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:spatial_storage` |
| **Element** | Space |
| **Modes** | 2 |
| **Max mastery** | 300 |
| **Activation** | Hold |

</div>

> Rift space to create a small pocket dimension to store items.

## Modes

| # | Mode |
|---|---|
| 1 | Spatial Bag |
| 2 | Dress Change |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 3,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (high upgraded tome)
- Can appear in rare tomes in ruined wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `formulaSuccessionBlacklist` config option (config/tensuramoreskills-grand.toml): Spell registry IDs that Formula Succession is not allowed to mirror.

## Related

- **Items:** [Spatial Bag](../../items/miscellaneous/spatial-bag.md)
- **Referenced by:** [Spatial Vault](../../../tr-nightmares/abilities/aspectual-magic/spatial-vault.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `SpatialStorage.castTime` | 40 | Cast time in tick. |
| `SpatialStorage.magiculeCost` | 3,000 | Magicule Cost to cast. |
| `SpatialStorage.spatialSlots` | 54 | The number of slots of the Spatial Storage. |
| `SpatialStorage.spatialStack` | 100 | The maximum stack size of items in the Spatial Storage. |
| `SpatialStorage.spatialStackMastered` | 200 | The maximum stack size of items in the Spatial Storage when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- %s is not a Spatial Storage ability.
- %s's Spatial Storage is full.

</details>

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/high_upgraded_tome_dwarf_trade`, `tensura:skills/rare_tome_ruined_wizard_tower`, `tensura:skills/unlearnt_cast_excluded`
