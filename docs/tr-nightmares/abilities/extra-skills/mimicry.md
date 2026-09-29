# Mimicry

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:mimicry` |
| **Modes** | 2 |
| **Activation** | Press |

</div>

> Analyze living entities, then mimic learned forms and end the mimicry when needed.

## Modes

| # | Mode |
|---|---|
| 1 | Mimicry |
| 2 | End Mimicry |

## How it works

- Activated by pressing the skill key

## Obtaining

- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.

## Related

- **Related skills:** [Predator](../../../tensura-reincarnated/abilities/unique-skills/predator.md), [Gluttony](../../../tensura-reincarnated/abilities/unique-skills/gluttony.md), [｢ Beelzebuth, Lord of Gluttony ｣](../ultimate-skills/beelzebuth.md)
- **Referenced by:** [Universal Shapeshift](universal-shapeshift.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `Mimicry.mimicryEpMaxDifference` | 0.3 | Maximum EP difference allowed between you and the target to analyze/mimic (fraction). |
| `Mimicry.mimicryAllowUniqueAndUltimate` | false | Allow Mimicry to copy Unique and Ultimate skills when enabled. |
| `Mimicry.learnRequired` | 100 | Number of learn points required to fully analyze a target (matches other imitator/artist configs). |
| `Mimicry.allowedSkillIds` | "tensura:predator", "tensura:gluttony", "tensura:beelzebuth" | Skill ids that are allowed to mimic. |

## Tags

`tensura:skills/no_plundering`
