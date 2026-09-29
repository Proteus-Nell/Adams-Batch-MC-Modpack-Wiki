# Lesser Fallen

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:lesser_fallen` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 4,500 - 5,500 |
| **Magicule** | 7,500 - 9,500 |
| **Health bonus** | 30 |
| **Spiritual health bonus** | 100 |
| **Attack damage bonus** | 0.5 |
| **Movement speed bonus** | 0.01 |

</div>

> A lesser angel that got corrupted by magicules, then chose to abandon the light for the darkness.

## Evolution

- **Evolves into:** [Greater Fallen](greater-fallen.md)
- **Default evolution:** [Greater Fallen](greater-fallen.md)
- **On awakening (True Demon Lord / True Hero):** [Fallen Lord](fallen-lord.md)
- **During the Harvest Festival:** [Greater Fallen](greater-fallen.md)

### Evolution tree

```mermaid
flowchart LR
  r0["Arch Fallen"]
  r1["Fallen"]
  r2["Fallen Lord"]
  r3["Greater Fallen"]
  r4["Lesser Fallen"]
  r0 --> r2
  r2 --> r1
  r3 --> r0
  r3 --> r2
  r4 --> r2
  r4 --> r3
```

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 30 | add |
| Max Spiritual Health | 100 | add |
| Attack Damage | 0.5 | add |
| Attack Speed | 0.1 | add |
| Knockback Resistance | 0.1 | add |
| Movement Speed | 0.01 | add |
| Swim Speed Multiplier | 0 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/angel_config.toml`](../configs/config-mysticism-race-angel-config.md).

| Option | Default | Description |
|---|---|---|
| `LesserFallen.minAura` | 4,500 | Minimal aura. |
| `LesserFallen.maxAura` | 5,500 | Maximum aura. |
| `LesserFallen.minMagicule` | 7,500 | Minimal magicule. |
| `LesserFallen.maxMagicule` | 9,500 | Maximum magicule. |
| `LesserFallen.size` | 0 | Bonus Size. |
| `LesserFallen.maxHealth` | 30 | Bonus Max Health. |
| `LesserFallen.maxSpiritualHealth` | 100 | Bonus Max Spiritual Health. |
| `LesserFallen.attack` | 0.5 | Bonus Attack Damage. |
| `LesserFallen.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `LesserFallen.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `LesserFallen.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `LesserFallen.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `LesserFallen.intrinsicSkills` | "tensura:magic_resistance", "mysticism:darkness_manipulation" | The list of intrinsic skills that the race gets. |
