# Overdrive

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Other Magic](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Other Magic |
| **ID** | `trnightmare:overdrive` |
| **Activation** | Hold |

</div>

> Overload enemy spells and use them for yourself.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 25,000 |  |

## How it works

- Triggers when the held key is released

## Stats (config defaults)

Set in [`config/nightmare/ability/magic/holy.toml`](../../configs/config-nightmare-ability-magic-holy.md).

| Option | Default | Description |
|---|---|---|
| `Overdrive.castTime` | 3 | Cast time in seconds. |
| `Overdrive.magiculeCost` | 25,000 | Magicule Cost to cast. |
| `Overdrive.spiritronCost` | 15 | Spiritron Cost to cast. |
| `Overdrive.range` | 12 | The block range of the spell unmastered. |
| `Overdrive.rangeMastered` | 30 | The block range of the spell mastered. |

## Tags

`tensura:skills/magic`, `tensura:skills/tome_copy_excluded`
