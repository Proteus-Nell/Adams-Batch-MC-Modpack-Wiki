# Wind Protection

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Wind Protection](../../../assets/icons/tensura/skill/wind_protection.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:wind_protection` |
| **Element** | Wind |
| **Max mastery** | 300 |
| **Activation** | Hold |

</div>

> Call forth flows of wind to coat the caster with speed and protection.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |

## How it works

- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Obtaining

- Can appear in common tomes in ruined wizard towers
- Sold by dwarf traders (medium basic tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `WindProtection.castTime` | 60 | Cast time in tick. |
| `WindProtection.magiculeCost` | 1,000 | Magicule Cost to cast. |
| `WindProtection.effectLevel` | 1 | The level of the Wind's Protection effect. |
| `WindProtection.effectDuration` | 2,400 | The duration in tick of the Wind's Protection effect. |
| `WindProtection.effectLevelMastered` | 3 | The level of the Wind's Protection effect when mastered. |
| `WindProtection.effectDurationMastered` | 3,600 | The duration in tick of the Wind's Protection effect when mastered. |
| `WindProtection.effectSpeed` | 0.2 | The speed boost multiplier of the Wind's Protection effect per level. |
| `WindProtection.effectDodge` | 100 | The projectile dodge chance of the Wind's Protection effect per level. |
| `WindProtection.effectKnockback` | 0.1 | The knockback resistance of the Wind's Protection effect per level (start from level 2). |
| `WindProtection.effectBurn` | 0.5 | The burning time percentage reduction of the Wind's Protection effect per level (start from level 2). |
| `WindProtection.effectFlameBoost` | 0.1 | The flame attack boost multiplier of the Wind's Protection effect per level (start from level 2). |

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

`tensura:skills/aspectual_magic`, `tensura:skills/common_tome_ruined_wizard_tower`, `tensura:skills/medium_basic_tome_dwarf_trade`
