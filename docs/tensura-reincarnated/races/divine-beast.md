# Divine Beast

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:divine_beast` |
| **Difficulty** | Easy |
| **Alignment** | Holy |
| **Aura** | 1,000,000 - 1,000,000 |
| **Magicule** | 1,000,000 - 1,000,000 |
| **Health bonus** | 1,180 |
| **Spiritual health bonus** | 7,940 |
| **Attack damage bonus** | 7 |
| **Movement speed bonus** | 0.12 |
| **EP to evolve into** | 2,000,000 |

</div>

> Beastfolk that achieved divinity, possessing an immortal physical body that will never age.

## Evolution

- **Evolves from:** [Spirit Beast](spirit-beast.md)

### Requirements to evolve into Divine Beast

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 2,000,000 | 100% |

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

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/divine_ki_release.png) [Divine Ki Release](../abilities/intrinsic-skills/divine-ki-release.md)

## Traits

- Beastfolk
- Divine

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 1,180 | add |
| Max Spiritual Health | 7,940 | add |
| Attack Damage | 7 | add |
| Attack Speed | 0.9 | add |
| Knockback Resistance | 0.3 | add |
| Movement Speed | 0.12 | add |
| Swim Speed Multiplier | 1.2 | add |

## Stats (config defaults)

Set in [`config/tensura/race/beastfolk_config.toml`](../configs/config-tensura-race-beastfolk-config.md).

| Option | Default | Description |
|---|---|---|
| `DivineBeast.epRequirement` | 2,000,000 | EP requirement to evolve into Divine Beast. |
| `DivineBeast.minAura` | 1,000,000 | Minimal aura. |
| `DivineBeast.maxAura` | 1,000,000 | Maximum aura. |
| `DivineBeast.minMagicule` | 1,000,000 | Minimal magicule. |
| `DivineBeast.maxMagicule` | 1,000,000 | Maximum magicule. |
| `DivineBeast.size` | 0 | Bonus Size. |
| `DivineBeast.maxHealth` | 1,180 | Bonus Max Health. |
| `DivineBeast.maxSpiritualHealth` | 7,940 | Bonus Max Spiritual Health. |
| `DivineBeast.attack` | 7 | Bonus Attack Damage. |
| `DivineBeast.attackSpeed` | 0.9 | Bonus Attack Speed. |
| `DivineBeast.knockbackResistance` | 0.3 | Bonus Knockback Resistance. |
| `DivineBeast.movementSpeed` | 0.12 | Bonus Movement Speed. |
| `DivineBeast.swimSpeed` | 1.2 | Bonus Swimming Speed Multiplier. |
| `SpiritBeast.epRequirement` | 400,000 | EP requirement to evolve into Spirit Beast. |
| `SpiritBeast.bossRequirement` | 4 | The number of Bosses defeated to evolve into Spirit Beast. |
| `SpiritBeast.minAura` | 400,000 | Minimal aura. |
| `SpiritBeast.maxAura` | 400,000 | Maximum aura. |
| `SpiritBeast.minMagicule` | 400,000 | Minimal magicule. |
| `SpiritBeast.maxMagicule` | 400,000 | Maximum magicule. |
| `SpiritBeast.size` | 0 | Bonus Size. |
| `SpiritBeast.maxHealth` | 580 | Bonus Max Health. |
| `SpiritBeast.maxSpiritualHealth` | 6,340 | Bonus Max Spiritual Health. |
| `SpiritBeast.attack` | 4 | Bonus Attack Damage. |
| `SpiritBeast.attackSpeed` | 0.6 | Bonus Attack Speed. |
| `SpiritBeast.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `SpiritBeast.movementSpeed` | 0.1 | Bonus Movement Speed. |
| `SpiritBeast.swimSpeed` | 1 | Bonus Swimming Speed Multiplier. |
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

`tensura:races/beastfolk`, `tensura:races/divine`
