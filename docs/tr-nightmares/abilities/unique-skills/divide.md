# Divide

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:divide` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 150,000 |
| **Max mastery** | 1,000 |
| **Activation** | Toggle, Press |

</div>

> These claws can sever anything  space, matter, or even concepts  leaving nothing behind.

## Modes

| # | Mode |
|---|---|
| 1 | Dragon Claw |
| 2 | Dragon's Claw |
| 3 | Cut Through |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| attack | bonus | add |
| degrade | 1 | add |

## Related

- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `divide.mpAcquirement` | 150,000 |  |
| `divide.maxMastery` | 1,000 |  |
| `divide.dragonClawCooldownSeconds` | 1 |  |
| `divide.dragonClawReachBonus` | 7 |  |
| `divide.dragonClawSlashWidth` | 8 |  |
