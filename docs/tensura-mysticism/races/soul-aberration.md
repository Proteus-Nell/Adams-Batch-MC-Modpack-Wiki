# Soul Aberration

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:soul_aberration` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Extreme |
| **Alignment** | Majin |
| **Aura** | 400,000 - 400,000 |
| **Magicule** | 400,000 - 400,000 |
| **Health bonus** | 930 |
| **Spiritual health bonus** | 4,730 |
| **Attack damage bonus** | 11 |
| **Movement speed bonus** | 0.03 |
| **EP to evolve into** | 400,000 |

</div>

> Very rarely, a Warden can evolve to an even bigger monstrosity. What this one will do with its power is still unknown. It is a demi-spiritual lifeform.

## Evolution

- **Evolves from:** [Warden](warden.md), [Sculk Worm](sculk-worm.md), [Soul Shrieker](soul-shrieker.md)
- **Evolves into:** [Reaper Aberration](reaper-aberration.md)
- **Default evolution:** [Warden](warden.md)
- **On awakening (True Demon Lord / True Hero):** [Reaper Aberration](reaper-aberration.md)

### Requirements to evolve into Soul Aberration

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 400,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Charged Perforator"]
  r1["Dissonance Deity"]
  r2["Enflamed Aberration"]
  r3["Lightning Aberration"]
  r4["Magma Worm"]
  r5["Molten Perforator"]
  r6["Overloading Worm"]
  r7["Reaper Aberration"]
  r8["Sculk Worm"]
  r9["Soul Aberration"]
  r10["Soul Shrieker"]
  r11["Violence Deity"]
  r12["Warden"]
  r0 --> r3
  r0 --> r6
  r2 --> r11
  r3 --> r1
  r4 --> r2
  r5 --> r2
  r5 --> r4
  r6 --> r3
  r8 --> r0
  r8 --> r5
  r8 --> r9
  r8 --> r10
  r9 --> r7
  r9 --> r12
  r10 --> r9
  r10 --> r12
  r12 --> r9
```

## Traits

- Spiritual lifeform

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 1 | add |
| Max Health | 930 | add |
| Max Spiritual Health | 4,730 | add |
| Attack Damage | 11 | add |
| Attack Speed | 2.75 | add |
| Knockback Resistance | 0.75 | add |
| Movement Speed | 0.03 | add |
| Swim Speed Multiplier | 0.4 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/sculk_config.toml`](../configs/config-mysticism-race-sculk-config.md).

| Option | Default | Description |
|---|---|---|
| `SoulAberration.epRequirement` | 400,000 | EP requirement to evolve into a Soul Aberration. |
| `SoulAberration.minAura` | 400,000 | Minimal aura. |
| `SoulAberration.maxAura` | 400,000 | Maximum aura. |
| `SoulAberration.minMagicule` | 400,000 | Minimal magicule. |
| `SoulAberration.maxMagicule` | 400,000 | Maximum magicule. |
| `SoulAberration.size` | 1 | Bonus Size. |
| `SoulAberration.maxHealth` | 930 | Bonus Max Health. |
| `SoulAberration.maxSpiritualHealth` | 4,730 | Bonus Max Spiritual Health. |
| `SoulAberration.attack` | 11 | Bonus Attack Damage. |
| `SoulAberration.attackSpeed` | 2.75 | Bonus Attack Speed. |
| `SoulAberration.knockbackResistance` | 0.75 | Bonus Knockback Resistance. |
| `SoulAberration.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `SoulAberration.swimSpeed` | 0.4 | Bonus Swimming Speed Multiplier. |
| `SoulAberration.intrinsicSkills` | "tensura:sense_soundwave", "tensura:pain_resistance", "tensura:ultrasonic_waves", "tensura:magic_resistance" | The list of intrinsic skills that the race gets. |
| `Warden.epRequirement` | 50,000 | EP requirement to evolve into a Warden. |
| `Warden.minAura` | 35,000 | Minimal aura. |
| `Warden.maxAura` | 35,000 | Maximum aura. |
| `Warden.minMagicule` | 65,000 | Minimal magicule. |
| `Warden.maxMagicule` | 65,000 | Maximum magicule. |
| `Warden.size` | 0.5 | Bonus Size. |
| `Warden.maxHealth` | 480 | Bonus Max Health. |
| `Warden.maxSpiritualHealth` | 980 | Bonus Max Spiritual Health. |
| `Warden.attack` | 7 | Bonus Attack Damage. |
| `Warden.attackSpeed` | 2.5 | Bonus Attack Speed. |
| `Warden.knockbackResistance` | 0.5 | Bonus Knockback Resistance. |
| `Warden.movementSpeed` | 0.025 | Bonus Movement Speed. |
| `Warden.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
| `Warden.intrinsicSkills` | "tensura:sense_soundwave", "tensura:pain_resistance", "tensura:ultrasonic_waves" | The list of intrinsic skills that the race gets. |
| `SoulShrieker.epRequirement` | 4,000 | EP requirement to evolve into a Soul Shrieker. |
| `SoulShrieker.minAura` | 1,500 | Minimal aura. |
| `SoulShrieker.maxAura` | 1,500 | Maximum aura. |
| `SoulShrieker.minMagicule` | 2,500 | Minimal magicule. |
| `SoulShrieker.maxMagicule` | 2,500 | Maximum magicule. |
| `SoulShrieker.size` | -0.25 | Bonus Size. |
| `SoulShrieker.maxHealth` | 4 | Bonus Max Health. |
| `SoulShrieker.maxSpiritualHealth` | 28 | Bonus Max Spiritual Health. |
| `SoulShrieker.attack` | 1 | Bonus Attack Damage. |
| `SoulShrieker.attackSpeed` | 3.5 | Bonus Attack Speed. |
| `SoulShrieker.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `SoulShrieker.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `SoulShrieker.swimSpeed` | 0.2 | Bonus Swimming Speed Multiplier. |
| `SoulShrieker.intrinsicSkills` | "tensura:sense_soundwave", "tensura:pain_resistance", "tensura:ultrasonic_waves" | The list of intrinsic skills that the race gets. |
| `SculkWorm.minAura` | 100 | Minimal aura. |
| `SculkWorm.maxAura` | 250 | Maximum aura. |
| `SculkWorm.minMagicule` | 800 | Minimal magicule. |
| `SculkWorm.maxMagicule` | 1,200 | Maximum magicule. |
| `SculkWorm.size` | -0.5 | Bonus Size. |
| `SculkWorm.maxHealth` | -12 | Bonus Max Health. |
| `SculkWorm.maxSpiritualHealth` | -4 | Bonus Max Spiritual Health. |
| `SculkWorm.attack` | -0.5 | Bonus Attack Damage. |
| `SculkWorm.attackSpeed` | 3.5 | Bonus Attack Speed. |
| `SculkWorm.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `SculkWorm.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `SculkWorm.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `SculkWorm.intrinsicSkills` | "tensura:sense_soundwave" | The list of intrinsic skills that the race gets. |

## Tags

`tensura:races/spiritual`
