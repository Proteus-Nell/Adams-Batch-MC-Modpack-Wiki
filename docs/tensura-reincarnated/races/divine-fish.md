# Divine Fish

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:divine_fish` |
| **Stage** | <span class="stage stage-final">Final</span> |
| **Difficulty** | Easy |
| **Alignment** | Holy |
| **Aura** | 1,000,000 - 1,000,000 |
| **Magicule** | 1,000,000 - 1,000,000 |
| **Health bonus** | 1,040 |
| **Spiritual health bonus** | 6,140 |
| **Attack damage bonus** | 3 |
| **Movement speed bonus** | 0.1 |
| **EP to evolve into** | 2,000,000 |

</div>

> Merfolk that achieved divinity, possessing an immortal physical body that will never age.

## Evolution

- **Evolves from:** [Merfolk Saint](merfolk-saint.md)

### Requirements to evolve into Divine Fish

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 2,000,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Divine Fish"]
  r1["Enlightened Merfolk"]
  r2["Merfolk"]
  r3["Merfolk Saint"]
  r1 --> r3
  r2 --> r1
  r2 --> r3
  r3 --> r0
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/divine_ki_release.png) [Divine Ki Release](../abilities/intrinsic-skills/divine-ki-release.md)
- ![](../../assets/icons/tensura/skill/water_breathing.png) [Water Breathing](../abilities/intrinsic-skills/water-breathing.md)
- ![](../../assets/icons/tensura/skill/hydraulic_propulsion.png) [Hydraulic Propulsion](../abilities/common-skills/hydraulic-propulsion.md)

## Traits

- Can breathe underwater
- Divine
- Needs moisture

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Submerged Mining Speed | 1 | add |
| Submerged Mining Speed | 0.8 | add |
| Submerged Mining Speed | 0.6 | add |
| Submerged Mining Speed | 0.4 | add |
| Scale | 0 | add |
| Max Health | 1,040 | add |
| Max Spiritual Health | 6,140 | add |
| Attack Damage | 3 | add |
| Attack Speed | 0.7 | add |
| Knockback Resistance | 0.2 | add |
| Movement Speed | 0.1 | add |
| Swim Speed Multiplier | 1.5 | add |

## Stats (config defaults)

Set in [`config/tensura/race/merfolk_config.toml`](../configs/config-tensura-race-merfolk-config.md).

| Option | Default | Description |
|---|---|---|
| `DivineFish.submergedMiningSpeed` | 1 | Bonus Submerged Mining Speed. |
| `DivineFish.epRequirement` | 2,000,000 | EP requirement to evolve into Divine Fish. |
| `DivineFish.minAura` | 1,000,000 | Minimal aura. |
| `DivineFish.maxAura` | 1,000,000 | Maximum aura. |
| `DivineFish.minMagicule` | 1,000,000 | Minimal magicule. |
| `DivineFish.maxMagicule` | 1,000,000 | Maximum magicule. |
| `DivineFish.size` | 0 | Bonus Size. |
| `DivineFish.maxHealth` | 1,040 | Bonus Max Health. |
| `DivineFish.maxSpiritualHealth` | 6,140 | Bonus Max Spiritual Health. |
| `DivineFish.attack` | 3 | Bonus Attack Damage. |
| `DivineFish.attackSpeed` | 0.7 | Bonus Attack Speed. |
| `DivineFish.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `DivineFish.movementSpeed` | 0.1 | Bonus Movement Speed. |
| `DivineFish.swimSpeed` | 1.5 | Bonus Swimming Speed Multiplier. |
| `DivineFish.submergedMiningSpeed` | 1 | Bonus Submerged Mining Speed. |
| `MerfolkSaint.submergedMiningSpeed` | 0.8 | Bonus Submerged Mining Speed. |
| `MerfolkSaint.epRequirement` | 400,000 | EP requirement to evolve into Merfolk Saint. |
| `MerfolkSaint.bossRequirement` | 4 | The number of Bosses defeated to evolve into Merfolk Saint. |
| `MerfolkSaint.minAura` | 400,000 | Minimal aura. |
| `MerfolkSaint.maxAura` | 400,000 | Maximum aura. |
| `MerfolkSaint.minMagicule` | 400,000 | Minimal magicule. |
| `MerfolkSaint.maxMagicule` | 400,000 | Maximum magicule. |
| `MerfolkSaint.size` | 0 | Bonus Size. |
| `MerfolkSaint.maxHealth` | 520 | Bonus Max Health. |
| `MerfolkSaint.maxSpiritualHealth` | 3,140 | Bonus Max Spiritual Health. |
| `MerfolkSaint.attack` | 2 | Bonus Attack Damage. |
| `MerfolkSaint.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `MerfolkSaint.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `MerfolkSaint.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `MerfolkSaint.swimSpeed` | 1 | Bonus Swimming Speed Multiplier. |
| `MerfolkSaint.submergedMiningSpeed` | 0.8 | Bonus Submerged Mining Speed. |
| `EnlightenedMerfolk.submergedMiningSpeed` | 0.6 | Bonus Submerged Mining Speed. |
| `EnlightenedMerfolk.epRequirement` | 100,000 | EP requirement to evolve into Enlightened Merfolk. |
| `EnlightenedMerfolk.minAura` | 140,000 | Minimal aura. |
| `EnlightenedMerfolk.maxAura` | 140,000 | Maximum aura. |
| `EnlightenedMerfolk.minMagicule` | 60,000 | Minimal magicule. |
| `EnlightenedMerfolk.maxMagicule` | 60,000 | Maximum magicule. |
| `EnlightenedMerfolk.size` | 0 | Bonus Size. |
| `EnlightenedMerfolk.maxHealth` | 100 | Bonus Max Health. |
| `EnlightenedMerfolk.maxSpiritualHealth` | 320 | Bonus Max Spiritual Health. |
| `EnlightenedMerfolk.attack` | 1 | Bonus Attack Damage. |
| `EnlightenedMerfolk.attackSpeed` | 0.2 | Bonus Attack Speed. |
| `EnlightenedMerfolk.knockbackResistance` | 0.05 | Bonus Knockback Resistance. |
| `EnlightenedMerfolk.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `EnlightenedMerfolk.swimSpeed` | 0.7 | Bonus Swimming Speed Multiplier. |
| `EnlightenedMerfolk.submergedMiningSpeed` | 0.6 | Bonus Submerged Mining Speed. |
| `Merfolk.submergedMiningSpeed` | 0.4 | Bonus Submerged Mining Speed. |
| `Merfolk.minAura` | 400 | Minimal aura. |
| `Merfolk.maxAura` | 600 | Maximum aura. |
| `Merfolk.minMagicule` | 500 | Minimal magicule. |
| `Merfolk.maxMagicule` | 600 | Maximum magicule. |
| `Merfolk.size` | 0 | Bonus Size. |
| `Merfolk.maxHealth` | 4 | Bonus Max Health. |
| `Merfolk.maxSpiritualHealth` | 20 | Bonus Max Spiritual Health. |
| `Merfolk.attack` | 0 | Bonus Attack Damage. |
| `Merfolk.attackSpeed` | 0 | Bonus Attack Speed. |
| `Merfolk.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Merfolk.movementSpeed` | -0.01 | Bonus Movement Speed. |
| `Merfolk.swimSpeed` | 0.5 | Bonus Swimming Speed Multiplier. |
| `Merfolk.submergedMiningSpeed` | 0.4 | Bonus Submerged Mining Speed. |

## Tags

`tensura:races/can_breath_water`, `tensura:races/divine`, `tensura:races/need_moist`
