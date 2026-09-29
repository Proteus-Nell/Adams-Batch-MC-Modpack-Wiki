# Magic Bullet

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Magic Bullet](../../../assets/icons/tensura/skill/magic_bullet.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:magic_bullet` |
| **Kind** | Projectile |
| **Activation** | Press, Hold |

</div>

> Gather your aura into a powerful blast.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 25 |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Does something when mastered

## Obtaining

- Sold by dwarf traders (high manual)
- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Related

- **Related skills:** [Maximum Magic Bullet](maximum-magic-bullet.md)
- **Referenced by:** [Maximum Magic Bullet](maximum-magic-bullet.md)

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `MagicBullet.auraCost` | 25 | Base Aura Cost to activate. |
| `MagicBullet.maxMultiplier` | 10 | The Max Multiplier of the Attack Power. |
| `MagicBullet.maxMultiplierMastered` | 20 | The Max Multiplier of the Attack Power when Mastered. |
| `MagicBullet.holdTime` | 30 | The Time the user need to hold down to increase 1 Power level. |
| `MagicBullet.holdTimeMastered` | 20 | The Time the user need to hold down to increase 1 Power level with Mastery. |
| `MagicBullet.baseDamage` | 10 | The Base Damage before Power Level calculation. |

## Tags

`tensura:skills/battlewill`, `tensura:skills/high_manual_dwarf_trade`
