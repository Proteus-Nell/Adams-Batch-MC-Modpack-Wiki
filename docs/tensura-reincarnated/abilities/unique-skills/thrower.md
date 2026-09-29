# Thrower

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Thrower](../../../assets/icons/tensura/skill/thrower.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:thrower` |
| **Acquisition cost (MP)** | 30,000 |
| **Activation** | Press |

</div>

> Use your skill and your precision to throw anything and deal massive damage. You can even shove air or push back your foes.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Innate to mobs: [Mark Lauren](../../mobs/mark-lauren.md)
- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.
- Listed in the `DemonicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Demonic skills registry names that can be created via Demon Essence consumption. Format: modid:skill_name

## Related

- **Related skills:** [Gravity Domination](../extra-skills/gravity-domination.md), [Gravity Manipulation](../extra-skills/gravity-manipulation.md)
- **Items:** [Severer Blade](../../items/weapons/severer-blade.md), [Kunai](../../items/weapons/kunai.md)
- **Summons / entities:** Web Bullet, Severer Blade, Spear, Thrown Item
- **Referenced by:** [Pride Manas](../../../tr-nightmares/abilities/ultimate-skills/pride-manas.md), [Melancholy](../../../tensura-mysticism/abilities/unique-skills/melancholy.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Thrower.mpAcquirement` | 30,000 | Magicule Acquirement Cost. |
| `Thrower.magiculeCost` | 50 | Magicule Cost to activate. |
| `Thrower.entityThrow` | 3 | The base entity throw power. |
| `Thrower.entityThrowManipulation` | 1 | The bonus entity throw power from Gravity Manipulation. |
| `Thrower.entityThrowDomination` | 2 | The bonus entity throw power from Gravity Domination. |
| `Thrower.airThrowDamage` | 30 | The base damage of thrown air. |
| `Thrower.airThrowDamageMastered` | 50 | The base damage of thrown air when mastered. |
| `Thrower.itemThrowDamage` | 50 | The base damage of thrown items. |
| `Thrower.itemThrowDamageMastered` | 100 | The base damage of thrown items when mastered. |
| `Thrower.itemThrowManipulation` | 2 | The bonus damage multiplier from Gravity Manipulation. |
| `Thrower.itemThrowDomination` | 3 | The bonus damage multiplier from Gravity Domination. |
| `Thrower.maxBreakableBlocks` | 10 | The maximum number of blocks that can be broken by throwing Mining Tools. |

## Tags

`tensura:skills/unique_skills`
