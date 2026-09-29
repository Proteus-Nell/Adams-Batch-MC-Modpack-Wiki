# The One Who Seals

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![The One Who Seals](../../../assets/icons/ascension/skill/one_who_seals.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `ascension:one_who_seals` |
| **Modes** | 3 |
| **Max mastery** | 100 |
| **Cooldowns (s)** | 20 mastered, 30 otherwise, 60, 10 mastered, 60 otherwise |
| **Activation** | Press |

</div>

> Ultimate awakening of Sealer. Passive: every kill grants +0.5 Max Spiritual HP, capped at +20,000. Modes: Seal (capture mob into stone if 1.5x stronger), Suppress (seal 20% of self or sneak-target's Max EP into a stone), Enough is Enough (steal a random skill — excluding ultimates / magics / battlewills — into a redeemable stone). All produced stones land in your inventory.

## Modes

| # | Mode |
|---|---|
| 1 | Seal |
| 2 | Suppress |
| 3 | Enough is Enough |

## How it works

- Activated by pressing the skill key

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| shp | next | add |

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `one_who_seals.enabled` | true | Enable One Who Seals. |
| `sealer.sealRange` | 16 (1 to 128) | Seal raycast range in blocks. |
| `sealer.sealEpThreshold` | 1.5 (1 to 100) | Caster-EP / target-EP ratio required to Seal (1.5 = 1.5x as strong). |
| `one_who_seals.sealCooldownSecondsMastered` | 20 (0 to 3,600) | Seal cooldown, mastered (seconds). |
| `one_who_seals.sealCooldownSeconds` | 30 (0 to 3,600) | Seal cooldown, unmastered (seconds). |
| `one_who_seals.suppressFractionMastered` | 0.3 (0 to 1) | Fraction of Max EP suppressed into a stone, mastered (0.30 = 30%). |
| `one_who_seals.suppressFraction` | 0.2 (0 to 1) | Fraction of Max EP suppressed into a stone, unmastered (0.20 = 20%). |
| `one_who_seals.range` | 16 (1 to 128) | Targeting raycast range for Suppress (sneak-target) and Enough is Enough (blocks). |
| `one_who_seals.suppressCooldownSecondsMastered` | 60 (0 to 3,600) | Suppress cooldown, mastered (seconds). |
| `one_who_seals.suppressCooldownSeconds` | 60 (0 to 3,600) | Suppress cooldown, unmastered (seconds). |
| `one_who_seals.enoughEpRatio` | 2 (1 to 100) | Caster-EP / target-EP ratio required to seal an ordinary skill. |
| `one_who_seals.enoughEpRatioUnique` | 3 (1 to 100) | Caster-EP / target-EP ratio required to seal a UNIQUE-tier skill. |
| `one_who_seals.enoughCooldownSecondsMastered` | 10 (0 to 3,600) | Enough is Enough cooldown, mastered (seconds). |
| `one_who_seals.enoughCooldownSeconds` | 60 (0 to 3,600) | Enough is Enough cooldown, unmastered (seconds). |
| `one_who_seals.killBonusPerKill` | 0.5 (0 to 1,000) | Max Spiritual HP gained per kill (passive). |
| `one_who_seals.killBonusCap` | 20,000 (0 to 1,000,000) | Cap on the cumulative kill-bonus Max Spiritual HP. |

## In-game messages

<details markdown><summary>Show 5 messages</summary>

- Target has no stealable skills.
- You must be at least 2x the target's EP to seal a skill.
- You must be at least 3x the target's EP to seal their Unique.
- You stole %2$s from %1$s.
- %1$s sealed your %2$s.

</details>
