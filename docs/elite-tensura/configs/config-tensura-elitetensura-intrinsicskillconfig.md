# `config/tensura/EliteTensura/IntrinsicSkillConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Kaioken]`

| Option | Default | Range | Description |
|---|---|---|---|
| `transformationDuration` | 3,600 |  | Transformation duration in ticks (unmastered). |
| `transformationDurationMastered` | 7,200 |  | Transformation duration in ticks (mastered). |
| `cooldown` | 60 |  | Cooldown in SECONDS after activating Kaioken (ManasCore decrements 1 per 20 ticks). |
| `mode0EnergyMultiplier` | 1 |  | Energy-pool multiplier bonus for tier 0 / Kaioken x2 (ADD_MULTIPLIED_TOTAL: 1.0 = double the max magicule &amp; aura). |
| `mode1EnergyMultiplier` | 2 |  | Energy-pool multiplier bonus for tier 1 / Kaioken x3 (2.0 = triple). |
| `mode2EnergyMultiplier` | 9 |  | Energy-pool multiplier bonus for tier 2 / Kaioken x10 (9.0 = ten times). |
| `mode3EnergyMultiplier` | 19 |  | Energy-pool multiplier bonus for tier 3 / Kaioken x20 (19.0 = twenty times). |
| `mode1EP` | 100,000 |  | Live EP required to unlock Kaioken x3 (tier 1). |
| `mode2EP` | 1,000,000 |  | Live EP required to unlock Kaioken x10 (tier 2). |
| `mode3EP` | 10,000,000 |  | Live EP required to unlock Kaioken x20 (tier 3). Also requires the skill be mastered. |
| `attackBonusPerTier` | 8 |  | Flat attack-damage bonus per tier (multiplied by tier+1: x2 = +this, x20 = +4x this). |
| `armorBonusPerTier` | 5 |  | Flat armor bonus per tier (multiplied by tier+1). |
| `speedBonusPerTier` | 0.02 |  | Flat movement-speed bonus per tier (multiplied by tier+1). |
| `healthDrainPerTick` | 1 |  | Health drained each drain-interval per tier (the body-strain of Kaioken). Floored by minHealthFraction so drain alone won't kill. |
| `energyDrainPerTick` | 50 |  | Magicule and aura drained each drain-interval per tier. |
| `drainIntervalTicks` | 20 |  | Interval in ticks between strain drains and red-aura particle emission. |
| `minHealthFraction` | 0.1 |  | Minimum health fraction (0-1) that Kaioken strain will not drain below. |
| `exhaustionDurationTicks` | 12,000 |  | Duration in ticks of the exhaustion debuff (Weakness + Fragility + Paralysis) applied when Kaioken ends. Kaioken cannot be re-ignited until it clears. Default 12000 = 10 minutes (Tensura's transformation default). |
| `activationMagiculeCostPerTier` | 0 |  | Magicule threshold per tier required to enter a Kaioken tier (multiplied by tier+1). 0 = no entry cost; the drain is the real cost. |
