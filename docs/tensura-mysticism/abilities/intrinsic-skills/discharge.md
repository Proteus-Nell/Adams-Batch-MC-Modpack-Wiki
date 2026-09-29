# Discharge

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Discharge](../../../assets/icons/mysticism/skill/discharge.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `mysticism:discharge` |
| **Cooldowns (s)** | 5 |
| **Activation** | Press |

</div>

> Strike a bolt of lightning using your inner bio-electricity generated from a sac within you. Can be used without thundering weather.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/sculk_config.toml): The list of intrinsic skills that the race gets.

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/intrinsic_config.toml`](../../configs/config-mysticism-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `Discharge.magiculeCost` | 1,000 | Magicule Cost to activate. |
| `Discharge.boltDamage` | 15 | How much damage that the Lightning Bolt does when activated. |
| `Discharge.boltRange` | 3 | The range for damage that the Lightning Bolt does when activated. |
| `Discharge.selectionRange` | 30 | The selection range of the target in blocks. |
| `Discharge.cooldown` | 5 | The cooldown in seconds. |

## Tags

`tensura:skills/intrinsic_skills`
