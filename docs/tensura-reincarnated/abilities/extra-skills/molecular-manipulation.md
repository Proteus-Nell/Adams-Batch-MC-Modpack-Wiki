# Molecular Manipulation

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Molecular Manipulation](../../../assets/icons/tensura/skill/molecular_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:molecular_manipulation` |
| **Modes** | 2 |
| **Activation** | Press, Hold |

</div>

> Use your intricate knowledge and power over the building blocks of the world to obtain blocks and move entities.

## Modes

| # | Mode |
|---|---|
| 1 | Block |
| 2 | Entity |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active

## Related

- **Related skills:** [Gravity Domination](gravity-domination.md), [Gravity Manipulation](gravity-manipulation.md)
- **Referenced by:** [Black Flame](black-flame.md), [Black Lightning](black-lightning.md), [Mana Manipulation](mana-manipulation.md), [Spatial Vault](../../../tr-nightmares/abilities/aspectual-magic/spatial-vault.md), [Melancholy](../../../tensura-mysticism/abilities/unique-skills/melancholy.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `MolecularManipulation.masteredManipulationAcquirement` | 2 | The number of mastered elemental manipulation skills needed to learn Molecular Manipulation. |
| `MolecularManipulation.magiculeCost` | 5 | Base Magicule Cost to activate. |
| `MolecularManipulation.maxRange` | 30 | The maximum range in block for activation. |
| `MolecularManipulation.maxSize` | 1 | The maximum size in block of a target for the Entity Mode. |
| `MolecularManipulation.maxSizeMastered` | 2 | The maximum size in block of a target for the Entity Mode when mastered. |
| `MolecularManipulation.maxSizeManipulation` | 6 | The bonus maximum size in block of a target for the Entity Mode with Gravity Manipulation. |
| `MolecularManipulation.maxSizeDomination` | 10 | The bonus maximum size in block of a target for the Entity Mode with Gravity Domination. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/extra_skills`
