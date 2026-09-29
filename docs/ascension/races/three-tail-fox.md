# 3 Tailed Fox

<small>[Ascension](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `ascension:three_tail_fox` |
| **Difficulty** | Intermediate |
| **Alignment** | Default |
| **Aura** | 1,500 - 2,500 |
| **Magicule** | 300 - 600 |
| **Health bonus** | 2 |
| **Spiritual health bonus** | 10 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0.05 |

</div>

> A Kitsune whose power has bloomed into three tails.

## Evolution

- **Evolves from:** [Kitsune](kitsune.md)
- **Evolves into:** [6 Tailed Fox](six-tail-fox.md)
- **Default evolution:** [6 Tailed Fox](six-tail-fox.md)
- **On awakening (True Demon Lord / True Hero):** [6 Tailed Fox](six-tail-fox.md)
- **During the Harvest Festival:** [6 Tailed Fox](six-tail-fox.md)

### Requirements to evolve into 3 Tailed Fox

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 300,000 | 50% |
| Be named | 50% |

### Evolution tree

```mermaid
flowchart LR
  r0["Divine Kitsune"]
  r1["Kitsune"]
  r2["9 Tailed Fox"]
  r3["6 Tailed Fox"]
  r4["3 Tailed Fox"]
  r1 --> r4
  r2 --> r0
  r3 --> r2
  r4 --> r3
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/charm.png) [Charm](../../tensura-reincarnated/abilities/intrinsic-skills/charm.md)
- ![](../../assets/icons/ascension/skill/sharpened_claws.png) [Sharpened Claws](../abilities/intrinsic-skills/sharpened-claws.md)

## Learnable skills

This race can learn these skills through training.

- ![](../../assets/icons/tensura/skill/mana_manipulation.png) [Mana Manipulation](../../tensura-reincarnated/abilities/extra-skills/mana-manipulation.md)
- ![](../../assets/icons/tensura/skill/snake_eye.png) [Snake Eye](../../tensura-reincarnated/abilities/extra-skills/snake-eye.md)
- ![](../../assets/icons/tensura/skill/magic_resistance.png) [Magic Resistance](../../tensura-reincarnated/abilities/resistance-skills/magic-resistance.md)
- ![](../../assets/icons/tensura/skill/magic_sense.png) [Magic Sense](../../tensura-reincarnated/abilities/extra-skills/magic-sense.md)
- ![](../../assets/icons/tensura/skill/danger_sense.png) [Danger Sense](../../tensura-reincarnated/abilities/extra-skills/danger-sense.md)
- ![](../../assets/icons/tensura/skill/farsight.png) [Farsight](../../tensura-reincarnated/abilities/common-skills/farsight.md)
- ![](../../assets/icons/tensura/skill/flame_attack_resistance.png) [Flame Attack Resistance](../../tensura-reincarnated/abilities/resistance-skills/flame-attack-resistance.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Scale | -0.1 | add |
| Scale | size | add |
| Max Health | max HP | add |
| Max Spiritual Health | max spiritual HP | add |
| Attack Damage | attack | add |
| Attack Speed | attack speed | add |
| Knockback Resistance | knockback resistance | add |
| Movement Speed | movement speed | add |
| Swim Speed Multiplier | swim speed | add |

## Stats (config defaults)

Set in [`config/tensura/race/beastfolk_config.toml`](../../tensura-reincarnated/configs/config-tensura-race-beastfolk-config.md).

| Option | Default | Description |
|---|---|---|
| `Beastfolk.minAura` | 1,500 | Minimal aura. |
| `Beastfolk.maxAura` | 2,500 | Maximum aura. |
| `Beastfolk.minMagicule` | 300 | Minimal magicule. |
| `Beastfolk.maxMagicule` | 600 | Maximum magicule. |
| `Beastfolk.size` | 0 | Bonus Size. |
| `Beastfolk.maxHealth` | 2 | Bonus Max Health. |
| `Beastfolk.maxSpiritualHealth` | 10 | Bonus Max Spiritual Health. |
| `Beastfolk.attack` | 0 | Bonus Attack Damage. |
| `Beastfolk.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `Beastfolk.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Beastfolk.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `Beastfolk.swimSpeed` | 0.5 | Bonus Swimming Speed Multiplier. |
