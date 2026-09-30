# Lesser Mystic Fox

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:lesser_mystic_fox` |
| **Stage** | <span class="stage stage-starting">Starting</span> |
| **Difficulty** | Intermediate |
| **Alignment** | Default |
| **Aura** | 4,000 - 9,000 |
| **Magicule** | 8,000 - 16,000 |
| **Health bonus** | 25 |
| **Spiritual health bonus** | 100 |
| **Attack damage bonus** | 0.7 |
| **Movement speed bonus** | 0.03 |
| **EP to evolve into** | 0 |

</div>

> A young fox spirit with budding mystic instincts.

## Evolution

- **Evolves into:** [Greater Mystic Fox](greater-mystic-fox.md)
- **Default evolution:** [Greater Mystic Fox](greater-mystic-fox.md)
- **On awakening (True Demon Lord / True Hero):** [Greater Mystic Fox](greater-mystic-fox.md)
- **During the Harvest Festival:** [Greater Mystic Fox](greater-mystic-fox.md)

### Evolution tree

```mermaid
flowchart LR
  r0["Divine Fox"]
  r1["Greater Mystic Fox"]
  r2["Lesser Mystic Fox"]
  r3["Ninehead"]
  r4["Ninetail"]
  r5["Soul Beast"]
  r1 --> r3
  r2 --> r1
  r3 --> r4
  r4 --> r5
  r5 --> r0
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/abnormal_condition_nullification.png) [Abnormal Condition Nullification](../../tensura-reincarnated/abilities/resistance-skills/abnormal-condition-nullification.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | -0.5 | add |
| Max Health | 25 | add |
| Max Spiritual Health | 100 | add |
| Attack Damage | 0.7 | add |
| Attack Speed | 0.15 | add |
| Knockback Resistance | 0.1 | add |
| Movement Speed | 0.03 | add |
| Swim Speed Multiplier | 0.02 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/mystic_fox_config.toml`](../configs/config-nightmare-race-mystic-fox-config.md).

| Option | Default | Description |
|---|---|---|
| `LesserMysticFox.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `LesserMysticFox.minAura` | 4,000 |  |
| `LesserMysticFox.maxAura` | 9,000 |  |
| `LesserMysticFox.minMagicule` | 8,000 |  |
| `LesserMysticFox.maxMagicule` | 16,000 |  |
| `LesserMysticFox.size` | -0.5 |  |
| `LesserMysticFox.maxHealth` | 25 |  |
| `LesserMysticFox.maxSpiritualHealth` | 100 |  |
| `LesserMysticFox.attack` | 0.7 |  |
| `LesserMysticFox.attackSpeed` | 0.15 |  |
| `LesserMysticFox.knockbackResistance` | 0.1 |  |
| `LesserMysticFox.movementSpeed` | 0.03 |  |
| `LesserMysticFox.swimSpeed` | 0.02 |  |
