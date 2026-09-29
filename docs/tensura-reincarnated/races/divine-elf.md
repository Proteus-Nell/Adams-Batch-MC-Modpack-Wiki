# Divine Elf

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:divine_elf` |
| **Difficulty** | Easy |
| **Alignment** | Holy |
| **Aura** | 1,000,000 - 1,000,000 |
| **Magicule** | 1,000,000 - 1,000,000 |
| **Health bonus** | 980 |
| **Spiritual health bonus** | 6,000 |
| **Attack damage bonus** | 3 |
| **Movement speed bonus** | 0.12 |
| **EP to evolve into** | 2,000,000 |

</div>

> Elf that achieved divinity, possessing an immortal physical body that will never age.

## Evolution

- **Evolves from:** [Elf Saint](elf-saint.md)

### Requirements to evolve into Divine Elf

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 2,000,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Divine Elf"]
  r1["Elf"]
  r2["Elf Saint"]
  r3["Enlightened Elf"]
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
| Max Health | 980 | add |
| Max Spiritual Health | 6,000 | add |
| Attack Damage | 3 | add |
| Attack Speed | 1 | add |
| Knockback Resistance | 0.2 | add |
| Movement Speed | 0.12 | add |
| Swim Speed Multiplier | 1.2 | add |

## Stats (config defaults)

Set in [`config/tensura/race/elf_config.toml`](../configs/config-tensura-race-elf-config.md).

| Option | Default | Description |
|---|---|---|
| `DivineElf.epRequirement` | 2,000,000 | EP requirement to evolve into Divine Elf. |
| `DivineElf.minAura` | 1,000,000 | Minimal aura. |
| `DivineElf.maxAura` | 1,000,000 | Maximum aura. |
| `DivineElf.minMagicule` | 1,000,000 | Minimal magicule. |
| `DivineElf.maxMagicule` | 1,000,000 | Maximum magicule. |
| `DivineElf.size` | 0 | Bonus Size. |
| `DivineElf.maxHealth` | 980 | Bonus Max Health. |
| `DivineElf.maxSpiritualHealth` | 6,000 | Bonus Max Spiritual Health. |
| `DivineElf.attack` | 3 | Bonus Attack Damage. |
| `DivineElf.attackSpeed` | 1 | Bonus Attack Speed. |
| `DivineElf.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `DivineElf.movementSpeed` | 0.12 | Bonus Movement Speed. |
| `DivineElf.swimSpeed` | 1.2 | Bonus Swimming Speed Multiplier. |
| `ElfSaint.epRequirement` | 400,000 | EP requirement to evolve into Elf Saint. |
| `ElfSaint.bossRequirement` | 4 | The number of Bosses defeated to evolve into Elf Saint. |
| `ElfSaint.minAura` | 400,000 | Minimal aura. |
| `ElfSaint.maxAura` | 400,000 | Maximum aura. |
| `ElfSaint.minMagicule` | 400,000 | Minimal magicule. |
| `ElfSaint.maxMagicule` | 400,000 | Maximum magicule. |
| `ElfSaint.size` | 0 | Bonus Size. |
| `ElfSaint.maxHealth` | 480 | Bonus Max Health. |
| `ElfSaint.maxSpiritualHealth` | 3,000 | Bonus Max Spiritual Health. |
| `ElfSaint.attack` | 2 | Bonus Attack Damage. |
| `ElfSaint.attackSpeed` | 0.6 | Bonus Attack Speed. |
| `ElfSaint.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `ElfSaint.movementSpeed` | 0.07 | Bonus Movement Speed. |
| `ElfSaint.swimSpeed` | 0.7 | Bonus Swimming Speed Multiplier. |
| `EnlightenedElf.epRequirement` | 100,000 | EP requirement to evolve into Enlightened Elf. |
| `EnlightenedElf.minAura` | 140,000 | Minimal aura. |
| `EnlightenedElf.maxAura` | 140,000 | Maximum aura. |
| `EnlightenedElf.minMagicule` | 60,000 | Minimal magicule. |
| `EnlightenedElf.maxMagicule` | 60,000 | Maximum magicule. |
| `EnlightenedElf.size` | 0 | Bonus Size. |
| `EnlightenedElf.maxHealth` | 80 | Bonus Max Health. |
| `EnlightenedElf.maxSpiritualHealth` | 300 | Bonus Max Spiritual Health. |
| `EnlightenedElf.attack` | 1 | Bonus Attack Damage. |
| `EnlightenedElf.attackSpeed` | 0.3 | Bonus Attack Speed. |
| `EnlightenedElf.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `EnlightenedElf.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `EnlightenedElf.swimSpeed` | 0.3 | Bonus Swimming Speed Multiplier. |
| `Elf.minAura` | 320 | Minimal aura. |
| `Elf.maxAura` | 600 | Maximum aura. |
| `Elf.minMagicule` | 600 | Minimal magicule. |
| `Elf.maxMagicule` | 800 | Maximum magicule. |
| `Elf.size` | 0 | Bonus Size. |
| `Elf.maxHealth` | 0 | Bonus Max Health. |
| `Elf.maxSpiritualHealth` | 0 | Bonus Max Spiritual Health. |
| `Elf.attack` | 0 | Bonus Attack Damage. |
| `Elf.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `Elf.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Elf.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `Elf.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |

## Tags

`tensura:races/divine`
