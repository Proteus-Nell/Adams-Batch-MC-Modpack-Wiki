# Earth Jail

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Earth Jail](../../../assets/icons/tensura/skill/earth_jail.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:earth_jail` |
| **Element** | Earth |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Cooldowns (s)** | 10 mastered, 20 otherwise |
| **Activation** | Hold |

</div>

> Restrict and weaken a single target, applying debuffs to allow you to finish them off.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 30,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Hinata Sakaguchi](../../mobs/hinata-sakaguchi.md), [War Gnome](../../mobs/war-gnome.md)
- Removed and re-rolled when you change race

## Related

- **Related skills:** [Earth Attack Nullification](../resistance-skills/earth-attack-nullification.md), [Earth Attack Resistance](../resistance-skills/earth-attack-resistance.md), [Burden](../aspectual-magic/burden.md)
- **Effects:** [Movement Interference](../../effects/movement-interference.md), [Fragility](../../effects/fragility.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `EarthJail.castTime` | 140 | Cast time in tick. |
| `EarthJail.castTimeMastered` | 140 | Cast time in tick when mastered. |
| `EarthJail.magiculeCost` | 30,000 | Magicule Cost to cast. |
| `EarthJail.range` | 20 | The range in block of the magic. |
| `EarthJail.rangeMastered` | 30 | The range in block of the magic when mastered. |
| `EarthJail.jailDamage` | 50 | The damage of the magic. |
| `EarthJail.jailSpeed` | 6 | The level of Movement Interference effect (-10% speed each) when applied by the magic. |
| `EarthJail.jailSpeedResisted` | 4 | The decreased level of Movement Interference effect if the target has Earth Attack Resistance. |
| `EarthJail.jailFatigue` | 2 | The level of the Mining Fatigue effect when applied by the magic. |
| `EarthJail.jailBurden` | 2 | The level of the Burden effect when applied by the magic. |
| `EarthJail.jailFragility` | 2 | The level of the Fragility effect when applied by the magic. |
| `EarthJail.jailDuration` | 1,200 | The duration in tick of each effect when applied by the magic. |
| `EarthJail.cooldown` | 20 | The cooldown in second of the magic. |
| `EarthJail.cooldownMastered` | 10 | The cooldown in second of the magic when mastered. |

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
