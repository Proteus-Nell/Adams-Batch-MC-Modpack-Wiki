# Conceptual Existence

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:conceptual_existence` |
| **Modes** | 2 |
| **Activation** | Press, Hold |

</div>

> A Body Double-line intrinsic that borrows weaker bodies, binds itself to player hosts, studies their skills, and channels energy into them.

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Mode 2 |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Obtaining

- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `ConceptualExistence.unityRange` | 12 | Targeting range for Unity possession on non-player bodies. |
| `ConceptualExistence.hostRange` | 32 | Targeting range for binding to a player host. |
| `ConceptualExistence.unityResistanceMultiplier` | 0.5 | Resistance multiplier passed to Tensura possession checks for Unity. |
| `ConceptualExistence.unityHpMultiplier` | 0.35 | Health multiplier passed to Tensura possession checks for Unity. |
| `ConceptualExistence.unityShpMultiplier` | 0.35 | Spiritual-health multiplier passed to Tensura possession checks for Unity. |
| `ConceptualExistence.unityEpMultiplier` | 0.5 | EP multiplier passed to Tensura possession checks for Unity. |
| `ConceptualExistence.unityMaxAttack` | 5,000 | Maximum attack copied into a borrowed Unity body. |
| `ConceptualExistence.unityMaxHealth` | 5,000 | Maximum health copied into a borrowed Unity body. |
| `ConceptualExistence.unityMinMinutes` | 5 | Minimum Unity possession duration in minutes before mastery. |
| `ConceptualExistence.unityMaxMinutes` | 20 | Maximum Unity possession duration in minutes before mastery. |
| `ConceptualExistence.unityMinMinutesMastered` | 10 | Minimum Unity possession duration in minutes after mastery. |
| `ConceptualExistence.unityMaxMinutesMastered` | 40 | Maximum Unity possession duration in minutes after mastery. |
| `ConceptualExistence.optimizeMinimumMagiculePerSecond` | 100 | Minimum magicule transferred per second while Optimize Energy is channeled. |
| `ConceptualExistence.optimizeMagiculePercentPerSecond` | 0.01 | Additional percent of the user's max magicule transferred per second while Optimize Energy is channeled. |

## In-game messages

<details markdown><summary>Show 25 messages</summary>

- Unity
- Host Management
- %s is now your host.
- You slip away from your host.
- That player is too far away to become your host.
- Conceptual Host Management
- You do not have a valid host.
- Rejoin %s with Host Management first.
- Use Host Management to reconnect with your host.
- Unity only works on non-player mobs with lower EP than you.
- That target is too far away for Unity.
- Target a weaker mob for Unity or a player to make them your host.
- Select a valid unique or ultimate host skill.
- Boosting %s for %s.
- Boost target cleared.
- Merged with %s through %s.
- Merged host skill cleared.
- That host skill can no longer be studied.
- No mastery was earned from that study.
- Granted %s mastery to %s for %s.
- Optimize Energy armed. Hold Host Management to transfer MP.
- Optimize Energy disarmed.
- You need to be linked to an active host first.
- You have no magicules left to transfer.
- %s is already full on magicules.

</details>

## Tags

`tensura:skills/no_plundering`, `tensura:skills/tome_copy_excluded`
