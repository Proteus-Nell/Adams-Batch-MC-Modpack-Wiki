# Mystic Aura

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Mystic Aura](../../../assets/icons/trnightmare/skill/mystic_aura.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:mystic_aura` |
| **Modes** | 1 |
| **Cooldowns (s)** | 10 |
| **Activation** | Press |

</div>

> Combining Aura and Magic results in a mystic art... Not even the antithesis to skills can resist.

## Modes

| # | Mode |
|---|---|
| 1 | Mystic |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Related

- **Effects:** [Mystic Aura](../../effects/mystic-aura.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `MysticAura.mpAcquirement` | 1,000 | Magicule Acquirement Cost. |
| `MysticAura.mpCost` | 500 | Percentage of Magicules regenerated every 5 seconds. |
| `MysticAura.requiredMagics` | 20 | Number of Mastered Spells required to obtain. |
| `MysticAura.requiredBattlewills` | 10 | Number of Mastered Battlewills required to obtain. |
| `MysticAura.durationUnmastered` | 30 | Duration in Seconds the effect will last when unmastered. |
