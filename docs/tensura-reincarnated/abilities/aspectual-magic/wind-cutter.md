# Wind Cutter

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Wind Cutter](../../../assets/icons/tensura/skill/wind_cutter.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:wind_cutter` |
| **Element** | Wind |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Fire concentrated blades of wind toward targets.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Lesser Daemon](../../mobs/lesser-daemon.md)
- Can appear in common tomes in ruined wizard towers
- Sold by dwarf traders (low basic tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Related skills:** [Wind Blade](../spiritual-magic/wind-blade.md)
- **Referenced by:** [Tornado Blade](tornado-blade.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `WindCutter.castTime` | 40 | Cast time in tick. |
| `WindCutter.castTimeMastered` | 30 | Cast time in tick when mastered. |
| `WindCutter.magiculeCost` | 500 | Magicule Cost to cast. |
| `WindCutter.magicDamage` | 30 | The magic damage of the wind cutter. |
| `WindCutter.windDamage` | 10 | The wind damage of the wind cutter. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/common_tome_ruined_wizard_tower`, `tensura:skills/low_basic_tome_dwarf_trade`
