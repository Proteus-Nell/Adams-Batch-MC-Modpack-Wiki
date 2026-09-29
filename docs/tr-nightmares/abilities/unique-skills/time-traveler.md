# Time Traveler

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:time_traveler` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 65,000 |
| **Max mastery** | 1,000 |
| **Cooldowns (s)** | 300, 600 |
| **Activation** | Press |

</div>

> Bend causality — auto-save your state, cheat death, and rewind the battlefield.

## Modes

| # | Mode |
|---|---|
| 1 | Time Leap |
| 2 | Further Fate |
| 3 | Reverse Fate |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you die

## Obtaining

- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.

## Related

- **Related skills:** [Usurper](../../../tensura-reincarnated/abilities/unique-skills/usurper.md), [Infinity Prison](../../../tensura-reincarnated/abilities/unique-skills/infinity-prison.md), [Absolute Severance](../../../tensura-reincarnated/abilities/unique-skills/absolute-severance.md)
- **Summons / entities:** [Hinata Sakaguchi](../../../tensura-reincarnated/mobs/hinata-sakaguchi.md), [Sentient Boss Masayuuki](../../mobs/sentient-boss-masayuuki.md)
- **Referenced by:** [Witch's Greed](witches-greed.md), [｢ Yog-Sothoth, Lord of Space-Time ｣](../ultimate-skills/yog-sothoth.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `timeTraveler.epAcquirement` | 65,000 | EP / magicule obtainment cost. |
| `timeTraveler.learningCost` | 1,500 | Learning / mastery point cost. |
| `timeTraveler.maxMastery` | 1,000 | Max mastery. |
| `timeTraveler.timeLeapCooldownSeconds` | 600 | Time Leap: cooldown between automatic saves (Tensura seconds). |
| `timeTraveler.deathHealHpFraction` | 0.1 | Time Leap: fraction of max HP restored on death rewind. |
| `timeTraveler.reverseFateLearnPoints` | 500 | Reverse Fate: learn points required. |
| `timeTraveler.reverseFateRadius` | 60 | Reverse Fate: snapshot radius in blocks. |
| `timeTraveler.reverseFateCooldownSeconds` | 300 | Reverse Fate: cooldown after rewind (Tensura seconds). |

## In-game messages

<details markdown><summary>Show 9 messages</summary>

- Time Leap
- Further Fate
- Reverse Fate
- Time Leap — returned to your last save.
- Reverse Fate anchored %s entities.
- Reverse Fate rewound %s entities.
- Reverse Fate requires mastery.
- Reverse Fate must be learned first.
- Further Fate granted %s

</details>

## Tags

`tensura:skills/no_plundering`
