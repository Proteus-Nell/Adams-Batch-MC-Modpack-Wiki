# Fire Storm

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Fire Storm](../../../assets/icons/tensura/skill/fire_storm.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:fire_storm` |
| **Element** | Fire |
| **Modes** | 2 |
| **Max mastery** | 700 |
| **Cooldowns (s)** | 5 mastered, 7 otherwise |
| **Activation** | Press, Hold |

</div>

> Call forth fiery surges of flame to incinerate targets.

## Modes

| # | Mode |
|---|---|
| 1 | Condensed |
| 2 | Spread |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (high basic tome)
- Can appear in uncommon tomes in burnt wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Summons / entities:** Fire Jail
- **Referenced by:** [Sunshine](../../../tr-nightmares/abilities/unique-skills/sunshine.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `FireStorm.castTime` | 100 | Cast time in tick. |
| `FireStorm.magiculeCost` | 10,000 | Magicule Cost to cast. |
| `FireStorm.range` | 20 | The range in block of the Condensed mode. |
| `FireStorm.width` | 15 | The width radius of the Fire Storm in Spread mode. |
| `FireStorm.height` | 10 | The surge height of the Fire  Storm in Spread mode. |
| `FireStorm.magicDamage` | 20 | The magic damage of the Fire Storm in Spread mode. |
| `FireStorm.fireDamage` | 30 | The fire damage of the Fire Storm in Spread mode. |
| `FireStorm.magicSurgeDamage` | 200 | The magic Surge damage of the Fire Storm in Spread mode. |
| `FireStorm.fireSurgeDamage` | 50 | The fire Surge damage of the Fire Storm in Spread mode. |
| `FireStorm.damageInterval` | 10 | The damaging interval in ticks of the Fire Storm in Spread mode. |
| `FireStorm.surgeInterval` | 30 | The surge interval in ticks of the Fire Storm in Spread mode. |
| `FireStorm.stormDuration` | 150 | The duration in ticks of the Fire Storm in Spread mode. |
| `FireStorm.condensedSize` | 5 | The size of the Fire Storm in Condensed mode. |
| `FireStorm.condensedInterval` | 20 | The damaging interval in ticks of the Fire Storm in Condensed mode. |
| `FireStorm.magicCondensedDamage` | 300 | The magic damage of the Fire Storm in Condensed mode. |
| `FireStorm.fireCondensedDamage` | 100 | The fire damage of the Fire Storm in Condensed mode. |
| `FireStorm.condensedDuration` | 40 | The duration in ticks of the Fire Storm in Condensed mode. |
| `FireStorm.cooldown` | 7 | The cooldown in second of the magic. |
| `FireStorm.cooldownMastered` | 5 | The cooldown in second of the magic when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/high_basic_tome_dwarf_trade`, `tensura:skills/uncommon_tome_burnt_wizard_tower`
