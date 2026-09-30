# Dragon Factor Haki

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:dragon_factor_haki` |
| **Modes** | 2 |
| **Activation** | Press, Hold |

</div>

> An elemental draconic haki. Toggle Elemental Boon for damage, keep it in-slot for Elemental Guard, and hold it to release Dragon Haki. Gain an element on becoming an Element Dragon; the zombie dragon line forces Corrosion.

## Modes

| # | Mode |
|---|---|
| 1 | Elemental Boon |
| 2 | Elemental Guard |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers on melee contact
- Triggers when you take damage
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| attribute | amount | op |
| armor | armor bonus | add |
| attackDamage | attack bonus | add |
| poisonResist | 0.15 | multiply total |
| heatResist | 0.15 | multiply total |
| physicalResist | 0.15 | multiply total |
| headResist | 0.15 | multiply total |
| attr | 1 | add |
| attrxx | water magic cost multiplier | multiply total |
| attrx | hp bonus | add |
| melee | wind melee dodge bonus | add |
| projectile | wind projectile dodge bonus | add |
| negate | wind dodge negate bonus | add |
| attr | light magicule regen bonus | add |

## Obtaining

- Intrinsic skill of: [Element Dragon](../../races/element-dragon.md)

## Related

- **Related skills:** [Infinite Regeneration](../../../tensura-reincarnated/abilities/extra-skills/infinite-regeneration.md), [Confusion](../../../tensura-reincarnated/abilities/aspectual-magic/confusion.md)
- **Effects:** [Rotting](../../effects/rotting.md), [Paralysis](../../../tensura-reincarnated/effects/paralysis.md), [Fragility](../../../tensura-reincarnated/effects/fragility.md), [Spatial Blockade](../../../tensura-reincarnated/effects/spatial-blockade.md), [Holy Damage](../../../tensura-reincarnated/effects/holy-damage.md), [Corrosion](../../../tensura-reincarnated/effects/corrosion.md)
- **Summons / entities:** Tensura, Trnightmare, Blood Ray

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `DragonFactorHaki.factorBonusEpThreshold` | 1,200,000 | EP required for Factor Bonus effects. |
| `DragonFactorHaki.earthFactorBonusMaxEp` | 2,000,000 | Max EP counted for Earth HP scaling. |
| `DragonFactorHaki.boonFlatDamage` | 50 | Elemental Boon flat damage for non-corrosion elements. |
| `DragonFactorHaki.bloodFactorFlatBonus` | 75 | Flat bonus applied to Blood Ray and Blood Drain damage for Vampiric Factor. |
| `DragonFactorHaki.boonCorrosionMultiplier` | 3 | Elemental Boon multiplier for Corrosion. |
| `DragonFactorHaki.corrosionRegenLockTicks` | 200 | Infinite Regeneration lock cooldown ticks applied by Corrosion Factor Bonus. |
| `DragonFactorHaki.fireDurabilityDamageMultiplier` | 4 | Fire Factor Bonus durability damage multiplier. |
| `DragonFactorHaki.waterMagicCostMultiplier` | -0.5 | Water Factor Bonus: MAGIC_COST_MULTIPLIER additive multiplier. |
| `DragonFactorHaki.earthHpPer100k` | 50 | Earth Factor Bonus HP per 100k EP over threshold. |
| `DragonFactorHaki.windMeleeDodgeBonus` | 35 | Wind Factor Bonus auto-melee dodge chance bonus. |
| `DragonFactorHaki.windProjectileDodgeBonus` | 35 | Wind Factor Bonus auto-projectile dodge chance bonus. |
| `DragonFactorHaki.windDodgeNegateBonus` | 35 | Wind Factor Bonus dodge negate bonus. |
| `DragonFactorHaki.lightMagiculeRegenBonus` | 4 | Light Factor Bonus magicule regeneration bonus. |
| `DragonFactorHaki.darknessSpiritualResistDegradation` | 1 | Darkness Factor Bonus spiritual resistance/nullification degradation value. |
| `DragonFactorHaki.corrosionResistDegradation` | 1 | Corrosion mastery Factor Bonus corrosion resistance/nullification degradation value. |
| `DragonFactorHaki.enderWeight` | 10 | Random roll weight for Ender. |
| `DragonFactorHaki.netherWeight` | 10 | Random roll weight for Nether. |
| `DragonFactorHaki.holyWeight` | 10 | Random roll weight for Holy. |
| `DragonFactorHaki.daemonicWeight` | 10 | Random roll weight for Daemonic. |
| `DragonFactorHaki.guardDamageMultiplier` | 0.5 | Elemental Guard damage multiplier for matching element. |
| `DragonFactorHaki.releasePulseIntervalTicks` | 20 | Dragon Haki Release pulse interval ticks. |
| `DragonFactorHaki.releaseRadius` | 5 | Dragon Haki Release target search radius. |
| `DragonFactorHaki.releaseEpDifferenceStepFraction` | 0.2 | EP difference step fraction for Dragon Haki Release (0.2 = per 20%). |
| `DragonFactorHaki.releaseDamagePerStep` | 25 | Element damage added by Dragon Haki Release per EP step. |
| `DragonFactorHaki.releaseConfusionDurationTicks` | 60 | Confusion duration from Dragon Haki Release. |
| `DragonFactorHaki.releaseConfusionMaxAmplifier` | 3 | Max confusion amplifier from Dragon Haki Release. |
| `DragonFactorHaki.spaceAuraIntervalTicks` | 20 | Space Factor Bonus aura interval ticks. |
| `DragonFactorHaki.spaceAuraRadius` | 6 | Space Factor Bonus aura range. |
| `DragonFactorHaki.spaceAuraTargetEpFraction` | 0.5 | Space Factor Bonus applies blockade when target EP is below this owner fraction. |
| `DragonFactorHaki.spaceAuraDurationTicks` | 60 | Space Factor Bonus spatial blockade duration ticks. |
| `DragonFactorHaki.fireWeight` | 30 | Random roll weight for Fire. |
| `DragonFactorHaki.waterWeight` | 30 | Random roll weight for Water. |
| `DragonFactorHaki.earthWeight` | 30 | Random roll weight for Earth. |
| `DragonFactorHaki.windWeight` | 30 | Random roll weight for Wind. |
| `DragonFactorHaki.spaceWeight` | 15 | Random roll weight for Space. |
| `DragonFactorHaki.lightWeight` | 10 | Random roll weight for Light. |
| `DragonFactorHaki.darknessWeight` | 10 | Random roll weight for Darkness. |

## In-game messages

<details markdown><summary>Show 14 messages</summary>

- Dragon Factor Element: %s
- Fire
- Water
- Earth
- Wind
- Space
- Light
- Darkness
- Corrosion
- Ender
- Nether
- Holy
- Daemonic
- Vampiric

</details>
