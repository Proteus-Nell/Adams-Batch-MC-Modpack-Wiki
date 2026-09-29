# Wicked Oni

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:wicked_oni` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 40,000 - 100,000 |
| **Magicule** | 40,000 - 100,000 |
| **Health bonus** | 110 |
| **Spiritual health bonus** | 460 |
| **Attack damage bonus** | 3.5 |
| **Movement speed bonus** | 0.03 |

</div>

> A variant of Oni, possessing an essence that leans closer towards that of a Daemon rather than that of a pure Elemental.

## Evolution

- **Evolves from:** [Enlightened Ogre](enlightened-ogre.md), [Kijin](kijin.md)
- **Evolves into:** [Death Oni](death-oni.md)
- **Default evolution:** [Death Oni](death-oni.md)
- **On awakening (True Demon Lord / True Hero):** [Spirit Oni](spirit-oni.md)

### Requirements to evolve into Wicked Oni

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Consume 10 of [Daemon Essence](../items/materials/daemon-essence.md) | 100% |

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

- ![](../../assets/icons/tensura/skill/strength.png) [Strength](../abilities/common-skills/strength.md)
- ![](../../assets/icons/tensura/skill/ultraspeed_regeneration.png) [Ultraspeed Regeneration](../abilities/extra-skills/ultraspeed-regeneration.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 110 | add |
| Max Spiritual Health | 460 | add |
| Attack Damage | 3.5 | add |
| Attack Speed | 0.4 | add |
| Knockback Resistance | 0.2 | add |
| Movement Speed | 0.03 | add |
| Swim Speed Multiplier | 0.3 | add |

## Stats (config defaults)

Set in [`config/tensura/race/ogre_config.toml`](../configs/config-tensura-race-ogre-config.md).

| Option | Default | Description |
|---|---|---|
| `WickedOni.essenceRequirement` | 10 | The number of Demon Essences consumed to evolve into Wicked Oni. |
| `WickedOni.minAura` | 40,000 | Minimal aura. |
| `WickedOni.maxAura` | 100,000 | Maximum aura. |
| `WickedOni.minMagicule` | 40,000 | Minimal magicule. |
| `WickedOni.maxMagicule` | 100,000 | Maximum magicule. |
| `WickedOni.size` | 0 | Bonus Size. |
| `WickedOni.maxHealth` | 110 | Bonus Max Health. |
| `WickedOni.maxSpiritualHealth` | 460 | Bonus Max Spiritual Health. |
| `WickedOni.attack` | 3.5 | Bonus Attack Damage. |
| `WickedOni.attackSpeed` | 0.4 | Bonus Attack Speed. |
| `WickedOni.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `WickedOni.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `WickedOni.swimSpeed` | 0.3 | Bonus Swimming Speed Multiplier. |
| `Kijin.spiritRequirement` | 1 | The number of Spirits obtained to evolve into Kijin. |
| `Kijin.minAura` | 5,000 | Minimal aura. |
| `Kijin.maxAura` | 5,000 | Maximum aura. |
| `Kijin.minMagicule` | 5,000 | Minimal magicule. |
| `Kijin.maxMagicule` | 5,000 | Maximum magicule. |
| `Kijin.size` | 0 | Bonus Size. |
| `Kijin.maxHealth` | 10 | Bonus Max Health. |
| `Kijin.maxSpiritualHealth` | 100 | Bonus Max Spiritual Health. |
| `Kijin.attack` | 3 | Bonus Attack Damage. |
| `Kijin.attackSpeed` | 0.2 | Bonus Attack Speed. |
| `Kijin.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `Kijin.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `Kijin.swimSpeed` | 0.2 | Bonus Swimming Speed Multiplier. |
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
