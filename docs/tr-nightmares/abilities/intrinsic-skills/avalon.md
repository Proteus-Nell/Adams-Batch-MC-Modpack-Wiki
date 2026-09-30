# Avalon

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Avalon](../../../assets/icons/trnightmare/skill/avalon.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:avalon` |
| **Activation** | Toggle |

</div>

> Blessed by the Fae, you often avoid getting hit by attacks

## How it works

- Can be toggled on and off
- Triggers when you are attacked

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| melee | 50 | add |
| projectile | 50 | add |

## Obtaining

- Listed in the `intrinsicSkills` config option (config/nightmare/race/scholar_config.toml): List of skills obtained by this race.
- Listed in the `allowedSkills` config option (config/nightmare/ability/skill/nightmare_unique.toml): List of skills Handler is allowed to upgrade. (is every skill it can by default)

## Related

- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `Avalon.mpAcquirement` | 10,000 | Magicule Acquirement Cost. |
| `Avalon.dodgeChance` | 50 | Dodge chance for Non-Magical attacks out of 100. |
| `Avalon.projectileChance` | 50 | Dodge chance for Projectile attacks out of 100. |
