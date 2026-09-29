# ｢ Haniel, Lord of Glory ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Haniel, Lord of Glory ｣](../../../assets/icons/trnightmare/skill/haniel.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:haniel` |
| **Modes** | 1 |
| **Acquisition cost (MP)** | 750,000 |
| **Max mastery** | 5,000 |
| **Activation** | Toggle |

</div>

> The Great Archangel of health blesses you with energy, you may not be able to fight, but you shall take no damage regardless.

## Modes

| # | Mode |
|---|---|
| 1 | Accord |

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage
- Triggers when a mob targets you

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| degrade | 1 | add |
| melee | 60 | add |
| projectile | 100 mastered, 60 otherwise | add |
| dodgeNegate | 80 | add |
| learning | 6 | add |
| mastery | 6 | add |
| critical | 80 | add |

## Obtaining

- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Acquisition checks: [Glorious](../unique-skills/glorious.md), [｢ Haniel, Lord of Glory ｣](haniel.md)
- In-game message: *Praise be, the graciousness of the world has granted unto you a powerful and holy blessing, Glorious is evolving into Haniel. To what extent will you shine now?*

## Related

- **Related skills:** [Glorious](../unique-skills/glorious.md)
- **Effects:** [Glorious Regen](../../effects/glorious-regen.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Haniel.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Haniel.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Haniel.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Haniel.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Haniel.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Haniel.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Haniel.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Haniel.enableUltimateEvolution` | true | Whether Glorious → Haniel evolution is allowed. |
| `Haniel.mpAcquirement` | 750,000 | Magicule Acquirement Cost. |
| `Haniel.regenCostMultiplier` | 0.5 | Magicule Cost multiplier for Infinite Regeneration. |
| `Haniel.swapMultiplier` | 0.5 | Damage Multiplier for offense defense swap. |
| `Haniel.critChance` | 80 | Critical Attack chance. |
| `Haniel.dodgeChanceIgnore` | 80 | Dodge ignoring chance. |
| `Haniel.dodgeChance` | 60 | Dodge chance. |
| `Haniel.dodgeChanceProjectile` | 100 | Projectile dodge chance on mastery. |
| `Haniel.resistanceDegradation` | 1 | Level of resistance degradation. |
| `Haniel.presenceSense` | 3 | Level of Presence Sense. |
| `Haniel.learningPoint` | 6 | Learning point boost for skills |
| `Haniel.masteryPoint` | 6 | Mastery point gain for Skills |
| `Haniel.hanielRaids` | 6 | Raids required to obtain Haniel. |
| `Haniel.hanielArmor` | 100 | Armor attribute required to obtain Haniel. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

## Tags

`tensura:skills/ultimate_skills`
