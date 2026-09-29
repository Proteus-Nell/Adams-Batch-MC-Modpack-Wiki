# Fledgling Bloodfiend

<small>[Ascension](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `ascension:fledgling_bloodfiend` |
| **Difficulty** | Easy |
| **Alignment** | Default |
| **Aura** | 300 - 300 |
| **Magicule** | 700 - 700 |
| **Health bonus** | -8 |
| **Spiritual health bonus** | -16 |
| **Attack damage bonus** | -0.5 |
| **Movement speed bonus** | -0.02 |

</div>

> A newly turned bloodfiend, still raw and hungry.

## Evolution

- **Evolves into:** [Kindred Bloodfiend](kindred-bloodfiend.md)
- **Default evolution:** [Kindred Bloodfiend](kindred-bloodfiend.md)
- **On awakening (True Demon Lord / True Hero):** [Kindred Bloodfiend](kindred-bloodfiend.md)
- **During the Harvest Festival:** [Kindred Bloodfiend](kindred-bloodfiend.md)

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

- ![](../../assets/icons/tensura/skill/drain.png) [Drain](../../tensura-reincarnated/abilities/intrinsic-skills/drain.md)

## Learnable skills

This race can learn these skills through training.

- ![](../../assets/icons/tensura/skill/magic_sense.png) [Magic Sense](../../tensura-reincarnated/abilities/extra-skills/magic-sense.md)
- ![](../../assets/icons/tensura/skill/danger_sense.png) [Danger Sense](../../tensura-reincarnated/abilities/extra-skills/danger-sense.md)
- ![](../../assets/icons/ascension/skill/blood_frenzy.png) [Blood Frenzy](../abilities/extra-skills/blood-frenzy.md)
- ![](../../assets/icons/tensura/skill/darkness_attack_resistance.png) [Darkness Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/darkness-attack-resistance.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
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
