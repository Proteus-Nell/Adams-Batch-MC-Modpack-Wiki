# Hell Passage

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Hell Passage](../../../assets/icons/ascension/skill/hell_passage.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `ascension:hell_passage` |
| **Activation** | Press |

</div>

> Active: open a Hell Portal in front of you. Costs 10%% current MP. CD 30s (10s mastered). Auto-learned once Gate is mastered and 30 Daemon Essences are consumed from your inventory.

## How it works

- Activated by pressing the skill key

## Related

- **Summons / entities:** Hell Portal

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `hell_passage.enabled` | true | Enable Hell Passage (and block its auto-unlock when false). |
| `hell_passage.magiculeFraction` | 0.1 (0 to 1) | Fraction of CURRENT magicule consumed per cast (0.10 = 10%). |
| `hell_passage.masteryPerCast` | 5 (0 to 500) | Mastery points awarded per successful cast.<br>EXTRA-tier mastery cap is 500, so 5/cast = 100 casts to master.<br>Set to 1 for the slow Tensura default; higher = faster mastery. |
| `hell_passage.cooldownSecondsMastered` | 10 (0 to 3,600) | Cooldown (seconds), mastered. |
| `hell_passage.cooldownSeconds` | 30 (0 to 3,600) | Cooldown (seconds), unmastered. |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- Not enough magicule.
- No room to open the portal.

</details>
