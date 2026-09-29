# Fire

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Fire](../../../assets/icons/tensura/skill/fire_aspectual.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:fire_aspectual` |
| **Element** | Fire |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Shoot magic fiery projectiles.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 150 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Lesser Daemon](../../mobs/lesser-daemon.md)
- Can appear in common tomes in burnt wizard towers
- Sold by dwarf traders (low basic tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `learnableMagics` config option (config/tensura/EliteTensura/Races.toml)

## Related

- **Referenced by:** [Fire Ball](fire-ball.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Fire.castTime` | 40 | Cast time in tick. |
| `Fire.castTimeMastered` | 20 | Cast time in tick when mastered. |
| `Fire.magiculeCost` | 150 | Magicule Cost to cast. |
| `Fire.magicDamage` | 20 | The magic damage of the fire. |
| `Fire.fireDamage` | 10 | The fire damage of the fire. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/common_tome_burnt_wizard_tower`, `tensura:skills/low_basic_tome_dwarf_trade`
