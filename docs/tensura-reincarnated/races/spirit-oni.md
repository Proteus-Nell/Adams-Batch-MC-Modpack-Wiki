# Spirit Oni

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:spirit_oni` |
| **Difficulty** | Easy |
| **Alignment** | Holy |
| **Aura** | 400,000 - 400,000 |
| **Magicule** | 400,000 - 400,000 |
| **Health bonus** | 500 |
| **Spiritual health bonus** | 3,440 |
| **Attack damage bonus** | 5 |
| **Movement speed bonus** | 0.05 |
| **EP to evolve into** | 400,000 |

</div>

> Oni that has "evolved the correct way" and became a Spiritual Lifeform.

## Evolution

- **Evolves from:** [Mystic Oni](mystic-oni.md), [Ogre](ogre.md), [Kijin](kijin.md), [Enlightened Ogre](enlightened-ogre.md), [Wicked Oni](wicked-oni.md)
- **Evolves into:** [Divine Oni](divine-oni.md)
- **Default evolution:** [Divine Oni](divine-oni.md)
- **On awakening (True Demon Lord / True Hero):** [Divine Oni](divine-oni.md)

### Requirements to evolve into Spirit Oni

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 400,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Death Oni"]
  r1["Divine Fighter"]
  r2["Divine Oni"]
  r3["Enlightened Hobgoblin"]
  r4["Enlightened Ogre"]
  r5["Goblin"]
  r6["Hobgoblin"]
  r7["Hobgoblin Saint"]
  r8["Kijin"]
  r9["Mystic Oni"]
  r10["Ogre"]
  r11["Spirit Oni"]
  r12["Wicked Oni"]
  r0 --> r1
  r0 --> r2
  r3 --> r7
  r4 --> r9
  r4 --> r11
  r4 --> r12
  r5 --> r6
  r5 --> r7
  r6 --> r3
  r6 --> r7
  r6 --> r10
  r7 --> r2
  r8 --> r9
  r8 --> r11
  r8 --> r12
  r9 --> r11
  r10 --> r4
  r10 --> r8
  r10 --> r11
  r11 --> r2
  r12 --> r0
  r12 --> r11
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/steel_strength.png) [Steel Strength](../abilities/extra-skills/steel-strength.md)
- ![](../../assets/icons/tensura/skill/strength.png) [Strength](../abilities/common-skills/strength.md)

## Traits

- Spiritual lifeform

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 500 | add |
| Max Spiritual Health | 3,440 | add |
| Attack Damage | 5 | add |
| Attack Speed | 0.5 | add |
| Knockback Resistance | 0.3 | add |
| Movement Speed | 0.05 | add |
| Swim Speed Multiplier | 0.5 | add |

## Stats (config defaults)

Set in [`config/tensura/race/ogre_config.toml`](../configs/config-tensura-race-ogre-config.md).

| Option | Default | Description |
|---|---|---|
| `SpiritOni.epRequirement` | 400,000 | EP requirement to evolve into Ogre Saint. |
| `SpiritOni.minAura` | 400,000 | Minimal aura. |
| `SpiritOni.maxAura` | 400,000 | Maximum aura. |
| `SpiritOni.minMagicule` | 400,000 | Minimal magicule. |
| `SpiritOni.maxMagicule` | 400,000 | Maximum magicule. |
| `SpiritOni.size` | 0 | Bonus Size. |
| `SpiritOni.maxHealth` | 500 | Bonus Max Health. |
| `SpiritOni.maxSpiritualHealth` | 3,440 | Bonus Max Spiritual Health. |
| `SpiritOni.attack` | 5 | Bonus Attack Damage. |
| `SpiritOni.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `SpiritOni.knockbackResistance` | 0.3 | Bonus Knockback Resistance. |
| `SpiritOni.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `SpiritOni.swimSpeed` | 0.5 | Bonus Swimming Speed Multiplier. |
| `MysticOni.essenceRequirement` | 10 | The number of Elemental Essences consumed to evolve into Mystic Oni. |
| `MysticOni.minAura` | 40,000 | Minimal aura. |
| `MysticOni.maxAura` | 100,000 | Maximum aura. |
| `MysticOni.minMagicule` | 40,000 | Minimal magicule. |
| `MysticOni.maxMagicule` | 100,000 | Maximum magicule. |
| `MysticOni.size` | 0 | Bonus Size. |
| `MysticOni.maxHealth` | 140 | Bonus Max Health. |
| `MysticOni.maxSpiritualHealth` | 400 | Bonus Max Spiritual Health. |
| `MysticOni.attack` | 4 | Bonus Attack Damage. |
| `MysticOni.attackSpeed` | 0.4 | Bonus Attack Speed. |
| `MysticOni.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `MysticOni.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `MysticOni.swimSpeed` | 0.3 | Bonus Swimming Speed Multiplier. |
| `EnlightenedOgre.epRequirement` | 100,000 | EP requirement to evolve into Enlightened Ogre. |
| `EnlightenedOgre.minAura` | 100,000 | Minimal aura. |
| `EnlightenedOgre.maxAura` | 100,000 | Maximum aura. |
| `EnlightenedOgre.minMagicule` | 100,000 | Minimal magicule. |
| `EnlightenedOgre.maxMagicule` | 100,000 | Maximum magicule. |
| `EnlightenedOgre.size` | 0 | Bonus Size. |
| `EnlightenedOgre.maxHealth` | 100 | Bonus Max Health. |
| `EnlightenedOgre.maxSpiritualHealth` | 340 | Bonus Max Spiritual Health. |
| `EnlightenedOgre.attack` | 4 | Bonus Attack Damage. |
| `EnlightenedOgre.attackSpeed` | 0.3 | Bonus Attack Speed. |
| `EnlightenedOgre.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `EnlightenedOgre.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `EnlightenedOgre.swimSpeed` | 0.2 | Bonus Swimming Speed Multiplier. |
| `Ogre.minAura` | 1,500 | Minimal aura. |
| `Ogre.maxAura` | 2,500 | Maximum aura. |
| `Ogre.minMagicule` | 300 | Minimal magicule. |
| `Ogre.maxMagicule` | 600 | Maximum magicule. |
| `Ogre.size` | 0 | Bonus Size. |
| `Ogre.maxHealth` | 6 | Bonus Max Health. |
| `Ogre.maxSpiritualHealth` | 15 | Bonus Max Spiritual Health. |
| `Ogre.attack` | 1 | Bonus Attack Damage. |
| `Ogre.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `Ogre.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `Ogre.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `Ogre.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |

## Tags

`tensura:races/spiritual`
