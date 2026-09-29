# Blood Frenzy

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Blood Frenzy](../../../assets/icons/ascension/skill/blood_frenzy.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `ascension:blood_frenzy` |
| **Activation** | Toggle |

</div>

> Toggle: bloodlust state — boosts attack damage and speed, drains your HP per second. Killing blows steal a portion of the victim's max HP back.

## How it works

- Can be toggled on and off
- Triggers when you damage a target

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| dmgInst | damage bonus | add |
| spdInst | speed bonus | add |

## Obtaining

- Can be learned by: [Fledgling Bloodfiend](../../races/fledgling-bloodfiend.md), [Kindred Bloodfiend](../../races/kindred-bloodfiend.md), [Blood Noble](../../races/blood-noble.md), [Elder Bloodfiend](../../races/elder-bloodfiend.md), [Progenitor Bloodfiend](../../races/progenitor-bloodfiend.md)

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `blood_frenzy.enabled` | true | Enable Blood Frenzy. |
| `blood_frenzy.attackDamageBonusMastered` | 5 (0 to 1,000) | Flat attack-damage bonus while toggled, mastered. |
| `blood_frenzy.attackDamageBonus` | 3 (0 to 1,000) | Flat attack-damage bonus while toggled, unmastered. |
| `blood_frenzy.attackSpeedBonusMastered` | 0.6 (0 to 10) | Flat attack-speed bonus while toggled, mastered. |
| `blood_frenzy.attackSpeedBonus` | 0.4 (0 to 10) | Flat attack-speed bonus while toggled, unmastered. |
| `blood_frenzy.auraDrainFractionMastered` | 0.0015 (0 to 1) | Fraction of max aura drained per tick, mastered. |
| `blood_frenzy.auraDrainFraction` | 0.003 (0 to 1) | Fraction of max aura drained per tick, unmastered. |
| `blood_frenzy.auraRestoreOnKillMastered` | 0.15 (0 to 1) | Fraction of max aura restored on kill, mastered. |
| `blood_frenzy.auraRestoreOnKill` | 0.1 (0 to 1) | Fraction of max aura restored on kill, unmastered. |

## Tags

`tensura:skills/extra_skills`
