# Elegy

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Elegy](../../../assets/icons/trnightmare/skill/elegy.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:elegy` |
| **Modes** | 3 |
| **Cooldowns (s)** | 60, 10 |
| **Activation** | Press |

</div>

> Elegy is a Space-Time Manipulation power with such fine control that one could move an individual's soul.

## Modes

| # | Mode |
|---|---|
| 1 | Barrier Refinement |
| 2 | Counter Barrier |
| 3 | Stability |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 or base cost |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you die
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Objects.requireNonNull(living.getAttribute(TensuraAttributes.MULTILAYER_BARRIER)) | 1 | multiply total |
| Objects.requireNonNull(entity.getAttribute(TensuraAttributes.MULTILAYER_BARRIER)) | -100 × mult | add |

## Related

- **Related skills:** [Multilayer Barrier](../../../tensura-reincarnated/abilities/extra-skills/multilayer-barrier.md), [Spatial Manipulation](../../../tensura-reincarnated/abilities/extra-skills/spatial-manipulation.md), [Spatial Motion](../../../tensura-reincarnated/abilities/extra-skills/spatial-motion.md)
- **Referenced by:** [｢ Lilith, Lord of Heresy ｣](../ultimate-skills/lilith.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Elegy.mpAcquirement` | 90,000 | Magicule Acquirement Cost. |
| `Elegy.refinementMultiplier` | 2 | Multiplier for Barrier Refinement. |
| `Elegy.magiculeCostCounter` | 100 | Magicule Cost to activate Counter Barrier. |
| `Elegy.barrierCostCounter` | 100 | Barrier Cost to activate Counter Barrier. |
| `Elegy.stabilityMagicule` | 100 | Magicules per Barrier point from Stability. |
| `Elegy.stabilityHealth` | 5 | Health per Barrier point from Stability. |
| `Elegy.counterCooldown` | 10 | Cooldown for activating Counter Barrier. |
| `Elegy.stabilityCooldown` | 60 | Cooldown for activating Stability. |
