# Heavenly Restriction

<small>[Tensura: Mysticism](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `mysticism:heavenly_restriction` |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 2,000,000 - 2,000,000 |
| **Magicule** | 100 - 100 |
| **Health bonus** | 1,470 |
| **Spiritual health bonus** | 9,000 |
| **Attack damage bonus** | 4.5 |
| **Movement speed bonus** | 0.15 |
| **EP to evolve into** | 4,000,000 |

</div>

## Evolution

- **Evolves from:** [Bound Enlightenment](bound-enlightenment.md)
- **During the Harvest Festival:** [Restricted Saint](restricted-saint.md)

### Requirements to evolve into Heavenly Restriction

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 4,000,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Bound Enlightenment"]
  r1["Heavenly Restriction"]
  r2["Restricted Human"]
  r3["Restricted Saint"]
  r0 --> r1
  r1 --> r3
  r2 --> r0
  r2 --> r3
  r3 --> r0
```

## Traits

- Divine

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 1,470 | add |
| Max Spiritual Health | 9,000 | add |
| Attack Damage | 4.5 | add |
| Attack Speed | 1.05 | add |
| Knockback Resistance | 0.45 | add |
| Movement Speed | 0.15 | add |
| Swim Speed Multiplier | 1.5 | add |

## Stats (config defaults)

Set in [`config/mysticism/race/restricted_human_config.toml`](../configs/config-mysticism-race-restricted-human-config.md).

| Option | Default | Description |
|---|---|---|
| `HeavenlyRestriction.epRequirement` | 4,000,000 | EP requirement to evolve into Heavenly Restriction. |
| `HeavenlyRestriction.minAura` | 2,000,000 | Minimal aura. |
| `HeavenlyRestriction.maxAura` | 2,000,000 | Maximum aura. |
| `HeavenlyRestriction.minMagicule` | 100 | Minimal magicule. |
| `HeavenlyRestriction.maxMagicule` | 100 | Maximum magicule. |
| `HeavenlyRestriction.size` | 0 | Bonus Size. |
| `HeavenlyRestriction.maxHealth` | 1,470 | Bonus Max Health. |
| `HeavenlyRestriction.maxSpiritualHealth` | 9,000 | Bonus Max Spiritual Health. |
| `HeavenlyRestriction.attack` | 4.5 | Bonus Attack Damage. |
| `HeavenlyRestriction.attackSpeed` | 1.05 | Bonus Attack Speed. |
| `HeavenlyRestriction.knockbackResistance` | 0.45 | Bonus Knockback Resistance. |
| `HeavenlyRestriction.movementSpeed` | 0.15 | Bonus Movement Speed. |
| `HeavenlyRestriction.swimSpeed` | 1.5 | Bonus Swimming Speed Multiplier. |
| `HeavenlyRestriction.intrinsicSkills` | "mysticism:restricted", "mysticism:tenacity", "tensura:divine_ki_release" | The list of intrinsic skills that the race gets. |
| `RestrictedHuman.epRequirement` | 50,000 | EP requirement to evolve into Restricted Human. |
| `RestrictedHuman.bossRequirement` | 2 | The number of Bosses defeated to evolve into Restricted Human. |
| `RestrictedHuman.minAura` | 1,520 | Minimal aura. |
| `RestrictedHuman.maxAura` | 2,280 | Maximum aura. |
| `RestrictedHuman.minMagicule` | 50 | Minimal magicule. |
| `RestrictedHuman.maxMagicule` | 70 | Maximum magicule. |
| `RestrictedHuman.size` | 0 | Bonus Size. |
| `RestrictedHuman.maxHealth` | 10 | Bonus Max Health. |
| `RestrictedHuman.maxSpiritualHealth` | 0 | Bonus Max Spiritual Health. |
| `RestrictedHuman.attack` | 0.5 | Bonus Attack Damage. |
| `RestrictedHuman.attackSpeed` | 0.1 | Bonus Attack Speed. |
| `RestrictedHuman.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `RestrictedHuman.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `RestrictedHuman.swimSpeed` | 0.1 | Bonus Swimming Speed Multiplier. |
| `RestrictedHuman.intrinsicSkills` | "mysticism:restricted" | The list of intrinsic skills that the race gets. |

Set in [`config/tensura/race/human_config.toml`](../../tensura-reincarnated/configs/config-tensura-race-human-config.md).

| Option | Default | Description |
|---|---|---|
| `Human.minAura` | 760 | Minimal aura. |
| `Human.maxAura` | 1,140 | Maximum aura. |
| `Human.minMagicule` | 50 | Minimal magicule. |
| `Human.maxMagicule` | 70 | Maximum magicule. |
| `Human.size` | 0 | Bonus Size. |
| `Human.maxHealth` | 0 | Bonus Max Health. |
| `Human.maxSpiritualHealth` | 0 | Bonus Max Spiritual Health. |
| `Human.attack` | 0 | Bonus Attack Damage. |
| `Human.attackSpeed` | 0 | Bonus Attack Speed. |
| `Human.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `Human.movementSpeed` | 0 | Bonus Movement Speed. |
| `Human.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |

## Tags

`tensura:races/divine`
