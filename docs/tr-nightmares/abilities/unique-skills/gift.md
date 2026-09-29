# Gift

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Gift](../../../assets/icons/trnightmare/skill/gift.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:gift` |
| **Acquisition cost (MP)** | 75,000 |
| **Max mastery** | 1,000 |
| **Cooldowns (s)** | 100 |
| **Activation** | Press, Hold |

</div>

> Forge Divine Protections as sub-skills

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 or base cost |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Triggers when you damage a target
- Triggers on melee contact
- Triggers when you are attacked
- Triggers when you take damage
- Triggers when an effect is applied to you
- Triggers when a projectile hits you
- Triggers when you die
- Triggers when you respawn

## Related

- **Related skills:** [Phoenix](../ultimate-skills/phoenix.md), [Sword Saint](../ultimate-skills/sword-saint.md), [Death God](../ultimate-skills/death-god.md), [Phoenix Next](../ultimate-skills/phoenix-next.md), [Hero Banner Blessing](../extra-skills/hero-banner-blessing.md)
- **Referenced by:** [｢ Astraea, Lord of Gifts ｣](../ultimate-skills/astraea.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Laguna.bannedSkills` | [] (empty) | List of banned Laguna Skills. |
| `Laguna.allowedSkills` | "trnightmare:dark_blessing", "trnightmare:earth_blessing", "trnightmare:fire_blessing", "trnightmare:gathering_spirits_blessing", "trnightmare:judgement_blessing", "trnightmare:lakes_blessing", "trnightmare:light_blessing", "trnightmare:sandplay_blessing", "trnightmare:shedding_blood_blessing", "trnightmare:time_blessing", "trnightmare:water_blessing", "trnightmare:wind_blessing", "trnightmare:unarmed_combat_blessing", "trnightmare:wind_reading", "trnightmare:wind_evasion", "trnightmare:sky_enjoyer", "trnightmare:insensitivity", "trnightmare:durability", "trnightmare:food_lover" | Permitted Laguna Skills. |
| `Laguna.swordSaintEpAcquirement` | 100,000 | EP obtainment cost for Laguna Sword Saint. |
| `Laguna.phoenixEpAcquirement` | 100,000 | EP obtainment cost for Laguna Phoenix. |
| `Laguna.deathGodEpAcquirement` | 500,000 | EP obtainment cost for Laguna Death God ultimate. |
| `Laguna.deathGodLearningCost` | 2,000 | Learning cost for Laguna Death God. |
| `Laguna.phoenixNextEpAcquirement` | 250,000 | EP obtainment cost for Laguna Phoenix Next ultimate. |
| `Laguna.phoenixNextLearningCost` | 2,000 | Learning cost for Laguna Phoenix Next. |
| `Gift.epAcquirement` | 75,000 | EP / magicule obtainment cost to acquire Gift. |
| `Gift.giftCreationCooldownTicks` | 100 | Cooldown in ticks after adding a divine protection (Gift Creation, mode 0). |
| `Gift.giftCreationMagiculeCost` | 0 | Magicule cost to use Gift Creation (mode 0); 0 disables. |

## In-game messages

<details markdown><summary>Show 4 messages</summary>

- Gift Creation
- Gift Creation
- Add Divine Protection
- Could not add that Divine Protection as a sub-skill.

</details>
