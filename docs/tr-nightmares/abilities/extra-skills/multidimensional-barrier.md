# Multidimensional Barrier

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:multidimensional_barrier` |
| **Cooldowns (s)** | 10 |
| **Activation** | Press |

</div>

> Create a layered barrier that unites the properties of the Multilayer Barrier Skill and Fault Field.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 250 |  |

## How it works

- Activated by pressing the skill key
- Triggers when you take damage

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| barrier | amount | add |

## Related

- **Referenced by:** [｢ Nodens, God of Abyss ｣](../ultimate-skills/nodens.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `MultidimensionalBarrier.mpAcquirement` | 2,500 | Magicule Acquirement Cost. |
| `MultidimensionalBarrier.mpCost` | 250 | Magicule cost per activation. |
| `MultidimensionalBarrier.pointMultiplier` | 1.5 | Barrier points multiplier based on the user's max health. |
| `MultidimensionalBarrier.allyPointMultiplier` | 0.75 | Barrier points multiplier for ally targets based on their max health. |
| `MultidimensionalBarrier.cooldown` | 10 | Cooldown in seconds before the barrier can be reactivated. |
| `MultidimensionalBarrier.barrierEPThreshold` | 0.5 | Legacy barrier strength threshold used for the multilayer barrier base value. |
| `MultidimensionalBarrier.barrierNormal` | 1 | Legacy barrier strength multiplier while the skill is not mastered. |
| `MultidimensionalBarrier.barrierMastered` | 1.5 | Legacy barrier strength multiplier while the skill is mastered. |
