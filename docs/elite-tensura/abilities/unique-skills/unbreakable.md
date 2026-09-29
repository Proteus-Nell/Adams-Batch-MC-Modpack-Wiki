# Unbreakable

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Unbreakable](../../../assets/icons/elitetensura/skill/unbreakable.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `elitetensura:unbreakable` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 1,000 |
| **Cooldowns (s)** | 720 or 360 |
| **Activation** | Press |

</div>

> Iron Resolve tempered into something unbreakable. Vein Sense, a 50% Iron Aegis, Strength IV Surge — and Undying Will cheats death itself once every cooldown.

## Modes

| # | Mode |
|---|---|
| 1 | Vein Sense |
| 2 | Iron Aegis |
| 3 | Resolute Surge |
| 4 | Undying Will |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 2,000 or 0 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you take damage
- Does something when first learned

## Related

- **Related skills:** [Iron Resolve](../extra-skills/iron-resolve.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UniqueSkillConfig.toml`](../../configs/config-tensura-elitetensura-uniqueskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `Unbreakable.enabled` | true | Master enable. When false the skill can never be acquired. |
| `Unbreakable.epAcquirement` | 150,000 | Max EP required to evolve Iron Resolve into Unbreakable. |
| `Unbreakable.bossKillsRequired` | 8 | Total boss kills required (Tensura bossesCounter bosses + world calamities). |
| `Unbreakable.hasteAmplifier` | 9 | Vein Sense Haste amplifier (9 = Haste 10, 0-indexed). |
| `Unbreakable.aegisMaxReduction` | 50 | Iron Aegis: maximum incoming-damage reduction percent at full magicule (Iron Resolve caps at 40). |
| `Unbreakable.surgeMagiculeCost` | 2,000 | Resolute Surge magicule cost per activation. |
| `Unbreakable.surgeStrengthAmplifier` | 3 | Resolute Surge Strength amplifier (3 = Strength IV, 0-indexed). |
| `Unbreakable.surgeDurationTicks` | 6,000 | Resolute Surge duration in ticks. |
| `Unbreakable.surgeDurationMasteredTicks` | 12,000 | Resolute Surge duration in ticks when mastered. |
| `Unbreakable.surgeCooldownSeconds` | 360 | Resolute Surge cooldown in SECONDS. |
| `Unbreakable.surgeCooldownMasteredSeconds` | 720 | Resolute Surge cooldown in SECONDS when mastered. Deliberately longer: duration doubles too (6000→12000t), holding uptime at ~83% — mastery buys fewer activations, not more uptime. |
| `Unbreakable.undyingSurviveHealthPct` | 10 | Undying Will: percent of max health restored when a fatal hit is cheated (0-100). |
| `Unbreakable.undyingImmunityTicks` | 60 | Undying Will: full-immunity duration in ticks after triggering (Resistance V). |
| `Unbreakable.undyingCooldownSeconds` | 600 | Undying Will internal cooldown in SECONDS. |
| `Unbreakable.undyingCooldownMasteredSeconds` | 360 | Undying Will internal cooldown in SECONDS when mastered. |

## In-game messages

<details markdown><summary>Show 4 messages</summary>

- Undying Will armed — a fatal blow will not end you.
- Undying Will disarmed.
- UNDYING WILL — death refused!
- %1$s has worn off.

</details>

## Tags

`tensura:skills/no_plundering`, `tensura:skills/unique_skills`
