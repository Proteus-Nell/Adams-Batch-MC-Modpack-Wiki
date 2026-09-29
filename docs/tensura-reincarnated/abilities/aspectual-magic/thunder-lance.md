# Thunder Lance

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Thunder Lance](../../../assets/icons/tensura/skill/thunder_lance.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:thunder_lance` |
| **Element** | Lightning |
| **Modes** | 2 |
| **Max mastery** | 300 |
| **Cooldowns (s)** | casting time(80, false) ÷ 20 |
| **Activation** | Press, Hold |

</div>

> Strike powerful thunder lances of magic.

## Modes

| # | Mode |
|---|---|
| 1 | Rain |
| 2 | Single |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (medium upgraded tome)
- Can appear in uncommon tomes in ruined wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Referenced by:** [Static Chain](../../../elite-tensura/abilities/aspectual-magic/static-chain.md), [Kamehameha](../../../elite-tensura/abilities/aspectual-magic/kamehameha.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `ThunderLance.castTime` | 80 | Cast time in tick. |
| `ThunderLance.magiculeCost` | 5,000 | Magicule Cost to cast. |
| `ThunderLance.magicDamage` | 50 | The magic damage of the lance. |
| `ThunderLance.lightningDamage` | 30 | The lightning damage of the lance. |
| `ThunderLance.rainRadius` | 5 | The radius in block of the Rain mode. |
| `ThunderLance.rainNumber` | 10 | The number of lances to shoot from Rain mode. |
| `ThunderLance.magicDamageRain` | 30 | The magic damage of each rain lance. |
| `ThunderLance.lightningDamageRain` | 30 | The lightning damage of each rain lance. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/medium_upgraded_tome_dwarf_trade`, `tensura:skills/uncommon_tome_ruined_wizard_tower`
