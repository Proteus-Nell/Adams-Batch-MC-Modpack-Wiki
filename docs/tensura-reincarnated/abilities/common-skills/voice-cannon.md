# Voice Cannon

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

![Voice Cannon](../../../assets/icons/tensura/skill/voice_cannon.png)

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `tensura:voice_cannon` |
| **Cooldowns (s)** | 3 |
| **Activation** | Press |

</div>

> Fire powerful blasts of concentrated sound waves by producing loud vocal sounds atomizing weaker targets.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Innate to mobs: [Blade Tiger](../../mobs/blade-tiger.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Greater Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Golden Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Chimera Lord can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.
- Acquisition checks: [Coercion](coercion.md)

## Related

- **Related skills:** [Coercion](coercion.md)
- **Effects:** [Silence](../../effects/silence.md)
- **Referenced by:** [｢ Hastur, Lord of Starwind ｣](../../../tr-nightmares/abilities/ultimate-skills/hastur.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/common_config.toml`](../../configs/config-tensura-ability-skill-common-config.md).

| Option | Default | Description |
|---|---|---|
| `VoiceCannon.epAcquirement` | 10,000 | EP Requirement for Learning when Coercion mastered. |
| `VoiceCannon.magiculeCost` | 500 | Magicule Cost to activate . |
| `VoiceCannon.cannonDamage` | 20 | The damage of the Voice Cannon when hit a target. |
| `VoiceCannon.cannonDamageMastered` | 30 | The damage of the Voice Cannon when hit a target with mastery. |
| `VoiceCannon.cannonRange` | 15 | The range in block of the Voice Cannon. |
| `VoiceCannon.cannonRangeMastered` | 20 | The range in block of the Voice Cannon when mastered. |
| `VoiceCannon.cannonCooldown` | 3 | The cooldown in second after activating Voice Cannon. |

## Tags

`tensura:skills/common_skills`, `tensura:skills/sound_skills`
