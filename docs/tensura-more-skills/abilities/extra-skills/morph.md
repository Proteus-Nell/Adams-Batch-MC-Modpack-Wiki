# Morph

<small>[TensuraMoreSkills](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Morph](../../../assets/icons/tensuramoreskills/skill/morph.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensuramoreskills:morph` |
| **Modes** | 1 |
| **Acquisition cost (MP)** | 10,000 |
| **Max mastery** | 1,000 |
| **Cooldowns (s)** | 60 |
| **Activation** | Press |

</div>

> An extra skill that copies the outer form of weaker living beings. Look at a target and use Morph to take its model. Sneak-use to release the transformation.

## Modes

| # | Mode |
|---|---|
| 1 | Transform |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 |  |

## How it works

- Activated by pressing the skill key

## Stats (config defaults)

Set in [`config/tensuramoreskills-grand.toml`](../../configs/config-tensuramoreskills-grand.md).

| Option | Default | Description |
|---|---|---|
| `obtainment.acquirementMagiculeCost` | 10,000 (0 to no limit) | Magicule cost required to naturally acquire Morph. |
| `obtainment.acquirementMastery` | 0 (-1 to no limit) | Starting mastery value when acquired. |
| `obtainment.requiredSkillId` | "tensura:spatial_domination" | Required skill registry ID for obtainment. Empty disables the required skill check. |
| `obtainment.requiredSkillMustBeMastered` | true | If true, the required skill must be mastered before Morph can be acquired. |
| `general.magiculeCost` | 500 (0 to no limit) | Magicule cost to transform into the selected target. |
| `obtainment.maxMastery` | 1,000 (1 to no limit) | Maximum mastery value for Morph. |
| `general.cooldownTicks` | 60 (0 to no limit) | Cooldown in ticks after morphing or cancelling Morph. |
| `general.range` | 12 (1 to 128) | Maximum look range for choosing a morph target. |
| `general.allowPlayerMorphs` | false | If true, Morph can try to copy players. Keep false or crashes may occur. |
| `general.blacklistedEntities` | "minecraft:ender_dragon", "minecraft:wither" | Entity IDs Morph can never copy. |
| `general.maxTargetEpPercent` | 0.01 (0 to 1) | Target must have EP at or below this fraction of the user's max EP. 0.01 means 1 percent. |

## In-game messages

<details markdown><summary>Show 6 messages</summary>

- Morphed into %s.
- Morph released.
- Look at a living entity to morph.
- That target cannot be morphed into.
- That entity is blacklisted from Morph.
- That entity's EP is too high to morph into.

</details>
