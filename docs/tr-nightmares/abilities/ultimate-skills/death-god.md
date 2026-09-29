# Death God

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Death God](../../../assets/icons/trnightmare/skill/death_god.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:death_god` |
| **Activation** | Press |

</div>

> A legacy ultimate-adjacent skill representing authority over deathly principles.

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target

## Related

- **Effects:** [Rotting](../../effects/rotting.md), [Corrosion](../../../tensura-reincarnated/effects/corrosion.md)
- **Referenced by:** [Gift](../unique-skills/gift.md), [｢ Astraea, Lord of Gifts ｣](astraea.md), [｢ Zehirete, God of Faith ｣](zehirete.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Laguna.deathGodLearningCost` | 2,000 | Learning cost for Laguna Death God. |
| `Laguna.bannedSkills` | [] (empty) | List of banned Laguna Skills. |
| `Laguna.allowedSkills` | "trnightmare:dark_blessing", "trnightmare:earth_blessing", "trnightmare:fire_blessing", "trnightmare:gathering_spirits_blessing", "trnightmare:judgement_blessing", "trnightmare:lakes_blessing", "trnightmare:light_blessing", "trnightmare:sandplay_blessing", "trnightmare:shedding_blood_blessing", "trnightmare:time_blessing", "trnightmare:water_blessing", "trnightmare:wind_blessing", "trnightmare:unarmed_combat_blessing", "trnightmare:wind_reading", "trnightmare:wind_evasion", "trnightmare:sky_enjoyer", "trnightmare:insensitivity", "trnightmare:durability", "trnightmare:food_lover" | Permitted Laguna Skills. |
| `Laguna.swordSaintEpAcquirement` | 100,000 | EP obtainment cost for Laguna Sword Saint. |
| `Laguna.phoenixEpAcquirement` | 100,000 | EP obtainment cost for Laguna Phoenix. |
| `Laguna.deathGodEpAcquirement` | 500,000 | EP obtainment cost for Laguna Death God ultimate. |
| `Laguna.deathGodLearningCost` | 2,000 | Learning cost for Laguna Death God. |
| `Laguna.phoenixNextEpAcquirement` | 250,000 | EP obtainment cost for Laguna Phoenix Next ultimate. |
| `Laguna.phoenixNextLearningCost` | 2,000 | Learning cost for Laguna Phoenix Next. |

## Tags

`tensura:skills/ultimate_skills`
