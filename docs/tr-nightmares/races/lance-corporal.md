# Lance hCorporal

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:lance_corporal` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Easy |
| **Alignment** | Holy |
| **Aura** | 375,000 - 750,000 |
| **Magicule** | 225,000 - 450,000 |
| **Health bonus** | 757 |
| **Spiritual health bonus** | 3,240 |
| **Attack damage bonus** | 4 |
| **Movement speed bonus** | 0.03 |
| **EP to evolve into** | 750,000 |

</div>

## Evolution

- **Evolves from:** [Divine hSoldier](divine-soldier.md)
- **Evolves into:** [Archangqel](archangel.md)
- **Default evolution:** [Archangqel](archangel.md)
- **On awakening (True Demon Lord / True Hero):** [Archangqel](archangel.md)
- **During the Harvest Festival:** [Archangqel](archangel.md)

### Requirements to evolve into Lance hCorporal

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 750,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["sAccursed gGoddess"]
  r1["Archangqel"]
  r2["Brother Of Chaos"]
  r3["Daughter pOf Light"]
  r4["Divine hSoldier"]
  r5["Higher hGoddess"]
  r6["Lance hCorporal"]
  r7["Lesser hGoddess"]
  r8["Medium hGoddess"]
  r9["Nameless Goddess"]
  r10["Goddess Princess"]
  r11["Wingless Goddess"]
  r3 --> r0
  r4 --> r6
  r5 --> r4
  r5 --> r10
  r5 --> r11
  r6 --> r1
  r7 --> r8
  r8 --> r5
  r9 --> r2
  r10 --> r3
  r11 --> r9
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/abnormal_condition_resistance.png) [Abnormal Condition Resistance](../../tensura-reincarnated/abilities/resistance-skills/abnormal-condition-resistance.md)
- ![](../../assets/icons/tensura/skill/ultraspeed_regeneration.png) [Ultraspeed Regeneration](../../tensura-reincarnated/abilities/extra-skills/ultraspeed-regeneration.md)
- ![](../../assets/icons/tensura/skill/universal_perception.png) [Universal Perception](../../tensura-reincarnated/abilities/extra-skills/universal-perception.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 1 | add |
| Max Health | 757 | add |
| Max Spiritual Health | 3,240 | add |
| Attack Damage | 4 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 1.1 | add |
| Movement Speed | 0.03 | add |
| Swim Speed Multiplier | 0.03 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/goddess_clan_config.toml`](../configs/config-nightmare-race-goddess-clan-config.md).

