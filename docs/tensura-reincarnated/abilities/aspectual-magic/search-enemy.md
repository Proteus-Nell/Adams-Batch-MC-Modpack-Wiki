# Search Enemy

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Search Enemy](../../../assets/icons/tensura/skill/search_enemy.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:search_enemy` |
| **Element** | Misc |
| **Modes** | 2 |
| **Max mastery** | 100 |
| **Cooldowns (s)** | 2 |
| **Activation** | Press, Hold |

</div>

> Highlight hostile mobs around the caster.

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Mode 2 |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Obtaining

- Sold by dwarf traders (low rare tome)
- Can appear in rare tomes in burnt wizard towers

## Related

- **Effects:** [Enemy Search](../../effects/enemy-search.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `SearchEnemy.castTime` | 40 | Cast time in tick. |
| `SearchEnemy.magiculeCost` | 100 | Magicule Cost to cast. |
| `SearchEnemy.magiculeCostConstant` | 5 | Magicule Cost per second to cast the Constant mode. |
| `SearchEnemy.searchDuration` | 2,400 | The duration in tick of the Enemy Search effect when using default mode. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/low_rare_tome_dwarf_trade`, `tensura:skills/rare_tome_burnt_wizard_tower`
