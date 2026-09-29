# Elder Bloodfiend

<small>[Ascension](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `ascension:elder_bloodfiend` |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 300 - 300 |
| **Magicule** | 700 - 700 |
| **Health bonus** | -8 |
| **Spiritual health bonus** | -16 |
| **Attack damage bonus** | -0.5 |
| **Movement speed bonus** | -0.02 |

</div>

> An ancient predator who moves between shadows like a wraith.

## Evolution

- **Evolves from:** [Blood Noble](blood-noble.md)
- **Evolves into:** [Progenitor Bloodfiend](progenitor-bloodfiend.md)
- **Default evolution:** [Progenitor Bloodfiend](progenitor-bloodfiend.md)
- **On awakening (True Demon Lord / True Hero):** [Progenitor Bloodfiend](progenitor-bloodfiend.md)
- **During the Harvest Festival:** [Progenitor Bloodfiend](progenitor-bloodfiend.md)

### Requirements to evolve into Elder Bloodfiend

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of elder_bloodfiend (evolution ep) | 50% |
| Consume 5 of [Daemon Essence](../../tensura-reincarnated/items/materials/daemon-essence.md) | 50% |

### Evolution tree

```mermaid
flowchart LR
  r0["Blood Noble"]
  r1["Elder Bloodfiend"]
  r2["Fledgling Bloodfiend"]
  r3["Kindred Bloodfiend"]
  r4["Progenitor Bloodfiend"]
  r0 --> r1
  r1 --> r4
  r2 --> r3
  r3 --> r0
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/charm.png) [Charm](../../tensura-reincarnated/abilities/intrinsic-skills/charm.md)
- ![](../../assets/icons/tensura/skill/body_armor.png) [Body Armor](../../tensura-reincarnated/abilities/intrinsic-skills/body-armor.md)
- ![](../../assets/icons/tensura/skill/blood_mist.png) [Blood Mist](../../tensura-reincarnated/abilities/intrinsic-skills/blood-mist.md)
- ![](../../assets/icons/tensura/skill/drain.png) [Drain](../../tensura-reincarnated/abilities/intrinsic-skills/drain.md)

## Learnable skills

This race can learn these skills through training.

- ![](../../assets/icons/tensura/skill/spatial_motion.png) [Spatial Motion](../../tensura-reincarnated/abilities/extra-skills/spatial-motion.md)
- ![](../../assets/icons/tensura/skill/majesty.png) [Majesty](../../tensura-reincarnated/abilities/extra-skills/majesty.md)
- ![](../../assets/icons/tensura/skill/physical_attack_resistance.png) [Physical Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/physical-attack-resistance.md)
- ![](../../assets/icons/tensura/skill/snake_eye.png) [Snake Eye](../../tensura-reincarnated/abilities/extra-skills/snake-eye.md)
- ![](../../assets/icons/tensura/skill/ultraspeed_regeneration.png) [Ultraspeed Regeneration](../../tensura-reincarnated/abilities/extra-skills/ultraspeed-regeneration.md)
- ![](../../assets/icons/tensura/skill/darkness_attack_nullification.png) [Darkness Attack Nullification](../../tensura-reincarnated/abilities/resistance-skills/darkness-attack-nullification.md)
- ![](../../assets/icons/ascension/skill/prickly_hands.png) [Prickly Hands](../abilities/common-skills/prickly-hands.md)
- ![](../../assets/icons/ascension/skill/blood_resistance.png) [Blood Resistance](../abilities/resistance-skills/blood-resistance.md)
- ![](../../assets/icons/ascension/skill/blood_manipulation.png) [Blood Manipulation](../abilities/extra-skills/blood-manipulation.md)
- ![](../../assets/icons/tensura/skill/mana_manipulation.png) [Mana Manipulation](../../tensura-reincarnated/abilities/extra-skills/mana-manipulation.md)
- ![](../../assets/icons/tensura/skill/mortal_fear.png) [Mortal Fear](../../tensura-reincarnated/abilities/extra-skills/mortal-fear.md)
- ![](../../assets/icons/tensura/skill/poison_resistance.png) [Poison Resistance](../../tensura-reincarnated/abilities/resistance-skills/poison-resistance.md)
- ![](../../assets/icons/tensura/skill/magic_sense.png) [Magic Sense](../../tensura-reincarnated/abilities/extra-skills/magic-sense.md)
- ![](../../assets/icons/tensura/skill/danger_sense.png) [Danger Sense](../../tensura-reincarnated/abilities/extra-skills/danger-sense.md)
- ![](../../assets/icons/ascension/skill/blood_frenzy.png) [Blood Frenzy](../abilities/extra-skills/blood-frenzy.md)
- ![](../../assets/icons/tensura/skill/darkness_attack_resistance.png) [Darkness Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/darkness-attack-resistance.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0.35 | add |
| Scale | 0.3 | add |
| Scale | 0.25 | add |
| Scale | 0.2 | add |
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
