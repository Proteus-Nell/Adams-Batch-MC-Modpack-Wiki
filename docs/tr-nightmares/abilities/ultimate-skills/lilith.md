# ｢ Lilith, Lord of Heresy ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:lilith` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 2,000,000 |
| **Max mastery** | 15,000 |
| **Activation** | Toggle, Press |

</div>

> An ultimate heresy authority that turns barrier points into a battlefield-shaping domain of reflection, restoration, and inverted defense.

## Modes

| # | Mode |
|---|---|
| 1 | Break Down Restoration |
| 2 | Dimensional Domination |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you take damage
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| barrier | barrier points | add |

## Obtaining

- Acquisition checks: [Elegy](../unique-skills/elegy.md), [｢ Lilith, Lord of Heresy ｣](lilith.md)
- In-game message: *Your Elegy has evolved into Lilith, Lord of Heresy.*

## Related

- **Related skills:** [Elegy](../unique-skills/elegy.md), [Spacetime Manipulation](../extra-skills/spacetime-manipulation.md), [Rebirth](../extra-skills/rebirth.md)
- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Lilith.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Lilith.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Lilith.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Lilith.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Lilith.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Lilith.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Lilith.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Lilith.mpAcquirement` | 2,000,000 | The Cost for the Ultimate Skill: Lilith. |
| `Lilith.worldOfHeresyCost` | 4,000 | Magicule cost for Dimensional Domination. |
| `Lilith.worldRadius` | 16 | Radius of Heretical World. |
| `Lilith.worldDurationTicks` | 3,600 | Duration of Heretical World in ticks. |
| `Lilith.barrierGenerationPerSecond` | 0.05 | Barrier points generated per second as a fraction of max health while Automatic Multi-Dimensional Barrier is active. 0.05 means 5% max HP per second. |
| `Lilith.enableUltimateEvolution` | true | Whether Lilith evolution is allowed. If false, Elegy cannot evolve into Lilith. |

## In-game messages

<details markdown><summary>Show 6 messages</summary>

- Recovery mode: HP
- Recovery mode: MP
- Recovered %1$s HP from barrier points.
- Restored %1$s MP from barrier points.
- Not enough barrier points.
- You are already at full health.

</details>
