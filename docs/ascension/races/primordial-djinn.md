# Primordial Djinn

<small>[Ascension](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `ascension:primordial_djinn` |
| **Difficulty** | Hard |
| **Alignment** | Holy |
| **Aura** | 300 - 300 |
| **Magicule** | 700 - 700 |
| **Health bonus** | -8 |
| **Spiritual health bonus** | -16 |
| **Attack damage bonus** | -0.5 |
| **Movement speed bonus** | -0.02 |

</div>

> An original djinn from before civilization. Their presence alone breaks lesser wills.

## Evolution

- **Evolves from:** [Wishbound Djinn](wishbound-djinn.md)
- **Evolves into:** [Ascended Djinn](ascended-djinn.md)
- **Default evolution:** [Ascended Djinn](ascended-djinn.md)
- **On awakening (True Demon Lord / True Hero):** [Ascended Djinn](ascended-djinn.md)
- **During the Harvest Festival:** [Ascended Djinn](ascended-djinn.md)

### Requirements to evolve into Primordial Djinn

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 700,000 | 50% |
| Consume 8 of [Daemon Essence](../../tensura-reincarnated/items/materials/daemon-essence.md) | 50% |

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

- ![](../../assets/icons/tensura/skill/titanification.png) [Titanification](../../tensura-reincarnated/abilities/intrinsic-skills/titanification.md)
- ![](../../assets/icons/tensura/skill/light_transform.png) [Light Transform](../../tensura-reincarnated/abilities/intrinsic-skills/light-transform.md)
- ![](../../assets/icons/tensura/skill/divine_ki_release.png) [Divine Ki Release](../../tensura-reincarnated/abilities/intrinsic-skills/divine-ki-release.md)
- ![](../../assets/icons/tensura/skill/body_armor.png) [Body Armor](../../tensura-reincarnated/abilities/intrinsic-skills/body-armor.md)
- ![](../../assets/icons/tensura/skill/charm.png) [Charm](../../tensura-reincarnated/abilities/intrinsic-skills/charm.md)

## Learnable skills

This race can learn these skills through training.

- ![](../../assets/icons/tensura/skill/hero_haki.png) [Hero Haki](../../tensura-reincarnated/abilities/extra-skills/hero-haki.md)
- ![](../../assets/icons/tensura/skill/mortal_fear.png) [Mortal Fear](../../tensura-reincarnated/abilities/extra-skills/mortal-fear.md)
- ![](../../assets/icons/tensura/skill/holy_attack_nullification.png) [Holy Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/holy-attack-nullification.md)
- ![](../../assets/icons/tensura/skill/ultraspeed_regeneration.png) [Ultraspeed Regeneration](../../tensura-reincarnated/abilities/extra-skills/ultraspeed-regeneration.md)
- ![](../../assets/icons/tensura/skill/multilayer_barrier.png) [Multilayer Barrier](../../tensura-reincarnated/abilities/extra-skills/multilayer-barrier.md)
- ![](../../assets/icons/tensura/skill/magic_nullification.png) [Magic Nullification](../../tensura-reincarnated/abilities/resistance-skills/magic-nullification.md)
- ![](../../assets/icons/tensura/skill/thought_acceleration.png) [Thought Acceleration](../../tensura-reincarnated/abilities/extra-skills/thought-acceleration.md)
- ![](../../assets/icons/tensura/skill/sacred_haki.png) [Sacred Haki](../../tensura-reincarnated/abilities/extra-skills/sacred-haki.md)
- ![](../../assets/icons/tensura/skill/holy_attack_resistance.png) [Holy Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/holy-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/flame_attack_resistance.png) [Flame Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/flame-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/snake_eye.png) [Snake Eye](../../tensura-reincarnated/abilities/extra-skills/snake-eye.md)
- ![](../../assets/icons/tensura/skill/spatial_motion.png) [Spatial Motion](../../tensura-reincarnated/abilities/extra-skills/spatial-motion.md)
- ![](../../assets/icons/tensura/skill/spatial_attack_resistance.png) [Spatial Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/spatial-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/mana_manipulation.png) [Mana Manipulation](../../tensura-reincarnated/abilities/extra-skills/mana-manipulation.md)
- ![](../../assets/icons/tensura/skill/magic_sense.png) [Magic Sense](../../tensura-reincarnated/abilities/extra-skills/magic-sense.md)
- ![](../../assets/icons/tensura/skill/danger_sense.png) [Danger Sense](../../tensura-reincarnated/abilities/extra-skills/danger-sense.md)
- ![](../../assets/icons/tensura/skill/farsight.png) [Farsight](../../tensura-reincarnated/abilities/common-skills/farsight.md)
- ![](../../assets/icons/tensura/skill/magic_resistance.png) [Magic Resistance](../../tensura-reincarnated/abilities/resistance-skills/magic-resistance.md)

## Traits

- Divine

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

## Tags

`tensura:races/divine`
