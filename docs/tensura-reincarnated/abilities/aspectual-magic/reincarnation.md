# Reincarnation

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Reincarnation](../../../assets/icons/tensura/skill/reincarnation.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:reincarnation` |
| **Element** | Misc |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Sacrifice a portion of the caster's power to reincarnate.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Can appear in epic tomes from wizard towers
- Listed in the `costFloorBlacklist` config option (config/tensura/EliteTensura/UniqueSkillConfig.toml): Spell registry IDs excluded from the in-slot cost floor (kept at full cost).

## Related

- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Reincarnation.castTime` | 200 | Cast time in tick. |
| `Reincarnation.minimalMagicule` | 10,000 | The minimal Magicule cost to cast. |
| `Reincarnation.auraCost` | 0.25 | The Max Aura multiplier of the caster to be consumed for this magic. |
| `Reincarnation.magiculeCost` | 0.25 | The Max Magicule multiplier of the caster to be consumed for this magic. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/epic_tome_wizard_tower`, `tensura:skills/unlearnt_cast_excluded`
