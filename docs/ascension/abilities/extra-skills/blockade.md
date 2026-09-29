# Blockade

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Blockade](../../../assets/icons/ascension/skill/blockade.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `ascension:blockade` |
| **Cooldowns (s)** | 30 |
| **Activation** | Press |

</div>

> Active: apply Regeneration Suppression to the target you're looking at (≤ 16 blocks) for 10s (20s mastered), force-disabling Self / Ultraspeed / Infinite Regeneration. CD 30s. Auto-learned when Magic Jamming is mastered and you've slain 30 Vexes.

## How it works

- Activated by pressing the skill key

## Related

- **Effects:** [Regeneration Suppression](../../effects/regen-suppression.md)

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `blockade.enabled` | true | Enable Blockade. |
| `blockade.durationSecondsMastered` | 20 (1 to 600) | Regen Suppression duration applied to the target, mastered (seconds). |
| `blockade.durationSeconds` | 10 (1 to 600) | Regen Suppression duration applied to the target, unmastered (seconds). |
| `blockade.cooldownSeconds` | 30 (0 to 3,600) | Blockade cooldown (seconds). |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- No target in front of you.

</details>
