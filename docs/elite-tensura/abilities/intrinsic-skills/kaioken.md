# Kaioken

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Kaioken](../../../assets/icons/elitetensura/skill/kaioken.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `elitetensura:kaioken` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 0 |
| **Cooldowns (s)** | 60 |
| **Activation** | Press |

</div>

> A body-burning Saiyan battle-aura. Multiply your power far past its limit in a crimson blaze — the higher the multiplier, the fiercer the strain on your body. Stronger tiers unlock as your EP grows and the technique is mastered.

## Modes

| # | Mode |
|---|---|
| 1 | Kaioken |
| 2 | Kaioken x3 |
| 3 | Kaioken x10 |
| 4 | Kaioken x20 |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 × (var3 + 1) |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Related

- **Effects:** [Kaioken](../../effects/kaioken.md), [Fragility](../../../tensura-reincarnated/effects/fragility.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/IntrinsicSkillConfig.toml`](../../configs/config-tensura-elitetensura-intrinsicskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `Kaioken.transformationDuration` | 3,600 | Transformation duration in ticks (unmastered). |
| `Kaioken.transformationDurationMastered` | 7,200 | Transformation duration in ticks (mastered). |
| `Kaioken.cooldown` | 60 | Cooldown in SECONDS after activating Kaioken (ManasCore decrements 1 per 20 ticks). |
| `Kaioken.mode0EnergyMultiplier` | 1 | Energy-pool multiplier bonus for tier 0 / Kaioken x2 (ADD_MULTIPLIED_TOTAL: 1.0 = double the max magicule &amp; aura). |
| `Kaioken.mode1EnergyMultiplier` | 2 | Energy-pool multiplier bonus for tier 1 / Kaioken x3 (2.0 = triple). |
| `Kaioken.mode2EnergyMultiplier` | 9 | Energy-pool multiplier bonus for tier 2 / Kaioken x10 (9.0 = ten times). |
| `Kaioken.mode3EnergyMultiplier` | 19 | Energy-pool multiplier bonus for tier 3 / Kaioken x20 (19.0 = twenty times). |
| `Kaioken.mode1EP` | 100,000 | Live EP required to unlock Kaioken x3 (tier 1). |
| `Kaioken.mode2EP` | 1,000,000 | Live EP required to unlock Kaioken x10 (tier 2). |
| `Kaioken.mode3EP` | 10,000,000 | Live EP required to unlock Kaioken x20 (tier 3). Also requires the skill be mastered. |
| `Kaioken.attackBonusPerTier` | 8 | Flat attack-damage bonus per tier (multiplied by tier+1: x2 = +this, x20 = +4x this). |
| `Kaioken.armorBonusPerTier` | 5 | Flat armor bonus per tier (multiplied by tier+1). |
| `Kaioken.speedBonusPerTier` | 0.02 | Flat movement-speed bonus per tier (multiplied by tier+1). |
| `Kaioken.healthDrainPerTick` | 1 | Health drained each drain-interval per tier (the body-strain of Kaioken). Floored by minHealthFraction so drain alone won't kill. |
| `Kaioken.energyDrainPerTick` | 50 | Magicule and aura drained each drain-interval per tier. |
| `Kaioken.drainIntervalTicks` | 20 | Interval in ticks between strain drains and red-aura particle emission. |
| `Kaioken.minHealthFraction` | 0.1 | Minimum health fraction (0-1) that Kaioken strain will not drain below. |
| `Kaioken.exhaustionDurationTicks` | 12,000 | Duration in ticks of the exhaustion debuff (Weakness + Fragility + Paralysis) applied when Kaioken ends. Kaioken cannot be re-ignited until it clears. Default 12000 = 10 minutes (Tensura's transformation default). |
| `Kaioken.activationMagiculeCostPerTier` | 0 | Magicule threshold per tier required to enter a Kaioken tier (multiplied by tier+1). 0 = no entry cost; the drain is the real cost. |

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

- Your body is still wracked from Kaioken — you can't ignite it again yet.

</details>

## Tags

`tensura:skills/intrinsic_skills`