| Option | Default | Description |
|---|---|---|
| `LanceCorporal.epRequirement` | 750,000 | Existence points required to evolve into Lance Corporal. |
| `LanceCorporal.minAura` | 375,000 | Minimal aura. |
| `LanceCorporal.maxAura` | 750,000 | Maximum aura. |
| `LanceCorporal.minMagicule` | 225,000 | Minimal magicule. |
| `LanceCorporal.maxMagicule` | 450,000 | Maximum magicule. |
| `LanceCorporal.size` | 1 | Bonus Size. |
| `LanceCorporal.maxHealth` | 757 | Bonus Max Health. |
| `LanceCorporal.maxSpiritualHealth` | 3,240 | Bonus Max Spiritual Health. |
| `LanceCorporal.attack` | 4 | Bonus Attack Damage. |
| `LanceCorporal.attackSpeed` | 0 | Bonus Attack Speed. |
| `LanceCorporal.knockbackResistance` | 1.1 | Bonus Knockback Resistance. |
| `LanceCorporal.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `LanceCorporal.swimSpeed` | 0.03 | Bonus Swimming Speed Multiplier. |
| `DivineSoldier.epRequirement` | 350,000 | Existence points required to evolve into Divine Soldier. |
| `DivineSoldier.essenceRequirementHoly` | 15 | Holy essence required to evolve into Divine Soldier. |
| `DivineSoldier.minAura` | 175,000 | Minimal aura. |
| `DivineSoldier.maxAura` | 350,000 | Maximum aura. |
| `DivineSoldier.minMagicule` | 105,000 | Minimal magicule. |
| `DivineSoldier.maxMagicule` | 210,000 | Maximum magicule. |
| `DivineSoldier.size` | 0.5 | Bonus Size. |
| `DivineSoldier.maxHealth` | 330 | Bonus Max Health. |
| `DivineSoldier.maxSpiritualHealth` | 1,140 | Bonus Max Spiritual Health. |
| `DivineSoldier.attack` | 3 | Bonus Attack Damage. |
| `DivineSoldier.attackSpeed` | 0 | Bonus Attack Speed. |
| `DivineSoldier.knockbackResistance` | 0.9 | Bonus Knockback Resistance. |
| `DivineSoldier.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `DivineSoldier.swimSpeed` | 0.02 | Bonus Swimming Speed Multiplier. |
| `HigherClassGoddess.epRequirement` | 150,000 | Existence points required to evolve into Higher Class Goddess. |
| `HigherClassGoddess.essenceRequirementHoly` | 10 | Holy essence required to evolve into Higher Class Goddess. |
| `HigherClassGoddess.minAura` | 75,000 | Minimal aura. |
| `HigherClassGoddess.maxAura` | 150,000 | Maximum aura. |
| `HigherClassGoddess.minMagicule` | 45,000 | Minimal magicule. |
| `HigherClassGoddess.maxMagicule` | 90,000 | Maximum magicule. |
| `HigherClassGoddess.size` | 0 | Bonus Size. |
| `HigherClassGoddess.maxHealth` | 230 | Bonus Max Health. |
| `HigherClassGoddess.maxSpiritualHealth` | 690 | Bonus Max Spiritual Health. |
| `HigherClassGoddess.attack` | 2.4 | Bonus Attack Damage. |
| `HigherClassGoddess.attackSpeed` | 0.3 | Bonus Attack Speed. |
| `HigherClassGoddess.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `HigherClassGoddess.movementSpeed` | 0.06 | Bonus Movement Speed. |
| `HigherClassGoddess.swimSpeed` | 0.06 | Bonus Swimming Speed Multiplier. |
| `MediumClassGoddess.essenceRequirementHoly` | 10 | Holy essence required to evolve into Medium Class Goddess. |
| `MediumClassGoddess.epRequirement` | 80,000 | Existence points required to evolve into Medium Class Goddess. |
| `MediumClassGoddess.essenceRequirementHoly` | 10 | Holy essence required to evolve into Medium Class Goddess. |
| `MediumClassGoddess.minAura` | 40,000 | Minimal aura. |
| `MediumClassGoddess.maxAura` | 80,000 | Maximum aura. |
| `MediumClassGoddess.minMagicule` | 24,000 | Minimal magicule. |
| `MediumClassGoddess.maxMagicule` | 48,000 | Maximum magicule. |
| `MediumClassGoddess.size` | 0 | Bonus Size. |
| `MediumClassGoddess.maxHealth` | 100 | Bonus Max Health. |
| `MediumClassGoddess.maxSpiritualHealth` | 200 | Bonus Max Spiritual Health. |
| `MediumClassGoddess.attack` | 1.4 | Bonus Attack Damage. |
| `MediumClassGoddess.attackSpeed` | 0 | Bonus Attack Speed. |
| `MediumClassGoddess.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `MediumClassGoddess.movementSpeed` | 0.04 | Bonus Movement Speed. |
| `MediumClassGoddess.swimSpeed` | 0.04 | Bonus Swimming Speed Multiplier. |
| `LowerClassGoddess.minAura` | 2,000 | Minimal aura. |
| `LowerClassGoddess.maxAura` | 4,000 | Maximum aura. |
| `LowerClassGoddess.minMagicule` | 500 | Minimal magicule. |
| `LowerClassGoddess.maxMagicule` | 1,000 | Maximum magicule. |
| `LowerClassGoddess.size` | 0 | Bonus Size. |
| `LowerClassGoddess.maxHealth` | 25 | Bonus Max Health. |
| `LowerClassGoddess.maxSpiritualHealth` | 90 | Bonus Max Spiritual Health. |
| `LowerClassGoddess.attack` | 0.7 | Bonus Attack Damage. |
| `LowerClassGoddess.attackSpeed` | -0.2 | Bonus Attack Speed. |
| `LowerClassGoddess.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `LowerClassGoddess.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `LowerClassGoddess.swimSpeed` | 0.02 | Bonus Swimming Speed Multiplier. |
