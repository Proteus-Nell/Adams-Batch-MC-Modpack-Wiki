# Death March Dance

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Death March Dance](../../../assets/icons/tensura/skill/death_march_dance.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:death_march_dance` |
| **Kind** | Projectile |
| **Activation** | Press, Hold |

</div>

> Gather your aura into a ring of devastating aura spheres that come crashing down.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 100 |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Acquisition checks: [Maximum Magic Bullet](maximum-magic-bullet.md)

## Related

- **Related skills:** [Maximum Magic Bullet](maximum-magic-bullet.md)
- **Summons / entities:** Aura Bullet
- **Referenced by:** [Maximum Magic Bullet](maximum-magic-bullet.md)

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `DeathMarchDance.auraCost` | 100 | Base Aura Cost to activate. |
| `DeathMarchDance.range` | 50 | The range in block of the bullets when homing. |
| `DeathMarchDance.maxMultiplier` | 5 | The Max Multiplier of the Attack Power. |
| `DeathMarchDance.maxMultiplierMastered` | 10 | The Max Multiplier of the Attack Power when Mastered. |
| `DeathMarchDance.holdTime` | 40 | The Time the user need to hold down to increase 1 Power level. |
| `DeathMarchDance.holdTimeMastered` | 20 | The Time the user need to hold down to increase 1 Power level with Mastery. |
| `DeathMarchDance.baseDamage` | 25 | The Base Damage of each Aura Bullet. |

## Tags

`tensura:skills/battlewill`
