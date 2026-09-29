# Bewilder

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Bewilder](../../../assets/icons/tensura/skill/bewilder.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:bewilder` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 30,000 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Press |

</div>

> Manipulate friends and foes, compelling them to act according to your will.

## Modes

| # | Mode |
|---|---|
| 1 | Target |
| 2 | Area |
| 3 | Charm |
| 4 | Kill |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Area | 80 |  |
| Charm | 200 |  |
| Kill | 100 |  |
| other modes | 50 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Innate to mobs: [Kirara Mizutani](../../mobs/kirara-mizutani.md)
- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Related skills:** [Spiritual Attack Resistance](../resistance-skills/spiritual-attack-resistance.md), [Spiritual Attack Nullification](../resistance-skills/spiritual-attack-nullification.md)
- **Effects:** [Mind Control](../../effects/mind-control.md), [Rampage](../../effects/rampage.md)
- **Referenced by:** [Pride Manas](../../../tr-nightmares/abilities/ultimate-skills/pride-manas.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Bewilder.mpAcquirement` | 30,000 | Magicule Acquirement Cost. |
| `Bewilder.magiculeCostTarget` | 50 | Magicule Cost to activate Target Mode. |
| `Bewilder.magiculeCostArea` | 80 | Magicule Cost to activate Area Mode. |
| `Bewilder.magiculeCostCharm` | 200 | Magicule Cost to activate Charm Mode. |
| `Bewilder.magiculeCostKill` | 100 | Magicule Cost to activate Kill Mode. |
| `Bewilder.controlDuration` | 12,000 | The duration in tick of the Mind Control effect (-1 = permanent). |
| `Bewilder.controlResistedDuration` | 6,000 | The duration in tick of the Mind Control effect when the target has Spiritual Attack Resistance (-1 = permanent). |
| `Bewilder.areaRadius` | 10 | The radius in block of the Area/Kill Mode. |
| `Bewilder.areaRadiusMastered` | 15 | The radius in block of the Area/Kill Mode when mastered. |
| `Bewilder.controlAreaDuration` | 6,000 | The duration in tick of the Mind Control effect when using Area Mode (-1 = permanent). |
| `Bewilder.controlAreaResistedDuration` | 3,000 | The duration in tick of the Mind Control effect when using Area Mode while the target has Spiritual Attack Resistance (-1 = permanent). |
| `Bewilder.heroDuration` | 2,400 | The duration in tick of the Hero of the Village effect when activating Charm Mode. |
| `Bewilder.heroLevel` | 5 | The level of the Hero of the Village effect when activating Charm Mode. |
| `Bewilder.killHPMultiplier` | 1 | The multiplier of targets' current HP to deal when activating Kill Mode. |
| `Bewilder.killHPResistedMultiplier` | 0.5 | The multiplier of targets' current HP to deal when activating Kill Mode while the target has Spiritual Attack Resistance. |
| `Bewilder.killCooldown` | 5 | The cooldown in second of the Kill Mode. |
| `Bewilder.killCooldownMastered` | 3 | The cooldown in second of the Kill Mode when mastered. |

## Tags

`tensura:skills/lust`, `tensura:skills/unique_skills`
