# Concentrator

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Concentrator](../../../assets/icons/trnightmare/skill/concentrator.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:concentrator` |
| **Activation** | Hold |

</div>

> Through rigorous study of the grimoire you discovered, you are now able to subconscious absorb surrounding magicules.

## How it works

- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Listed in the `allowedSkills` config option (config/nightmare/ability/skill/nightmare_unique.toml): List of skills Handler is allowed to upgrade. (is every skill it can by default)

## Related

- **Referenced by:** [Lemegeton](../unique-skills/lemegeton.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `Concentrator.mpAcquirement` | 10,000 | Magicule Acquirement Cost. |
| `Concentrator.magiculeRegenPercent` | 0.5 | Percentage of Magicules regenerated every 5 seconds. |
| `Concentrator.epRequirement` | 1,000,000 | Number of Existence Points the player must have to meet the natural requirements. |
