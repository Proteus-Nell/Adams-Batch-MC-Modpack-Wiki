# Wind Reading

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Wind Reading](../../../assets/icons/trnightmare/skill/wind_reading.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:wind_reading` |
| **Activation** | Toggle |

</div>

> Read the flow of battle like the wind itself. Improves reaction speed and awareness of enemy actions.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers on melee contact

## Obtaining

- Listed in the `allowedSkills` config option (config/nightmare/ability/skill/nightmare_unique.toml): Permitted Laguna Skills.
- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `allowedBlessings` config option (config/nightmare/ability/skill/nightmare_ult.toml): Permitted Divine Protection skills for Astraea menus and sub-skill creation.

## Related

- **Effects:** [Presence Concealment](../../../tensura-reincarnated/effects/presence-concealment.md), [Presence Sense](../../../tensura-reincarnated/effects/presence-sense.md)
