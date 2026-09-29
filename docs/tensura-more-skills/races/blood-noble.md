# Blood Noble

<small>[TensuraMoreSkills](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensuramoreskills:blood_noble` |
| **Stage** | <span class="stage stage-in-between">In-between</span> |
| **Difficulty** | Hard |
| **Alignment** | Majin |
| **Aura** | 700,000 - 950,000 |
| **Magicule** | 850,000 - 1,200,000 |
| **Health bonus** | 700 |
| **Spiritual health bonus** | 5,000 |
| **Attack damage bonus** | 6.5 |
| **Movement speed bonus** | 0.055 |
| **EP to evolve into** | 1,500,000 |

</div>

> A highborn Bloodfiend capable of ruling lesser kindred. Blood Nobles possess a larger blood reserve, stronger regeneration, sharper Blood Arts, and a greater talent for binding weakened mobs into blood thralls.

## Evolution

- **Evolves from:** [Elder Bloodfiend](elder-bloodfiend.md)
- **Evolves into:** [Blood Monarch](blood-monarch.md)
- **Default evolution:** [Blood Monarch](blood-monarch.md)
- **During the Harvest Festival:** [Blood Monarch](blood-monarch.md)

### Requirements to evolve into Blood Noble

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of ep requirement | 45% |
| Kill boss requirement bosses | 20% |
| Blood | 20% |
| Thrall | 15% |

### Evolution tree

```mermaid
flowchart LR
  r0["Blood Monarch"]
  r1["Blood Noble"]
  r2["Bloodfiend"]
  r3["Crimson Progenitor"]
  r4["Elder Bloodfiend"]
  r0 --> r3
  r1 --> r0
  r2 --> r4
  r4 --> r1
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensuramoreskills/skill/blood_arts.png) [Blood Arts](../abilities/intrinsic-skills/blood-arts.md)

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

Set in [`config/tensuramoreskills-races.toml`](../configs/config-tensuramoreskills-races.md).

