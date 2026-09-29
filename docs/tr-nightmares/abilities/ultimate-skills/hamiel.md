# ｢ Hamiel, King of Splendour ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Hamiel, King of Splendour ｣](../../../assets/icons/trnightmare/skill/hamiel.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:hamiel` |
| **Acquisition cost (MP)** | 900,000 |
| **Max mastery** | 5,000 |
| **Activation** | Toggle |

</div>

> Your journey for glory is over... You have succeeded. While all that you hurt, only receives half, so shall you.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage
- Triggers when a mob targets you
- Triggers when an effect is applied to you

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| degrade | 1 | add |
| melee | 75 | add |
| projectile | 100 | add |
| dodgeNegate | 90 | add |
| learning | 8 | add |
| mastery | 8 | add |
| critical | 100 | add |

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.

## Related

- **Effects:** [Glorious Regen](../../effects/glorious-regen.md), [Holy Damage](../../../tensura-reincarnated/effects/holy-damage.md), [Infection](../../../tensura-reincarnated/effects/infection.md), [Infinite Imprisonment](../../../tensura-reincarnated/effects/infinite-imprisonment.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Hamiel.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Hamiel.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Hamiel.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Hamiel.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Hamiel.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Hamiel.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Hamiel.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Hamiel.mpAcquirement` | 900,000 | Magicule Acquirement Cost. |
| `Hamiel.regenCostMultiplier` | 0.33 | Magicule Cost multiplier for Infinite Regeneration. |
| `Hamiel.swapMultiplier` | 2 | Damage Multiplier for offense defense swap. |
| `Hamiel.critChance` | 100 | Critical Attack chance. |
| `Hamiel.dodgeChanceIgnore` | 90 | Dodge ignoring chance. |
| `Hamiel.dodgeChance` | 75 | Dodge chance. |
| `Hamiel.dodgeChanceProjectile` | 100 | Projectile dodge chance on mastery. |
| `Hamiel.resistanceDegradation` | 1 | Level of resistance degradation. |
| `Hamiel.presenceSense` | 3 | Level of Presence Sense. |
| `Hamiel.learningPoint` | 8 | Learning point boost for skills |
| `Hamiel.masteryPoint` | 8 | Mastery point gain for Skills |
| `Hamiel.enableUltimateEvolution` | true | Whether hamiel can be obtained naturally |
| `Hamiel.hamielRaids` | 12 | Raids required to obtain Hamiel. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

## Tags

`tensura:skills/ultimate_skills`
