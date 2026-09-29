# Critical Blessing

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Critical Blessing](../../../assets/icons/trnightmare/skill/critical_blessing.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:critical_blessing` |
| **Activation** | Toggle |

</div>

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| critChance | 50 | add |
| critMultiplier | 2 | add |

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `allowedBlessings` config option (config/nightmare/ability/skill/nightmare_ult.toml): Permitted Divine Protection skills for Astraea menus and sub-skill creation.

## Tags

`tensura:skills/no_plundering`
