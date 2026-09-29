# Sense Heat Source

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Sense Heat Source](../../../assets/icons/tensura/skill/sense_heat_source.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:sense_heat_source` |
| **Activation** | Toggle, Press |

</div>

> Highlights entities that generate heat nearby.

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Does something when first learned

## Obtaining

- Innate to mobs: [Hover Lizard](../../mobs/hover-lizard.md), [Leech Lizard](../../mobs/leech-lizard.md), [Tempest Serpent](../../mobs/tempest-serpent.md)

## Related

- **Related skills:** [Sense Soundwave](sense-soundwave.md), [Magic Sense](magic-sense.md), [Universal Perception](universal-perception.md)
- **Referenced by:** [Magic Sense](magic-sense.md), [Sense Soundwave](sense-soundwave.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `SenseHeatSource.heatRadius` | 20 | The radius in block that mobs and blocks around the user will be detected by heat sense. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/extra_skills`
