# Lesser Saiyan

<small>[Elite Tensura](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `elitetensura:lesser_saiyan` |
| **Stage** | <span class="stage stage-starting">Starting</span> |
| **Difficulty** | Extreme |
| **Alignment** | Default |
| **Aura** | 2,000 - 3,000 |
| **Magicule** | 5,000 - 6,000 |
| **Health bonus** | 5 |
| **Spiritual health bonus** | 10 |
| **Attack damage bonus** | 0.5 |
| **Movement speed bonus** | 0 |
| **EP to evolve into** | 0 |

</div>

## Evolution

- **Evolves into:** [Medium Class Saiyan](medium-saiyan.md)
- **Default evolution:** [Medium Class Saiyan](medium-saiyan.md)
- **On awakening (True Demon Lord / True Hero):** [High Class Saiyan](high-saiyan.md)
- **During the Harvest Festival:** [Medium Class Saiyan](medium-saiyan.md)

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

- ![](../../assets/icons/tensura/skill/absorb_and_dissolve.png) [Absorb &amp; Dissolve](../../tensura-reincarnated/abilities/intrinsic-skills/absorb-and-dissolve.md)

## Traits

- Human-like

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 5 | add |
| Max Spiritual Health | 10 | add |
| Attack Damage | 0.5 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0 | add |
| Movement Speed | 0 | add |
| Swim Speed Multiplier | 0 | add |

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/Races.toml`](../configs/config-tensura-elitetensura-races.md).

| Option | Default | Description |
|---|---|---|
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

## Tags

`tensura:races/human_like`
