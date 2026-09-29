# Spatial Motion

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Spatial Motion](../../../assets/icons/tensura/skill/spatial_motion.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:spatial_motion` |
| **Modes** | 2 |
| **Cooldowns (s)** | 2 mastered, 5 otherwise |
| **Activation** | Press |

</div>

> Tear space asunder granting yourself and your allies safe passage.

## Modes

| # | Mode |
|---|---|
| 1 | Blink |
| 2 | Warp |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10 |  |

## How it works

- Activated by pressing the skill key
- Does something when first learned
- Does something when mastered

## Obtaining

- Can be learned by: [6 Tailed Fox](../../../ascension/races/six-tail-fox.md), [9 Tailed Fox](../../../ascension/races/nine-tail-fox.md), [Divine Kitsune](../../../ascension/races/divine-kitsune.md), [Elder Bloodfiend](../../../ascension/races/elder-bloodfiend.md), [Progenitor Bloodfiend](../../../ascension/races/progenitor-bloodfiend.md), [Phantom Djinn](../../../ascension/races/phantom-djinn.md), [Royal Djinn](../../../ascension/races/royal-djinn.md), [Wishbound Djinn](../../../ascension/races/wishbound-djinn.md), [Primordial Djinn](../../../ascension/races/primordial-djinn.md), [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md), [Phantom Corsair](../../../ascension/races/phantom-corsair.md), [Davy Jones](../../../ascension/races/davy-jones.md), [Ender Dragonewt](../../../ascension/races/ender-dragonewt.md), [Void Dragonewt](../../../ascension/races/void-dragonewt.md), [Abyssal Dragonewt](../../../ascension/races/abyssal-dragonewt.md), [Chaos Dragon](../../../ascension/races/chaos-dragon.md)
- Innate to mobs: [Mai Furuki](../../mobs/mai-furuki.md)

## Related

- **Related skills:** [Spatial Manipulation](spatial-manipulation.md)
- **Referenced by:** [Gate](../spiritual-magic/gate.md), [Warp Portal](../aspectual-magic/warp-portal.md), [Elegy](../../../tr-nightmares/abilities/unique-skills/elegy.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `SpatialMotion.magiculeCost` | 10 | Base Magicule Cost to teleport per block. |
| `SpatialMotion.magiculeCostPortal` | 50 | Base Magicule Cost to teleport per block using portal. |
| `SpatialMotion.blinkRange` | 30 | The maximum Blink range in block. |
| `SpatialMotion.blinkRangeMastered` | 50 | The maximum Blink range in block when mastered. |
| `SpatialMotion.blinkCooldown` | 5 | The cooldown for Blink Mode. |
| `SpatialMotion.blinkCooldownMastered` | 2 | The cooldown for Blink Mode when mastered. |
| `SpatialMotion.warpChargeTick` | 100 | The charge tick of the warp mode before warping any entity. |
| `SpatialMotion.warpChargeTickMastered` | 0 | The charge tick of the warp mode before warping any entity when mastered. |
| `SpatialMotion.warpCooldown` | 20 | The cooldown for Warp Mode. |
| `SpatialMotion.warpCooldownMastered` | 10 | The cooldown for Warp Mode when mastered. |

## Tags

`tensura:skills/extra_skills`, `tensura:skills/space_skills`
