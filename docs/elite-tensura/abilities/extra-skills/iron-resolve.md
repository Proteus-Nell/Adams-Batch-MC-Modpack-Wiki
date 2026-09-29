# Iron Resolve

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Iron Resolve](../../../assets/icons/elitetensura/skill/iron_resolve.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `elitetensura:iron_resolve` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 10,000 |
| **Cooldowns (s)** | 720 or 360 |
| **Activation** | Press |

</div>

> A unique skill born from an unbreakable will to endure. The holder bends hardship into strength, refusing to be undone by the world around them.

## Modes

| # | Mode |
|---|---|
| 1 | Vein Sense |
| 2 | Iron Aegis |
| 3 | Resolute Surge |
| 4 | Last Stand |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 2,000 or 0 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage

## Related

- **Referenced by:** [Unbreakable](../unique-skills/unbreakable.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/ExtraSkillConfig.toml`](../../configs/config-tensura-elitetensura-extraskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `Iron_Resolve.mpAcquirement` | 10,000 |  |
| `Iron_Resolve.hasteAmplifier` | 9 |  |
| `Iron_Resolve.aegisMaxReduction` | 40 |  |
| `Iron_Resolve.surgeMagiculeCost` | 2,000 |  |
| `Iron_Resolve.surgeStrengthAmplifier` | 2 |  |
| `Iron_Resolve.surgeDurationTicks` | 6,000 |  |
| `Iron_Resolve.surgeDurationMasteredTicks` | 12,000 |  |
| `Iron_Resolve.surgeCooldownSeconds` | 360 | Cooldown after using Resolute Surge, in SECONDS. Default 360 = 6 minutes. |
| `Iron_Resolve.surgeCooldownMasteredSeconds` | 720 | Cooldown after using Resolute Surge when mastered, in SECONDS. Default 720 = 12 minutes. |
| `Iron_Resolve.lastStandThresholdPct` | 40 |  |
| `Iron_Resolve.lastStandImmunityTicks` | 60 | Duration of the Last Stand immunity window, in TICKS. Default 60 = 3 seconds. |
| `Iron_Resolve.lastStandResistanceAmplifier` | 4 |  |
| `Iron_Resolve.lastStandInternalCooldownTicks` | 300 | Internal cooldown before Last Stand can re-fire, in TICKS. Default 300 = 15 seconds. |
| `Iron_Resolve.enabled` | true |  |
| `Iron_Resolve.epAcquirement` | 20,000 |  |

## In-game messages

<details markdown><summary>Show 7 messages</summary>

- Last Stand is now active.
- Last Stand has been disabled.
- Last Stand has activated — resolve holds.
- %s has expired.
- Vein Sense
- Iron Aegis
- Resolute Surge

</details>

## Tags

`tensura:skills/extra_skills`, `tensura:skills/no_plundering`
