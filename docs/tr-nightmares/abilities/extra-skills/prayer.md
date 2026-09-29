# Prayer

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:prayer` |
| **Activation** | Hold |

</div>

> Harvest the belief of your subordinates to generate holy energy and use holy spells

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |

## How it works

- Charged or channelled by holding the skill key

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -1 | multiply total |

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `Prayer.mpAcquirement` | 10,000 | Magicule Acquirement Cost. |
| `Prayer.mpCost` | 1,000 | Magicule Cost per second. |
| `Prayer.spPerSub` | 1 | Number of Spiritrons generated per subordinate. |
| `Prayer.spMax` | 8 | Maximum number of Spiritrons that can be generated per 5 seconds. |
