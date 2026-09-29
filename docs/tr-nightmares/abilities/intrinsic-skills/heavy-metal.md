# Heavy METAL!

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Heavy METAL!](../../../assets/icons/trnightmare/skill/heavy_metal.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:heavy_metal` |
| **Activation** | Press |

</div>

> An intrinsic skill that hardens the body and massively increases physical durability.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5,000 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Intrinsic skill of: [Lesser Giant](../../races/lesser-giant.md)

## Related

- **Effects:** [Metal Mode](../../effects/metal-mode.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `HeavyMetal.magiculeCost` | 5,000 | Magicule cost to transform. |
| `HeavyMetal.effectDurationTicks` | 3,600 | Heavy Metal effect duration (ticks) when not mastered. |
| `HeavyMetal.effectDurationMasteredTicks` | 7,200 | Heavy Metal effect duration (ticks) when mastered. |
| `HeavyMetal.removeEarlyCooldownTicks` | 600 | Cooldown (ticks) after removing the transformation early. |
| `HeavyMetal.applyCooldownTicks` | 780 | Cooldown (ticks) after applying transformation. |
| `HeavyMetal.applyCooldownMasteredTicks` | 960 | Cooldown (ticks) after applying transformation when mastered. |
| `HeavyMetal.effectLevel` | 0 | Heavy Metal mob effect amplifier. |
| `HeavyMetal.resistanceLevelNormal` | 0 | Resistance amplifier when not mastered (0 = I). |
| `HeavyMetal.resistanceLevelMastered` | 2 | Resistance amplifier when mastered. |
