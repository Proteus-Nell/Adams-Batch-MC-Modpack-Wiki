# Contractor

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:contractor` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Intermediate |
| **Alignment** | Majin |
| **Aura** | 20,000 - 100,000 |
| **Magicule** | 20,000 - 200,000 |
| **Health bonus** | 180 |
| **Spiritual health bonus** | 1,540 |
| **Attack damage bonus** | 3 |
| **Movement speed bonus** | 0.06 |
| **EP to evolve into** | 100,000 |

</div>

## Evolution

- **Evolves from:** [Wanderer](wanderer.md), [Scholar](scholar.md)
- **Evolves into:** [Trickster](trickster.md)
- **Default evolution:** [Trickster](trickster.md)
- **On awakening (True Demon Lord / True Hero):** [Enforcer](enforcer.md)
- **During the Harvest Festival:** [Trickster](trickster.md)

### Requirements to evolve into Contractor

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 100,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Apostle"]
  r1["Contractor"]
  r2["Disciple"]
  r3["Enforcer"]
  r4["Hermit"]
  r5["Jedidiah"]
  r6["Myrddin"]
  r7["Scholar"]
  r8["Sorcerer"]
  r9["Trickster"]
  r10["Wanderer"]
  r0 --> r2
  r1 --> r3
  r1 --> r9
  r2 --> r5
  r3 --> r6
  r4 --> r0
  r4 --> r2
  r4 --> r8
  r5 --> r2
  r6 --> r3
  r7 --> r1
  r7 --> r3
  r7 --> r4
  r7 --> r10
  r8 --> r0
  r8 --> r2
  r9 --> r3
  r10 --> r1
  r10 --> r3
  r10 --> r9
```

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 180 | add |
| Max Spiritual Health | 1,540 | add |
| Attack Damage | 3 | add |
| Attack Speed | -1.5 | add |
| Knockback Resistance | 0.3 | add |
| Movement Speed | 0.06 | add |
| Swim Speed Multiplier | 0.06 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/scholar_config.toml`](../configs/config-nightmare-race-scholar-config.md).

| Option | Default | Description |
|---|---|---|
| `Contractor.epRequirement` | 100,000 | EP requirement to evolve into Contractor. |
| `Contractor.minAura` | 20,000 | Minimal aura. |
| `Contractor.maxAura` | 100,000 | Maximum aura. |
| `Contractor.minMagicule` | 20,000 | Minimal magicule. |
| `Contractor.maxMagicule` | 200,000 | Maximum magicule. |
| `Contractor.size` | 0 | Bonus Size. |
| `Contractor.maxHealth` | 180 | Bonus Max Health. |
| `Contractor.maxSpiritualHealth` | 1,540 | Bonus Max Spiritual Health. |
| `Contractor.attack` | 3 | Bonus Attack Damage. |
| `Contractor.attackSpeed` | -1.5 | Bonus Attack Speed. |
| `Contractor.knockbackResistance` | 0.3 | Bonus Knockback Resistance. |
| `Contractor.movementSpeed` | 0.06 | Bonus Movement Speed. |
| `Contractor.swimSpeed` | 0.06 | Bonus Swimming Speed Multiplier. |
| `Contractor.intrinsicSkills` | "trnightmare:avalon" | List of skills obtained by this race. |
| `Wanderer.epRequirement` | 50,000 | EP requirement to evolve into Wanderer. |
| `Wanderer.minAura` | 20,000 | Minimal aura. |
| `Wanderer.maxAura` | 50,000 | Maximum aura. |
| `Wanderer.minMagicule` | 20,000 | Minimal magicule. |
| `Wanderer.maxMagicule` | 100,000 | Maximum magicule. |
| `Wanderer.size` | 0 | Bonus Size. |
| `Wanderer.maxHealth` | 80 | Bonus Max Health. |
| `Wanderer.maxSpiritualHealth` | 740 | Bonus Max Spiritual Health. |
| `Wanderer.attack` | 2 | Bonus Attack Damage. |
| `Wanderer.attackSpeed` | -1 | Bonus Attack Speed. |
| `Wanderer.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `Wanderer.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `Wanderer.swimSpeed` | 0.05 | Bonus Swimming Speed Multiplier. |
| `Wanderer.intrinsicSkills` | "tensura:magic_aura" | List of skills obtained by this race. |
| `Scholar.minAura` | 500 | Minimal aura. |
| `Scholar.maxAura` | 2,000 | Maximum aura. |
| `Scholar.minMagicule` | 5,500 | Minimal magicule. |
| `Scholar.maxMagicule` | 8,000 | Maximum magicule. |
| `Scholar.size` | 0 | Bonus Size. |
| `Scholar.maxHealth` | 20 | Bonus Max Health. |
| `Scholar.maxSpiritualHealth` | 340 | Bonus Max Spiritual Health. |
| `Scholar.attack` | 0 | Bonus Attack Damage. |
| `Scholar.attackSpeed` | -0.5 | Bonus Attack Speed. |
| `Scholar.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `Scholar.movementSpeed` | 0 | Bonus Movement Speed. |
| `Scholar.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `Scholar.intrinsicSkills` | "tensura:chant_annulment", "tensura:sage" | List of skills obtained by this race. |
