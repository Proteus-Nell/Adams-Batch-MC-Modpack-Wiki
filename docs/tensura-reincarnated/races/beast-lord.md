# Beast Lord

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:beast_lord` |
| **Difficulty** | Easy |
| **Alignment** | Default |
| **Aura** | 100,000 - 100,000 |
| **Magicule** | 100,000 - 100,000 |
| **Health bonus** | 140 |
| **Spiritual health bonus** | 440 |
| **Attack damage bonus** | 3 |
| **Movement speed bonus** | 0.06 |
| **EP to evolve into** | 100,000 |

</div>

> Beastfolk that has "evolved the correct way" and became a Demi-Spiritual Lifeform.

## Evolution

- **Evolves from:** [Beastfolk](beastfolk.md)
- **Evolves into:** [Spirit Beast](spirit-beast.md)
- **Default evolution:** [Spirit Beast](spirit-beast.md)
- **On awakening (True Demon Lord / True Hero):** [Spirit Beast](spirit-beast.md)

### Requirements to evolve into Beast Lord

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 100,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Beast Lord"]
  r1["Beastfolk"]
  r2["Divine Beast"]
  r3["Spirit Beast"]
  r0 --> r3
  r1 --> r0
  r1 --> r3
  r3 --> r2
```

## Traits

- Beastfolk

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 140 | add |
| Max Spiritual Health | 440 | add |
| Attack Damage | 3 | add |
| Attack Speed | 0.3 | add |
| Knockback Resistance | 0.1 | add |
| Movement Speed | 0.06 | add |
| Swim Speed Multiplier | 0.7 | add |

## Stats (config defaults)

Set in [`config/tensura/race/beastfolk_config.toml`](../configs/config-tensura-race-beastfolk-config.md).

| Option | Default | Description |
|---|---|---|
| `BeastLord.epRequirement` | 100,000 | EP requirement to evolve into Beast Lord. |
| `BeastLord.minAura` | 100,000 | Minimal aura. |
| `BeastLord.maxAura` | 100,000 | Maximum aura. |
| `BeastLord.minMagicule` | 100,000 | Minimal magicule. |
| `BeastLord.maxMagicule` | 100,000 | Maximum magicule. |
| `BeastLord.size` | 0 | Bonus Size. |
| `BeastLord.maxHealth` | 140 | Bonus Max Health. |
| `BeastLord.maxSpiritualHealth` | 440 | Bonus Max Spiritual Health. |
| `BeastLord.attack` | 3 | Bonus Attack Damage. |
| `BeastLord.attackSpeed` | 0.3 | Bonus Attack Speed. |
| `BeastLord.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `BeastLord.movementSpeed` | 0.06 | Bonus Movement Speed. |
| `BeastLord.swimSpeed` | 0.7 | Bonus Swimming Speed Multiplier. |
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

## Tags

`tensura:races/beastfolk`
