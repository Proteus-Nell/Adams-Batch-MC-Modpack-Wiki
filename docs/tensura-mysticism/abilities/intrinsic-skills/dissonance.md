# Dissonance

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Dissonance](../../../assets/icons/mysticism/skill/dissonance.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `mysticism:dissonance` |
| **Cooldowns (s)** | 5 |
| **Activation** | Press |

</div>

> You are the calamity. You are the storm, and you are approaching. Strike lightning in all cardinal directions that deal massive Electricity Damage to all those unfortunate to be hit by it.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10,000 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/sculk_config.toml): The list of intrinsic skills that the race gets.

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/intrinsic_config.toml`](../../configs/config-mysticism-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `Dissonance.magiculeCost` | 10,000 | Magicule Cost to activate. |
| `Dissonance.boltDamage` | 30 | How much damage that the Lightning Bolt does when activated. |
| `Dissonance.boltRange` | 5 | The range for damage that the Lightning Bolt does when activated. |
| `Dissonance.selectionRange` | 30 | The selection range of the target in blocks. |
| `Dissonance.cooldown` | 5 | The cooldown in seconds. |
| `Dissonance.radius` | 5 | The radius of effect. |

## Tags

`tensura:skills/intrinsic_skills`
