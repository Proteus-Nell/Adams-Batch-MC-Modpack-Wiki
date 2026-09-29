# Black Flame Thunder

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Black Flame Thunder](../../../assets/icons/trnightmare/skill/black_flame_thunder.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:black_flame_thunder` |
| **Max mastery** | 5,000 |
| **Activation** | Toggle |

</div>

> Black Flame Thunder is the fused skill of Black Flame's Coating applied with the properties of Black Lightning to produce a greater Offensive Threat.

## How it works

- Can be toggled on and off
- Triggers when you damage a target
- Triggers on melee contact
- Does something when first learned

## Obtaining

- Acquisition checks: [Demon Slime](../../../tensura-reincarnated/races/demon-slime.md), [God Slime](../../../tensura-reincarnated/races/god-slime.md), [Black Flame](../../../tensura-reincarnated/abilities/extra-skills/black-flame.md), [Black Lightning](../../../tensura-reincarnated/abilities/extra-skills/black-lightning.md)

## Related

- **Related skills:** [Black Flame](../../../tensura-reincarnated/abilities/extra-skills/black-flame.md), [Black Lightning](../../../tensura-reincarnated/abilities/extra-skills/black-lightning.md)
- **Effects:** [Black Burn](../../../tensura-reincarnated/effects/black-burn.md), [Blackpara](../../effects/blackpara.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `BlackFlameThunder.epAcquirement` | 500 | EP obtainment cost. |
| `BlackFlameThunder.learningCost` | 500 | Learning cost. |
| `BlackFlameThunder.maxMastery` | 5,000 | Max mastery. |
| `BlackFlameThunder.physicalHitMultiplier` | 1.5 | Physical hit damage multiplier while toggled (non-fire). |
| `BlackFlameThunder.igniteTicks` | 60 | Fire ticks applied on physical proc. |
| `BlackFlameThunder.elementalBoostMultiplier` | 10 | Multiplier for fire/lightning/light while flame+thunder. |
| `BlackFlameThunder.touchOnHitMagiculeCost` | 5 | Magicule cost per on-touch proc. |
| `BlackFlameThunder.blackBurnDurationTicks` | 200 | Black burn duration (ticks). |
| `BlackFlameThunder.blackBurnLevelNormal` | 1 | Black burn amplifier when not mastered. |
| `BlackFlameThunder.blackBurnLevelMastered` | 2 | Black burn amplifier when mastered. |
