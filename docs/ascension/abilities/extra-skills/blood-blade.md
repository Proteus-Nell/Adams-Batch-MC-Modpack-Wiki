# Blood Blade

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Blood Blade](../../../assets/icons/ascension/skill/blood_blade.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `ascension:blood_blade` |
| **Activation** | Press |

</div>

> Active: fire a crimson blade for 10 blood-attribute damage. Costs 1 HP — pays in blood, not magicule.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 |  |

## How it works

- Activated by pressing the skill key

## Related

- **Summons / entities:** [Blood Blade](blood-blade.md)

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `blood_blade.enabled` | true | Enable Blood Blade. |
| `blood_blade.healthCost` | 1 (0 to 100) | HP cost paid by the caster per cast. |
| `blood_blade.speed` | 3 (0.1 to 20) | Projectile flight speed multiplier. |
| `blood_blade.damage` | 10 (0 to 1,000) | Damage dealt to target on hit. |

## Tags

`tensura:skills/extra_skills`
