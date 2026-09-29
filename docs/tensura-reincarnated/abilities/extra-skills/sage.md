# Sage

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Sage](../../../assets/icons/tensura/skill/sage.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:sage` |
| **Activation** | Toggle |

</div>

> Increase the speed at which you learn and master skills, magic and arts.

## How it works

- Can be toggled on and off

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| learning | 2 | add |
| mastery | 2 | add |

## Obtaining

- Intrinsic skill of: [Medium Class Saiyan](../../../elite-tensura/races/medium-saiyan.md), [High Class Saiyan](../../../elite-tensura/races/high-saiyan.md), [Divine Saiyan](../../../elite-tensura/races/divine-saiyan.md)
- Can be learned by: [Elder Lich](../../../ascension/races/elder-lich.md), [Lich](../../../ascension/races/lich.md), [Lich King](../../../ascension/races/lich-king.md)
- Listed in the `intrinsicSkills` config option (config/nightmare/race/scholar_config.toml): List of skills obtained by this race.

## Related

- **Referenced by:** [｢ Raphael, Lord of Knowledge ｣](../../../tr-nightmares/abilities/ultimate-skills/raphael-knowledge.md), [｢ Raphael, Lord of Wisdom ｣](../../../tr-nightmares/abilities/ultimate-skills/raphael-wisdom.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `Sage.abilityMastered` | 20 | The number of Magic/Art needed to be mastered to learn Sage. |
| `Sage.learningPoint` | 2 | The bonus number of learning point to gain when toggled. |
| `Sage.masteryPoint` | 2 | The bonus number of mastery point to gain when toggled. |

## Tags

`tensura:skills/extra_skills`
