# Ideal

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Ideal](../../../assets/icons/trnightmare/skill/ideal.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:ideal` |
| **Activation** | Toggle |

</div>

> After refining your craft for so long, you have finally reached an ideal, your attacks will always land.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| critical | 100 or 60 | add |

## Obtaining

- Listed in the `intrinsicSkills` config option (config/nightmare/race/scholar_config.toml): List of skills obtained by this race.
- Listed in the `allowedSkills` config option (config/nightmare/ability/skill/nightmare_unique.toml): List of skills Handler is allowed to upgrade. (is every skill it can by default)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `Ideal.mpAcquirement` | 10,000 | Magicule Acquirement Cost. |
| `Ideal.critChance` | 60 | Critical Attack Chance. |
| `Ideal.luckMultiplier` | 1 | Level of Luck granted passively by ideal. |
