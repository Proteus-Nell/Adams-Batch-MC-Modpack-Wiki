# Domicile

<small>[TR: Nightmares](../index.md) &rsaquo; [Dimensions](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:domicile` |
| **Dimension type** | `trnightmare:domicile` |
| **Generator** | `minecraft:flat` |
| **Has skylight** | True |
| **Has ceiling** | False |
| **Ultrawarm** | False |
| **Natural** | True |
| **Piglin safe** | False |
| **Bed works** | True |
| **Respawn anchor works** | False |
| **Has raids** | False |
| **Min y** | -64 |
| **Height** | 384 |
| **Ambient light** | 0.0 |
| **Coordinate scale** | 1.0 |

</div>

## What it does

The template for the personal pocket worlds made by the [Domicile](../abilities/unique-skills/domicile.md) skill. Every player who uses it gets two of their own: a **Homestead** (a house) and a **Shop**. They are built from a saved structure the first time you enter, then stay as you leave them.

**Getting in:** look at any door or trapdoor within 5 blocks and use the skill. The door turns into a [Domicile Door](../blocks/domicile-door.md) (or [Domicile Trapdoor](../blocks/domicile-trapdoor.md)) linked to you, and you step inside: Homestead mode for the house, Shopkeeper mode for the shop. Linking a new door reverts your old one to a plain oak door. After that, **anyone** who walks through the open linked door is taken to your domicile. Use the skill again inside, or open the door inside, to go back out through your linked door.

**Inside:**

- Nothing can take damage.
- Only you, your allies and your subordinates can place or break blocks, and only you can open chests, barrels, furnaces, hoppers and other containers. The linked doors can't be broken.
- The chunk you stand in stays loaded while the skill is active.
- In the shop, Shopkeeper mode summons an invulnerable Domicile Shopkeeper that sells what you stock in its chests and barrel (Shift + use on it to remove it). If you have [The Warden](../abilities/unique-skills/the-warden.md), it gains mastery for every visitor in your shop and every door you convert.

**Commands:** `/domicile` (Homestead) and `/domicilestore` (Shop) let the owner kick a player, or everyone not on their whitelist, back to world spawn. The whitelist only matters for that kick: the blacklist, lock and safety settings are saved, but nothing reads them in this version, so they don't keep anyone out. Operators can rebuild someone's Homestead or Shop with `/resetdomicile <players> base|shop`.
