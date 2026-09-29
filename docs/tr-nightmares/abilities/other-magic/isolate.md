# Isolate

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Other Magic](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Other Magic |
| **ID** | `trnightmare:isolate` |
| **Activation** | Hold |

</div>

> A holy magic that isolates a target from outside interference and support.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 15,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Can be found in skill tomes
- Can appear in rare tomes in buried wizard towers
- Can appear in rare tomes in rotted wizard towers
- Can appear in rare tomes in ruined wizard towers

## Related

- **Effects:** [Isolate](../../effects/isolate.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/magic/holy.toml`](../../configs/config-nightmare-ability-magic-holy.md).

| Option | Default | Description |
|---|---|---|
| `Isolate.castTime` | 6 | Cast time in seconds. |
| `Isolate.magiculeCost` | 15,000 | Magicule Cost to cast. |
| `Isolate.spiritronCost` | 10 | Spiritron Cost to cast. |
| `Isolate.debuffPercentage` | 10 | Percentage of magicule cost added per level of Isolate Effect. |
| `Isolate.isolateLevel` | 2 | Level of Isolate applied. |
| `Isolate.isolateLevelMastered` | 3 | Isolate level applied on Mastery. |
| `Isolate.range` | 5 | The block range of the spell unmastered. |
| `Isolate.rangeMastered` | 7 | The block range of the spell mastered. |
| `Isolate.isolateDuration` | 60 | Effect duration of Isolate in seconds. |

## Tags

`tensura:skills/found_in_tome`, `tensura:skills/magic`, `tensura:skills/rare_tome_buried_wizard_tower`, `tensura:skills/rare_tome_rotted_wizard_tower`, `tensura:skills/rare_tome_ruined_wizard_tower`
