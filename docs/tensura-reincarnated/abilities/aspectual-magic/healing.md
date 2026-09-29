# Healing

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Healing](../../../assets/icons/tensura/skill/healing.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:healing` |
| **Element** | Recovery |
| **Max mastery** | 300 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Hold |

</div>

> Heal a living being on a low level.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (low rare tome)
- Can appear in uncommon tomes in frozen wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Referenced by:** [Healing Rain](healing-rain.md), [Recovery](recovery.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Healing.castTime` | 60 | Cast time in tick. |
| `Healing.castTimeMastered` | 30 | Cast time in tick when mastered. |
| `Healing.minCost` | 1,000 | Minimal Magicule Cost to cast. |
| `Healing.magiculeCost` | 100 | Magicule Cost  to heal each HP. |
| `Healing.range` | 6 | The range in block of the magic. |
| `Healing.hpHeal` | 50 | The amount of HP that the magic heals. |
| `Healing.hpHealMastered` | 100 | The amount of HP that the magic heals when mastered. |
| `Healing.hpHealPercentage` | 0.25 | The percentage of max HP that the magic heals when mastered (if higher than 100). |
| `Healing.cooldown` | 5 | The cooldown in second when activated Healing. |
| `Healing.cooldownMastered` | 3 | The cooldown in second when activated Healing with mastery. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/low_rare_tome_dwarf_trade`, `tensura:skills/uncommon_tome_frozen_wizard_tower`
