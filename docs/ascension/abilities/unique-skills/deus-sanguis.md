# Deus Sanguis

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Deus Sanguis](../../../assets/icons/ascension/skill/deus_sanguis.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `ascension:deus_sanguis` |
| **Modes** | 3 |
| **Cooldowns (s)** | 3 |
| **Activation** | Press, Hold |

</div>

> Toggle: at night, gain Strength III, Speed II, Haste II. Toggle: melee hits inflict Bleeding 6 for 4s (Bleeding 10 mastered). Modes: Bite (Paralysis IV / Blindness IV / Darkness IV + 20 blood damage on the target you're looking at, 25 mastered, 3s CD), Shift (toggle to half-size with 50% max HP and creative flight, 20s/10s CD), Health Drain (held: drain 10% / 20% of nearby enemies' current HP per second as blood damage in 6 blocks, 30s/10s CD).

## Modes

| # | Mode |
|---|---|
| 1 | Bite |
| 2 | Shift |
| 3 | Health Drain |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers on melee contact

## Obtaining

- Listed in the `additionalUniqueSkills` config option (config/tensura/ascension-common.toml): Unique skills added to the reincarnation pool. Remove an entry to exclude that skill from random reincarnation rolls.

## Related

- **Effects:** [Bleeding](../../effects/bleeding.md), [Paralysis](../../../tensura-reincarnated/effects/paralysis.md)

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `deus_sanguis.enabled` | true | Enable Deus Sanguis. |
| `deus_sanguis.bleedTierMastered` | 10 (1 to 32) | Bleed tier when mastered. |
| `deus_sanguis.bleedTier` | 6 (1 to 32) | Bleed-on-melee tier applied while toggled, unmastered (1 = amplifier 0). |
| `deus_sanguis.bleedDurationSeconds` | 4 (1 to 60) | Bleed duration on melee hit (seconds). |
| `deus_sanguis.biteDamageMastered` | 25 (0 to 1,000) | Bite damage (HP), mastered. |
| `deus_sanguis.biteDamage` | 20 (0 to 1,000) | Bite damage (HP), unmastered. |
| `deus_sanguis.biteCooldownSeconds` | 3 (0 to 3,600) | Bite cooldown (seconds). |
| `deus_sanguis.shiftCooldownSecondsMastered` | 10 (0 to 3,600) | Shift cooldown (seconds), mastered. |
| `deus_sanguis.shiftCooldownSeconds` | 20 (0 to 3,600) | Shift cooldown (seconds), unmastered. Press cycles in OR out and consumes the cooldown either way. |
| `deus_sanguis.drainCooldownSecondsMastered` | 10 (0 to 3,600) | Health Drain cooldown (seconds), mastered. |
| `deus_sanguis.drainCooldownSeconds` | 30 (0 to 3,600) | Health Drain cooldown (seconds), unmastered. Set on press so a tap still consumes the full cooldown. |
| `deus_sanguis.drainFractionMastered` | 0.2 (0 to 1) | Health Drain fraction per second, mastered. |
| `deus_sanguis.drainFraction` | 0.1 (0 to 1) | Health Drain: fraction of each enemy's CURRENT HP drained per second, unmastered (0.10 = 10%). |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- No target in front of you.

</details>
