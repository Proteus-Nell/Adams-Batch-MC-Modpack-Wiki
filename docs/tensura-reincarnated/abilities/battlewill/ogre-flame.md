# Ogre Flame

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Ogre Flame](../../../assets/icons/tensura/skill/ogre_flame.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:ogre_flame` |
| **Kind** | Projectile |
| **Activation** | Hold |

</div>

> Use your aura to create a pillar of fire.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 200 |

## How it works

- Charged or channelled by holding the skill key

## Obtaining

- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Related

- **Related skills:** [Flare Circle](../spiritual-magic/flare-circle.md)
- **Referenced by:** [Black Flame](../extra-skills/black-flame.md), [Oni Pyre](../../../tr-nightmares/abilities/battlewill/oni-pyre.md)

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `OgreFlame.auraCost` | 200 | Base Aura Cost to activate. |
| `OgreFlame.castTime` | 100 | The Cast Time in tick to activate. |
| `OgreFlame.maxTime` | 100 | The Max Time in tick for the Ogre Flame to stay after activation (doubled when Mastered). |
| `OgreFlame.maxDistance` | 15 | The Max Distance away from the user to spawn Ogre Flame. |
| `OgreFlame.flameDamage` | 50 | The Ogre Flame's damage each second. |
| `OgreFlame.flameRadius` | 4 | The Ogre Flame's radius. |

## Tags

`tensura:skills/battlewill`
