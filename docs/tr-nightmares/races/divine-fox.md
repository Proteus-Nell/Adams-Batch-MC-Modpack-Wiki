# Divine Fox

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:divine_fox` |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 1,000 - 2,000 |
| **Magicule** | 2,000 - 4,000 |
| **Health bonus** | 15 |
| **Spiritual health bonus** | 60 |
| **Attack damage bonus** | 0 |
| **Movement speed bonus** | 0 |
| **EP to evolve into** | 0 |

</div>

> The apex of the mystic fox lineage.

## Evolution

- **Evolves from:** [Soul Beast](soul-beast.md)

### Requirements to evolve into Divine Fox

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of ep requirement | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Divine Fox"]
  r1["Greater Mystic Fox"]
  r2["Lesser Mystic Fox"]
  r3["Ninehead"]
  r4["Ninetail"]
  r5["Soul Beast"]
  r1 --> r3
  r2 --> r1
  r3 --> r4
  r4 --> r5
  r5 --> r0
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/abnormal_condition_nullification.png) [Abnormal Condition Nullification](../../tensura-reincarnated/abilities/resistance-skills/abnormal-condition-nullification.md)
- ![](../../assets/icons/tensura/skill/divine_ki_release.png) [Divine Ki Release](../../tensura-reincarnated/abilities/intrinsic-skills/divine-ki-release.md)
-  [Beast Unification](../abilities/intrinsic-skills/beast-unification.md)
-  [Beast Domination](../abilities/intrinsic-skills/beast-domination.md)

## Traits

- Divine

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | size | add |
| Max Health | max HP | add |
| Max Spiritual Health | max spiritual HP | add |
| Attack Damage | attack | add |
| Attack Speed | attack speed | add |
| Knockback Resistance | knockback resistance | add |
| Movement Speed | movement speed | add |
| Swim Speed Multiplier | swim speed | add |

## Stats (config defaults)

Set in [`config/nightmare/race/mystic_fox_config.toml`](../configs/config-nightmare-race-mystic-fox-config.md).

| Option | Default | Description |
|---|---|---|
| `DivineFox.epRequirement` | 0 | EP requirement to evolve into this tier. |
| `DivineFox.minAura` | 1,000 | Minimal aura. |
| `DivineFox.maxAura` | 2,000 | Maximum aura. |
| `DivineFox.minMagicule` | 2,000 | Minimal magicule. |
| `DivineFox.maxMagicule` | 4,000 | Maximum magicule. |
| `DivineFox.size` | 0 | Bonus Size. |
| `DivineFox.maxHealth` | 15 | Bonus Max Health. |
| `DivineFox.maxSpiritualHealth` | 60 | Bonus Max Spiritual Health. |
| `DivineFox.attack` | 0 | Bonus Attack Damage. |
| `DivineFox.attackSpeed` | 0 | Bonus Attack Speed. |
| `DivineFox.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `DivineFox.movementSpeed` | 0 | Bonus Movement Speed. |
| `DivineFox.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `DivineFox.epRequirement` | 2,000,000 |  |
| `DivineFox.minAura` | 800,000 |  |
| `DivineFox.maxAura` | 1,400,000 |  |
| `DivineFox.minMagicule` | 1,600,000 |  |
| `DivineFox.maxMagicule` | 2,800,000 |  |
| `DivineFox.size` | 0 |  |
| `DivineFox.maxHealth` | 999 |  |
| `DivineFox.maxSpiritualHealth` | 6,541 |  |
| `DivineFox.attack` | 3.6 |  |
| `DivineFox.attackSpeed` | 0.45 |  |
| `DivineFox.knockbackResistance` | 0.85 |  |
| `DivineFox.movementSpeed` | 0.06 |  |
| `DivineFox.swimSpeed` | 0.15 |  |

## Tags

`tensura:races/divine`
