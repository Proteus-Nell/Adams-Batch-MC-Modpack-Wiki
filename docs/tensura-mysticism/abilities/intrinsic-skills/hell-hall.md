# Hell Hall

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Hell Hall](../../../assets/icons/mysticism/skill/hell_hall.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `mysticism:hell_hall` |
| **Cooldowns (s)** | 600 |
| **Activation** | Press |

</div>

> Rupture the floor, raising your natural body temperature to liquefy all surfaces around you to molten levels.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5,000 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/sculk_config.toml): The list of intrinsic skills that the race gets.

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/intrinsic_config.toml`](../../configs/config-mysticism-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `HellHall.magiculeCost` | 5,000 | Magicule Cost to activate. |
| `HellHall.cooldown` | 600 | The cooldown in seconds. |
| `HellHall.cooldownMastered` | 600 | The cooldown in seconds when the skill is mastered. |
| `HellHall.radius` | 4 | The radius. |
| `HellHall.radiusMastered` | 4 | The radius when the skill is mastered. |

## Tags

`tensura:skills/intrinsic_skills`
