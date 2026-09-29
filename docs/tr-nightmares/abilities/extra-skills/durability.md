# Durability

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Durability](../../../assets/icons/trnightmare/skill/durability.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:durability` |
| **Activation** | Toggle |

</div>

> Grants immense toughness and stamina. Endure what others cannot, and keep fighting when others fall.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| armor | armor value | add |
| toughness | toughness value | add |

## Obtaining

- Listed in the `allowedSkills` config option (config/nightmare/ability/skill/nightmare_unique.toml): Permitted Laguna Skills.
- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `allowedBlessings` config option (config/nightmare/ability/skill/nightmare_ult.toml): Permitted Divine Protection skills for Astraea menus and sub-skill creation.
