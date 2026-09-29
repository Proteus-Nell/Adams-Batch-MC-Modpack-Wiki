# Daemon Lord

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:daemon_lord` |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 100,000 - 300,000 |
| **Magicule** | 200,000 - 500,000 |
| **Health bonus** | 646 |
| **Spiritual health bonus** | 3,606 |
| **Attack damage bonus** | 3 |
| **Movement speed bonus** | 0.04 |
| **EP to evolve into** | 140,000 |

</div>

> One of the most powerful evolutionary stages of daemons, achieved only by the most powerful arch daemons.

## Evolution

- **Evolves from:** [Arch Daemon](arch-daemon.md)
- **Evolves into:** [Devil Lord](devil-lord.md)
- **Default evolution:** [Devil Lord](devil-lord.md)

### Requirements to evolve into Daemon Lord

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Awaken [True Demon Lord./True Hero.] | 50% |
| Be named | 50% |
| Have a physical body | 50% |

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

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/magic_resistance.png) [Magic Resistance](../abilities/resistance-skills/magic-resistance.md)
- ![](../../assets/icons/tensura/skill/possession.png) [Possession](../abilities/intrinsic-skills/possession.md)

## Traits

- Daemon
- EP is limited in the central world
- Has creative-style flight

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 646 | add |
| Max Spiritual Health | 3,606 | add |
| Attack Damage | 3 | add |
| Attack Speed | 0.5 | add |
| Knockback Resistance | 0.6 | add |
| Movement Speed | 0.04 | add |
| Swim Speed Multiplier | 0.4 | add |

## Stats (config defaults)

Set in [`config/tensura/race/daemon_config.toml`](../configs/config-tensura-race-daemon-config.md).

| Option | Default | Description |
|---|---|---|
| `DaemonLord.minAura` | 100,000 | Minimal aura. |
| `DaemonLord.maxAura` | 300,000 | Maximum aura. |
| `DaemonLord.minMagicule` | 200,000 | Minimal magicule. |
| `DaemonLord.maxMagicule` | 500,000 | Maximum magicule. |
| `DaemonLord.size` | 0 | Bonus Size. |
| `DaemonLord.maxHealth` | 646 | Bonus Max Health. |
| `DaemonLord.maxSpiritualHealth` | 3,606 | Bonus Max Spiritual Health. |
| `DaemonLord.attack` | 3 | Bonus Attack Damage. |
| `DaemonLord.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `DaemonLord.knockbackResistance` | 0.6 | Bonus Knockback Resistance. |
| `DaemonLord.movementSpeed` | 0.04 | Bonus Movement Speed. |
| `DaemonLord.swimSpeed` | 0.4 | Bonus Swimming Speed Multiplier. |
| `DaemonLord.learnableMagics` | "tensura:mud_spears", "tensura:icicle_rain", "tensura:ice_breaker", "tensura:thunder_rain", "tensura:dimension_cutter", "tensura:full_recovery", "tensura:explosion", "tensura:dominate", "tensura:mirage", "tensura:reinforced_barrier" | List of Magics that players automatically get as learnable. |
| `ArchDaemon.epRequirement` | 140,000 | EP requirement to evolve into Arch Daemon. |
| `ArchDaemon.minAura` | 40,000 | Minimal aura. |
| `ArchDaemon.maxAura` | 40,000 | Maximum aura. |
| `ArchDaemon.minMagicule` | 100,000 | Minimal magicule. |
| `ArchDaemon.maxMagicule` | 100,000 | Maximum magicule. |
| `ArchDaemon.size` | 0 | Bonus Size. |
| `ArchDaemon.maxHealth` | 100 | Bonus Max Health. |
| `ArchDaemon.maxSpiritualHealth` | 606 | Bonus Max Spiritual Health. |
| `ArchDaemon.attack` | 2 | Bonus Attack Damage. |
| `ArchDaemon.attackSpeed` | 0.2 | Bonus Attack Speed. |
| `ArchDaemon.knockbackResistance` | 0.4 | Bonus Knockback Resistance. |
| `ArchDaemon.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `ArchDaemon.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
| `ArchDaemon.learnableMagics` | "tensura:stone_shot", "tensura:fire_ball", "tensura:fire_storm", "tensura:icicle_spear", "tensura:icicle_lance", "tensura:ice_blizzard", "tensura:thunder_orb", "tensura:warp_portal", "tensura:water_jail", "tensura:acid_shell", "tensura:tornado_blade", "tensura:airflow_shut", "tensura:lighten", "tensura:burden", "tensura:protection", "tensura:confusion", "tensura:invisible", "tensura:recovery", "tensura:healing_rain", "tensura:antidote" ... (22 total) | List of Magics that players automatically get as learnable. |
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

`tensura:races/daemon`, `tensura:races/has_creative_flight`, `tensura:races/limited_ep_in_central`
