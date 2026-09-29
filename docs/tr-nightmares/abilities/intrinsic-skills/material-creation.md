# Material Creation

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:material_creation` |
| **Modes** | 2 |
| **Cooldowns (s)** | 30 |
| **Activation** | Press |

</div>

> Daemon intrinsic — Understanding researches EMC-valued matter into transmutation knowledge; Transmutation opens the transmutation table. EMC values are prices only; maximum magicules are spent instead of player EMC.

## Modes

| # | Mode |
|---|---|
| 1 | Understanding |
| 2 | Transmutation |

## How it works

- Activated by pressing the skill key

## Related

- **Referenced by:** [Ultimate Arroganz](../ultimate-skills/ultimate-arroganz.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `MaterialCreation.epAcquirement` | 10,000 | EP obtainment cost (intrinsic skill parity). |
| `MaterialCreation.researchHitsToLearn` | 100 | Total research points needed on one item/block identity before it is learned (Understanding mode). |
| `MaterialCreation.destroyChance` | 0.15 | Chance to destroy the researched stack or block each pulse. |
| `MaterialCreation.understandingCooldownTicks` | 600 | Cooldown in Minecraft ticks after each Understanding pulse (skill UI uses seconds → stored value / 20). |
| `MaterialCreation.reachDistance` | 6 | Ray trace reach when main hand is empty. |
| `MaterialCreation.refundFraction` | 0.5 | Refund fraction when inserting daemon-bound stacks into the bench refund slot. |
| `MaterialCreation.softMagiculeThreshold` | 4,096 | EMC at or below this value spends current magicules only and is not daemon-bound. |
