# True Dragonoid

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:true_dragonoid` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 1,000,000 - 1,000,000 |
| **Magicule** | 1,000,000 - 1,000,000 |
| **Health bonus** | 0 |
| **Spiritual health bonus** | 20 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0 |
| **EP to evolve into** | 2,000,000 |

</div>

> A child of the stars and hopes of the world. A being that has achieved divinity, challenging the existence that brought you into this world.

## Evolution

- **Evolves from:** [Dragonoid](dragonoid.md)

### Requirements to evolve into True Dragonoid

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 2,000,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Dragonoid"]
  r1["True Dragonoid"]
  r0 --> r1
```

## Traits

- Divine
- Has creative-style flight

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 0 | add |
| Max Spiritual Health | 20 | add |
| Attack Damage | 0 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0 | add |
| Movement Speed | 0 | add |
| Swim Speed Multiplier | 0 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/dragonoid_config.toml`](../configs/config-mysticism-race-dragonoid-config.md).

| Option | Default | Description |
|---|---|---|
| `TrueDragonoid.epRequirement` | 2,000,000 | EP requirement to evolve into True Dragonoid. |
| `TrueDragonoid.minAura` | 1,000,000 | Minimal aura. |
| `TrueDragonoid.maxAura` | 1,000,000 | Maximum aura. |
| `TrueDragonoid.minMagicule` | 1,000,000 | Minimal magicule. |
| `TrueDragonoid.maxMagicule` | 1,000,000 | Maximum magicule. |
| `TrueDragonoid.size` | 0 | Bonus Size. |
| `TrueDragonoid.maxHealth` | 0 | Bonus Max Health. |
| `TrueDragonoid.maxSpiritualHealth` | 20 | Bonus Max Spiritual Health. |
| `TrueDragonoid.attack` | 0 | Bonus Attack Damage. |
| `TrueDragonoid.attackSpeed` | 0 | Bonus Attack Speed. |
| `TrueDragonoid.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `TrueDragonoid.movementSpeed` | 0 | Bonus Movement Speed. |
| `TrueDragonoid.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `TrueDragonoid.intrinsicSkills` | "tensura:divine_ki_release", "tensura:dragon_ear", "tensura:dragon_eye" | The list of intrinsic skills that the race gets. |
| `Dragonoid.minMP` | 10,000 | Dragonoid Min MP. |
| `Dragonoid.maxMP` | 1,000,000 | Dragonoid Max MP. |
| `Dragonoid.dragonoidMinHP` | 30 | Min amount of HP. |
| `Dragonoid.dragonoidMaxHP` | 1,080 | Min amount of HP. |
| `Dragonoid.dragonoidMinAttackDamage` | 1 | Min amount of attack damage. |
| `Dragonoid.dragonoidMaxAttackDamage` | 5 | Min amount of attack damage. |
| `Dragonoid.dragonoidMinAttackSpeed` | 4 | Min amount of attack speed. |
| `Dragonoid.dragonoidMaxAttackSpeed` | 6 | Max amount of attack speed. |
| `Dragonoid.dragonoidMinMovementSpeed` | 0.1 | Min amount of movement speed. |
| `Dragonoid.dragonoidMaxMovementSpeed` | 0.18 | Max amount of movement speed. |
| `Dragonoid.minAura` | 5,000 | Minimal aura. |
| `Dragonoid.maxAura` | 5,000 | Maximum aura. |
| `Dragonoid.minMagicule` | 5,000 | Minimal magicule. |
| `Dragonoid.maxMagicule` | 5,000 | Maximum magicule. |
| `Dragonoid.size` | 0 | Bonus Size. |
| `Dragonoid.maxHealth` | 0 | Bonus Max Health. |
| `Dragonoid.maxSpiritualHealth` | 20 | Bonus Max Spiritual Health. |
| `Dragonoid.attack` | 0 | Bonus Attack Damage. |
| `Dragonoid.attackSpeed` | 0 | Bonus Attack Speed. |
| `Dragonoid.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Dragonoid.movementSpeed` | 0 | Bonus Movement Speed. |
| `Dragonoid.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `Dragonoid.intrinsicSkills` | "tensura:dragon_ear", "tensura:dragon_eye" | The list of intrinsic skills that the race gets. |

## Tags

`tensura:races/divine`, `tensura:races/has_creative_flight`
