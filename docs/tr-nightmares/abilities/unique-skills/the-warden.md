# The Warden

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:the_warden` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 25,000 |
| **Activation** | Press |

</div>

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Mode 2 |
| 3 | Mode 3 |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Related

- **Referenced by:** [Domicile](domicile.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_common.toml`](../../configs/config-nightmare-ability-skill-nightmare-common.md).

| Option | Default | Description |
|---|---|---|
| `Domicile.epAcquirement` | 250,000 | EP requirement for natural learning. |
| `Domicile.mpAcquirement` | 25,000 | Minimum base max magicule required to learn. |
| `Domicile.magiculeCost` | 0 | Magicule cost to activate. |
| `Domicile.cooldown` | 10 | Cooldown in seconds after activation. |
| `TheWarden.epAcquirement` | 500,000 | EP requirement for natural learning. |
| `TheWarden.mpAcquirement` | 50,000 | Minimum base max magicule required to learn. |
| `TheWarden.magiculeCost` | 0 | Magicule cost to activate. |
| `TheWarden.cooldown` | 30 | Cooldown in seconds after activation. |
| `TheWarden.masteryPerVisitorTick` | 0.1 | Mastery gained per tick when other players are in your shopkeeper dimension. |
| `TheWarden.masteryPerDoorConversion` | 0.5 | Mastery gained per door conversion. |
| `TheWarden.visitorMasteryInterval` | 100 | Ticks between mastery gains from visitors. |
