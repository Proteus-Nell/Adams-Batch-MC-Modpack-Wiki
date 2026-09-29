# Cultist

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:cultist` |
| **Modes** | 3 |
| **Max mastery** | 1,000 |
| **Cooldowns (s)** | 5 |
| **Activation** | Toggle, Press |

</div>

> A devotional Unique Skill that turns pain, madness, and sacrifice into power for the greater good.

## Modes

| # | Mode |
|---|---|
| 1 | Joy In Service |
| 2 | Praise |
| 3 | Carnage |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Triggers when you damage a target
- Triggers when you take damage

## Related

- **Effects:** [Insanity](../../../tensura-reincarnated/effects/insanity.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `cultist.mpAcquirement` | 75,000 | MP cost to obtain Cultist. |
| `cultist.maxMastery` | 1,000 | Max mastery. |
| `cultist.joySpiritualDamageMultiplier` | 0.5 | Joy In Service: spiritual damage multiplier while in slot. |
| `cultist.joyKillSacrificePoints` | 1 | Joy In Service: sacrifice points gained for mob kills while insane. |
| `cultist.insanityToggleLevel` | 3 | Insanity toggle: Insanity level applied. |
| `cultist.greaterGoodEpFraction` | 0.15 | Greater Good: EP fraction gained from subordinates killed by outside sources when mastered. |
| `cultist.praiseHpCost` | 10 | Praise: HP damage to self. |
| `cultist.praiseShpCost` | 20 | Praise: SHP damage to self. |
| `cultist.praiseSacrificePoints` | 4 | Praise: sacrifice points generated. |
| `cultist.praiseCooldownSeconds` | 5 | Praise cooldown in seconds. |
| `cultist.carnageDamagePerPoint` | 2 | Carnage: spiritual damage dealt per sacrifice point. |
| `cultist.carnageDamageCap` | 100 | Carnage: maximum spiritual damage added per hit. |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- Sacrifice Points: %s
- The Greater Good claims %s EP.

</details>
