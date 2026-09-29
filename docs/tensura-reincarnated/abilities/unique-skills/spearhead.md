# Spearhead

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Spearhead](../../../assets/icons/tensura/skill/spearhead.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:spearhead` |
| **Acquisition cost (MP)** | 60,000 |
| **Activation** | Press |

</div>

> Empower and command your allies, and then collect their abilities once they pass on.

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when one of your subordinates dies

## Obtaining

- Innate to mobs: [Folgen](../../mobs/folgen.md)
- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Effects:** [Spearhead](../../effects/spearhead.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Spearhead.mpAcquirement` | 60,000 | Magicule Acquirement Cost. |
| `Spearhead.allyRadius` | 20 | The radius in block to apply skill effect on Allies. |
| `Spearhead.allyAttack` | 10 | The bonus attack damage allies gain when activated (doubled with Mastery). |
| `Spearhead.allyArmor` | 5 | The bonus armor allies gain when activated (doubled with Mastery). |
| `Spearhead.allySpeed` | 0.02 | The bonus speed allies gain when activated (doubled with Mastery). |
| `Spearhead.allySwim` | 1 | The bonus swimming speed allies gain when activated (doubled with Mastery). |
| `Spearhead.fallenRange` | 20 | The range in block that the owner needs to be within fallen subordinates to gain their power. |

## Tags

`tensura:skills/unique_skills`
