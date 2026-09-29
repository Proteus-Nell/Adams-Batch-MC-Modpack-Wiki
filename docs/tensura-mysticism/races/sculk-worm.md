# Sculk Worm

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:sculk_worm` |
| **Stage** | <span class="stage stage-starting">Starting</span> |
| **Difficulty** | Extreme |
| **Alignment** | Majin |
| **Aura** | 100 - 250 |
| **Magicule** | 800 - 1,200 |
| **Health bonus** | -12 |
| **Spiritual health bonus** | -4 |
| **Attack damage bonus** | -0.5 |
| **Movement speed bonus** | 0.01 |

</div>

> An ancient family of sculk inhabitants, where evolution has given them permanent darkness. Starts off weak, but grows to become a monstrosity.

## Evolution

- **Evolves into:** [Soul Shrieker](soul-shrieker.md), [Molten Perforator](molten-perforator.md), [Charged Perforator](charged-perforator.md)
- **Default evolution:** [Soul Shrieker](soul-shrieker.md)
- **On awakening (True Demon Lord / True Hero):** [Soul Aberration](soul-aberration.md)
- **During the Harvest Festival:** [Soul Shrieker](soul-shrieker.md)

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

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | -0.5 | add |
| Max Health | -12 | add |
| Max Spiritual Health | -4 | add |
| Attack Damage | -0.5 | add |
| Attack Speed | 3.5 | add |
| Knockback Resistance | 0 | add |
| Movement Speed | 0.01 | add |
| Swim Speed Multiplier | 0 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/sculk_config.toml`](../configs/config-mysticism-race-sculk-config.md).

| Option | Default | Description |
|---|---|---|
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
