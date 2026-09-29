# Kyurem

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Kyurem](../../../assets/icons/mysticism/skill/kyurem.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:kyurem` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 64,600 |
| **Cooldowns (s)** | 5 mastered, 10 otherwise, 30, 10 mastered, 20 otherwise, 10 |
| **Activation** | Press, Hold |

</div>

> A husk of what you formally were. The leftovers, discarded without a second thought when the split happened. Coldness seeps through your skin as you freeze everything to reclaim your other parts.

## Modes

| # | Mode |
|---|---|
| 1 | Glaciate |
| 2 | Draconic Pulse |
| 3 | Freeze Dry |
| 4 | Blizzard |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Glaciate | 900 |  |
| Draconic Pulse | 700 |  |
| Freeze Dry | 800 |  |
| Blizzard | 900 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you are attacked

## Obtaining

- Acquisition checks: [Zekrom](zekrom.md), [Kyurem](kyurem.md), [Reshiram](reshiram.md), [Ice Essence](../../items/materials/ice-essence.md), [Dragon Essence](../../../tensura-reincarnated/items/materials/dragon-essence.md)

## Related

- **Related skills:** [Zekrom](zekrom.md), [Reshiram](reshiram.md), [Blizzard](../../../tensura-reincarnated/abilities/spiritual-magic/blizzard.md), [Cold Resistance](../../../tensura-reincarnated/abilities/resistance-skills/cold-resistance.md), [Thermal Fluctuation Resistance](../../../tensura-reincarnated/abilities/resistance-skills/thermal-fluctuation-resistance.md), [Cold Nullification](../../../tensura-reincarnated/abilities/resistance-skills/cold-nullification.md), [Thermal Fluctuation Nullification](../../../tensura-reincarnated/abilities/resistance-skills/thermal-fluctuation-nullification.md)
- **Effects:** [Pressure](../../effects/pressure.md), [Chill](../../../tensura-reincarnated/effects/chill.md)
- **Items:** [Ice Essence](../../items/materials/ice-essence.md), [Dragon Essence](../../../tensura-reincarnated/items/materials/dragon-essence.md)
- **Referenced by:** [Reshiram](reshiram.md), [Zekrom](zekrom.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Kyurem.epRequirement` | 100,000 | EP Needed to Obtain. |
| `Kyurem.canAcquireWithOtherSkills` | true | Should this skill be acquirable if you have [Reshiram] or [Zekrom]? |
| `Kyurem.iceEssenceAmount` | 10 | Amount of Ice Essence needed to be consumed for acquisition. |
| `Kyurem.dragonEssenceAmount` | 10 | Amount of Dragon Essence needed to be consumed for acquisition. |
| `Kyurem.mpAcquirement` | 64,600 | Magicule Acquirement Cost. |
| `Kyurem.pressureEffectDuration` | 30 | Pressure Effect Duration in Seconds |
| `Kyurem.pressureCostMultiplier` | 2 | Pressure Cost Multiplier. |
| `Kyurem.glaciateMPCost` | 900 | Magicule cost for the Glaciate Mode. |
| `Kyurem.glaciateRange` | 15 | Range of Glaciate Mode in blocks |
| `Kyurem.glaciateDamageIncrement` | 10 | The amount of incremented damage for Glaciate mode per 10 seconds |
| `Kyurem.glaciateMaxDamageMastered` | 200 | The Max Damage Glaciate can deal when Mastered. |
| `Kyurem.glaciateMaxDamage` | 100 | The Max Damage Glaciate can deal. |
| `Kyurem.glaciateCooldown` | 30 | Cooldown of Glaciate Mode. |
| `Kyurem.draconicPulseMPCost` | 700 | Magicule cost for the Draconic Pulse Mode. |
| `Kyurem.draconicPulseDamage` | 40 | Draconic Pulse Damage. |
| `Kyurem.draconicPulseExplosionRadius` | 7.5 | Draconic Pulse Explosion Radius. |
| `Kyurem.draconicPulseCooldown` | 10 | Draconic Pulse Cooldown. |
| `Kyurem.draconicPulseCooldownMastered` | 5 | Draconic Pulse Cooldown Mastered. |
| `Kyurem.freezeDryMPCost` | 800 | Magicule cost for the Freeze Dry Mode. |
| `Kyurem.freezeDryDamage` | 20 | Damage of Freeze Dry Mode. |
| `Kyurem.freezeDryCooldown` | 20 | Cooldown of Freeze Dry Mode. |
| `Kyurem.freezeDryCooldownMastered` | 10 | Cooldown of Freeze Dry Mode when Mastered. |
| `Kyurem.blizzardMPCost` | 900 | Magicule cost for the Blizzard Mode. |
| `Kyurem.blizzardDamage` | 40 | Blizzard Damage. |
| `Kyurem.blizzardCooldown` | 10 | Cooldown of Blizzard. |
| `Kyurem.blizzardRadius` | 7.5 | Radius of Blizzard |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/unique_skills`
