# Stone Shot

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Stone Shot](../../../assets/icons/tensura/skill/stone_shot.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:stone_shot` |
| **Element** | Earth |
| **Modes** | 2 |
| **Max mastery** | 700 |
| **Cooldowns (s)** | 1 mastered, 3 otherwise |
| **Activation** | Press, Hold |

</div>

> Shoot rock spikes toward targets.

## Modes

| # | Mode |
|---|---|
| 1 | Chain Mode |
| 2 | Spread Mode |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 45,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Arch Daemon](../../mobs/arch-daemon.md), [Greater Daemon](../../mobs/greater-daemon.md), [Lesser Daemon](../../mobs/lesser-daemon.md)
- Sold by dwarf traders (high basic tome)
- Can appear in uncommon tomes in buried wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Referenced by:** [Gaia, Lord of Earth](../../../elite-tensura/abilities/ultimate-skills/gaia.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `StoneShot.castTime` | 80 | Cast time in tick. |
| `StoneShot.magiculeCost` | 45,000 | Magicule Cost to cast. |
| `StoneShot.stoneNumber` | 3 | The number of stones to shoot each usage. |
| `StoneShot.magicDamage` | 150 | The magic damage of each stone shot. |
| `StoneShot.earthDamage` | 50 | The earth damage of each stone shot. |
| `StoneShot.cooldown` | 3 | The cooldown in second of the magic in the default mode. |
| `StoneShot.cooldownMastered` | 1 | The cooldown in second of the magic in the default mode when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/high_basic_tome_dwarf_trade`, `tensura:skills/uncommon_tome_buried_wizard_tower`
