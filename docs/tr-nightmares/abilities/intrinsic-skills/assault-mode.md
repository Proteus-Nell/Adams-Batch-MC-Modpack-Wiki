# Assault Mode

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:assault_mode` |
| **Activation** | Press |

</div>

> Assault Mode is an native power to the Royals of the Demon Clan that allow them to thrive in combat, This ability releases their surpressed Demonic Power in order to slaughter their foes.

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Intrinsic skill of: [Royal Demon](../../races/royal-demon.md)

## Related

- **Effects:** [Assault Moded](../../effects/assault-moded.md), [Magic Interference](../../../tensura-reincarnated/effects/magic-interference.md)
- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `AssaultMode.epAcquirement` | 20,000 | EP obtainment cost. |
| `AssaultMode.applyCooldownTicks` | 1,200 | Cooldown (ticks) after activating burst. |
| `AssaultMode.effectDurationTicks` | 3,600 | Effect duration (ticks) when not mastered. |
| `AssaultMode.effectDurationMasteredTicks` | 7,200 | Effect duration (ticks) when mastered. |
| `AssaultMode.effectAmplifier` | 1 | Mob effect amplifier for burst state. |
| `AssaultMode.masteryPointEveryTicks` | 6 | Grant mastery every N ticks while active. |
| `Apotheosis.epAcquirement` | 20,000 | EP obtainment cost. |
| `Apotheosis.applyCooldownTicks` | 1,200 | Cooldown (ticks) after activating burst. |
| `Apotheosis.effectDurationTicks` | 3,600 | Effect duration (ticks) when not mastered. |
| `Apotheosis.effectDurationMasteredTicks` | 7,200 | Effect duration (ticks) when mastered. |
| `Apotheosis.effectAmplifier` | 1 | Mob effect amplifier for burst state. |
| `Apotheosis.masteryPointEveryTicks` | 6 | Grant mastery every N ticks while active. |
