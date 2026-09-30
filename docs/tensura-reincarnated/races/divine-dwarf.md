# Divine Dwarf

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:divine_dwarf` |
| **Stage** | <span class="stage stage-final">Final</span> |
| **Difficulty** | Easy |
| **Alignment** | Holy |
| **Aura** | 1,000,000 - 1,000,000 |
| **Magicule** | 1,000,000 - 1,000,000 |
| **Health bonus** | 1,040 |
| **Spiritual health bonus** | 6,140 |
| **Attack damage bonus** | 3.5 |
| **Movement speed bonus** | 0.08 |
| **EP to evolve into** | 2,000,000 |

</div>

> Dwarf that achieved divinity, possessing an immortal physical body that will never age.

## Evolution

- **Evolves from:** [Dwarf Saint](dwarf-saint.md)

### Requirements to evolve into Divine Dwarf

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 2,000,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Divine Dwarf"]
  r1["Dwarf"]
  r2["Dwarf Saint"]
  r3["Enlightened Dwarf"]
  r1 --> r2
  r1 --> r3
  r2 --> r0
  r3 --> r2
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/divine_ki_release.png) [Divine Ki Release](../abilities/intrinsic-skills/divine-ki-release.md)

## Traits

- Divine

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 1,040 | add |
| Max Spiritual Health | 6,140 | add |
| Attack Damage | 3.5 | add |
| Attack Speed | 0.5 | add |
| Knockback Resistance | 0.4 | add |
| Movement Speed | 0.08 | add |
| Swim Speed Multiplier | 0.8 | add |

## Stats (config defaults)

Set in [`config/tensura/race/dwarf_config.toml`](../configs/config-tensura-race-dwarf-config.md).

| Option | Default | Description |
|---|---|---|
| `DivineDwarf.epRequirement` | 2,000,000 | EP requirement to evolve into Divine Dwarf. |
| `DivineDwarf.minAura` | 1,000,000 | Minimal aura. |
| `DivineDwarf.maxAura` | 1,000,000 | Maximum aura. |
| `DivineDwarf.minMagicule` | 1,000,000 | Minimal magicule. |
| `DivineDwarf.maxMagicule` | 1,000,000 | Maximum magicule. |
| `DivineDwarf.size` | 0 | Bonus Size. |
| `DivineDwarf.maxHealth` | 1,040 | Bonus Max Health. |
| `DivineDwarf.maxSpiritualHealth` | 6,140 | Bonus Max Spiritual Health. |
| `DivineDwarf.attack` | 3.5 | Bonus Attack Damage. |
| `DivineDwarf.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `DivineDwarf.knockbackResistance` | 0.4 | Bonus Knockback Resistance. |
| `DivineDwarf.movementSpeed` | 0.08 | Bonus Movement Speed. |
| `DivineDwarf.swimSpeed` | 0.8 | Bonus Swimming Speed Multiplier. |
| `DwarfSaint.epRequirement` | 400,000 | EP requirement to evolve into Dwarf Saint. |
| `DwarfSaint.bossRequirement` | 4 | The number of Bosses defeated to evolve into Dwarf Saint. |
| `DwarfSaint.minAura` | 400,000 | Minimal aura. |
| `DwarfSaint.maxAura` | 400,000 | Maximum aura. |
| `DwarfSaint.minMagicule` | 400,000 | Minimal magicule. |
| `DwarfSaint.maxMagicule` | 400,000 | Maximum magicule. |
| `DwarfSaint.size` | -0.125 | Bonus Size. |
| `DwarfSaint.maxHealth` | 520 | Bonus Max Health. |
| `DwarfSaint.maxSpiritualHealth` | 3,140 | Bonus Max Spiritual Health. |
| `DwarfSaint.attack` | 2.5 | Bonus Attack Damage. |
| `DwarfSaint.attackSpeed` | 0.4 | Bonus Attack Speed. |
| `DwarfSaint.knockbackResistance` | 0.3 | Bonus Knockback Resistance. |
| `DwarfSaint.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `DwarfSaint.swimSpeed` | 0.3 | Bonus Swimming Speed Multiplier. |
| `EnlightenedDwarf.epRequirement` | 100,000 | EP requirement to evolve into Enlightened Dwarf. |
| `EnlightenedDwarf.minAura` | 140,000 | Minimal aura. |
| `EnlightenedDwarf.maxAura` | 140,000 | Maximum aura. |
| `EnlightenedDwarf.minMagicule` | 60,000 | Minimal magicule. |
| `EnlightenedDwarf.maxMagicule` | 60,000 | Maximum magicule. |
| `EnlightenedDwarf.size` | -0.25 | Bonus Size. |
| `EnlightenedDwarf.maxHealth` | 90 | Bonus Max Health. |
| `EnlightenedDwarf.maxSpiritualHealth` | 320 | Bonus Max Spiritual Health. |
| `EnlightenedDwarf.attack` | 1.5 | Bonus Attack Damage. |
| `EnlightenedDwarf.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `EnlightenedDwarf.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `EnlightenedDwarf.movementSpeed` | 0 | Bonus Movement Speed. |
| `EnlightenedDwarf.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `Dwarf.minAura` | 720 | Minimal aura. |
| `Dwarf.maxAura` | 1,080 | Maximum aura. |
| `Dwarf.minMagicule` | 80 | Minimal magicule. |
| `Dwarf.maxMagicule` | 120 | Maximum magicule. |
| `Dwarf.size` | -0.375 | Bonus Size. |
| `Dwarf.maxHealth` | 4 | Bonus Max Health. |
| `Dwarf.maxSpiritualHealth` | 10 | Bonus Max Spiritual Health. |
| `Dwarf.attack` | 0.5 | Bonus Attack Damage. |
| `Dwarf.attackSpeed` | -0.1 | Bonus Attack Speed. |
| `Dwarf.knockbackResistance` | 0.02 | Bonus Knockback Resistance. |
| `Dwarf.movementSpeed` | -0.01 | Bonus Movement Speed. |
| `Dwarf.swimSpeed` | -0.1 | Bonus Swimming Speed Multiplier. |

## Tags

`tensura:races/divine`
