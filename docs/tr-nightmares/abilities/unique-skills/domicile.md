# Domicile

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:domicile` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 25,000 |
| **Activation** | Press |

</div>

> Domicile is a unique Space-Type Skill that allows the user to create and manage their own personal pocket dimensions. With two modes — Homestead and Shopkeeper — the user can build a safe home or establish a trading post.

## Modes

| # | Mode |
|---|---|
| 1 | Homestead |
| 2 | Shopkeeper |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Related

- **Related skills:** [The Warden](the-warden.md)
- **Summons / entities:** [Domicile Shopkeeper](../../mobs/domicile-shopkeeper.md)

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

## In-game messages

<details markdown><summary>Show 8 messages</summary>

- You must look at a door or trapdoor to activate Homestead mode!
- Shopkeeper removed.
- You are not the owner of this domicile!
- Could not find return position!
- Door linked to your domicile!
- Shopkeeper summoned!
- No trades available! Place items in chests and stock in a barrel.
- This shopkeeper is currently trading with someone else!

</details>
