# Airflow Shut

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Airflow Shut](../../../assets/icons/tensura/skill/airflow_shut.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:airflow_shut` |
| **Element** | Wind |
| **Modes** | 2 |
| **Max mastery** | 300 |
| **Activation** | Press, Hold |

</div>

> Drain out all the air surrounding the targets and suffocate them.

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Mode 2 |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 3,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Sold by dwarf traders (medium basic tome)
- Can appear in uncommon tomes in ruined wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Effects:** [Silence](../../effects/silence.md)
- **Summons / entities:** Air Jail

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `AirflowShut.castTime` | 100 | Cast time in tick. |
| `AirflowShut.castTimeMastered` | 80 | Cast time in tick when mastered. |
| `AirflowShut.castTimeHold` | 20 | Cast time in tick between effect inflicting when held down. |
| `AirflowShut.magiculeCost` | 3,000 | Magicule Cost to cast. |
| `AirflowShut.magiculeCostHold` | 1,300 | Magicule Cost to hold down each 20 ticks (castTimeHold). |
| `AirflowShut.range` | 20 | The range in block of the magic. |
| `AirflowShut.sphereSize` | 5 | The size in block of the Air Sphere. |
| `AirflowShut.sphereSizeMastered` | 8 | The size in block of the Air Sphere from the Expanded Mode. |
| `AirflowShut.silenceLevel` | 1 | The level of the Silence effect. |
| `AirflowShut.silenceDuration` | 100 | The duration in tick of the Silence effect. |
| `AirflowShut.sphereDuration` | 200 | The duration in tick of the Air Sphere after casting. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/medium_basic_tome_dwarf_trade`, `tensura:skills/uncommon_tome_ruined_wizard_tower`
