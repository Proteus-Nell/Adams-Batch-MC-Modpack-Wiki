# Saint

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:saint` |
| **Modes** | 2 |
| **Cooldowns (s)** | 1 |
| **Activation** | Hold |

</div>

> As a young hero, you fancy yourself holier and more pure than others, in fact, you could be considered rather Chaste compared to a nun, and your attacks leave others feeling no better.

## Modes

| # | Mode |
|---|---|
| 1 | Disintegration |
| 2 | Melt Cut |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Disintegration | 25,000 |  |
| other modes | *set by config (base cost)* |  |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -1 | multiply total |

## Obtaining

- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.

## Related

- **Effects:** [Holy Damage](../../../tensura-reincarnated/effects/holy-damage.md), [Movement Interference](../../../tensura-reincarnated/effects/movement-interference.md)
- **Referenced by:** [Secret of Grace](../extra-skills/secret-of-grace.md), [｢ Metatron, Lord of Purity ｣](../ultimate-skills/metatron.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Saint.mpAcquirement` | 95,000 | Magicule Acquirement Cost. |
| `Saint.spiritronReqPercent` | 90 | Percentage of magicules required to generate Spiritron Points. |
| `Saint.spGenerationDefault` | 1 | Number of Spiritrons generated (Unmastered). |
| `Saint.spGenerationMastered` | 5 | Number of Spiritrons generated (Mastered). |
| `Saint.spPurifyRequirement` | 50 | Spiritron Points required to purify attacks. |
| `Saint.purifyDamage` | 20 | Amount of Holy Damage dealt by physical attacks (Doubled on mastery). |
| `Saint.miracleBuff` | 25 | Amount Holy damage is buffed by Holy Miracle. |
| `Saint.miracleBuffMastered` | 75 | Amount Holy damage is buffed by Holy Miracle when mastered. |
| `Saint.miracleDebuff` | 50 | Amount of damage dealt to user by Holy Miracle. |
| `Saint.miracleDebuffMastered` | 25 | Amount of damage dealt to user by Holy Miracle when mastered. |
| `Saint.spDisintegrationRequirement` | 75 | Spiritron Points required to cast Disintegration. |
| `Saint.mpDisintegrationRequirement` | 25,000 | Magicules required to cast Disintegration. |
| `Saint.disintegrationDamage` | 150 | Amount of damage dealt by disintegration. |
| `Saint.meltDamage` | 75 | Amount of Holy damage dealt by Melt Cut. |
| `Saint.meltCooldown` | 1 | Cooldown of Melt Cut. |

## Tags

`tensura:skills/nun`
