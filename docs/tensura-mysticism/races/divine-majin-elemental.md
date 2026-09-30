# Divine Majin Elemental

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:divine_majin_elemental` |
| **Stage** | <span class="stage stage-final">Final</span> |
| **Difficulty** | Hard |
| **Alignment** | Majin |
| **Aura** | 1,000,000 - 1,000,000 |
| **Magicule** | 1,000,000 - 1,000,000 |
| **Health bonus** | 680 |
| **Spiritual health bonus** | 12,630 |
| **Attack damage bonus** | 2 |
| **Movement speed bonus** | 0.1 |
| **EP to evolve into** | 2,000,000 |

</div>

> An aspect of perfection that embodies its element to perfection. This being possesses God-level Spiritual Magic rivaling King-Tier Ultimate Skills that can wipe out continents should they be cast.

> [!NOTE]
> **Pack note:** this pack changes the defaults below.
> - `General.refresh` is **false** (mod default: true)

## Evolution

- **Evolves from:** [Majin Elemental Lord](majin-lord.md)

### Requirements to evolve into Divine Majin Elemental

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 2,000,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Divine Elemental"]
  r1["Divine Majin Elemental"]
  r2["Elemental Lord"]
  r3["Greater Elemental"]
  r4["Lesser Elemental"]
  r5["Majin Elemental Lord"]
  r6["Medium Elemental"]
  r2 --> r0
  r3 --> r2
  r3 --> r5
  r4 --> r2
  r4 --> r6
  r5 --> r1
  r5 --> r2
  r6 --> r2
  r6 --> r3
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/divine_ki_release.png) [Divine Ki Release](../../tensura-reincarnated/abilities/intrinsic-skills/divine-ki-release.md)
- ![](../../assets/icons/tensura/skill/physical_attack_resistance.png) [Physical Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/physical-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/possession.png) [Possession](../../tensura-reincarnated/abilities/intrinsic-skills/possession.md)

## Traits

- Divine

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 680 | add |
| Max Spiritual Health | 12,630 | add |
| Attack Damage | 2 | add |
| Attack Speed | 0.5 | add |
| Knockback Resistance | 0.5 | add |
| Movement Speed | 0.1 | add |
| Swim Speed Multiplier | 0.8 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/elemental_config.toml`](../configs/config-mysticism-race-elemental-config.md).

