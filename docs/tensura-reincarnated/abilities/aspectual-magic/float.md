# Float

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Float](../../../assets/icons/tensura/skill/float.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:float` |
| **Element** | Gravity |
| **Modes** | 2 |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Decrease the caster's gravity to float.

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

- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Obtaining

- Sold by dwarf traders (low upgraded tome)
- Can appear in uncommon tomes in buried wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Float.castTime` | 40 | Cast time in tick. |
| `Float.magiculeCost` | 100 | Magicule Cost to cast. |
| `Float.levitationDuration` | 200 | The duration in tick of the Levitation effect to apply on the caster. |
| `Float.levitationLevel` | 1 | The level of the Levitation effect to apply on the caster. |
| `Float.projectileDamage` | 25 | The magic damage of the projectile. |
| `Float.projectileDuration` | 200 | The duration in tick of the Levitation effect of the projectile. |
| `Float.projectileLevel` | 1 | The level of the Levitation effect of the projectile. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/low_upgraded_tome_dwarf_trade`, `tensura:skills/uncommon_tome_buried_wizard_tower`
