# Scavenger

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Scavenger](../../../assets/icons/elitetensura/skill/scavenger.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `elitetensura:scavenger` |
| **Modes** | 1 |
| **Acquisition cost (MP)** | 500 |
| **Activation** | Toggle |

</div>

> A keen eye for treasure. Passively grants Luck II, improving loot from chests, mob drops, and mining. Mastery unlocks a toggle that upgrades the buff to Luck III.

## Modes

| # | Mode |
|---|---|
| 1 | Default |

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

## Related

- **Referenced by:** [Fortune's Eye](../unique-skills/fortunes-eye.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/ExtraSkillConfig.toml`](../../configs/config-tensura-elitetensura-extraskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `Scavenger.mpAcquirement` | 500 | Magicule cost to learn Scavenger. |
| `Scavenger.baseLuckAmplifier` | 1 | Luck amplifier for unmastered holders (0=Luck I, 1=Luck II, 2=Luck III). Default: 1 = Luck II. |
| `Scavenger.masteredLuckAmplifier` | 2 | Luck amplifier for mastered holders with toggle active (0=Luck I, 1=Luck II, 2=Luck III). Default: 2 = Luck III. |
| `Scavenger.enabled` | true |  |
| `Scavenger.epAcquirement` | 15,000 |  |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- Scavenger activated — Luck III is now active.
- Scavenger deactivated.

</details>

## Tags

`tensura:skills/extra_skills`, `tensura:skills/no_plundering`
