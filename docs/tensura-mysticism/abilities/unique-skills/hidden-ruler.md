# Hidden Ruler

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Hidden Ruler](../../../assets/icons/mysticism/skill/hidden_ruler.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:hidden_ruler` |
| **Modes** | 4 |
| **Cooldowns (s)** | 10, 5 |
| **Activation** | Toggle, Press |

</div>

> Inspire your allies. Conscript allies in the dark. Copy abilities from your foes and Paste them onto allies.

## Modes

| # | Mode |
|---|---|
| 1 | Copy |
| 2 | Paste |
| 3 | Clear Bank |
| 4 | Darkness Conscription |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Copy | 1,000 |  |
| Paste | 1,000 |  |
| other modes | 1,000 |  |
| Darkness Conscription | 1,000 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you die

## Related

- **Effects:** [Presence Concealment](../../../tensura-reincarnated/effects/presence-concealment.md), [Presence Sense](../../../tensura-reincarnated/effects/presence-sense.md), [Inspiration](../../../tensura-reincarnated/effects/inspiration.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `HiddenRuler.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `HiddenRuler.vanishMagiculeCost` | 50 | The Magicule cost of Hidden Ruler's toggled passive. |
| `HiddenRuler.vanishAuraCost` | 0 | The Aura cost of Hidden Ruler's toggled passive. |
| `HiddenRuler.inspireRadius` | 15 | The radius in blocks of the Inspiration effect provided by Hidden Ruler to nearby allies. |
| `HiddenRuler.noTargetCooldown` | 5 | The cooldown that is applied if there is no target for either Copy or Paste. |
| `HiddenRuler.copyCost` | 1,000 | The FLAT cost of the Copy mode when attempting to copy a skill from the target. |
| `HiddenRuler.copyCooldown` | 10 | The cooldown of the Copy mode. |
| `HiddenRuler.copyCooldownMastered` | 10 | The cooldown of the Copy mode when the skill is mastered. |
| `HiddenRuler.copyChance` | 25 | The chance for the Copy mode to pass. |
| `HiddenRuler.copyChanceMastered` | 50 | The chance for the Copy mode to pass when the skill is mastered. |
| `HiddenRuler.copyFailedCooldown` | 10 | The cooldown of the Copy mode when a failure is encountered. |
| `HiddenRuler.failureThreshold` | 2 | The EP threshold that is checked when the user is weaker than the target when the Copy mode is used. |
| `HiddenRuler.failureThresholdMastered` | 2.5 | The EP threshold that is checked when the user is weaker than the target when the Copy mode is used and the skill is mastered. |
| `HiddenRuler.pasteCost` | 1,000 | The FLAT cost of the Paste mode when attempting to paste a skill onto the target. |
| `HiddenRuler.pasteCooldown` | 10 | The cooldown of the Paste mode. |
| `HiddenRuler.pasteCooldownMastered` | 10 | The cooldown of the Paste mode when the skill is mastered. |
| `HiddenRuler.pasteChance` | 25 | The chance for the Paste mode to pass. |
| `HiddenRuler.pasteChanceMastered` | 50 | The chance for the Paste mode to pass when the skill is mastered. |
| `HiddenRuler.pasteFailedCooldown` | 10 | The cooldown of the Paste mode when a failure is encountered. |
| `HiddenRuler.darknessConscriptionCost` | 1,000 | How many magicules should be taken from the user when attempting to Charm a target?. |
| `HiddenRuler.lightLevel` | 5 | The light level that both the target AND user MUST be under to successfully charm the target with Darkness Conscription. |
| `HiddenRuler.darknessConscriptionCooldown` | 10 | The cooldown of the Darkness Conscription mode. |
| `HiddenRuler.darknessConscriptionCooldownMastery` | 10 | The cooldown of the Darkness Conscription mode when the skill is mastered. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- You died! Your Hidden Ruler skill bank was wiped.

</details>

## Tags

`tensura:skills/unique_skills`
