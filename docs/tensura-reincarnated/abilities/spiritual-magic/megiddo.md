# Megiddo

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Megiddo](../../../assets/icons/tensura/skill/megiddo.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:megiddo` |
| **Element** | Water |
| **Modes** | 2 |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Cooldowns (s)** | 1, 10 mastered, 15 otherwise |
| **Activation** | Press, Hold |

</div>

> Unleash powerful sun blasts using water to kill any nearby foes. It can also be used manually to concentrate fire for any stronger foes.

## Modes

| # | Mode |
|---|---|
| 1 | Single Target |
| 2 | Auto Target |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50,000 or 30,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Removed and re-rolled when you change race
- Listed in the `formulaSuccessionBlacklist` config option (config/tensuramoreskills-grand.toml): Spell registry IDs that Formula Succession is not allowed to mirror.
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill registry IDs automatically granted with Albis Vina.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `Megiddo.castTime` | 140 | Cast time in tick. |
| `Megiddo.castTimeMastered` | 140 | Cast time in tick when mastered. |
| `Megiddo.magiculeCostSingle` | 30,000 | Magicule Cost to cast the Single Target mode. |
| `Megiddo.magiculeCostAuto` | 50,000 | Magicule Cost to cast the Auto Target mode. |
| `Megiddo.beamDamage` | 150 | The damage of each beam. |
| `Megiddo.singleDuration` | 6,000 | The duration in tick of the Single Target mode. |
| `Megiddo.singleBeam` | 10 | The number of attack beam of the Single Target mode. |
| `Megiddo.singleBeamMastered` | 20 | The number of attack beam of the Single Target mode when mastered. |
| `Megiddo.singleRange` | 60 | The range in block of the Single Target mode. |
| `Megiddo.singleCooldown` | 1 | The cooldown in second for each beam of the Single Target mode. |
| `Megiddo.autoDuration` | 600 | The duration in tick of the Single Target mode. |
| `Megiddo.autoBeam` | 5 | The number of attack beam of the Single Target mode. |
| `Megiddo.autoBeamMastered` | 10 | The number of attack beam of the Single Target mode when mastered. |
| `Megiddo.autoRange` | 40 | The range in block of the Single Target mode. |
| `Megiddo.autoBeamTime` | 200 | How often in tick that the Auto Target mode releases more beams. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryMedium` | 500 | The max amount of mastery point for Medium Spiritual Magic. |
| `SpiritualMagic.masteryGreater` | 1,000 | The max amount of mastery point for Greater Spiritual Magic. |
| `SpiritualMagic.masteryLord` | 10,000 | The max amount of mastery point for Lord Spiritual Magic. |

## Tags

`tensura:skills/reset_with_race`, `tensura:skills/spiritual_magic`
