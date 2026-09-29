# Whisper Djinn

<small>[Ascension](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `ascension:whisper_djinn` |
| **Stage** | <span class="stage stage-starting">Starting</span> |
| **Difficulty** | Easy |
| **Alignment** | Default |
| **Aura** | 300 - 300 |
| **Magicule** | 700 - 700 |
| **Health bonus** | -8 |
| **Spiritual health bonus** | -16 |
| **Attack damage bonus** | -0.5 |
| **Movement speed bonus** | -0.02 |

</div>

> A newborn djinn of small stature and great magical potential.

## Evolution

- **Evolves into:** [Trickster Djinn](trickster-djinn.md)
- **Default evolution:** [Trickster Djinn](trickster-djinn.md)
- **On awakening (True Demon Lord / True Hero):** [Trickster Djinn](trickster-djinn.md)
- **During the Harvest Festival:** [Trickster Djinn](trickster-djinn.md)

### Evolution tree

```mermaid
flowchart LR
  r0["Ascended Djinn"]
  r1["Infinite Djinn"]
  r2["Omniversal Djinn"]
  r3["Phantom Djinn"]
  r4["Primordial Djinn"]
  r5["Royal Djinn"]
  r6["Sovereign Djinn"]
  r7["Trickster Djinn"]
  r8["Whisper Djinn"]
  r9["Wishbound Djinn"]
  r0 --> r6
  r1 --> r2
  r3 --> r5
  r4 --> r0
  r5 --> r9
  r6 --> r1
  r7 --> r3
  r8 --> r7
  r9 --> r4
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/charm.png) [Charm](../../tensura-reincarnated/abilities/intrinsic-skills/charm.md)

## Learnable skills

This race can learn these skills through training.

- ![](../../assets/icons/tensura/skill/magic_sense.png) [Magic Sense](../../tensura-reincarnated/abilities/extra-skills/magic-sense.md)
- ![](../../assets/icons/tensura/skill/danger_sense.png) [Danger Sense](../../tensura-reincarnated/abilities/extra-skills/danger-sense.md)
- ![](../../assets/icons/tensura/skill/farsight.png) [Farsight](../../tensura-reincarnated/abilities/common-skills/farsight.md)
- ![](../../assets/icons/tensura/skill/magic_resistance.png) [Magic Resistance](../../tensura-reincarnated/abilities/resistance-skills/magic-resistance.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | size | add |
| Max Health | max HP | add |
| Max Spiritual Health | max spiritual HP | add |
| Attack Damage | attack | add |
| Attack Speed | attack speed | add |
| Knockback Resistance | knockback resistance | add |
| Movement Speed | movement speed | add |
| Swim Speed Multiplier | swim speed | add |

## Stats (config defaults)

Set in [`config/tensura/race/goblin_config.toml`](../../tensura-reincarnated/configs/config-tensura-race-goblin-config.md).

| Option | Default | Description |
|---|---|---|
| `Goblin.minAura` | 300 | Minimal aura. |
| `Goblin.maxAura` | 300 | Maximum aura. |
| `Goblin.minMagicule` | 700 | Minimal magicule. |
| `Goblin.maxMagicule` | 700 | Maximum magicule. |
| `Goblin.size` | -0.25 | Bonus Size. |
| `Goblin.maxHealth` | -8 | Bonus Max Health. |
| `Goblin.maxSpiritualHealth` | -16 | Bonus Max Spiritual Health. |
| `Goblin.attack` | -0.5 | Bonus Attack Damage. |
| `Goblin.attackSpeed` | -0.5 | Bonus Attack Speed. |
| `Goblin.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Goblin.movementSpeed` | -0.02 | Bonus Movement Speed. |
| `Goblin.swimSpeed` | -0.2 | Bonus Swimming Speed Multiplier. |
