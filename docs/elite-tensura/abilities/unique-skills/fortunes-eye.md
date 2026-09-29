# Fortune's Eye

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Fortune's Eye](../../../assets/icons/elitetensura/skill/fortunes_eye.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `elitetensura:fortunes_eye` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 1,000 |
| **Cooldowns (s)** | 30 or 60 |
| **Activation** | Press |

</div>

> A scavenger's instinct honed into true sight. Permanent Luck III (Luck IV mastered), and Loot Sense reveals every dropped item nearby with a golden outline.

## Modes

| # | Mode |
|---|---|
| 1 | Fortune |
| 2 | Loot Sense |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 or 0 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Does something when first learned

## Related

- **Related skills:** [Scavenger](../extra-skills/scavenger.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UniqueSkillConfig.toml`](../../configs/config-tensura-elitetensura-uniqueskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `FortunesEye.enabled` | true | Master enable. When false the skill can never be acquired. |
| `FortunesEye.epAcquirement` | 100,000 | Max EP required to evolve Scavenger into Fortune's Eye. |
| `FortunesEye.bossKillsRequired` | 5 | Total boss kills required (Tensura bossesCounter bosses + world calamities). |
| `FortunesEye.baseLuckAmplifier` | 2 | Passive Luck amplifier (2 = Luck III, 0-indexed). Scavenger's passive is Luck II. |
| `FortunesEye.masteredLuckAmplifier` | 3 | Passive Luck amplifier when mastered (3 = Luck IV). |
| `FortunesEye.senseRadius` | 24 | Loot Sense: radius in blocks that dropped items are revealed in. |
| `FortunesEye.senseRadiusMastered` | 40 | Loot Sense radius when mastered. |
| `FortunesEye.senseDurationTicks` | 200 | Loot Sense: how long revealed items glow, in ticks. |
| `FortunesEye.senseCooldownSeconds` | 60 | Loot Sense cooldown in SECONDS. |
| `FortunesEye.senseCooldownMasteredSeconds` | 30 | Loot Sense cooldown in SECONDS when mastered. |
| `FortunesEye.senseMagiculeCost` | 100 | Loot Sense magicule cost per press. |

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

<details markdown><summary>Show 1 messages</summary>

- Loot Sense — %1$s item(s) revealed.

</details>

## Tags

`tensura:skills/no_plundering`, `tensura:skills/unique_skills`
