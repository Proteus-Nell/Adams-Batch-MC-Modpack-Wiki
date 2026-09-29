# Bubble Majin

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Bubble Majin](../../../assets/icons/ascension/skill/bubble_majin.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `ascension:bubble_majin` |
| **Modes** | 3 |
| **Cooldowns (s)** | 30, 10 mastered, 30 otherwise, 4 mastered, 8 otherwise |
| **Activation** | Press |

</div>

> Passive: +10% magicule regen. Toggle: reflect projectiles back at their source. Modes: Storage (pocket dimension, 81 stacks), Candy Beam (turn a non-player at least 1.5x weaker than you into edible candy that passes their EP and skills to whoever eats it), Regeneration (full HP for 5% max aura).

## Modes

| # | Mode |
|---|---|
| 1 | Storage |
| 2 | Candy Beam |
| 3 | Regeneration |

## How it works

- Activated by pressing the skill key
- Triggers when a projectile hits you

## Obtaining

- Listed in the `additionalUniqueSkills` config option (config/tensura/ascension-common.toml): Unique skills added to the reincarnation pool. Remove an entry to exclude that skill from random reincarnation rolls.

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `bubble_majin.enabled` | true | Enable Bubble Majin. |
| `bubble_majin.reflectSpeedMultiplier` | 1.5 (0 to 100) | Speed multiplier applied to reflected projectiles. |
| `bubble_majin.reflectDamageMultiplier` | 1.5 (0 to 100) | Damage multiplier applied to reflected Tensura projectiles. |
| `bubble_majin.candyBeamRange` | 30 (1 to 256) | Candy Beam targeting range in blocks. |
| `bubble_majin.candyAllowPlayers` | false | When true, Candy Beam can target other players (subject to the EP threshold). PvP servers only — leave false for co-op. |
| `bubble_majin.candyEpThreshold` | 2 (1 to 100) | Caster-EP / target-EP ratio required for Candy Beam to transmute (2.0 = 2x as strong). |
| `bubble_majin.candyCooldownSeconds` | 30 (0 to 3,600) | Candy Beam cooldown, unmastered (seconds). |
| `bubble_majin.candyEpRetained` | 0.1 (0 to 1) | Fraction of the target's EP stored in the resulting candy (0.10 = 10%). |
| `bubble_majin.candyCooldownSecondsMastered` | 10 (0 to 3,600) | Candy Beam cooldown, mastered (seconds). |
| `bubble_majin.regenAuraCost` | 0.05 (0 to 1) | Regeneration aura cost (fraction of max aura). |
| `bubble_majin.regenCooldownSecondsMastered` | 4 (0 to 3,600) | Regeneration cooldown, mastered (seconds). |
| `bubble_majin.regenCooldownSeconds` | 8 (0 to 3,600) | Regeneration cooldown, unmastered (seconds). |

## In-game messages

<details markdown><summary>Show 5 messages</summary>

- Candy Beam cannot be used on players.
- This target is too important to eat.
- The target is too strong to be turned into candy.
- You are already at full health.
- %1$s was absorbed by %2$s.

</details>

## Tags

`tensura:skills/unique_skills`
