# Giant Dance

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Giant Dance](../../../assets/icons/trnightmare/skill/giant_dance.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:giant_dance` |
| **Activation** | Press |

</div>

> An intrinsic giant-line skill that increases rhythm-based mobility and combat flow.

## How it works

- Activated by pressing the skill key

## Related

- **Effects:** [Giant Dance](../../effects/giant-dance.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `GiantDance.magiculeCost` | 5,000 | Magicule cost to transform. |
| `GiantDance.effectDurationTicks` | 3,600 | Giant Dance effect duration (ticks) when not mastered. |
| `GiantDance.effectDurationMasteredTicks` | 7,200 | Giant Dance effect duration (ticks) when mastered. |
| `GiantDance.removeEarlyCooldownTicks` | 600 | Cooldown (ticks) after removing the transformation early. |
| `GiantDance.applyCooldownTicks` | 780 | Cooldown (ticks) after applying transformation. |
| `GiantDance.applyCooldownMasteredTicks` | 960 | Cooldown (ticks) after applying transformation when mastered. |
| `GiantDance.effectLevel` | 0 | Mob effect amplifier for Giant Dance (usually 0). |
