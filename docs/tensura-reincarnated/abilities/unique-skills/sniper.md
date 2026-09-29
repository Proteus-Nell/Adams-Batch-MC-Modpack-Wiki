# Sniper

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Sniper](../../../assets/icons/tensura/skill/sniper.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:sniper` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 50,000 |
| **Cooldowns (s)** | 1 mastered, 3 otherwise |
| **Activation** | Toggle, Press |

</div>

> Deal damage from afar while using different bullets to get past resistances and ensure a quick kill.

## Modes

| # | Mode |
|---|---|
| 1 | Create Weapon |
| 2 | Spatial Manipulation |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| degrade | 1 | add |
| melee | 10 | add |
| projectile | 10 | add |
| negate | 50 | add |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Items:** [Walther P99](../../items/weapons/walther-p99.md)
- **Summons / entities:** Tensura, Sniper Grenade
- **Referenced by:** [Alteration](../../../tr-nightmares/abilities/extra-skills/alteration.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Sniper.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Sniper.magiculeCostWeapon` | 100 | Magicule Cost to activate Create Weapon. |
| `Sniper.meleeDodge` | 10 | Melee Dodge Chance when toggled. |
| `Sniper.projectileDodge` | 10 | Projectile Dodge Chance when toggled. |
| `Sniper.dodgeNegation` | 50 | Dodge Negation Chance when toggled. |
| `Sniper.presenceSense` | 2 | The level of Presence Sense when toggled. |
| `Sniper.manipulationBoost` | 2 | The Spatial Damage Boost when activated Manipulation. |
| `Sniper.warpShot` | 0.5 | The warp shot level when activated Spatial Manipulation's Warp Shot. |
| `Sniper.energyCostPistol` | 100 | Magicule/Aura Cost to use the created pistol. |
| `Sniper.physicalDamage` | 30 | The damage output of the Physical bullet. |
| `Sniper.physicalCooldown` | 10 | The cooldown in tick of the Physical bullet. |
| `Sniper.magicDamage` | 100 | The damage output of the Magic bullet. |
| `Sniper.magicDamageMastered` | 200 | The damage output of the Magic bullet when mastered. |
| `Sniper.magicCooldown` | 60 | The cooldown in tick of the Magic bullet. |
| `Sniper.grenadeExplosion` | 4 | The explosion radius of the Grenade. |
| `Sniper.grenadeCooldown` | 3 | The cooldown in second of the Grenade. |
| `Sniper.grenadeCooldownMastered` | 1 | The cooldown in second of the Grenade when mastered. |

## Tags

`tensura:skills/space_skills`, `tensura:skills/unique_skills`
