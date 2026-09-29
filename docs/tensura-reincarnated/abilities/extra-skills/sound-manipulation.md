# Sound Manipulation

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Sound Manipulation](../../../assets/icons/tensura/skill/sound_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:sound_manipulation` |
| **Activation** | Toggle |

</div>

> Boosts Sound abilities by a decent amount.

## How it works

- Can be toggled on and off
- Triggers on melee contact
- Does something when mastered

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/wyrm_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Sound Domination](sound-domination.md)
- **Referenced by:** [Sound Domination](sound-domination.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `SoundManipulation.soundMasteredSkillAcquirement` | 3 | The number of mastered sound/wind skills needed to learn Sound Manipulation. |
| `SoundManipulation.dominationEpAcquirement` | 400,000 | EP Requirement for to learn Domination. |
| `SoundManipulation.manipulationBoost` | 1.5 | The Sound Damage Boost when activated Manipulation. |
| `SoundManipulation.dominationBoost` | 3 | The Sound Damage Boost when activated Domination. |

## Tags

`tensura:skills/extra_skills`, `tensura:skills/sound_skills`
