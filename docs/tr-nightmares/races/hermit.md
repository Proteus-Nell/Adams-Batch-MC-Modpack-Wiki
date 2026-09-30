# Hermit

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:hermit` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Easy |
| **Alignment** | Holy |
| **Aura** | 20,000 - 100,000 |
| **Magicule** | 20,000 - 50,000 |
| **Health bonus** | 80 |
| **Spiritual health bonus** | 740 |
| **Attack damage bonus** | 2 |
| **Movement speed bonus** | 0.05 |
| **EP to evolve into** | 50,000 |

</div>

## Evolution

- **Evolves from:** [Scholar](scholar.md)
- **Evolves into:** [Sorcerer](sorcerer.md)
- **Default evolution:** [Sorcerer](sorcerer.md)
- **On awakening (True Demon Lord / True Hero):** [Disciple](disciple.md)
- **During the Harvest Festival:** [Apostle](apostle.md)

### Requirements to evolve into Hermit

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 50,000 | 100% |

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
| Max Health | 80 | add |
| Max Spiritual Health | 740 | add |
| Attack Damage | 2 | add |
| Attack Speed | -1 | add |
| Knockback Resistance | 0.2 | add |
| Movement Speed | 0.05 | add |
| Swim Speed Multiplier | 0.05 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/scholar_config.toml`](../configs/config-nightmare-race-scholar-config.md).

| Option | Default | Description |
|---|---|---|
| `Hermit.epRequirement` | 50,000 | EP requirement to evolve into Hermit. |
| `Hermit.minAura` | 20,000 | Minimal aura. |
| `Hermit.maxAura` | 100,000 | Maximum aura. |
| `Hermit.minMagicule` | 20,000 | Minimal magicule. |
| `Hermit.maxMagicule` | 50,000 | Maximum magicule. |
| `Hermit.size` | 0 | Bonus Size. |
| `Hermit.maxHealth` | 80 | Bonus Max Health. |
| `Hermit.maxSpiritualHealth` | 740 | Bonus Max Spiritual Health. |
| `Hermit.attack` | 2 | Bonus Attack Damage. |
| `Hermit.attackSpeed` | -1 | Bonus Attack Speed. |
| `Hermit.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `Hermit.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `Hermit.swimSpeed` | 0.05 | Bonus Swimming Speed Multiplier. |
| `Hermit.intrinsicSkills` | "tensura:shadow_motion" | List of skills obtained by this race. |
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
