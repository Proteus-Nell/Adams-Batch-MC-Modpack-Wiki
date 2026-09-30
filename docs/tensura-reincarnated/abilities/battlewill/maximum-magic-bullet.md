# Maximum Magic Bullet

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Maximum Magic Bullet](../../../assets/icons/tensura/skill/maximum_magic_bullet.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:maximum_magic_bullet` |
| **Kind** | Projectile |
| **Activation** | Press, Hold |

</div>

> Gather your aura into a gargantuan blast obliterating all who dare oppose you.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 100 |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Does something when mastered

## Obtaining

- Acquisition checks: [Magic Bullet](magic-bullet.md)

## Related

- **Related skills:** [Magic Bullet](magic-bullet.md), [Death March Dance](death-march-dance.md)
- **Summons / entities:** Aura Bullet
- **Referenced by:** [Death March Dance](death-march-dance.md), [Magic Bullet](magic-bullet.md)

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `MaximumMagicBullet.auraCost` | 100 | Base Aura Cost to activate. |
| `MaximumMagicBullet.maxMultiplier` | 15 | The Max Multiplier of the Attack Power. |
| `MaximumMagicBullet.maxMultiplierMastered` | 30 | The Max Multiplier of the Attack Power when Mastered. |
| `MaximumMagicBullet.holdTime` | 30 | The Time the user need to hold down to increase 1 Power level. |
| `MaximumMagicBullet.holdTimeMastered` | 20 | The Time the user need to hold down to increase 1 Power level with Mastery. |
| `MaximumMagicBullet.baseDamage` | 25 | The Base Damage before Power Level calculation. |

## Tags

`tensura:skills/battlewill`
