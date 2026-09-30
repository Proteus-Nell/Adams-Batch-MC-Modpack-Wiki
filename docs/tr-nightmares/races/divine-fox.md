# Divine Fox

<small>[TR: Nightmares](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `trnightmare:divine_fox` |
| **Stage** | <span class="stage stage-final">Final</span> |
| **Difficulty** | Hard |
| **Alignment** | Default |
| **Aura** | 800,000 - 1,400,000 |
| **Magicule** | 1,600,000 - 2,800,000 |
| **Health bonus** | 999 |
| **Spiritual health bonus** | 6,541 |
| **Attack damage bonus** | 3.6 |
| **Movement speed bonus** | 0.06 |
| **EP to evolve into** | 2,000,000 |

</div>

> The apex of the mystic fox lineage.

## Evolution

- **Evolves from:** [Soul Beast](soul-beast.md)

### Requirements to evolve into Divine Fox

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 2,000,000 | 100% |

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
| Scale | 0 | add |
| Max Health | 999 | add |
| Max Spiritual Health | 6,541 | add |
| Attack Damage | 3.6 | add |
| Attack Speed | 0.45 | add |
| Knockback Resistance | 0.85 | add |
| Movement Speed | 0.06 | add |
| Swim Speed Multiplier | 0.15 | add |

## Stats (config defaults)

Set in [`config/nightmare/race/mystic_fox_config.toml`](../configs/config-nightmare-race-mystic-fox-config.md).

| Option | Default | Description |
|---|---|---|
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
