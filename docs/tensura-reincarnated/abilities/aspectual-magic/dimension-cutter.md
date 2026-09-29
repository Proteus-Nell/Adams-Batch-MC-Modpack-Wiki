# Dimension Cutter

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Dimension Cutter](../../../assets/icons/tensura/skill/dimension_cutter.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:dimension_cutter` |
| **Element** | Space |
| **Max mastery** | 700 |
| **Cooldowns (s)** | 1 mastered, 3 otherwise |
| **Activation** | Hold |

</div>

> Tear space to send forward a blade of dimension rift.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 20,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (high upgraded tome)
- Can appear in rare tomes in ruined wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `DimensionCutter.castTime` | 120 | Cast time in tick. |
| `DimensionCutter.magiculeCost` | 20,000 | Magicule Cost to cast. |
| `DimensionCutter.spatialDamage` | 50 | The spatial damage of the dimension cutter. |
| `DimensionCutter.spatialDamageMastered` | 100 | The spatial damage of the dimension cutter when mastered. |
| `DimensionCutter.size` | 2 | The size multiplier of the dimension cutter. |
| `DimensionCutter.sizeMastered` | 4 | The size multiplier of the dimension cutter when mastered. |
| `DimensionCutter.cooldown` | 3 | The cooldown in second of the magic. |
| `DimensionCutter.cooldownMastered` | 1 | The cooldown in second of the magic when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/high_upgraded_tome_dwarf_trade`, `tensura:skills/rare_tome_ruined_wizard_tower`
