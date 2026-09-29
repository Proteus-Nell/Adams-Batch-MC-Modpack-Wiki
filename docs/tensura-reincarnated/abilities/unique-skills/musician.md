# Musician

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Musician](../../../assets/icons/tensura/skill/musician.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:musician` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 70,000 |
| **Cooldowns (s)** | 1, 3 |
| **Activation** | Toggle, Press |

</div>

> Turn beautiful music into an instrument of destruction. Use sound to create powerful blasts which ignore armor.

## Modes

| # | Mode |
|---|---|
| 1 | Sonic Blast |
| 2 | Sound Wave |
| 3 | Mind Requiem |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Sound Wave | 100 |  |
| Mind Requiem | 200 |  |
| other modes | 50 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Musician.mpAcquirement` | 70,000 | Magicule Acquirement Cost. |
| `Musician.magiculeCostBlast` | 50 | Magicule Cost to activate Sonic Blast. |
| `Musician.magiculeCostWave` | 100 | Magicule Cost to activate Sonic Wave. |
| `Musician.magiculeCostRequiem` | 200 | Magicule Cost to activate Mind Requiem. |
| `Musician.blastRange` | 8 | The range in block of the Sonic Blast mode. |
| `Musician.blastRangeMastered` | 12 | The range in block of the Sonic Blast mode when mastered. |
| `Musician.blastDamage` | 75 | The damage of the Sonic Blast mode. |
| `Musician.blastDamageMastered` | 150 | The damage of the Sonic Blast mode when mastered. |
| `Musician.blastCooldown` | 1 | The cooldown in second of the Sonic Blast mode. |
| `Musician.waveRadius` | 5 | The radius in block of the Sonic Wave mode. |
| `Musician.waveDamage` | 40 | The damage of the Sonic Wave mode. |
| `Musician.waveDamageMastered` | 75 | The damage of the Sonic Wave mode when mastered. |
| `Musician.waveCooldown` | 1 | The cooldown in second of the Sonic Wave mode. |
| `Musician.requiemRange` | 10 | The range in block of the Mind Requiem mode. |
| `Musician.requiemDamage` | 150 | The damage of the Mind Requiem mode. |
| `Musician.requiemSpiritualDamage` | 100 | The spiritual damage of the Mind Requiem mode. |
| `Musician.requiemCooldown` | 3 | The cooldown in second of the Mind Requiem mode. |

## Tags

`tensura:skills/sound_skills`, `tensura:skills/unique_skills`
