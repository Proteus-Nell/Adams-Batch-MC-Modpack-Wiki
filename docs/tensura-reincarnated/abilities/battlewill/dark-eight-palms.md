# Dark Eight Palms

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Dark Eight Palms](../../../assets/icons/tensura/skill/dark_eight_palms.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:dark_eight_palms` |
| **Kind** | Projectile |
| **Activation** | Press, Hold |

</div>

> Launch up to eight devastating aura blasts at foes.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 200 |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Intrinsic skill of: [Lost Fairy](../../../tr-nightmares/races/lost-fairy.md)
- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `DarkEightPalms.auraCost` | 200 | Base Aura Cost to activate. |
| `DarkEightPalms.maxMultiplier` | 8 | The Max Multiplier of the Attack Power. |
| `DarkEightPalms.holdTime` | 20 | The Time the user need to hold down to increase 1 Power level. |
| `DarkEightPalms.holdTimeMastered` | 10 | The Time the user need to hold down to increase 1 Power level with Mastery. |
| `DarkEightPalms.baseDamage` | 100 | The Base Damage of each Aura Bullet. |

## Tags

`tensura:skills/battlewill`
