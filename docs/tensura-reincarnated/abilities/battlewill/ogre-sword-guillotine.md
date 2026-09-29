# Ogre-sword Guillotine

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Ogre-sword Guillotine](../../../assets/icons/tensura/skill/ogre_sword_guillotine.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:ogre_sword_guillotine` |
| **Kind** | Melee |
| **Activation** | Press |

</div>

> Coat your weapon in aura enhancing its blows.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 200 |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Does something when mastered

## Obtaining

- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Related

- **Related skills:** [Ogre-sword Cannon](ogre-sword-cannon.md)
- **Effects:** [Ogre Guillotine](../../effects/ogre-guillotine.md)
- **Referenced by:** [Ogre-sword Cannon](ogre-sword-cannon.md), [Phainon, The Deliverer](../../../tensura-more-skills/abilities/ultimate-skills/phainon.md)

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `OgreSwordGuillotine.auraCost` | 200 | Aura Cost to activate. |
| `OgreSwordGuillotine.effectTime` | 300 | How long in tick that Ogre-Sword Guillotine will stay on user after activated. |
| `OgreSwordGuillotine.effectTimeMastered` | 600 | How long in tick that Ogre-Sword Guillotine will stay on user after activated while mastered. |
| `OgreSwordGuillotine.attackMultiplier` | 1.5 | The multiplier of Attack Damage that the user gains when activated. |
| `OgreSwordGuillotine.reachMultiplier` | 1.5 | The multiplier of Attack Reach that the user gains when activated. |
| `OgreSwordGuillotine.attackSpeedMultiplier` | 0.8 | The multiplier of Attack Speed that the user gains when activated. |

## Tags

`tensura:skills/battlewill`
