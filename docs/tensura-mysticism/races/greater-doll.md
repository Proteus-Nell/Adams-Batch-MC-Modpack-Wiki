# Greater Doll

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:greater_doll` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 15,000 - 25,000 |
| **Magicule** | 30,000 - 60,000 |
| **Health bonus** | 50 |
| **Spiritual health bonus** | 200 |
| **Attack damage bonus** | 1.2 |
| **Movement speed bonus** | 0 |
| **EP to evolve into** | 20,000 |

</div>

> The result of a Greater Daemon possessing a magisteel body.

## Evolution

- **Evolves from:** [Greater Daemon](../../tensura-reincarnated/races/greater-daemon.md)
- **Evolves into:** [Arch Doll](arch-doll.md)
- **Default evolution:** [Arch Doll](arch-doll.md)
- **On awakening (True Demon Lord / True Hero):** [Daemon Doll](daemon-doll.md)
- **During the Harvest Festival:** [Arch Doll](arch-doll.md)

### Requirements to evolve into Greater Doll

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Possess a Bone Golem. | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Arch Doll"]
  r1["Chaos Doll"]
  r2["Chaos Metalloid"]
  r3["Daemon Doll"]
  r4["Devil Doll"]
  r5["Greater Doll"]
  r6["Arch Daemon"]
  r7["Daemon Lord"]
  r8["Devil Lord"]
  r9["Greater Daemon"]
  r10["Lesser Daemon"]
  r0 --> r1
  r0 --> r3
  r1 --> r2
  r3 --> r4
  r5 --> r0
  r5 --> r3
  r6 --> r7
  r7 --> r8
  r9 --> r5
  r9 --> r6
  r10 --> r6
  r10 --> r9
```

## Traits

- Has creative-style flight
- Spiritual lifeform

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 50 | add |
| Max Spiritual Health | 200 | add |
| Attack Damage | 1.2 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 0.4 | add |
| Movement Speed | 0 | add |
| Swim Speed Multiplier | 0 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/daemon_doll_config.toml`](../configs/config-mysticism-race-daemon-doll-config.md).

| Option | Default | Description |
|---|---|---|
| `GreaterDoll.minAura` | 15,000 | Minimal aura. |
| `GreaterDoll.maxAura` | 25,000 | Maximum aura. |
| `GreaterDoll.minMagicule` | 30,000 | Minimal magicule. |
| `GreaterDoll.maxMagicule` | 60,000 | Maximum magicule. |
| `GreaterDoll.size` | 0 | Bonus Size. |
| `GreaterDoll.maxHealth` | 50 | Bonus Max Health. |
| `GreaterDoll.maxSpiritualHealth` | 200 | Bonus Max Spiritual Health. |
| `GreaterDoll.attack` | 1.2 | Bonus Attack Damage. |
| `GreaterDoll.attackSpeed` | 0 | Bonus Attack Speed. |
| `GreaterDoll.knockbackResistance` | 0.4 | Bonus Knockback Resistance. |
| `GreaterDoll.movementSpeed` | 0 | Bonus Movement Speed. |
| `GreaterDoll.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `GreaterDoll.intrinsicSkills` | "mysticism:magisteel_body" | The list of intrinsic skills that the race gets. |

Set in [`config/tensura/race/daemon_config.toml`](../../tensura-reincarnated/configs/config-tensura-race-daemon-config.md).

| Option | Default | Description |
|---|---|---|
| `GreaterDaemon.epRequirement` | 20,000 | EP requirement to evolve into Greater Daemon. |
| `GreaterDaemon.minAura` | 10,000 | Minimal aura. |
| `GreaterDaemon.maxAura` | 20,000 | Maximum aura. |
| `GreaterDaemon.minMagicule` | 10,000 | Minimal magicule. |
| `GreaterDaemon.maxMagicule` | 30,000 | Maximum magicule. |
| `GreaterDaemon.size` | 0.25 | Bonus Size. |
| `GreaterDaemon.maxHealth` | 60 | Bonus Max Health. |
| `GreaterDaemon.maxSpiritualHealth` | 200 | Bonus Max Spiritual Health. |
| `GreaterDaemon.attack` | 1 | Bonus Attack Damage. |
| `GreaterDaemon.attackSpeed` | 0 | Bonus Attack Speed. |
| `GreaterDaemon.knockbackResistance` | 0.2 | Bonus Knockback Resistance. |
| `GreaterDaemon.movementSpeed` | 0 | Bonus Movement Speed. |
| `GreaterDaemon.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `GreaterDaemon.learnableMagics` | "tensura:mud_hand", "tensura:earth_wall", "tensura:fire_lance", "tensura:fire_wall", "tensura:icicle_lance", "tensura:ice_wall", "tensura:thunder", "tensura:thunder_lance", "tensura:spatial_storage", "tensura:wind_cutter", "tensura:sleep_mist", "tensura:water_cutter_aspectual", "tensura:wind_protection", "tensura:float", "tensura:healing", "tensura:flame_wall", "tensura:agility", "tensura:reinforcement", "tensura:strength_aspectual", "tensura:magic_wall" | List of Magics that players automatically get as learnable. |
| `LesserDaemon.minAura` | 2,000 | Minimal aura. |
| `LesserDaemon.maxAura` | 3,000 | Maximum aura. |
| `LesserDaemon.minMagicule` | 5,000 | Minimal magicule. |
| `LesserDaemon.maxMagicule` | 6,000 | Maximum magicule. |
| `LesserDaemon.size` | 0.5 | Bonus Size. |
| `LesserDaemon.maxHealth` | 20 | Bonus Max Health. |
| `LesserDaemon.maxSpiritualHealth` | 90 | Bonus Max Spiritual Health. |
| `LesserDaemon.attack` | 0.4 | Bonus Attack Damage. |
| `LesserDaemon.attackSpeed` | -0.5 | Bonus Attack Speed. |
| `LesserDaemon.knockbackResistance` | 0.1 | Bonus Knockback Resistance. |
| `LesserDaemon.movementSpeed` | 0 | Bonus Movement Speed. |
| `LesserDaemon.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `LesserDaemon.learnableMagics` | "tensura:earth_lock", "tensura:liquidize", "tensura:fire_aspectual", "tensura:water_aspectual", "tensura:drainage", "tensura:wind_gust", "tensura:escape", "tensura:freeze" | List of Magics that players automatically get as learnable. |

## Tags

`tensura:races/has_creative_flight`, `tensura:races/spiritual`
