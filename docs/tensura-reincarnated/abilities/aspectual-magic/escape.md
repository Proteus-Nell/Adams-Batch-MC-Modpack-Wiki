# Escape

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Escape](../../../assets/icons/tensura/skill/escape.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:escape` |
| **Element** | Space |
| **Max mastery** | 100 |
| **Cooldowns (s)** | 5 mastered, 10 otherwise |
| **Activation** | Hold |

</div>

> Connect two points in space to create a escape route.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 800 |  |

## How it works

- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Obtaining

- Can appear in common tomes in ruined wizard towers
- Sold by dwarf traders (medium upgraded tome)
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `learnableMagics` config option (config/tensura/EliteTensura/Races.toml)
- Listed in the `formulaSuccessionBlacklist` config option (config/tensuramoreskills-grand.toml): Spell registry IDs that Formula Succession is not allowed to mirror.

## Related

- **Effects:** [Anti-Magic](../../effects/anti-magic.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Escape.castTime` | 100 | Cast time in tick. |
| `Escape.magiculeCost` | 800 | Magicule Cost to cast. |
| `Escape.warpChargeTick` | 100 | The charge time in tick before warping the user. |
| `Escape.maxRange` | 500 | The max range in blocks away from the escape magic circle that the user can teleport to. |
| `Escape.maxRangeMastered` | 1,000 | The max range in blocks away from the escape magic circle that the user can teleport to when mastered. |
| `Escape.autoEscapeHP` | 0.1 | The multiplier of max HP that the user needs have below to activate the auto-escape when toggled with mastery. |
| `Escape.autoEscapeMP` | 0.01 | The multiplier of max MP that the user needs have below to activate the auto-escape when toggled with mastery. |
| `Escape.cooldown` | 10 | The cooldown in second of the magic. |
| `Escape.cooldownMastered` | 5 | The cooldown in second of the magic when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |
| `unlearntCastMultiplier` | 2 | The multiplier of cast time compared to normal cast when casting a unlearnt magic from a magic-holder item. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- The escape magic circle is too far away.

</details>

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/common_tome_ruined_wizard_tower`, `tensura:skills/medium_upgraded_tome_dwarf_trade`
