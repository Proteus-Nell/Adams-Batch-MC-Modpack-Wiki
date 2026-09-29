# Prickly Hands

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

![Prickly Hands](../../../assets/icons/ascension/skill/prickly_hands.png)

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `ascension:prickly_hands` |
| **Activation** | Passive |

</div>

> Toggle: melee hits inflict Bleeding (tier 1, tier 2 mastered). Direct contact only.

## How it works

- Triggers on melee contact

## Obtaining

- Can be learned by: [Blood Noble](../../races/blood-noble.md), [Elder Bloodfiend](../../races/elder-bloodfiend.md), [Progenitor Bloodfiend](../../races/progenitor-bloodfiend.md)

## Related

- **Effects:** [Bleeding](../../effects/bleeding.md)

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `prickly_hands.enabled` | true | Enable Prickly Hands. |
| `prickly_hands.tierMastered` | 2 (1 to 10) | Bleeding tier applied on melee hit, mastered. |
| `prickly_hands.tier` | 1 (1 to 10) | Bleeding tier applied on melee hit, unmastered (1 = 0.5 dmg/s). |
| `prickly_hands.durationSecondsMastered` | 10 (1 to 600) | Bleeding duration, mastered (seconds). |
| `prickly_hands.durationSeconds` | 5 (1 to 600) | Bleeding duration, unmastered (seconds). |

## Tags

`tensura:skills/common_skills`
