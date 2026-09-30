# Blood Mist

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Blood Mist](../../../assets/icons/tensura/skill/blood_mist.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:blood_mist` |
| **Modes** | 2 |
| **Cooldowns (s)** | 2 mastered, 4 otherwise |
| **Activation** | Press, Hold |

</div>

> Spill your own blood to summon a mist which steals the vitality of your enemies and can be blown up to harm any nearby entities or shoot a powerful blood beam.

## Modes

| # | Mode |
|---|---|
| 1 | Default |
| 2 | Blood Ray |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10,000 or 500 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Related

- **Summons / entities:** Blood Ray, [Blood Mist](blood-mist.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `BloodMist.rayAcquirement` | 500,000 | EP Requirement to use Blood Ray. |
| `BloodMist.magiculeCost` | 500 | Magicule Cost to activate the Default Mode. |
| `BloodMist.rayMagiculeCost` | 10,000 | Magicule Cost to activate Blood Ray. |
| `BloodMist.mistRange` | 10 | The spawn range in block of the blood mist. |
| `BloodMist.mistDamage` | 10 | The damage per second of the blood mist. |
| `BloodMist.mistRadius` | 5 | The radius of the blood mist. |
| `BloodMist.mistCooldown` | 4 | The cooldown of the blood mist (halved with mastery). |
| `BloodMist.rayRange` | 40 | The spawn range in block of the blood ray. |
| `BloodMist.rayDamage` | 50 | The damage per second of the blood ray. |
| `BloodMist.rayHPCost` | 10 | How much HP the user loses every 10 tick of using blood ray. |

## Tags

`tensura:skills/intrinsic_skills`
