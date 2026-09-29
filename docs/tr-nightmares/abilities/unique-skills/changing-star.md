# Changing Star

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Changing Star](../../../assets/icons/trnightmare/skill/changing_star.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:changing_star` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 120,000 |
| **Max mastery** | 1,000 |
| **Activation** | Toggle, Press |

</div>

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Mode 2 |
| 3 | Mode 3 |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers on melee contact

## Related

- **Effects:** [Inspiration](../../../tensura-reincarnated/effects/inspiration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `changingStar.mpAcquirement` | 120,000 | Magicule obtainment cost. |
| `changingStar.maxMastery` | 1,000 | Max mastery. |
| `changingStar.radiantRestorationMagiculeCost` | 500 | Magicule cost per tick for Radiant Restoration when active. |
| `changingStar.auraOfInspirationMagiculeCost` | 500 | Magicule cost for Aura of Inspiration pulses. |
| `changingStar.incandescentActivationMagiculeCost` | 10,000 | Activation cost for Incandescent Augment. |
| `changingStar.incandescentDamageBonus` | 10 | Base melee damage bonus from Incandescent Augment. |
| `changingStar.incandescentDamageBonusMastered` | 15 | Mastered melee damage bonus from Incandescent Augment. |
| `changingStar.incandescentAttackSpeedBonus` | 1 | Base attack speed bonus from Incandescent Augment. |
| `changingStar.incandescentAttackSpeedBonusMastered` | 1.5 | Mastered attack speed bonus from Incandescent Augment. |
| `changingStar.incandescentKnockbackBonus` | 0.3 | Base knockback bonus from Incandescent Augment. |
| `changingStar.incandescentKnockbackBonusMastered` | 0.5 | Mastered knockback bonus from Incandescent Augment. |
| `changingStar.auraRadius` | 12 | Radius for Aura of Inspiration. |
| `changingStar.inspirationDurationTicks` | 200 | Duration in ticks for the inspiration aura effect. |
| `changingStar.flameOfLongingConversion` | 0.5 | Flame of Longing half-damage conversion factor. |
