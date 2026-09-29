# Coercion

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

![Coercion](../../../assets/icons/tensura/skill/coercion.png)

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `tensura:coercion` |
| **Cooldowns (s)** | 1 mastered, 2 otherwise |
| **Activation** | Press |

</div>

> Shoot a blast of roar in front of you scaring any afflicted entities.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50 |  |

## How it works

- Activated by pressing the skill key
- Adjusted by scrolling while active

## Obtaining

- Intrinsic skill of: [Vampire](../../races/vampire.md), [Vampire Overcomer](../../races/vampire-overcomer.md), [Vampire Lord](../../races/vampire-lord.md), [Divine Vampire](../../races/divine-vampire.md)
- Innate to mobs: [Direwolf](../../mobs/direwolf.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/direwolf_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/special_direwolf_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Effects:** [Fear](../../effects/fear.md)
- **Referenced by:** [Voice Cannon](voice-cannon.md), [Haki](../extra-skills/haki.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/common_config.toml`](../../configs/config-tensura-ability-skill-common-config.md).

| Option | Default | Description |
|---|---|---|
| `Coercion.epAcquirement` | 5,000 | EP Requirement for Learning. |
| `Coercion.magiculeCost` | 50 | Magicule Cost to activate. |
| `Coercion.roarRange` | 14 | The attack range of the roar in blocks. |
| `Coercion.epDifferenceMultiplier` | 0.25 | The EP difference multiplier for each Fear Level. |
| `Coercion.fearDuration` | 200 | The duration in tick of the Fear effect. |
| `Coercion.cooldown` | 2 | The Cooldown in second after activation (halved when mastered). |

Set in [`config/tensura/entity/effect_config.toml`](../../configs/config-tensura-entity-effect-config.md).

| Option | Default | Description |
|---|---|---|
| `maxFear` | 20 | The max level of Fear can be applied legally in game. |
| `maxFear` | 20 | The max level of Fear can be applied legally in game. |

## Tags

`tensura:skills/common_skills`
