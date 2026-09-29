# Choas Strikes

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Choas Strikes](../../../assets/icons/trnightmare/skill/chaos_strikes.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:chaos_strikes` |
| **Activation** | Toggle |

</div>

> Your attacks are chaotic infused

## How it works

- Can be toggled on and off
- Triggers when you damage a target

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `ChaosStrikes.epAcquirement` | 5,000 | EP obtainment cost. |
| `ChaosStrikes.maxScaledDamage` | 500 | Max extra damage from EP scaling. |
| `ChaosStrikes.scalingReferenceEp` | 5,000,000 | Target EP reference for scaling. |
| `ChaosStrikes.hitsPerCycle` | 3 | Hits per toggle cycle. |
| `ChaosStrikes.procMagiculeMin` | 5,000 | Minimum magicule spent per proc. |
| `ChaosStrikes.procMagiculeFromBaseDivisor` | 100 | Magicule cost divisor from base magicule. |
| `ChaosStrikes.procMagiculeMax` | 1,000,000 | Maximum magicule spent per proc. |
