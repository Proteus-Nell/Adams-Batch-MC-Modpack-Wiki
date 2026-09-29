# Ultrasonic Waves

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Ultrasonic Waves](../../../assets/icons/tensura/skill/ultrasonic_waves.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:ultrasonic_waves` |
| **Modes** | 2 |
| **Cooldowns (s)** | 1 mastered, 3 otherwise |
| **Activation** | Press |

</div>

> Shoot out a screech of sound which damages physical bodies or use echolocation to highlight nearby entities.

## Modes

| # | Mode |
|---|---|
| 1 | Sonic Wave |
| 2 | Auditory Sense |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 30 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Innate to mobs: [Giant Bat](../../mobs/giant-bat.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/sculk_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/wyrm_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Effects:** [Auditory Sense](../../effects/auditory-sense.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `UltrasonicWaves.magiculeCost` | 30 | Magicule Cost to activate . |
| `UltrasonicWaves.auditoryDuration` | 200 | The duration in tick of the Auditory Sense effect when activated. |
| `UltrasonicWaves.sonicRange` | 8 | The range in block of the Sonic Waves mode. |
| `UltrasonicWaves.sonicDamage` | 8 | The damage of the Sonic Waves when hit a target. |
| `UltrasonicWaves.sonicCooldown` | 3 | The cooldown in second after activating Sonic Waves (halved with mastery). |

## Tags

`tensura:skills/intrinsic_skills`, `tensura:skills/sound_skills`
