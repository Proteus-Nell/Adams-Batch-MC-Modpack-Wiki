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

## What it does

The template for the personal pocket worlds made by the [Domicile](domicile.md) skill. Every player who uses it gets two of their own: a **Homestead** (a house) and a **Shop**. They are built from a saved structure the first time you enter, then stay as you leave them.

**Getting in:** look at any door or trapdoor within 5 blocks and use the skill. The door turns into a [Domicile Door](../../blocks/domicile-door.md) (or [Domicile Trapdoor](../../blocks/domicile-trapdoor.md)) linked to you, and you step inside: Homestead mode for the house, Shopkeeper mode for the shop. Linking a new door reverts your old one to a plain oak door. After that, **anyone** who walks through the open linked door is taken to your domicile. Use the skill again inside, or open the door inside, to go back out through your linked door.

**Inside:**

- Nothing can take damage.
- Only you, your allies and your subordinates can place or break blocks, and only you can open chests, barrels, furnaces, hoppers and other containers. The linked doors can't be broken.
- The chunk you stand in stays loaded while the skill is active.
- In the shop, Shopkeeper mode summons an invulnerable Domicile Shopkeeper that sells what you stock in its chests and barrel (Shift + use on it to remove it). If you have [The Warden](the-warden.md), it gains mastery for every visitor in your shop and every door you convert.

**Commands:** `/domicile` (Homestead) and `/domicilestore` (Shop) let the owner kick a player, or everyone not on their whitelist, back to world spawn. The whitelist only matters for that kick: the blacklist, lock and safety settings are saved, but nothing reads them in this version, so they don't keep anyone out. Operators can rebuild someone's Homestead or Shop with `/resetdomicile <players> base|shop`.

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
