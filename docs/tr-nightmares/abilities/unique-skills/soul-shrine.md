# Soul Shrine

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Soul Shrine](../../../assets/icons/trnightmare/skill/soul_shrine.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:soul_shrine` |
| **Modes** | 2 |
| **Activation** | Press |

</div>

> Having devoured the energy of a powerful majin, you now take on some of its characteristics... Your punches hurt the soul...

## Modes

| # | Mode |
|---|---|
| 1 | Divergent Fist |
| 2 | Simple Domain |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you are attacked
- Triggers when you take damage
- Triggers when an effect is applied to you

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| instas | 0.2 | multiply total |

## Related

- **Related skills:** [Curse](../../../tensura-reincarnated/abilities/spiritual-magic/curse.md)
- **Effects:** [Zone](../../effects/zone.md), [Simple Domain](../../effects/simple.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `SoulShrine.mpAcquirement` | 75,000 | Magicule Acquirement Cost. |
| `SoulShrine.magiculeCostFist` | 100 | Magicule Cost to Divergent Fist or Cursed Energy reinforcement. |
| `SoulShrine.magiculeCostSimple` | 2,000 | Magicule Cost to activate Simple Domain. |
| `SoulShrine.divergentDamage` | 1.5 | Damage multiplier dealt by divergent unmastered. |
| `SoulShrine.reinforcementDamage` | 2 | Damage dealt by reinforcement mastered. |
| `SoulShrine.divergentCooldown` | 2 | Cooldown for activating Divergent Fist minus one. |
| `SoulShrine.reinforcementCooldown` | 0 | Cooldown for activating Reinforcement minus one. |
| `SoulShrine.simpleDuration` | 30 | How long simple domain lasts in seconds. |
| `SoulShrine.simpleDurationMastered` | 60 | How long simple domain lasts in seconds with mastery. |
| `SoulShrine.simpleCooldown` | 120 | Cooldown for Simple Domain. |
| `SoulShrine.flashChance` | 1 | Chance out of 100 for a physical attack to trigger a black flash without mastery. |
| `SoulShrine.flashChanceMastered` | 5 | Chance out of 100 for a physical attack to trigger a black flash with mastery. |
| `SoulShrine.flashZoneChance` | 20 | How much having Zone effect increases chances out of 100. |
| `SoulShrine.effectImmunities` | "tensura:black_burn", "tensura:spatial_blockade", "tensura:soul_drain" | List of effects User is immune to. |
| `SoulShrine.simpleResistance` | 50 | Percentage of magical and spiritual damage resisted when in simple domain. |
| `SoulShrine.flashMultiplier` | 2.5 | Damage multiplier on an attack with black flash. |
