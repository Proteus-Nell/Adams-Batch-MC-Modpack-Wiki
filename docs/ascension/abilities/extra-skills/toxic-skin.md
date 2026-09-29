# Toxic Skin

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Toxic Skin](../../../assets/icons/ascension/skill/toxic_skin.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `ascension:toxic_skin` |
| **Activation** | Passive |

</div>

> Toggle: melee attackers are poisoned for 5s (10s mastered, stronger).

## How it works

- Triggers when you are attacked

## Obtaining

- Can be learned by: [Frog](../../races/frog.md), [Giant Frog](../../races/giant-frog.md), [Poison Toad](../../races/poison-toad.md), [Swamp Sovereign](../../races/swamp-sovereign.md), [Bog Ancient](../../races/bog-ancient.md), [Venom Lord](../../races/venom-lord.md), [Frog Monarch](../../races/frog-monarch.md)

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `toxic_skin.enabled` | true | Enable Toxic Skin. |
| `toxic_skin.poisonDurationSecondsMastered` | 10 (1 to 600) | Poison duration, mastered (seconds). |
| `toxic_skin.poisonDurationSeconds` | 5 (1 to 600) | Poison duration, unmastered (seconds). |

## Tags

`tensura:skills/extra_skills`
