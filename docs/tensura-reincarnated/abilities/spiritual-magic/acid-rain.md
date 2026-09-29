# Acid Rain

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Acid Rain](../../../assets/icons/tensura/skill/acid_rain.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:acid_rain` |
| **Element** | Water |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Cooldowns (s)** | 1 mastered, 3 otherwise |
| **Activation** | Press, Hold |

</div>

> Summon an acidic cloud which will corrode any afflicted entities.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Undine](../../mobs/undine.md)
- Removed and re-rolled when you change race
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill registry IDs automatically granted with Albis Vina.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `AcidRain.castTime` | 80 | Cast time in tick. |
| `AcidRain.castTimeMastered` | 60 | Cast time in tick when mastered. |
| `AcidRain.magiculeCost` | 1,000 | Magicule Cost to cast. |
| `AcidRain.range` | 20 | The range in block of the magic. |
| `AcidRain.rainDamage` | 40 | The damage of the acid rain. |
| `AcidRain.rainRadius` | 7.5 | The radius in block of the acid rain. |
| `AcidRain.rainRadiusMastered` | 10 | The radius in block of the acid rain when mastered. |
| `AcidRain.rainDuration` | 400 | The max duration in tick that the magic can be used. |
| `AcidRain.cooldown` | 3 | The cooldown in second of the magic. |
| `AcidRain.cooldownMastered` | 1 | The cooldown in second of the magic when mastered. |

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
