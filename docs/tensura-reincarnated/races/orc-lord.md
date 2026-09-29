# Orc Lord

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:orc_lord` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 3,000 - 5,000 |
| **Magicule** | 7,000 - 10,000 |
| **Health bonus** | 80 |
| **Spiritual health bonus** | 360 |
| **Attack damage bonus** | 1.5 |
| **Movement speed bonus** | 0 |
| **EP to evolve into** | 5,000 |

</div>

> A very rare and powerful member of the Orc race with high intelligence who appears roughly every few centuries.

## Evolution

- **Evolves from:** [High Orc](high-orc.md)
- **Evolves into:** [Orc Disaster](orc-disaster.md)
- **Default evolution:** [Orc Disaster](orc-disaster.md)
- **On awakening (True Demon Lord / True Hero):** [Spirit Boar](spirit-boar.md)
- **During the Harvest Festival:** [Orc Disaster](orc-disaster.md)

### Requirements to evolve into Orc Lord

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Consume 10 of [Royal Blood](../items/miscellaneous/royal-blood.md) | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Divine Boar"]
  r1["High Orc"]
  r2["Orc"]
  r3["Orc Disaster"]
  r4["Orc Lord"]
  r5["Spirit Boar"]
  r1 --> r4
  r1 --> r5
  r2 --> r1
  r2 --> r5
  r3 --> r5
  r4 --> r3
  r4 --> r5
  r5 --> r0
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/starved.png) [Starved](../abilities/unique-skills/starved.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0.5 | add |
| Max Health | 80 | add |
| Max Spiritual Health | 360 | add |
| Attack Damage | 1.5 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0.4 | add |
| Movement Speed | 0 | add |
| Swim Speed Multiplier | 0 | add |

## Stats (config defaults)

Set in [`config/tensura/race/orc_config.toml`](../configs/config-tensura-race-orc-config.md).

| Option | Default | Description |
|---|---|---|
| `OrcLord.bloodRequirement` | 10 | The number of Royal Blood consumed to evolve into Orc Lord. |
| `OrcLord.minAura` | 3,000 | Minimal aura. |
| `OrcLord.maxAura` | 5,000 | Maximum aura. |
| `OrcLord.minMagicule` | 7,000 | Minimal magicule. |
| `OrcLord.maxMagicule` | 10,000 | Maximum magicule. |
| `OrcLord.size` | 0.5 | Bonus Size. |
| `OrcLord.maxHealth` | 80 | Bonus Max Health. |
| `OrcLord.maxSpiritualHealth` | 360 | Bonus Max Spiritual Health. |
| `OrcLord.attack` | 1.5 | Bonus Attack Damage. |
| `OrcLord.attackSpeed` | 0 | Bonus Attack Speed. |
| `OrcLord.knockbackResistance` | 0.4 | Bonus Knockback Resistance. |
| `OrcLord.movementSpeed` | 0 | Bonus Movement Speed. |
| `OrcLord.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `HighOrc.epRequirement` | 5,000 | EP requirement to evolve into High Orc. |
| `HighOrc.minAura` | 2,000 | Minimal aura. |
| `HighOrc.maxAura` | 2,000 | Maximum aura. |
| `HighOrc.minMagicule` | 1,000 | Minimal magicule. |
| `HighOrc.maxMagicule` | 1,000 | Maximum magicule. |
| `HighOrc.size` | 0.5 | Bonus Size. |
| `HighOrc.maxHealth` | 12 | Bonus Max Health. |
| `HighOrc.maxSpiritualHealth` | 100 | Bonus Max Spiritual Health. |
| `HighOrc.attack` | 1.5 | Bonus Attack Damage. |
| `HighOrc.attackSpeed` | -0.25 | Bonus Attack Speed. |
| `HighOrc.knockbackResistance` | 0.3 | Bonus Knockback Resistance. |
| `HighOrc.movementSpeed` | 0 | Bonus Movement Speed. |
| `HighOrc.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `Orc.minAura` | 400 | Minimal aura. |
| `Orc.maxAura` | 600 | Maximum aura. |
| `Orc.minMagicule` | 50 | Minimal magicule. |
| `Orc.maxMagicule` | 100 | Maximum magicule. |
| `Orc.size` | 0.5 | Bonus Size. |
| `Orc.maxHealth` | 8 | Bonus Max Health. |
| `Orc.maxSpiritualHealth` | 16 | Bonus Max Spiritual Health. |
| `Orc.attack` | 0.5 | Bonus Attack Damage. |
| `Orc.attackSpeed` | -0.5 | Bonus Attack Speed. |
| `Orc.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `Orc.movementSpeed` | -0.02 | Bonus Movement Speed. |
| `Orc.swimSpeed` | -0.2 | Bonus Swimming Speed Multiplier. |
