# Medium Class Saiyan

<small>[Elite Tensura](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `elitetensura:medium_saiyan` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Extreme |
| **Alignment** | Default |
| **Aura** | 6,000 - 10,000 |
| **Magicule** | 12,000 - 20,000 |
| **Health bonus** | 12 |
| **Spiritual health bonus** | 5 |
| **Attack damage bonus** | 2 |
| **Movement speed bonus** | 0.01 |
| **EP to evolve into** | 100,000 |

</div>

## Evolution

- **Evolves from:** [Lesser Saiyan](lesser-saiyan.md)
- **Evolves into:** [High Class Saiyan](high-saiyan.md)
- **Default evolution:** [High Class Saiyan](high-saiyan.md)
- **On awakening (True Demon Lord / True Hero):** [High Class Saiyan](high-saiyan.md)

### Requirements to evolve into Medium Class Saiyan

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 100,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Divine Saiyan"]
  r1["High Class Saiyan"]
  r2["Lesser Saiyan"]
  r3["Medium Class Saiyan"]
  r1 --> r0
  r2 --> r1
  r2 --> r3
  r3 --> r1
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/body_armor.png) [Body Armor](../../tensura-reincarnated/abilities/intrinsic-skills/body-armor.md)
- ![](../../assets/icons/tensura/skill/charm.png) [Charm](../../tensura-reincarnated/abilities/intrinsic-skills/charm.md)
- ![](../../assets/icons/tensura/skill/sage.png) [Sage](../../tensura-reincarnated/abilities/extra-skills/sage.md)
- ![](../../assets/icons/tensura/skill/absorb_and_dissolve.png) [Absorb &amp; Dissolve](../../tensura-reincarnated/abilities/intrinsic-skills/absorb-and-dissolve.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 12 | add |
| Max Spiritual Health | 5 | add |
| Attack Damage | 2 | add |
| Attack Speed | 0.5 | add |
| Knockback Resistance | 0 | add |
| Movement Speed | 0.01 | add |
| Swim Speed Multiplier | 0 | add |

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/Races.toml`](../configs/config-tensura-elitetensura-races.md).

| Option | Default | Description |
|---|---|---|
| `mediumSaiyan.minAura` | 6,000 | Minimal aura. |
| `mediumSaiyan.maxAura` | 10,000 | Maximum aura. |
| `mediumSaiyan.minMagicule` | 12,000 | Minimal magicule. |
| `mediumSaiyan.maxMagicule` | 20,000 | Maximum magicule. |
| `mediumSaiyan.size` | 0 | Bonus Size. |
| `mediumSaiyan.maxHealth` | 12 | Bonus Max Health. |
| `mediumSaiyan.maxSpiritualHealth` | 5 | Bonus Max Spiritual Health. |
| `mediumSaiyan.attack` | 2 | Bonus Attack Damage. |
| `mediumSaiyan.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `mediumSaiyan.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `mediumSaiyan.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `mediumSaiyan.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `mediumSaiyan.epRequirement` | 100,000 |  |
| `lesserSaiyan.epRequirement` | 0 | EP required to enter this race (starter tier — 0 = no gate). |
| `lesserSaiyan.minAura` | 2,000 | Minimal aura. |
| `lesserSaiyan.maxAura` | 3,000 | Maximum aura. |
| `lesserSaiyan.minMagicule` | 5,000 | Minimal magicule. |
| `lesserSaiyan.maxMagicule` | 6,000 | Maximum magicule. |
| `lesserSaiyan.size` | 0 | Bonus Size. |
| `lesserSaiyan.maxHealth` | 5 | Bonus Max Health. |
| `lesserSaiyan.maxSpiritualHealth` | 10 | Bonus Max Spiritual Health. |
| `lesserSaiyan.attack` | 0.5 | Bonus Attack Damage. |
| `lesserSaiyan.attackSpeed` | 0 | Bonus Attack Speed. |
| `lesserSaiyan.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `lesserSaiyan.movementSpeed` | 0 | Bonus Movement Speed. |
| `lesserSaiyan.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `lesserSaiyan.learnableMagics` | "tensura:earth_lock", "tensura:liquidize", "tensura:fire_aspectual", "tensura:water_aspectual", "tensura:drainage", "tensura:wind_gust", "tensura:escape", "tensura:freeze" |  |