| Option | Default | Description |
|---|---|---|
| `evolution.epRequirement` | 1,500,000 (0 to no limit) | EP required to evolve into this race. The base Bloodfiend value is unused for normal starting race selection. |
| `evolution.bossRequirement` | 0 (0 to no limit) | Boss kills required to evolve into this race. Set to 0 to disable this requirement. |
| `evolution.bloodRequirement` | 5,500 (0 to no limit) | Total blood drained required to evolve into this race. Set to 0 to disable this requirement. |
| `evolution.mobTurnRequirement` | 50 (0 to no limit) | Total mobs or players turned into kindred required to evolve into this race. Set to 0 to disable this requirement. |
| `base_energy.minAura` | 700,000 (0 to no limit) | Minimum base aura for this race. |
| `base_energy.maxAura` | 950,000 (0 to no limit) | Maximum base aura for this race. |
| `base_energy.minMagicule` | 850,000 (0 to no limit) | Minimum base magicule for this race. |
| `base_energy.maxMagicule` | 1,200,000 (0 to no limit) | Maximum base magicule for this race. |
| `attributes.size` | 0.05 (-0.9 to 16) | Scale modifier for this race. 0 means normal size. |
| `attributes.maxHealth` | 700 (0 to no limit) | Max health bonus/value used by the race config. |
| `attributes.maxSpiritualHealth` | 5,000 (0 to no limit) | Max spiritual health bonus/value used by the race config. |
| `attributes.attack` | 6.5 (0 to no limit) | Attack damage bonus/value used by the race config. |
| `attributes.attackSpeed` | 0.42 (-1 to no limit) | Attack speed modifier used by the race config. |
| `attributes.knockbackResistance` | 0.28 (0 to 1) | Knockback resistance modifier used by the race config. |
| `attributes.movementSpeed` | 0.055 (-1 to no limit) | Movement speed modifier used by the race config. |
| `attributes.swimSpeed` | -0.15 (-1 to no limit) | Swim speed modifier. Negative values make Bloodfiends worse in water. |
| `blood.maxBlood` | 240 (1 to no limit) | Maximum stored blood for this race before generation penalties. |
| `blood.bloodRegenThreshold` | 80 (0 to no limit) | Blood amount required before passive blood regeneration can activate. |
| `evolution.epRequirement` | 0 (0 to no limit) | EP required to evolve into this race. The base Bloodfiend value is unused for normal starting race selection. |
| `evolution.bossRequirement` | 0 (0 to no limit) | Boss kills required to evolve into this race. Set to 0 to disable this requirement. |
| `evolution.bloodRequirement` | 0 (0 to no limit) | Total blood drained required to evolve into this race. Set to 0 to disable this requirement. |
| `evolution.mobTurnRequirement` | 0 (0 to no limit) | Total mobs or players turned into kindred required to evolve into this race. Set to 0 to disable this requirement. |
| `base_energy.minAura` | 7,500 (0 to no limit) | Minimum base aura for this race. |
| `base_energy.maxAura` | 12,000 (0 to no limit) | Maximum base aura for this race. |
| `base_energy.minMagicule` | 9,000 (0 to no limit) | Minimum base magicule for this race. |
| `base_energy.maxMagicule` | 16,000 (0 to no limit) | Maximum base magicule for this race. |
| `attributes.size` | 0 (-0.9 to 16) | Scale modifier for this race. 0 means normal size. |
| `attributes.maxHealth` | 20 (0 to no limit) | Max health bonus/value used by the race config. |
| `attributes.maxSpiritualHealth` | 120 (0 to no limit) | Max spiritual health bonus/value used by the race config. |
| `attributes.attack` | 1.5 (0 to no limit) | Attack damage bonus/value used by the race config. |
| `attributes.attackSpeed` | 0.1 (-1 to no limit) | Attack speed modifier used by the race config. |
| `attributes.knockbackResistance` | 0.05 (0 to 1) | Knockback resistance modifier used by the race config. |
| `attributes.movementSpeed` | 0.025 (-1 to no limit) | Movement speed modifier used by the race config. |
| `attributes.swimSpeed` | -0.35 (-1 to no limit) | Swim speed modifier. Negative values make Bloodfiends worse in water. |
| `blood.maxBlood` | 100 (1 to no limit) | Maximum stored blood for this race before generation penalties. |
| `blood.bloodRegenThreshold` | 45 (0 to no limit) | Blood amount required before passive blood regeneration can activate. |
| `evolution.epRequirement` | 120,000 (0 to no limit) | EP required to evolve into this race. The base Bloodfiend value is unused for normal starting race selection. |
| `evolution.bossRequirement` | 0 (0 to no limit) | Boss kills required to evolve into this race. Set to 0 to disable this requirement. |
| `evolution.bloodRequirement` | 400 (0 to no limit) | Total blood drained required to evolve into this race. Set to 0 to disable this requirement. |
| `evolution.mobTurnRequirement` | 5 (0 to no limit) | Total mobs or players turned into kindred required to evolve into this race. Set to 0 to disable this requirement. |
| `base_energy.minAura` | 40,000 (0 to no limit) | Minimum base aura for this race. |
| `base_energy.maxAura` | 65,000 (0 to no limit) | Maximum base aura for this race. |
| `base_energy.minMagicule` | 50,000 (0 to no limit) | Minimum base magicule for this race. |
| `base_energy.maxMagicule` | 85,000 (0 to no limit) | Maximum base magicule for this race. |
| `attributes.size` | 0 (-0.9 to 16) | Scale modifier for this race. 0 means normal size. |
| `attributes.maxHealth` | 80 (0 to no limit) | Max health bonus/value used by the race config. |
| `attributes.maxSpiritualHealth` | 900 (0 to no limit) | Max spiritual health bonus/value used by the race config. |
| `attributes.attack` | 2.5 (0 to no limit) | Attack damage bonus/value used by the race config. |
| `attributes.attackSpeed` | 0.18 (-1 to no limit) | Attack speed modifier used by the race config. |
| `attributes.knockbackResistance` | 0.1 (0 to 1) | Knockback resistance modifier used by the race config. |
| `attributes.movementSpeed` | 0.035 (-1 to no limit) | Movement speed modifier used by the race config. |
| `attributes.swimSpeed` | -0.28 (-1 to no limit) | Swim speed modifier. Negative values make Bloodfiends worse in water. |
| `blood.maxBlood` | 140 (1 to no limit) | Maximum stored blood for this race before generation penalties. |
| `blood.bloodRegenThreshold` | 55 (0 to no limit) | Blood amount required before passive blood regeneration can activate. |
| `evolution.epRequirement` | 450,000 (0 to no limit) | EP required to evolve into this race. The base Bloodfiend value is unused for normal starting race selection. |
| `evolution.bossRequirement` | 0 (0 to no limit) | Boss kills required to evolve into this race. Set to 0 to disable this requirement. |
| `evolution.bloodRequirement` | 1,500 (0 to no limit) | Total blood drained required to evolve into this race. Set to 0 to disable this requirement. |
| `evolution.mobTurnRequirement` | 18 (0 to no limit) | Total mobs or players turned into kindred required to evolve into this race. Set to 0 to disable this requirement. |
| `base_energy.minAura` | 160,000 (0 to no limit) | Minimum base aura for this race. |
| `base_energy.maxAura` | 240,000 (0 to no limit) | Maximum base aura for this race. |
| `base_energy.minMagicule` | 180,000 (0 to no limit) | Minimum base magicule for this race. |
| `base_energy.maxMagicule` | 300,000 (0 to no limit) | Maximum base magicule for this race. |
| `attributes.size` | 0 (-0.9 to 16) | Scale modifier for this race. 0 means normal size. |
| `attributes.maxHealth` | 300 (0 to no limit) | Max health bonus/value used by the race config. |
| `attributes.maxSpiritualHealth` | 2,500 (0 to no limit) | Max spiritual health bonus/value used by the race config. |
| `attributes.attack` | 4 (0 to no limit) | Attack damage bonus/value used by the race config. |
| `attributes.attackSpeed` | 0.28 (-1 to no limit) | Attack speed modifier used by the race config. |
| `attributes.knockbackResistance` | 0.18 (0 to 1) | Knockback resistance modifier used by the race config. |
| `attributes.movementSpeed` | 0.045 (-1 to no limit) | Movement speed modifier used by the race config. |
| `attributes.swimSpeed` | -0.22 (-1 to no limit) | Swim speed modifier. Negative values make Bloodfiends worse in water. |
| `blood.maxBlood` | 185 (1 to no limit) | Maximum stored blood for this race before generation penalties. |
| `blood.bloodRegenThreshold` | 65 (0 to no limit) | Blood amount required before passive blood regeneration can activate. |
| `evolution.epRequirement` | 1,500,000 (0 to no limit) | EP required to evolve into this race. The base Bloodfiend value is unused for normal starting race selection. |
| `evolution.bossRequirement` | 0 (0 to no limit) | Boss kills required to evolve into this race. Set to 0 to disable this requirement. |
| `evolution.bloodRequirement` | 5,500 (0 to no limit) | Total blood drained required to evolve into this race. Set to 0 to disable this requirement. |
| `evolution.mobTurnRequirement` | 50 (0 to no limit) | Total mobs or players turned into kindred required to evolve into this race. Set to 0 to disable this requirement. |
| `base_energy.minAura` | 700,000 (0 to no limit) | Minimum base aura for this race. |
| `base_energy.maxAura` | 950,000 (0 to no limit) | Maximum base aura for this race. |
| `base_energy.minMagicule` | 850,000 (0 to no limit) | Minimum base magicule for this race. |
| `base_energy.maxMagicule` | 1,200,000 (0 to no limit) | Maximum base magicule for this race. |
| `attributes.size` | 0.05 (-0.9 to 16) | Scale modifier for this race. 0 means normal size. |
| `attributes.maxHealth` | 700 (0 to no limit) | Max health bonus/value used by the race config. |
| `attributes.maxSpiritualHealth` | 5,000 (0 to no limit) | Max spiritual health bonus/value used by the race config. |
| `attributes.attack` | 6.5 (0 to no limit) | Attack damage bonus/value used by the race config. |
| `attributes.attackSpeed` | 0.42 (-1 to no limit) | Attack speed modifier used by the race config. |
| `attributes.knockbackResistance` | 0.28 (0 to 1) | Knockback resistance modifier used by the race config. |
| `attributes.movementSpeed` | 0.055 (-1 to no limit) | Movement speed modifier used by the race config. |
| `attributes.swimSpeed` | -0.15 (-1 to no limit) | Swim speed modifier. Negative values make Bloodfiends worse in water. |
| `blood.maxBlood` | 240 (1 to no limit) | Maximum stored blood for this race before generation penalties. |
| `blood.bloodRegenThreshold` | 80 (0 to no limit) | Blood amount required before passive blood regeneration can activate. |
| `evolution.epRequirement` | 3,500,000 (0 to no limit) | EP required to evolve into this race. The base Bloodfiend value is unused for normal starting race selection. |
| `evolution.bossRequirement` | 2 (0 to no limit) | Boss kills required to evolve into this race. Set to 0 to disable this requirement. |
| `evolution.bloodRequirement` | 15,000 (0 to no limit) | Total blood drained required to evolve into this race. Set to 0 to disable this requirement. |
| `evolution.mobTurnRequirement` | 120 (0 to no limit) | Total mobs or players turned into kindred required to evolve into this race. Set to 0 to disable this requirement. |
| `base_energy.minAura` | 1,800,000 (0 to no limit) | Minimum base aura for this race. |
| `base_energy.maxAura` | 2,400,000 (0 to no limit) | Maximum base aura for this race. |
| `base_energy.minMagicule` | 2,200,000 (0 to no limit) | Minimum base magicule for this race. |
| `base_energy.maxMagicule` | 3,000,000 (0 to no limit) | Maximum base magicule for this race. |
| `attributes.size` | 0.08 (-0.9 to 16) | Scale modifier for this race. 0 means normal size. |
| `attributes.maxHealth` | 1,100 (0 to no limit) | Max health bonus/value used by the race config. |
| `attributes.maxSpiritualHealth` | 10,000 (0 to no limit) | Max spiritual health bonus/value used by the race config. |
| `attributes.attack` | 9 (0 to no limit) | Attack damage bonus/value used by the race config. |
| `attributes.attackSpeed` | 0.65 (-1 to no limit) | Attack speed modifier used by the race config. |
| `attributes.knockbackResistance` | 0.4 (0 to 1) | Knockback resistance modifier used by the race config. |
| `attributes.movementSpeed` | 0.07 (-1 to no limit) | Movement speed modifier used by the race config. |
| `attributes.swimSpeed` | -0.05 (-1 to no limit) | Swim speed modifier. Negative values make Bloodfiends worse in water. |
| `blood.maxBlood` | 320 (1 to no limit) | Maximum stored blood for this race before generation penalties. |
| `blood.bloodRegenThreshold` | 110 (0 to no limit) | Blood amount required before passive blood regeneration can activate. |
