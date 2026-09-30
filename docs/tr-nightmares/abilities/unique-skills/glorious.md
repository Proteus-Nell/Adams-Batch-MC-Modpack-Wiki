# Glorious

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Glorious](../../../assets/icons/trnightmare/skill/glorious.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:glorious` |
| **Activation** | Toggle |

</div>

> You shan't take severing damage, and forever will you heal.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Triggers when a mob targets you

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| dodgeNegate | 50 | add |
| learning | 4 | add |
| mastery | 4 | add |

## Related

- **Effects:** [Glorious Regen](../../effects/glorious-regen.md)
- **Summons / entities:** Tensura
- **Referenced by:** [｢ Astraea, Lord of Gifts ｣](../ultimate-skills/astraea.md), [｢ Haniel, Lord of Glory ｣](../ultimate-skills/haniel.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Glorious.mpAcquirement` | 75,000 | Magicule Acquirement Cost. |
| `Glorious.regenCostMultiplier` | 0.5 | Magicule Cost multiplier for ultraspeed regen. |
| `Glorious.dodgeChanceIgnore` | 50 | Dodge ignoring chance. |
| `Glorious.presenceSense` | 2 | Level of Presence Sense. |
| `Glorious.learningPoint` | 4 | Learning point boost for skills |
| `Glorious.masteryPoint` | 4 | Mastery point gain for Skills |
