# Carnation

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Carnation](../../../assets/icons/trnightmare/skill/carnation.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:carnation` |
| **Modes** | 5 |
| **Activation** | Press, Hold |

</div>

> After taking in the power of those around you to the point of gluttonous overconsumption. You absorb energy just as you did before, with your limits on uniques refreshed. Your growth fuels everyone.

## Modes

| # | Mode |
|---|---|
| 1 | Snack For Later! |
| 2 | Family Bonds! |
| 3 | Predation |
| 4 | Stomach |
| 5 | Recovery |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.5 | multiply total |
| law | 1 | add |
| Magicule Regeneration Multiplier | `(instance.isMastered(entity) ? 2.0F : 1.0F) \* this.cfg().snackmultiplier - 1.0` | multiply total |

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Acquisition checks: [Sentient Being](sentient-being.md), [Gluttony](../../../tensura-reincarnated/abilities/unique-skills/gluttony.md)

## Related

- **Related skills:** [Sentient Being](sentient-being.md), [Gluttony](../../../tensura-reincarnated/abilities/unique-skills/gluttony.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Carnation.corrosionSpeedMultiplier` | 0.5 | Activation Speed Multiplier when activating the Corrosion Mode. |
| `Carnation.mpAcquirement` | 295,000 | Magicule Acquirement Cost. |
| `Carnation.essenceRequirementDragon` | 10 | Dragon Essence requirement. |
| `Carnation.abundanceMultiplier` | 2 | Multiplier for Magicule Regeneration via Abundance. |
| `Carnation.snackmultiplier` | 5 | Multiplier for Magicule Regeneration via Snack For Later (doubled on mastery). |
| `Carnation.recoveryCooldown` | 10 | Cooldown for activating Recovery. |
| `Carnation.bondsCooldown` | 120 | Cooldown for activating Family Bonds!. |
| `Carnation.recoveryCost` | 90 | Magicule cost of Recovery per HP healed while unmastered. |
| `Carnation.recoveryCostMastered` | 45 | Magicule cost of Recovery per HP healed while mastered. |
| `Carnation.recoveryCostSHP` | 70 | Magicule cost of Recovery per SHP healed. |
| `Carnation.predationRange` | 10 | The max range in block of the Predation Mode. |
| `Carnation.predationRangeMastered` | 15 | The max range in block of the Predation Mode when mastered. |
| `Carnation.predationDamage` | 100 | The attack damage of the Predation Mode. |
| `Carnation.corrosionSpeedMultiplier` | 0.5 | Activation Speed Multiplier when activating the Corrosion Mode. |
| `Carnation.predationEPDrain` | 1,000 | The amount of EP that the user drains from target using the Predation Mode. |
| `Carnation.predationSkillChance` | 30 | The chance to obtain skills from targets without killing them with the Predation Mode. |
| `Carnation.predationSkillNumber` | 3 | The number of skills to gain from targets at a time without killing them with the Predation Mode. |
| `Carnation.predationCorrosionDuration` | 100 | The duration in tick of the Corrosion effect applied by the Predation Mode. |
| `Carnation.predationCorrosionLevel` | 2 | The level of the Corrosion effect applied by the Predation Mode. |
| `Carnation.predationEPSteal` | 0.5 | The multiplier of the target's EP to be turned into the user's EP when killed with the Predation Mode. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
