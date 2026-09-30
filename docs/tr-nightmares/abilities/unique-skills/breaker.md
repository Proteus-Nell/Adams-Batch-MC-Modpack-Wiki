# Breaker

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:breaker` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 90,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> A unique skill focused on shattering enemy techniques, barriers, and resistances.

## Modes

| # | Mode |
|---|---|
| 1 | Bullet Break |
| 2 | Limitless Space |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage

## Obtaining

- Listed in the `astralExtraUniqueSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Extra unique skill IDs merged into Astral Light Skill Creation (after Tensura Creator).

## Related

- **Effects:** [Mystic Aura](../../effects/mystic-aura.md), [Spatial Blockade](../../../tensura-reincarnated/effects/spatial-blockade.md)
- **Summons / entities:** Bouncing Aura Bullet
- **Referenced by:** [｢ Abaddon, King of Destruction ｣](../ultimate-skills/abaddon.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Breaker.mpAcquirement` | 90,000 | Magicule Acquirement Cost for Breaker. |
| `Breaker.BreakerMPRegenMulti` | 20 | Magicule regen multiplier while Boundary Breaker is active (mode 0). |
| `Breaker.BreakerAPRegenMulti` | 20 | Aura regen multiplier while Boundary Breaker is active (mode 0). |
