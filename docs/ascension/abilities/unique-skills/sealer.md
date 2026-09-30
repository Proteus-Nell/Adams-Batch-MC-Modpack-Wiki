# Sealer

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Sealer](../../../assets/icons/ascension/skill/sealer.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `ascension:sealer` |
| **Modes** | 3 |
| **Cooldowns (s)** | 20 mastered, 30 otherwise, 10 mastered, 20 otherwise |
| **Activation** | Toggle, Press |

</div>

> Toggle: +100 max spiritual HP. Modes: Seal (trap a non-player at least 1.5x weaker than you into a stone — 30s, 20s mastered), Suppress (bank 20% of your max EP into a stone for later — 30s, 20s mastered), Stored Strength (+0.2 attack damage per use, +0.3 mastered, capped at +20, lost on death — 20s, 10s mastered).

## Modes

| # | Mode |
|---|---|
| 1 | Seal |
| 2 | Suppress |
| 3 | Stored Strength |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| attr | 100 | add |
| dmg | bonus | add |

## Obtaining

- Listed in the `additionalUniqueSkills` config option (config/tensura/ascension-common.toml): Unique skills added to the reincarnation pool. Remove an entry to exclude that skill from random reincarnation rolls.

## Related

- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `sealer.enabled` | true | Enable Sealer. |
| `sealer.passiveSpiritHp` | 100 (0 to 100,000) | Max spiritual HP bonus while toggled. |
| `sealer.sealRange` | 16 (1 to 128) | Seal raycast range in blocks. |
| `sealer.sealEpThreshold` | 1.5 (1 to 100) | Caster-EP / target-EP ratio required to Seal (1.5 = 1.5x as strong). |
| `sealer.sealCooldownSecondsMastered` | 20 (0 to 3,600) | Seal cooldown, mastered (seconds). |
| `sealer.sealCooldownSeconds` | 30 (0 to 3,600) | Seal cooldown, unmastered (seconds). |
| `sealer.suppressFraction` | 0.1 (0 to 1) | Fraction of max aura AND max magicule each removed on Suppress (0.10 = 10% from each, total 20% of max EP). |
| `sealer.suppressCooldownSecondsMastered` | 20 (0 to 3,600) | Suppress cooldown, mastered (seconds). |
| `sealer.suppressCooldownSeconds` | 30 (0 to 3,600) | Suppress cooldown, unmastered (seconds). |
| `sealer.strengthPerStackMastered` | 0.2 (0 to 100) | Attack-damage added per Stored Strength activation, mastered. |
| `sealer.strengthPerStack` | 0.2 (0 to 100) | Attack-damage added per Stored Strength activation, unmastered. |
| `sealer.strengthCapMastered` | 40 (0 to 1,000) | Total attack-damage cap for Stored Strength, mastered. |
| `sealer.strengthCap` | 20 (0 to 1,000) | Total attack-damage cap for Stored Strength, unmastered. |
| `sealer.strengthCooldownSecondsMastered` | 10 (0 to 3,600) | Stored Strength cooldown, mastered (seconds). |
| `sealer.strengthCooldownSeconds` | 20 (0 to 3,600) | Stored Strength cooldown, unmastered (seconds). |

## In-game messages

<details markdown><summary>Show 5 messages</summary>

- You cannot seal another player.
- The target is too strong to be sealed.
- You have no EP to suppress.
- Stored Strength: +%s attack damage.
- Stored Strength is already at its cap (+%s).

</details>

## Tags

`tensura:skills/unique_skills`
