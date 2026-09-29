# Hyperbolic Passage

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Hyperbolic Passage](../../../assets/icons/ascension/skill/hyperbolic_passage.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `ascension:hyperbolic_passage` |
| **Activation** | Press |

</div>

> Active: open a white Hyperbolic Portal leading to the Hyperbolic Chamber. Costs 10%% current MP. CD 30s (10s mastered). Auto-learned once Gate AND Sacred Haki are both mastered.

## How it works

- Activated by pressing the skill key

## Related

- **Summons / entities:** Hyperbolic Portal

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `hyperbolic_passage.enabled` | true | Enable Hyperbolic Passage (and block its auto-unlock when false). |
| `hyperbolic_passage.magiculeFraction` | 0.1 (0 to 1) | Fraction of CURRENT magicule consumed per cast (0.10 = 10%). |
| `hyperbolic_passage.masteryPerCast` | 5 (0 to 500) | Mastery points awarded per successful cast.<br>EXTRA-tier mastery cap is 500, so 5/cast = 100 casts to master.<br>Set to 1 for the slow Tensura default; higher = faster mastery. |
| `hyperbolic_passage.cooldownSecondsMastered` | 10 (0 to 3,600) | Cooldown (seconds), mastered. |
| `hyperbolic_passage.cooldownSeconds` | 30 (0 to 3,600) | Cooldown (seconds), unmastered. |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- Not enough magicule.
- No room to open the portal.

</details>
