# Mud Spears

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Mud Spears](../../../assets/icons/tensura/skill/mud_spears.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:mud_spears` |
| **Element** | Earth |
| **Modes** | 2 |
| **Max mastery** | 700 |
| **Cooldowns (s)** | 1 mastered, 3 otherwise |
| **Activation** | Hold |

</div>

> Raise mud spikes from the ground to pierce through your enemies.

## Modes

| # | Mode |
|---|---|
| 1 | Spread Mode |
| 2 | Targeted Mode |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 70,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Arch Daemon](../../mobs/arch-daemon.md)
- Sold by dwarf traders (high basic tome)
- Can appear in rare tomes in buried wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Related skills:** [Mud Hand](mud-hand.md)
- **Effects:** [Anti-Magic](../../effects/anti-magic.md), [Movement Interference](../../effects/movement-interference.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `MudSpears.castTime` | 80 | Cast time in tick. |
| `MudSpears.castTimeMudHand` | 40 | Cast time in tick when Mud Hand is already casted. |
| `MudSpears.magiculeCost` | 70,000 | Magicule Cost to cast. |
| `MudSpears.range` | 20 | The range in block of the magic. |
| `MudSpears.magicDamage` | 250 | The magic damage of each mud spike. |
| `MudSpears.magicDamageBonus` | 50 | The bonus magic damage of each mud spike if Mud Hand is already casted. |
| `MudSpears.earthDamage` | 50 | The earth damage of each mud spike. |
| `MudSpears.spreadDamage` | 20 | The earth damage of each mud spike casted from Spread Mode. |
| `MudSpears.spreadDuration` | 600 | The duration in tick of each mud spike casted from Spread Mode. |
| `MudSpears.spreadRadius` | 5 | The radius in block of the Spread Mode. |
| `MudSpears.cooldown` | 3 | The cooldown in second of the magic in the default mode. |
| `MudSpears.cooldownMastered` | 1 | The cooldown in second of the magic in the default mode when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/high_basic_tome_dwarf_trade`, `tensura:skills/rare_tome_buried_wizard_tower`
