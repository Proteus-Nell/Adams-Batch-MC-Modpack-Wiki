# Earth Lock

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Earth Lock](../../../assets/icons/tensura/skill/earth_lock.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:earth_lock` |
| **Element** | Earth |
| **Modes** | 2 |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Solidify the earth where the caster desires.

## Modes

| # | Mode |
|---|---|
| 1 | Earth Lock |
| 2 | Self-lock |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Lesser Daemon](../../mobs/lesser-daemon.md)
- Can appear in common tomes in buried wizard towers
- Sold by dwarf traders (low basic tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `learnableMagics` config option (config/tensura/EliteTensura/Races.toml)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `EarthLock.castTime` | 40 | Cast time in tick. |
| `EarthLock.magiculeCost` | 100 | Magicule Cost to cast. |
| `EarthLock.range` | 10 | The range in block of the magic. |
| `EarthLock.radius` | 2 | The radius in block of where the caster targeted to be turned into solid version. |
| `EarthLock.knockbackResistance` | 0.2 | The amount of knockback resistance that the caster gains when using the Self-Lock mode when mastered. |
| `EarthLock.knockbackResistanceDuration` | 240 | The duration in tick of knockback resistance that the caster gains when using the Self-Lock mode when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/common_tome_buried_wizard_tower`, `tensura:skills/low_basic_tome_dwarf_trade`
