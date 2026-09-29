# Satella

<small>[TensuraMoreSkills](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Satella](../../../assets/icons/tensuramoreskills/skill/satella.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensuramoreskills:satella` |
| **Modes** | 2 |
| **Activation** | Toggle, Press |

</div>

> Aishteru.

## Modes

| # | Mode |
|---|---|
| 1 | Shadow Tendrils |
| 2 | Devouring Shadows |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | `(mode == 1 ? (Integer)cfg().devouringShadowsCost.get() : (Integer)cfg().shadowTendrilsCost.get()).intValue()` |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you are attacked
- Does something when first learned
- Does something when mastered

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| magiculeGain | gain | add |
| magiculeRegen | regen - 1 | multiply total |

## Related

- **Related skills:** [Shadow Motion](../../../tensura-reincarnated/abilities/extra-skills/shadow-motion.md), [Physical Attack Nullification](../../../tensura-reincarnated/abilities/resistance-skills/physical-attack-nullification.md), [Magic Darkness Transform](../../../tensura-reincarnated/abilities/extra-skills/magic-darkness-transform.md), [Darkness Attack Nullification](../../../tensura-reincarnated/abilities/resistance-skills/darkness-attack-nullification.md), [Authority of Greed](authority-of-greed.md), [True Authority of Greed](../ultimate-skills/true-authority-of-greed.md), [Witch of Envy, Satella](../ultimate-skills/witch-of-envy-satella.md), [Darkness](../../../tensura-reincarnated/abilities/spiritual-magic/darkness.md), [Shadow Bind](../../../tensura-reincarnated/abilities/spiritual-magic/shadow-bind.md), [Dark Cube](../../../tensura-reincarnated/abilities/spiritual-magic/dark-cube.md), [Darkness Cannon](../../../tensura-reincarnated/abilities/spiritual-magic/darkness-cannon.md), [True Darkness](../../../tensura-reincarnated/abilities/spiritual-magic/true-darkness.md)
- **Referenced by:** [Witch of Envy, Satella](../ultimate-skills/witch-of-envy-satella.md)

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- Satella copied %s
- Aishteru. The witch's love crawls through shadow and devours what touches it.

</details>