| Option | Default | Description |
|---|---|---|
| `DivineMajinElemental.epRequirement` | 2,000,000 | EP requirement to evolve into Divine Majin Elemental. |
| `DivineMajinElemental.minAura` | 1,000,000 | Minimal aura. |
| `DivineMajinElemental.maxAura` | 1,000,000 | Maximum aura. |
| `DivineMajinElemental.minMagicule` | 1,000,000 | Minimal magicule. |
| `DivineMajinElemental.maxMagicule` | 1,000,000 | Maximum magicule. |
| `DivineMajinElemental.size` | 0 | Bonus Size. |
| `DivineMajinElemental.maxHealth` | 680 | Bonus Max Health. |
| `DivineMajinElemental.maxSpiritualHealth` | 12,630 | Bonus Max Spiritual Health. |
| `DivineMajinElemental.attack` | 2 | Bonus Attack Damage. |
| `DivineMajinElemental.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `DivineMajinElemental.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `DivineMajinElemental.movementSpeed` | 0.1 | Bonus Movement Speed. |
| `DivineMajinElemental.swimSpeed` | 0.8 | Bonus Swimming Speed Multiplier. |
| `DivineMajinElemental.flightSpeed` | 0 | Bonus Flight Speed. |
| `MajinLord.epRequirement` | 800,000 | EP requirement to evolve into Majin Lord. |
| `MajinLord.minAura` | 400,000 | Minimal aura. |
| `MajinLord.maxAura` | 400,000 | Maximum aura. |
| `MajinLord.minMagicule` | 600,000 | Minimal magicule. |
| `MajinLord.maxMagicule` | 600,000 | Maximum magicule. |
| `MajinLord.size` | 0 | Bonus Size. |
| `MajinLord.maxHealth` | 430 | Bonus Max Health. |
| `MajinLord.maxSpiritualHealth` | 8,625 | Bonus Max Spiritual Health. |
| `MajinLord.attack` | 1 | Bonus Attack Damage. |
| `MajinLord.attackSpeed` | 0.35 | Bonus Attack Speed. |
| `MajinLord.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `MajinLord.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `MajinLord.swimSpeed` | 0.625 | Bonus Swimming Speed Multiplier. |
| `MajinLord.flightSpeed` | 0 | Bonus Flight Speed. |
| `GreaterElemental.epRequirement` | 200,000 | EP requirement to evolve into Greater Elemental. |
| `GreaterElemental.minAura` | 200,000 | Minimal aura. |
| `GreaterElemental.maxAura` | 200,000 | Maximum aura. |
| `GreaterElemental.minMagicule` | 100,000 | Minimal magicule. |
| `GreaterElemental.maxMagicule` | 100,000 | Maximum magicule. |
| `GreaterElemental.size` | 0 | Bonus Size. |
| `GreaterElemental.maxHealth` | 180 | Bonus Max Health. |
| `GreaterElemental.maxSpiritualHealth` | 1,260 | Bonus Max Spiritual Health. |
| `GreaterElemental.attack` | 0 | Bonus Attack Damage. |
| `GreaterElemental.attackSpeed` | 0.2 | Bonus Attack Speed. |
| `GreaterElemental.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `GreaterElemental.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `GreaterElemental.swimSpeed` | 0.45 | Bonus Swimming Speed Multiplier. |
| `GreaterElemental.flightSpeed` | 0 | Bonus Flight Speed. |
| `MediumElemental.epRequirement` | 20,000 | EP requirement to evolve into Medium Elemental. |
| `MediumElemental.minAura` | 11,250 | Minimal aura. |
| `MediumElemental.maxAura` | 11,250 | Maximum aura. |
| `MediumElemental.minMagicule` | 11,250 | Minimal magicule. |
| `MediumElemental.maxMagicule` | 11,250 | Maximum magicule. |
| `MediumElemental.size` | -0.5 | Bonus Size. |
| `MediumElemental.maxHealth` | 5 | Bonus Max Health. |
| `MediumElemental.maxSpiritualHealth` | 425 | Bonus Max Spiritual Health. |
| `MediumElemental.attack` | -0.5 | Bonus Attack Damage. |
| `MediumElemental.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `MediumElemental.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `MediumElemental.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `MediumElemental.swimSpeed` | 0.2 | Bonus Swimming Speed Multiplier. |
| `MediumElemental.flightSpeed` | -0.01 | Bonus Flight Speed. |
| `LesserElemental.minAura` | 300 | Minimal aura. |
| `LesserElemental.maxAura` | 500 | Maximum aura. |
| `LesserElemental.minMagicule` | 500 | Minimal magicule. |
| `LesserElemental.maxMagicule` | 1,000 | Maximum magicule. |
| `LesserElemental.size` | -0.75 | Bonus Size. |
| `LesserElemental.maxHealth` | -12 | Bonus Max Health. |
| `LesserElemental.maxSpiritualHealth` | 120 | Bonus Max Spiritual Health. |
| `LesserElemental.attack` | -0.8 | Bonus Attack Damage. |
| `LesserElemental.attackSpeed` | 0 | Bonus Attack Speed. |
| `LesserElemental.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `LesserElemental.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `LesserElemental.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `LesserElemental.flightSpeed` | -0.025 | Bonus Flight Speed. |

Set in [`config/mysticism/general.toml`](../configs/config-mysticism-general.md).

| Option | Default | This pack | Description |
|---|---|---|---|
| `General.refresh` | true | false | Should the Tensura configurations add Mysticism's skills and races on next launch? |
| `General.flightSpeed` | 0.05 | | The default flying speed of all Mysticism races. |
| `General.seCostMultiplier` | 4 | | SE cost multiplier when acquiring a Unique Skill. Default: 4, which means the skill's magicule cost \* 4 |

## Tags

`tensura:races/divine`
