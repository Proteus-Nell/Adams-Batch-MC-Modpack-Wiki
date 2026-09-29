# Flight

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Flight](../../../assets/icons/tensura/skill/flight.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:flight` |
| **Element** | Misc |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Propel the caster forward in the air.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 |  |

## How it works

- Charged or channelled by holding the skill key

## Obtaining

- Sold by dwarf traders (low rare tome)
- Can appear in rare tomes in burnt wizard towers

## Related

- **Effects:** [Magic Interference](../../effects/magic-interference.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Flight.castTime` | 60 | Cast time in tick. |
| `Flight.magiculeCost` | 500 | Magicule Cost per second to cast. |
| `Flight.pushForce` | 0.05 | The push force on the caster when held down. |
| `Flight.flightDuration` | 200 | The max duration in tick that the magic can be used. |
| `Flight.flightDurationMastered` | 300 | The max duration in tick that the magic can be used when mastered. |

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
